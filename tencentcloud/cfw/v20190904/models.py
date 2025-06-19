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


class AcListsData(AbstractModel):
    """访问控制列表对象

    """

    def __init__(self):
        r"""
        :param _Id: 规则id
        :type Id: int
        :param _SourceIp: 访问源
        :type SourceIp: str
        :param _TargetIp: 访问目的
        :type TargetIp: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Port: 端口
        :type Port: str
        :param _Strategy: 策略
        :type Strategy: int
        :param _Detail: 描述
        :type Detail: str
        :param _Count: 命中次数
        :type Count: int
        :param _OrderIndex: 执行顺序
        :type OrderIndex: int
        :param _LogId: 告警规则id
        :type LogId: str
        :param _Status: 规则开关状态 1打开 0关闭
        :type Status: int
        :param _SrcType: 规则源类型
        :type SrcType: int
        :param _DstType: 规则目的类型
        :type DstType: int
        :param _Uuid: 规则唯一ID
        :type Uuid: str
        :param _Invalid: 规则有效性
1 有效
0 无效
        :type Invalid: int
        :param _IsRegion: 是否地域规则
        :type IsRegion: int
        :param _CloudCode: 云厂商代码
        :type CloudCode: str
        :param _AutoTask: 自动化助手信息
        :type AutoTask: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _RegionCode: 地域码信息
        :type RegionCode: str
        :param _Country: 国家代码
        :type Country: int
        :param _City: 城市代码
        :type City: int
        :param _RegName1: 国家名称
        :type RegName1: str
        :param _RegName2: 城市名称
        :type RegName2: str
        """
        self._Id = None
        self._SourceIp = None
        self._TargetIp = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Detail = None
        self._Count = None
        self._OrderIndex = None
        self._LogId = None
        self._Status = None
        self._SrcType = None
        self._DstType = None
        self._Uuid = None
        self._Invalid = None
        self._IsRegion = None
        self._CloudCode = None
        self._AutoTask = None
        self._InstanceName = None
        self._RegionCode = None
        self._Country = None
        self._City = None
        self._RegName1 = None
        self._RegName2 = None

    @property
    def Id(self):
        """规则id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SourceIp(self):
        """访问源
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def TargetIp(self):
        """访问目的
        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

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
    def Port(self):
        """端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        """策略
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Detail(self):
        """描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Count(self):
        """命中次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def OrderIndex(self):
        """执行顺序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def LogId(self):
        """告警规则id
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def Status(self):
        """规则开关状态 1打开 0关闭
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SrcType(self):
        """规则源类型
        :rtype: int
        """
        return self._SrcType

    @SrcType.setter
    def SrcType(self, SrcType):
        self._SrcType = SrcType

    @property
    def DstType(self):
        """规则目的类型
        :rtype: int
        """
        return self._DstType

    @DstType.setter
    def DstType(self, DstType):
        self._DstType = DstType

    @property
    def Uuid(self):
        """规则唯一ID
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Invalid(self):
        """规则有效性
1 有效
0 无效
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid

    @property
    def IsRegion(self):
        """是否地域规则
        :rtype: int
        """
        return self._IsRegion

    @IsRegion.setter
    def IsRegion(self, IsRegion):
        self._IsRegion = IsRegion

    @property
    def CloudCode(self):
        """云厂商代码
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode

    @property
    def AutoTask(self):
        """自动化助手信息
        :rtype: str
        """
        return self._AutoTask

    @AutoTask.setter
    def AutoTask(self, AutoTask):
        self._AutoTask = AutoTask

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def RegionCode(self):
        """地域码信息
        :rtype: str
        """
        return self._RegionCode

    @RegionCode.setter
    def RegionCode(self, RegionCode):
        self._RegionCode = RegionCode

    @property
    def Country(self):
        """国家代码
        :rtype: int
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def City(self):
        """城市代码
        :rtype: int
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def RegName1(self):
        """国家名称
        :rtype: str
        """
        return self._RegName1

    @RegName1.setter
    def RegName1(self, RegName1):
        self._RegName1 = RegName1

    @property
    def RegName2(self):
        """城市名称
        :rtype: str
        """
        return self._RegName2

    @RegName2.setter
    def RegName2(self, RegName2):
        self._RegName2 = RegName2


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SourceIp = params.get("SourceIp")
        self._TargetIp = params.get("TargetIp")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Detail = params.get("Detail")
        self._Count = params.get("Count")
        self._OrderIndex = params.get("OrderIndex")
        self._LogId = params.get("LogId")
        self._Status = params.get("Status")
        self._SrcType = params.get("SrcType")
        self._DstType = params.get("DstType")
        self._Uuid = params.get("Uuid")
        self._Invalid = params.get("Invalid")
        self._IsRegion = params.get("IsRegion")
        self._CloudCode = params.get("CloudCode")
        self._AutoTask = params.get("AutoTask")
        self._InstanceName = params.get("InstanceName")
        self._RegionCode = params.get("RegionCode")
        self._Country = params.get("Country")
        self._City = params.get("City")
        self._RegName1 = params.get("RegName1")
        self._RegName2 = params.get("RegName2")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAclRuleRequest(AbstractModel):
    """AddAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 需要添加的访问控制规则列表
        :type Rules: list of CreateRuleItem
        :param _From: 添加规则的来源，一般不需要使用，值insert_rule 表示插入指定位置的规则；值batch_import 表示批量导入规则；为空时表示添加规则
        :type From: str
        """
        self._Rules = None
        self._From = None

    @property
    def Rules(self):
        """需要添加的访问控制规则列表
        :rtype: list of CreateRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def From(self):
        """添加规则的来源，一般不需要使用，值insert_rule 表示插入指定位置的规则；值batch_import 表示批量导入规则；为空时表示添加规则
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CreateRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAclRuleResponse(AbstractModel):
    """AddAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 创建成功后返回新策略ID列表
        :type RuleUuid: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """创建成功后返回新策略ID列表
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

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
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class AddEnterpriseSecurityGroupRulesRequest(AbstractModel):
    """AddEnterpriseSecurityGroupRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建规则数据
        :type Data: list of SecurityGroupRule
        :param _Type: 添加类型，0：添加到最后，1：添加到最前；2：中间插入；默认0添加到最后
        :type Type: int
        :param _ClientToken: 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。
        :type ClientToken: str
        :param _IsDelay: （IsDelay为老版参数，新版无需输入）是否延迟下发，1则延迟下发，否则立即下发
        :type IsDelay: int
        :param _From: 来源 默认空 覆盖导入是 batch_import_cover
        :type From: str
        :param _IsUseId: 是否复用rule id，1为是，默认不需要
        :type IsUseId: int
        """
        self._Data = None
        self._Type = None
        self._ClientToken = None
        self._IsDelay = None
        self._From = None
        self._IsUseId = None

    @property
    def Data(self):
        """创建规则数据
        :rtype: list of SecurityGroupRule
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """添加类型，0：添加到最后，1：添加到最前；2：中间插入；默认0添加到最后
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClientToken(self):
        """保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def IsDelay(self):
        """（IsDelay为老版参数，新版无需输入）是否延迟下发，1则延迟下发，否则立即下发
        :rtype: int
        """
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

    @property
    def From(self):
        """来源 默认空 覆盖导入是 batch_import_cover
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def IsUseId(self):
        """是否复用rule id，1为是，默认不需要
        :rtype: int
        """
        return self._IsUseId

    @IsUseId.setter
    def IsUseId(self, IsUseId):
        self._IsUseId = IsUseId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._ClientToken = params.get("ClientToken")
        self._IsDelay = params.get("IsDelay")
        self._From = params.get("From")
        self._IsUseId = params.get("IsUseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEnterpriseSecurityGroupRulesResponse(AbstractModel):
    """AddEnterpriseSecurityGroupRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0：添加成功，非0：添加失败
        :type Status: int
        :param _Rules: 添加成功的规则详情
        :type Rules: list of SecurityGroupSimplifyRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Rules = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0：添加成功，非0：添加失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Rules(self):
        """添加成功的规则详情
        :rtype: list of SecurityGroupSimplifyRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

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
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SecurityGroupSimplifyRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RequestId = params.get("RequestId")


class AddNatAcRuleRequest(AbstractModel):
    """AddNatAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 需要添加的nat访问控制规则列表
        :type Rules: list of CreateNatRuleItem
        :param _From: 添加规则的来源，一般不需要使用，值insert_rule 表示插入指定位置的规则；值batch_import 表示批量导入规则；为空时表示添加规则
        :type From: str
        """
        self._Rules = None
        self._From = None

    @property
    def Rules(self):
        """需要添加的nat访问控制规则列表
        :rtype: list of CreateNatRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def From(self):
        """添加规则的来源，一般不需要使用，值insert_rule 表示插入指定位置的规则；值batch_import 表示批量导入规则；为空时表示添加规则
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CreateNatRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNatAcRuleResponse(AbstractModel):
    """AddNatAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 创建成功后返回新策略ID列表
        :type RuleUuid: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """创建成功后返回新策略ID列表
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

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
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class AddVpcAcRuleRequest(AbstractModel):
    """AddVpcAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 需要添加的vpc内网间规则列表
        :type Rules: list of VpcRuleItem
        :param _From: 添加规则的来源，一般不需要使用，值insert_rule 表示插入指定位置的规则；值batch_import 表示批量导入规则；为空时表示添加规则
        :type From: str
        """
        self._Rules = None
        self._From = None

    @property
    def Rules(self):
        """需要添加的vpc内网间规则列表
        :rtype: list of VpcRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def From(self):
        """添加规则的来源，一般不需要使用，值insert_rule 表示插入指定位置的规则；值batch_import 表示批量导入规则；为空时表示添加规则
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = VpcRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddVpcAcRuleResponse(AbstractModel):
    """AddVpcAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuids: 创建成功后返回新策略ID列表
        :type RuleUuids: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuids = None
        self._RequestId = None

    @property
    def RuleUuids(self):
        """创建成功后返回新策略ID列表
        :rtype: list of int
        """
        return self._RuleUuids

    @RuleUuids.setter
    def RuleUuids(self, RuleUuids):
        self._RuleUuids = RuleUuids

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
        self._RuleUuids = params.get("RuleUuids")
        self._RequestId = params.get("RequestId")


class AssetZone(AbstractModel):
    """AssetZone

    """

    def __init__(self):
        r"""
        :param _Zone: 地域
        :type Zone: str
        :param _ZoneEng: 地域英文
        :type ZoneEng: str
        """
        self._Zone = None
        self._ZoneEng = None

    @property
    def Zone(self):
        """地域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneEng(self):
        """地域英文
        :rtype: str
        """
        return self._ZoneEng

    @ZoneEng.setter
    def ZoneEng(self, ZoneEng):
        self._ZoneEng = ZoneEng


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneEng = params.get("ZoneEng")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociatedInstanceInfo(AbstractModel):
    """企业安全组关联实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Type: 实例类型，3是cvm实例,4是clb实例,5是eni实例,6是云数据库
        :type Type: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _VpcName: 私有网络名称
        :type VpcName: str
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _Ip: 内网IP
        :type Ip: str
        :param _SecurityGroupCount: 关联安全组数量
        :type SecurityGroupCount: int
        :param _SecurityGroupRuleCount: 关联安全组规则数量
        :type SecurityGroupRuleCount: int
        :param _CdbId: 关联数据库代理Id
        :type CdbId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Type = None
        self._VpcId = None
        self._VpcName = None
        self._PublicIp = None
        self._Ip = None
        self._SecurityGroupCount = None
        self._SecurityGroupRuleCount = None
        self._CdbId = None

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
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Type(self):
        """实例类型，3是cvm实例,4是clb实例,5是eni实例,6是云数据库
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VpcId(self):
        """私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        """私有网络名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

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
    def Ip(self):
        """内网IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def SecurityGroupCount(self):
        """关联安全组数量
        :rtype: int
        """
        return self._SecurityGroupCount

    @SecurityGroupCount.setter
    def SecurityGroupCount(self, SecurityGroupCount):
        self._SecurityGroupCount = SecurityGroupCount

    @property
    def SecurityGroupRuleCount(self):
        """关联安全组规则数量
        :rtype: int
        """
        return self._SecurityGroupRuleCount

    @SecurityGroupRuleCount.setter
    def SecurityGroupRuleCount(self, SecurityGroupRuleCount):
        self._SecurityGroupRuleCount = SecurityGroupRuleCount

    @property
    def CdbId(self):
        """关联数据库代理Id
        :rtype: str
        """
        return self._CdbId

    @CdbId.setter
    def CdbId(self, CdbId):
        self._CdbId = CdbId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Type = params.get("Type")
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._PublicIp = params.get("PublicIp")
        self._Ip = params.get("Ip")
        self._SecurityGroupCount = params.get("SecurityGroupCount")
        self._SecurityGroupRuleCount = params.get("SecurityGroupRuleCount")
        self._CdbId = params.get("CdbId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BanAndAllowRule(AbstractModel):
    """封禁列表和放通列表结构体

    """

    def __init__(self):
        r"""
        :param _Comment: 规则评论
        :type Comment: str
        :param _CustomRule: 自定义白名单规则
        :type CustomRule: :class:`tencentcloud.cfw.v20190904.models.CustomWhiteRule`
        :param _DirectionList: 0互联网出站 1互联网入站 5内网访问源 6内网访问目的
        :type DirectionList: str
        :param _EndTime: 规则截止时间
        :type EndTime: str
        :param _FwType: 放通的引擎: 1针对互联网边界 2针对nat防火墙 4针对vpc防火墙
        :type FwType: int
        :param _Ioc: 封禁和放通对象
        :type Ioc: str
        """
        self._Comment = None
        self._CustomRule = None
        self._DirectionList = None
        self._EndTime = None
        self._FwType = None
        self._Ioc = None

    @property
    def Comment(self):
        """规则评论
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CustomRule(self):
        """自定义白名单规则
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CustomWhiteRule`
        """
        return self._CustomRule

    @CustomRule.setter
    def CustomRule(self, CustomRule):
        self._CustomRule = CustomRule

    @property
    def DirectionList(self):
        """0互联网出站 1互联网入站 5内网访问源 6内网访问目的
        :rtype: str
        """
        return self._DirectionList

    @DirectionList.setter
    def DirectionList(self, DirectionList):
        self._DirectionList = DirectionList

    @property
    def EndTime(self):
        """规则截止时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FwType(self):
        """放通的引擎: 1针对互联网边界 2针对nat防火墙 4针对vpc防火墙
        :rtype: int
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Ioc(self):
        """封禁和放通对象
        :rtype: str
        """
        return self._Ioc

    @Ioc.setter
    def Ioc(self, Ioc):
        self._Ioc = Ioc


    def _deserialize(self, params):
        self._Comment = params.get("Comment")
        if params.get("CustomRule") is not None:
            self._CustomRule = CustomWhiteRule()
            self._CustomRule._deserialize(params.get("CustomRule"))
        self._DirectionList = params.get("DirectionList")
        self._EndTime = params.get("EndTime")
        self._FwType = params.get("FwType")
        self._Ioc = params.get("Ioc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BanAndAllowRuleDel(AbstractModel):
    """封禁列表和放通列表结构体

    """

    def __init__(self):
        r"""
        :param _Ioc: 封禁和放通对象
        :type Ioc: str
        :param _DirectionList: 0互联网出站 1互联网入站 5内网访问源 6内网访问目的 （DeleteBlockIgnoreRuleNew接口，该字段无效）
        :type DirectionList: str
        :param _RuleType: 规则类型
RuleType: 1黑名单 2外部IP 3域名 4情报 5资产 6自定义规则  7入侵防御规则
        :type RuleType: int
        """
        self._Ioc = None
        self._DirectionList = None
        self._RuleType = None

    @property
    def Ioc(self):
        """封禁和放通对象
        :rtype: str
        """
        return self._Ioc

    @Ioc.setter
    def Ioc(self, Ioc):
        self._Ioc = Ioc

    @property
    def DirectionList(self):
        """0互联网出站 1互联网入站 5内网访问源 6内网访问目的 （DeleteBlockIgnoreRuleNew接口，该字段无效）
        :rtype: str
        """
        return self._DirectionList

    @DirectionList.setter
    def DirectionList(self, DirectionList):
        self._DirectionList = DirectionList

    @property
    def RuleType(self):
        """规则类型
RuleType: 1黑名单 2外部IP 3域名 4情报 5资产 6自定义规则  7入侵防御规则
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType


    def _deserialize(self, params):
        self._Ioc = params.get("Ioc")
        self._DirectionList = params.get("DirectionList")
        self._RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BetaInfoByACL(AbstractModel):
    """规则关联的beta任务

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _LastTime: 上次执行时间
        :type LastTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._LastTime = None

    @property
    def TaskId(self):
        """任务id
        :rtype: int
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
    def LastTime(self):
        """上次执行时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._LastTime = params.get("LastTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlockIgnoreRule(AbstractModel):
    """入侵防御放通封禁规则

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型，取值：1 封禁，2外部IP，3域名，4情报，5assets，6自定义策略，7入侵防御规则id （2-7属于白名单类型）
        :type RuleType: int
        :param _Ioc: 规则ip或白名单内容
        :type Ioc: str
        :param _IocName: 资产实例名称、自定义策略名称等
        :type IocName: str
        :param _IocInfo: 白名单信息
        :type IocInfo: str
        :param _Domain: 域名
        :type Domain: str
        :param _IP: IP
        :type IP: str
        :param _Level: 危险等级
        :type Level: str
        :param _EventName: 来源事件名称
        :type EventName: str
        :param _Direction: 方向：1入站，0出站
        :type Direction: int
        :param _DirectionList: 所有方向聚合成字符串
        :type DirectionList: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Address: 地理位置
        :type Address: str
        :param _Action: 规则类型：1封禁，2放通
        :type Action: int
        :param _StartTime: 规则生效开始时间
        :type StartTime: str
        :param _EndTime: 规则生效结束时间
        :type EndTime: str
        :param _IgnoreReason: 忽略原因
        :type IgnoreReason: str
        :param _Source: 安全事件来源
        :type Source: str
        :param _UniqueId: 规则id
        :type UniqueId: str
        :param _MatchTimes: 规则命中次数
        :type MatchTimes: int
        :param _Country: 国家
        :type Country: str
        :param _Comment: 备注
        :type Comment: str
        :param _LastHitTime: 上次命中时间
        :type LastHitTime: str
        :param _CustomRule: 自定义规则细节
        :type CustomRule: :class:`tencentcloud.cfw.v20190904.models.CustomWhiteRule`
        :param _FwType: 1 border 2 nat 4 vpc 8 border-serial
        :type FwType: int
        """
        self._RuleType = None
        self._Ioc = None
        self._IocName = None
        self._IocInfo = None
        self._Domain = None
        self._IP = None
        self._Level = None
        self._EventName = None
        self._Direction = None
        self._DirectionList = None
        self._Protocol = None
        self._Address = None
        self._Action = None
        self._StartTime = None
        self._EndTime = None
        self._IgnoreReason = None
        self._Source = None
        self._UniqueId = None
        self._MatchTimes = None
        self._Country = None
        self._Comment = None
        self._LastHitTime = None
        self._CustomRule = None
        self._FwType = None

    @property
    def RuleType(self):
        """规则类型，取值：1 封禁，2外部IP，3域名，4情报，5assets，6自定义策略，7入侵防御规则id （2-7属于白名单类型）
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def Ioc(self):
        """规则ip或白名单内容
        :rtype: str
        """
        return self._Ioc

    @Ioc.setter
    def Ioc(self, Ioc):
        self._Ioc = Ioc

    @property
    def IocName(self):
        """资产实例名称、自定义策略名称等
        :rtype: str
        """
        return self._IocName

    @IocName.setter
    def IocName(self, IocName):
        self._IocName = IocName

    @property
    def IocInfo(self):
        """白名单信息
        :rtype: str
        """
        return self._IocInfo

    @IocInfo.setter
    def IocInfo(self, IocInfo):
        self._IocInfo = IocInfo

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def IP(self):
        """IP
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Level(self):
        """危险等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def EventName(self):
        """来源事件名称
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def Direction(self):
        """方向：1入站，0出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def DirectionList(self):
        """所有方向聚合成字符串
        :rtype: str
        """
        return self._DirectionList

    @DirectionList.setter
    def DirectionList(self, DirectionList):
        self._DirectionList = DirectionList

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
    def Address(self):
        """地理位置
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Action(self):
        """规则类型：1封禁，2放通
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StartTime(self):
        """规则生效开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """规则生效结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IgnoreReason(self):
        """忽略原因
        :rtype: str
        """
        return self._IgnoreReason

    @IgnoreReason.setter
    def IgnoreReason(self, IgnoreReason):
        self._IgnoreReason = IgnoreReason

    @property
    def Source(self):
        """安全事件来源
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def UniqueId(self):
        """规则id
        :rtype: str
        """
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def MatchTimes(self):
        """规则命中次数
        :rtype: int
        """
        return self._MatchTimes

    @MatchTimes.setter
    def MatchTimes(self, MatchTimes):
        self._MatchTimes = MatchTimes

    @property
    def Country(self):
        """国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Comment(self):
        """备注
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def LastHitTime(self):
        """上次命中时间
        :rtype: str
        """
        return self._LastHitTime

    @LastHitTime.setter
    def LastHitTime(self, LastHitTime):
        self._LastHitTime = LastHitTime

    @property
    def CustomRule(self):
        """自定义规则细节
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CustomWhiteRule`
        """
        return self._CustomRule

    @CustomRule.setter
    def CustomRule(self, CustomRule):
        self._CustomRule = CustomRule

    @property
    def FwType(self):
        """1 border 2 nat 4 vpc 8 border-serial
        :rtype: int
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._Ioc = params.get("Ioc")
        self._IocName = params.get("IocName")
        self._IocInfo = params.get("IocInfo")
        self._Domain = params.get("Domain")
        self._IP = params.get("IP")
        self._Level = params.get("Level")
        self._EventName = params.get("EventName")
        self._Direction = params.get("Direction")
        self._DirectionList = params.get("DirectionList")
        self._Protocol = params.get("Protocol")
        self._Address = params.get("Address")
        self._Action = params.get("Action")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IgnoreReason = params.get("IgnoreReason")
        self._Source = params.get("Source")
        self._UniqueId = params.get("UniqueId")
        self._MatchTimes = params.get("MatchTimes")
        self._Country = params.get("Country")
        self._Comment = params.get("Comment")
        self._LastHitTime = params.get("LastHitTime")
        if params.get("CustomRule") is not None:
            self._CustomRule = CustomWhiteRule()
            self._CustomRule._deserialize(params.get("CustomRule"))
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfwInsStatus(AbstractModel):
    """防火墙实例运行状态

    """

    def __init__(self):
        r"""
        :param _CfwInsId: 防火墙实例id
        :type CfwInsId: str
        :param _FwType: 防火墙类型，nat：nat防火墙；ew：vpc间防火墙
        :type FwType: str
        :param _Region: 实例所属地域
        :type Region: str
        :param _Status: 实例运行状态，Running：正常运行；BypassAutoFix：bypass修复；Updating：升级中；Expand：扩容中；BypassManual：手动触发bypass中；BypassAuto：自动触发bypass中
        :type Status: str
        :param _EventTime: 事件时间
        :type EventTime: str
        :param _RecoverTime: 恢复时间
        :type RecoverTime: str
        :param _CfwInsName: 实例名称
        :type CfwInsName: str
        :param _TrafficMode: Normal: 正常模式
OnlyRoute: 透明模式
        :type TrafficMode: str
        """
        self._CfwInsId = None
        self._FwType = None
        self._Region = None
        self._Status = None
        self._EventTime = None
        self._RecoverTime = None
        self._CfwInsName = None
        self._TrafficMode = None

    @property
    def CfwInsId(self):
        """防火墙实例id
        :rtype: str
        """
        return self._CfwInsId

    @CfwInsId.setter
    def CfwInsId(self, CfwInsId):
        self._CfwInsId = CfwInsId

    @property
    def FwType(self):
        """防火墙类型，nat：nat防火墙；ew：vpc间防火墙
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Region(self):
        """实例所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        """实例运行状态，Running：正常运行；BypassAutoFix：bypass修复；Updating：升级中；Expand：扩容中；BypassManual：手动触发bypass中；BypassAuto：自动触发bypass中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EventTime(self):
        """事件时间
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def RecoverTime(self):
        """恢复时间
        :rtype: str
        """
        return self._RecoverTime

    @RecoverTime.setter
    def RecoverTime(self, RecoverTime):
        self._RecoverTime = RecoverTime

    @property
    def CfwInsName(self):
        """实例名称
        :rtype: str
        """
        return self._CfwInsName

    @CfwInsName.setter
    def CfwInsName(self, CfwInsName):
        self._CfwInsName = CfwInsName

    @property
    def TrafficMode(self):
        """Normal: 正常模式
OnlyRoute: 透明模式
        :rtype: str
        """
        return self._TrafficMode

    @TrafficMode.setter
    def TrafficMode(self, TrafficMode):
        self._TrafficMode = TrafficMode


    def _deserialize(self, params):
        self._CfwInsId = params.get("CfwInsId")
        self._FwType = params.get("FwType")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._EventTime = params.get("EventTime")
        self._RecoverTime = params.get("RecoverTime")
        self._CfwInsName = params.get("CfwInsName")
        self._TrafficMode = params.get("TrafficMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfwNatDnatRule(AbstractModel):
    """NAT防火墙Dnat规则

    """

    def __init__(self):
        r"""
        :param _IpProtocol: 网络协议，可选值：TCP、UDP。
        :type IpProtocol: str
        :param _PublicIpAddress: 弹性IP。
        :type PublicIpAddress: str
        :param _PublicPort: 公网端口。
        :type PublicPort: int
        :param _PrivateIpAddress: 内网地址。
        :type PrivateIpAddress: str
        :param _PrivatePort: 内网端口。
        :type PrivatePort: int
        :param _Description: NAT防火墙转发规则描述。
        :type Description: str
        """
        self._IpProtocol = None
        self._PublicIpAddress = None
        self._PublicPort = None
        self._PrivateIpAddress = None
        self._PrivatePort = None
        self._Description = None

    @property
    def IpProtocol(self):
        """网络协议，可选值：TCP、UDP。
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PublicIpAddress(self):
        """弹性IP。
        :rtype: str
        """
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def PublicPort(self):
        """公网端口。
        :rtype: int
        """
        return self._PublicPort

    @PublicPort.setter
    def PublicPort(self, PublicPort):
        self._PublicPort = PublicPort

    @property
    def PrivateIpAddress(self):
        """内网地址。
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress

    @property
    def PrivatePort(self):
        """内网端口。
        :rtype: int
        """
        return self._PrivatePort

    @PrivatePort.setter
    def PrivatePort(self, PrivatePort):
        self._PrivatePort = PrivatePort

    @property
    def Description(self):
        """NAT防火墙转发规则描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IpProtocol = params.get("IpProtocol")
        self._PublicIpAddress = params.get("PublicIpAddress")
        self._PublicPort = params.get("PublicPort")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        self._PrivatePort = params.get("PrivatePort")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Column(AbstractModel):
    """日志分析的列属性

    """

    def __init__(self):
        r"""
        :param _Name: 列的名字
        :type Name: str
        :param _Type: 列的属性
        :type Type: str
        """
        self._Name = None
        self._Type = None

    @property
    def Name(self):
        """列的名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """列的属性
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonFilter(AbstractModel):
    """通用的列表检索过滤选项

    """

    def __init__(self):
        r"""
        :param _Name: 检索的键值
        :type Name: str
        :param _OperatorType: 枚举类型，代表Name与Values之间的匹配关系
enum FilterOperatorType {
    //等于
    FILTER_OPERATOR_TYPE_EQUAL = 1;
    //大于
    FILTER_OPERATOR_TYPE_GREATER = 2;
    //小于
    FILTER_OPERATOR_TYPE_LESS = 3;
    //大于等于
    FILTER_OPERATOR_TYPE_GREATER_EQ = 4;
    //小于等于
    FILTER_OPERATOR_TYPE_LESS_EQ = 5;
    //不等于
    FILTER_OPERATOR_TYPE_NO_EQ = 6;
    //not in
    FILTER_OPERATOR_TYPE_NOT_IN = 8;
    //模糊匹配
    FILTER_OPERATOR_TYPE_FUZZINESS = 9;
}
        :type OperatorType: int
        :param _Values: 检索的值，各检索值间为OR关系
        :type Values: list of str
        """
        self._Name = None
        self._OperatorType = None
        self._Values = None

    @property
    def Name(self):
        """检索的键值
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OperatorType(self):
        """枚举类型，代表Name与Values之间的匹配关系
enum FilterOperatorType {
    //等于
    FILTER_OPERATOR_TYPE_EQUAL = 1;
    //大于
    FILTER_OPERATOR_TYPE_GREATER = 2;
    //小于
    FILTER_OPERATOR_TYPE_LESS = 3;
    //大于等于
    FILTER_OPERATOR_TYPE_GREATER_EQ = 4;
    //小于等于
    FILTER_OPERATOR_TYPE_LESS_EQ = 5;
    //不等于
    FILTER_OPERATOR_TYPE_NO_EQ = 6;
    //not in
    FILTER_OPERATOR_TYPE_NOT_IN = 8;
    //模糊匹配
    FILTER_OPERATOR_TYPE_FUZZINESS = 9;
}
        :rtype: int
        """
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType

    @property
    def Values(self):
        """检索的值，各检索值间为OR关系
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._OperatorType = params.get("OperatorType")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesRequest(AbstractModel):
    """CreateAcRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建规则数据
        :type Data: list of RuleInfoData
        :param _Type: 0：添加（默认），1：插入
        :type Type: int
        :param _EdgeId: 边id
        :type EdgeId: str
        :param _Enable: 访问控制规则状态
        :type Enable: int
        :param _Overwrite: 0：添加，1：覆盖
        :type Overwrite: int
        :param _InstanceId: NAT实例ID, 参数Area存在的时候这个必传
        :type InstanceId: str
        :param _From: portScan: 来自于端口扫描, patchImport: 来自于批量导入
        :type From: str
        :param _Area: NAT地域
        :type Area: str
        """
        self._Data = None
        self._Type = None
        self._EdgeId = None
        self._Enable = None
        self._Overwrite = None
        self._InstanceId = None
        self._From = None
        self._Area = None

    @property
    def Data(self):
        """创建规则数据
        :rtype: list of RuleInfoData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        """0：添加（默认），1：插入
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EdgeId(self):
        """边id
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Enable(self):
        """访问控制规则状态
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Overwrite(self):
        """0：添加，1：覆盖
        :rtype: int
        """
        return self._Overwrite

    @Overwrite.setter
    def Overwrite(self, Overwrite):
        self._Overwrite = Overwrite

    @property
    def InstanceId(self):
        """NAT实例ID, 参数Area存在的时候这个必传
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def From(self):
        """portScan: 来自于端口扫描, patchImport: 来自于批量导入
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Area(self):
        """NAT地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Type = params.get("Type")
        self._EdgeId = params.get("EdgeId")
        self._Enable = params.get("Enable")
        self._Overwrite = params.get("Overwrite")
        self._InstanceId = params.get("InstanceId")
        self._From = params.get("From")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcRulesResponse(AbstractModel):
    """CreateAcRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0:操作成功
        :type Status: int
        :param _Info: 返回多余的信息
        :type Info: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0:操作成功
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """返回多余的信息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class CreateAddressTemplateRequest(AbstractModel):
    """CreateAddressTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 模板名称
        :type Name: str
        :param _Detail: 模板描述
        :type Detail: str
        :param _IpString: Type为1，ip模板eg：1.1.1.1,2.2.2.2；
Type为5，域名模板eg：www.qq.com,www.tencent.com
        :type IpString: str
        :param _Type: 1 ip模板
5 域名模板
6 协议端口模板
        :type Type: int
        :param _ProtocolType: 协议端口模板，协议类型，4:4层协议，7:7层协议，Type=6时必填
        :type ProtocolType: str
        :param _IpVersion: IP版本,0 IPV4;1 IPV6
        :type IpVersion: int
        """
        self._Name = None
        self._Detail = None
        self._IpString = None
        self._Type = None
        self._ProtocolType = None
        self._IpVersion = None

    @property
    def Name(self):
        """模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Detail(self):
        """模板描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def IpString(self):
        """Type为1，ip模板eg：1.1.1.1,2.2.2.2；
Type为5，域名模板eg：www.qq.com,www.tencent.com
        :rtype: str
        """
        return self._IpString

    @IpString.setter
    def IpString(self, IpString):
        self._IpString = IpString

    @property
    def Type(self):
        """1 ip模板
5 域名模板
6 协议端口模板
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProtocolType(self):
        """协议端口模板，协议类型，4:4层协议，7:7层协议，Type=6时必填
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def IpVersion(self):
        """IP版本,0 IPV4;1 IPV6
        :rtype: int
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Detail = params.get("Detail")
        self._IpString = params.get("IpString")
        self._Type = params.get("Type")
        self._ProtocolType = params.get("ProtocolType")
        self._IpVersion = params.get("IpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressTemplateResponse(AbstractModel):
    """CreateAddressTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 创建结果,0成功
        :type Status: int
        :param _Uuid: 唯一Id
        :type Uuid: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Uuid = None
        self._RequestId = None

    @property
    def Status(self):
        """创建结果,0成功
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Uuid(self):
        """唯一Id
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

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
        self._Uuid = params.get("Uuid")
        self._RequestId = params.get("RequestId")


class CreateAlertCenterIsolateRequest(AbstractModel):
    """CreateAlertCenterIsolate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HandleAssetList: 处置对象,资产列表
        :type HandleAssetList: list of str
        :param _HandleTime: 处置时间
1  1天
7   7天
-2 永久
        :type HandleTime: int
        :param _AlertDirection: 当前日志方向： 0 出向 1 入向
        :type AlertDirection: int
        :param _IsolateType: 隔离类型 
1 互联网入站
2 互联网出站
4 内网访问
        :type IsolateType: list of int
        :param _OmMode: 运维模式 1 IP白名单 2 身份认证  0 非运维模式
        :type OmMode: int
        """
        self._HandleAssetList = None
        self._HandleTime = None
        self._AlertDirection = None
        self._IsolateType = None
        self._OmMode = None

    @property
    def HandleAssetList(self):
        """处置对象,资产列表
        :rtype: list of str
        """
        return self._HandleAssetList

    @HandleAssetList.setter
    def HandleAssetList(self, HandleAssetList):
        self._HandleAssetList = HandleAssetList

    @property
    def HandleTime(self):
        """处置时间
1  1天
7   7天
-2 永久
        :rtype: int
        """
        return self._HandleTime

    @HandleTime.setter
    def HandleTime(self, HandleTime):
        self._HandleTime = HandleTime

    @property
    def AlertDirection(self):
        """当前日志方向： 0 出向 1 入向
        :rtype: int
        """
        return self._AlertDirection

    @AlertDirection.setter
    def AlertDirection(self, AlertDirection):
        self._AlertDirection = AlertDirection

    @property
    def IsolateType(self):
        """隔离类型 
1 互联网入站
2 互联网出站
4 内网访问
        :rtype: list of int
        """
        return self._IsolateType

    @IsolateType.setter
    def IsolateType(self, IsolateType):
        self._IsolateType = IsolateType

    @property
    def OmMode(self):
        """运维模式 1 IP白名单 2 身份认证  0 非运维模式
        :rtype: int
        """
        return self._OmMode

    @OmMode.setter
    def OmMode(self, OmMode):
        self._OmMode = OmMode


    def _deserialize(self, params):
        self._HandleAssetList = params.get("HandleAssetList")
        self._HandleTime = params.get("HandleTime")
        self._AlertDirection = params.get("AlertDirection")
        self._IsolateType = params.get("IsolateType")
        self._OmMode = params.get("OmMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertCenterIsolateResponse(AbstractModel):
    """CreateAlertCenterIsolate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回状态码：
0 成功
非0 失败
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息：
success 成功
其他
        :type ReturnMsg: str
        :param _Status: 处置状态码：
0  处置成功
-1 通用错误，不用处理
-3 表示重复，需重新刷新列表
其他
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._Status = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        """返回状态码：
0 成功
非0 失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息：
success 成功
其他
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def Status(self):
        """处置状态码：
0  处置成功
-1 通用错误，不用处理
-3 表示重复，需重新刷新列表
其他
        :rtype: int
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
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateAlertCenterOmitRequest(AbstractModel):
    """CreateAlertCenterOmit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HandleIdList: 处置对象,ID列表，  IdLists和IpList二选一
        :type HandleIdList: list of str
        :param _TableType: 忽略数据来源：
AlertTable 告警中心  InterceptionTable拦截列表
        :type TableType: str
        :param _HandleEventIdList: 处置对象,事件ID列表
        :type HandleEventIdList: list of str
        """
        self._HandleIdList = None
        self._TableType = None
        self._HandleEventIdList = None

    @property
    def HandleIdList(self):
        """处置对象,ID列表，  IdLists和IpList二选一
        :rtype: list of str
        """
        return self._HandleIdList

    @HandleIdList.setter
    def HandleIdList(self, HandleIdList):
        self._HandleIdList = HandleIdList

    @property
    def TableType(self):
        """忽略数据来源：
AlertTable 告警中心  InterceptionTable拦截列表
        :rtype: str
        """
        return self._TableType

    @TableType.setter
    def TableType(self, TableType):
        self._TableType = TableType

    @property
    def HandleEventIdList(self):
        """处置对象,事件ID列表
        :rtype: list of str
        """
        return self._HandleEventIdList

    @HandleEventIdList.setter
    def HandleEventIdList(self, HandleEventIdList):
        self._HandleEventIdList = HandleEventIdList


    def _deserialize(self, params):
        self._HandleIdList = params.get("HandleIdList")
        self._TableType = params.get("TableType")
        self._HandleEventIdList = params.get("HandleEventIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertCenterOmitResponse(AbstractModel):
    """CreateAlertCenterOmit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回状态码：
0 成功
非0 失败
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息：
success 成功
其他
        :type ReturnMsg: str
        :param _Status: 处置状态码：
0  处置成功
-1 通用错误，不用处理
-3 表示重复，需重新刷新列表
其他
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._Status = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        """返回状态码：
0 成功
非0 失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息：
success 成功
其他
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def Status(self):
        """处置状态码：
0  处置成功
-1 通用错误，不用处理
-3 表示重复，需重新刷新列表
其他
        :rtype: int
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
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateAlertCenterRuleRequest(AbstractModel):
    """CreateAlertCenterRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HandleTime: 处置时间
1  1天
7   7天
-2 永久
        :type HandleTime: int
        :param _HandleType: 处置类型
当HandleIdList 不为空时：1封禁 2放通  
当HandleIpList 不为空时：3放通 4封禁
        :type HandleType: int
        :param _AlertDirection: 当前日志方向： 0 出向 1 入向
        :type AlertDirection: int
        :param _HandleDirection: 处置方向： 0出向 1入向 0,1出入向 3内网
        :type HandleDirection: str
        :param _HandleIdList: 处置对象,ID列表，  IdLists和IpList二选一
        :type HandleIdList: list of str
        :param _HandleIpList: 处置对象,IP列表，  IdLists和IpList二选一
        :type HandleIpList: list of str
        :param _HandleComment: 处置描述
        :type HandleComment: str
        :param _IgnoreReason: 放通原因:
0默认 1重复 2误报 3紧急放通
        :type IgnoreReason: int
        :param _BlockDomain: 封禁域名-保留字段
        :type BlockDomain: str
        """
        self._HandleTime = None
        self._HandleType = None
        self._AlertDirection = None
        self._HandleDirection = None
        self._HandleIdList = None
        self._HandleIpList = None
        self._HandleComment = None
        self._IgnoreReason = None
        self._BlockDomain = None

    @property
    def HandleTime(self):
        """处置时间
1  1天
7   7天
-2 永久
        :rtype: int
        """
        return self._HandleTime

    @HandleTime.setter
    def HandleTime(self, HandleTime):
        self._HandleTime = HandleTime

    @property
    def HandleType(self):
        """处置类型
当HandleIdList 不为空时：1封禁 2放通  
当HandleIpList 不为空时：3放通 4封禁
        :rtype: int
        """
        return self._HandleType

    @HandleType.setter
    def HandleType(self, HandleType):
        self._HandleType = HandleType

    @property
    def AlertDirection(self):
        """当前日志方向： 0 出向 1 入向
        :rtype: int
        """
        return self._AlertDirection

    @AlertDirection.setter
    def AlertDirection(self, AlertDirection):
        self._AlertDirection = AlertDirection

    @property
    def HandleDirection(self):
        """处置方向： 0出向 1入向 0,1出入向 3内网
        :rtype: str
        """
        return self._HandleDirection

    @HandleDirection.setter
    def HandleDirection(self, HandleDirection):
        self._HandleDirection = HandleDirection

    @property
    def HandleIdList(self):
        """处置对象,ID列表，  IdLists和IpList二选一
        :rtype: list of str
        """
        return self._HandleIdList

    @HandleIdList.setter
    def HandleIdList(self, HandleIdList):
        self._HandleIdList = HandleIdList

    @property
    def HandleIpList(self):
        """处置对象,IP列表，  IdLists和IpList二选一
        :rtype: list of str
        """
        return self._HandleIpList

    @HandleIpList.setter
    def HandleIpList(self, HandleIpList):
        self._HandleIpList = HandleIpList

    @property
    def HandleComment(self):
        """处置描述
        :rtype: str
        """
        return self._HandleComment

    @HandleComment.setter
    def HandleComment(self, HandleComment):
        self._HandleComment = HandleComment

    @property
    def IgnoreReason(self):
        """放通原因:
0默认 1重复 2误报 3紧急放通
        :rtype: int
        """
        return self._IgnoreReason

    @IgnoreReason.setter
    def IgnoreReason(self, IgnoreReason):
        self._IgnoreReason = IgnoreReason

    @property
    def BlockDomain(self):
        """封禁域名-保留字段
        :rtype: str
        """
        return self._BlockDomain

    @BlockDomain.setter
    def BlockDomain(self, BlockDomain):
        self._BlockDomain = BlockDomain


    def _deserialize(self, params):
        self._HandleTime = params.get("HandleTime")
        self._HandleType = params.get("HandleType")
        self._AlertDirection = params.get("AlertDirection")
        self._HandleDirection = params.get("HandleDirection")
        self._HandleIdList = params.get("HandleIdList")
        self._HandleIpList = params.get("HandleIpList")
        self._HandleComment = params.get("HandleComment")
        self._IgnoreReason = params.get("IgnoreReason")
        self._BlockDomain = params.get("BlockDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertCenterRuleResponse(AbstractModel):
    """CreateAlertCenterRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回状态码：
0 成功
非0 失败
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息：
success 成功
其他
        :type ReturnMsg: str
        :param _Status: 处置状态码：
0  处置成功
-1 通用错误，不用处理
-3 表示重复，需重新刷新列表
其他
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._Status = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        """返回状态码：
0 成功
非0 失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息：
success 成功
其他
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def Status(self):
        """处置状态码：
0  处置成功
-1 通用错误，不用处理
-3 表示重复，需重新刷新列表
其他
        :rtype: int
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
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateBlockIgnoreRuleListRequest(AbstractModel):
    """CreateBlockIgnoreRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
        :type Rules: list of IntrusionDefenseRule
        :param _RuleType: 规则类型，1封禁，2放通，不支持域名封禁
        :type RuleType: int
        :param _CoverDuplicate: 是否覆盖重复数据，1覆盖，非1不覆盖，跳过重复数据
        :type CoverDuplicate: int
        """
        self._Rules = None
        self._RuleType = None
        self._CoverDuplicate = None

    @property
    def Rules(self):
        """规则列表
        :rtype: list of IntrusionDefenseRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RuleType(self):
        """规则类型，1封禁，2放通，不支持域名封禁
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def CoverDuplicate(self):
        """是否覆盖重复数据，1覆盖，非1不覆盖，跳过重复数据
        :rtype: int
        """
        return self._CoverDuplicate

    @CoverDuplicate.setter
    def CoverDuplicate(self, CoverDuplicate):
        self._CoverDuplicate = CoverDuplicate


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = IntrusionDefenseRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RuleType = params.get("RuleType")
        self._CoverDuplicate = params.get("CoverDuplicate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlockIgnoreRuleListResponse(AbstractModel):
    """CreateBlockIgnoreRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 成功返回
        :type List: list of IocListData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """成功返回
        :rtype: list of IocListData
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
                obj = IocListData()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class CreateBlockIgnoreRuleNewRequest(AbstractModel):
    """CreateBlockIgnoreRuleNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 非自定义类型规则列表
        :type Rules: list of BanAndAllowRule
        :param _RuleType: RuleType: 1黑名单 2外部IP 3域名 4情报 5资产 6自定义规则  7入侵防御规则
        :type RuleType: int
        :param _CoverDuplicate: 是否覆盖重复数据，1覆盖，非1不覆盖，跳过重复数据
        :type CoverDuplicate: int
        """
        self._Rules = None
        self._RuleType = None
        self._CoverDuplicate = None

    @property
    def Rules(self):
        """非自定义类型规则列表
        :rtype: list of BanAndAllowRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RuleType(self):
        """RuleType: 1黑名单 2外部IP 3域名 4情报 5资产 6自定义规则  7入侵防御规则
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def CoverDuplicate(self):
        """是否覆盖重复数据，1覆盖，非1不覆盖，跳过重复数据
        :rtype: int
        """
        return self._CoverDuplicate

    @CoverDuplicate.setter
    def CoverDuplicate(self, CoverDuplicate):
        self._CoverDuplicate = CoverDuplicate


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = BanAndAllowRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RuleType = params.get("RuleType")
        self._CoverDuplicate = params.get("CoverDuplicate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlockIgnoreRuleNewResponse(AbstractModel):
    """CreateBlockIgnoreRuleNew返回参数结构体

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


class CreateChooseVpcsRequest(AbstractModel):
    """CreateChooseVpcs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcList: vpc列表
        :type VpcList: list of str
        :param _AllZoneList: zone列表
        :type AllZoneList: list of VpcZoneData
        """
        self._VpcList = None
        self._AllZoneList = None

    @property
    def VpcList(self):
        """vpc列表
        :rtype: list of str
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def AllZoneList(self):
        """zone列表
        :rtype: list of VpcZoneData
        """
        return self._AllZoneList

    @AllZoneList.setter
    def AllZoneList(self, AllZoneList):
        self._AllZoneList = AllZoneList


    def _deserialize(self, params):
        self._VpcList = params.get("VpcList")
        if params.get("AllZoneList") is not None:
            self._AllZoneList = []
            for item in params.get("AllZoneList"):
                obj = VpcZoneData()
                obj._deserialize(item)
                self._AllZoneList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChooseVpcsResponse(AbstractModel):
    """CreateChooseVpcs返回参数结构体

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


class CreateDatabaseWhiteListRulesRequest(AbstractModel):
    """CreateDatabaseWhiteListRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatabaseWhiteListRuleData: 创建白名单数据
        :type DatabaseWhiteListRuleData: list of DatabaseWhiteListRuleData
        """
        self._DatabaseWhiteListRuleData = None

    @property
    def DatabaseWhiteListRuleData(self):
        """创建白名单数据
        :rtype: list of DatabaseWhiteListRuleData
        """
        return self._DatabaseWhiteListRuleData

    @DatabaseWhiteListRuleData.setter
    def DatabaseWhiteListRuleData(self, DatabaseWhiteListRuleData):
        self._DatabaseWhiteListRuleData = DatabaseWhiteListRuleData


    def _deserialize(self, params):
        if params.get("DatabaseWhiteListRuleData") is not None:
            self._DatabaseWhiteListRuleData = []
            for item in params.get("DatabaseWhiteListRuleData"):
                obj = DatabaseWhiteListRuleData()
                obj._deserialize(item)
                self._DatabaseWhiteListRuleData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatabaseWhiteListRulesResponse(AbstractModel):
    """CreateDatabaseWhiteListRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0:添加成功，非0：添加失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0:添加成功，非0：添加失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateIdsWhiteRuleRequest(AbstractModel):
    """CreateIdsWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdsRuleId: 入侵防御规则ID
        :type IdsRuleId: str
        :param _WhiteRuleType: 白名单类型：
src 针对源放通
dst 针对目的放通
srcdst 针对源和目的放通
        :type WhiteRuleType: str
        :param _FwType: 白名单生效防火墙范围：
1 边界防火墙
2 nat防火墙
4 vpc防火墙
7 = 1+2+4  所有防火墙
        :type FwType: int
        :param _SrcIp: 源IP
        :type SrcIp: str
        :param _DstIp: 目的IP
        :type DstIp: str
        """
        self._IdsRuleId = None
        self._WhiteRuleType = None
        self._FwType = None
        self._SrcIp = None
        self._DstIp = None

    @property
    def IdsRuleId(self):
        """入侵防御规则ID
        :rtype: str
        """
        return self._IdsRuleId

    @IdsRuleId.setter
    def IdsRuleId(self, IdsRuleId):
        self._IdsRuleId = IdsRuleId

    @property
    def WhiteRuleType(self):
        """白名单类型：
src 针对源放通
dst 针对目的放通
srcdst 针对源和目的放通
        :rtype: str
        """
        return self._WhiteRuleType

    @WhiteRuleType.setter
    def WhiteRuleType(self, WhiteRuleType):
        self._WhiteRuleType = WhiteRuleType

    @property
    def FwType(self):
        """白名单生效防火墙范围：
1 边界防火墙
2 nat防火墙
4 vpc防火墙
7 = 1+2+4  所有防火墙
        :rtype: int
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def SrcIp(self):
        """源IP
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def DstIp(self):
        """目的IP
        :rtype: str
        """
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp


    def _deserialize(self, params):
        self._IdsRuleId = params.get("IdsRuleId")
        self._WhiteRuleType = params.get("WhiteRuleType")
        self._FwType = params.get("FwType")
        self._SrcIp = params.get("SrcIp")
        self._DstIp = params.get("DstIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIdsWhiteRuleResponse(AbstractModel):
    """CreateIdsWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回状态码：
0 成功
非0 失败
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息：
success 成功
其他
        :type ReturnMsg: str
        :param _Status: 返回状态码：
0  处置成功
-1 通用错误，不用处理
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._Status = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        """返回状态码：
0 成功
非0 失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息：
success 成功
其他
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def Status(self):
        """返回状态码：
0  处置成功
-1 通用错误，不用处理
        :rtype: int
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
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateNatFwInstanceRequest(AbstractModel):
    """CreateNatFwInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 防火墙实例名称
        :type Name: str
        :param _Width: 带宽
        :type Width: int
        :param _Mode: 模式 1：接入模式；0：新增模式
        :type Mode: int
        :param _NewModeItems: 新增模式传递参数，其中NewModeItems和NatgwList至少传递一种。
        :type NewModeItems: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        :param _NatGwList: 接入模式接入的nat网关列表，其中NewModeItems和NatgwList至少传递一种。
        :type NatGwList: list of str
        :param _Zone: 主可用区，为空则选择默认可用区
        :type Zone: str
        :param _ZoneBak: 备可用区，为空则选择默认可用区
        :type ZoneBak: str
        :param _CrossAZone: 异地灾备 1：使用异地灾备；0：不使用异地灾备；为空则默认不使用异地灾备
        :type CrossAZone: int
        :param _FwCidrInfo: 指定防火墙使用网段信息
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        self._Name = None
        self._Width = None
        self._Mode = None
        self._NewModeItems = None
        self._NatGwList = None
        self._Zone = None
        self._ZoneBak = None
        self._CrossAZone = None
        self._FwCidrInfo = None

    @property
    def Name(self):
        """防火墙实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Width(self):
        """带宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Mode(self):
        """模式 1：接入模式；0：新增模式
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def NewModeItems(self):
        """新增模式传递参数，其中NewModeItems和NatgwList至少传递一种。
        :rtype: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        """
        return self._NewModeItems

    @NewModeItems.setter
    def NewModeItems(self, NewModeItems):
        self._NewModeItems = NewModeItems

    @property
    def NatGwList(self):
        """接入模式接入的nat网关列表，其中NewModeItems和NatgwList至少传递一种。
        :rtype: list of str
        """
        return self._NatGwList

    @NatGwList.setter
    def NatGwList(self, NatGwList):
        self._NatGwList = NatGwList

    @property
    def Zone(self):
        """主可用区，为空则选择默认可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneBak(self):
        """备可用区，为空则选择默认可用区
        :rtype: str
        """
        return self._ZoneBak

    @ZoneBak.setter
    def ZoneBak(self, ZoneBak):
        self._ZoneBak = ZoneBak

    @property
    def CrossAZone(self):
        """异地灾备 1：使用异地灾备；0：不使用异地灾备；为空则默认不使用异地灾备
        :rtype: int
        """
        return self._CrossAZone

    @CrossAZone.setter
    def CrossAZone(self, CrossAZone):
        self._CrossAZone = CrossAZone

    @property
    def FwCidrInfo(self):
        """指定防火墙使用网段信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Width = params.get("Width")
        self._Mode = params.get("Mode")
        if params.get("NewModeItems") is not None:
            self._NewModeItems = NewModeItems()
            self._NewModeItems._deserialize(params.get("NewModeItems"))
        self._NatGwList = params.get("NatGwList")
        self._Zone = params.get("Zone")
        self._ZoneBak = params.get("ZoneBak")
        self._CrossAZone = params.get("CrossAZone")
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatFwInstanceResponse(AbstractModel):
    """CreateNatFwInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CfwInsId: 防火墙实例id
        :type CfwInsId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CfwInsId = None
        self._RequestId = None

    @property
    def CfwInsId(self):
        """防火墙实例id
        :rtype: str
        """
        return self._CfwInsId

    @CfwInsId.setter
    def CfwInsId(self, CfwInsId):
        self._CfwInsId = CfwInsId

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
        self._CfwInsId = params.get("CfwInsId")
        self._RequestId = params.get("RequestId")


class CreateNatFwInstanceWithDomainRequest(AbstractModel):
    """CreateNatFwInstanceWithDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 防火墙实例名称
        :type Name: str
        :param _Width: 带宽
        :type Width: int
        :param _Mode: 模式 1：接入模式；0：新增模式
        :type Mode: int
        :param _NewModeItems: 新增模式传递参数，其中NewModeItems和NatgwList至少传递一种。
        :type NewModeItems: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        :param _NatGwList: 接入模式接入的nat网关列表，其中NewModeItems和NatgwList至少传递一种。
        :type NatGwList: list of str
        :param _Zone: 主可用区，为空则选择默认可用区
        :type Zone: str
        :param _ZoneBak: 备可用区，为空则选择默认可用区
        :type ZoneBak: str
        :param _CrossAZone: 异地灾备 1：使用异地灾备；0：不使用异地灾备；为空则默认不使用异地灾备
        :type CrossAZone: int
        :param _IsCreateDomain: 0不创建域名,1创建域名
        :type IsCreateDomain: int
        :param _Domain: 如果要创建域名则必填
        :type Domain: str
        :param _FwCidrInfo: 指定防火墙使用网段信息
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        self._Name = None
        self._Width = None
        self._Mode = None
        self._NewModeItems = None
        self._NatGwList = None
        self._Zone = None
        self._ZoneBak = None
        self._CrossAZone = None
        self._IsCreateDomain = None
        self._Domain = None
        self._FwCidrInfo = None

    @property
    def Name(self):
        """防火墙实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Width(self):
        """带宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Mode(self):
        """模式 1：接入模式；0：新增模式
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def NewModeItems(self):
        """新增模式传递参数，其中NewModeItems和NatgwList至少传递一种。
        :rtype: :class:`tencentcloud.cfw.v20190904.models.NewModeItems`
        """
        return self._NewModeItems

    @NewModeItems.setter
    def NewModeItems(self, NewModeItems):
        self._NewModeItems = NewModeItems

    @property
    def NatGwList(self):
        """接入模式接入的nat网关列表，其中NewModeItems和NatgwList至少传递一种。
        :rtype: list of str
        """
        return self._NatGwList

    @NatGwList.setter
    def NatGwList(self, NatGwList):
        self._NatGwList = NatGwList

    @property
    def Zone(self):
        """主可用区，为空则选择默认可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneBak(self):
        """备可用区，为空则选择默认可用区
        :rtype: str
        """
        return self._ZoneBak

    @ZoneBak.setter
    def ZoneBak(self, ZoneBak):
        self._ZoneBak = ZoneBak

    @property
    def CrossAZone(self):
        """异地灾备 1：使用异地灾备；0：不使用异地灾备；为空则默认不使用异地灾备
        :rtype: int
        """
        return self._CrossAZone

    @CrossAZone.setter
    def CrossAZone(self, CrossAZone):
        self._CrossAZone = CrossAZone

    @property
    def IsCreateDomain(self):
        """0不创建域名,1创建域名
        :rtype: int
        """
        return self._IsCreateDomain

    @IsCreateDomain.setter
    def IsCreateDomain(self, IsCreateDomain):
        self._IsCreateDomain = IsCreateDomain

    @property
    def Domain(self):
        """如果要创建域名则必填
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def FwCidrInfo(self):
        """指定防火墙使用网段信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Width = params.get("Width")
        self._Mode = params.get("Mode")
        if params.get("NewModeItems") is not None:
            self._NewModeItems = NewModeItems()
            self._NewModeItems._deserialize(params.get("NewModeItems"))
        self._NatGwList = params.get("NatGwList")
        self._Zone = params.get("Zone")
        self._ZoneBak = params.get("ZoneBak")
        self._CrossAZone = params.get("CrossAZone")
        self._IsCreateDomain = params.get("IsCreateDomain")
        self._Domain = params.get("Domain")
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatFwInstanceWithDomainResponse(AbstractModel):
    """CreateNatFwInstanceWithDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CfwInsId: nat实例信息
        :type CfwInsId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CfwInsId = None
        self._RequestId = None

    @property
    def CfwInsId(self):
        """nat实例信息
        :rtype: str
        """
        return self._CfwInsId

    @CfwInsId.setter
    def CfwInsId(self, CfwInsId):
        self._CfwInsId = CfwInsId

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
        self._CfwInsId = params.get("CfwInsId")
        self._RequestId = params.get("RequestId")


class CreateNatRuleItem(AbstractModel):
    """创建NAT ACL规则参数结构

    """

    def __init__(self):
        r"""
        :param _SourceContent: 访问源示例： net：IP/CIDR(192.168.0.2)
        :type SourceContent: str
        :param _SourceType: 访问源类型：入向规则时类型可以为 ip,net,template,location；出向规则时可以为 ip,net,template,instance,group,tag
        :type SourceType: str
        :param _TargetContent: 访问目的示例： net：IP/CIDR(192.168.0.2) domain：域名规则，例如*.qq.com
        :type TargetContent: str
        :param _TargetType: 访问目的类型：入向规则时类型可以为ip,net,template,instance,group,tag；出向规则时可以为  ip,net,domain,template,location
        :type TargetType: str
        :param _Protocol: 协议，可选的值： TCP UDP ICMP ANY HTTP HTTPS HTTP/HTTPS SMTP SMTPS SMTP/SMTPS FTP DNS
        :type Protocol: str
        :param _RuleAction: 访问控制策略中设置的流量通过云防火墙的方式。取值： accept：放行 drop：拒绝 log：观察
        :type RuleAction: str
        :param _Port: 访问控制策略的端口。取值： -1/-1：全部端口 80：80端口
        :type Port: str
        :param _Direction: 规则方向：1，入站；0，出站
        :type Direction: int
        :param _OrderIndex: 规则序号
        :type OrderIndex: int
        :param _Enable: 规则状态，true表示启用，false表示禁用
        :type Enable: str
        :param _Uuid: 规则对应的唯一id，创建规则时无需填写
        :type Uuid: int
        :param _Description: 描述
        :type Description: str
        :param _ParamTemplateId: 端口协议组ID
        :type ParamTemplateId: str
        :param _InternalUuid: 内部id
        :type InternalUuid: int
        :param _Scope: 规则生效的范围：ALL，全局生效；ap-guangzhou，生效的地域；cfwnat-xxx，生效基于实例维度
        :type Scope: str
        """
        self._SourceContent = None
        self._SourceType = None
        self._TargetContent = None
        self._TargetType = None
        self._Protocol = None
        self._RuleAction = None
        self._Port = None
        self._Direction = None
        self._OrderIndex = None
        self._Enable = None
        self._Uuid = None
        self._Description = None
        self._ParamTemplateId = None
        self._InternalUuid = None
        self._Scope = None

    @property
    def SourceContent(self):
        """访问源示例： net：IP/CIDR(192.168.0.2)
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        """访问源类型：入向规则时类型可以为 ip,net,template,location；出向规则时可以为 ip,net,template,instance,group,tag
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetContent(self):
        """访问目的示例： net：IP/CIDR(192.168.0.2) domain：域名规则，例如*.qq.com
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def TargetType(self):
        """访问目的类型：入向规则时类型可以为ip,net,template,instance,group,tag；出向规则时可以为  ip,net,domain,template,location
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        """协议，可选的值： TCP UDP ICMP ANY HTTP HTTPS HTTP/HTTPS SMTP SMTPS SMTP/SMTPS FTP DNS
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        """访问控制策略中设置的流量通过云防火墙的方式。取值： accept：放行 drop：拒绝 log：观察
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Port(self):
        """访问控制策略的端口。取值： -1/-1：全部端口 80：80端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Direction(self):
        """规则方向：1，入站；0，出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def OrderIndex(self):
        """规则序号
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Enable(self):
        """规则状态，true表示启用，false表示禁用
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Uuid(self):
        """规则对应的唯一id，创建规则时无需填写
        :rtype: int
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

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
    def ParamTemplateId(self):
        """端口协议组ID
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def InternalUuid(self):
        """内部id
        :rtype: int
        """
        return self._InternalUuid

    @InternalUuid.setter
    def InternalUuid(self, InternalUuid):
        self._InternalUuid = InternalUuid

    @property
    def Scope(self):
        """规则生效的范围：ALL，全局生效；ap-guangzhou，生效的地域；cfwnat-xxx，生效基于实例维度
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._TargetContent = params.get("TargetContent")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Port = params.get("Port")
        self._Direction = params.get("Direction")
        self._OrderIndex = params.get("OrderIndex")
        self._Enable = params.get("Enable")
        self._Uuid = params.get("Uuid")
        self._Description = params.get("Description")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._InternalUuid = params.get("InternalUuid")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleItem(AbstractModel):
    """创建互联网边界规则参数结构

    """

    def __init__(self):
        r"""
        :param _SourceContent: 访问源示例： net：IP/CIDR(192.168.0.2)
        :type SourceContent: str
        :param _SourceType: 访问源类型：入向规则时类型可以为 ip,net,template,location；出向规则时可以为 ip,net,template,instance,group,tag
        :type SourceType: str
        :param _TargetContent: 访问目的示例： net：IP/CIDR(192.168.0.2) domain：域名规则，例如*.qq.com
        :type TargetContent: str
        :param _TargetType: 访问目的类型：入向规则时类型可以为ip,net,template,instance,group,tag；出向规则时可以为  ip,net,domain,template,location
        :type TargetType: str
        :param _Protocol: 协议，可选的值： TCP UDP ICMP ANY HTTP HTTPS HTTP/HTTPS SMTP SMTPS SMTP/SMTPS FTP DNS
1. 入方向  旁路防火墙/全局规则 仅支持TCP

2.出方向  旁路防火墙/全局规则 仅支持TCP HTTP/HTTPS TLS/SSL

3.domain  请选择七层协议 如HTTP/HTTPS

        :type Protocol: str
        :param _RuleAction: 访问控制策略中设置的流量通过云防火墙的方式。取值： accept：放行 drop：拒绝 log：观察
        :type RuleAction: str
        :param _Port: 访问控制策略的端口。取值： -1/-1：全部端口 80：80端口
        :type Port: str
        :param _Direction: 规则方向：1，入站；0，出站
        :type Direction: int
        :param _OrderIndex: 规则序号
        :type OrderIndex: int
        :param _Uuid: 规则对应的唯一id，创建规则时无需填写
        :type Uuid: int
        :param _Enable: 规则状态，true表示启用，false表示禁用
        :type Enable: str
        :param _Description: 描述
        :type Description: str
        :param _Scope: all
        :type Scope: str
        :param _RuleSource: 0，正常规则添加；1，入侵检测添加
        :type RuleSource: int
        :param _LogId: 告警Id
        :type LogId: str
        :param _ParamTemplateId: 端都协议组ID
        :type ParamTemplateId: str
        """
        self._SourceContent = None
        self._SourceType = None
        self._TargetContent = None
        self._TargetType = None
        self._Protocol = None
        self._RuleAction = None
        self._Port = None
        self._Direction = None
        self._OrderIndex = None
        self._Uuid = None
        self._Enable = None
        self._Description = None
        self._Scope = None
        self._RuleSource = None
        self._LogId = None
        self._ParamTemplateId = None

    @property
    def SourceContent(self):
        """访问源示例： net：IP/CIDR(192.168.0.2)
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        """访问源类型：入向规则时类型可以为 ip,net,template,location；出向规则时可以为 ip,net,template,instance,group,tag
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetContent(self):
        """访问目的示例： net：IP/CIDR(192.168.0.2) domain：域名规则，例如*.qq.com
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def TargetType(self):
        """访问目的类型：入向规则时类型可以为ip,net,template,instance,group,tag；出向规则时可以为  ip,net,domain,template,location
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        """协议，可选的值： TCP UDP ICMP ANY HTTP HTTPS HTTP/HTTPS SMTP SMTPS SMTP/SMTPS FTP DNS
1. 入方向  旁路防火墙/全局规则 仅支持TCP

2.出方向  旁路防火墙/全局规则 仅支持TCP HTTP/HTTPS TLS/SSL

3.domain  请选择七层协议 如HTTP/HTTPS

        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        """访问控制策略中设置的流量通过云防火墙的方式。取值： accept：放行 drop：拒绝 log：观察
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Port(self):
        """访问控制策略的端口。取值： -1/-1：全部端口 80：80端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Direction(self):
        """规则方向：1，入站；0，出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def OrderIndex(self):
        """规则序号
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Uuid(self):
        """规则对应的唯一id，创建规则时无需填写
        :rtype: int
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Enable(self):
        """规则状态，true表示启用，false表示禁用
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

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
    def Scope(self):
        """all
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def RuleSource(self):
        """0，正常规则添加；1，入侵检测添加
        :rtype: int
        """
        return self._RuleSource

    @RuleSource.setter
    def RuleSource(self, RuleSource):
        self._RuleSource = RuleSource

    @property
    def LogId(self):
        """告警Id
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def ParamTemplateId(self):
        """端都协议组ID
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._TargetContent = params.get("TargetContent")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Port = params.get("Port")
        self._Direction = params.get("Direction")
        self._OrderIndex = params.get("OrderIndex")
        self._Uuid = params.get("Uuid")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._Scope = params.get("Scope")
        self._RuleSource = params.get("RuleSource")
        self._LogId = params.get("LogId")
        self._ParamTemplateId = params.get("ParamTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupRulesRequest(AbstractModel):
    """CreateSecurityGroupRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 添加的企业安全组规则数据
        :type Data: list of SecurityGroupListData
        :param _Direction: 方向，0：出站，1：入站，默认1
        :type Direction: int
        :param _Type: 0：后插，1：前插，2：中插，默认0
        :type Type: int
        :param _Enable: 添加后是否启用规则，0：不启用，1：启用，默认1
        :type Enable: int
        """
        self._Data = None
        self._Direction = None
        self._Type = None
        self._Enable = None

    @property
    def Data(self):
        """添加的企业安全组规则数据
        :rtype: list of SecurityGroupListData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Direction(self):
        """方向，0：出站，1：入站，默认1
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Type(self):
        """0：后插，1：前插，2：中插，默认0
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Enable(self):
        """添加后是否启用规则，0：不启用，1：启用，默认1
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Direction = params.get("Direction")
        self._Type = params.get("Type")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupRulesResponse(AbstractModel):
    """CreateSecurityGroupRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0：添加成功，非0：添加失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0：添加成功，非0：添加失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateVpcFwGroupRequest(AbstractModel):
    """CreateVpcFwGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: VPC防火墙(组)名称
        :type Name: str
        :param _Mode: 模式 1：CCN云联网模式；0：私有网络模式 2: sase 模式 3：ccn 高级模式 4: 私有网络(跨租户单边模式)
        :type Mode: int
        :param _VpcFwInstances: 防火墙(组)下的防火墙实例列表
        :type VpcFwInstances: list of VpcFwInstance
        :param _SwitchMode: 防火墙实例的开关模式
1: 单点互通
2: 多点互通
3: 全互通
4: 自定义路由
        :type SwitchMode: int
        :param _FwVpcCidr: auto 自动选择防火墙网段
10.10.10.0/24 用户输入的防火墙网段
        :type FwVpcCidr: str
        :param _CcnId: 云联网id ，适用于云联网模式
        :type CcnId: str
        :param _FwCidrInfo: 指定防火墙使用网段信息
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        :param _CrossUserMode: 跨租户管理员模式  1管理员 2多账号
        :type CrossUserMode: str
        """
        self._Name = None
        self._Mode = None
        self._VpcFwInstances = None
        self._SwitchMode = None
        self._FwVpcCidr = None
        self._CcnId = None
        self._FwCidrInfo = None
        self._CrossUserMode = None

    @property
    def Name(self):
        """VPC防火墙(组)名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Mode(self):
        """模式 1：CCN云联网模式；0：私有网络模式 2: sase 模式 3：ccn 高级模式 4: 私有网络(跨租户单边模式)
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def VpcFwInstances(self):
        """防火墙(组)下的防火墙实例列表
        :rtype: list of VpcFwInstance
        """
        return self._VpcFwInstances

    @VpcFwInstances.setter
    def VpcFwInstances(self, VpcFwInstances):
        self._VpcFwInstances = VpcFwInstances

    @property
    def SwitchMode(self):
        """防火墙实例的开关模式
1: 单点互通
2: 多点互通
3: 全互通
4: 自定义路由
        :rtype: int
        """
        return self._SwitchMode

    @SwitchMode.setter
    def SwitchMode(self, SwitchMode):
        self._SwitchMode = SwitchMode

    @property
    def FwVpcCidr(self):
        """auto 自动选择防火墙网段
10.10.10.0/24 用户输入的防火墙网段
        :rtype: str
        """
        return self._FwVpcCidr

    @FwVpcCidr.setter
    def FwVpcCidr(self, FwVpcCidr):
        self._FwVpcCidr = FwVpcCidr

    @property
    def CcnId(self):
        """云联网id ，适用于云联网模式
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def FwCidrInfo(self):
        """指定防火墙使用网段信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo

    @property
    def CrossUserMode(self):
        """跨租户管理员模式  1管理员 2多账号
        :rtype: str
        """
        return self._CrossUserMode

    @CrossUserMode.setter
    def CrossUserMode(self, CrossUserMode):
        self._CrossUserMode = CrossUserMode


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Mode = params.get("Mode")
        if params.get("VpcFwInstances") is not None:
            self._VpcFwInstances = []
            for item in params.get("VpcFwInstances"):
                obj = VpcFwInstance()
                obj._deserialize(item)
                self._VpcFwInstances.append(obj)
        self._SwitchMode = params.get("SwitchMode")
        self._FwVpcCidr = params.get("FwVpcCidr")
        self._CcnId = params.get("CcnId")
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        self._CrossUserMode = params.get("CrossUserMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcFwGroupResponse(AbstractModel):
    """CreateVpcFwGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FwGroupId: 防火墙组ID
        :type FwGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FwGroupId = None
        self._RequestId = None

    @property
    def FwGroupId(self):
        """防火墙组ID
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

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
        self._FwGroupId = params.get("FwGroupId")
        self._RequestId = params.get("RequestId")


class CustomWhiteRule(AbstractModel):
    """自定义白名单规则

    """

    def __init__(self):
        r"""
        :param _DstIP: 访问目的
        :type DstIP: str
        :param _IdsRuleId: 规则ID
        :type IdsRuleId: str
        :param _IdsRuleName: 规则名称
        :type IdsRuleName: str
        :param _SrcIP: 访问源
        :type SrcIP: str
        """
        self._DstIP = None
        self._IdsRuleId = None
        self._IdsRuleName = None
        self._SrcIP = None

    @property
    def DstIP(self):
        """访问目的
        :rtype: str
        """
        return self._DstIP

    @DstIP.setter
    def DstIP(self, DstIP):
        self._DstIP = DstIP

    @property
    def IdsRuleId(self):
        """规则ID
        :rtype: str
        """
        return self._IdsRuleId

    @IdsRuleId.setter
    def IdsRuleId(self, IdsRuleId):
        self._IdsRuleId = IdsRuleId

    @property
    def IdsRuleName(self):
        """规则名称
        :rtype: str
        """
        return self._IdsRuleName

    @IdsRuleName.setter
    def IdsRuleName(self, IdsRuleName):
        self._IdsRuleName = IdsRuleName

    @property
    def SrcIP(self):
        """访问源
        :rtype: str
        """
        return self._SrcIP

    @SrcIP.setter
    def SrcIP(self, SrcIP):
        self._SrcIP = SrcIP


    def _deserialize(self, params):
        self._DstIP = params.get("DstIP")
        self._IdsRuleId = params.get("IdsRuleId")
        self._IdsRuleName = params.get("IdsRuleName")
        self._SrcIP = params.get("SrcIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseWhiteListRuleData(AbstractModel):
    """数据库白名单规则数据

    """

    def __init__(self):
        r"""
        :param _SourceIp: 访问源
        :type SourceIp: str
        :param _SourceType: 访问源类型，1 ip；6 实例；100 资源分组
        :type SourceType: int
        :param _TargetIp: 访问目的
        :type TargetIp: str
        :param _TargetType: 访问目的类型，1 ip；6 实例；100 资源分组
        :type TargetType: int
        :param _Detail: 规则描述
        :type Detail: str
        :param _IsRegionRule: 是否地域规则，0不是 1是
        :type IsRegionRule: int
        :param _IsCloudRule: 是否云厂商规则，0不是 1 时
        :type IsCloudRule: int
        :param _Enable: 是否启用，0 不启用，1启用
        :type Enable: int
        :param _FirstLevelRegionCode: 地域码1
        :type FirstLevelRegionCode: int
        :param _SecondLevelRegionCode: 地域码2
        :type SecondLevelRegionCode: int
        :param _FirstLevelRegionName: 地域名称1
        :type FirstLevelRegionName: str
        :param _SecondLevelRegionName: 地域名称2
        :type SecondLevelRegionName: str
        :param _CloudCode: 云厂商码
        :type CloudCode: str
        """
        self._SourceIp = None
        self._SourceType = None
        self._TargetIp = None
        self._TargetType = None
        self._Detail = None
        self._IsRegionRule = None
        self._IsCloudRule = None
        self._Enable = None
        self._FirstLevelRegionCode = None
        self._SecondLevelRegionCode = None
        self._FirstLevelRegionName = None
        self._SecondLevelRegionName = None
        self._CloudCode = None

    @property
    def SourceIp(self):
        """访问源
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def SourceType(self):
        """访问源类型，1 ip；6 实例；100 资源分组
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetIp(self):
        """访问目的
        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def TargetType(self):
        """访问目的类型，1 ip；6 实例；100 资源分组
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Detail(self):
        """规则描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def IsRegionRule(self):
        """是否地域规则，0不是 1是
        :rtype: int
        """
        return self._IsRegionRule

    @IsRegionRule.setter
    def IsRegionRule(self, IsRegionRule):
        self._IsRegionRule = IsRegionRule

    @property
    def IsCloudRule(self):
        """是否云厂商规则，0不是 1 时
        :rtype: int
        """
        return self._IsCloudRule

    @IsCloudRule.setter
    def IsCloudRule(self, IsCloudRule):
        self._IsCloudRule = IsCloudRule

    @property
    def Enable(self):
        """是否启用，0 不启用，1启用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def FirstLevelRegionCode(self):
        """地域码1
        :rtype: int
        """
        return self._FirstLevelRegionCode

    @FirstLevelRegionCode.setter
    def FirstLevelRegionCode(self, FirstLevelRegionCode):
        self._FirstLevelRegionCode = FirstLevelRegionCode

    @property
    def SecondLevelRegionCode(self):
        """地域码2
        :rtype: int
        """
        return self._SecondLevelRegionCode

    @SecondLevelRegionCode.setter
    def SecondLevelRegionCode(self, SecondLevelRegionCode):
        self._SecondLevelRegionCode = SecondLevelRegionCode

    @property
    def FirstLevelRegionName(self):
        """地域名称1
        :rtype: str
        """
        return self._FirstLevelRegionName

    @FirstLevelRegionName.setter
    def FirstLevelRegionName(self, FirstLevelRegionName):
        self._FirstLevelRegionName = FirstLevelRegionName

    @property
    def SecondLevelRegionName(self):
        """地域名称2
        :rtype: str
        """
        return self._SecondLevelRegionName

    @SecondLevelRegionName.setter
    def SecondLevelRegionName(self, SecondLevelRegionName):
        self._SecondLevelRegionName = SecondLevelRegionName

    @property
    def CloudCode(self):
        """云厂商码
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode


    def _deserialize(self, params):
        self._SourceIp = params.get("SourceIp")
        self._SourceType = params.get("SourceType")
        self._TargetIp = params.get("TargetIp")
        self._TargetType = params.get("TargetType")
        self._Detail = params.get("Detail")
        self._IsRegionRule = params.get("IsRegionRule")
        self._IsCloudRule = params.get("IsCloudRule")
        self._Enable = params.get("Enable")
        self._FirstLevelRegionCode = params.get("FirstLevelRegionCode")
        self._SecondLevelRegionCode = params.get("SecondLevelRegionCode")
        self._FirstLevelRegionName = params.get("FirstLevelRegionName")
        self._SecondLevelRegionName = params.get("SecondLevelRegionName")
        self._CloudCode = params.get("CloudCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAcRuleRequest(AbstractModel):
    """DeleteAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 删除规则对应的id值, 对应获取规则列表接口的Id 值
        :type Id: int
        :param _Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param _EdgeId: EdgeId值两个vpc间的边id
        :type EdgeId: str
        :param _Area: NAT地域， 如ap-shanghai/ap-guangzhou/ap-chongqing等
        :type Area: str
        """
        self._Id = None
        self._Direction = None
        self._EdgeId = None
        self._Area = None

    @property
    def Id(self):
        """删除规则对应的id值, 对应获取规则列表接口的Id 值
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Direction(self):
        """方向，0：出站，1：入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """EdgeId值两个vpc间的边id
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Area(self):
        """NAT地域， 如ap-shanghai/ap-guangzhou/ap-chongqing等
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAcRuleResponse(AbstractModel):
    """DeleteAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值 0: 删除成功, !0: 删除失败
        :type Status: int
        :param _Info: 返回多余的信息
        :type Info: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值 0: 删除成功, !0: 删除失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """返回多余的信息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DeleteAddressTemplateRequest(AbstractModel):
    """DeleteAddressTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 模板id
        :type Uuid: str
        """
        self._Uuid = None

    @property
    def Uuid(self):
        """模板id
        :rtype: str
        """
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
        


class DeleteAddressTemplateResponse(AbstractModel):
    """DeleteAddressTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 删除结果,0成功
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """删除结果,0成功
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteAllAccessControlRuleRequest(AbstractModel):
    """DeleteAllAccessControlRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Direction: 方向，0：出站，1：入站  默认值是 0
        :type Direction: int
        :param _EdgeId: VPC间防火墙开关ID  全部删除 EdgeId和Area只填写一个，不填写则不删除vpc间防火墙开关 ，默认值为‘’
        :type EdgeId: str
        :param _Area: nat地域 全部删除 EdgeId和Area只填写一个，不填写则不删除nat防火墙开关 默认值为‘’
        :type Area: str
        """
        self._Direction = None
        self._EdgeId = None
        self._Area = None

    @property
    def Direction(self):
        """方向，0：出站，1：入站  默认值是 0
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """VPC间防火墙开关ID  全部删除 EdgeId和Area只填写一个，不填写则不删除vpc间防火墙开关 ，默认值为‘’
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Area(self):
        """nat地域 全部删除 EdgeId和Area只填写一个，不填写则不删除nat防火墙开关 默认值为‘’
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAllAccessControlRuleResponse(AbstractModel):
    """DeleteAllAccessControlRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值 0: 修改成功, 非0: 修改失败
        :type Status: int
        :param _Info: 删除了几条访问控制规则
        :type Info: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值 0: 修改成功, 非0: 修改失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """删除了几条访问控制规则
        :rtype: int
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DeleteBlockIgnoreRuleListRequest(AbstractModel):
    """DeleteBlockIgnoreRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
        :type Rules: list of IocListData
        :param _RuleType: 规则类型，1封禁，2放通，不支持域名封禁
        :type RuleType: int
        """
        self._Rules = None
        self._RuleType = None

    @property
    def Rules(self):
        """规则列表
        :rtype: list of IocListData
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RuleType(self):
        """规则类型，1封禁，2放通，不支持域名封禁
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = IocListData()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlockIgnoreRuleListResponse(AbstractModel):
    """DeleteBlockIgnoreRuleList返回参数结构体

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


class DeleteBlockIgnoreRuleNewRequest(AbstractModel):
    """DeleteBlockIgnoreRuleNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteAll: 是否删除全部
        :type DeleteAll: int
        :param _Rules: 规则列表
        :type Rules: list of BanAndAllowRuleDel
        :param _RuleType: 封禁：1，放通：100，
主要用于全部删除时区分列表类型
        :type RuleType: int
        :param _ShowType: blocklist 封禁列表 whitelist 白名单列表
        :type ShowType: str
        """
        self._DeleteAll = None
        self._Rules = None
        self._RuleType = None
        self._ShowType = None

    @property
    def DeleteAll(self):
        """是否删除全部
        :rtype: int
        """
        return self._DeleteAll

    @DeleteAll.setter
    def DeleteAll(self, DeleteAll):
        self._DeleteAll = DeleteAll

    @property
    def Rules(self):
        """规则列表
        :rtype: list of BanAndAllowRuleDel
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def RuleType(self):
        """封禁：1，放通：100，
主要用于全部删除时区分列表类型
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def ShowType(self):
        """blocklist 封禁列表 whitelist 白名单列表
        :rtype: str
        """
        return self._ShowType

    @ShowType.setter
    def ShowType(self, ShowType):
        self._ShowType = ShowType


    def _deserialize(self, params):
        self._DeleteAll = params.get("DeleteAll")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = BanAndAllowRuleDel()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._RuleType = params.get("RuleType")
        self._ShowType = params.get("ShowType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlockIgnoreRuleNewResponse(AbstractModel):
    """DeleteBlockIgnoreRuleNew返回参数结构体

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


class DeleteIdsWhiteRuleRequest(AbstractModel):
    """DeleteIdsWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 入侵防御白名单id
参考DescribeIdsWhiteRule接口返回的Id字段
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        """入侵防御白名单id
参考DescribeIdsWhiteRule接口返回的Id字段
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
        


class DeleteIdsWhiteRuleResponse(AbstractModel):
    """DeleteIdsWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回状态码：
0 成功
非0 失败
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息：
success 成功
其他
        :type ReturnMsg: str
        :param _Status: 返回状态码：
0  处置成功
-1 通用错误，不用处理
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._Status = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        """返回状态码：
0 成功
非0 失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息：
success 成功
其他
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def Status(self):
        """返回状态码：
0  处置成功
-1 通用错误，不用处理
        :rtype: int
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
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteNatFwInstanceRequest(AbstractModel):
    """DeleteNatFwInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CfwInstance: 防火墙实例id
        :type CfwInstance: str
        """
        self._CfwInstance = None

    @property
    def CfwInstance(self):
        """防火墙实例id
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance


    def _deserialize(self, params):
        self._CfwInstance = params.get("CfwInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatFwInstanceResponse(AbstractModel):
    """DeleteNatFwInstance返回参数结构体

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


class DeleteRemoteAccessDomainRequest(AbstractModel):
    """DeleteRemoteAccessDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessDomainList: 域名列表
        :type AccessDomainList: list of str
        """
        self._AccessDomainList = None

    @property
    def AccessDomainList(self):
        """域名列表
        :rtype: list of str
        """
        return self._AccessDomainList

    @AccessDomainList.setter
    def AccessDomainList(self, AccessDomainList):
        self._AccessDomainList = AccessDomainList


    def _deserialize(self, params):
        self._AccessDomainList = params.get("AccessDomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRemoteAccessDomainResponse(AbstractModel):
    """DeleteRemoteAccessDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值 0：删除成功，非 0：删除失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值 0：删除成功，非 0：删除失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DeleteResourceGroupRequest(AbstractModel):
    """DeleteResourceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 组id
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """组id
        :rtype: str
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
        


class DeleteResourceGroupResponse(AbstractModel):
    """DeleteResourceGroup返回参数结构体

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


class DeleteSecurityGroupRuleRequest(AbstractModel):
    """DeleteSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 所需要删除规则的ID
        :type Id: int
        :param _Area: 腾讯云地域的英文简写
        :type Area: str
        :param _Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param _IsDelReverse: 是否删除反向规则，0：否，1：是
        :type IsDelReverse: int
        """
        self._Id = None
        self._Area = None
        self._Direction = None
        self._IsDelReverse = None

    @property
    def Id(self):
        """所需要删除规则的ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Area(self):
        """腾讯云地域的英文简写
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """方向，0：出站，1：入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def IsDelReverse(self):
        """是否删除反向规则，0：否，1：是
        :rtype: int
        """
        return self._IsDelReverse

    @IsDelReverse.setter
    def IsDelReverse(self, IsDelReverse):
        self._IsDelReverse = IsDelReverse


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        self._IsDelReverse = params.get("IsDelReverse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupRuleResponse(AbstractModel):
    """DeleteSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0：成功，非0：失败
        :type Status: int
        :param _Info: 返回多余的信息
        :type Info: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0：成功，非0：失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """返回多余的信息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class DeleteVpcFwGroupRequest(AbstractModel):
    """DeleteVpcFwGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FwGroupId: 防火墙(组)Id
        :type FwGroupId: str
        :param _DeleteFwGroup: 是否删除整个防火墙(组)
0：不删除防火墙(组)，只删除单独实例
1：删除整个防火墙(组)
        :type DeleteFwGroup: int
        :param _VpcFwInsList: 待删除的防火墙实例数组
        :type VpcFwInsList: list of str
        """
        self._FwGroupId = None
        self._DeleteFwGroup = None
        self._VpcFwInsList = None

    @property
    def FwGroupId(self):
        """防火墙(组)Id
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def DeleteFwGroup(self):
        """是否删除整个防火墙(组)
0：不删除防火墙(组)，只删除单独实例
1：删除整个防火墙(组)
        :rtype: int
        """
        return self._DeleteFwGroup

    @DeleteFwGroup.setter
    def DeleteFwGroup(self, DeleteFwGroup):
        self._DeleteFwGroup = DeleteFwGroup

    @property
    def VpcFwInsList(self):
        """待删除的防火墙实例数组
        :rtype: list of str
        """
        return self._VpcFwInsList

    @VpcFwInsList.setter
    def VpcFwInsList(self, VpcFwInsList):
        self._VpcFwInsList = VpcFwInsList


    def _deserialize(self, params):
        self._FwGroupId = params.get("FwGroupId")
        self._DeleteFwGroup = params.get("DeleteFwGroup")
        self._VpcFwInsList = params.get("VpcFwInsList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcFwGroupResponse(AbstractModel):
    """DeleteVpcFwGroup返回参数结构体

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


class DescAcItem(AbstractModel):
    """访问控制列表对象

    """

    def __init__(self):
        r"""
        :param _SourceContent: 访问源
        :type SourceContent: str
        :param _TargetContent: 访问目的
        :type TargetContent: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Port: 端口
        :type Port: str
        :param _RuleAction: 访问控制策略中设置的流量通过云防火墙的方式。取值： accept：放行 drop：拒绝 log：观察
        :type RuleAction: str
        :param _Description: 描述
        :type Description: str
        :param _Count: 命中次数
        :type Count: int
        :param _OrderIndex: 执行顺序
        :type OrderIndex: int
        :param _SourceType: 访问源类型：入向规则时类型可以为 ip,net,template,location；出向规则时可以为 ip,net,template,instance,group,tag
        :type SourceType: str
        :param _TargetType: 访问目的类型：入向规则时类型可以为ip,net,template,instance,group,tag；出向规则时可以为 ip,net,domain,template,location,dnsparse
        :type TargetType: str
        :param _Uuid: 规则对应的唯一id
        :type Uuid: int
        :param _Invalid: 规则有效性
        :type Invalid: int
        :param _IsRegion: 0为正常规则,1为地域规则
        :type IsRegion: int
        :param _CountryCode: 国家id
        :type CountryCode: int
        :param _CityCode: 城市id
        :type CityCode: int
        :param _CountryName: 国家名称
        :type CountryName: str
        :param _CityName: 省名称
        :type CityName: str
        :param _CloudCode: 云厂商code
        :type CloudCode: str
        :param _IsCloud: 0为正常规则,1为云厂商规则
        :type IsCloud: int
        :param _Enable: 规则状态，true表示启用，false表示禁用
        :type Enable: str
        :param _Direction: 规则方向：1，入向；0，出向
        :type Direction: int
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InternalUuid: 内部使用的uuid，一般情况下不会使用到该字段
        :type InternalUuid: int
        :param _Status: 规则状态，查询规则命中详情时该字段有效，0：新增，1: 已删除, 2: 编辑删除
        :type Status: int
        :param _BetaList: 关联任务详情
        :type BetaList: list of BetaInfoByACL
        :param _Scope: （1）互联网边界防火墙，生效范围：serial，串行；side，旁路；all，全局；
（2）NAT边界防火墙：ALL，全局生效；ap-guangzhou，生效的地域；cfwnat-xxx，生效基于实例维度
        :type Scope: str
        :param _ScopeDesc: 生效范围描述
        :type ScopeDesc: str
        :param _InternetBorderUuid: 互联网边界防火墙使用的内部规则id
        :type InternetBorderUuid: str
        :param _ParamTemplateName: 协议端口组名称
        :type ParamTemplateName: str
        :param _ParamTemplateId: 协议端口组ID
        :type ParamTemplateId: str
        :param _SourceName: 访问源名称
        :type SourceName: str
        :param _TargetName: 访问目的名称
        :type TargetName: str
        :param _LastHitTime: 规则最近命中时间
        :type LastHitTime: str
        :param _CountryKey: 地区简称
        :type CountryKey: str
        :param _CityKey: 省份、城市简称
        :type CityKey: str
        """
        self._SourceContent = None
        self._TargetContent = None
        self._Protocol = None
        self._Port = None
        self._RuleAction = None
        self._Description = None
        self._Count = None
        self._OrderIndex = None
        self._SourceType = None
        self._TargetType = None
        self._Uuid = None
        self._Invalid = None
        self._IsRegion = None
        self._CountryCode = None
        self._CityCode = None
        self._CountryName = None
        self._CityName = None
        self._CloudCode = None
        self._IsCloud = None
        self._Enable = None
        self._Direction = None
        self._InstanceName = None
        self._InternalUuid = None
        self._Status = None
        self._BetaList = None
        self._Scope = None
        self._ScopeDesc = None
        self._InternetBorderUuid = None
        self._ParamTemplateName = None
        self._ParamTemplateId = None
        self._SourceName = None
        self._TargetName = None
        self._LastHitTime = None
        self._CountryKey = None
        self._CityKey = None

    @property
    def SourceContent(self):
        """访问源
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def TargetContent(self):
        """访问目的
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

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
    def Port(self):
        """端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RuleAction(self):
        """访问控制策略中设置的流量通过云防火墙的方式。取值： accept：放行 drop：拒绝 log：观察
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

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
    def Count(self):
        """命中次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def OrderIndex(self):
        """执行顺序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceType(self):
        """访问源类型：入向规则时类型可以为 ip,net,template,location；出向规则时可以为 ip,net,template,instance,group,tag
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetType(self):
        """访问目的类型：入向规则时类型可以为ip,net,template,instance,group,tag；出向规则时可以为 ip,net,domain,template,location,dnsparse
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Uuid(self):
        """规则对应的唯一id
        :rtype: int
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Invalid(self):
        """规则有效性
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid

    @property
    def IsRegion(self):
        """0为正常规则,1为地域规则
        :rtype: int
        """
        return self._IsRegion

    @IsRegion.setter
    def IsRegion(self, IsRegion):
        self._IsRegion = IsRegion

    @property
    def CountryCode(self):
        """国家id
        :rtype: int
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def CityCode(self):
        """城市id
        :rtype: int
        """
        return self._CityCode

    @CityCode.setter
    def CityCode(self, CityCode):
        self._CityCode = CityCode

    @property
    def CountryName(self):
        """国家名称
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName

    @property
    def CityName(self):
        """省名称
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName

    @property
    def CloudCode(self):
        """云厂商code
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode

    @property
    def IsCloud(self):
        """0为正常规则,1为云厂商规则
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def Enable(self):
        """规则状态，true表示启用，false表示禁用
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Direction(self):
        """规则方向：1，入向；0，出向
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InternalUuid(self):
        """内部使用的uuid，一般情况下不会使用到该字段
        :rtype: int
        """
        return self._InternalUuid

    @InternalUuid.setter
    def InternalUuid(self, InternalUuid):
        self._InternalUuid = InternalUuid

    @property
    def Status(self):
        """规则状态，查询规则命中详情时该字段有效，0：新增，1: 已删除, 2: 编辑删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BetaList(self):
        """关联任务详情
        :rtype: list of BetaInfoByACL
        """
        return self._BetaList

    @BetaList.setter
    def BetaList(self, BetaList):
        self._BetaList = BetaList

    @property
    def Scope(self):
        """（1）互联网边界防火墙，生效范围：serial，串行；side，旁路；all，全局；
（2）NAT边界防火墙：ALL，全局生效；ap-guangzhou，生效的地域；cfwnat-xxx，生效基于实例维度
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ScopeDesc(self):
        """生效范围描述
        :rtype: str
        """
        return self._ScopeDesc

    @ScopeDesc.setter
    def ScopeDesc(self, ScopeDesc):
        self._ScopeDesc = ScopeDesc

    @property
    def InternetBorderUuid(self):
        """互联网边界防火墙使用的内部规则id
        :rtype: str
        """
        return self._InternetBorderUuid

    @InternetBorderUuid.setter
    def InternetBorderUuid(self, InternetBorderUuid):
        self._InternetBorderUuid = InternetBorderUuid

    @property
    def ParamTemplateName(self):
        """协议端口组名称
        :rtype: str
        """
        return self._ParamTemplateName

    @ParamTemplateName.setter
    def ParamTemplateName(self, ParamTemplateName):
        self._ParamTemplateName = ParamTemplateName

    @property
    def ParamTemplateId(self):
        """协议端口组ID
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def SourceName(self):
        """访问源名称
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def TargetName(self):
        """访问目的名称
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def LastHitTime(self):
        """规则最近命中时间
        :rtype: str
        """
        return self._LastHitTime

    @LastHitTime.setter
    def LastHitTime(self, LastHitTime):
        self._LastHitTime = LastHitTime

    @property
    def CountryKey(self):
        """地区简称
        :rtype: str
        """
        return self._CountryKey

    @CountryKey.setter
    def CountryKey(self, CountryKey):
        self._CountryKey = CountryKey

    @property
    def CityKey(self):
        """省份、城市简称
        :rtype: str
        """
        return self._CityKey

    @CityKey.setter
    def CityKey(self, CityKey):
        self._CityKey = CityKey


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._TargetContent = params.get("TargetContent")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._Count = params.get("Count")
        self._OrderIndex = params.get("OrderIndex")
        self._SourceType = params.get("SourceType")
        self._TargetType = params.get("TargetType")
        self._Uuid = params.get("Uuid")
        self._Invalid = params.get("Invalid")
        self._IsRegion = params.get("IsRegion")
        self._CountryCode = params.get("CountryCode")
        self._CityCode = params.get("CityCode")
        self._CountryName = params.get("CountryName")
        self._CityName = params.get("CityName")
        self._CloudCode = params.get("CloudCode")
        self._IsCloud = params.get("IsCloud")
        self._Enable = params.get("Enable")
        self._Direction = params.get("Direction")
        self._InstanceName = params.get("InstanceName")
        self._InternalUuid = params.get("InternalUuid")
        self._Status = params.get("Status")
        if params.get("BetaList") is not None:
            self._BetaList = []
            for item in params.get("BetaList"):
                obj = BetaInfoByACL()
                obj._deserialize(item)
                self._BetaList.append(obj)
        self._Scope = params.get("Scope")
        self._ScopeDesc = params.get("ScopeDesc")
        self._InternetBorderUuid = params.get("InternetBorderUuid")
        self._ParamTemplateName = params.get("ParamTemplateName")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._SourceName = params.get("SourceName")
        self._TargetName = params.get("TargetName")
        self._LastHitTime = params.get("LastHitTime")
        self._CountryKey = params.get("CountryKey")
        self._CityKey = params.get("CityKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescNatDnatRule(AbstractModel):
    """NAT防火墙Dnat规则列表

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _IpProtocol: 网络协议，可选值：TCP、UDP。
        :type IpProtocol: str
        :param _PublicIpAddress: 弹性IP。
        :type PublicIpAddress: str
        :param _PublicPort: 公网端口。
        :type PublicPort: int
        :param _PrivateIpAddress: 内网地址。
        :type PrivateIpAddress: str
        :param _PrivatePort: 内网端口。
        :type PrivatePort: int
        :param _Description: NAT防火墙转发规则描述。
        :type Description: str
        :param _IsReferenced: 是否被关联引用，如被远程运维使用
        :type IsReferenced: int
        :param _FwInsId: 所属防火墙实例id
        :type FwInsId: str
        :param _NatGwId: 关联的nat网关Id
        :type NatGwId: str
        """
        self._Id = None
        self._IpProtocol = None
        self._PublicIpAddress = None
        self._PublicPort = None
        self._PrivateIpAddress = None
        self._PrivatePort = None
        self._Description = None
        self._IsReferenced = None
        self._FwInsId = None
        self._NatGwId = None

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
    def IpProtocol(self):
        """网络协议，可选值：TCP、UDP。
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def PublicIpAddress(self):
        """弹性IP。
        :rtype: str
        """
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def PublicPort(self):
        """公网端口。
        :rtype: int
        """
        return self._PublicPort

    @PublicPort.setter
    def PublicPort(self, PublicPort):
        self._PublicPort = PublicPort

    @property
    def PrivateIpAddress(self):
        """内网地址。
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress

    @property
    def PrivatePort(self):
        """内网端口。
        :rtype: int
        """
        return self._PrivatePort

    @PrivatePort.setter
    def PrivatePort(self, PrivatePort):
        self._PrivatePort = PrivatePort

    @property
    def Description(self):
        """NAT防火墙转发规则描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsReferenced(self):
        """是否被关联引用，如被远程运维使用
        :rtype: int
        """
        return self._IsReferenced

    @IsReferenced.setter
    def IsReferenced(self, IsReferenced):
        self._IsReferenced = IsReferenced

    @property
    def FwInsId(self):
        """所属防火墙实例id
        :rtype: str
        """
        return self._FwInsId

    @FwInsId.setter
    def FwInsId(self, FwInsId):
        self._FwInsId = FwInsId

    @property
    def NatGwId(self):
        """关联的nat网关Id
        :rtype: str
        """
        return self._NatGwId

    @NatGwId.setter
    def NatGwId(self, NatGwId):
        self._NatGwId = NatGwId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._IpProtocol = params.get("IpProtocol")
        self._PublicIpAddress = params.get("PublicIpAddress")
        self._PublicPort = params.get("PublicPort")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        self._PrivatePort = params.get("PrivatePort")
        self._Description = params.get("Description")
        self._IsReferenced = params.get("IsReferenced")
        self._FwInsId = params.get("FwInsId")
        self._NatGwId = params.get("NatGwId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAcListsRequest(AbstractModel):
    """DescribeAcLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议
        :type Protocol: str
        :param _Strategy: 策略
        :type Strategy: str
        :param _SearchValue: 搜索值
        :type SearchValue: str
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Direction: 出站还是入站，1：入站，0：出站
        :type Direction: int
        :param _EdgeId: EdgeId值
        :type EdgeId: str
        :param _Status: 规则是否开启，'0': 未开启，'1': 开启, 默认为'0'
        :type Status: str
        :param _Area: 地域
        :type Area: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._Protocol = None
        self._Strategy = None
        self._SearchValue = None
        self._Limit = None
        self._Offset = None
        self._Direction = None
        self._EdgeId = None
        self._Status = None
        self._Area = None
        self._InstanceId = None

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
    def Strategy(self):
        """策略
        :rtype: str
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def SearchValue(self):
        """搜索值
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Direction(self):
        """出站还是入站，1：入站，0：出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """EdgeId值
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Status(self):
        """规则是否开启，'0': 未开启，'1': 开启, 默认为'0'
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Strategy = params.get("Strategy")
        self._SearchValue = params.get("SearchValue")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAcListsResponse(AbstractModel):
    """DescribeAcLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Data: 访问控制列表数据
        :type Data: list of AcListsData
        :param _AllTotal: 不算筛选条数的总条数
        :type AllTotal: int
        :param _Enable: 访问控制规则全部启用/全部停用
        :type Enable: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AllTotal = None
        self._Enable = None
        self._RequestId = None

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """访问控制列表数据
        :rtype: list of AcListsData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AllTotal(self):
        """不算筛选条数的总条数
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def Enable(self):
        """访问控制规则全部启用/全部停用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AcListsData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AllTotal = params.get("AllTotal")
        self._Enable = params.get("Enable")
        self._RequestId = params.get("RequestId")


class DescribeAclRuleRequest(AbstractModel):
    """DescribeAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Index: 需要查询的索引，特定场景使用，可不填
        :type Index: str
        :param _Filters: 过滤条件组合
        :type Filters: list of CommonFilter
        :param _StartTime: 检索的起始时间，可不传
        :type StartTime: str
        :param _EndTime: 检索的截止时间，可不传
        :type EndTime: str
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值，默认为asc
        :type Order: str
        :param _By: 排序所用到的字段，默认为sequence
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Index = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Index(self):
        """需要查询的索引，特定场景使用，可不填
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Filters(self):
        """过滤条件组合
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """检索的起始时间，可不传
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """检索的截止时间，可不传
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值，默认为asc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段，默认为sequence
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Index = params.get("Index")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
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
        :param _Total: 总条数
        :type Total: int
        :param _Data: nat访问控制列表数据
        :type Data: list of DescAcItem
        :param _AllTotal: 未过滤的总条数
        :type AllTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AllTotal = None
        self._RequestId = None

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """nat访问控制列表数据
        :rtype: list of DescAcItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AllTotal(self):
        """未过滤的总条数
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescAcItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AllTotal = params.get("AllTotal")
        self._RequestId = params.get("RequestId")


class DescribeAddressTemplateListRequest(AbstractModel):
    """DescribeAddressTemplateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，分页用
        :type Offset: int
        :param _Limit: 条数，分页用
        :type Limit: int
        :param _By: 排序字段，取值：UpdateTime最近更新时间，RulesNum关联规则数
        :type By: str
        :param _Order: 排序，取值 ：asc正序，desc逆序
        :type Order: str
        :param _SearchValue: 搜索值
        :type SearchValue: str
        :param _Uuid: 检索地址模板唯一id
        :type Uuid: str
        :param _TemplateType: 模板类型，取值：1：ip模板，5：域名模板，6：协议端口模板
        :type TemplateType: str
        :param _TemplateId: 模板Id
        :type TemplateId: str
        """
        self._Offset = None
        self._Limit = None
        self._By = None
        self._Order = None
        self._SearchValue = None
        self._Uuid = None
        self._TemplateType = None
        self._TemplateId = None

    @property
    def Offset(self):
        """偏移量，分页用
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """条数，分页用
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def By(self):
        """排序字段，取值：UpdateTime最近更新时间，RulesNum关联规则数
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Order(self):
        """排序，取值 ：asc正序，desc逆序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SearchValue(self):
        """搜索值
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Uuid(self):
        """检索地址模板唯一id
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def TemplateType(self):
        """模板类型，取值：1：ip模板，5：域名模板，6：协议端口模板
        :rtype: str
        """
        return self._TemplateType

    @TemplateType.setter
    def TemplateType(self, TemplateType):
        self._TemplateType = TemplateType

    @property
    def TemplateId(self):
        """模板Id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._By = params.get("By")
        self._Order = params.get("Order")
        self._SearchValue = params.get("SearchValue")
        self._Uuid = params.get("Uuid")
        self._TemplateType = params.get("TemplateType")
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressTemplateListResponse(AbstractModel):
    """DescribeAddressTemplateList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 模板总数
        :type Total: int
        :param _Data: 模板列表数据
        :type Data: list of TemplateListInfo
        :param _NameList: 模板名称列表
        :type NameList: list of str
        :param _IpTemplateCount: Ip地址模板数量
        :type IpTemplateCount: int
        :param _DomainTemplateCount: 域名地址模板数量
        :type DomainTemplateCount: int
        :param _PortTemplateCount: 协议端口模板数量
        :type PortTemplateCount: int
        :param _UsedTemplateCount: 已使用的地址模板数
        :type UsedTemplateCount: int
        :param _TemplateQuotaCount: 地址模板配额数量
        :type TemplateQuotaCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._NameList = None
        self._IpTemplateCount = None
        self._DomainTemplateCount = None
        self._PortTemplateCount = None
        self._UsedTemplateCount = None
        self._TemplateQuotaCount = None
        self._RequestId = None

    @property
    def Total(self):
        """模板总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """模板列表数据
        :rtype: list of TemplateListInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def NameList(self):
        """模板名称列表
        :rtype: list of str
        """
        return self._NameList

    @NameList.setter
    def NameList(self, NameList):
        self._NameList = NameList

    @property
    def IpTemplateCount(self):
        """Ip地址模板数量
        :rtype: int
        """
        return self._IpTemplateCount

    @IpTemplateCount.setter
    def IpTemplateCount(self, IpTemplateCount):
        self._IpTemplateCount = IpTemplateCount

    @property
    def DomainTemplateCount(self):
        """域名地址模板数量
        :rtype: int
        """
        return self._DomainTemplateCount

    @DomainTemplateCount.setter
    def DomainTemplateCount(self, DomainTemplateCount):
        self._DomainTemplateCount = DomainTemplateCount

    @property
    def PortTemplateCount(self):
        """协议端口模板数量
        :rtype: int
        """
        return self._PortTemplateCount

    @PortTemplateCount.setter
    def PortTemplateCount(self, PortTemplateCount):
        self._PortTemplateCount = PortTemplateCount

    @property
    def UsedTemplateCount(self):
        """已使用的地址模板数
        :rtype: int
        """
        return self._UsedTemplateCount

    @UsedTemplateCount.setter
    def UsedTemplateCount(self, UsedTemplateCount):
        self._UsedTemplateCount = UsedTemplateCount

    @property
    def TemplateQuotaCount(self):
        """地址模板配额数量
        :rtype: int
        """
        return self._TemplateQuotaCount

    @TemplateQuotaCount.setter
    def TemplateQuotaCount(self, TemplateQuotaCount):
        self._TemplateQuotaCount = TemplateQuotaCount

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TemplateListInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._NameList = params.get("NameList")
        self._IpTemplateCount = params.get("IpTemplateCount")
        self._DomainTemplateCount = params.get("DomainTemplateCount")
        self._PortTemplateCount = params.get("PortTemplateCount")
        self._UsedTemplateCount = params.get("UsedTemplateCount")
        self._TemplateQuotaCount = params.get("TemplateQuotaCount")
        self._RequestId = params.get("RequestId")


class DescribeAssetSyncRequest(AbstractModel):
    """DescribeAssetSync请求参数结构体

    """


class DescribeAssetSyncResponse(AbstractModel):
    """DescribeAssetSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 返回状态
1 更新中
2 更新完成
3 更新失败
4 更新失败
        :type Status: int
        :param _ReturnMsg: success 成功
其他失败
        :type ReturnMsg: str
        :param _ReturnCode: 0 成功
非0 失败
        :type ReturnCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def Status(self):
        """返回状态
1 更新中
2 更新完成
3 更新失败
4 更新失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReturnMsg(self):
        """success 成功
其他失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """0 成功
非0 失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

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
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class DescribeAssociatedInstanceListRequest(AbstractModel):
    """DescribeAssociatedInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 列表偏移量
        :type Offset: int
        :param _Limit: 每页记录条数
        :type Limit: int
        :param _Area: 地域代码（例：ap-guangzhou）,支持腾讯云全地域
        :type Area: str
        :param _SearchValue: 额外检索条件（JSON字符串）
        :type SearchValue: str
        :param _By: 排序字段
        :type By: str
        :param _Order: 排序方式（asc:升序,desc:降序）
        :type Order: str
        :param _SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param _Type: 实例类型,'3'是cvm实例,'4'是clb实例,'5'是eni实例,'6'是云数据库
        :type Type: str
        """
        self._Offset = None
        self._Limit = None
        self._Area = None
        self._SearchValue = None
        self._By = None
        self._Order = None
        self._SecurityGroupId = None
        self._Type = None

    @property
    def Offset(self):
        """列表偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页记录条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        """地域代码（例：ap-guangzhou）,支持腾讯云全地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SearchValue(self):
        """额外检索条件（JSON字符串）
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def By(self):
        """排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Order(self):
        """排序方式（asc:升序,desc:降序）
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def SecurityGroupId(self):
        """安全组ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def Type(self):
        """实例类型,'3'是cvm实例,'4'是clb实例,'5'是eni实例,'6'是云数据库
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        self._SearchValue = params.get("SearchValue")
        self._By = params.get("By")
        self._Order = params.get("Order")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssociatedInstanceListResponse(AbstractModel):
    """DescribeAssociatedInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 实例数量
        :type Total: int
        :param _Data: 实例列表
        :type Data: list of AssociatedInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """实例数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """实例列表
        :rtype: list of AssociatedInstanceInfo
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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AssociatedInstanceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlockByIpTimesListRequest(AbstractModel):
    """DescribeBlockByIpTimesList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Ip: ip查询条件
        :type Ip: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Direction: 方向
        :type Direction: str
        :param _EdgeId: vpc间防火墙开关边id
        :type EdgeId: str
        :param _LogSource: 日志来源 move：vpc间防火墙
        :type LogSource: str
        :param _Source: 来源
        :type Source: str
        :param _Zone: 地域
        :type Zone: str
        """
        self._EndTime = None
        self._Ip = None
        self._StartTime = None
        self._Direction = None
        self._EdgeId = None
        self._LogSource = None
        self._Source = None
        self._Zone = None

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
    def Ip(self):
        """ip查询条件
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
    def Direction(self):
        """方向
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """vpc间防火墙开关边id
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def LogSource(self):
        """日志来源 move：vpc间防火墙
        :rtype: str
        """
        return self._LogSource

    @LogSource.setter
    def LogSource(self, LogSource):
        self._LogSource = LogSource

    @property
    def Source(self):
        """来源
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Zone(self):
        """地域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._Ip = params.get("Ip")
        self._StartTime = params.get("StartTime")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._LogSource = params.get("LogSource")
        self._Source = params.get("Source")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockByIpTimesListResponse(AbstractModel):
    """DescribeBlockByIpTimesList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of IpStatic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """返回数据
        :rtype: list of IpStatic
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
                obj = IpStatic()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBlockIgnoreListRequest(AbstractModel):
    """DescribeBlockIgnoreList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 单页数量
        :type Limit: int
        :param _Offset: 页偏移量
        :type Offset: int
        :param _Direction: 方向：1互联网入站，0互联网出站，3内网，空 全部方向
        :type Direction: str
        :param _Order: 排序类型：desc降序，asc正序
        :type Order: str
        :param _By: 排序列：EndTime结束时间，StartTime开始时间，MatchTimes命中次数
        :type By: str
        :param _SearchValue: 搜索参数，json格式字符串，空则传"{}"，域名：domain，危险等级：level，放通原因：ignore_reason，安全事件来源：rule_source，地理位置：address，模糊搜索：common
        :type SearchValue: str
        :param _RuleType: 规则类型：1封禁，2放通
        :type RuleType: int
        :param _ShowType: blocklist 封禁列表
whitelist 白名单列表
        :type ShowType: str
        """
        self._Limit = None
        self._Offset = None
        self._Direction = None
        self._Order = None
        self._By = None
        self._SearchValue = None
        self._RuleType = None
        self._ShowType = None

    @property
    def Limit(self):
        """单页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Direction(self):
        """方向：1互联网入站，0互联网出站，3内网，空 全部方向
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Order(self):
        """排序类型：desc降序，asc正序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序列：EndTime结束时间，StartTime开始时间，MatchTimes命中次数
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def SearchValue(self):
        """搜索参数，json格式字符串，空则传"{}"，域名：domain，危险等级：level，放通原因：ignore_reason，安全事件来源：rule_source，地理位置：address，模糊搜索：common
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def RuleType(self):
        """规则类型：1封禁，2放通
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def ShowType(self):
        """blocklist 封禁列表
whitelist 白名单列表
        :rtype: str
        """
        return self._ShowType

    @ShowType.setter
    def ShowType(self, ShowType):
        self._ShowType = ShowType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Direction = params.get("Direction")
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._SearchValue = params.get("SearchValue")
        self._RuleType = params.get("RuleType")
        self._ShowType = params.get("ShowType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockIgnoreListResponse(AbstractModel):
    """DescribeBlockIgnoreList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 列表数据
        :type Data: list of BlockIgnoreRule
        :param _Total: 查询结果总数，用于分页
        :type Total: int
        :param _ReturnCode: 状态值，0：查询成功，非0：查询失败
        :type ReturnCode: int
        :param _ReturnMsg: 状态信息，success：查询成功，fail：查询失败
        :type ReturnMsg: str
        :param _SourceList: 安全事件来源下拉框
        :type SourceList: list of str
        :param _RuleTypeDataList: 对应规则类型的数量，示例：[0,122,30,55,12,232,0]，封禁0个，IP地址122个，域名30个，威胁情报55个，资产实例12个，自定义策略232个，入侵防御规则0个
        :type RuleTypeDataList: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._SourceList = None
        self._RuleTypeDataList = None
        self._RequestId = None

    @property
    def Data(self):
        """列表数据
        :rtype: list of BlockIgnoreRule
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """查询结果总数，用于分页
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ReturnCode(self):
        """状态值，0：查询成功，非0：查询失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """状态信息，success：查询成功，fail：查询失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def SourceList(self):
        """安全事件来源下拉框
        :rtype: list of str
        """
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def RuleTypeDataList(self):
        """对应规则类型的数量，示例：[0,122,30,55,12,232,0]，封禁0个，IP地址122个，域名30个，威胁情报55个，资产实例12个，自定义策略232个，入侵防御规则0个
        :rtype: list of int
        """
        return self._RuleTypeDataList

    @RuleTypeDataList.setter
    def RuleTypeDataList(self, RuleTypeDataList):
        self._RuleTypeDataList = RuleTypeDataList

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
                obj = BlockIgnoreRule()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._SourceList = params.get("SourceList")
        self._RuleTypeDataList = params.get("RuleTypeDataList")
        self._RequestId = params.get("RequestId")


class DescribeBlockStaticListRequest(AbstractModel):
    """DescribeBlockStaticList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _QueryType: 列表类型，只能是下面三种之一：port、address、ip
        :type QueryType: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Top: top数
        :type Top: int
        :param _SearchValue: 查询条件
        :type SearchValue: str
        """
        self._EndTime = None
        self._QueryType = None
        self._StartTime = None
        self._Top = None
        self._SearchValue = None

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
    def QueryType(self):
        """列表类型，只能是下面三种之一：port、address、ip
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

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
    def Top(self):
        """top数
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def SearchValue(self):
        """查询条件
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._QueryType = params.get("QueryType")
        self._StartTime = params.get("StartTime")
        self._Top = params.get("Top")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlockStaticListResponse(AbstractModel):
    """DescribeBlockStaticList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询结果
        :type Data: list of StaticInfo
        :param _Status: 异步查询状态，1查询执行中，0查询已结束
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Status = None
        self._RequestId = None

    @property
    def Data(self):
        """查询结果
        :rtype: list of StaticInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """异步查询状态，1查询执行中，0查询已结束
        :rtype: int
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StaticInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeCfwEipsRequest(AbstractModel):
    """DescribeCfwEips请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 1：cfw接入模式，目前仅支持接入模式实例
        :type Mode: int
        :param _NatGatewayId: ALL：查询所有弹性公网ip; nat-xxxxx：接入模式场景指定网关的弹性公网ip
        :type NatGatewayId: str
        :param _CfwInstance: 防火墙实例id，当前仅支持接入模式的实例，该字段必填
        :type CfwInstance: str
        """
        self._Mode = None
        self._NatGatewayId = None
        self._CfwInstance = None

    @property
    def Mode(self):
        """1：cfw接入模式，目前仅支持接入模式实例
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def NatGatewayId(self):
        """ALL：查询所有弹性公网ip; nat-xxxxx：接入模式场景指定网关的弹性公网ip
        :rtype: str
        """
        return self._NatGatewayId

    @NatGatewayId.setter
    def NatGatewayId(self, NatGatewayId):
        self._NatGatewayId = NatGatewayId

    @property
    def CfwInstance(self):
        """防火墙实例id，当前仅支持接入模式的实例，该字段必填
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._NatGatewayId = params.get("NatGatewayId")
        self._CfwInstance = params.get("CfwInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCfwEipsResponse(AbstractModel):
    """DescribeCfwEips返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NatFwEipList: 返回值信息
        :type NatFwEipList: list of NatFwEipsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NatFwEipList = None
        self._RequestId = None

    @property
    def NatFwEipList(self):
        """返回值信息
        :rtype: list of NatFwEipsInfo
        """
        return self._NatFwEipList

    @NatFwEipList.setter
    def NatFwEipList(self, NatFwEipList):
        self._NatFwEipList = NatFwEipList

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
        if params.get("NatFwEipList") is not None:
            self._NatFwEipList = []
            for item in params.get("NatFwEipList"):
                obj = NatFwEipsInfo()
                obj._deserialize(item)
                self._NatFwEipList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCfwInsStatusRequest(AbstractModel):
    """DescribeCfwInsStatus请求参数结构体

    """


class DescribeCfwInsStatusResponse(AbstractModel):
    """DescribeCfwInsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CfwInsStatus: 防火墙实例运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CfwInsStatus: list of CfwInsStatus
        :param _TotalCount: 0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CfwInsStatus = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CfwInsStatus(self):
        """防火墙实例运行状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CfwInsStatus
        """
        return self._CfwInsStatus

    @CfwInsStatus.setter
    def CfwInsStatus(self, CfwInsStatus):
        self._CfwInsStatus = CfwInsStatus

    @property
    def TotalCount(self):
        """0
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
        if params.get("CfwInsStatus") is not None:
            self._CfwInsStatus = []
            for item in params.get("CfwInsStatus"):
                obj = CfwInsStatus()
                obj._deserialize(item)
                self._CfwInsStatus.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDefenseSwitchRequest(AbstractModel):
    """DescribeDefenseSwitch请求参数结构体

    """


class DescribeDefenseSwitchResponse(AbstractModel):
    """DescribeDefenseSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BasicRuleSwitch: 基础防御开关
        :type BasicRuleSwitch: int
        :param _BaselineAllSwitch: 安全基线开关
        :type BaselineAllSwitch: int
        :param _TiSwitch: 威胁情报开关
        :type TiSwitch: int
        :param _VirtualPatchSwitch: 虚拟补丁开关
        :type VirtualPatchSwitch: int
        :param _HistoryOpen: 是否历史开启
        :type HistoryOpen: int
        :param _ReturnCode: 状态值，0：查询成功，非0：查询失败
        :type ReturnCode: int
        :param _ReturnMsg: 状态信息，success：查询成功，fail：查询失败
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BasicRuleSwitch = None
        self._BaselineAllSwitch = None
        self._TiSwitch = None
        self._VirtualPatchSwitch = None
        self._HistoryOpen = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def BasicRuleSwitch(self):
        """基础防御开关
        :rtype: int
        """
        return self._BasicRuleSwitch

    @BasicRuleSwitch.setter
    def BasicRuleSwitch(self, BasicRuleSwitch):
        self._BasicRuleSwitch = BasicRuleSwitch

    @property
    def BaselineAllSwitch(self):
        """安全基线开关
        :rtype: int
        """
        return self._BaselineAllSwitch

    @BaselineAllSwitch.setter
    def BaselineAllSwitch(self, BaselineAllSwitch):
        self._BaselineAllSwitch = BaselineAllSwitch

    @property
    def TiSwitch(self):
        """威胁情报开关
        :rtype: int
        """
        return self._TiSwitch

    @TiSwitch.setter
    def TiSwitch(self, TiSwitch):
        self._TiSwitch = TiSwitch

    @property
    def VirtualPatchSwitch(self):
        """虚拟补丁开关
        :rtype: int
        """
        return self._VirtualPatchSwitch

    @VirtualPatchSwitch.setter
    def VirtualPatchSwitch(self, VirtualPatchSwitch):
        self._VirtualPatchSwitch = VirtualPatchSwitch

    @property
    def HistoryOpen(self):
        """是否历史开启
        :rtype: int
        """
        return self._HistoryOpen

    @HistoryOpen.setter
    def HistoryOpen(self, HistoryOpen):
        self._HistoryOpen = HistoryOpen

    @property
    def ReturnCode(self):
        """状态值，0：查询成功，非0：查询失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """状态信息，success：查询成功，fail：查询失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        self._BasicRuleSwitch = params.get("BasicRuleSwitch")
        self._BaselineAllSwitch = params.get("BaselineAllSwitch")
        self._TiSwitch = params.get("TiSwitch")
        self._VirtualPatchSwitch = params.get("VirtualPatchSwitch")
        self._HistoryOpen = params.get("HistoryOpen")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeEnterpriseSGRuleProgressRequest(AbstractModel):
    """DescribeEnterpriseSGRuleProgress请求参数结构体

    """


class DescribeEnterpriseSGRuleProgressResponse(AbstractModel):
    """DescribeEnterpriseSGRuleProgress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 0-100，代表下发进度百分比
        :type Progress: int
        :param _UserStopped: 是否用户中止 用户中止返回true
        :type UserStopped: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Progress = None
        self._UserStopped = None
        self._RequestId = None

    @property
    def Progress(self):
        """0-100，代表下发进度百分比
        :rtype: int
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def UserStopped(self):
        """是否用户中止 用户中止返回true
        :rtype: bool
        """
        return self._UserStopped

    @UserStopped.setter
    def UserStopped(self, UserStopped):
        self._UserStopped = UserStopped

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
        self._Progress = params.get("Progress")
        self._UserStopped = params.get("UserStopped")
        self._RequestId = params.get("RequestId")


class DescribeEnterpriseSecurityGroupRuleListRequest(AbstractModel):
    """DescribeEnterpriseSecurityGroupRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页每页数量
        :type Limit: int
        :param _Offset: 分页当前页
        :type Offset: int
        :param _Status: 启用状态 1启用 0 未启用
        :type Status: str
        :param _Area: 地域
        :type Area: str
        :param _Filter: 规则下发方式筛选  1 新规则和延迟下发  2  仅看新规则  
        :type Filter: int
        :param _SearchValue: 查询条件
        :type SearchValue: str
        :param _SearchFilters: 查询条件新
        :type SearchFilters: list of CommonFilter
        """
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._Area = None
        self._Filter = None
        self._SearchValue = None
        self._SearchFilters = None

    @property
    def Limit(self):
        """分页每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页当前页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        """启用状态 1启用 0 未启用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Filter(self):
        """规则下发方式筛选  1 新规则和延迟下发  2  仅看新规则  
        :rtype: int
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def SearchValue(self):
        """查询条件
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def SearchFilters(self):
        """查询条件新
        :rtype: list of CommonFilter
        """
        return self._SearchFilters

    @SearchFilters.setter
    def SearchFilters(self, SearchFilters):
        self._SearchFilters = SearchFilters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        self._Filter = params.get("Filter")
        self._SearchValue = params.get("SearchValue")
        if params.get("SearchFilters") is not None:
            self._SearchFilters = []
            for item in params.get("SearchFilters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._SearchFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnterpriseSecurityGroupRuleListResponse(AbstractModel):
    """DescribeEnterpriseSecurityGroupRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 查询结果总数
        :type Total: int
        :param _AllTotal: 规则总数
        :type AllTotal: int
        :param _Data: 规则列表
        :type Data: list of EnterpriseSecurityGroupRuleRuleInfo
        :param _Enable: 规则列表整体启用状态 
取值范围 0/1/2
0.表示没有启用的(可以批量启用)  
1.表示没有禁用的(可以批量禁用)    
2 表示混合情况（不可批量操作）
        :type Enable: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AllTotal = None
        self._Data = None
        self._Enable = None
        self._RequestId = None

    @property
    def Total(self):
        """查询结果总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AllTotal(self):
        """规则总数
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def Data(self):
        """规则列表
        :rtype: list of EnterpriseSecurityGroupRuleRuleInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Enable(self):
        """规则列表整体启用状态 
取值范围 0/1/2
0.表示没有启用的(可以批量启用)  
1.表示没有禁用的(可以批量禁用)    
2 表示混合情况（不可批量操作）
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

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
        self._Total = params.get("Total")
        self._AllTotal = params.get("AllTotal")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EnterpriseSecurityGroupRuleRuleInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Enable = params.get("Enable")
        self._RequestId = params.get("RequestId")


class DescribeEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """DescribeEnterpriseSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNo: 分页查询时，显示的当前页的页码。

默认值为1。
        :type PageNo: str
        :param _PageSize: 分页查询时，显示的每页数据的最大条数。

可设置值最大为50。
        :type PageSize: str
        :param _SourceContent: 访问源示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
支持通配
        :type SourceContent: str
        :param _DestContent: 访问目的示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
支持通配
        :type DestContent: str
        :param _Description: 规则描述，支持通配
        :type Description: str
        :param _RuleAction: 访问控制策略中设置的流量通过云防火墙的方式。取值：
accept：放行
drop：拒绝
        :type RuleAction: str
        :param _Enable: 是否启用规则，默认为启用，取值：
true为启用，false为不启用
        :type Enable: str
        :param _Port: 访问控制策略的端口。取值：
-1/-1：全部端口
80：80端口
        :type Port: str
        :param _Protocol: 协议；TCP/UDP/ICMP/ANY
        :type Protocol: str
        :param _ServiceTemplateId: 端口协议类型参数模板id；协议端口模板id
        :type ServiceTemplateId: str
        :param _RuleUuid: 规则的uuid
        :type RuleUuid: int
        """
        self._PageNo = None
        self._PageSize = None
        self._SourceContent = None
        self._DestContent = None
        self._Description = None
        self._RuleAction = None
        self._Enable = None
        self._Port = None
        self._Protocol = None
        self._ServiceTemplateId = None
        self._RuleUuid = None

    @property
    def PageNo(self):
        """分页查询时，显示的当前页的页码。

默认值为1。
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """分页查询时，显示的每页数据的最大条数。

可设置值最大为50。
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SourceContent(self):
        """访问源示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
支持通配
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def DestContent(self):
        """访问目的示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
支持通配
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def Description(self):
        """规则描述，支持通配
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleAction(self):
        """访问控制策略中设置的流量通过云防火墙的方式。取值：
accept：放行
drop：拒绝
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Enable(self):
        """是否启用规则，默认为启用，取值：
true为启用，false为不启用
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Port(self):
        """访问控制策略的端口。取值：
-1/-1：全部端口
80：80端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        """协议；TCP/UDP/ICMP/ANY
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ServiceTemplateId(self):
        """端口协议类型参数模板id；协议端口模板id
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def RuleUuid(self):
        """规则的uuid
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._SourceContent = params.get("SourceContent")
        self._DestContent = params.get("DestContent")
        self._Description = params.get("Description")
        self._RuleAction = params.get("RuleAction")
        self._Enable = params.get("Enable")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._RuleUuid = params.get("RuleUuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """DescribeEnterpriseSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNo: 分页查询时，显示的当前页的页码。
        :type PageNo: str
        :param _PageSize: 分页查询时，显示的每页数据的最大条数。
        :type PageSize: str
        :param _Rules: 访问控制策略列表
        :type Rules: list of SecurityGroupRule
        :param _TotalCount: 访问控制策略的总数量。
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PageNo = None
        self._PageSize = None
        self._Rules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PageNo(self):
        """分页查询时，显示的当前页的页码。
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """分页查询时，显示的每页数据的最大条数。
        :rtype: str
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Rules(self):
        """访问控制策略列表
        :rtype: list of SecurityGroupRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        """访问控制策略的总数量。
        :rtype: str
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
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeFwEdgeIpsRequest(AbstractModel):
    """DescribeFwEdgeIps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件组合
        :type Filters: list of CommonFilter
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _StartTime: 检索的起始时间，可不传
        :type StartTime: str
        :param _EndTime: 检索的截止时间，可不传
        :type EndTime: str
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :type Order: str
        :param _By: 排序所用到的字段
        :type By: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Filters(self):
        """过滤条件组合
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        """检索的起始时间，可不传
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """检索的截止时间，可不传
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFwEdgeIpsResponse(AbstractModel):
    """DescribeFwEdgeIps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: ip 开关列表
        :type Data: list of EdgeIpInfo
        :param _Total: ip 开关列表个数
        :type Total: int
        :param _RegionLst: 地域列表
        :type RegionLst: list of str
        :param _InstanceTypeLst: 实例类型列表
        :type InstanceTypeLst: list of str
        :param _SerilCount: 串行模式开关个数
        :type SerilCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RegionLst = None
        self._InstanceTypeLst = None
        self._SerilCount = None
        self._RequestId = None

    @property
    def Data(self):
        """ip 开关列表
        :rtype: list of EdgeIpInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """ip 开关列表个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RegionLst(self):
        """地域列表
        :rtype: list of str
        """
        return self._RegionLst

    @RegionLst.setter
    def RegionLst(self, RegionLst):
        self._RegionLst = RegionLst

    @property
    def InstanceTypeLst(self):
        """实例类型列表
        :rtype: list of str
        """
        return self._InstanceTypeLst

    @InstanceTypeLst.setter
    def InstanceTypeLst(self, InstanceTypeLst):
        self._InstanceTypeLst = InstanceTypeLst

    @property
    def SerilCount(self):
        """串行模式开关个数
        :rtype: int
        """
        return self._SerilCount

    @SerilCount.setter
    def SerilCount(self, SerilCount):
        self._SerilCount = SerilCount

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
                obj = EdgeIpInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RegionLst = params.get("RegionLst")
        self._InstanceTypeLst = params.get("InstanceTypeLst")
        self._SerilCount = params.get("SerilCount")
        self._RequestId = params.get("RequestId")


class DescribeFwGroupInstanceInfoRequest(AbstractModel):
    """DescribeFwGroupInstanceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Filters: 过滤条件组合
        :type Filters: list of CommonFilter
        :param _StartTime: 检索的起始时间，可不传
        :type StartTime: str
        :param _EndTime: 检索的截止时间，可不传
        :type EndTime: str
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :type Order: str
        :param _By: 排序所用到的字段
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤条件组合
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """检索的起始时间，可不传
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """检索的截止时间，可不传
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFwGroupInstanceInfoResponse(AbstractModel):
    """DescribeFwGroupInstanceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcFwGroupLst: 防火墙(组)详细信息
        :type VpcFwGroupLst: list of VpcFwGroupInfo
        :param _Total: 防火墙(组)个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcFwGroupLst = None
        self._Total = None
        self._RequestId = None

    @property
    def VpcFwGroupLst(self):
        """防火墙(组)详细信息
        :rtype: list of VpcFwGroupInfo
        """
        return self._VpcFwGroupLst

    @VpcFwGroupLst.setter
    def VpcFwGroupLst(self, VpcFwGroupLst):
        self._VpcFwGroupLst = VpcFwGroupLst

    @property
    def Total(self):
        """防火墙(组)个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("VpcFwGroupLst") is not None:
            self._VpcFwGroupLst = []
            for item in params.get("VpcFwGroupLst"):
                obj = VpcFwGroupInfo()
                obj._deserialize(item)
                self._VpcFwGroupLst.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeFwSyncStatusRequest(AbstractModel):
    """DescribeFwSyncStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncType: 查询的同步状态类型：Route,同步路由状态
        :type SyncType: str
        """
        self._SyncType = None

    @property
    def SyncType(self):
        """查询的同步状态类型：Route,同步路由状态
        :rtype: str
        """
        return self._SyncType

    @SyncType.setter
    def SyncType(self, SyncType):
        self._SyncType = SyncType


    def _deserialize(self, params):
        self._SyncType = params.get("SyncType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFwSyncStatusResponse(AbstractModel):
    """DescribeFwSyncStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncStatus: 同步状态：1，同步中；0，同步完成
        :type SyncStatus: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SyncStatus = None
        self._RequestId = None

    @property
    def SyncStatus(self):
        """同步状态：1，同步中；0，同步完成
        :rtype: int
        """
        return self._SyncStatus

    @SyncStatus.setter
    def SyncStatus(self, SyncStatus):
        self._SyncStatus = SyncStatus

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
        self._SyncStatus = params.get("SyncStatus")
        self._RequestId = params.get("RequestId")


class DescribeGuideScanInfoRequest(AbstractModel):
    """DescribeGuideScanInfo请求参数结构体

    """


class DescribeGuideScanInfoResponse(AbstractModel):
    """DescribeGuideScanInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 扫描信息
        :type Data: :class:`tencentcloud.cfw.v20190904.models.ScanInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """扫描信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ScanInfo`
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
            self._Data = ScanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeIPStatusListRequest(AbstractModel):
    """DescribeIPStatusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IPList: 资产Id
        :type IPList: list of str
        """
        self._IPList = None

    @property
    def IPList(self):
        """资产Id
        :rtype: list of str
        """
        return self._IPList

    @IPList.setter
    def IPList(self, IPList):
        self._IPList = IPList


    def _deserialize(self, params):
        self._IPList = params.get("IPList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStatusListResponse(AbstractModel):
    """DescribeIPStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatusList: IP状态信息
        :type StatusList: list of IPDefendStatus
        :param _ReturnCode: 状态码
        :type ReturnCode: int
        :param _ReturnMsg: 状态信息
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatusList = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def StatusList(self):
        """IP状态信息
        :rtype: list of IPDefendStatus
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def ReturnCode(self):
        """状态码
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """状态信息
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        if params.get("StatusList") is not None:
            self._StatusList = []
            for item in params.get("StatusList"):
                obj = IPDefendStatus()
                obj._deserialize(item)
                self._StatusList.append(obj)
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeIdsWhiteRuleRequest(AbstractModel):
    """DescribeIdsWhiteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Filters: 过滤条件组合
        :type Filters: list of CommonFilter
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :type Order: str
        :param _By: 排序所用到的字段
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤条件组合
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdsWhiteRuleResponse(AbstractModel):
    """DescribeIdsWhiteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Data: 规则详情
        :type Data: list of IdsWhiteInfo
        :param _ReturnCode: 返回状态码 0 成功 非0不成功
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息  success 成功 其他 不成功
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """规则详情
        :rtype: list of IdsWhiteInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        """返回状态码 0 成功 非0不成功
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息  success 成功 其他 不成功
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = IdsWhiteInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeLogsRequest(AbstractModel):
    """DescribeLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Index: 日志类型标识
流量日志：互联网边界防火墙netflow_border，NAT边界防火墙netflow_nat，VPC间防火墙vpcnetflow，内网流量日志netflow_fl，流量分析日志netflow_nta
入侵防御日志rule_threatinfo
访问控制日志：互联网边界规则rule_acl，NAT边界规则rule_acl，内网间规则rule_vpcacl，企业安全组rule_sg
操作日志：防火墙开关-开关操作operate_switch，防火墙开关-实例配置operate_instance，资产中心操作operate_assetgroup，访问控制操作operate_acl，零信任防护操作operate_identity，入侵防御操作-入侵防御operate_ids，入侵防御操作-安全基线operate_baseline，常用工具操作operate_tool，网络蜜罐操作operate_honeypot，日志投递操作operate_logdelivery，通用设置操作operate_logstorage，登录日志operate_login
        :type Index: str
        :param _Limit: 每页条数，最大支持2000
        :type Limit: int
        :param _Offset: 偏移值，最大支持60000
        :type Offset: int
        :param _StartTime: 筛选开始时间
        :type StartTime: str
        :param _EndTime: 筛选结束时间
        :type EndTime: str
        :param _Filters: 过滤条件组合，各数组元素间为AND关系，查询字段名Name参考文档https://cloud.tencent.com/document/product/1132/87894，数值类型字段不支持模糊匹配
        :type Filters: list of CommonFilter
        """
        self._Index = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None

    @property
    def Index(self):
        """日志类型标识
流量日志：互联网边界防火墙netflow_border，NAT边界防火墙netflow_nat，VPC间防火墙vpcnetflow，内网流量日志netflow_fl，流量分析日志netflow_nta
入侵防御日志rule_threatinfo
访问控制日志：互联网边界规则rule_acl，NAT边界规则rule_acl，内网间规则rule_vpcacl，企业安全组rule_sg
操作日志：防火墙开关-开关操作operate_switch，防火墙开关-实例配置operate_instance，资产中心操作operate_assetgroup，访问控制操作operate_acl，零信任防护操作operate_identity，入侵防御操作-入侵防御operate_ids，入侵防御操作-安全基线operate_baseline，常用工具操作operate_tool，网络蜜罐操作operate_honeypot，日志投递操作operate_logdelivery，通用设置操作operate_logstorage，登录日志operate_login
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Limit(self):
        """每页条数，最大支持2000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值，最大支持60000
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        """筛选开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """筛选结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        """过滤条件组合，各数组元素间为AND关系，查询字段名Name参考文档https://cloud.tencent.com/document/product/1132/87894，数值类型字段不支持模糊匹配
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogsResponse(AbstractModel):
    """DescribeLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 日志列表
        :type Data: str
        :param _Total: 总条数
        :type Total: int
        :param _ReturnCode: 返回状态码 0 成功 非0不成功
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息  success 成功 其他 不成功
        :type ReturnMsg: str
        :param _AppProtocolList: 七层协议，NTA日志有效
        :type AppProtocolList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._AppProtocolList = None
        self._RequestId = None

    @property
    def Data(self):
        """日志列表
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ReturnCode(self):
        """返回状态码 0 成功 非0不成功
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息  success 成功 其他 不成功
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def AppProtocolList(self):
        """七层协议，NTA日志有效
        :rtype: list of str
        """
        return self._AppProtocolList

    @AppProtocolList.setter
    def AppProtocolList(self, AppProtocolList):
        self._AppProtocolList = AppProtocolList

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
        self._Data = params.get("Data")
        self._Total = params.get("Total")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._AppProtocolList = params.get("AppProtocolList")
        self._RequestId = params.get("RequestId")


class DescribeNatAcRuleRequest(AbstractModel):
    """DescribeNatAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Index: 需要查询的索引，特定场景使用，可不填
        :type Index: str
        :param _Filters: 过滤条件组合，Direction 为0时表述查询出向规则，为1时表示查询入向规则
        :type Filters: list of CommonFilter
        :param _StartTime: 检索的起始时间，可不传
        :type StartTime: str
        :param _EndTime: 检索的截止时间，可不传
        :type EndTime: str
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值，默认为asc
        :type Order: str
        :param _By: 排序所用到的字段，默认为sequence
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Index = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Index(self):
        """需要查询的索引，特定场景使用，可不填
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Filters(self):
        """过滤条件组合，Direction 为0时表述查询出向规则，为1时表示查询入向规则
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """检索的起始时间，可不传
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """检索的截止时间，可不传
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值，默认为asc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段，默认为sequence
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Index = params.get("Index")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatAcRuleResponse(AbstractModel):
    """DescribeNatAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Data: nat访问控制列表数据
        :type Data: list of DescAcItem
        :param _AllTotal: 未过滤的总条数
        :type AllTotal: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AllTotal = None
        self._RequestId = None

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """nat访问控制列表数据
        :rtype: list of DescAcItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AllTotal(self):
        """未过滤的总条数
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescAcItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AllTotal = params.get("AllTotal")
        self._RequestId = params.get("RequestId")


class DescribeNatFwDnatRuleRequest(AbstractModel):
    """DescribeNatFwDnatRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Index: 需要查询的索引，特定场景使用，可不填
        :type Index: str
        :param _Filters: 过滤条件组合
        :type Filters: list of CommonFilter
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _StartTime: 检索的起始时间，可不传
        :type StartTime: str
        :param _EndTime: 检索的截止时间，可不传
        :type EndTime: str
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值，可不传
        :type Order: str
        :param _By: 排序所用到的字段，可不传
        :type By: str
        """
        self._Index = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Index(self):
        """需要查询的索引，特定场景使用，可不填
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Filters(self):
        """过滤条件组合
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def StartTime(self):
        """检索的起始时间，可不传
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """检索的截止时间，可不传
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值，可不传
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段，可不传
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Index = params.get("Index")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatFwDnatRuleResponse(AbstractModel):
    """DescribeNatFwDnatRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: Dnat规则列表
        :type Data: list of DescNatDnatRule
        :param _Total: 列表总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        """Dnat规则列表
        :rtype: list of DescNatDnatRule
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
                obj = DescNatDnatRule()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeNatFwInfoCountRequest(AbstractModel):
    """DescribeNatFwInfoCount请求参数结构体

    """


class DescribeNatFwInfoCountResponse(AbstractModel):
    """DescribeNatFwInfoCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: 返回参数 success 成功 failed 失败
        :type ReturnMsg: str
        :param _NatFwInsCount: 当前租户的nat防火墙实例个数
        :type NatFwInsCount: int
        :param _SubnetCount: 当前租户接入防火墙的子网个数
        :type SubnetCount: int
        :param _OpenSwitchCount: 打开NAT防火墙开关个数
        :type OpenSwitchCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._NatFwInsCount = None
        self._SubnetCount = None
        self._OpenSwitchCount = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """返回参数 success 成功 failed 失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def NatFwInsCount(self):
        """当前租户的nat防火墙实例个数
        :rtype: int
        """
        return self._NatFwInsCount

    @NatFwInsCount.setter
    def NatFwInsCount(self, NatFwInsCount):
        self._NatFwInsCount = NatFwInsCount

    @property
    def SubnetCount(self):
        """当前租户接入防火墙的子网个数
        :rtype: int
        """
        return self._SubnetCount

    @SubnetCount.setter
    def SubnetCount(self, SubnetCount):
        self._SubnetCount = SubnetCount

    @property
    def OpenSwitchCount(self):
        """打开NAT防火墙开关个数
        :rtype: int
        """
        return self._OpenSwitchCount

    @OpenSwitchCount.setter
    def OpenSwitchCount(self, OpenSwitchCount):
        self._OpenSwitchCount = OpenSwitchCount

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
        self._ReturnMsg = params.get("ReturnMsg")
        self._NatFwInsCount = params.get("NatFwInsCount")
        self._SubnetCount = params.get("SubnetCount")
        self._OpenSwitchCount = params.get("OpenSwitchCount")
        self._RequestId = params.get("RequestId")


class DescribeNatFwInstanceRequest(AbstractModel):
    """DescribeNatFwInstance请求参数结构体

    """


class DescribeNatFwInstanceResponse(AbstractModel):
    """DescribeNatFwInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NatinsLst: 实例数组
        :type NatinsLst: list of NatFwInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NatinsLst = None
        self._RequestId = None

    @property
    def NatinsLst(self):
        """实例数组
        :rtype: list of NatFwInstance
        """
        return self._NatinsLst

    @NatinsLst.setter
    def NatinsLst(self, NatinsLst):
        self._NatinsLst = NatinsLst

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
        if params.get("NatinsLst") is not None:
            self._NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatFwInstance()
                obj._deserialize(item)
                self._NatinsLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNatFwInstanceWithRegionRequest(AbstractModel):
    """DescribeNatFwInstanceWithRegion请求参数结构体

    """


class DescribeNatFwInstanceWithRegionResponse(AbstractModel):
    """DescribeNatFwInstanceWithRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NatinsLst: 实例数组
        :type NatinsLst: list of NatFwInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NatinsLst = None
        self._RequestId = None

    @property
    def NatinsLst(self):
        """实例数组
        :rtype: list of NatFwInstance
        """
        return self._NatinsLst

    @NatinsLst.setter
    def NatinsLst(self, NatinsLst):
        self._NatinsLst = NatinsLst

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
        if params.get("NatinsLst") is not None:
            self._NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatFwInstance()
                obj._deserialize(item)
                self._NatinsLst.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNatFwInstancesInfoRequest(AbstractModel):
    """DescribeNatFwInstancesInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filter: 获取实例列表过滤字段
        :type Filter: list of NatFwFilter
        :param _Offset: 第几页
        :type Offset: int
        :param _Limit: 每页长度
        :type Limit: int
        """
        self._Filter = None
        self._Offset = None
        self._Limit = None

    @property
    def Filter(self):
        """获取实例列表过滤字段
        :rtype: list of NatFwFilter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Offset(self):
        """第几页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页长度
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = NatFwFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatFwInstancesInfoResponse(AbstractModel):
    """DescribeNatFwInstancesInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NatinsLst: 实例卡片信息数组
        :type NatinsLst: list of NatInstanceInfo
        :param _Total: nat 防火墙个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NatinsLst = None
        self._Total = None
        self._RequestId = None

    @property
    def NatinsLst(self):
        """实例卡片信息数组
        :rtype: list of NatInstanceInfo
        """
        return self._NatinsLst

    @NatinsLst.setter
    def NatinsLst(self, NatinsLst):
        self._NatinsLst = NatinsLst

    @property
    def Total(self):
        """nat 防火墙个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("NatinsLst") is not None:
            self._NatinsLst = []
            for item in params.get("NatinsLst"):
                obj = NatInstanceInfo()
                obj._deserialize(item)
                self._NatinsLst.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeNatFwVpcDnsLstRequest(AbstractModel):
    """DescribeNatFwVpcDnsLst请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatFwInsId: natfw 防火墙实例id
        :type NatFwInsId: str
        :param _NatInsIdFilter: natfw 过滤，以','分隔
        :type NatInsIdFilter: str
        :param _Offset: 分页页数
        :type Offset: int
        :param _Limit: 每页最多个数
        :type Limit: int
        """
        self._NatFwInsId = None
        self._NatInsIdFilter = None
        self._Offset = None
        self._Limit = None

    @property
    def NatFwInsId(self):
        """natfw 防火墙实例id
        :rtype: str
        """
        return self._NatFwInsId

    @NatFwInsId.setter
    def NatFwInsId(self, NatFwInsId):
        self._NatFwInsId = NatFwInsId

    @property
    def NatInsIdFilter(self):
        """natfw 过滤，以','分隔
        :rtype: str
        """
        return self._NatInsIdFilter

    @NatInsIdFilter.setter
    def NatInsIdFilter(self, NatInsIdFilter):
        self._NatInsIdFilter = NatInsIdFilter

    @property
    def Offset(self):
        """分页页数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页最多个数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._NatFwInsId = params.get("NatFwInsId")
        self._NatInsIdFilter = params.get("NatInsIdFilter")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatFwVpcDnsLstResponse(AbstractModel):
    """DescribeNatFwVpcDnsLst返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcDnsSwitchLst: nat防火墙vpc dns 信息数组
        :type VpcDnsSwitchLst: list of VpcDnsInfo
        :param _ReturnMsg: 返回参数 success成功 failed 失败
        :type ReturnMsg: str
        :param _Total: 开关总条数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VpcDnsSwitchLst = None
        self._ReturnMsg = None
        self._Total = None
        self._RequestId = None

    @property
    def VpcDnsSwitchLst(self):
        """nat防火墙vpc dns 信息数组
        :rtype: list of VpcDnsInfo
        """
        return self._VpcDnsSwitchLst

    @VpcDnsSwitchLst.setter
    def VpcDnsSwitchLst(self, VpcDnsSwitchLst):
        self._VpcDnsSwitchLst = VpcDnsSwitchLst

    @property
    def ReturnMsg(self):
        """返回参数 success成功 failed 失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def Total(self):
        """开关总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("VpcDnsSwitchLst") is not None:
            self._VpcDnsSwitchLst = []
            for item in params.get("VpcDnsSwitchLst"):
                obj = VpcDnsInfo()
                obj._deserialize(item)
                self._VpcDnsSwitchLst.append(obj)
        self._ReturnMsg = params.get("ReturnMsg")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeResourceGroupNewRequest(AbstractModel):
    """DescribeResourceGroupNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueryType: 查询类型 网络结构-vpc，业务识别-resource ，资源标签-tag
        :type QueryType: str
        :param _GroupId: 资产组id  全部传0
        :type GroupId: str
        :param _ShowType: all  包含子组 own自己
        :type ShowType: str
        """
        self._QueryType = None
        self._GroupId = None
        self._ShowType = None

    @property
    def QueryType(self):
        """查询类型 网络结构-vpc，业务识别-resource ，资源标签-tag
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def GroupId(self):
        """资产组id  全部传0
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ShowType(self):
        """all  包含子组 own自己
        :rtype: str
        """
        return self._ShowType

    @ShowType.setter
    def ShowType(self, ShowType):
        self._ShowType = ShowType


    def _deserialize(self, params):
        self._QueryType = params.get("QueryType")
        self._GroupId = params.get("GroupId")
        self._ShowType = params.get("ShowType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceGroupNewResponse(AbstractModel):
    """DescribeResourceGroupNew返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回树形结构
        :type Data: str
        :param _ReturnCode: 返回码；0为请求成功
        :type ReturnCode: int
        :param _ReturnMsg: 接口返回消息
        :type ReturnMsg: str
        :param _UnResourceNum: 未分类实例数量
        :type UnResourceNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._UnResourceNum = None
        self._RequestId = None

    @property
    def Data(self):
        """返回树形结构
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        """返回码；0为请求成功
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """接口返回消息
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def UnResourceNum(self):
        """未分类实例数量
        :rtype: int
        """
        return self._UnResourceNum

    @UnResourceNum.setter
    def UnResourceNum(self, UnResourceNum):
        self._UnResourceNum = UnResourceNum

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
        self._Data = params.get("Data")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._UnResourceNum = params.get("UnResourceNum")
        self._RequestId = params.get("RequestId")


class DescribeResourceGroupRequest(AbstractModel):
    """DescribeResourceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QueryType: 查询类型 网络结构 vpc，业务识别- resource ，资源标签-tag
        :type QueryType: str
        :param _GroupId: 资产组id  全部传0
        :type GroupId: str
        :param _ShowType: all  包含子组 own自己
        :type ShowType: str
        """
        self._QueryType = None
        self._GroupId = None
        self._ShowType = None

    @property
    def QueryType(self):
        """查询类型 网络结构 vpc，业务识别- resource ，资源标签-tag
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def GroupId(self):
        """资产组id  全部传0
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ShowType(self):
        """all  包含子组 own自己
        :rtype: str
        """
        return self._ShowType

    @ShowType.setter
    def ShowType(self, ShowType):
        self._ShowType = ShowType


    def _deserialize(self, params):
        self._QueryType = params.get("QueryType")
        self._GroupId = params.get("GroupId")
        self._ShowType = params.get("ShowType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceGroupResponse(AbstractModel):
    """DescribeResourceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回树形结构
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """返回树形结构
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeRuleOverviewRequest(AbstractModel):
    """DescribeRuleOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Direction: 方向，0：出站，1：入站
        :type Direction: int
        """
        self._Direction = None

    @property
    def Direction(self):
        """方向，0：出站，1：入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleOverviewResponse(AbstractModel):
    """DescribeRuleOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllTotal: 规则总数
        :type AllTotal: int
        :param _StrategyNum: 阻断策略规则数量
        :type StrategyNum: int
        :param _StartRuleNum: 启用规则数量
        :type StartRuleNum: int
        :param _StopRuleNum: 停用规则数量
        :type StopRuleNum: int
        :param _RemainingNum: 剩余配额
        :type RemainingNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllTotal = None
        self._StrategyNum = None
        self._StartRuleNum = None
        self._StopRuleNum = None
        self._RemainingNum = None
        self._RequestId = None

    @property
    def AllTotal(self):
        """规则总数
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def StrategyNum(self):
        """阻断策略规则数量
        :rtype: int
        """
        return self._StrategyNum

    @StrategyNum.setter
    def StrategyNum(self, StrategyNum):
        self._StrategyNum = StrategyNum

    @property
    def StartRuleNum(self):
        """启用规则数量
        :rtype: int
        """
        return self._StartRuleNum

    @StartRuleNum.setter
    def StartRuleNum(self, StartRuleNum):
        self._StartRuleNum = StartRuleNum

    @property
    def StopRuleNum(self):
        """停用规则数量
        :rtype: int
        """
        return self._StopRuleNum

    @StopRuleNum.setter
    def StopRuleNum(self, StopRuleNum):
        self._StopRuleNum = StopRuleNum

    @property
    def RemainingNum(self):
        """剩余配额
        :rtype: int
        """
        return self._RemainingNum

    @RemainingNum.setter
    def RemainingNum(self, RemainingNum):
        self._RemainingNum = RemainingNum

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
        self._AllTotal = params.get("AllTotal")
        self._StrategyNum = params.get("StrategyNum")
        self._StartRuleNum = params.get("StartRuleNum")
        self._StopRuleNum = params.get("StopRuleNum")
        self._RemainingNum = params.get("RemainingNum")
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupListRequest(AbstractModel):
    """DescribeSecurityGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Direction: 0: 出站规则，1：入站规则
        :type Direction: int
        :param _Area: 地域代码（例: ap-guangzhou),支持腾讯云全部地域
        :type Area: str
        :param _SearchValue: 搜索值
        :type SearchValue: str
        :param _Limit: 每页条数，默认为10
        :type Limit: int
        :param _Offset: 偏移值，默认为0
        :type Offset: int
        :param _Status: 状态，'': 全部，'0'：筛选停用规则，'1'：筛选启用规则
        :type Status: str
        :param _Filter: 0: 不过滤，1：过滤掉正常规则，保留下发异常规则
        :type Filter: int
        """
        self._Direction = None
        self._Area = None
        self._SearchValue = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._Filter = None

    @property
    def Direction(self):
        """0: 出站规则，1：入站规则
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Area(self):
        """地域代码（例: ap-guangzhou),支持腾讯云全部地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SearchValue(self):
        """搜索值
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Limit(self):
        """每页条数，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        """状态，'': 全部，'0'：筛选停用规则，'1'：筛选启用规则
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Filter(self):
        """0: 不过滤，1：过滤掉正常规则，保留下发异常规则
        :rtype: int
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._Area = params.get("Area")
        self._SearchValue = params.get("SearchValue")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupListResponse(AbstractModel):
    """DescribeSecurityGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 列表当前规则总条数
        :type Total: int
        :param _Data: 安全组规则列表数据
        :type Data: list of SecurityGroupListData
        :param _AllTotal: 不算筛选条数的总条数
        :type AllTotal: int
        :param _Enable: 访问控制规则全部启用/全部停用
        :type Enable: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AllTotal = None
        self._Enable = None
        self._RequestId = None

    @property
    def Total(self):
        """列表当前规则总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """安全组规则列表数据
        :rtype: list of SecurityGroupListData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AllTotal(self):
        """不算筛选条数的总条数
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def Enable(self):
        """访问控制规则全部启用/全部停用
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AllTotal = params.get("AllTotal")
        self._Enable = params.get("Enable")
        self._RequestId = params.get("RequestId")


class DescribeSourceAssetRequest(AbstractModel):
    """DescribeSourceAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChooseType: ChooseType为1，查询已经分组的资产；ChooseType不为1查询没有分组的资产
        :type ChooseType: str
        :param _FuzzySearch: 模糊查询
        :type FuzzySearch: str
        :param _InsType: 资产类型 1公网 2内网
        :type InsType: str
        :param _Limit: 查询单页的最大值；eg：10；则最多返回10条结果
        :type Limit: int
        :param _Offset: 查询结果的偏移量
        :type Offset: int
        :param _Zone: 地域
        :type Zone: str
        """
        self._ChooseType = None
        self._FuzzySearch = None
        self._InsType = None
        self._Limit = None
        self._Offset = None
        self._Zone = None

    @property
    def ChooseType(self):
        """ChooseType为1，查询已经分组的资产；ChooseType不为1查询没有分组的资产
        :rtype: str
        """
        return self._ChooseType

    @ChooseType.setter
    def ChooseType(self, ChooseType):
        self._ChooseType = ChooseType

    @property
    def FuzzySearch(self):
        """模糊查询
        :rtype: str
        """
        return self._FuzzySearch

    @FuzzySearch.setter
    def FuzzySearch(self, FuzzySearch):
        self._FuzzySearch = FuzzySearch

    @property
    def InsType(self):
        """资产类型 1公网 2内网
        :rtype: str
        """
        return self._InsType

    @InsType.setter
    def InsType(self, InsType):
        self._InsType = InsType

    @property
    def Limit(self):
        """查询单页的最大值；eg：10；则最多返回10条结果
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询结果的偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Zone(self):
        """地域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ChooseType = params.get("ChooseType")
        self._FuzzySearch = params.get("FuzzySearch")
        self._InsType = params.get("InsType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSourceAssetResponse(AbstractModel):
    """DescribeSourceAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据
        :type Data: list of InstanceInfo
        :param _Total: 返回数据总数
        :type Total: int
        :param _ZoneList: 地域集合
        :type ZoneList: list of AssetZone
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._ZoneList = None
        self._RequestId = None

    @property
    def Data(self):
        """数据
        :rtype: list of InstanceInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        """返回数据总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ZoneList(self):
        """地域集合
        :rtype: list of AssetZone
        """
        return self._ZoneList

    @ZoneList.setter
    def ZoneList(self, ZoneList):
        self._ZoneList = ZoneList

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
                obj = InstanceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        if params.get("ZoneList") is not None:
            self._ZoneList = []
            for item in params.get("ZoneList"):
                obj = AssetZone()
                obj._deserialize(item)
                self._ZoneList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSwitchListsRequest(AbstractModel):
    """DescribeSwitchLists请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 防火墙状态  0: 关闭，1：开启
        :type Status: int
        :param _Type: 资产类型 CVM/NAT/VPN/CLB/其它
        :type Type: str
        :param _Area: 地域 上海/重庆/广州，等等
        :type Area: str
        :param _SearchValue: 搜索值  例子："{"common":"106.54.189.45"}"
        :type SearchValue: str
        :param _Limit: 条数  默认值:10
        :type Limit: int
        :param _Offset: 偏移值 默认值: 0
        :type Offset: int
        :param _Order: 排序，desc：降序，asc：升序
        :type Order: str
        :param _By: 排序字段 PortTimes(风险端口数)
        :type By: str
        """
        self._Status = None
        self._Type = None
        self._Area = None
        self._SearchValue = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def Status(self):
        """防火墙状态  0: 关闭，1：开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        """资产类型 CVM/NAT/VPN/CLB/其它
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Area(self):
        """地域 上海/重庆/广州，等等
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SearchValue(self):
        """搜索值  例子："{"common":"106.54.189.45"}"
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Limit(self):
        """条数  默认值:10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值 默认值: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        """排序，desc：降序，asc：升序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序字段 PortTimes(风险端口数)
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._Area = params.get("Area")
        self._SearchValue = params.get("SearchValue")
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
        


class DescribeSwitchListsResponse(AbstractModel):
    """DescribeSwitchLists返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Data: 列表数据
        :type Data: list of SwitchListsData
        :param _AreaLists: 区域列表
        :type AreaLists: list of str
        :param _OnNum: 打开个数
        :type OnNum: int
        :param _OffNum: 关闭个数
        :type OffNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._AreaLists = None
        self._OnNum = None
        self._OffNum = None
        self._RequestId = None

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """列表数据
        :rtype: list of SwitchListsData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def AreaLists(self):
        """区域列表
        :rtype: list of str
        """
        return self._AreaLists

    @AreaLists.setter
    def AreaLists(self, AreaLists):
        self._AreaLists = AreaLists

    @property
    def OnNum(self):
        """打开个数
        :rtype: int
        """
        return self._OnNum

    @OnNum.setter
    def OnNum(self, OnNum):
        self._OnNum = OnNum

    @property
    def OffNum(self):
        """关闭个数
        :rtype: int
        """
        return self._OffNum

    @OffNum.setter
    def OffNum(self, OffNum):
        self._OffNum = OffNum

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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SwitchListsData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._AreaLists = params.get("AreaLists")
        self._OnNum = params.get("OnNum")
        self._OffNum = params.get("OffNum")
        self._RequestId = params.get("RequestId")


class DescribeTLogInfoRequest(AbstractModel):
    """DescribeTLogInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _QueryType: 类型 1 告警 2阻断
        :type QueryType: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _SearchValue: 查询条件
        :type SearchValue: str
        """
        self._EndTime = None
        self._QueryType = None
        self._StartTime = None
        self._SearchValue = None

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
    def QueryType(self):
        """类型 1 告警 2阻断
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

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
    def SearchValue(self):
        """查询条件
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._QueryType = params.get("QueryType")
        self._StartTime = params.get("StartTime")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogInfoResponse(AbstractModel):
    """DescribeTLogInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: "NetworkNum":网络扫描探测
 "HandleNum": 待处理事件
"BanNum": 
  "VulNum": 漏洞利用
  "OutNum": 失陷主机
"BruteForceNum": 0
        :type Data: :class:`tencentcloud.cfw.v20190904.models.TLogInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """"NetworkNum":网络扫描探测
 "HandleNum": 待处理事件
"BanNum": 
  "VulNum": 漏洞利用
  "OutNum": 失陷主机
"BruteForceNum": 0
        :rtype: :class:`tencentcloud.cfw.v20190904.models.TLogInfo`
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
            self._Data = TLogInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTLogIpListRequest(AbstractModel):
    """DescribeTLogIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _QueryType: 类型 1 告警 2阻断
        :type QueryType: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Top: top数
        :type Top: int
        :param _SearchValue: 查询条件
        :type SearchValue: str
        """
        self._EndTime = None
        self._QueryType = None
        self._StartTime = None
        self._Top = None
        self._SearchValue = None

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
    def QueryType(self):
        """类型 1 告警 2阻断
        :rtype: str
        """
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

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
    def Top(self):
        """top数
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def SearchValue(self):
        """查询条件
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._QueryType = params.get("QueryType")
        self._StartTime = params.get("StartTime")
        self._Top = params.get("Top")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTLogIpListResponse(AbstractModel):
    """DescribeTLogIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据集合
        :type Data: list of StaticInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """数据集合
        :rtype: list of StaticInfo
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
                obj = StaticInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTableStatusRequest(AbstractModel):
    """DescribeTableStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeId: EdgeId值两个vpc间的边id vpc填Edgeid，不要填Area；
        :type EdgeId: str
        :param _Status: 状态值，0：检查表的状态 确实只有一个默认值
        :type Status: int
        :param _Area: Nat所在地域 NAT填Area，不要填Edgeid；
        :type Area: str
        :param _Direction: 方向，0：出站，1：入站 默认值为 0
        :type Direction: int
        """
        self._EdgeId = None
        self._Status = None
        self._Area = None
        self._Direction = None

    @property
    def EdgeId(self):
        """EdgeId值两个vpc间的边id vpc填Edgeid，不要填Area；
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Status(self):
        """状态值，0：检查表的状态 确实只有一个默认值
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """Nat所在地域 NAT填Area，不要填Edgeid；
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """方向，0：出站，1：入站 默认值为 0
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTableStatusResponse(AbstractModel):
    """DescribeTableStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0：正常，其它：不正常
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0：正常，其它：不正常
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeUnHandleEventTabListRequest(AbstractModel):
    """DescribeUnHandleEventTabList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _AssetID: 查询示例ID
        :type AssetID: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AssetID = None

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
    def AssetID(self):
        """查询示例ID
        :rtype: str
        """
        return self._AssetID

    @AssetID.setter
    def AssetID(self, AssetID):
        self._AssetID = AssetID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AssetID = params.get("AssetID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnHandleEventTabListResponse(AbstractModel):
    """DescribeUnHandleEventTabList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 租户伪攻击链未处置事件
        :type Data: :class:`tencentcloud.cfw.v20190904.models.UnHandleEvent`
        :param _ReturnCode: 错误码，0成功 非0错误
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息 success成功
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
        """租户伪攻击链未处置事件
        :rtype: :class:`tencentcloud.cfw.v20190904.models.UnHandleEvent`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ReturnCode(self):
        """错误码，0成功 非0错误
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """返回信息 success成功
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
            self._Data = UnHandleEvent()
            self._Data._deserialize(params.get("Data"))
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class DescribeVpcAcRuleRequest(AbstractModel):
    """DescribeVpcAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Index: 需要查询的索引，特定场景使用，可不填
        :type Index: str
        :param _Filters: 过滤条件组合
        :type Filters: list of CommonFilter
        :param _StartTime: 检索的起始时间，可不传
        :type StartTime: str
        :param _EndTime: 检索的截止时间，可不传
        :type EndTime: str
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :type Order: str
        :param _By: 排序所用到的字段
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Index = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Index(self):
        """需要查询的索引，特定场景使用，可不填
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Filters(self):
        """过滤条件组合
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """检索的起始时间，可不传
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """检索的截止时间，可不传
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Index = params.get("Index")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAcRuleResponse(AbstractModel):
    """DescribeVpcAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总条数
        :type Total: int
        :param _Data: 内网间访问控制列表数据
        :type Data: list of VpcRuleItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        """内网间访问控制列表数据
        :rtype: list of VpcRuleItem
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
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VpcRuleItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcFwGroupSwitchRequest(AbstractModel):
    """DescribeVpcFwGroupSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页条数
        :type Limit: int
        :param _Offset: 偏移值
        :type Offset: int
        :param _Filters: 过滤条件组合
        :type Filters: list of CommonFilter
        :param _StartTime: 检索的起始时间，可不传
        :type StartTime: str
        :param _EndTime: 检索的截止时间，可不传
        :type EndTime: str
        :param _Order: desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :type Order: str
        :param _By: 排序所用到的字段
        :type By: str
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None
        self._Order = None
        self._By = None

    @property
    def Limit(self):
        """每页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移值
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """过滤条件组合
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        """检索的起始时间，可不传
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """检索的截止时间，可不传
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Order(self):
        """desc：降序；asc：升序。根据By字段的值进行排序，这里传参的话则By也必须有值
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        """排序所用到的字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcFwGroupSwitchResponse(AbstractModel):
    """DescribeVpcFwGroupSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SwitchList: 开关列表
        :type SwitchList: list of FwGroupSwitchShow
        :param _Total: 开关总个数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SwitchList = None
        self._Total = None
        self._RequestId = None

    @property
    def SwitchList(self):
        """开关列表
        :rtype: list of FwGroupSwitchShow
        """
        return self._SwitchList

    @SwitchList.setter
    def SwitchList(self, SwitchList):
        self._SwitchList = SwitchList

    @property
    def Total(self):
        """开关总个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("SwitchList") is not None:
            self._SwitchList = []
            for item in params.get("SwitchList"):
                obj = FwGroupSwitchShow()
                obj._deserialize(item)
                self._SwitchList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DnsVpcSwitch(AbstractModel):
    """设置nat防火墙的vpc dns 接入开关

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
        :type VpcId: str
        :param _Status: 0：设置为关闭 1:设置为打开
        :type Status: int
        """
        self._VpcId = None
        self._Status = None

    @property
    def VpcId(self):
        """vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Status(self):
        """0：设置为关闭 1:设置为打开
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeIpInfo(AbstractModel):
    """边界防火墙公网IP开关列表

    """

    def __init__(self):
        r"""
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _PublicIpType: 公网 IP 类型 1 公网,2 弹性,3 弹性ipv6,4 anycastIP, 6 HighQualityEIP
        :type PublicIpType: int
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _IntranetIp: 内网IP
        :type IntranetIp: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _Region: 地域
        :type Region: str
        :param _PortRiskCount: 风险端口数
        :type PortRiskCount: int
        :param _LastScanTime: 最近扫描时间
        :type LastScanTime: str
        :param _IsRegionEip: 是否为region eip
0 不为region eip，不能选择串行
1 为region eip 可以选择串行
        :type IsRegionEip: int
        :param _VpcId: EIP 所关联的VPC
        :type VpcId: str
        :param _IsSerialRegion: 0: 该地域暂未支持串行
1: 该用户未在该地域配置串行带宽
2: 该用户已在该地域配置串行带宽，可以开启串行开关
        :type IsSerialRegion: int
        :param _IsPublicClb: 0: 不是公网CLB 可以开启串行开关
1: 是公网CLB 不可以开启串行开关

        :type IsPublicClb: int
        :param _EndpointBindEipNum: 0: 开启开关时提示要创建私有连接。
1: 关闭该开关是提示删除私有连接。
如果大于 1: 关闭开关 、开启开关不需提示创建删除私有连接。
        :type EndpointBindEipNum: int
        :param _ScanMode: 扫描深度
        :type ScanMode: str
        :param _ScanStatus: 扫描状态
        :type ScanStatus: int
        :param _Status: 开关状态
0 : 关闭
1 : 开启
2 : 开启中
3 : 关闭中
4 : 异常
        :type Status: int
        :param _EndpointId: 私有连接ID
        :type EndpointId: str
        :param _EndpointIp: 私有连接IP
        :type EndpointIp: str
        :param _SwitchMode: 0 : 旁路
1 : 串行
2 : 正在模式切换
        :type SwitchMode: int
        :param _SwitchWeight: 开关权重
        :type SwitchWeight: int
        :param _Domain: 域名化CLB的域名
        :type Domain: str
        :param _OverUsedStatus: IP超量状态
        :type OverUsedStatus: int
        """
        self._PublicIp = None
        self._PublicIpType = None
        self._InstanceId = None
        self._InstanceName = None
        self._IntranetIp = None
        self._AssetType = None
        self._Region = None
        self._PortRiskCount = None
        self._LastScanTime = None
        self._IsRegionEip = None
        self._VpcId = None
        self._IsSerialRegion = None
        self._IsPublicClb = None
        self._EndpointBindEipNum = None
        self._ScanMode = None
        self._ScanStatus = None
        self._Status = None
        self._EndpointId = None
        self._EndpointIp = None
        self._SwitchMode = None
        self._SwitchWeight = None
        self._Domain = None
        self._OverUsedStatus = None

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
    def PublicIpType(self):
        """公网 IP 类型 1 公网,2 弹性,3 弹性ipv6,4 anycastIP, 6 HighQualityEIP
        :rtype: int
        """
        return self._PublicIpType

    @PublicIpType.setter
    def PublicIpType(self, PublicIpType):
        self._PublicIpType = PublicIpType

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
    def InstanceName(self):
        """实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def IntranetIp(self):
        """内网IP
        :rtype: str
        """
        return self._IntranetIp

    @IntranetIp.setter
    def IntranetIp(self, IntranetIp):
        self._IntranetIp = IntranetIp

    @property
    def AssetType(self):
        """资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PortRiskCount(self):
        """风险端口数
        :rtype: int
        """
        return self._PortRiskCount

    @PortRiskCount.setter
    def PortRiskCount(self, PortRiskCount):
        self._PortRiskCount = PortRiskCount

    @property
    def LastScanTime(self):
        """最近扫描时间
        :rtype: str
        """
        return self._LastScanTime

    @LastScanTime.setter
    def LastScanTime(self, LastScanTime):
        self._LastScanTime = LastScanTime

    @property
    def IsRegionEip(self):
        """是否为region eip
0 不为region eip，不能选择串行
1 为region eip 可以选择串行
        :rtype: int
        """
        return self._IsRegionEip

    @IsRegionEip.setter
    def IsRegionEip(self, IsRegionEip):
        self._IsRegionEip = IsRegionEip

    @property
    def VpcId(self):
        """EIP 所关联的VPC
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IsSerialRegion(self):
        """0: 该地域暂未支持串行
1: 该用户未在该地域配置串行带宽
2: 该用户已在该地域配置串行带宽，可以开启串行开关
        :rtype: int
        """
        return self._IsSerialRegion

    @IsSerialRegion.setter
    def IsSerialRegion(self, IsSerialRegion):
        self._IsSerialRegion = IsSerialRegion

    @property
    def IsPublicClb(self):
        """0: 不是公网CLB 可以开启串行开关
1: 是公网CLB 不可以开启串行开关

        :rtype: int
        """
        return self._IsPublicClb

    @IsPublicClb.setter
    def IsPublicClb(self, IsPublicClb):
        self._IsPublicClb = IsPublicClb

    @property
    def EndpointBindEipNum(self):
        """0: 开启开关时提示要创建私有连接。
1: 关闭该开关是提示删除私有连接。
如果大于 1: 关闭开关 、开启开关不需提示创建删除私有连接。
        :rtype: int
        """
        return self._EndpointBindEipNum

    @EndpointBindEipNum.setter
    def EndpointBindEipNum(self, EndpointBindEipNum):
        self._EndpointBindEipNum = EndpointBindEipNum

    @property
    def ScanMode(self):
        """扫描深度
        :rtype: str
        """
        return self._ScanMode

    @ScanMode.setter
    def ScanMode(self, ScanMode):
        self._ScanMode = ScanMode

    @property
    def ScanStatus(self):
        """扫描状态
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def Status(self):
        """开关状态
0 : 关闭
1 : 开启
2 : 开启中
3 : 关闭中
4 : 异常
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EndpointId(self):
        """私有连接ID
        :rtype: str
        """
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def EndpointIp(self):
        """私有连接IP
        :rtype: str
        """
        return self._EndpointIp

    @EndpointIp.setter
    def EndpointIp(self, EndpointIp):
        self._EndpointIp = EndpointIp

    @property
    def SwitchMode(self):
        """0 : 旁路
1 : 串行
2 : 正在模式切换
        :rtype: int
        """
        return self._SwitchMode

    @SwitchMode.setter
    def SwitchMode(self, SwitchMode):
        self._SwitchMode = SwitchMode

    @property
    def SwitchWeight(self):
        """开关权重
        :rtype: int
        """
        return self._SwitchWeight

    @SwitchWeight.setter
    def SwitchWeight(self, SwitchWeight):
        self._SwitchWeight = SwitchWeight

    @property
    def Domain(self):
        """域名化CLB的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def OverUsedStatus(self):
        """IP超量状态
        :rtype: int
        """
        return self._OverUsedStatus

    @OverUsedStatus.setter
    def OverUsedStatus(self, OverUsedStatus):
        self._OverUsedStatus = OverUsedStatus


    def _deserialize(self, params):
        self._PublicIp = params.get("PublicIp")
        self._PublicIpType = params.get("PublicIpType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._IntranetIp = params.get("IntranetIp")
        self._AssetType = params.get("AssetType")
        self._Region = params.get("Region")
        self._PortRiskCount = params.get("PortRiskCount")
        self._LastScanTime = params.get("LastScanTime")
        self._IsRegionEip = params.get("IsRegionEip")
        self._VpcId = params.get("VpcId")
        self._IsSerialRegion = params.get("IsSerialRegion")
        self._IsPublicClb = params.get("IsPublicClb")
        self._EndpointBindEipNum = params.get("EndpointBindEipNum")
        self._ScanMode = params.get("ScanMode")
        self._ScanStatus = params.get("ScanStatus")
        self._Status = params.get("Status")
        self._EndpointId = params.get("EndpointId")
        self._EndpointIp = params.get("EndpointIp")
        self._SwitchMode = params.get("SwitchMode")
        self._SwitchWeight = params.get("SwitchWeight")
        self._Domain = params.get("Domain")
        self._OverUsedStatus = params.get("OverUsedStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeIpSwitch(AbstractModel):
    """开启、关闭 防火墙互联网边界开关

    """

    def __init__(self):
        r"""
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _SubnetId: vpc 中第一个EIP开关打开，需要指定子网创建私有连接
        :type SubnetId: str
        :param _EndpointIp: 创建私有连接指定IP
        :type EndpointIp: str
        :param _SwitchMode: 0 : 旁路 1 : 串行
        :type SwitchMode: int
        """
        self._PublicIp = None
        self._SubnetId = None
        self._EndpointIp = None
        self._SwitchMode = None

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
    def SubnetId(self):
        """vpc 中第一个EIP开关打开，需要指定子网创建私有连接
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EndpointIp(self):
        """创建私有连接指定IP
        :rtype: str
        """
        return self._EndpointIp

    @EndpointIp.setter
    def EndpointIp(self, EndpointIp):
        self._EndpointIp = EndpointIp

    @property
    def SwitchMode(self):
        """0 : 旁路 1 : 串行
        :rtype: int
        """
        return self._SwitchMode

    @SwitchMode.setter
    def SwitchMode(self, SwitchMode):
        self._SwitchMode = SwitchMode


    def _deserialize(self, params):
        self._PublicIp = params.get("PublicIp")
        self._SubnetId = params.get("SubnetId")
        self._EndpointIp = params.get("EndpointIp")
        self._SwitchMode = params.get("SwitchMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterpriseSecurityGroupRuleBetaInfo(AbstractModel):
    """企业安全组自动化任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: int
        :param _TaskName: 任务名称
        :type TaskName: str
        :param _LastTime: 时间
        :type LastTime: str
        """
        self._TaskId = None
        self._TaskName = None
        self._LastTime = None

    @property
    def TaskId(self):
        """任务id
        :rtype: int
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
    def LastTime(self):
        """时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._LastTime = params.get("LastTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnterpriseSecurityGroupRuleRuleInfo(AbstractModel):
    """企业安全组规则列表信息

    """

    def __init__(self):
        r"""
        :param _OrderIndex: 排序
        :type OrderIndex: int
        :param _RuleUuid: 主键id
        :type RuleUuid: int
        :param _Uuid: 规则uuid
        :type Uuid: str
        :param _SourceId: 源规则内容
        :type SourceId: str
        :param _SourceType: 源规则类型 
取值范围 0/1/2/3/4/5/6/7/8/9/100
0表示ip(net),
1表示VPC实例(instance)
2表示子网实例(instance)
3表示CVM实例(instance)
4表示CLB实例(instance)
5表示ENI实例(instance)
6表示数据库实例(instance)
7表示模板(template)
8表示标签(tag)
9表示地域(region)
100表示资产分组(resourcegroup)
        :type SourceType: int
        :param _TargetId: 目的规则内容
        :type TargetId: str
        :param _TargetType: 目的规则类型 
取值范围 0/1/2/3/4/5/6/7/8/9/100
0表示ip(net),
1表示VPC实例(instance)
2表示子网实例(instance)
3表示CVM实例(instance)
4表示CLB实例(instance)
5表示ENI实例(instance)
6表示数据库实例(instance)
7表示模板(template)
8表示标签(tag)
9表示地域(region)
100表示资产分组(resourcegroup)
        :type TargetType: int
        :param _Protocol: 协议名称
取值范围:TCP/ANY/ICMP/UDP
ANY:表示所有

        :type Protocol: str
        :param _Port: 端口
        :type Port: str
        :param _Strategy: 规则策略
取值范围:1/2
1:阻断
2:放行
        :type Strategy: int
        :param _Status: 规则启用状态 
取值范围： 0/1
0:未开启
1:开启
        :type Status: int
        :param _Detail: 描述
        :type Detail: str
        :param _AclTags: 标签
        :type AclTags: str
        :param _IsNew: 规则最新一次是否有改动
取值范围：0/1
0:否
1:是
        :type IsNew: int
        :param _Region: 地域
        :type Region: str
        :param _IsDelay: 是否延迟下发规则 
取值范围：0/1
0:立即下发 1:延迟下发
        :type IsDelay: int
        :param _ServiceTemplateId: 服务模板id
        :type ServiceTemplateId: str
        :param _SouInstanceName: 源资产名称
        :type SouInstanceName: str
        :param _SouPublicIp: 源资产公网ip
        :type SouPublicIp: str
        :param _SouPrivateIp: 源资产内网ip
        :type SouPrivateIp: str
        :param _SouCidr: 源资产网段信息
        :type SouCidr: str
        :param _SouParameterName: 源模板名称
        :type SouParameterName: str
        :param _InstanceName: 目的资产名称
        :type InstanceName: str
        :param _PublicIp: 目的资产公网ip
        :type PublicIp: str
        :param _PrivateIp: 目的资产内网ip
        :type PrivateIp: str
        :param _Cidr: 目的资产网段信息
        :type Cidr: str
        :param _ParameterName: 目的模板名称
        :type ParameterName: str
        :param _ProtocolPortName: 端口模板名称
        :type ProtocolPortName: str
        :param _BetaList: 自动化任务信息
        :type BetaList: list of EnterpriseSecurityGroupRuleBetaInfo
        :param _Id: 规则id  等同RuleUuid
        :type Id: int
        :param _DnsParseCount: 域名解析的IP统计
        :type DnsParseCount: :class:`tencentcloud.cfw.v20190904.models.SgDnsParseCount`
        """
        self._OrderIndex = None
        self._RuleUuid = None
        self._Uuid = None
        self._SourceId = None
        self._SourceType = None
        self._TargetId = None
        self._TargetType = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Status = None
        self._Detail = None
        self._AclTags = None
        self._IsNew = None
        self._Region = None
        self._IsDelay = None
        self._ServiceTemplateId = None
        self._SouInstanceName = None
        self._SouPublicIp = None
        self._SouPrivateIp = None
        self._SouCidr = None
        self._SouParameterName = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cidr = None
        self._ParameterName = None
        self._ProtocolPortName = None
        self._BetaList = None
        self._Id = None
        self._DnsParseCount = None

    @property
    def OrderIndex(self):
        """排序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def RuleUuid(self):
        """主键id
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def Uuid(self):
        """规则uuid
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def SourceId(self):
        """源规则内容
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceType(self):
        """源规则类型 
取值范围 0/1/2/3/4/5/6/7/8/9/100
0表示ip(net),
1表示VPC实例(instance)
2表示子网实例(instance)
3表示CVM实例(instance)
4表示CLB实例(instance)
5表示ENI实例(instance)
6表示数据库实例(instance)
7表示模板(template)
8表示标签(tag)
9表示地域(region)
100表示资产分组(resourcegroup)
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetId(self):
        """目的规则内容
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        """目的规则类型 
取值范围 0/1/2/3/4/5/6/7/8/9/100
0表示ip(net),
1表示VPC实例(instance)
2表示子网实例(instance)
3表示CVM实例(instance)
4表示CLB实例(instance)
5表示ENI实例(instance)
6表示数据库实例(instance)
7表示模板(template)
8表示标签(tag)
9表示地域(region)
100表示资产分组(resourcegroup)
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        """协议名称
取值范围:TCP/ANY/ICMP/UDP
ANY:表示所有

        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        """规则策略
取值范围:1/2
1:阻断
2:放行
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Status(self):
        """规则启用状态 
取值范围： 0/1
0:未开启
1:开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Detail(self):
        """描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def AclTags(self):
        """标签
        :rtype: str
        """
        return self._AclTags

    @AclTags.setter
    def AclTags(self, AclTags):
        self._AclTags = AclTags

    @property
    def IsNew(self):
        """规则最新一次是否有改动
取值范围：0/1
0:否
1:是
        :rtype: int
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IsDelay(self):
        """是否延迟下发规则 
取值范围：0/1
0:立即下发 1:延迟下发
        :rtype: int
        """
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

    @property
    def ServiceTemplateId(self):
        """服务模板id
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def SouInstanceName(self):
        """源资产名称
        :rtype: str
        """
        return self._SouInstanceName

    @SouInstanceName.setter
    def SouInstanceName(self, SouInstanceName):
        self._SouInstanceName = SouInstanceName

    @property
    def SouPublicIp(self):
        """源资产公网ip
        :rtype: str
        """
        return self._SouPublicIp

    @SouPublicIp.setter
    def SouPublicIp(self, SouPublicIp):
        self._SouPublicIp = SouPublicIp

    @property
    def SouPrivateIp(self):
        """源资产内网ip
        :rtype: str
        """
        return self._SouPrivateIp

    @SouPrivateIp.setter
    def SouPrivateIp(self, SouPrivateIp):
        self._SouPrivateIp = SouPrivateIp

    @property
    def SouCidr(self):
        """源资产网段信息
        :rtype: str
        """
        return self._SouCidr

    @SouCidr.setter
    def SouCidr(self, SouCidr):
        self._SouCidr = SouCidr

    @property
    def SouParameterName(self):
        """源模板名称
        :rtype: str
        """
        return self._SouParameterName

    @SouParameterName.setter
    def SouParameterName(self, SouParameterName):
        self._SouParameterName = SouParameterName

    @property
    def InstanceName(self):
        """目的资产名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        """目的资产公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """目的资产内网ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cidr(self):
        """目的资产网段信息
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def ParameterName(self):
        """目的模板名称
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ProtocolPortName(self):
        """端口模板名称
        :rtype: str
        """
        return self._ProtocolPortName

    @ProtocolPortName.setter
    def ProtocolPortName(self, ProtocolPortName):
        self._ProtocolPortName = ProtocolPortName

    @property
    def BetaList(self):
        """自动化任务信息
        :rtype: list of EnterpriseSecurityGroupRuleBetaInfo
        """
        return self._BetaList

    @BetaList.setter
    def BetaList(self, BetaList):
        self._BetaList = BetaList

    @property
    def Id(self):
        """规则id  等同RuleUuid
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DnsParseCount(self):
        """域名解析的IP统计
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SgDnsParseCount`
        """
        return self._DnsParseCount

    @DnsParseCount.setter
    def DnsParseCount(self, DnsParseCount):
        self._DnsParseCount = DnsParseCount


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._RuleUuid = params.get("RuleUuid")
        self._Uuid = params.get("Uuid")
        self._SourceId = params.get("SourceId")
        self._SourceType = params.get("SourceType")
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Status = params.get("Status")
        self._Detail = params.get("Detail")
        self._AclTags = params.get("AclTags")
        self._IsNew = params.get("IsNew")
        self._Region = params.get("Region")
        self._IsDelay = params.get("IsDelay")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._SouInstanceName = params.get("SouInstanceName")
        self._SouPublicIp = params.get("SouPublicIp")
        self._SouPrivateIp = params.get("SouPrivateIp")
        self._SouCidr = params.get("SouCidr")
        self._SouParameterName = params.get("SouParameterName")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cidr = params.get("Cidr")
        self._ParameterName = params.get("ParameterName")
        self._ProtocolPortName = params.get("ProtocolPortName")
        if params.get("BetaList") is not None:
            self._BetaList = []
            for item in params.get("BetaList"):
                obj = EnterpriseSecurityGroupRuleBetaInfo()
                obj._deserialize(item)
                self._BetaList.append(obj)
        self._Id = params.get("Id")
        if params.get("DnsParseCount") is not None:
            self._DnsParseCount = SgDnsParseCount()
            self._DnsParseCount._deserialize(params.get("DnsParseCount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCfwVerticalRequest(AbstractModel):
    """ExpandCfwVertical请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FwType: nat：nat防火墙，ew：东西向防火墙
        :type FwType: str
        :param _Width: 带宽值
        :type Width: int
        :param _CfwInstance: 防火墙实例id
        :type CfwInstance: str
        :param _ElasticSwitch: 弹性开关 1打开 0 关闭
        :type ElasticSwitch: int
        :param _ElasticBandwidth: 弹性带宽上限，单位Mbps
        :type ElasticBandwidth: int
        :param _Tags: 按量计费标签
        :type Tags: list of TagInfo
        """
        self._FwType = None
        self._Width = None
        self._CfwInstance = None
        self._ElasticSwitch = None
        self._ElasticBandwidth = None
        self._Tags = None

    @property
    def FwType(self):
        """nat：nat防火墙，ew：东西向防火墙
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def Width(self):
        """带宽值
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def CfwInstance(self):
        """防火墙实例id
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance

    @property
    def ElasticSwitch(self):
        """弹性开关 1打开 0 关闭
        :rtype: int
        """
        return self._ElasticSwitch

    @ElasticSwitch.setter
    def ElasticSwitch(self, ElasticSwitch):
        self._ElasticSwitch = ElasticSwitch

    @property
    def ElasticBandwidth(self):
        """弹性带宽上限，单位Mbps
        :rtype: int
        """
        return self._ElasticBandwidth

    @ElasticBandwidth.setter
    def ElasticBandwidth(self, ElasticBandwidth):
        self._ElasticBandwidth = ElasticBandwidth

    @property
    def Tags(self):
        """按量计费标签
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._FwType = params.get("FwType")
        self._Width = params.get("Width")
        self._CfwInstance = params.get("CfwInstance")
        self._ElasticSwitch = params.get("ElasticSwitch")
        self._ElasticBandwidth = params.get("ElasticBandwidth")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpandCfwVerticalResponse(AbstractModel):
    """ExpandCfwVertical返回参数结构体

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


class FwCidrInfo(AbstractModel):
    """防火墙网段信息

    """

    def __init__(self):
        r"""
        :param _FwCidrType: 防火墙使用的网段类型，值VpcSelf/Assis/Custom分别代表自有网段优先/扩展网段优先/自定义
        :type FwCidrType: str
        :param _FwCidrLst: 为每个vpc指定防火墙的网段
        :type FwCidrLst: list of FwVpcCidr
        :param _ComFwCidr: 其他防火墙占用网段，一般是防火墙需要独占vpc时指定的网段
        :type ComFwCidr: str
        """
        self._FwCidrType = None
        self._FwCidrLst = None
        self._ComFwCidr = None

    @property
    def FwCidrType(self):
        """防火墙使用的网段类型，值VpcSelf/Assis/Custom分别代表自有网段优先/扩展网段优先/自定义
        :rtype: str
        """
        return self._FwCidrType

    @FwCidrType.setter
    def FwCidrType(self, FwCidrType):
        self._FwCidrType = FwCidrType

    @property
    def FwCidrLst(self):
        """为每个vpc指定防火墙的网段
        :rtype: list of FwVpcCidr
        """
        return self._FwCidrLst

    @FwCidrLst.setter
    def FwCidrLst(self, FwCidrLst):
        self._FwCidrLst = FwCidrLst

    @property
    def ComFwCidr(self):
        """其他防火墙占用网段，一般是防火墙需要独占vpc时指定的网段
        :rtype: str
        """
        return self._ComFwCidr

    @ComFwCidr.setter
    def ComFwCidr(self, ComFwCidr):
        self._ComFwCidr = ComFwCidr


    def _deserialize(self, params):
        self._FwCidrType = params.get("FwCidrType")
        if params.get("FwCidrLst") is not None:
            self._FwCidrLst = []
            for item in params.get("FwCidrLst"):
                obj = FwVpcCidr()
                obj._deserialize(item)
                self._FwCidrLst.append(obj)
        self._ComFwCidr = params.get("ComFwCidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FwDeploy(AbstractModel):
    """防火墙部署输入参数列表

    """

    def __init__(self):
        r"""
        :param _DeployRegion: 防火墙部署地域
        :type DeployRegion: str
        :param _Width: 带宽，单位：Mbps
        :type Width: int
        :param _CrossAZone: 异地灾备 1：使用异地灾备；0：不使用异地灾备；为空则默认不使用异地灾备
        :type CrossAZone: int
        :param _Zone: 主可用区，为空则选择默认可用区
        :type Zone: str
        :param _ZoneBak: 备可用区，为空则选择默认可用区
        :type ZoneBak: str
        :param _CdcId: 若为cdc防火墙时填充该id
        :type CdcId: str
        """
        self._DeployRegion = None
        self._Width = None
        self._CrossAZone = None
        self._Zone = None
        self._ZoneBak = None
        self._CdcId = None

    @property
    def DeployRegion(self):
        """防火墙部署地域
        :rtype: str
        """
        return self._DeployRegion

    @DeployRegion.setter
    def DeployRegion(self, DeployRegion):
        self._DeployRegion = DeployRegion

    @property
    def Width(self):
        """带宽，单位：Mbps
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def CrossAZone(self):
        """异地灾备 1：使用异地灾备；0：不使用异地灾备；为空则默认不使用异地灾备
        :rtype: int
        """
        return self._CrossAZone

    @CrossAZone.setter
    def CrossAZone(self, CrossAZone):
        self._CrossAZone = CrossAZone

    @property
    def Zone(self):
        """主可用区，为空则选择默认可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneBak(self):
        """备可用区，为空则选择默认可用区
        :rtype: str
        """
        return self._ZoneBak

    @ZoneBak.setter
    def ZoneBak(self, ZoneBak):
        self._ZoneBak = ZoneBak

    @property
    def CdcId(self):
        """若为cdc防火墙时填充该id
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._DeployRegion = params.get("DeployRegion")
        self._Width = params.get("Width")
        self._CrossAZone = params.get("CrossAZone")
        self._Zone = params.get("Zone")
        self._ZoneBak = params.get("ZoneBak")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FwGateway(AbstractModel):
    """防火墙引流网关信息

    """

    def __init__(self):
        r"""
        :param _GatewayId: 防火墙网关id
        :type GatewayId: str
        :param _VpcId: 网关所属vpc id
        :type VpcId: str
        :param _IpAddress: 网关ip地址
        :type IpAddress: str
        """
        self._GatewayId = None
        self._VpcId = None
        self._IpAddress = None

    @property
    def GatewayId(self):
        """防火墙网关id
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def VpcId(self):
        """网关所属vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IpAddress(self):
        """网关ip地址
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._VpcId = params.get("VpcId")
        self._IpAddress = params.get("IpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FwGroupSwitch(AbstractModel):
    """多种VPC墙模式开关结构

    """

    def __init__(self):
        r"""
        :param _SwitchMode: 防火墙实例的开关模式 1: 单点互通 2: 多点互通 3: 全互通 4: 自定义路由
        :type SwitchMode: int
        :param _SwitchId: 防火墙开关ID
支持三种类型
1. 边开关(单点互通)
2. 点开关(多点互通)
3. 全开关(全互通)
        :type SwitchId: str
        """
        self._SwitchMode = None
        self._SwitchId = None

    @property
    def SwitchMode(self):
        """防火墙实例的开关模式 1: 单点互通 2: 多点互通 3: 全互通 4: 自定义路由
        :rtype: int
        """
        return self._SwitchMode

    @SwitchMode.setter
    def SwitchMode(self, SwitchMode):
        self._SwitchMode = SwitchMode

    @property
    def SwitchId(self):
        """防火墙开关ID
支持三种类型
1. 边开关(单点互通)
2. 点开关(多点互通)
3. 全开关(全互通)
        :rtype: str
        """
        return self._SwitchId

    @SwitchId.setter
    def SwitchId(self, SwitchId):
        self._SwitchId = SwitchId


    def _deserialize(self, params):
        self._SwitchMode = params.get("SwitchMode")
        self._SwitchId = params.get("SwitchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FwGroupSwitchShow(AbstractModel):
    """VPC防火墙(组)四种开关展示

    """

    def __init__(self):
        r"""
        :param _SwitchId: 防火墙开关ID
        :type SwitchId: str
        :param _SwitchName: 防火墙开关NAME
        :type SwitchName: str
        :param _SwitchMode: 互通模式
        :type SwitchMode: int
        :param _ConnectType: 开关边连接类型 0：对等连接， 1：云连网
        :type ConnectType: int
        :param _ConnectId: 连接ID
        :type ConnectId: str
        :param _ConnectName: 连接名称
        :type ConnectName: str
        :param _SrcInstancesInfo: 源实例信息
        :type SrcInstancesInfo: list of NetInstancesInfo
        :param _DstInstancesInfo: 目的实例信息
        :type DstInstancesInfo: list of NetInstancesInfo
        :param _FwGroupId: 防火墙(组)数据
        :type FwGroupId: str
        :param _FwGroupName: 防火墙(组)名称
        :type FwGroupName: str
        :param _Enable: 开关状态 0：关 ， 1：开
        :type Enable: int
        :param _Status: 开关的状态 0：正常， 1：转换中
        :type Status: int
        :param _AttachWithEdge: 0-非sase实例，忽略，1-未绑定状态，2-已绑定
        :type AttachWithEdge: int
        :param _CrossEdgeStatus: 对等防火墙和开关状态 0：正常， 1：对等未创建防火墙，2：对等已创建防火墙，未打开开关
        :type CrossEdgeStatus: int
        :param _FwInsRegion: 网络经过VPC防火墙CVM所在地域
        :type FwInsRegion: list of str
        :param _IpsAction: 0 观察 1 拦截 2 严格 3 关闭 4 不支持ips 前端展示tag
        :type IpsAction: int
        :param _FwInsLst: 开关关联的防火墙实例列表
        :type FwInsLst: list of VpcFwInstanceShow
        :param _BypassStatus: 开关是否处于bypass状态
0：正常状态
1：bypass状态
        :type BypassStatus: int
        :param _IpVersion: 0: ipv4 , 1:ipv6
        :type IpVersion: int
        """
        self._SwitchId = None
        self._SwitchName = None
        self._SwitchMode = None
        self._ConnectType = None
        self._ConnectId = None
        self._ConnectName = None
        self._SrcInstancesInfo = None
        self._DstInstancesInfo = None
        self._FwGroupId = None
        self._FwGroupName = None
        self._Enable = None
        self._Status = None
        self._AttachWithEdge = None
        self._CrossEdgeStatus = None
        self._FwInsRegion = None
        self._IpsAction = None
        self._FwInsLst = None
        self._BypassStatus = None
        self._IpVersion = None

    @property
    def SwitchId(self):
        """防火墙开关ID
        :rtype: str
        """
        return self._SwitchId

    @SwitchId.setter
    def SwitchId(self, SwitchId):
        self._SwitchId = SwitchId

    @property
    def SwitchName(self):
        """防火墙开关NAME
        :rtype: str
        """
        return self._SwitchName

    @SwitchName.setter
    def SwitchName(self, SwitchName):
        self._SwitchName = SwitchName

    @property
    def SwitchMode(self):
        """互通模式
        :rtype: int
        """
        return self._SwitchMode

    @SwitchMode.setter
    def SwitchMode(self, SwitchMode):
        self._SwitchMode = SwitchMode

    @property
    def ConnectType(self):
        """开关边连接类型 0：对等连接， 1：云连网
        :rtype: int
        """
        return self._ConnectType

    @ConnectType.setter
    def ConnectType(self, ConnectType):
        self._ConnectType = ConnectType

    @property
    def ConnectId(self):
        """连接ID
        :rtype: str
        """
        return self._ConnectId

    @ConnectId.setter
    def ConnectId(self, ConnectId):
        self._ConnectId = ConnectId

    @property
    def ConnectName(self):
        """连接名称
        :rtype: str
        """
        return self._ConnectName

    @ConnectName.setter
    def ConnectName(self, ConnectName):
        self._ConnectName = ConnectName

    @property
    def SrcInstancesInfo(self):
        """源实例信息
        :rtype: list of NetInstancesInfo
        """
        return self._SrcInstancesInfo

    @SrcInstancesInfo.setter
    def SrcInstancesInfo(self, SrcInstancesInfo):
        self._SrcInstancesInfo = SrcInstancesInfo

    @property
    def DstInstancesInfo(self):
        """目的实例信息
        :rtype: list of NetInstancesInfo
        """
        return self._DstInstancesInfo

    @DstInstancesInfo.setter
    def DstInstancesInfo(self, DstInstancesInfo):
        self._DstInstancesInfo = DstInstancesInfo

    @property
    def FwGroupId(self):
        """防火墙(组)数据
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def FwGroupName(self):
        """防火墙(组)名称
        :rtype: str
        """
        return self._FwGroupName

    @FwGroupName.setter
    def FwGroupName(self, FwGroupName):
        self._FwGroupName = FwGroupName

    @property
    def Enable(self):
        """开关状态 0：关 ， 1：开
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Status(self):
        """开关的状态 0：正常， 1：转换中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AttachWithEdge(self):
        """0-非sase实例，忽略，1-未绑定状态，2-已绑定
        :rtype: int
        """
        return self._AttachWithEdge

    @AttachWithEdge.setter
    def AttachWithEdge(self, AttachWithEdge):
        self._AttachWithEdge = AttachWithEdge

    @property
    def CrossEdgeStatus(self):
        """对等防火墙和开关状态 0：正常， 1：对等未创建防火墙，2：对等已创建防火墙，未打开开关
        :rtype: int
        """
        return self._CrossEdgeStatus

    @CrossEdgeStatus.setter
    def CrossEdgeStatus(self, CrossEdgeStatus):
        self._CrossEdgeStatus = CrossEdgeStatus

    @property
    def FwInsRegion(self):
        """网络经过VPC防火墙CVM所在地域
        :rtype: list of str
        """
        return self._FwInsRegion

    @FwInsRegion.setter
    def FwInsRegion(self, FwInsRegion):
        self._FwInsRegion = FwInsRegion

    @property
    def IpsAction(self):
        """0 观察 1 拦截 2 严格 3 关闭 4 不支持ips 前端展示tag
        :rtype: int
        """
        return self._IpsAction

    @IpsAction.setter
    def IpsAction(self, IpsAction):
        self._IpsAction = IpsAction

    @property
    def FwInsLst(self):
        """开关关联的防火墙实例列表
        :rtype: list of VpcFwInstanceShow
        """
        return self._FwInsLst

    @FwInsLst.setter
    def FwInsLst(self, FwInsLst):
        self._FwInsLst = FwInsLst

    @property
    def BypassStatus(self):
        """开关是否处于bypass状态
0：正常状态
1：bypass状态
        :rtype: int
        """
        return self._BypassStatus

    @BypassStatus.setter
    def BypassStatus(self, BypassStatus):
        self._BypassStatus = BypassStatus

    @property
    def IpVersion(self):
        """0: ipv4 , 1:ipv6
        :rtype: int
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion


    def _deserialize(self, params):
        self._SwitchId = params.get("SwitchId")
        self._SwitchName = params.get("SwitchName")
        self._SwitchMode = params.get("SwitchMode")
        self._ConnectType = params.get("ConnectType")
        self._ConnectId = params.get("ConnectId")
        self._ConnectName = params.get("ConnectName")
        if params.get("SrcInstancesInfo") is not None:
            self._SrcInstancesInfo = []
            for item in params.get("SrcInstancesInfo"):
                obj = NetInstancesInfo()
                obj._deserialize(item)
                self._SrcInstancesInfo.append(obj)
        if params.get("DstInstancesInfo") is not None:
            self._DstInstancesInfo = []
            for item in params.get("DstInstancesInfo"):
                obj = NetInstancesInfo()
                obj._deserialize(item)
                self._DstInstancesInfo.append(obj)
        self._FwGroupId = params.get("FwGroupId")
        self._FwGroupName = params.get("FwGroupName")
        self._Enable = params.get("Enable")
        self._Status = params.get("Status")
        self._AttachWithEdge = params.get("AttachWithEdge")
        self._CrossEdgeStatus = params.get("CrossEdgeStatus")
        self._FwInsRegion = params.get("FwInsRegion")
        self._IpsAction = params.get("IpsAction")
        if params.get("FwInsLst") is not None:
            self._FwInsLst = []
            for item in params.get("FwInsLst"):
                obj = VpcFwInstanceShow()
                obj._deserialize(item)
                self._FwInsLst.append(obj)
        self._BypassStatus = params.get("BypassStatus")
        self._IpVersion = params.get("IpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FwVpcCidr(AbstractModel):
    """vpc的防火墙网段

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc的id
        :type VpcId: str
        :param _FwCidr: 防火墙网段，最少/24的网段
        :type FwCidr: str
        """
        self._VpcId = None
        self._FwCidr = None

    @property
    def VpcId(self):
        """vpc的id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def FwCidr(self):
        """防火墙网段，最少/24的网段
        :rtype: str
        """
        return self._FwCidr

    @FwCidr.setter
    def FwCidr(self, FwCidr):
        self._FwCidr = FwCidr


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._FwCidr = params.get("FwCidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPDefendStatus(AbstractModel):
    """ip防护状态

    """

    def __init__(self):
        r"""
        :param _IP: ip地址
        :type IP: str
        :param _Status: 防护状态   1:防护打开; -1:地址错误; 其他:未防护
        :type Status: int
        """
        self._IP = None
        self._Status = None

    @property
    def IP(self):
        """ip地址
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Status(self):
        """防护状态   1:防护打开; -1:地址错误; 其他:未防护
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdsWhiteInfo(AbstractModel):
    """入侵防御规则白名单详情

    """

    def __init__(self):
        r"""
        :param _Id: 白名单唯一ID
        :type Id: int
        :param _SrcIp: 源IP
        :type SrcIp: str
        :param _DstIp: 目的IP
        :type DstIp: str
        :param _WhiteRuleType: 规则类型
        :type WhiteRuleType: str
        :param _FwType: 白名单生效防火墙范围： 1 边界防火墙 2 nat防火墙 4 vpc防火墙 7 = 1+2+4 所有防火墙
        :type FwType: int
        :param _RuleId: 入侵防御规则ID
        :type RuleId: str
        """
        self._Id = None
        self._SrcIp = None
        self._DstIp = None
        self._WhiteRuleType = None
        self._FwType = None
        self._RuleId = None

    @property
    def Id(self):
        """白名单唯一ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SrcIp(self):
        """源IP
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def DstIp(self):
        """目的IP
        :rtype: str
        """
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def WhiteRuleType(self):
        """规则类型
        :rtype: str
        """
        return self._WhiteRuleType

    @WhiteRuleType.setter
    def WhiteRuleType(self, WhiteRuleType):
        self._WhiteRuleType = WhiteRuleType

    @property
    def FwType(self):
        """白名单生效防火墙范围： 1 边界防火墙 2 nat防火墙 4 vpc防火墙 7 = 1+2+4 所有防火墙
        :rtype: int
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType

    @property
    def RuleId(self):
        """入侵防御规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SrcIp = params.get("SrcIp")
        self._DstIp = params.get("DstIp")
        self._WhiteRuleType = params.get("WhiteRuleType")
        self._FwType = params.get("FwType")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """实例详情结果

    """

    def __init__(self):
        r"""
        :param _AppId: appid信息
        :type AppId: str
        :param _InsSource: 资产来源
1公网 2内网
        :type InsSource: str
        :param _InsType: 资产类型
 3是cvm实例,4是clb实例,5是eni实例,6是mysql,7是redis,8是NAT,9是VPN,10是ES,11是MARIADB,12是KAFKA 13 NATFW
        :type InsType: int
        :param _InstanceId: 资产id
        :type InstanceId: str
        :param _InstanceName: 资产名
        :type InstanceName: str
        :param _LeakNum: 漏洞数
        :type LeakNum: str
        :param _PortNum: 端口数
        :type PortNum: str
        :param _PrivateIp: 内网ip
        :type PrivateIp: str
        :param _PublicIp: 公网ip
        :type PublicIp: str
        :param _Region: 地域
        :type Region: str
        :param _RegionKey: 地域
        :type RegionKey: str
        :param _ResourcePath: 资产路径
        :type ResourcePath: list of str
        :param _Server: 扫描结果
        :type Server: list of str
        :param _SubnetId: 子网id
        :type SubnetId: str
        :param _VPCName: vpc名称
        :type VPCName: str
        :param _VpcId: vpcid信息
        :type VpcId: str
        """
        self._AppId = None
        self._InsSource = None
        self._InsType = None
        self._InstanceId = None
        self._InstanceName = None
        self._LeakNum = None
        self._PortNum = None
        self._PrivateIp = None
        self._PublicIp = None
        self._Region = None
        self._RegionKey = None
        self._ResourcePath = None
        self._Server = None
        self._SubnetId = None
        self._VPCName = None
        self._VpcId = None

    @property
    def AppId(self):
        """appid信息
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def InsSource(self):
        """资产来源
1公网 2内网
        :rtype: str
        """
        return self._InsSource

    @InsSource.setter
    def InsSource(self, InsSource):
        self._InsSource = InsSource

    @property
    def InsType(self):
        """资产类型
 3是cvm实例,4是clb实例,5是eni实例,6是mysql,7是redis,8是NAT,9是VPN,10是ES,11是MARIADB,12是KAFKA 13 NATFW
        :rtype: int
        """
        return self._InsType

    @InsType.setter
    def InsType(self, InsType):
        self._InsType = InsType

    @property
    def InstanceId(self):
        """资产id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """资产名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LeakNum(self):
        """漏洞数
        :rtype: str
        """
        return self._LeakNum

    @LeakNum.setter
    def LeakNum(self, LeakNum):
        self._LeakNum = LeakNum

    @property
    def PortNum(self):
        """端口数
        :rtype: str
        """
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum

    @property
    def PrivateIp(self):
        """内网ip
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def PublicIp(self):
        """公网ip
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionKey(self):
        """地域
        :rtype: str
        """
        return self._RegionKey

    @RegionKey.setter
    def RegionKey(self, RegionKey):
        self._RegionKey = RegionKey

    @property
    def ResourcePath(self):
        """资产路径
        :rtype: list of str
        """
        return self._ResourcePath

    @ResourcePath.setter
    def ResourcePath(self, ResourcePath):
        self._ResourcePath = ResourcePath

    @property
    def Server(self):
        """扫描结果
        :rtype: list of str
        """
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

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
    def VPCName(self):
        """vpc名称
        :rtype: str
        """
        return self._VPCName

    @VPCName.setter
    def VPCName(self, VPCName):
        self._VPCName = VPCName

    @property
    def VpcId(self):
        """vpcid信息
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._InsSource = params.get("InsSource")
        self._InsType = params.get("InsType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._LeakNum = params.get("LeakNum")
        self._PortNum = params.get("PortNum")
        self._PrivateIp = params.get("PrivateIp")
        self._PublicIp = params.get("PublicIp")
        self._Region = params.get("Region")
        self._RegionKey = params.get("RegionKey")
        self._ResourcePath = params.get("ResourcePath")
        self._Server = params.get("Server")
        self._SubnetId = params.get("SubnetId")
        self._VPCName = params.get("VPCName")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntrusionDefenseRule(AbstractModel):
    """入侵防御封禁列表、放通列表添加规则入参

    """

    def __init__(self):
        r"""
        :param _Direction: 规则方向，0出站，1入站，3内网间
        :type Direction: int
        :param _EndTime: 规则结束时间，格式：2006-01-02 15:04:05，必须大于当前时间
        :type EndTime: str
        :param _IP: 规则IP地址，IP与Domain必填其中之一
        :type IP: str
        :param _Domain: 规则域名，IP与Domain必填其中之一
        :type Domain: str
        :param _StartTime: 规则开始时间
        :type StartTime: str
        :param _Comment: 备注信息，长度不能超过50
        :type Comment: str
        """
        self._Direction = None
        self._EndTime = None
        self._IP = None
        self._Domain = None
        self._StartTime = None
        self._Comment = None

    @property
    def Direction(self):
        """规则方向，0出站，1入站，3内网间
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EndTime(self):
        """规则结束时间，格式：2006-01-02 15:04:05，必须大于当前时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IP(self):
        """规则IP地址，IP与Domain必填其中之一
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Domain(self):
        """规则域名，IP与Domain必填其中之一
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        """规则开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Comment(self):
        """备注信息，长度不能超过50
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._EndTime = params.get("EndTime")
        self._IP = params.get("IP")
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IocListData(AbstractModel):
    """封禁放通IOC列表

    """

    def __init__(self):
        r"""
        :param _IP: 待处置IP地址，IP/Domain字段二选一
        :type IP: str
        :param _Direction: 只能为0或者1   0代表出站 1代表入站
        :type Direction: int
        :param _Domain: 待处置域名，IP/Domain字段二选一
        :type Domain: str
        """
        self._IP = None
        self._Direction = None
        self._Domain = None

    @property
    def IP(self):
        """待处置IP地址，IP/Domain字段二选一
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Direction(self):
        """只能为0或者1   0代表出站 1代表入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Domain(self):
        """待处置域名，IP/Domain字段二选一
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Direction = params.get("Direction")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatic(AbstractModel):
    """统计折线图通用结构体

    """

    def __init__(self):
        r"""
        :param _Num: 值
        :type Num: int
        :param _StatTime: 折线图横坐标时间
        :type StatTime: str
        """
        self._Num = None
        self._StatTime = None

    @property
    def Num(self):
        """值
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def StatTime(self):
        """折线图横坐标时间
        :rtype: str
        """
        return self._StatTime

    @StatTime.setter
    def StatTime(self, StatTime):
        self._StatTime = StatTime


    def _deserialize(self, params):
        self._Num = params.get("Num")
        self._StatTime = params.get("StatTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """日志结果信息

    """

    def __init__(self):
        r"""
        :param _Time: 日志时间，单位ms
        :type Time: int
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _Source: 日志来源IP
        :type Source: str
        :param _FileName: 日志文件名称
        :type FileName: str
        :param _PkgId: 日志上报请求包的ID
        :type PkgId: str
        :param _PkgLogId: 请求包内日志的ID
        :type PkgLogId: str
        :param _LogJson: 日志内容的Json序列化字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type LogJson: str
        :param _HostName: 日志来源主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param _RawLog: 原始日志(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :type RawLog: str
        :param _IndexStatus: 日志创建索引异常原因(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :type IndexStatus: str
        """
        self._Time = None
        self._TopicId = None
        self._TopicName = None
        self._Source = None
        self._FileName = None
        self._PkgId = None
        self._PkgLogId = None
        self._LogJson = None
        self._HostName = None
        self._RawLog = None
        self._IndexStatus = None

    @property
    def Time(self):
        """日志时间，单位ms
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Source(self):
        """日志来源IP
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def FileName(self):
        """日志文件名称
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def PkgId(self):
        """日志上报请求包的ID
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def PkgLogId(self):
        """请求包内日志的ID
        :rtype: str
        """
        return self._PkgLogId

    @PkgLogId.setter
    def PkgLogId(self, PkgLogId):
        self._PkgLogId = PkgLogId

    @property
    def LogJson(self):
        """日志内容的Json序列化字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogJson

    @LogJson.setter
    def LogJson(self, LogJson):
        self._LogJson = LogJson

    @property
    def HostName(self):
        """日志来源主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def RawLog(self):
        """原始日志(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RawLog

    @RawLog.setter
    def RawLog(self, RawLog):
        self._RawLog = RawLog

    @property
    def IndexStatus(self):
        """日志创建索引异常原因(仅在日志创建索引异常时有值)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IndexStatus

    @IndexStatus.setter
    def IndexStatus(self, IndexStatus):
        self._IndexStatus = IndexStatus


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Source = params.get("Source")
        self._FileName = params.get("FileName")
        self._PkgId = params.get("PkgId")
        self._PkgLogId = params.get("PkgLogId")
        self._LogJson = params.get("LogJson")
        self._HostName = params.get("HostName")
        self._RawLog = params.get("RawLog")
        self._IndexStatus = params.get("IndexStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogItem(AbstractModel):
    """日志中的KV对

    """

    def __init__(self):
        r"""
        :param _Key: 日志Key
        :type Key: str
        :param _Value: 日志Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """日志Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """日志Value
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
        


class LogItems(AbstractModel):
    """LogItem的数组

    """

    def __init__(self):
        r"""
        :param _Data: 分析结果返回的KV数据对
        :type Data: list of LogItem
        """
        self._Data = None

    @property
    def Data(self):
        """分析结果返回的KV数据对
        :rtype: list of LogItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LogItem()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleRequest(AbstractModel):
    """ModifyAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 规则数组
        :type Data: list of RuleInfoData
        :param _EdgeId: EdgeId值
        :type EdgeId: str
        :param _Enable: 访问规则状态
        :type Enable: int
        :param _Area: NAT地域
        :type Area: str
        """
        self._Data = None
        self._EdgeId = None
        self._Enable = None
        self._Area = None

    @property
    def Data(self):
        """规则数组
        :rtype: list of RuleInfoData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def EdgeId(self):
        """EdgeId值
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Enable(self):
        """访问规则状态
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Area(self):
        """NAT地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RuleInfoData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._EdgeId = params.get("EdgeId")
        self._Enable = params.get("Enable")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAcRuleResponse(AbstractModel):
    """ModifyAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0:操作成功，非0：操作失败
        :type Status: int
        :param _Info: 返回多余的信息
        :type Info: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0:操作成功，非0：操作失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        """返回多余的信息
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        self._Info = params.get("Info")
        self._RequestId = params.get("RequestId")


class ModifyAclRuleRequest(AbstractModel):
    """ModifyAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 需要编辑的规则数组，基于Uuid唯一id修改该规则
        :type Rules: list of CreateRuleItem
        """
        self._Rules = None

    @property
    def Rules(self):
        """需要编辑的规则数组，基于Uuid唯一id修改该规则
        :rtype: list of CreateRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CreateRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
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
        :param _RuleUuid: 编辑成功后返回新策略ID列表
        :type RuleUuid: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """编辑成功后返回新策略ID列表
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

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
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class ModifyAddressTemplateRequest(AbstractModel):
    """ModifyAddressTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Uuid: 地址模板唯一Id
        :type Uuid: str
        :param _Name: 模板名称
        :type Name: str
        :param _Detail: 模板描述
        :type Detail: str
        :param _IpString: Type为1，ip模板eg：1.1.1.1,2.2.2.2；
Type为5，域名模板eg：www.qq.com,www.tencent.com
        :type IpString: str
        :param _Type: 1 ip模板
5 域名模板
        :type Type: int
        :param _ProtocolType: 协议端口模板，协议类型，4:4层协议，7:7层协议。Type=6时必填。
        :type ProtocolType: str
        """
        self._Uuid = None
        self._Name = None
        self._Detail = None
        self._IpString = None
        self._Type = None
        self._ProtocolType = None

    @property
    def Uuid(self):
        """地址模板唯一Id
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Name(self):
        """模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Detail(self):
        """模板描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def IpString(self):
        """Type为1，ip模板eg：1.1.1.1,2.2.2.2；
Type为5，域名模板eg：www.qq.com,www.tencent.com
        :rtype: str
        """
        return self._IpString

    @IpString.setter
    def IpString(self, IpString):
        self._IpString = IpString

    @property
    def Type(self):
        """1 ip模板
5 域名模板
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProtocolType(self):
        """协议端口模板，协议类型，4:4层协议，7:7层协议。Type=6时必填。
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Name = params.get("Name")
        self._Detail = params.get("Detail")
        self._IpString = params.get("IpString")
        self._Type = params.get("Type")
        self._ProtocolType = params.get("ProtocolType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressTemplateResponse(AbstractModel):
    """ModifyAddressTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 创建结果,0成功
        :type Status: int
        :param _Uuid: 唯一Id
        :type Uuid: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Uuid = None
        self._RequestId = None

    @property
    def Status(self):
        """创建结果,0成功
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Uuid(self):
        """唯一Id
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

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
        self._Uuid = params.get("Uuid")
        self._RequestId = params.get("RequestId")


class ModifyAllPublicIPSwitchStatusRequest(AbstractModel):
    """ModifyAllPublicIPSwitchStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态，0：关闭，1：开启
        :type Status: int
        :param _FireWallPublicIPs: 选中的防火墙开关Id
        :type FireWallPublicIPs: list of str
        """
        self._Status = None
        self._FireWallPublicIPs = None

    @property
    def Status(self):
        """状态，0：关闭，1：开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FireWallPublicIPs(self):
        """选中的防火墙开关Id
        :rtype: list of str
        """
        return self._FireWallPublicIPs

    @FireWallPublicIPs.setter
    def FireWallPublicIPs(self, FireWallPublicIPs):
        self._FireWallPublicIPs = FireWallPublicIPs


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._FireWallPublicIPs = params.get("FireWallPublicIPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllPublicIPSwitchStatusResponse(AbstractModel):
    """ModifyAllPublicIPSwitchStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: 接口返回信息
        :type ReturnMsg: str
        :param _ReturnCode: 接口返回错误码，0请求成功  非0失败
        :type ReturnCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """接口返回信息
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """接口返回错误码，0请求成功  非0失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

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
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class ModifyAllRuleStatusRequest(AbstractModel):
    """ModifyAllRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态，0：全部停用，1：全部启用
        :type Status: int
        :param _Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param _EdgeId: Edge ID值
        :type EdgeId: str
        :param _Area: NAT地域
        :type Area: str
        """
        self._Status = None
        self._Direction = None
        self._EdgeId = None
        self._Area = None

    @property
    def Status(self):
        """状态，0：全部停用，1：全部启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Direction(self):
        """方向，0：出站，1：入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def EdgeId(self):
        """Edge ID值
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Area(self):
        """NAT地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Direction = params.get("Direction")
        self._EdgeId = params.get("EdgeId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAllRuleStatusResponse(AbstractModel):
    """ModifyAllRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0: 修改成功, 其他: 修改失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: 修改成功, 其他: 修改失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyAssetScanRequest(AbstractModel):
    """ModifyAssetScan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScanRange: 扫描范围：1端口, 2端口+漏扫
        :type ScanRange: int
        :param _ScanDeep: 扫描深度：'heavy', 'medium', 'light'
        :type ScanDeep: str
        :param _RangeType: 扫描类型：1立即扫描 2 周期任务
        :type RangeType: int
        :param _ScanPeriod: RangeType为2 是必须添加，定时任务时间
        :type ScanPeriod: str
        :param _ScanFilterIp: 立即扫描这个字段传过滤的扫描集合
        :type ScanFilterIp: list of str
        :param _ScanType: 1全量2单个
        :type ScanType: int
        """
        self._ScanRange = None
        self._ScanDeep = None
        self._RangeType = None
        self._ScanPeriod = None
        self._ScanFilterIp = None
        self._ScanType = None

    @property
    def ScanRange(self):
        """扫描范围：1端口, 2端口+漏扫
        :rtype: int
        """
        return self._ScanRange

    @ScanRange.setter
    def ScanRange(self, ScanRange):
        self._ScanRange = ScanRange

    @property
    def ScanDeep(self):
        """扫描深度：'heavy', 'medium', 'light'
        :rtype: str
        """
        return self._ScanDeep

    @ScanDeep.setter
    def ScanDeep(self, ScanDeep):
        self._ScanDeep = ScanDeep

    @property
    def RangeType(self):
        """扫描类型：1立即扫描 2 周期任务
        :rtype: int
        """
        return self._RangeType

    @RangeType.setter
    def RangeType(self, RangeType):
        self._RangeType = RangeType

    @property
    def ScanPeriod(self):
        """RangeType为2 是必须添加，定时任务时间
        :rtype: str
        """
        return self._ScanPeriod

    @ScanPeriod.setter
    def ScanPeriod(self, ScanPeriod):
        self._ScanPeriod = ScanPeriod

    @property
    def ScanFilterIp(self):
        """立即扫描这个字段传过滤的扫描集合
        :rtype: list of str
        """
        return self._ScanFilterIp

    @ScanFilterIp.setter
    def ScanFilterIp(self, ScanFilterIp):
        self._ScanFilterIp = ScanFilterIp

    @property
    def ScanType(self):
        """1全量2单个
        :rtype: int
        """
        return self._ScanType

    @ScanType.setter
    def ScanType(self, ScanType):
        self._ScanType = ScanType


    def _deserialize(self, params):
        self._ScanRange = params.get("ScanRange")
        self._ScanDeep = params.get("ScanDeep")
        self._RangeType = params.get("RangeType")
        self._ScanPeriod = params.get("ScanPeriod")
        self._ScanFilterIp = params.get("ScanFilterIp")
        self._ScanType = params.get("ScanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssetScanResponse(AbstractModel):
    """ModifyAssetScan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: 接口返回信息
        :type ReturnMsg: str
        :param _ReturnCode: 接口返回错误码，0请求成功  非0失败
        :type ReturnCode: int
        :param _Status: 状态值 0：成功，1 执行扫描中,其他：失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._ReturnCode = None
        self._Status = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """接口返回信息
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """接口返回错误码，0请求成功  非0失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Status(self):
        """状态值 0：成功，1 执行扫描中,其他：失败
        :rtype: int
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
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyAssetSyncRequest(AbstractModel):
    """ModifyAssetSync请求参数结构体

    """


class ModifyAssetSyncResponse(AbstractModel):
    """ModifyAssetSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 返回状态
0 请求成功
2 请求失败
3 请求失败-频率限制
        :type Status: int
        :param _ReturnMsg: success 成功
其他失败
        :type ReturnMsg: str
        :param _ReturnCode: 0 成功
非0 失败
        :type ReturnCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def Status(self):
        """返回状态
0 请求成功
2 请求失败
3 请求失败-频率限制
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReturnMsg(self):
        """success 成功
其他失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """0 成功
非0 失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

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
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class ModifyBlockIgnoreListRequest(AbstractModel):
    """ModifyBlockIgnoreList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleType: 1封禁列表 2 放通列表
        :type RuleType: int
        :param _IOC: IP、Domain二选一（注：封禁列表，只能填写IP），不能同时为空
        :type IOC: list of IocListData
        :param _IocAction: 可选值：delete（删除）、edit（编辑）、add（添加）  其他值无效
        :type IocAction: str
        :param _StartTime: 时间格式：yyyy-MM-dd HH:mm:ss，IocAction 为edit或add时必填
        :type StartTime: str
        :param _EndTime: 时间格式：yyyy-MM-dd HH:mm:ss，IocAction 为edit或add时必填，必须大于当前时间且大于StartTime
        :type EndTime: str
        """
        self._RuleType = None
        self._IOC = None
        self._IocAction = None
        self._StartTime = None
        self._EndTime = None

    @property
    def RuleType(self):
        """1封禁列表 2 放通列表
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def IOC(self):
        """IP、Domain二选一（注：封禁列表，只能填写IP），不能同时为空
        :rtype: list of IocListData
        """
        return self._IOC

    @IOC.setter
    def IOC(self, IOC):
        self._IOC = IOC

    @property
    def IocAction(self):
        """可选值：delete（删除）、edit（编辑）、add（添加）  其他值无效
        :rtype: str
        """
        return self._IocAction

    @IocAction.setter
    def IocAction(self, IocAction):
        self._IocAction = IocAction

    @property
    def StartTime(self):
        """时间格式：yyyy-MM-dd HH:mm:ss，IocAction 为edit或add时必填
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """时间格式：yyyy-MM-dd HH:mm:ss，IocAction 为edit或add时必填，必须大于当前时间且大于StartTime
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        if params.get("IOC") is not None:
            self._IOC = []
            for item in params.get("IOC"):
                obj = IocListData()
                obj._deserialize(item)
                self._IOC.append(obj)
        self._IocAction = params.get("IocAction")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIgnoreListResponse(AbstractModel):
    """ModifyBlockIgnoreList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: 接口返回信息
        :type ReturnMsg: str
        :param _ReturnCode: 接口返回错误码，0请求成功  非0失败
        :type ReturnCode: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._ReturnCode = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """接口返回信息
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def ReturnCode(self):
        """接口返回错误码，0请求成功  非0失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

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
        self._ReturnMsg = params.get("ReturnMsg")
        self._ReturnCode = params.get("ReturnCode")
        self._RequestId = params.get("RequestId")


class ModifyBlockIgnoreRuleNewRequest(AbstractModel):
    """ModifyBlockIgnoreRuleNew请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.cfw.v20190904.models.BanAndAllowRule`
        :param _RuleType: RuleType: 1放通列表 2外部IP 3域名 4情报 5资产 6自定义规则  7入侵防御规则
        :type RuleType: int
        """
        self._Rule = None
        self._RuleType = None

    @property
    def Rule(self):
        """规则
        :rtype: :class:`tencentcloud.cfw.v20190904.models.BanAndAllowRule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RuleType(self):
        """RuleType: 1放通列表 2外部IP 3域名 4情报 5资产 6自定义规则  7入侵防御规则
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = BanAndAllowRule()
            self._Rule._deserialize(params.get("Rule"))
        self._RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIgnoreRuleNewResponse(AbstractModel):
    """ModifyBlockIgnoreRuleNew返回参数结构体

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


class ModifyBlockIgnoreRuleRequest(AbstractModel):
    """ModifyBlockIgnoreRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则列表
        :type Rule: :class:`tencentcloud.cfw.v20190904.models.IntrusionDefenseRule`
        :param _RuleType: 规则类型，1封禁，2放通
        :type RuleType: int
        """
        self._Rule = None
        self._RuleType = None

    @property
    def Rule(self):
        """规则列表
        :rtype: :class:`tencentcloud.cfw.v20190904.models.IntrusionDefenseRule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RuleType(self):
        """规则类型，1封禁，2放通
        :rtype: int
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = IntrusionDefenseRule()
            self._Rule._deserialize(params.get("Rule"))
        self._RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockIgnoreRuleResponse(AbstractModel):
    """ModifyBlockIgnoreRule返回参数结构体

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


class ModifyBlockTopRequest(AbstractModel):
    """ModifyBlockTop请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OpeType: 操作类型 1 置顶 0取消
        :type OpeType: str
        :param _UniqueId: 记录id
        :type UniqueId: str
        """
        self._OpeType = None
        self._UniqueId = None

    @property
    def OpeType(self):
        """操作类型 1 置顶 0取消
        :rtype: str
        """
        return self._OpeType

    @OpeType.setter
    def OpeType(self, OpeType):
        self._OpeType = OpeType

    @property
    def UniqueId(self):
        """记录id
        :rtype: str
        """
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId


    def _deserialize(self, params):
        self._OpeType = params.get("OpeType")
        self._UniqueId = params.get("UniqueId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBlockTopResponse(AbstractModel):
    """ModifyBlockTop返回参数结构体

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


class ModifyEWRuleStatusRequest(AbstractModel):
    """ModifyEWRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeId: vpc规则必填，边id
        :type EdgeId: str
        :param _Status: 是否开关开启，0：未开启，1：开启
        :type Status: int
        :param _Direction: 规则方向，0：出站，1：入站，默认1
        :type Direction: int
        :param _RuleSequence: 更改的规则当前执行顺序
        :type RuleSequence: int
        :param _RuleType: 规则类型，vpc：VPC间规则、nat：Nat边界规则
        :type RuleType: str
        """
        self._EdgeId = None
        self._Status = None
        self._Direction = None
        self._RuleSequence = None
        self._RuleType = None

    @property
    def EdgeId(self):
        """vpc规则必填，边id
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Status(self):
        """是否开关开启，0：未开启，1：开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Direction(self):
        """规则方向，0：出站，1：入站，默认1
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RuleSequence(self):
        """更改的规则当前执行顺序
        :rtype: int
        """
        return self._RuleSequence

    @RuleSequence.setter
    def RuleSequence(self, RuleSequence):
        self._RuleSequence = RuleSequence

    @property
    def RuleType(self):
        """规则类型，vpc：VPC间规则、nat：Nat边界规则
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        self._Status = params.get("Status")
        self._Direction = params.get("Direction")
        self._RuleSequence = params.get("RuleSequence")
        self._RuleType = params.get("RuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEWRuleStatusResponse(AbstractModel):
    """ModifyEWRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 状态值，0：修改成功，非0：修改失败
        :type ReturnCode: int
        :param _ReturnMsg: 状态信息，success：查询成功，fail：查询失败
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        """状态值，0：修改成功，非0：修改失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """状态信息，success：查询成功，fail：查询失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class ModifyEdgeIpSwitchRequest(AbstractModel):
    """ModifyEdgeIpSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 0 关闭开关
1 打开开关
2 不操作开关，此次切换模式
        :type Enable: int
        :param _EdgeIpSwitchLst: 操作开关详情
        :type EdgeIpSwitchLst: list of EdgeIpSwitch
        :param _AutoChooseSubnet: 0 不自动选择子网
1 自动选择子网创建私有连接
        :type AutoChooseSubnet: int
        :param _SwitchMode: 0 切换为旁路
1 切换为串行
2 不切换模式，此次操作开关
        :type SwitchMode: int
        """
        self._Enable = None
        self._EdgeIpSwitchLst = None
        self._AutoChooseSubnet = None
        self._SwitchMode = None

    @property
    def Enable(self):
        """0 关闭开关
1 打开开关
2 不操作开关，此次切换模式
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def EdgeIpSwitchLst(self):
        """操作开关详情
        :rtype: list of EdgeIpSwitch
        """
        return self._EdgeIpSwitchLst

    @EdgeIpSwitchLst.setter
    def EdgeIpSwitchLst(self, EdgeIpSwitchLst):
        self._EdgeIpSwitchLst = EdgeIpSwitchLst

    @property
    def AutoChooseSubnet(self):
        """0 不自动选择子网
1 自动选择子网创建私有连接
        :rtype: int
        """
        return self._AutoChooseSubnet

    @AutoChooseSubnet.setter
    def AutoChooseSubnet(self, AutoChooseSubnet):
        self._AutoChooseSubnet = AutoChooseSubnet

    @property
    def SwitchMode(self):
        """0 切换为旁路
1 切换为串行
2 不切换模式，此次操作开关
        :rtype: int
        """
        return self._SwitchMode

    @SwitchMode.setter
    def SwitchMode(self, SwitchMode):
        self._SwitchMode = SwitchMode


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        if params.get("EdgeIpSwitchLst") is not None:
            self._EdgeIpSwitchLst = []
            for item in params.get("EdgeIpSwitchLst"):
                obj = EdgeIpSwitch()
                obj._deserialize(item)
                self._EdgeIpSwitchLst.append(obj)
        self._AutoChooseSubnet = params.get("AutoChooseSubnet")
        self._SwitchMode = params.get("SwitchMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeIpSwitchResponse(AbstractModel):
    """ModifyEdgeIpSwitch返回参数结构体

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


class ModifyEnterpriseSecurityDispatchStatusRequest(AbstractModel):
    """ModifyEnterpriseSecurityDispatchStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0：打开立即下发开关；

1：关闭立即下发开关；

2：关闭立即下发开关情况下，触发开始下发
        :type Status: int
        """
        self._Status = None

    @property
    def Status(self):
        """0：打开立即下发开关；

1：关闭立即下发开关；

2：关闭立即下发开关情况下，触发开始下发
        :rtype: int
        """
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
        


class ModifyEnterpriseSecurityDispatchStatusResponse(AbstractModel):
    """ModifyEnterpriseSecurityDispatchStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0: 修改成功, 其他: 修改失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: 修改成功, 其他: 修改失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """ModifyEnterpriseSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 规则的uuid，可通过查询规则列表获取
        :type RuleUuid: int
        :param _ModifyType: 修改类型，0：修改规则内容；1：修改单条规则开关状态；2：修改所有规则开关状态
        :type ModifyType: int
        :param _Data: 编辑后的企业安全组规则数据；修改规则状态不用填该字段
        :type Data: :class:`tencentcloud.cfw.v20190904.models.SecurityGroupRule`
        :param _Enable: 0是关闭,1是开启
        :type Enable: int
        """
        self._RuleUuid = None
        self._ModifyType = None
        self._Data = None
        self._Enable = None

    @property
    def RuleUuid(self):
        """规则的uuid，可通过查询规则列表获取
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def ModifyType(self):
        """修改类型，0：修改规则内容；1：修改单条规则开关状态；2：修改所有规则开关状态
        :rtype: int
        """
        return self._ModifyType

    @ModifyType.setter
    def ModifyType(self, ModifyType):
        self._ModifyType = ModifyType

    @property
    def Data(self):
        """编辑后的企业安全组规则数据；修改规则状态不用填该字段
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SecurityGroupRule`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Enable(self):
        """0是关闭,1是开启
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._ModifyType = params.get("ModifyType")
        if params.get("Data") is not None:
            self._Data = SecurityGroupRule()
            self._Data._deserialize(params.get("Data"))
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """ModifyEnterpriseSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0：编辑成功，非0：编辑失败
        :type Status: int
        :param _NewRuleUuid: 编辑后新生成规则的Id
        :type NewRuleUuid: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._NewRuleUuid = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0：编辑成功，非0：编辑失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NewRuleUuid(self):
        """编辑后新生成规则的Id
        :rtype: int
        """
        return self._NewRuleUuid

    @NewRuleUuid.setter
    def NewRuleUuid(self, NewRuleUuid):
        self._NewRuleUuid = NewRuleUuid

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
        self._NewRuleUuid = params.get("NewRuleUuid")
        self._RequestId = params.get("RequestId")


class ModifyFwGroupSwitchRequest(AbstractModel):
    """ModifyFwGroupSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 打开或关闭开关
0：关闭开关
1：打开开关
        :type Enable: int
        :param _AllSwitch: 是否操作全部开关 0 不操作全部开关，1 操作全部开关
        :type AllSwitch: int
        :param _SwitchList: 开关列表
        :type SwitchList: list of FwGroupSwitch
        """
        self._Enable = None
        self._AllSwitch = None
        self._SwitchList = None

    @property
    def Enable(self):
        """打开或关闭开关
0：关闭开关
1：打开开关
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def AllSwitch(self):
        """是否操作全部开关 0 不操作全部开关，1 操作全部开关
        :rtype: int
        """
        return self._AllSwitch

    @AllSwitch.setter
    def AllSwitch(self, AllSwitch):
        self._AllSwitch = AllSwitch

    @property
    def SwitchList(self):
        """开关列表
        :rtype: list of FwGroupSwitch
        """
        return self._SwitchList

    @SwitchList.setter
    def SwitchList(self, SwitchList):
        self._SwitchList = SwitchList


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._AllSwitch = params.get("AllSwitch")
        if params.get("SwitchList") is not None:
            self._SwitchList = []
            for item in params.get("SwitchList"):
                obj = FwGroupSwitch()
                obj._deserialize(item)
                self._SwitchList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFwGroupSwitchResponse(AbstractModel):
    """ModifyFwGroupSwitch返回参数结构体

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


class ModifyNatAcRuleRequest(AbstractModel):
    """ModifyNatAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 需要编辑的规则数组,基于Uuid唯一id来修改该规则
        :type Rules: list of CreateNatRuleItem
        """
        self._Rules = None

    @property
    def Rules(self):
        """需要编辑的规则数组,基于Uuid唯一id来修改该规则
        :rtype: list of CreateNatRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = CreateNatRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatAcRuleResponse(AbstractModel):
    """ModifyNatAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 编辑成功后返回新策略ID列表
        :type RuleUuid: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """编辑成功后返回新策略ID列表
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

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
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class ModifyNatFwReSelectRequest(AbstractModel):
    """ModifyNatFwReSelect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 模式 1：接入模式；0：新增模式
        :type Mode: int
        :param _CfwInstance: 防火墙实例id
        :type CfwInstance: str
        :param _NatGwList: 接入模式重新接入的nat网关列表，其中NatGwList和VpcList只能传递一个。
        :type NatGwList: list of str
        :param _VpcList: 新增模式重新接入的vpc列表，其中NatGwList和NatgwList只能传递一个。
        :type VpcList: list of str
        :param _FwCidrInfo: 指定防火墙使用网段信息
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        self._Mode = None
        self._CfwInstance = None
        self._NatGwList = None
        self._VpcList = None
        self._FwCidrInfo = None

    @property
    def Mode(self):
        """模式 1：接入模式；0：新增模式
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CfwInstance(self):
        """防火墙实例id
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance

    @property
    def NatGwList(self):
        """接入模式重新接入的nat网关列表，其中NatGwList和VpcList只能传递一个。
        :rtype: list of str
        """
        return self._NatGwList

    @NatGwList.setter
    def NatGwList(self, NatGwList):
        self._NatGwList = NatGwList

    @property
    def VpcList(self):
        """新增模式重新接入的vpc列表，其中NatGwList和NatgwList只能传递一个。
        :rtype: list of str
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def FwCidrInfo(self):
        """指定防火墙使用网段信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._CfwInstance = params.get("CfwInstance")
        self._NatGwList = params.get("NatGwList")
        self._VpcList = params.get("VpcList")
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwReSelectResponse(AbstractModel):
    """ModifyNatFwReSelect返回参数结构体

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


class ModifyNatFwSwitchRequest(AbstractModel):
    """ModifyNatFwSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Enable: 开关，0：关闭，1：开启
        :type Enable: int
        :param _CfwInsIdList: 防火墙实例id列表，其中CfwInsIdList，SubnetIdList和RouteTableIdList只能传递一种。
        :type CfwInsIdList: list of str
        :param _SubnetIdList: 子网id列表，其中CfwInsIdList，SubnetIdList和RouteTableIdList只能传递一种。
        :type SubnetIdList: list of str
        :param _RouteTableIdList: 路由表id列表，其中CfwInsIdList，SubnetIdList和RouteTableIdList只能传递一种。
        :type RouteTableIdList: list of str
        """
        self._Enable = None
        self._CfwInsIdList = None
        self._SubnetIdList = None
        self._RouteTableIdList = None

    @property
    def Enable(self):
        """开关，0：关闭，1：开启
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def CfwInsIdList(self):
        """防火墙实例id列表，其中CfwInsIdList，SubnetIdList和RouteTableIdList只能传递一种。
        :rtype: list of str
        """
        return self._CfwInsIdList

    @CfwInsIdList.setter
    def CfwInsIdList(self, CfwInsIdList):
        self._CfwInsIdList = CfwInsIdList

    @property
    def SubnetIdList(self):
        """子网id列表，其中CfwInsIdList，SubnetIdList和RouteTableIdList只能传递一种。
        :rtype: list of str
        """
        return self._SubnetIdList

    @SubnetIdList.setter
    def SubnetIdList(self, SubnetIdList):
        self._SubnetIdList = SubnetIdList

    @property
    def RouteTableIdList(self):
        """路由表id列表，其中CfwInsIdList，SubnetIdList和RouteTableIdList只能传递一种。
        :rtype: list of str
        """
        return self._RouteTableIdList

    @RouteTableIdList.setter
    def RouteTableIdList(self, RouteTableIdList):
        self._RouteTableIdList = RouteTableIdList


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._CfwInsIdList = params.get("CfwInsIdList")
        self._SubnetIdList = params.get("SubnetIdList")
        self._RouteTableIdList = params.get("RouteTableIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwSwitchResponse(AbstractModel):
    """ModifyNatFwSwitch返回参数结构体

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


class ModifyNatFwVpcDnsSwitchRequest(AbstractModel):
    """ModifyNatFwVpcDnsSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NatFwInsId: nat 防火墙 id
        :type NatFwInsId: str
        :param _DnsVpcSwitchLst: DNS 开关切换列表
        :type DnsVpcSwitchLst: list of DnsVpcSwitch
        """
        self._NatFwInsId = None
        self._DnsVpcSwitchLst = None

    @property
    def NatFwInsId(self):
        """nat 防火墙 id
        :rtype: str
        """
        return self._NatFwInsId

    @NatFwInsId.setter
    def NatFwInsId(self, NatFwInsId):
        self._NatFwInsId = NatFwInsId

    @property
    def DnsVpcSwitchLst(self):
        """DNS 开关切换列表
        :rtype: list of DnsVpcSwitch
        """
        return self._DnsVpcSwitchLst

    @DnsVpcSwitchLst.setter
    def DnsVpcSwitchLst(self, DnsVpcSwitchLst):
        self._DnsVpcSwitchLst = DnsVpcSwitchLst


    def _deserialize(self, params):
        self._NatFwInsId = params.get("NatFwInsId")
        if params.get("DnsVpcSwitchLst") is not None:
            self._DnsVpcSwitchLst = []
            for item in params.get("DnsVpcSwitchLst"):
                obj = DnsVpcSwitch()
                obj._deserialize(item)
                self._DnsVpcSwitchLst.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatFwVpcDnsSwitchResponse(AbstractModel):
    """ModifyNatFwVpcDnsSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnMsg: 修改成功
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def ReturnMsg(self):
        """修改成功
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class ModifyNatInstanceRequest(AbstractModel):
    """ModifyNatInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: NAT防火墙实例名称
        :type InstanceName: str
        :param _NatInstanceId: NAT防火墙实例ID
        :type NatInstanceId: str
        """
        self._InstanceName = None
        self._NatInstanceId = None

    @property
    def InstanceName(self):
        """NAT防火墙实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def NatInstanceId(self):
        """NAT防火墙实例ID
        :rtype: str
        """
        return self._NatInstanceId

    @NatInstanceId.setter
    def NatInstanceId(self, NatInstanceId):
        self._NatInstanceId = NatInstanceId


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._NatInstanceId = params.get("NatInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatInstanceResponse(AbstractModel):
    """ModifyNatInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0 正常
-1 异常
        :type Status: int
        :param _NatInstanceId: nat实例唯一ID
        :type NatInstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._NatInstanceId = None
        self._RequestId = None

    @property
    def Status(self):
        """0 正常
-1 异常
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NatInstanceId(self):
        """nat实例唯一ID
        :rtype: str
        """
        return self._NatInstanceId

    @NatInstanceId.setter
    def NatInstanceId(self, NatInstanceId):
        self._NatInstanceId = NatInstanceId

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
        self._NatInstanceId = params.get("NatInstanceId")
        self._RequestId = params.get("RequestId")


class ModifyNatSequenceRulesRequest(AbstractModel):
    """ModifyNatSequenceRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleChangeItems: 规则快速排序：OrderIndex，原始序号；NewOrderIndex：新序号
        :type RuleChangeItems: list of RuleChangeItem
        :param _Direction: 规则方向：1，入站；0，出站
        :type Direction: int
        """
        self._RuleChangeItems = None
        self._Direction = None

    @property
    def RuleChangeItems(self):
        """规则快速排序：OrderIndex，原始序号；NewOrderIndex：新序号
        :rtype: list of RuleChangeItem
        """
        return self._RuleChangeItems

    @RuleChangeItems.setter
    def RuleChangeItems(self, RuleChangeItems):
        self._RuleChangeItems = RuleChangeItems

    @property
    def Direction(self):
        """规则方向：1，入站；0，出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        if params.get("RuleChangeItems") is not None:
            self._RuleChangeItems = []
            for item in params.get("RuleChangeItems"):
                obj = RuleChangeItem()
                obj._deserialize(item)
                self._RuleChangeItems.append(obj)
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatSequenceRulesResponse(AbstractModel):
    """ModifyNatSequenceRules返回参数结构体

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


class ModifyResourceGroupRequest(AbstractModel):
    """ModifyResourceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 资产组id
        :type GroupId: str
        :param _GroupName: 组名称
        :type GroupName: str
        :param _ParentId: 上级组资产组id
        :type ParentId: str
        """
        self._GroupId = None
        self._GroupName = None
        self._ParentId = None

    @property
    def GroupId(self):
        """资产组id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ParentId(self):
        """上级组资产组id
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceGroupResponse(AbstractModel):
    """ModifyResourceGroup返回参数结构体

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


class ModifyRunSyncAssetRequest(AbstractModel):
    """ModifyRunSyncAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 0: 互联网防火墙开关，1：vpc 防火墙开关
        :type Type: int
        """
        self._Type = None

    @property
    def Type(self):
        """0: 互联网防火墙开关，1：vpc 防火墙开关
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRunSyncAssetResponse(AbstractModel):
    """ModifyRunSyncAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0：同步成功，1：资产更新中，2：后台同步调用失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0：同步成功，1：资产更新中，2：后台同步调用失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupItemRuleStatusRequest(AbstractModel):
    """ModifySecurityGroupItemRuleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Direction: 方向，0：出站，1：入站，默认1
        :type Direction: int
        :param _Status: 是否开关开启，0：未开启，1：开启
        :type Status: int
        :param _RuleSequence: 更改的企业安全组规则的执行顺序
        :type RuleSequence: int
        """
        self._Direction = None
        self._Status = None
        self._RuleSequence = None

    @property
    def Direction(self):
        """方向，0：出站，1：入站，默认1
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Status(self):
        """是否开关开启，0：未开启，1：开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleSequence(self):
        """更改的企业安全组规则的执行顺序
        :rtype: int
        """
        return self._RuleSequence

    @RuleSequence.setter
    def RuleSequence(self, RuleSequence):
        self._RuleSequence = RuleSequence


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._Status = params.get("Status")
        self._RuleSequence = params.get("RuleSequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupItemRuleStatusResponse(AbstractModel):
    """ModifySecurityGroupItemRuleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0：修改成功，非0：修改失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0：修改成功，非0：修改失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupRuleRequest(AbstractModel):
    """ModifySecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Direction: 方向，0：出站，1：入站，默认1
        :type Direction: int
        :param _Enable: 编辑后是否启用规则，0：不启用，1：启用，默认1
        :type Enable: int
        :param _Data: 编辑的企业安全组规则数据
        :type Data: list of SecurityGroupListData
        :param _SgRuleOriginSequence: 编辑的企业安全组规则的原始执行顺序
        :type SgRuleOriginSequence: int
        """
        self._Direction = None
        self._Enable = None
        self._Data = None
        self._SgRuleOriginSequence = None

    @property
    def Direction(self):
        """方向，0：出站，1：入站，默认1
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Enable(self):
        """编辑后是否启用规则，0：不启用，1：启用，默认1
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Data(self):
        """编辑的企业安全组规则数据
        :rtype: list of SecurityGroupListData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SgRuleOriginSequence(self):
        """编辑的企业安全组规则的原始执行顺序
        :rtype: int
        """
        return self._SgRuleOriginSequence

    @SgRuleOriginSequence.setter
    def SgRuleOriginSequence(self, SgRuleOriginSequence):
        self._SgRuleOriginSequence = SgRuleOriginSequence


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._Enable = params.get("Enable")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupListData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._SgRuleOriginSequence = params.get("SgRuleOriginSequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupRuleResponse(AbstractModel):
    """ModifySecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0：编辑成功，非0：编辑失败
        :type Status: int
        :param _NewRuleId: 编辑后新生成规则的Id
        :type NewRuleId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._NewRuleId = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0：编辑成功，非0：编辑失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NewRuleId(self):
        """编辑后新生成规则的Id
        :rtype: int
        """
        return self._NewRuleId

    @NewRuleId.setter
    def NewRuleId(self, NewRuleId):
        self._NewRuleId = NewRuleId

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
        self._NewRuleId = params.get("NewRuleId")
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupSequenceRulesRequest(AbstractModel):
    """ModifySecurityGroupSequenceRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Direction: 方向，0：出站，1：入站，默认1
        :type Direction: int
        :param _Data: 企业安全组规则快速排序数据
        :type Data: list of SecurityGroupOrderIndexData
        """
        self._Direction = None
        self._Data = None

    @property
    def Direction(self):
        """方向，0：出站，1：入站，默认1
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Data(self):
        """企业安全组规则快速排序数据
        :rtype: list of SecurityGroupOrderIndexData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SecurityGroupOrderIndexData()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupSequenceRulesResponse(AbstractModel):
    """ModifySecurityGroupSequenceRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态值，0：修改成功，非0：修改失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """状态值，0：修改成功，非0：修改失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifySequenceAclRulesRequest(AbstractModel):
    """ModifySequenceAclRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleChangeItems: 规则快速排序：OrderIndex，原始序号；NewOrderIndex：新序号
        :type RuleChangeItems: list of RuleChangeItem
        :param _Direction: 规则方向：1，入站；0，出站
        :type Direction: int
        """
        self._RuleChangeItems = None
        self._Direction = None

    @property
    def RuleChangeItems(self):
        """规则快速排序：OrderIndex，原始序号；NewOrderIndex：新序号
        :rtype: list of RuleChangeItem
        """
        return self._RuleChangeItems

    @RuleChangeItems.setter
    def RuleChangeItems(self, RuleChangeItems):
        self._RuleChangeItems = RuleChangeItems

    @property
    def Direction(self):
        """规则方向：1，入站；0，出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        if params.get("RuleChangeItems") is not None:
            self._RuleChangeItems = []
            for item in params.get("RuleChangeItems"):
                obj = RuleChangeItem()
                obj._deserialize(item)
                self._RuleChangeItems.append(obj)
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySequenceAclRulesResponse(AbstractModel):
    """ModifySequenceAclRules返回参数结构体

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


class ModifySequenceRulesRequest(AbstractModel):
    """ModifySequenceRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeId: 边Id值
        :type EdgeId: str
        :param _Data: 修改数据
        :type Data: list of SequenceData
        :param _Area: NAT地域
        :type Area: str
        :param _Direction: 方向，0：出向，1：入向
        :type Direction: int
        """
        self._EdgeId = None
        self._Data = None
        self._Area = None
        self._Direction = None

    @property
    def EdgeId(self):
        """边Id值
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Data(self):
        """修改数据
        :rtype: list of SequenceData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Area(self):
        """NAT地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """方向，0：出向，1：入向
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SequenceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySequenceRulesResponse(AbstractModel):
    """ModifySequenceRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0: 修改成功, 非0: 修改失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0: 修改成功, 非0: 修改失败
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyStorageSettingRequest(AbstractModel):
    """ModifyStorageSetting请求参数结构体

    """


class ModifyStorageSettingResponse(AbstractModel):
    """ModifyStorageSetting返回参数结构体

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


class ModifyTableStatusRequest(AbstractModel):
    """ModifyTableStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgeId: EdgeId值两个vpc间的边id
        :type EdgeId: str
        :param _Status: 状态值，1：锁表，2：解锁表
        :type Status: int
        :param _Area: Nat所在地域
        :type Area: str
        :param _Direction: 0： 出向，1：入向
        :type Direction: int
        """
        self._EdgeId = None
        self._Status = None
        self._Area = None
        self._Direction = None

    @property
    def EdgeId(self):
        """EdgeId值两个vpc间的边id
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Status(self):
        """状态值，1：锁表，2：解锁表
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """Nat所在地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Direction(self):
        """0： 出向，1：入向
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._EdgeId = params.get("EdgeId")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTableStatusResponse(AbstractModel):
    """ModifyTableStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0：正常，-1：不正常
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """0：正常，-1：不正常
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class ModifyVpcAcRuleRequest(AbstractModel):
    """ModifyVpcAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 需要编辑的规则数组
        :type Rules: list of VpcRuleItem
        """
        self._Rules = None

    @property
    def Rules(self):
        """需要编辑的规则数组
        :rtype: list of VpcRuleItem
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = VpcRuleItem()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAcRuleResponse(AbstractModel):
    """ModifyVpcAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuids: 编辑成功后返回新策略ID列表
        :type RuleUuids: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuids = None
        self._RequestId = None

    @property
    def RuleUuids(self):
        """编辑成功后返回新策略ID列表
        :rtype: list of int
        """
        return self._RuleUuids

    @RuleUuids.setter
    def RuleUuids(self, RuleUuids):
        self._RuleUuids = RuleUuids

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
        self._RuleUuids = params.get("RuleUuids")
        self._RequestId = params.get("RequestId")


class ModifyVpcFwGroupRequest(AbstractModel):
    """ModifyVpcFwGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FwGroupId: 编辑的防火墙(组)ID
        :type FwGroupId: str
        :param _Name: 修改防火墙(组)名称
        :type Name: str
        :param _VpcFwInstances: 编辑的防火墙实例列表
        :type VpcFwInstances: list of VpcFwInstance
        :param _FwCidrInfo: 指定防火墙使用网段信息
        :type FwCidrInfo: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        self._FwGroupId = None
        self._Name = None
        self._VpcFwInstances = None
        self._FwCidrInfo = None

    @property
    def FwGroupId(self):
        """编辑的防火墙(组)ID
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def Name(self):
        """修改防火墙(组)名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VpcFwInstances(self):
        """编辑的防火墙实例列表
        :rtype: list of VpcFwInstance
        """
        return self._VpcFwInstances

    @VpcFwInstances.setter
    def VpcFwInstances(self, VpcFwInstances):
        self._VpcFwInstances = VpcFwInstances

    @property
    def FwCidrInfo(self):
        """指定防火墙使用网段信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwCidrInfo`
        """
        return self._FwCidrInfo

    @FwCidrInfo.setter
    def FwCidrInfo(self, FwCidrInfo):
        self._FwCidrInfo = FwCidrInfo


    def _deserialize(self, params):
        self._FwGroupId = params.get("FwGroupId")
        self._Name = params.get("Name")
        if params.get("VpcFwInstances") is not None:
            self._VpcFwInstances = []
            for item in params.get("VpcFwInstances"):
                obj = VpcFwInstance()
                obj._deserialize(item)
                self._VpcFwInstances.append(obj)
        if params.get("FwCidrInfo") is not None:
            self._FwCidrInfo = FwCidrInfo()
            self._FwCidrInfo._deserialize(params.get("FwCidrInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcFwGroupResponse(AbstractModel):
    """ModifyVpcFwGroup返回参数结构体

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


class ModifyVpcFwSequenceRulesRequest(AbstractModel):
    """ModifyVpcFwSequenceRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleChangeItems: 规则快速排序：OrderIndex，原始序号；NewOrderIndex：新序号
        :type RuleChangeItems: list of RuleChangeItem
        """
        self._RuleChangeItems = None

    @property
    def RuleChangeItems(self):
        """规则快速排序：OrderIndex，原始序号；NewOrderIndex：新序号
        :rtype: list of RuleChangeItem
        """
        return self._RuleChangeItems

    @RuleChangeItems.setter
    def RuleChangeItems(self, RuleChangeItems):
        self._RuleChangeItems = RuleChangeItems


    def _deserialize(self, params):
        if params.get("RuleChangeItems") is not None:
            self._RuleChangeItems = []
            for item in params.get("RuleChangeItems"):
                obj = RuleChangeItem()
                obj._deserialize(item)
                self._RuleChangeItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcFwSequenceRulesResponse(AbstractModel):
    """ModifyVpcFwSequenceRules返回参数结构体

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


class MultiTopicSearchInformation(AbstractModel):
    """多日志主题检索相关信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 要检索分析的日志主题ID
        :type TopicId: str
        :param _Context: 透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时
        :type Context: str
        """
        self._TopicId = None
        self._Context = None

    @property
    def TopicId(self):
        """要检索分析的日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Context(self):
        """透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatFwEipsInfo(AbstractModel):
    """Nat防火墙弹性公网ip列表

    """

    def __init__(self):
        r"""
        :param _Eip: 弹性公网ip
        :type Eip: str
        :param _NatGatewayId: 所属的Nat网关Id
        :type NatGatewayId: str
        :param _NatGatewayName: Nat网关名称
        :type NatGatewayName: str
        """
        self._Eip = None
        self._NatGatewayId = None
        self._NatGatewayName = None

    @property
    def Eip(self):
        """弹性公网ip
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def NatGatewayId(self):
        """所属的Nat网关Id
        :rtype: str
        """
        return self._NatGatewayId

    @NatGatewayId.setter
    def NatGatewayId(self, NatGatewayId):
        self._NatGatewayId = NatGatewayId

    @property
    def NatGatewayName(self):
        """Nat网关名称
        :rtype: str
        """
        return self._NatGatewayName

    @NatGatewayName.setter
    def NatGatewayName(self, NatGatewayName):
        self._NatGatewayName = NatGatewayName


    def _deserialize(self, params):
        self._Eip = params.get("Eip")
        self._NatGatewayId = params.get("NatGatewayId")
        self._NatGatewayName = params.get("NatGatewayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatFwFilter(AbstractModel):
    """nat fw 实例展示的过滤列表

    """

    def __init__(self):
        r"""
        :param _FilterType: 过滤的类型，例如实例id
        :type FilterType: str
        :param _FilterContent: 过滤的内容，以',' 分隔
        :type FilterContent: str
        """
        self._FilterType = None
        self._FilterContent = None

    @property
    def FilterType(self):
        """过滤的类型，例如实例id
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def FilterContent(self):
        """过滤的内容，以',' 分隔
        :rtype: str
        """
        return self._FilterContent

    @FilterContent.setter
    def FilterContent(self, FilterContent):
        self._FilterContent = FilterContent


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._FilterContent = params.get("FilterContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatFwInstance(AbstractModel):
    """Nat实例类型

    """

    def __init__(self):
        r"""
        :param _NatinsId: nat实例id
        :type NatinsId: str
        :param _NatinsName: nat实例名称
        :type NatinsName: str
        :param _Region: 实例所在地域
        :type Region: str
        :param _FwMode: 0:新增模式，1:接入模式
        :type FwMode: int
        :param _Status: 0:正常状态， 1: 正在创建
        :type Status: int
        :param _NatIp: nat公网ip
        :type NatIp: str
        """
        self._NatinsId = None
        self._NatinsName = None
        self._Region = None
        self._FwMode = None
        self._Status = None
        self._NatIp = None

    @property
    def NatinsId(self):
        """nat实例id
        :rtype: str
        """
        return self._NatinsId

    @NatinsId.setter
    def NatinsId(self, NatinsId):
        self._NatinsId = NatinsId

    @property
    def NatinsName(self):
        """nat实例名称
        :rtype: str
        """
        return self._NatinsName

    @NatinsName.setter
    def NatinsName(self, NatinsName):
        self._NatinsName = NatinsName

    @property
    def Region(self):
        """实例所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FwMode(self):
        """0:新增模式，1:接入模式
        :rtype: int
        """
        return self._FwMode

    @FwMode.setter
    def FwMode(self, FwMode):
        self._FwMode = FwMode

    @property
    def Status(self):
        """0:正常状态， 1: 正在创建
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NatIp(self):
        """nat公网ip
        :rtype: str
        """
        return self._NatIp

    @NatIp.setter
    def NatIp(self, NatIp):
        self._NatIp = NatIp


    def _deserialize(self, params):
        self._NatinsId = params.get("NatinsId")
        self._NatinsName = params.get("NatinsName")
        self._Region = params.get("Region")
        self._FwMode = params.get("FwMode")
        self._Status = params.get("Status")
        self._NatIp = params.get("NatIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatInstanceInfo(AbstractModel):
    """Nat实例卡片详细信息

    """

    def __init__(self):
        r"""
        :param _NatinsId: nat实例id
        :type NatinsId: str
        :param _NatinsName: nat实例名称
        :type NatinsName: str
        :param _Region: 实例所在地域
        :type Region: str
        :param _FwMode: 0: 新增模式，1:接入模式
        :type FwMode: int
        :param _BandWidth: 实例带宽大小 Mbps
        :type BandWidth: int
        :param _InFlowMax: 入向带宽峰值 bps
        :type InFlowMax: int
        :param _OutFlowMax: 出向带宽峰值 bps
        :type OutFlowMax: int
        :param _RegionZh: 地域中文信息
        :type RegionZh: str
        :param _EipAddress: 公网ip数组
        :type EipAddress: list of str
        :param _VpcIp: 内外使用ip数组
        :type VpcIp: list of str
        :param _Subnets: 实例关联子网数组
        :type Subnets: list of str
        :param _Status: 0 :正常 1：正在初始化
        :type Status: int
        :param _RegionDetail: 地域区域信息
        :type RegionDetail: str
        :param _ZoneZh: 实例所在可用区
        :type ZoneZh: str
        :param _ZoneZhBak: 实例所在可用区
        :type ZoneZhBak: str
        :param _RuleUsed: 已使用规则数
        :type RuleUsed: int
        :param _RuleMax: 实例的规则限制最大规格数
        :type RuleMax: int
        :param _EngineVersion: 实例引擎版本
        :type EngineVersion: str
        :param _UpdateEnable: 引擎是否可升级：0，不可升级；1，可升级
        :type UpdateEnable: int
        :param _NeedProbeEngineUpdate: 是的需要升级引擎 支持 nat拨测 1需要 0不需要
        :type NeedProbeEngineUpdate: int
        :param _TrafficMode: 引擎运行模式，Normal:正常, OnlyRoute:透明模式
        :type TrafficMode: str
        :param _Zone: 实例主所在可用区
        :type Zone: str
        :param _ZoneBak: 实例备所在可用区
        :type ZoneBak: str
        :param _ReserveTime: 引擎预约升级时间
        :type ReserveTime: str
        :param _ReserveVersion: 引擎预约升级版本
        :type ReserveVersion: str
        :param _ReserveVersionState: 引擎预约升级版本状态 stable:稳定版；previewed:预览版
        :type ReserveVersionState: str
        :param _ElasticSwitch: 弹性开关
1 打开
0 关闭
        :type ElasticSwitch: int
        :param _ElasticBandwidth: 弹性带宽，单位Mbps
        :type ElasticBandwidth: int
        :param _IsFirstAfterPay: 是否首次开通按量付费
1 是
0 不是
        :type IsFirstAfterPay: int
        """
        self._NatinsId = None
        self._NatinsName = None
        self._Region = None
        self._FwMode = None
        self._BandWidth = None
        self._InFlowMax = None
        self._OutFlowMax = None
        self._RegionZh = None
        self._EipAddress = None
        self._VpcIp = None
        self._Subnets = None
        self._Status = None
        self._RegionDetail = None
        self._ZoneZh = None
        self._ZoneZhBak = None
        self._RuleUsed = None
        self._RuleMax = None
        self._EngineVersion = None
        self._UpdateEnable = None
        self._NeedProbeEngineUpdate = None
        self._TrafficMode = None
        self._Zone = None
        self._ZoneBak = None
        self._ReserveTime = None
        self._ReserveVersion = None
        self._ReserveVersionState = None
        self._ElasticSwitch = None
        self._ElasticBandwidth = None
        self._IsFirstAfterPay = None

    @property
    def NatinsId(self):
        """nat实例id
        :rtype: str
        """
        return self._NatinsId

    @NatinsId.setter
    def NatinsId(self, NatinsId):
        self._NatinsId = NatinsId

    @property
    def NatinsName(self):
        """nat实例名称
        :rtype: str
        """
        return self._NatinsName

    @NatinsName.setter
    def NatinsName(self, NatinsName):
        self._NatinsName = NatinsName

    @property
    def Region(self):
        """实例所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FwMode(self):
        """0: 新增模式，1:接入模式
        :rtype: int
        """
        return self._FwMode

    @FwMode.setter
    def FwMode(self, FwMode):
        self._FwMode = FwMode

    @property
    def BandWidth(self):
        """实例带宽大小 Mbps
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def InFlowMax(self):
        """入向带宽峰值 bps
        :rtype: int
        """
        return self._InFlowMax

    @InFlowMax.setter
    def InFlowMax(self, InFlowMax):
        self._InFlowMax = InFlowMax

    @property
    def OutFlowMax(self):
        """出向带宽峰值 bps
        :rtype: int
        """
        return self._OutFlowMax

    @OutFlowMax.setter
    def OutFlowMax(self, OutFlowMax):
        self._OutFlowMax = OutFlowMax

    @property
    def RegionZh(self):
        """地域中文信息
        :rtype: str
        """
        return self._RegionZh

    @RegionZh.setter
    def RegionZh(self, RegionZh):
        self._RegionZh = RegionZh

    @property
    def EipAddress(self):
        """公网ip数组
        :rtype: list of str
        """
        return self._EipAddress

    @EipAddress.setter
    def EipAddress(self, EipAddress):
        self._EipAddress = EipAddress

    @property
    def VpcIp(self):
        """内外使用ip数组
        :rtype: list of str
        """
        return self._VpcIp

    @VpcIp.setter
    def VpcIp(self, VpcIp):
        self._VpcIp = VpcIp

    @property
    def Subnets(self):
        """实例关联子网数组
        :rtype: list of str
        """
        return self._Subnets

    @Subnets.setter
    def Subnets(self, Subnets):
        self._Subnets = Subnets

    @property
    def Status(self):
        """0 :正常 1：正在初始化
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RegionDetail(self):
        """地域区域信息
        :rtype: str
        """
        return self._RegionDetail

    @RegionDetail.setter
    def RegionDetail(self, RegionDetail):
        self._RegionDetail = RegionDetail

    @property
    def ZoneZh(self):
        """实例所在可用区
        :rtype: str
        """
        return self._ZoneZh

    @ZoneZh.setter
    def ZoneZh(self, ZoneZh):
        self._ZoneZh = ZoneZh

    @property
    def ZoneZhBak(self):
        """实例所在可用区
        :rtype: str
        """
        return self._ZoneZhBak

    @ZoneZhBak.setter
    def ZoneZhBak(self, ZoneZhBak):
        self._ZoneZhBak = ZoneZhBak

    @property
    def RuleUsed(self):
        """已使用规则数
        :rtype: int
        """
        return self._RuleUsed

    @RuleUsed.setter
    def RuleUsed(self, RuleUsed):
        self._RuleUsed = RuleUsed

    @property
    def RuleMax(self):
        """实例的规则限制最大规格数
        :rtype: int
        """
        return self._RuleMax

    @RuleMax.setter
    def RuleMax(self, RuleMax):
        self._RuleMax = RuleMax

    @property
    def EngineVersion(self):
        """实例引擎版本
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def UpdateEnable(self):
        """引擎是否可升级：0，不可升级；1，可升级
        :rtype: int
        """
        return self._UpdateEnable

    @UpdateEnable.setter
    def UpdateEnable(self, UpdateEnable):
        self._UpdateEnable = UpdateEnable

    @property
    def NeedProbeEngineUpdate(self):
        """是的需要升级引擎 支持 nat拨测 1需要 0不需要
        :rtype: int
        """
        return self._NeedProbeEngineUpdate

    @NeedProbeEngineUpdate.setter
    def NeedProbeEngineUpdate(self, NeedProbeEngineUpdate):
        self._NeedProbeEngineUpdate = NeedProbeEngineUpdate

    @property
    def TrafficMode(self):
        """引擎运行模式，Normal:正常, OnlyRoute:透明模式
        :rtype: str
        """
        return self._TrafficMode

    @TrafficMode.setter
    def TrafficMode(self, TrafficMode):
        self._TrafficMode = TrafficMode

    @property
    def Zone(self):
        """实例主所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneBak(self):
        """实例备所在可用区
        :rtype: str
        """
        return self._ZoneBak

    @ZoneBak.setter
    def ZoneBak(self, ZoneBak):
        self._ZoneBak = ZoneBak

    @property
    def ReserveTime(self):
        """引擎预约升级时间
        :rtype: str
        """
        return self._ReserveTime

    @ReserveTime.setter
    def ReserveTime(self, ReserveTime):
        self._ReserveTime = ReserveTime

    @property
    def ReserveVersion(self):
        """引擎预约升级版本
        :rtype: str
        """
        return self._ReserveVersion

    @ReserveVersion.setter
    def ReserveVersion(self, ReserveVersion):
        self._ReserveVersion = ReserveVersion

    @property
    def ReserveVersionState(self):
        """引擎预约升级版本状态 stable:稳定版；previewed:预览版
        :rtype: str
        """
        return self._ReserveVersionState

    @ReserveVersionState.setter
    def ReserveVersionState(self, ReserveVersionState):
        self._ReserveVersionState = ReserveVersionState

    @property
    def ElasticSwitch(self):
        """弹性开关
1 打开
0 关闭
        :rtype: int
        """
        return self._ElasticSwitch

    @ElasticSwitch.setter
    def ElasticSwitch(self, ElasticSwitch):
        self._ElasticSwitch = ElasticSwitch

    @property
    def ElasticBandwidth(self):
        """弹性带宽，单位Mbps
        :rtype: int
        """
        return self._ElasticBandwidth

    @ElasticBandwidth.setter
    def ElasticBandwidth(self, ElasticBandwidth):
        self._ElasticBandwidth = ElasticBandwidth

    @property
    def IsFirstAfterPay(self):
        """是否首次开通按量付费
1 是
0 不是
        :rtype: int
        """
        return self._IsFirstAfterPay

    @IsFirstAfterPay.setter
    def IsFirstAfterPay(self, IsFirstAfterPay):
        self._IsFirstAfterPay = IsFirstAfterPay


    def _deserialize(self, params):
        self._NatinsId = params.get("NatinsId")
        self._NatinsName = params.get("NatinsName")
        self._Region = params.get("Region")
        self._FwMode = params.get("FwMode")
        self._BandWidth = params.get("BandWidth")
        self._InFlowMax = params.get("InFlowMax")
        self._OutFlowMax = params.get("OutFlowMax")
        self._RegionZh = params.get("RegionZh")
        self._EipAddress = params.get("EipAddress")
        self._VpcIp = params.get("VpcIp")
        self._Subnets = params.get("Subnets")
        self._Status = params.get("Status")
        self._RegionDetail = params.get("RegionDetail")
        self._ZoneZh = params.get("ZoneZh")
        self._ZoneZhBak = params.get("ZoneZhBak")
        self._RuleUsed = params.get("RuleUsed")
        self._RuleMax = params.get("RuleMax")
        self._EngineVersion = params.get("EngineVersion")
        self._UpdateEnable = params.get("UpdateEnable")
        self._NeedProbeEngineUpdate = params.get("NeedProbeEngineUpdate")
        self._TrafficMode = params.get("TrafficMode")
        self._Zone = params.get("Zone")
        self._ZoneBak = params.get("ZoneBak")
        self._ReserveTime = params.get("ReserveTime")
        self._ReserveVersion = params.get("ReserveVersion")
        self._ReserveVersionState = params.get("ReserveVersionState")
        self._ElasticSwitch = params.get("ElasticSwitch")
        self._ElasticBandwidth = params.get("ElasticBandwidth")
        self._IsFirstAfterPay = params.get("IsFirstAfterPay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetInstancesInfo(AbstractModel):
    """网络实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 网络实例ID
        :type InstanceId: str
        :param _InstanceName: 网络实例名称
        :type InstanceName: str
        :param _InstanceCidr: 网络cidr (多段以逗号分隔)
        :type InstanceCidr: str
        :param _Region: 网络实例所在地域
        :type Region: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceCidr = None
        self._Region = None

    @property
    def InstanceId(self):
        """网络实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """网络实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceCidr(self):
        """网络cidr (多段以逗号分隔)
        :rtype: str
        """
        return self._InstanceCidr

    @InstanceCidr.setter
    def InstanceCidr(self, InstanceCidr):
        self._InstanceCidr = InstanceCidr

    @property
    def Region(self):
        """网络实例所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceCidr = params.get("InstanceCidr")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewModeItems(AbstractModel):
    """新增模式传递参数

    """

    def __init__(self):
        r"""
        :param _VpcList: 新增模式下接入的vpc列表
        :type VpcList: list of str
        :param _Eips: 新增模式下绑定的出口弹性公网ip列表，其中Eips和AddCount至少传递一个。
        :type Eips: list of str
        :param _AddCount: 新增模式下新增绑定的出口弹性公网ip个数，其中Eips和AddCount至少传递一个。
        :type AddCount: int
        """
        self._VpcList = None
        self._Eips = None
        self._AddCount = None

    @property
    def VpcList(self):
        """新增模式下接入的vpc列表
        :rtype: list of str
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def Eips(self):
        """新增模式下绑定的出口弹性公网ip列表，其中Eips和AddCount至少传递一个。
        :rtype: list of str
        """
        return self._Eips

    @Eips.setter
    def Eips(self, Eips):
        self._Eips = Eips

    @property
    def AddCount(self):
        """新增模式下新增绑定的出口弹性公网ip个数，其中Eips和AddCount至少传递一个。
        :rtype: int
        """
        return self._AddCount

    @AddCount.setter
    def AddCount(self, AddCount):
        self._AddCount = AddCount


    def _deserialize(self, params):
        self._VpcList = params.get("VpcList")
        self._Eips = params.get("Eips")
        self._AddCount = params.get("AddCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAcRuleRequest(AbstractModel):
    """RemoveAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 规则的uuid，可通过查询规则列表获取
        :type RuleUuid: int
        """
        self._RuleUuid = None

    @property
    def RuleUuid(self):
        """规则的uuid，可通过查询规则列表获取
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAcRuleResponse(AbstractModel):
    """RemoveAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 删除成功后返回被删除策略的uuid
        :type RuleUuid: int
        :param _ReturnCode: 0代表成功，-1代表失败
        :type ReturnCode: int
        :param _ReturnMsg: success代表成功，failed代表失败
        :type ReturnMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._ReturnCode = None
        self._ReturnMsg = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """删除成功后返回被删除策略的uuid
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def ReturnCode(self):
        """0代表成功，-1代表失败
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        """success代表成功，failed代表失败
        :rtype: str
        """
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

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
        self._RuleUuid = params.get("RuleUuid")
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._RequestId = params.get("RequestId")


class RemoveAclRuleRequest(AbstractModel):
    """RemoveAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 规则的uuid列表，可通过查询规则列表获取，注意：如果传入的是[-1]将删除所有规则
        :type RuleUuid: list of int
        :param _Direction: 规则方向：1，入站；0，出站
        :type Direction: int
        """
        self._RuleUuid = None
        self._Direction = None

    @property
    def RuleUuid(self):
        """规则的uuid列表，可通过查询规则列表获取，注意：如果传入的是[-1]将删除所有规则
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def Direction(self):
        """规则方向：1，入站；0，出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveAclRuleResponse(AbstractModel):
    """RemoveAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 删除成功后返回被删除策略的uuid列表
        :type RuleUuid: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """删除成功后返回被删除策略的uuid列表
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

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
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class RemoveEnterpriseSecurityGroupRuleRequest(AbstractModel):
    """RemoveEnterpriseSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 规则的uuid，可通过查询规则列表获取
        :type RuleUuid: int
        :param _RemoveType: 删除类型，0是单条删除，RuleUuid填写删除规则id，1为全部删除，RuleUuid填0即可
        :type RemoveType: int
        """
        self._RuleUuid = None
        self._RemoveType = None

    @property
    def RuleUuid(self):
        """规则的uuid，可通过查询规则列表获取
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def RemoveType(self):
        """删除类型，0是单条删除，RuleUuid填写删除规则id，1为全部删除，RuleUuid填0即可
        :rtype: int
        """
        return self._RemoveType

    @RemoveType.setter
    def RemoveType(self, RemoveType):
        self._RemoveType = RemoveType


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._RemoveType = params.get("RemoveType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveEnterpriseSecurityGroupRuleResponse(AbstractModel):
    """RemoveEnterpriseSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 删除成功后返回被删除策略的uuid
        :type RuleUuid: int
        :param _Status: 0代表成功，-1代表失败
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._Status = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """删除成功后返回被删除策略的uuid
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def Status(self):
        """0代表成功，-1代表失败
        :rtype: int
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
        self._RuleUuid = params.get("RuleUuid")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class RemoveNatAcRuleRequest(AbstractModel):
    """RemoveNatAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 规则的uuid列表，可通过查询规则列表获取，注意：如果传入的是[-1]将删除所有规则
        :type RuleUuid: list of int
        :param _Direction: 规则方向：1，入站；0，出站
        :type Direction: int
        """
        self._RuleUuid = None
        self._Direction = None

    @property
    def RuleUuid(self):
        """规则的uuid列表，可通过查询规则列表获取，注意：如果传入的是[-1]将删除所有规则
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def Direction(self):
        """规则方向：1，入站；0，出站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._RuleUuid = params.get("RuleUuid")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNatAcRuleResponse(AbstractModel):
    """RemoveNatAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuid: 删除成功后返回被删除策略的uuid列表
        :type RuleUuid: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuid = None
        self._RequestId = None

    @property
    def RuleUuid(self):
        """删除成功后返回被删除策略的uuid列表
        :rtype: list of int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

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
        self._RuleUuid = params.get("RuleUuid")
        self._RequestId = params.get("RequestId")


class RemoveVpcAcRuleRequest(AbstractModel):
    """RemoveVpcAcRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuids: 规则的uuid列表，可通过查询规则列表获取，注意：如果传入的是[-1]将删除所有规则
        :type RuleUuids: list of int
        :param _IpVersion: 仅当RuleUuids为-1时有效；0：删除Ipv4规则，1：删除Ipv6规则；默认为Ipv4类型规则
        :type IpVersion: int
        """
        self._RuleUuids = None
        self._IpVersion = None

    @property
    def RuleUuids(self):
        """规则的uuid列表，可通过查询规则列表获取，注意：如果传入的是[-1]将删除所有规则
        :rtype: list of int
        """
        return self._RuleUuids

    @RuleUuids.setter
    def RuleUuids(self, RuleUuids):
        self._RuleUuids = RuleUuids

    @property
    def IpVersion(self):
        """仅当RuleUuids为-1时有效；0：删除Ipv4规则，1：删除Ipv6规则；默认为Ipv4类型规则
        :rtype: int
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion


    def _deserialize(self, params):
        self._RuleUuids = params.get("RuleUuids")
        self._IpVersion = params.get("IpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveVpcAcRuleResponse(AbstractModel):
    """RemoveVpcAcRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleUuids: 删除成功后返回被删除策略的uuid列表
        :type RuleUuids: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleUuids = None
        self._RequestId = None

    @property
    def RuleUuids(self):
        """删除成功后返回被删除策略的uuid列表
        :rtype: list of int
        """
        return self._RuleUuids

    @RuleUuids.setter
    def RuleUuids(self, RuleUuids):
        self._RuleUuids = RuleUuids

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
        self._RuleUuids = params.get("RuleUuids")
        self._RequestId = params.get("RequestId")


class RuleChangeItem(AbstractModel):
    """规则顺序变更项，由原始id值变为新的id值。

    """

    def __init__(self):
        r"""
        :param _OrderIndex: 原始sequence 值
        :type OrderIndex: int
        :param _NewOrderIndex: 新的sequence 值
        :type NewOrderIndex: int
        :param _IpVersion: Ip版本，0：IPv4，1：IPv6，默认为IPv4
        :type IpVersion: int
        """
        self._OrderIndex = None
        self._NewOrderIndex = None
        self._IpVersion = None

    @property
    def OrderIndex(self):
        """原始sequence 值
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def NewOrderIndex(self):
        """新的sequence 值
        :rtype: int
        """
        return self._NewOrderIndex

    @NewOrderIndex.setter
    def NewOrderIndex(self, NewOrderIndex):
        self._NewOrderIndex = NewOrderIndex

    @property
    def IpVersion(self):
        """Ip版本，0：IPv4，1：IPv6，默认为IPv4
        :rtype: int
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._NewOrderIndex = params.get("NewOrderIndex")
        self._IpVersion = params.get("IpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfoData(AbstractModel):
    """规则输入对象

    """

    def __init__(self):
        r"""
        :param _OrderIndex: 执行顺序
        :type OrderIndex: int
        :param _SourceIp: 访问源
        :type SourceIp: str
        :param _TargetIp: 访问目的
        :type TargetIp: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Strategy: 策略, 0：观察，1：阻断，2：放行
        :type Strategy: str
        :param _SourceType: 访问源类型，1是IP，3是域名，4是IP地址模板，5是域名地址模板
        :type SourceType: int
        :param _Direction: 方向，0：出站，1：入站
        :type Direction: int
        :param _Detail: 描述
        :type Detail: str
        :param _TargetType: 访问目的类型，1是IP，3是域名，4是IP地址模板，5是域名地址模板
        :type TargetType: int
        :param _Port: 端口
        :type Port: str
        :param _Id: id值
        :type Id: int
        :param _LogId: 日志id，从告警处创建必传，其它为空
        :type LogId: str
        :param _City: 城市Code
        :type City: int
        :param _Country: 国家Code
        :type Country: int
        :param _CloudCode: 云厂商，支持多个，以逗号分隔， 1:腾讯云（仅中国香港及海外）,2:阿里云,3:亚马逊云,4:华为云,5:微软云
        :type CloudCode: str
        :param _IsRegion: 是否为地域
        :type IsRegion: int
        :param _CityName: 城市名
        :type CityName: str
        :param _CountryName: 国家名
        :type CountryName: str
        :param _RegionIso: 国家二位iso代码或者省份缩写代码
        :type RegionIso: str
        """
        self._OrderIndex = None
        self._SourceIp = None
        self._TargetIp = None
        self._Protocol = None
        self._Strategy = None
        self._SourceType = None
        self._Direction = None
        self._Detail = None
        self._TargetType = None
        self._Port = None
        self._Id = None
        self._LogId = None
        self._City = None
        self._Country = None
        self._CloudCode = None
        self._IsRegion = None
        self._CityName = None
        self._CountryName = None
        self._RegionIso = None

    @property
    def OrderIndex(self):
        """执行顺序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceIp(self):
        """访问源
        :rtype: str
        """
        return self._SourceIp

    @SourceIp.setter
    def SourceIp(self, SourceIp):
        self._SourceIp = SourceIp

    @property
    def TargetIp(self):
        """访问目的
        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

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
    def Strategy(self):
        """策略, 0：观察，1：阻断，2：放行
        :rtype: str
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def SourceType(self):
        """访问源类型，1是IP，3是域名，4是IP地址模板，5是域名地址模板
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def Direction(self):
        """方向，0：出站，1：入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Detail(self):
        """描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def TargetType(self):
        """访问目的类型，1是IP，3是域名，4是IP地址模板，5是域名地址模板
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Port(self):
        """端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Id(self):
        """id值
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LogId(self):
        """日志id，从告警处创建必传，其它为空
        :rtype: str
        """
        return self._LogId

    @LogId.setter
    def LogId(self, LogId):
        self._LogId = LogId

    @property
    def City(self):
        """城市Code
        :rtype: int
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Country(self):
        """国家Code
        :rtype: int
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def CloudCode(self):
        """云厂商，支持多个，以逗号分隔， 1:腾讯云（仅中国香港及海外）,2:阿里云,3:亚马逊云,4:华为云,5:微软云
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode

    @property
    def IsRegion(self):
        """是否为地域
        :rtype: int
        """
        return self._IsRegion

    @IsRegion.setter
    def IsRegion(self, IsRegion):
        self._IsRegion = IsRegion

    @property
    def CityName(self):
        """城市名
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName

    @property
    def CountryName(self):
        """国家名
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName

    @property
    def RegionIso(self):
        """国家二位iso代码或者省份缩写代码
        :rtype: str
        """
        return self._RegionIso

    @RegionIso.setter
    def RegionIso(self, RegionIso):
        self._RegionIso = RegionIso


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._SourceIp = params.get("SourceIp")
        self._TargetIp = params.get("TargetIp")
        self._Protocol = params.get("Protocol")
        self._Strategy = params.get("Strategy")
        self._SourceType = params.get("SourceType")
        self._Direction = params.get("Direction")
        self._Detail = params.get("Detail")
        self._TargetType = params.get("TargetType")
        self._Port = params.get("Port")
        self._Id = params.get("Id")
        self._LogId = params.get("LogId")
        self._City = params.get("City")
        self._Country = params.get("Country")
        self._CloudCode = params.get("CloudCode")
        self._IsRegion = params.get("IsRegion")
        self._CityName = params.get("CityName")
        self._CountryName = params.get("CountryName")
        self._RegionIso = params.get("RegionIso")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanInfo(AbstractModel):
    """新手引导扫描信息

    """

    def __init__(self):
        r"""
        :param _ScanPercent: 进度
        :type ScanPercent: float
        :param _ScanResultInfo: 扫描结果信息
        :type ScanResultInfo: :class:`tencentcloud.cfw.v20190904.models.ScanResultInfo`
        :param _ScanStatus: 扫描状态 0扫描中 1完成  2未勾选自动扫描
        :type ScanStatus: int
        :param _ScanTime: 预计完成时间
        :type ScanTime: str
        """
        self._ScanPercent = None
        self._ScanResultInfo = None
        self._ScanStatus = None
        self._ScanTime = None

    @property
    def ScanPercent(self):
        """进度
        :rtype: float
        """
        return self._ScanPercent

    @ScanPercent.setter
    def ScanPercent(self, ScanPercent):
        self._ScanPercent = ScanPercent

    @property
    def ScanResultInfo(self):
        """扫描结果信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ScanResultInfo`
        """
        return self._ScanResultInfo

    @ScanResultInfo.setter
    def ScanResultInfo(self, ScanResultInfo):
        self._ScanResultInfo = ScanResultInfo

    @property
    def ScanStatus(self):
        """扫描状态 0扫描中 1完成  2未勾选自动扫描
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def ScanTime(self):
        """预计完成时间
        :rtype: str
        """
        return self._ScanTime

    @ScanTime.setter
    def ScanTime(self, ScanTime):
        self._ScanTime = ScanTime


    def _deserialize(self, params):
        self._ScanPercent = params.get("ScanPercent")
        if params.get("ScanResultInfo") is not None:
            self._ScanResultInfo = ScanResultInfo()
            self._ScanResultInfo._deserialize(params.get("ScanResultInfo"))
        self._ScanStatus = params.get("ScanStatus")
        self._ScanTime = params.get("ScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanResultInfo(AbstractModel):
    """新手引导扫描结果信息

    """

    def __init__(self):
        r"""
        :param _BanStatus: 是否禁封端口
        :type BanStatus: bool
        :param _IPNum: 防护ip数量
        :type IPNum: int
        :param _IPStatus: 是否开启防护
        :type IPStatus: bool
        :param _IdpStatus: 是否拦截攻击
        :type IdpStatus: bool
        :param _LeakNum: 暴露漏洞数量
        :type LeakNum: int
        :param _PortNum: 暴露端口数量
        :type PortNum: int
        """
        self._BanStatus = None
        self._IPNum = None
        self._IPStatus = None
        self._IdpStatus = None
        self._LeakNum = None
        self._PortNum = None

    @property
    def BanStatus(self):
        """是否禁封端口
        :rtype: bool
        """
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def IPNum(self):
        """防护ip数量
        :rtype: int
        """
        return self._IPNum

    @IPNum.setter
    def IPNum(self, IPNum):
        self._IPNum = IPNum

    @property
    def IPStatus(self):
        """是否开启防护
        :rtype: bool
        """
        return self._IPStatus

    @IPStatus.setter
    def IPStatus(self, IPStatus):
        self._IPStatus = IPStatus

    @property
    def IdpStatus(self):
        """是否拦截攻击
        :rtype: bool
        """
        return self._IdpStatus

    @IdpStatus.setter
    def IdpStatus(self, IdpStatus):
        self._IdpStatus = IdpStatus

    @property
    def LeakNum(self):
        """暴露漏洞数量
        :rtype: int
        """
        return self._LeakNum

    @LeakNum.setter
    def LeakNum(self, LeakNum):
        self._LeakNum = LeakNum

    @property
    def PortNum(self):
        """暴露端口数量
        :rtype: int
        """
        return self._PortNum

    @PortNum.setter
    def PortNum(self, PortNum):
        self._PortNum = PortNum


    def _deserialize(self, params):
        self._BanStatus = params.get("BanStatus")
        self._IPNum = params.get("IPNum")
        self._IPStatus = params.get("IPStatus")
        self._IdpStatus = params.get("IdpStatus")
        self._LeakNum = params.get("LeakNum")
        self._PortNum = params.get("PortNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogErrors(AbstractModel):
    """多日志主题检索错误信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _ErrorCodeStr: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCodeStr: str
        """
        self._TopicId = None
        self._ErrorMsg = None
        self._ErrorCodeStr = None

    @property
    def TopicId(self):
        """日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def ErrorMsg(self):
        """错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorCodeStr(self):
        """错误码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCodeStr

    @ErrorCodeStr.setter
    def ErrorCodeStr(self, ErrorCodeStr):
        self._ErrorCodeStr = ErrorCodeStr


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorCodeStr = params.get("ErrorCodeStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogInfos(AbstractModel):
    """多日志主题检索topic信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Period: 日志存储生命周期
        :type Period: int
        :param _Context: 透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        """
        self._TopicId = None
        self._Period = None
        self._Context = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Period(self):
        """日志存储生命周期
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Context(self):
        """透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._Period = params.get("Period")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogRequest(AbstractModel):
    """SearchLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _From: 要检索分析的日志的起始时间，Unix时间戳（毫秒）
        :type From: int
        :param _To: 要检索分析的日志的结束时间，Unix时间戳（毫秒）
        :type To: int
        :param _Query: 检索分析语句，最大长度为12KB
语句由 <a href="https://cloud.tencent.com/document/product/614/47044" target="_blank">[检索条件]</a> | <a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>构成，无需对日志进行统计分析时，可省略其中的管道符<code> | </code>及SQL语句
使用*或空字符串可查询所有日志
        :type Query: str
        :param _SyntaxRule: 检索语法规则，默认值为0，推荐使用1 。

- 0：Lucene语法
- 1：CQL语法（日志服务专用检索语法，控制台默认也使用该语法规则）。

详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :type SyntaxRule: int
        :param _TopicId: - 要检索分析的日志主题ID，仅能指定一个日志主题。
- 如需同时检索多个日志主题，请使用Topics参数。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
各日志主题ID如下
访问控制-互联网边界 cfw_rule_acl
访问控制-NAT边界 cfw_rule_nat_acl
访问控制-VPC边界 cfw_rule_vpc_acl
访问控制-DNS开关 cfw_rule_dns_acl
入侵防御 cfw_rule_threatinfo
全流量检测与响应日志-流量分析 cfw_netflow_nta
全流量检测与响应日志-流量告警 cfw_rule_ndr_threatinfo
零信任运维-数据库登录 cfw_operate_db
零信任运维-服务器访问 operate_remote_om
零信任运维-Web服务访问 operate_web_access
零信任运维-行为审计 remoteom_commands
流量日志-互联网边界 cfw_netflow_border
流量日志-NAT边界 cfw_netflow_nat
流量日志-VPC边界 cfw_netflow_vpc
流量日志-DNS开关 cfw_netflow_dns
流量日志-内网流量 cfw_netflow_fl
操作日志 operate_log_all
        :type TopicId: str
        :param _Topics: - 要检索分析的日志主题列表，最大支持50个日志主题。
- 检索单个日志主题时请使用TopicId。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
        :type Topics: list of MultiTopicSearchInformation
        :param _Sort: 原始日志是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果排序方式参考<a href="https://cloud.tencent.com/document/product/614/58978" target="_blank">SQL ORDER BY语法</a>
        :type Sort: str
        :param _Limit: 表示单次查询返回的原始日志条数，默认为100，最大值为1000。
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果条数指定方式参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>

可通过两种方式获取后续更多日志：
* Context:透传上次接口返回的Context值，获取后续更多日志，总计最多可获取1万条原始日志
* Offset:偏移量，表示从第几行开始返回原始日志，无日志条数限制
        :type Limit: int
        :param _Offset: 查询原始日志的偏移量，表示从第几行开始返回原始日志，默认为0。 
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* 不能与Context参数同时使用
* 仅适用于单日志主题检索
        :type Offset: int
        :param _Context: 透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时。
注意：
* 透传该参数时，请勿修改除该参数外的其它参数
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
* 仅当检索分析语句(Query)不包含SQL时有效，SQL获取后续结果参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :type Context: str
        :param _SamplingRate: 执行统计分析（Query中包含SQL）时，是否对原始日志先进行采样，再进行统计分析。
0：自动采样;
0～1：按指定采样率采样，例如0.02;
1：不采样，即精确分析
默认值为1
        :type SamplingRate: float
        :param _UseNewAnalysis: 为true代表使用新的检索结果返回方式，输出参数AnalysisRecords和Columns有效
为false时代表使用老的检索结果返回方式, 输出AnalysisResults和ColNames有效
两种返回方式在编码格式上有少量区别，建议使用true
        :type UseNewAnalysis: bool
        """
        self._From = None
        self._To = None
        self._Query = None
        self._SyntaxRule = None
        self._TopicId = None
        self._Topics = None
        self._Sort = None
        self._Limit = None
        self._Offset = None
        self._Context = None
        self._SamplingRate = None
        self._UseNewAnalysis = None

    @property
    def From(self):
        """要检索分析的日志的起始时间，Unix时间戳（毫秒）
        :rtype: int
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        """要检索分析的日志的结束时间，Unix时间戳（毫秒）
        :rtype: int
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Query(self):
        """检索分析语句，最大长度为12KB
语句由 <a href="https://cloud.tencent.com/document/product/614/47044" target="_blank">[检索条件]</a> | <a href="https://cloud.tencent.com/document/product/614/44061" target="_blank">[SQL语句]</a>构成，无需对日志进行统计分析时，可省略其中的管道符<code> | </code>及SQL语句
使用*或空字符串可查询所有日志
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def SyntaxRule(self):
        """检索语法规则，默认值为0，推荐使用1 。

- 0：Lucene语法
- 1：CQL语法（日志服务专用检索语法，控制台默认也使用该语法规则）。

详细说明参见<a href="https://cloud.tencent.com/document/product/614/47044#RetrievesConditionalRules" target="_blank">检索条件语法规则</a>
        :rtype: int
        """
        return self._SyntaxRule

    @SyntaxRule.setter
    def SyntaxRule(self, SyntaxRule):
        self._SyntaxRule = SyntaxRule

    @property
    def TopicId(self):
        """- 要检索分析的日志主题ID，仅能指定一个日志主题。
- 如需同时检索多个日志主题，请使用Topics参数。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
各日志主题ID如下
访问控制-互联网边界 cfw_rule_acl
访问控制-NAT边界 cfw_rule_nat_acl
访问控制-VPC边界 cfw_rule_vpc_acl
访问控制-DNS开关 cfw_rule_dns_acl
入侵防御 cfw_rule_threatinfo
全流量检测与响应日志-流量分析 cfw_netflow_nta
全流量检测与响应日志-流量告警 cfw_rule_ndr_threatinfo
零信任运维-数据库登录 cfw_operate_db
零信任运维-服务器访问 operate_remote_om
零信任运维-Web服务访问 operate_web_access
零信任运维-行为审计 remoteom_commands
流量日志-互联网边界 cfw_netflow_border
流量日志-NAT边界 cfw_netflow_nat
流量日志-VPC边界 cfw_netflow_vpc
流量日志-DNS开关 cfw_netflow_dns
流量日志-内网流量 cfw_netflow_fl
操作日志 operate_log_all
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Topics(self):
        """- 要检索分析的日志主题列表，最大支持50个日志主题。
- 检索单个日志主题时请使用TopicId。
- TopicId 和 Topics 不能同时使用，在一次请求中有且只能选择一个。
        :rtype: list of MultiTopicSearchInformation
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def Sort(self):
        """原始日志是否按时间排序返回；可选值：asc(升序)、desc(降序)，默认为 desc
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果排序方式参考<a href="https://cloud.tencent.com/document/product/614/58978" target="_blank">SQL ORDER BY语法</a>
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Limit(self):
        """表示单次查询返回的原始日志条数，默认为100，最大值为1000。
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* SQL结果条数指定方式参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>

可通过两种方式获取后续更多日志：
* Context:透传上次接口返回的Context值，获取后续更多日志，总计最多可获取1万条原始日志
* Offset:偏移量，表示从第几行开始返回原始日志，无日志条数限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """查询原始日志的偏移量，表示从第几行开始返回原始日志，默认为0。 
注意：
* 仅当检索分析语句(Query)不包含SQL时有效
* 不能与Context参数同时使用
* 仅适用于单日志主题检索
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Context(self):
        """透传上次接口返回的Context值，可获取后续更多日志，总计最多可获取1万条原始日志，过期时间1小时。
注意：
* 透传该参数时，请勿修改除该参数外的其它参数
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
* 仅当检索分析语句(Query)不包含SQL时有效，SQL获取后续结果参考<a href="https://cloud.tencent.com/document/product/614/58977" target="_blank">SQL LIMIT语法</a>
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def SamplingRate(self):
        """执行统计分析（Query中包含SQL）时，是否对原始日志先进行采样，再进行统计分析。
0：自动采样;
0～1：按指定采样率采样，例如0.02;
1：不采样，即精确分析
默认值为1
        :rtype: float
        """
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def UseNewAnalysis(self):
        """为true代表使用新的检索结果返回方式，输出参数AnalysisRecords和Columns有效
为false时代表使用老的检索结果返回方式, 输出AnalysisResults和ColNames有效
两种返回方式在编码格式上有少量区别，建议使用true
        :rtype: bool
        """
        return self._UseNewAnalysis

    @UseNewAnalysis.setter
    def UseNewAnalysis(self, UseNewAnalysis):
        self._UseNewAnalysis = UseNewAnalysis


    def _deserialize(self, params):
        self._From = params.get("From")
        self._To = params.get("To")
        self._Query = params.get("Query")
        self._SyntaxRule = params.get("SyntaxRule")
        self._TopicId = params.get("TopicId")
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = MultiTopicSearchInformation()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._Sort = params.get("Sort")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Context = params.get("Context")
        self._SamplingRate = params.get("SamplingRate")
        self._UseNewAnalysis = params.get("UseNewAnalysis")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogResponse(AbstractModel):
    """SearchLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时。
注意：
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
        :type Context: str
        :param _ListOver: 符合检索条件的日志是否已全部返回，如未全部返回可使用Context参数获取后续更多日志
注意：仅当检索分析语句(Query)不包含SQL时有效
        :type ListOver: bool
        :param _Analysis: 返回的是否为统计分析（即SQL）结果
        :type Analysis: bool
        :param _Results: 匹配检索条件的原始日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of LogInfo
        :param _ColNames: 日志统计分析结果的列名
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ColNames: list of str
        :param _AnalysisResults: 日志统计分析结果
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisResults: list of LogItems
        :param _AnalysisRecords: 日志统计分析结果
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisRecords: list of str
        :param _Columns: 日志统计分析结果的列属性
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of Column
        :param _SamplingRate: 本次统计分析使用的采样率
注意：此字段可能返回 null，表示取不到有效值。
        :type SamplingRate: float
        :param _Topics: 使用多日志主题检索时，各个日志主题的基本信息，例如报错信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: :class:`tencentcloud.cfw.v20190904.models.SearchLogTopics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._Analysis = None
        self._Results = None
        self._ColNames = None
        self._AnalysisResults = None
        self._AnalysisRecords = None
        self._Columns = None
        self._SamplingRate = None
        self._Topics = None
        self._RequestId = None

    @property
    def Context(self):
        """透传本次接口返回的Context值，可获取后续更多日志，过期时间1小时。
注意：
* 仅适用于单日志主题检索，检索多个日志主题时，请使用Topics中的Context
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        """符合检索条件的日志是否已全部返回，如未全部返回可使用Context参数获取后续更多日志
注意：仅当检索分析语句(Query)不包含SQL时有效
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def Analysis(self):
        """返回的是否为统计分析（即SQL）结果
        :rtype: bool
        """
        return self._Analysis

    @Analysis.setter
    def Analysis(self, Analysis):
        self._Analysis = Analysis

    @property
    def Results(self):
        """匹配检索条件的原始日志
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogInfo
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def ColNames(self):
        """日志统计分析结果的列名
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ColNames

    @ColNames.setter
    def ColNames(self, ColNames):
        self._ColNames = ColNames

    @property
    def AnalysisResults(self):
        """日志统计分析结果
当UseNewAnalysis为false时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogItems
        """
        return self._AnalysisResults

    @AnalysisResults.setter
    def AnalysisResults(self, AnalysisResults):
        self._AnalysisResults = AnalysisResults

    @property
    def AnalysisRecords(self):
        """日志统计分析结果
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AnalysisRecords

    @AnalysisRecords.setter
    def AnalysisRecords(self, AnalysisRecords):
        self._AnalysisRecords = AnalysisRecords

    @property
    def Columns(self):
        """日志统计分析结果的列属性
当UseNewAnalysis为true时生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Column
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def SamplingRate(self):
        """本次统计分析使用的采样率
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._SamplingRate

    @SamplingRate.setter
    def SamplingRate(self, SamplingRate):
        self._SamplingRate = SamplingRate

    @property
    def Topics(self):
        """使用多日志主题检索时，各个日志主题的基本信息，例如报错信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SearchLogTopics`
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

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
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        self._Analysis = params.get("Analysis")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Results.append(obj)
        self._ColNames = params.get("ColNames")
        if params.get("AnalysisResults") is not None:
            self._AnalysisResults = []
            for item in params.get("AnalysisResults"):
                obj = LogItems()
                obj._deserialize(item)
                self._AnalysisResults.append(obj)
        self._AnalysisRecords = params.get("AnalysisRecords")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = Column()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._SamplingRate = params.get("SamplingRate")
        if params.get("Topics") is not None:
            self._Topics = SearchLogTopics()
            self._Topics._deserialize(params.get("Topics"))
        self._RequestId = params.get("RequestId")


class SearchLogTopics(AbstractModel):
    """多主题检索返回信息

    """

    def __init__(self):
        r"""
        :param _Errors: 多日志主题检索对应的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of SearchLogErrors
        :param _Infos: 多日志主题检索各日志主题信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Infos: list of SearchLogInfos
        """
        self._Errors = None
        self._Infos = None

    @property
    def Errors(self):
        """多日志主题检索对应的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SearchLogErrors
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def Infos(self):
        """多日志主题检索各日志主题信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SearchLogInfos
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos


    def _deserialize(self, params):
        if params.get("Errors") is not None:
            self._Errors = []
            for item in params.get("Errors"):
                obj = SearchLogErrors()
                obj._deserialize(item)
                self._Errors.append(obj)
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = SearchLogInfos()
                obj._deserialize(item)
                self._Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupBothWayInfo(AbstractModel):
    """双向下发的企业安全组规则

    """

    def __init__(self):
        r"""
        :param _OrderIndex: 执行顺序
        :type OrderIndex: int
        :param _SourceId: 访问源
        :type SourceId: str
        :param _SourceType: 访问源类型，默认为0，0: IP, 1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100: 资产分组
        :type SourceType: int
        :param _TargetId: 访问目的
        :type TargetId: str
        :param _TargetType: 访问目的类型，默认为0，0: IP, 1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100: 资产分组
        :type TargetType: int
        :param _Protocol: 协议
        :type Protocol: str
        :param _Port: 目的端口
        :type Port: str
        :param _Strategy: 策略, 1：阻断，2：放行
        :type Strategy: int
        :param _Direction: 方向，0：出站，1：入站，默认1
        :type Direction: int
        :param _Region: 地域
        :type Region: str
        :param _Detail: 描述
        :type Detail: str
        :param _Status: 是否开关开启，0：未开启，1：开启
        :type Status: int
        :param _IsNew: 是否是正常规则，0：正常，1：异常
        :type IsNew: int
        :param _BothWay: 单/双向下发，0:单向下发，1：双向下发
        :type BothWay: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _PublicIp: 公网IP，多个以英文逗号分隔
        :type PublicIp: str
        :param _PrivateIp: 内网IP，多个以英文逗号分隔
        :type PrivateIp: str
        :param _Cidr: 掩码地址，多个以英文逗号分隔
        :type Cidr: str
        :param _ServiceTemplateId: 端口协议类型参数模板id
        :type ServiceTemplateId: str
        :param _ProtocolPortType: 是否使用端口协议模板，0：否，1：是
        :type ProtocolPortType: int
        """
        self._OrderIndex = None
        self._SourceId = None
        self._SourceType = None
        self._TargetId = None
        self._TargetType = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Direction = None
        self._Region = None
        self._Detail = None
        self._Status = None
        self._IsNew = None
        self._BothWay = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cidr = None
        self._ServiceTemplateId = None
        self._ProtocolPortType = None

    @property
    def OrderIndex(self):
        """执行顺序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceId(self):
        """访问源
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceType(self):
        """访问源类型，默认为0，0: IP, 1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100: 资产分组
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetId(self):
        """访问目的
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        """访问目的类型，默认为0，0: IP, 1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100: 资产分组
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

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
    def Port(self):
        """目的端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        """策略, 1：阻断，2：放行
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Direction(self):
        """方向，0：出站，1：入站，默认1
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Detail(self):
        """描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Status(self):
        """是否开关开启，0：未开启，1：开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsNew(self):
        """是否是正常规则，0：正常，1：异常
        :rtype: int
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def BothWay(self):
        """单/双向下发，0:单向下发，1：双向下发
        :rtype: int
        """
        return self._BothWay

    @BothWay.setter
    def BothWay(self, BothWay):
        self._BothWay = BothWay

    @property
    def VpcId(self):
        """私有网络ID
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
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        """公网IP，多个以英文逗号分隔
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """内网IP，多个以英文逗号分隔
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cidr(self):
        """掩码地址，多个以英文逗号分隔
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def ServiceTemplateId(self):
        """端口协议类型参数模板id
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def ProtocolPortType(self):
        """是否使用端口协议模板，0：否，1：是
        :rtype: int
        """
        return self._ProtocolPortType

    @ProtocolPortType.setter
    def ProtocolPortType(self, ProtocolPortType):
        self._ProtocolPortType = ProtocolPortType


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._SourceId = params.get("SourceId")
        self._SourceType = params.get("SourceType")
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Direction = params.get("Direction")
        self._Region = params.get("Region")
        self._Detail = params.get("Detail")
        self._Status = params.get("Status")
        self._IsNew = params.get("IsNew")
        self._BothWay = params.get("BothWay")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cidr = params.get("Cidr")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._ProtocolPortType = params.get("ProtocolPortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupListData(AbstractModel):
    """安全组列表数据

    """

    def __init__(self):
        r"""
        :param _OrderIndex: 执行顺序
        :type OrderIndex: int
        :param _SourceId: 访问源
        :type SourceId: str
        :param _SourceType: 访问源类型，默认为0，1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100: 资源组
        :type SourceType: int
        :param _TargetId: 访问目的
        :type TargetId: str
        :param _TargetType: 访问目的类型，默认为0，1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100:资源组
        :type TargetType: int
        :param _Protocol: 协议
        :type Protocol: str
        :param _Port: 目的端口
        :type Port: str
        :param _Strategy: 策略, 1：阻断，2：放行
        :type Strategy: int
        :param _Detail: 描述
        :type Detail: str
        :param _BothWay: 单/双向下发，0:单向下发，1：双向下发
        :type BothWay: int
        :param _Id: 规则ID
        :type Id: int
        :param _Status: 是否开关开启，0：未开启，1：开启
        :type Status: int
        :param _IsNew: 是否是正常规则，0：正常，1：异常
        :type IsNew: int
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _PublicIp: 公网IP，多个以英文逗号分隔
        :type PublicIp: str
        :param _PrivateIp: 内网IP，多个以英文逗号分隔
        :type PrivateIp: str
        :param _Cidr: 掩码地址，多个以英文逗号分隔
        :type Cidr: str
        :param _ServiceTemplateId: 端口协议类型参数模板id
        :type ServiceTemplateId: str
        :param _BothWayInfo: 生成双向下发规则
        :type BothWayInfo: list of SecurityGroupBothWayInfo
        :param _Direction: 方向，0：出站，1：入站，默认1
        :type Direction: int
        :param _ProtocolPortType: 是否使用端口协议模板，0：否，1：是
        :type ProtocolPortType: int
        :param _Uuid: Uuid
        :type Uuid: str
        :param _Region: 地域
        :type Region: str
        :param _AssetGroupNameIn: 资产分组名称
        :type AssetGroupNameIn: str
        :param _AssetGroupNameOut: 资产分组名称
        :type AssetGroupNameOut: str
        :param _ParameterName: 模板名称
        :type ParameterName: str
        :param _ProtocolPortName: 端口协议类型参数模板名称
        :type ProtocolPortName: str
        """
        self._OrderIndex = None
        self._SourceId = None
        self._SourceType = None
        self._TargetId = None
        self._TargetType = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Detail = None
        self._BothWay = None
        self._Id = None
        self._Status = None
        self._IsNew = None
        self._VpcId = None
        self._SubnetId = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cidr = None
        self._ServiceTemplateId = None
        self._BothWayInfo = None
        self._Direction = None
        self._ProtocolPortType = None
        self._Uuid = None
        self._Region = None
        self._AssetGroupNameIn = None
        self._AssetGroupNameOut = None
        self._ParameterName = None
        self._ProtocolPortName = None

    @property
    def OrderIndex(self):
        """执行顺序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def SourceId(self):
        """访问源
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceType(self):
        """访问源类型，默认为0，1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100: 资源组
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetId(self):
        """访问目的
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        """访问目的类型，默认为0，1: VPC, 2: SUBNET, 3: CVM, 4: CLB, 5: ENI, 6: CDB, 7: 参数模板, 100:资源组
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

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
    def Port(self):
        """目的端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        """策略, 1：阻断，2：放行
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Detail(self):
        """描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def BothWay(self):
        """单/双向下发，0:单向下发，1：双向下发
        :rtype: int
        """
        return self._BothWay

    @BothWay.setter
    def BothWay(self, BothWay):
        self._BothWay = BothWay

    @property
    def Id(self):
        """规则ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        """是否开关开启，0：未开启，1：开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsNew(self):
        """是否是正常规则，0：正常，1：异常
        :rtype: int
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def VpcId(self):
        """私有网络ID
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
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        """公网IP，多个以英文逗号分隔
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        """内网IP，多个以英文逗号分隔
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cidr(self):
        """掩码地址，多个以英文逗号分隔
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def ServiceTemplateId(self):
        """端口协议类型参数模板id
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def BothWayInfo(self):
        """生成双向下发规则
        :rtype: list of SecurityGroupBothWayInfo
        """
        return self._BothWayInfo

    @BothWayInfo.setter
    def BothWayInfo(self, BothWayInfo):
        self._BothWayInfo = BothWayInfo

    @property
    def Direction(self):
        """方向，0：出站，1：入站，默认1
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def ProtocolPortType(self):
        """是否使用端口协议模板，0：否，1：是
        :rtype: int
        """
        return self._ProtocolPortType

    @ProtocolPortType.setter
    def ProtocolPortType(self, ProtocolPortType):
        self._ProtocolPortType = ProtocolPortType

    @property
    def Uuid(self):
        """Uuid
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AssetGroupNameIn(self):
        """资产分组名称
        :rtype: str
        """
        return self._AssetGroupNameIn

    @AssetGroupNameIn.setter
    def AssetGroupNameIn(self, AssetGroupNameIn):
        self._AssetGroupNameIn = AssetGroupNameIn

    @property
    def AssetGroupNameOut(self):
        """资产分组名称
        :rtype: str
        """
        return self._AssetGroupNameOut

    @AssetGroupNameOut.setter
    def AssetGroupNameOut(self, AssetGroupNameOut):
        self._AssetGroupNameOut = AssetGroupNameOut

    @property
    def ParameterName(self):
        """模板名称
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ProtocolPortName(self):
        """端口协议类型参数模板名称
        :rtype: str
        """
        return self._ProtocolPortName

    @ProtocolPortName.setter
    def ProtocolPortName(self, ProtocolPortName):
        self._ProtocolPortName = ProtocolPortName


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._SourceId = params.get("SourceId")
        self._SourceType = params.get("SourceType")
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Detail = params.get("Detail")
        self._BothWay = params.get("BothWay")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._IsNew = params.get("IsNew")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cidr = params.get("Cidr")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        if params.get("BothWayInfo") is not None:
            self._BothWayInfo = []
            for item in params.get("BothWayInfo"):
                obj = SecurityGroupBothWayInfo()
                obj._deserialize(item)
                self._BothWayInfo.append(obj)
        self._Direction = params.get("Direction")
        self._ProtocolPortType = params.get("ProtocolPortType")
        self._Uuid = params.get("Uuid")
        self._Region = params.get("Region")
        self._AssetGroupNameIn = params.get("AssetGroupNameIn")
        self._AssetGroupNameOut = params.get("AssetGroupNameOut")
        self._ParameterName = params.get("ParameterName")
        self._ProtocolPortName = params.get("ProtocolPortName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupOrderIndexData(AbstractModel):
    """企业安全组规则执行顺序修改对象

    """

    def __init__(self):
        r"""
        :param _OrderIndex: 企业安全组规则当前执行顺序
        :type OrderIndex: int
        :param _NewOrderIndex: 企业安全组规则更新目标执行顺序
        :type NewOrderIndex: int
        """
        self._OrderIndex = None
        self._NewOrderIndex = None

    @property
    def OrderIndex(self):
        """企业安全组规则当前执行顺序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def NewOrderIndex(self):
        """企业安全组规则更新目标执行顺序
        :rtype: int
        """
        return self._NewOrderIndex

    @NewOrderIndex.setter
    def NewOrderIndex(self, NewOrderIndex):
        self._NewOrderIndex = NewOrderIndex


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupRule(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        r"""
        :param _SourceContent: 访问源示例：
net：IP/CIDR(192.168.0.2)
template：参数模板id(ipm-dyodhpby)
instance：资产实例id(ins-123456)
resourcegroup：资产分组id(cfwrg-xxxx)
tag：资源标签({\"Key\":\"标签key值\",\"Value\":\"标签Value值\"})
region：地域(ap-gaungzhou)
        :type SourceContent: str
        :param _SourceType: 访问源类型，类型可以为以下6种：net|template|instance|resourcegroup|tag|region
        :type SourceType: str
        :param _DestContent: 访问目的示例：
net：IP/CIDR(192.168.0.2)
template：参数模板id(ipm-dyodhpby)
instance：资产实例id(ins-123456)
resourcegroup：资产分组id(cfwrg-xxxx)
tag：资源标签({\"Key\":\"标签key值\",\"Value\":\"标签Value值\"})
region：地域(ap-gaungzhou)
        :type DestContent: str
        :param _DestType: 访问目的类型，类型可以为以下6种：net|template|instance|resourcegroup|tag|region
        :type DestType: str
        :param _RuleAction: 访问控制策略中设置的流量通过云防火墙的方式。取值：
accept：放行
drop：拒绝
        :type RuleAction: str
        :param _Description: 规则描述 用于规则使用或者场景的描述，最多支持50个字符
        :type Description: str
        :param _OrderIndex: 规则顺序，-1表示最低，1表示最高，请勿和外层Type冲突（和外层的Type配合使用，当中间插入时，指定添加位置）
        :type OrderIndex: str
        :param _Protocol: 协议；TCP/UDP/ICMP/ICMPv6/ANY
        :type Protocol: str
        :param _Port: 访问控制策略的端口。取值：
-1/-1：全部端口
80：80端口
        :type Port: str
        :param _ServiceTemplateId: 端口协议类型参数模板id；协议端口模板id；与Protocol,Port互斥
        :type ServiceTemplateId: str
        :param _Id: （入参时无需填写，自动生成）规则对应的唯一id
        :type Id: str
        :param _Enable: （入参时Enable无意义；由通用配置中新增规则启用状态控制）
规则状态，true表示启用，false表示禁用
        :type Enable: str
        :param _Uid: 规则对应的唯一内部id
        :type Uid: str
        """
        self._SourceContent = None
        self._SourceType = None
        self._DestContent = None
        self._DestType = None
        self._RuleAction = None
        self._Description = None
        self._OrderIndex = None
        self._Protocol = None
        self._Port = None
        self._ServiceTemplateId = None
        self._Id = None
        self._Enable = None
        self._Uid = None

    @property
    def SourceContent(self):
        """访问源示例：
net：IP/CIDR(192.168.0.2)
template：参数模板id(ipm-dyodhpby)
instance：资产实例id(ins-123456)
resourcegroup：资产分组id(cfwrg-xxxx)
tag：资源标签({\"Key\":\"标签key值\",\"Value\":\"标签Value值\"})
region：地域(ap-gaungzhou)
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        """访问源类型，类型可以为以下6种：net|template|instance|resourcegroup|tag|region
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DestContent(self):
        """访问目的示例：
net：IP/CIDR(192.168.0.2)
template：参数模板id(ipm-dyodhpby)
instance：资产实例id(ins-123456)
resourcegroup：资产分组id(cfwrg-xxxx)
tag：资源标签({\"Key\":\"标签key值\",\"Value\":\"标签Value值\"})
region：地域(ap-gaungzhou)
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def DestType(self):
        """访问目的类型，类型可以为以下6种：net|template|instance|resourcegroup|tag|region
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def RuleAction(self):
        """访问控制策略中设置的流量通过云防火墙的方式。取值：
accept：放行
drop：拒绝
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        """规则描述 用于规则使用或者场景的描述，最多支持50个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OrderIndex(self):
        """规则顺序，-1表示最低，1表示最高，请勿和外层Type冲突（和外层的Type配合使用，当中间插入时，指定添加位置）
        :rtype: str
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Protocol(self):
        """协议；TCP/UDP/ICMP/ICMPv6/ANY
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """访问控制策略的端口。取值：
-1/-1：全部端口
80：80端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceTemplateId(self):
        """端口协议类型参数模板id；协议端口模板id；与Protocol,Port互斥
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def Id(self):
        """（入参时无需填写，自动生成）规则对应的唯一id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Enable(self):
        """（入参时Enable无意义；由通用配置中新增规则启用状态控制）
规则状态，true表示启用，false表示禁用
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Uid(self):
        """规则对应的唯一内部id
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._DestContent = params.get("DestContent")
        self._DestType = params.get("DestType")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._OrderIndex = params.get("OrderIndex")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._Id = params.get("Id")
        self._Enable = params.get("Enable")
        self._Uid = params.get("Uid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupSimplifyRule(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        r"""
        :param _SourceContent: 访问源示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
        :type SourceContent: str
        :param _DestContent: 访问目的示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
        :type DestContent: str
        :param _Protocol: 协议；TCP/UDP/ICMP/ANY
        :type Protocol: str
        :param _Description: 描述
        :type Description: str
        :param _RuleUuid: 规则对应的唯一id
        :type RuleUuid: int
        :param _Sequence: 规则序号
        :type Sequence: int
        """
        self._SourceContent = None
        self._DestContent = None
        self._Protocol = None
        self._Description = None
        self._RuleUuid = None
        self._Sequence = None

    @property
    def SourceContent(self):
        """访问源示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def DestContent(self):
        """访问目的示例：
net：IP/CIDR(192.168.0.2)
template：参数模板(ipm-dyodhpby)
instance：资产实例(ins-123456)
resourcegroup：资产分组(/全部分组/分组1/子分组1)
tag：资源标签({"Key":"标签key值","Value":"标签Value值"})
region：地域(ap-gaungzhou)
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def Protocol(self):
        """协议；TCP/UDP/ICMP/ANY
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

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
    def RuleUuid(self):
        """规则对应的唯一id
        :rtype: int
        """
        return self._RuleUuid

    @RuleUuid.setter
    def RuleUuid(self, RuleUuid):
        self._RuleUuid = RuleUuid

    @property
    def Sequence(self):
        """规则序号
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._DestContent = params.get("DestContent")
        self._Protocol = params.get("Protocol")
        self._Description = params.get("Description")
        self._RuleUuid = params.get("RuleUuid")
        self._Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SequenceData(AbstractModel):
    """执行顺序对象

    """

    def __init__(self):
        r"""
        :param _Id: 规则Id值
        :type Id: int
        :param _OrderIndex: 修改前执行顺序
        :type OrderIndex: int
        :param _NewOrderIndex: 修改后执行顺序
        :type NewOrderIndex: int
        """
        self._Id = None
        self._OrderIndex = None
        self._NewOrderIndex = None

    @property
    def Id(self):
        """规则Id值
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def OrderIndex(self):
        """修改前执行顺序
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def NewOrderIndex(self):
        """修改后执行顺序
        :rtype: int
        """
        return self._NewOrderIndex

    @NewOrderIndex.setter
    def NewOrderIndex(self, NewOrderIndex):
        self._NewOrderIndex = NewOrderIndex


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._OrderIndex = params.get("OrderIndex")
        self._NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleRequest(AbstractModel):
    """SetNatFwDnatRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 0：cfw新增模式，1：cfw接入模式。
        :type Mode: int
        :param _OperationType: 操作类型，可选值：add，del，modify。
        :type OperationType: str
        :param _CfwInstance: 防火墙实例id，该字段必须传递。
        :type CfwInstance: str
        :param _AddOrDelDnatRules: 添加或删除操作的Dnat规则列表。
        :type AddOrDelDnatRules: list of CfwNatDnatRule
        :param _OriginDnat: 修改操作的原始Dnat规则
        :type OriginDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        :param _NewDnat: 修改操作的新的Dnat规则
        :type NewDnat: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        self._Mode = None
        self._OperationType = None
        self._CfwInstance = None
        self._AddOrDelDnatRules = None
        self._OriginDnat = None
        self._NewDnat = None

    @property
    def Mode(self):
        """0：cfw新增模式，1：cfw接入模式。
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def OperationType(self):
        """操作类型，可选值：add，del，modify。
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def CfwInstance(self):
        """防火墙实例id，该字段必须传递。
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance

    @property
    def AddOrDelDnatRules(self):
        """添加或删除操作的Dnat规则列表。
        :rtype: list of CfwNatDnatRule
        """
        return self._AddOrDelDnatRules

    @AddOrDelDnatRules.setter
    def AddOrDelDnatRules(self, AddOrDelDnatRules):
        self._AddOrDelDnatRules = AddOrDelDnatRules

    @property
    def OriginDnat(self):
        """修改操作的原始Dnat规则
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        return self._OriginDnat

    @OriginDnat.setter
    def OriginDnat(self, OriginDnat):
        self._OriginDnat = OriginDnat

    @property
    def NewDnat(self):
        """修改操作的新的Dnat规则
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CfwNatDnatRule`
        """
        return self._NewDnat

    @NewDnat.setter
    def NewDnat(self, NewDnat):
        self._NewDnat = NewDnat


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._OperationType = params.get("OperationType")
        self._CfwInstance = params.get("CfwInstance")
        if params.get("AddOrDelDnatRules") is not None:
            self._AddOrDelDnatRules = []
            for item in params.get("AddOrDelDnatRules"):
                obj = CfwNatDnatRule()
                obj._deserialize(item)
                self._AddOrDelDnatRules.append(obj)
        if params.get("OriginDnat") is not None:
            self._OriginDnat = CfwNatDnatRule()
            self._OriginDnat._deserialize(params.get("OriginDnat"))
        if params.get("NewDnat") is not None:
            self._NewDnat = CfwNatDnatRule()
            self._NewDnat._deserialize(params.get("NewDnat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwDnatRuleResponse(AbstractModel):
    """SetNatFwDnatRule返回参数结构体

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


class SetNatFwEipRequest(AbstractModel):
    """SetNatFwEip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationType: bind：绑定eip；unbind：解绑eip；newAdd：新增防火墙弹性公网ip
        :type OperationType: str
        :param _CfwInstance: 防火墙实例id
        :type CfwInstance: str
        :param _EipList: 当OperationType 为bind或unbind操作时，使用该字段。
        :type EipList: list of str
        """
        self._OperationType = None
        self._CfwInstance = None
        self._EipList = None

    @property
    def OperationType(self):
        """bind：绑定eip；unbind：解绑eip；newAdd：新增防火墙弹性公网ip
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType

    @property
    def CfwInstance(self):
        """防火墙实例id
        :rtype: str
        """
        return self._CfwInstance

    @CfwInstance.setter
    def CfwInstance(self, CfwInstance):
        self._CfwInstance = CfwInstance

    @property
    def EipList(self):
        """当OperationType 为bind或unbind操作时，使用该字段。
        :rtype: list of str
        """
        return self._EipList

    @EipList.setter
    def EipList(self, EipList):
        self._EipList = EipList


    def _deserialize(self, params):
        self._OperationType = params.get("OperationType")
        self._CfwInstance = params.get("CfwInstance")
        self._EipList = params.get("EipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNatFwEipResponse(AbstractModel):
    """SetNatFwEip返回参数结构体

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


class SgDnsParseCount(AbstractModel):
    """企业安全组域名解析的IP统计

    """

    def __init__(self):
        r"""
        :param _ValidCount: 有效下发的IP个数，离散数据
        :type ValidCount: int
        :param _InvalidCount: 未下发的IP个数，离散数据
        :type InvalidCount: int
        """
        self._ValidCount = None
        self._InvalidCount = None

    @property
    def ValidCount(self):
        """有效下发的IP个数，离散数据
        :rtype: int
        """
        return self._ValidCount

    @ValidCount.setter
    def ValidCount(self, ValidCount):
        self._ValidCount = ValidCount

    @property
    def InvalidCount(self):
        """未下发的IP个数，离散数据
        :rtype: int
        """
        return self._InvalidCount

    @InvalidCount.setter
    def InvalidCount(self, InvalidCount):
        self._InvalidCount = InvalidCount


    def _deserialize(self, params):
        self._ValidCount = params.get("ValidCount")
        self._InvalidCount = params.get("InvalidCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticInfo(AbstractModel):
    """StaticInfo 告警柱形图统计信息

    """

    def __init__(self):
        r"""
        :param _Address: 地址
        :type Address: str
        :param _InsID: 资产id
        :type InsID: str
        :param _InsName: 资产名称
        :type InsName: str
        :param _Ip: ip信息
        :type Ip: str
        :param _Num: 数
        :type Num: int
        :param _Port: 端口
        :type Port: str
        """
        self._Address = None
        self._InsID = None
        self._InsName = None
        self._Ip = None
        self._Num = None
        self._Port = None

    @property
    def Address(self):
        """地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def InsID(self):
        """资产id
        :rtype: str
        """
        return self._InsID

    @InsID.setter
    def InsID(self, InsID):
        self._InsID = InsID

    @property
    def InsName(self):
        """资产名称
        :rtype: str
        """
        return self._InsName

    @InsName.setter
    def InsName(self, InsName):
        self._InsName = InsName

    @property
    def Ip(self):
        """ip信息
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Num(self):
        """数
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Port(self):
        """端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._InsID = params.get("InsID")
        self._InsName = params.get("InsName")
        self._Ip = params.get("Ip")
        self._Num = params.get("Num")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSecurityGroupRuleDispatchRequest(AbstractModel):
    """StopSecurityGroupRuleDispatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StopType: 值为1，中止全部
        :type StopType: int
        """
        self._StopType = None

    @property
    def StopType(self):
        """值为1，中止全部
        :rtype: int
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopSecurityGroupRuleDispatchResponse(AbstractModel):
    """StopSecurityGroupRuleDispatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: true代表成功，false代表错误
        :type Status: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """true代表成功，false代表错误
        :rtype: bool
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class SwitchListsData(AbstractModel):
    """防火墙开关列表对象

    """

    def __init__(self):
        r"""
        :param _PublicIp: 公网IP
        :type PublicIp: str
        :param _IntranetIp: 内网IP
        :type IntranetIp: str
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AssetType: 资产类型
        :type AssetType: str
        :param _Area: 地域
        :type Area: str
        :param _Switch: 防火墙开关
        :type Switch: int
        :param _Id: id值
        :type Id: int
        :param _PublicIpType: 公网 IP 类型
        :type PublicIpType: int
        :param _PortTimes: 风险端口数
        :type PortTimes: int
        :param _LastTime: 最近扫描时间
        :type LastTime: str
        :param _ScanMode: 扫描深度
        :type ScanMode: str
        :param _ScanStatus: 扫描状态
        :type ScanStatus: int
        """
        self._PublicIp = None
        self._IntranetIp = None
        self._InstanceName = None
        self._InstanceId = None
        self._AssetType = None
        self._Area = None
        self._Switch = None
        self._Id = None
        self._PublicIpType = None
        self._PortTimes = None
        self._LastTime = None
        self._ScanMode = None
        self._ScanStatus = None

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
    def IntranetIp(self):
        """内网IP
        :rtype: str
        """
        return self._IntranetIp

    @IntranetIp.setter
    def IntranetIp(self, IntranetIp):
        self._IntranetIp = IntranetIp

    @property
    def InstanceName(self):
        """实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

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
    def AssetType(self):
        """资产类型
        :rtype: str
        """
        return self._AssetType

    @AssetType.setter
    def AssetType(self, AssetType):
        self._AssetType = AssetType

    @property
    def Area(self):
        """地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Switch(self):
        """防火墙开关
        :rtype: int
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Id(self):
        """id值
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PublicIpType(self):
        """公网 IP 类型
        :rtype: int
        """
        return self._PublicIpType

    @PublicIpType.setter
    def PublicIpType(self, PublicIpType):
        self._PublicIpType = PublicIpType

    @property
    def PortTimes(self):
        """风险端口数
        :rtype: int
        """
        return self._PortTimes

    @PortTimes.setter
    def PortTimes(self, PortTimes):
        self._PortTimes = PortTimes

    @property
    def LastTime(self):
        """最近扫描时间
        :rtype: str
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def ScanMode(self):
        """扫描深度
        :rtype: str
        """
        return self._ScanMode

    @ScanMode.setter
    def ScanMode(self, ScanMode):
        self._ScanMode = ScanMode

    @property
    def ScanStatus(self):
        """扫描状态
        :rtype: int
        """
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus


    def _deserialize(self, params):
        self._PublicIp = params.get("PublicIp")
        self._IntranetIp = params.get("IntranetIp")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._AssetType = params.get("AssetType")
        self._Area = params.get("Area")
        self._Switch = params.get("Switch")
        self._Id = params.get("Id")
        self._PublicIpType = params.get("PublicIpType")
        self._PortTimes = params.get("PortTimes")
        self._LastTime = params.get("LastTime")
        self._ScanMode = params.get("ScanMode")
        self._ScanStatus = params.get("ScanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncFwOperateRequest(AbstractModel):
    """SyncFwOperate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncType: 同步操作类型：Route，同步防火墙路由
        :type SyncType: str
        :param _FwType: 防火墙类型；nat,nat防火墙;ew,vpc间防火墙
        :type FwType: str
        """
        self._SyncType = None
        self._FwType = None

    @property
    def SyncType(self):
        """同步操作类型：Route，同步防火墙路由
        :rtype: str
        """
        return self._SyncType

    @SyncType.setter
    def SyncType(self, SyncType):
        self._SyncType = SyncType

    @property
    def FwType(self):
        """防火墙类型；nat,nat防火墙;ew,vpc间防火墙
        :rtype: str
        """
        return self._FwType

    @FwType.setter
    def FwType(self, FwType):
        self._FwType = FwType


    def _deserialize(self, params):
        self._SyncType = params.get("SyncType")
        self._FwType = params.get("FwType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncFwOperateResponse(AbstractModel):
    """SyncFwOperate返回参数结构体

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


class TLogInfo(AbstractModel):
    """告警中心概览数据

    """

    def __init__(self):
        r"""
        :param _BanNum: 封禁列表
        :type BanNum: int
        :param _BruteForceNum: 暴力破解
        :type BruteForceNum: int
        :param _HandleNum: 待处置告警
        :type HandleNum: int
        :param _NetworkNum: 网络探测
        :type NetworkNum: int
        :param _OutNum: 失陷主机
        :type OutNum: int
        :param _VulNum: 漏洞攻击
        :type VulNum: int
        """
        self._BanNum = None
        self._BruteForceNum = None
        self._HandleNum = None
        self._NetworkNum = None
        self._OutNum = None
        self._VulNum = None

    @property
    def BanNum(self):
        """封禁列表
        :rtype: int
        """
        return self._BanNum

    @BanNum.setter
    def BanNum(self, BanNum):
        self._BanNum = BanNum

    @property
    def BruteForceNum(self):
        """暴力破解
        :rtype: int
        """
        return self._BruteForceNum

    @BruteForceNum.setter
    def BruteForceNum(self, BruteForceNum):
        self._BruteForceNum = BruteForceNum

    @property
    def HandleNum(self):
        """待处置告警
        :rtype: int
        """
        return self._HandleNum

    @HandleNum.setter
    def HandleNum(self, HandleNum):
        self._HandleNum = HandleNum

    @property
    def NetworkNum(self):
        """网络探测
        :rtype: int
        """
        return self._NetworkNum

    @NetworkNum.setter
    def NetworkNum(self, NetworkNum):
        self._NetworkNum = NetworkNum

    @property
    def OutNum(self):
        """失陷主机
        :rtype: int
        """
        return self._OutNum

    @OutNum.setter
    def OutNum(self, OutNum):
        self._OutNum = OutNum

    @property
    def VulNum(self):
        """漏洞攻击
        :rtype: int
        """
        return self._VulNum

    @VulNum.setter
    def VulNum(self, VulNum):
        self._VulNum = VulNum


    def _deserialize(self, params):
        self._BanNum = params.get("BanNum")
        self._BruteForceNum = params.get("BruteForceNum")
        self._HandleNum = params.get("HandleNum")
        self._NetworkNum = params.get("NetworkNum")
        self._OutNum = params.get("OutNum")
        self._VulNum = params.get("VulNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 目标key
        :type TagKey: str
        :param _TagValue: 目标值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """目标key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """目标值
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
        


class TemplateListInfo(AbstractModel):
    """地址模板列表数据

    """

    def __init__(self):
        r"""
        :param _Uuid: 模板ID
        :type Uuid: str
        :param _Name: 模板名称
        :type Name: str
        :param _Detail: 描述
        :type Detail: str
        :param _IpString: IP模板
        :type IpString: str
        :param _InsertTime: 插入时间
        :type InsertTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _Type: 模板类型
        :type Type: int
        :param _RulesNum: 关联规则条数
        :type RulesNum: int
        :param _TemplateId: 模板Id
        :type TemplateId: str
        :param _ProtocolType: 协议端口模板，协议类型，4:4层协议，7:7层协议
        :type ProtocolType: str
        :param _IPNum: 模板包含地址数量
        :type IPNum: int
        :param _IpVersion: IP版本,0,IPv4;1,IPv6
        :type IpVersion: int
        """
        self._Uuid = None
        self._Name = None
        self._Detail = None
        self._IpString = None
        self._InsertTime = None
        self._UpdateTime = None
        self._Type = None
        self._RulesNum = None
        self._TemplateId = None
        self._ProtocolType = None
        self._IPNum = None
        self._IpVersion = None

    @property
    def Uuid(self):
        """模板ID
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Name(self):
        """模板名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Detail(self):
        """描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def IpString(self):
        """IP模板
        :rtype: str
        """
        return self._IpString

    @IpString.setter
    def IpString(self, IpString):
        self._IpString = IpString

    @property
    def InsertTime(self):
        """插入时间
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def UpdateTime(self):
        """修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Type(self):
        """模板类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RulesNum(self):
        """关联规则条数
        :rtype: int
        """
        return self._RulesNum

    @RulesNum.setter
    def RulesNum(self, RulesNum):
        self._RulesNum = RulesNum

    @property
    def TemplateId(self):
        """模板Id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ProtocolType(self):
        """协议端口模板，协议类型，4:4层协议，7:7层协议
        :rtype: str
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def IPNum(self):
        """模板包含地址数量
        :rtype: int
        """
        return self._IPNum

    @IPNum.setter
    def IPNum(self, IPNum):
        self._IPNum = IPNum

    @property
    def IpVersion(self):
        """IP版本,0,IPv4;1,IPv6
        :rtype: int
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion


    def _deserialize(self, params):
        self._Uuid = params.get("Uuid")
        self._Name = params.get("Name")
        self._Detail = params.get("Detail")
        self._IpString = params.get("IpString")
        self._InsertTime = params.get("InsertTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Type = params.get("Type")
        self._RulesNum = params.get("RulesNum")
        self._TemplateId = params.get("TemplateId")
        self._ProtocolType = params.get("ProtocolType")
        self._IPNum = params.get("IPNum")
        self._IpVersion = params.get("IpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEvent(AbstractModel):
    """未处置事件详情

    """

    def __init__(self):
        r"""
        :param _EventTableListStruct: 伪攻击链类型
        :type EventTableListStruct: list of UnHandleEventDetail
        :param _BaseLineUser: 1 是  0否
        :type BaseLineUser: int
        :param _BaseLineInSwitch: 1 打开 0 关闭
        :type BaseLineInSwitch: int
        :param _BaseLineOutSwitch: 1 打开 0 关闭
        :type BaseLineOutSwitch: int
        :param _VpcFwCount: vpc间防火墙实例数量
        :type VpcFwCount: int
        """
        self._EventTableListStruct = None
        self._BaseLineUser = None
        self._BaseLineInSwitch = None
        self._BaseLineOutSwitch = None
        self._VpcFwCount = None

    @property
    def EventTableListStruct(self):
        """伪攻击链类型
        :rtype: list of UnHandleEventDetail
        """
        return self._EventTableListStruct

    @EventTableListStruct.setter
    def EventTableListStruct(self, EventTableListStruct):
        self._EventTableListStruct = EventTableListStruct

    @property
    def BaseLineUser(self):
        """1 是  0否
        :rtype: int
        """
        return self._BaseLineUser

    @BaseLineUser.setter
    def BaseLineUser(self, BaseLineUser):
        self._BaseLineUser = BaseLineUser

    @property
    def BaseLineInSwitch(self):
        """1 打开 0 关闭
        :rtype: int
        """
        return self._BaseLineInSwitch

    @BaseLineInSwitch.setter
    def BaseLineInSwitch(self, BaseLineInSwitch):
        self._BaseLineInSwitch = BaseLineInSwitch

    @property
    def BaseLineOutSwitch(self):
        """1 打开 0 关闭
        :rtype: int
        """
        return self._BaseLineOutSwitch

    @BaseLineOutSwitch.setter
    def BaseLineOutSwitch(self, BaseLineOutSwitch):
        self._BaseLineOutSwitch = BaseLineOutSwitch

    @property
    def VpcFwCount(self):
        """vpc间防火墙实例数量
        :rtype: int
        """
        return self._VpcFwCount

    @VpcFwCount.setter
    def VpcFwCount(self, VpcFwCount):
        self._VpcFwCount = VpcFwCount


    def _deserialize(self, params):
        if params.get("EventTableListStruct") is not None:
            self._EventTableListStruct = []
            for item in params.get("EventTableListStruct"):
                obj = UnHandleEventDetail()
                obj._deserialize(item)
                self._EventTableListStruct.append(obj)
        self._BaseLineUser = params.get("BaseLineUser")
        self._BaseLineInSwitch = params.get("BaseLineInSwitch")
        self._BaseLineOutSwitch = params.get("BaseLineOutSwitch")
        self._VpcFwCount = params.get("VpcFwCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnHandleEventDetail(AbstractModel):
    """未处置事件信息汇总

    """

    def __init__(self):
        r"""
        :param _EventName: 安全事件名称
        :type EventName: str
        :param _Total: 未处置事件数量
        :type Total: int
        """
        self._EventName = None
        self._Total = None

    @property
    def EventName(self):
        """安全事件名称
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def Total(self):
        """未处置事件数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcDnsInfo(AbstractModel):
    """nat防火墙 vpc dns 开关信息

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
        :type VpcId: str
        :param _VpcName: vpc 名称
        :type VpcName: str
        :param _FwMode: nat 防火墙模式 0：新增模式， 1: 接入模式
        :type FwMode: int
        :param _VpcIpv4Cidr: vpc ipv4网段范围 CIDR（Classless Inter-Domain Routing，无类域间路由选择）
        :type VpcIpv4Cidr: str
        :param _DNSEip: 外网弹性ip，防火墙 dns解析地址
        :type DNSEip: str
        :param _NatInsId: nat网关id
        :type NatInsId: str
        :param _NatInsName: nat网关名称
        :type NatInsName: str
        :param _SwitchStatus: 0：开关关闭 ， 1: 开关打开
        :type SwitchStatus: int
        :param _ProtectedStatus: 0：未防护， 1: 已防护，2：忽略此字段
        :type ProtectedStatus: int
        :param _SupportDNSFW: 是否支持DNS FW，0-不支持、1-支持
        :type SupportDNSFW: int
        """
        self._VpcId = None
        self._VpcName = None
        self._FwMode = None
        self._VpcIpv4Cidr = None
        self._DNSEip = None
        self._NatInsId = None
        self._NatInsName = None
        self._SwitchStatus = None
        self._ProtectedStatus = None
        self._SupportDNSFW = None

    @property
    def VpcId(self):
        """vpc id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VpcName(self):
        """vpc 名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def FwMode(self):
        """nat 防火墙模式 0：新增模式， 1: 接入模式
        :rtype: int
        """
        return self._FwMode

    @FwMode.setter
    def FwMode(self, FwMode):
        self._FwMode = FwMode

    @property
    def VpcIpv4Cidr(self):
        """vpc ipv4网段范围 CIDR（Classless Inter-Domain Routing，无类域间路由选择）
        :rtype: str
        """
        return self._VpcIpv4Cidr

    @VpcIpv4Cidr.setter
    def VpcIpv4Cidr(self, VpcIpv4Cidr):
        self._VpcIpv4Cidr = VpcIpv4Cidr

    @property
    def DNSEip(self):
        """外网弹性ip，防火墙 dns解析地址
        :rtype: str
        """
        return self._DNSEip

    @DNSEip.setter
    def DNSEip(self, DNSEip):
        self._DNSEip = DNSEip

    @property
    def NatInsId(self):
        """nat网关id
        :rtype: str
        """
        return self._NatInsId

    @NatInsId.setter
    def NatInsId(self, NatInsId):
        self._NatInsId = NatInsId

    @property
    def NatInsName(self):
        """nat网关名称
        :rtype: str
        """
        return self._NatInsName

    @NatInsName.setter
    def NatInsName(self, NatInsName):
        self._NatInsName = NatInsName

    @property
    def SwitchStatus(self):
        """0：开关关闭 ， 1: 开关打开
        :rtype: int
        """
        return self._SwitchStatus

    @SwitchStatus.setter
    def SwitchStatus(self, SwitchStatus):
        self._SwitchStatus = SwitchStatus

    @property
    def ProtectedStatus(self):
        """0：未防护， 1: 已防护，2：忽略此字段
        :rtype: int
        """
        return self._ProtectedStatus

    @ProtectedStatus.setter
    def ProtectedStatus(self, ProtectedStatus):
        self._ProtectedStatus = ProtectedStatus

    @property
    def SupportDNSFW(self):
        """是否支持DNS FW，0-不支持、1-支持
        :rtype: int
        """
        return self._SupportDNSFW

    @SupportDNSFW.setter
    def SupportDNSFW(self, SupportDNSFW):
        self._SupportDNSFW = SupportDNSFW


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._VpcName = params.get("VpcName")
        self._FwMode = params.get("FwMode")
        self._VpcIpv4Cidr = params.get("VpcIpv4Cidr")
        self._DNSEip = params.get("DNSEip")
        self._NatInsId = params.get("NatInsId")
        self._NatInsName = params.get("NatInsName")
        self._SwitchStatus = params.get("SwitchStatus")
        self._ProtectedStatus = params.get("ProtectedStatus")
        self._SupportDNSFW = params.get("SupportDNSFW")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcFwCvmInsInfo(AbstractModel):
    """VPC防火墙实例的CVM信息

    """

    def __init__(self):
        r"""
        :param _FwInsId: VPC防火墙实例ID
        :type FwInsId: str
        :param _Region: CVM所在地域
        :type Region: str
        :param _RegionZh: CVM所在地域中文
        :type RegionZh: str
        :param _RegionDetail: CVM所在地域详情
        :type RegionDetail: str
        :param _ZoneZh: 主机所在可用区
        :type ZoneZh: str
        :param _ZoneZhBack: 备机所在可用区
        :type ZoneZhBack: str
        :param _BandWidth: 防火墙CVM带宽值
        :type BandWidth: int
        :param _Zone: 实例主机所在可用区
        :type Zone: str
        :param _ZoneBak: 实例备机所在可用区
        :type ZoneBak: str
        """
        self._FwInsId = None
        self._Region = None
        self._RegionZh = None
        self._RegionDetail = None
        self._ZoneZh = None
        self._ZoneZhBack = None
        self._BandWidth = None
        self._Zone = None
        self._ZoneBak = None

    @property
    def FwInsId(self):
        """VPC防火墙实例ID
        :rtype: str
        """
        return self._FwInsId

    @FwInsId.setter
    def FwInsId(self, FwInsId):
        self._FwInsId = FwInsId

    @property
    def Region(self):
        """CVM所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionZh(self):
        """CVM所在地域中文
        :rtype: str
        """
        return self._RegionZh

    @RegionZh.setter
    def RegionZh(self, RegionZh):
        self._RegionZh = RegionZh

    @property
    def RegionDetail(self):
        """CVM所在地域详情
        :rtype: str
        """
        return self._RegionDetail

    @RegionDetail.setter
    def RegionDetail(self, RegionDetail):
        self._RegionDetail = RegionDetail

    @property
    def ZoneZh(self):
        """主机所在可用区
        :rtype: str
        """
        return self._ZoneZh

    @ZoneZh.setter
    def ZoneZh(self, ZoneZh):
        self._ZoneZh = ZoneZh

    @property
    def ZoneZhBack(self):
        """备机所在可用区
        :rtype: str
        """
        return self._ZoneZhBack

    @ZoneZhBack.setter
    def ZoneZhBack(self, ZoneZhBack):
        self._ZoneZhBack = ZoneZhBack

    @property
    def BandWidth(self):
        """防火墙CVM带宽值
        :rtype: int
        """
        return self._BandWidth

    @BandWidth.setter
    def BandWidth(self, BandWidth):
        self._BandWidth = BandWidth

    @property
    def Zone(self):
        """实例主机所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneBak(self):
        """实例备机所在可用区
        :rtype: str
        """
        return self._ZoneBak

    @ZoneBak.setter
    def ZoneBak(self, ZoneBak):
        self._ZoneBak = ZoneBak


    def _deserialize(self, params):
        self._FwInsId = params.get("FwInsId")
        self._Region = params.get("Region")
        self._RegionZh = params.get("RegionZh")
        self._RegionDetail = params.get("RegionDetail")
        self._ZoneZh = params.get("ZoneZh")
        self._ZoneZhBack = params.get("ZoneZhBack")
        self._BandWidth = params.get("BandWidth")
        self._Zone = params.get("Zone")
        self._ZoneBak = params.get("ZoneBak")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcFwGroupInfo(AbstractModel):
    """VPC防火墙(组)及防火墙实例详情信息

    """

    def __init__(self):
        r"""
        :param _FwGroupId: 防火墙(组)ID
        :type FwGroupId: str
        :param _FwGroupName: 防火墙(组)名称
        :type FwGroupName: str
        :param _FwSwitchNum: 防火墙组涉及到的开关个数
        :type FwSwitchNum: int
        :param _RegionLst: 防火墙(组)部署的地域
        :type RegionLst: list of str
        :param _Mode: 模式 1：CCN云联网模式；0：私有网络模式 2: sase 模式 3：ccn 高级模式 4: 私有网络(跨租户单边模式)
        :type Mode: int
        :param _SwitchMode: 防火墙实例的开关模式 1: 单点互通 2: 多点互通 3: 全互通 4: 自定义路由
        :type SwitchMode: int
        :param _FwInstanceLst: VPC防火墙实例卡片信息数组
        :type FwInstanceLst: list of VpcFwInstanceInfo
        :param _Status: 防火墙(状态) 0：正常 1: 初始化或操作中
        :type Status: int
        :param _FwVpcCidr: auto :自动选择
如果为网段，则为用户自定义 192.168.0.0/20 
        :type FwVpcCidr: str
        :param _CdcId: cdc专用集群场景时表示部署所属的cdc
        :type CdcId: str
        :param _CdcName: cdc专用集群场景时表示cdc名称
        :type CdcName: str
        :param _CrossUserMode: 跨租户模式 1管理员 2单边 0 非跨租户
        :type CrossUserMode: str
        :param _NeedSwitchCcnOverlap: 云联网模式下，当前实例是否需要开启重叠路由开关，1：需要开启，0：不需要开启
        :type NeedSwitchCcnOverlap: int
        :param _CcnId: 云联网模式下，实例关联的云联网id
        :type CcnId: str
        """
        self._FwGroupId = None
        self._FwGroupName = None
        self._FwSwitchNum = None
        self._RegionLst = None
        self._Mode = None
        self._SwitchMode = None
        self._FwInstanceLst = None
        self._Status = None
        self._FwVpcCidr = None
        self._CdcId = None
        self._CdcName = None
        self._CrossUserMode = None
        self._NeedSwitchCcnOverlap = None
        self._CcnId = None

    @property
    def FwGroupId(self):
        """防火墙(组)ID
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def FwGroupName(self):
        """防火墙(组)名称
        :rtype: str
        """
        return self._FwGroupName

    @FwGroupName.setter
    def FwGroupName(self, FwGroupName):
        self._FwGroupName = FwGroupName

    @property
    def FwSwitchNum(self):
        """防火墙组涉及到的开关个数
        :rtype: int
        """
        return self._FwSwitchNum

    @FwSwitchNum.setter
    def FwSwitchNum(self, FwSwitchNum):
        self._FwSwitchNum = FwSwitchNum

    @property
    def RegionLst(self):
        """防火墙(组)部署的地域
        :rtype: list of str
        """
        return self._RegionLst

    @RegionLst.setter
    def RegionLst(self, RegionLst):
        self._RegionLst = RegionLst

    @property
    def Mode(self):
        """模式 1：CCN云联网模式；0：私有网络模式 2: sase 模式 3：ccn 高级模式 4: 私有网络(跨租户单边模式)
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SwitchMode(self):
        """防火墙实例的开关模式 1: 单点互通 2: 多点互通 3: 全互通 4: 自定义路由
        :rtype: int
        """
        return self._SwitchMode

    @SwitchMode.setter
    def SwitchMode(self, SwitchMode):
        self._SwitchMode = SwitchMode

    @property
    def FwInstanceLst(self):
        """VPC防火墙实例卡片信息数组
        :rtype: list of VpcFwInstanceInfo
        """
        return self._FwInstanceLst

    @FwInstanceLst.setter
    def FwInstanceLst(self, FwInstanceLst):
        self._FwInstanceLst = FwInstanceLst

    @property
    def Status(self):
        """防火墙(状态) 0：正常 1: 初始化或操作中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FwVpcCidr(self):
        """auto :自动选择
如果为网段，则为用户自定义 192.168.0.0/20 
        :rtype: str
        """
        return self._FwVpcCidr

    @FwVpcCidr.setter
    def FwVpcCidr(self, FwVpcCidr):
        self._FwVpcCidr = FwVpcCidr

    @property
    def CdcId(self):
        """cdc专用集群场景时表示部署所属的cdc
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def CdcName(self):
        """cdc专用集群场景时表示cdc名称
        :rtype: str
        """
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CrossUserMode(self):
        """跨租户模式 1管理员 2单边 0 非跨租户
        :rtype: str
        """
        return self._CrossUserMode

    @CrossUserMode.setter
    def CrossUserMode(self, CrossUserMode):
        self._CrossUserMode = CrossUserMode

    @property
    def NeedSwitchCcnOverlap(self):
        """云联网模式下，当前实例是否需要开启重叠路由开关，1：需要开启，0：不需要开启
        :rtype: int
        """
        return self._NeedSwitchCcnOverlap

    @NeedSwitchCcnOverlap.setter
    def NeedSwitchCcnOverlap(self, NeedSwitchCcnOverlap):
        self._NeedSwitchCcnOverlap = NeedSwitchCcnOverlap

    @property
    def CcnId(self):
        """云联网模式下，实例关联的云联网id
        :rtype: str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId


    def _deserialize(self, params):
        self._FwGroupId = params.get("FwGroupId")
        self._FwGroupName = params.get("FwGroupName")
        self._FwSwitchNum = params.get("FwSwitchNum")
        self._RegionLst = params.get("RegionLst")
        self._Mode = params.get("Mode")
        self._SwitchMode = params.get("SwitchMode")
        if params.get("FwInstanceLst") is not None:
            self._FwInstanceLst = []
            for item in params.get("FwInstanceLst"):
                obj = VpcFwInstanceInfo()
                obj._deserialize(item)
                self._FwInstanceLst.append(obj)
        self._Status = params.get("Status")
        self._FwVpcCidr = params.get("FwVpcCidr")
        self._CdcId = params.get("CdcId")
        self._CdcName = params.get("CdcName")
        self._CrossUserMode = params.get("CrossUserMode")
        self._NeedSwitchCcnOverlap = params.get("NeedSwitchCcnOverlap")
        self._CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcFwInstance(AbstractModel):
    """vpc 防火墙下单防火墙实例结构体

    """

    def __init__(self):
        r"""
        :param _Name: 防火墙实例名称
        :type Name: str
        :param _VpcIds: 私有网络模式下接入的VpcId列表；仅私有网络模式使用
        :type VpcIds: list of str
        :param _FwDeploy: 部署地域信息
        :type FwDeploy: :class:`tencentcloud.cfw.v20190904.models.FwDeploy`
        :param _FwInsId: 防火墙实例ID (编辑场景传)
        :type FwInsId: str
        """
        self._Name = None
        self._VpcIds = None
        self._FwDeploy = None
        self._FwInsId = None

    @property
    def Name(self):
        """防火墙实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VpcIds(self):
        """私有网络模式下接入的VpcId列表；仅私有网络模式使用
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def FwDeploy(self):
        """部署地域信息
        :rtype: :class:`tencentcloud.cfw.v20190904.models.FwDeploy`
        """
        return self._FwDeploy

    @FwDeploy.setter
    def FwDeploy(self, FwDeploy):
        self._FwDeploy = FwDeploy

    @property
    def FwInsId(self):
        """防火墙实例ID (编辑场景传)
        :rtype: str
        """
        return self._FwInsId

    @FwInsId.setter
    def FwInsId(self, FwInsId):
        self._FwInsId = FwInsId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._VpcIds = params.get("VpcIds")
        if params.get("FwDeploy") is not None:
            self._FwDeploy = FwDeploy()
            self._FwDeploy._deserialize(params.get("FwDeploy"))
        self._FwInsId = params.get("FwInsId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcFwInstanceInfo(AbstractModel):
    """VPC防火墙实例卡片信息

    """

    def __init__(self):
        r"""
        :param _FwInsName: VPC防火墙实例名称
        :type FwInsName: str
        :param _FwInsId: VPC防火墙实例ID
        :type FwInsId: str
        :param _FwMode: VPC防火墙实例模式 0: 旧VPC模式防火墙 1: CCN模式防火墙
        :type FwMode: int
        :param _JoinInsNum: VPC防火墙接入网络实例个数
        :type JoinInsNum: int
        :param _FwSwitchNum: VPC防火墙开关个数
        :type FwSwitchNum: int
        :param _Status: VPC防火墙状态 0:正常 ， 1：创建中 2: 变更中
        :type Status: int
        :param _Time: VPC防火墙创建时间
        :type Time: str
        :param _CcnId: VPC 相关云联网ID列表
        :type CcnId: list of str
        :param _CcnName: VPC 相关云联网名称列表
        :type CcnName: list of str
        :param _PeerConnectionId: VPC 相关对等连接ID列表
        :type PeerConnectionId: list of str
        :param _PeerConnectionName: VPC 相关对等连接名称列表
        :type PeerConnectionName: list of str
        :param _FwCvmLst: VPC防火墙CVM的列表
        :type FwCvmLst: list of VpcFwCvmInsInfo
        :param _JoinInsLst: VPC防火墙接入网络实例类型列表
        :type JoinInsLst: list of VpcFwJoinInstanceType
        :param _FwGateway: 防火墙网关信息
        :type FwGateway: list of FwGateway
        :param _FwGroupId: 防火墙(组)ID
        :type FwGroupId: str
        :param _RuleUsed: 已使用规则数
        :type RuleUsed: int
        :param _RuleMax: 最大规则数
        :type RuleMax: int
        :param _Width: 防火墙实例带宽
        :type Width: int
        :param _UserVpcWidth: 用户VPC墙总带宽
        :type UserVpcWidth: int
        :param _JoinInsIdLst: 接入的vpc列表
        :type JoinInsIdLst: list of str
        :param _FlowMax: 内网间峰值带宽 (单位 bps )
        :type FlowMax: int
        :param _EngineVersion: 实例引擎版本
        :type EngineVersion: str
        :param _UpdateEnable: 引擎是否可升级：0，不可升级；1，可升级
        :type UpdateEnable: int
        :param _TrafficMode: 引擎运行模式，Normal:正常, OnlyRoute:透明模式
        :type TrafficMode: str
        :param _ReserveTime: 引擎预约升级时间
        :type ReserveTime: str
        :param _ReserveVersion: 预约引擎升级版本
        :type ReserveVersion: str
        :param _ReserveVersionState: 引擎预约升级版本状态
        :type ReserveVersionState: str
        :param _ElasticSwitch: 弹性开关 1打开 0关闭
        :type ElasticSwitch: int
        :param _ElasticBandwidth: 弹性带宽，单位Mbps
        :type ElasticBandwidth: int
        :param _IsFirstAfterPay: 是否首次开通按量付费
1 是
0 不是
        :type IsFirstAfterPay: int
        """
        self._FwInsName = None
        self._FwInsId = None
        self._FwMode = None
        self._JoinInsNum = None
        self._FwSwitchNum = None
        self._Status = None
        self._Time = None
        self._CcnId = None
        self._CcnName = None
        self._PeerConnectionId = None
        self._PeerConnectionName = None
        self._FwCvmLst = None
        self._JoinInsLst = None
        self._FwGateway = None
        self._FwGroupId = None
        self._RuleUsed = None
        self._RuleMax = None
        self._Width = None
        self._UserVpcWidth = None
        self._JoinInsIdLst = None
        self._FlowMax = None
        self._EngineVersion = None
        self._UpdateEnable = None
        self._TrafficMode = None
        self._ReserveTime = None
        self._ReserveVersion = None
        self._ReserveVersionState = None
        self._ElasticSwitch = None
        self._ElasticBandwidth = None
        self._IsFirstAfterPay = None

    @property
    def FwInsName(self):
        """VPC防火墙实例名称
        :rtype: str
        """
        return self._FwInsName

    @FwInsName.setter
    def FwInsName(self, FwInsName):
        self._FwInsName = FwInsName

    @property
    def FwInsId(self):
        """VPC防火墙实例ID
        :rtype: str
        """
        return self._FwInsId

    @FwInsId.setter
    def FwInsId(self, FwInsId):
        self._FwInsId = FwInsId

    @property
    def FwMode(self):
        """VPC防火墙实例模式 0: 旧VPC模式防火墙 1: CCN模式防火墙
        :rtype: int
        """
        return self._FwMode

    @FwMode.setter
    def FwMode(self, FwMode):
        self._FwMode = FwMode

    @property
    def JoinInsNum(self):
        """VPC防火墙接入网络实例个数
        :rtype: int
        """
        return self._JoinInsNum

    @JoinInsNum.setter
    def JoinInsNum(self, JoinInsNum):
        self._JoinInsNum = JoinInsNum

    @property
    def FwSwitchNum(self):
        """VPC防火墙开关个数
        :rtype: int
        """
        return self._FwSwitchNum

    @FwSwitchNum.setter
    def FwSwitchNum(self, FwSwitchNum):
        self._FwSwitchNum = FwSwitchNum

    @property
    def Status(self):
        """VPC防火墙状态 0:正常 ， 1：创建中 2: 变更中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Time(self):
        """VPC防火墙创建时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def CcnId(self):
        """VPC 相关云联网ID列表
        :rtype: list of str
        """
        return self._CcnId

    @CcnId.setter
    def CcnId(self, CcnId):
        self._CcnId = CcnId

    @property
    def CcnName(self):
        """VPC 相关云联网名称列表
        :rtype: list of str
        """
        return self._CcnName

    @CcnName.setter
    def CcnName(self, CcnName):
        self._CcnName = CcnName

    @property
    def PeerConnectionId(self):
        """VPC 相关对等连接ID列表
        :rtype: list of str
        """
        return self._PeerConnectionId

    @PeerConnectionId.setter
    def PeerConnectionId(self, PeerConnectionId):
        self._PeerConnectionId = PeerConnectionId

    @property
    def PeerConnectionName(self):
        """VPC 相关对等连接名称列表
        :rtype: list of str
        """
        return self._PeerConnectionName

    @PeerConnectionName.setter
    def PeerConnectionName(self, PeerConnectionName):
        self._PeerConnectionName = PeerConnectionName

    @property
    def FwCvmLst(self):
        """VPC防火墙CVM的列表
        :rtype: list of VpcFwCvmInsInfo
        """
        return self._FwCvmLst

    @FwCvmLst.setter
    def FwCvmLst(self, FwCvmLst):
        self._FwCvmLst = FwCvmLst

    @property
    def JoinInsLst(self):
        """VPC防火墙接入网络实例类型列表
        :rtype: list of VpcFwJoinInstanceType
        """
        return self._JoinInsLst

    @JoinInsLst.setter
    def JoinInsLst(self, JoinInsLst):
        self._JoinInsLst = JoinInsLst

    @property
    def FwGateway(self):
        """防火墙网关信息
        :rtype: list of FwGateway
        """
        return self._FwGateway

    @FwGateway.setter
    def FwGateway(self, FwGateway):
        self._FwGateway = FwGateway

    @property
    def FwGroupId(self):
        """防火墙(组)ID
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def RuleUsed(self):
        """已使用规则数
        :rtype: int
        """
        return self._RuleUsed

    @RuleUsed.setter
    def RuleUsed(self, RuleUsed):
        self._RuleUsed = RuleUsed

    @property
    def RuleMax(self):
        """最大规则数
        :rtype: int
        """
        return self._RuleMax

    @RuleMax.setter
    def RuleMax(self, RuleMax):
        self._RuleMax = RuleMax

    @property
    def Width(self):
        """防火墙实例带宽
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def UserVpcWidth(self):
        """用户VPC墙总带宽
        :rtype: int
        """
        return self._UserVpcWidth

    @UserVpcWidth.setter
    def UserVpcWidth(self, UserVpcWidth):
        self._UserVpcWidth = UserVpcWidth

    @property
    def JoinInsIdLst(self):
        """接入的vpc列表
        :rtype: list of str
        """
        return self._JoinInsIdLst

    @JoinInsIdLst.setter
    def JoinInsIdLst(self, JoinInsIdLst):
        self._JoinInsIdLst = JoinInsIdLst

    @property
    def FlowMax(self):
        """内网间峰值带宽 (单位 bps )
        :rtype: int
        """
        return self._FlowMax

    @FlowMax.setter
    def FlowMax(self, FlowMax):
        self._FlowMax = FlowMax

    @property
    def EngineVersion(self):
        """实例引擎版本
        :rtype: str
        """
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def UpdateEnable(self):
        """引擎是否可升级：0，不可升级；1，可升级
        :rtype: int
        """
        return self._UpdateEnable

    @UpdateEnable.setter
    def UpdateEnable(self, UpdateEnable):
        self._UpdateEnable = UpdateEnable

    @property
    def TrafficMode(self):
        """引擎运行模式，Normal:正常, OnlyRoute:透明模式
        :rtype: str
        """
        return self._TrafficMode

    @TrafficMode.setter
    def TrafficMode(self, TrafficMode):
        self._TrafficMode = TrafficMode

    @property
    def ReserveTime(self):
        """引擎预约升级时间
        :rtype: str
        """
        return self._ReserveTime

    @ReserveTime.setter
    def ReserveTime(self, ReserveTime):
        self._ReserveTime = ReserveTime

    @property
    def ReserveVersion(self):
        """预约引擎升级版本
        :rtype: str
        """
        return self._ReserveVersion

    @ReserveVersion.setter
    def ReserveVersion(self, ReserveVersion):
        self._ReserveVersion = ReserveVersion

    @property
    def ReserveVersionState(self):
        """引擎预约升级版本状态
        :rtype: str
        """
        return self._ReserveVersionState

    @ReserveVersionState.setter
    def ReserveVersionState(self, ReserveVersionState):
        self._ReserveVersionState = ReserveVersionState

    @property
    def ElasticSwitch(self):
        """弹性开关 1打开 0关闭
        :rtype: int
        """
        return self._ElasticSwitch

    @ElasticSwitch.setter
    def ElasticSwitch(self, ElasticSwitch):
        self._ElasticSwitch = ElasticSwitch

    @property
    def ElasticBandwidth(self):
        """弹性带宽，单位Mbps
        :rtype: int
        """
        return self._ElasticBandwidth

    @ElasticBandwidth.setter
    def ElasticBandwidth(self, ElasticBandwidth):
        self._ElasticBandwidth = ElasticBandwidth

    @property
    def IsFirstAfterPay(self):
        """是否首次开通按量付费
1 是
0 不是
        :rtype: int
        """
        return self._IsFirstAfterPay

    @IsFirstAfterPay.setter
    def IsFirstAfterPay(self, IsFirstAfterPay):
        self._IsFirstAfterPay = IsFirstAfterPay


    def _deserialize(self, params):
        self._FwInsName = params.get("FwInsName")
        self._FwInsId = params.get("FwInsId")
        self._FwMode = params.get("FwMode")
        self._JoinInsNum = params.get("JoinInsNum")
        self._FwSwitchNum = params.get("FwSwitchNum")
        self._Status = params.get("Status")
        self._Time = params.get("Time")
        self._CcnId = params.get("CcnId")
        self._CcnName = params.get("CcnName")
        self._PeerConnectionId = params.get("PeerConnectionId")
        self._PeerConnectionName = params.get("PeerConnectionName")
        if params.get("FwCvmLst") is not None:
            self._FwCvmLst = []
            for item in params.get("FwCvmLst"):
                obj = VpcFwCvmInsInfo()
                obj._deserialize(item)
                self._FwCvmLst.append(obj)
        if params.get("JoinInsLst") is not None:
            self._JoinInsLst = []
            for item in params.get("JoinInsLst"):
                obj = VpcFwJoinInstanceType()
                obj._deserialize(item)
                self._JoinInsLst.append(obj)
        if params.get("FwGateway") is not None:
            self._FwGateway = []
            for item in params.get("FwGateway"):
                obj = FwGateway()
                obj._deserialize(item)
                self._FwGateway.append(obj)
        self._FwGroupId = params.get("FwGroupId")
        self._RuleUsed = params.get("RuleUsed")
        self._RuleMax = params.get("RuleMax")
        self._Width = params.get("Width")
        self._UserVpcWidth = params.get("UserVpcWidth")
        self._JoinInsIdLst = params.get("JoinInsIdLst")
        self._FlowMax = params.get("FlowMax")
        self._EngineVersion = params.get("EngineVersion")
        self._UpdateEnable = params.get("UpdateEnable")
        self._TrafficMode = params.get("TrafficMode")
        self._ReserveTime = params.get("ReserveTime")
        self._ReserveVersion = params.get("ReserveVersion")
        self._ReserveVersionState = params.get("ReserveVersionState")
        self._ElasticSwitch = params.get("ElasticSwitch")
        self._ElasticBandwidth = params.get("ElasticBandwidth")
        self._IsFirstAfterPay = params.get("IsFirstAfterPay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcFwInstanceShow(AbstractModel):
    """VPC防火墙实例信息

    """

    def __init__(self):
        r"""
        :param _FwInsId: VPC防火墙实例ID
        :type FwInsId: str
        :param _FwInsName: VPC防火墙实例名称
        :type FwInsName: str
        :param _FwInsRegion: 网络经过VPC防火墙CVM所在地域
        :type FwInsRegion: str
        """
        self._FwInsId = None
        self._FwInsName = None
        self._FwInsRegion = None

    @property
    def FwInsId(self):
        """VPC防火墙实例ID
        :rtype: str
        """
        return self._FwInsId

    @FwInsId.setter
    def FwInsId(self, FwInsId):
        self._FwInsId = FwInsId

    @property
    def FwInsName(self):
        """VPC防火墙实例名称
        :rtype: str
        """
        return self._FwInsName

    @FwInsName.setter
    def FwInsName(self, FwInsName):
        self._FwInsName = FwInsName

    @property
    def FwInsRegion(self):
        """网络经过VPC防火墙CVM所在地域
        :rtype: str
        """
        return self._FwInsRegion

    @FwInsRegion.setter
    def FwInsRegion(self, FwInsRegion):
        self._FwInsRegion = FwInsRegion


    def _deserialize(self, params):
        self._FwInsId = params.get("FwInsId")
        self._FwInsName = params.get("FwInsName")
        self._FwInsRegion = params.get("FwInsRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcFwJoinInstanceType(AbstractModel):
    """VPC防火墙接入的网络实例类型及数量

    """

    def __init__(self):
        r"""
        :param _JoinType: 接入实例类型，VPC、DIRECTCONNECT、 VPNGW 等
        :type JoinType: str
        :param _Num: 接入的对应网络实例类型的数量
        :type Num: int
        """
        self._JoinType = None
        self._Num = None

    @property
    def JoinType(self):
        """接入实例类型，VPC、DIRECTCONNECT、 VPNGW 等
        :rtype: str
        """
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType

    @property
    def Num(self):
        """接入的对应网络实例类型的数量
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._JoinType = params.get("JoinType")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcRuleItem(AbstractModel):
    """VPC内网间规则

    """

    def __init__(self):
        r"""
        :param _SourceContent: 访问源示例：
net：IP/CIDR(192.168.0.2)
        :type SourceContent: str
        :param _SourceType: 访问源类型，类型可以为：net
        :type SourceType: str
        :param _DestContent: 访问目的示例：
net：IP/CIDR(192.168.0.2)
domain：域名规则，例如*.qq.com
        :type DestContent: str
        :param _DestType: 访问目的类型，类型可以为：net，domain，dnsparse
        :type DestType: str
        :param _Protocol: 协议，可选的值：
TCP
UDP
ICMP
ANY
HTTP
HTTPS
HTTP/HTTPS
SMTP
SMTPS
SMTP/SMTPS
FTP
DNS
TLS/SSL
        :type Protocol: str
        :param _RuleAction: 访问控制策略中设置的流量通过云防火墙的方式。取值：
accept：放行
drop：拒绝
log：观察
        :type RuleAction: str
        :param _Port: 访问控制策略的端口。取值：
-1/-1：全部端口
80：80端口
        :type Port: str
        :param _Description: 描述
        :type Description: str
        :param _OrderIndex: 规则顺序，-1表示最低，1表示最高
        :type OrderIndex: int
        :param _Enable: 规则状态，true表示启用，false表示禁用
        :type Enable: str
        :param _EdgeId: 规则生效的范围，是在哪对vpc之间还是针对所有vpc间生效
        :type EdgeId: str
        :param _Uuid: 规则对应的唯一id，添加规则时忽略该字段，修改该规则时需要填写Uuid;查询返回时会返回该参数
        :type Uuid: int
        :param _DetectedTimes: 规则的命中次数，增删改查规则时无需传入此参数，主要用于返回查询结果数据
        :type DetectedTimes: int
        :param _EdgeName: EdgeId对应的这对VPC间防火墙的描述
        :type EdgeName: str
        :param _InternalUuid: 内部使用的uuid，一般情况下不会使用到该字段
        :type InternalUuid: int
        :param _Deleted: 规则被删除：1，已删除；0，未删除
        :type Deleted: int
        :param _FwGroupId: 规则生效的防火墙实例ID
        :type FwGroupId: str
        :param _FwGroupName: 防火墙名称
        :type FwGroupName: str
        :param _BetaList: beta任务详情
        :type BetaList: list of BetaInfoByACL
        :param _ParamTemplateId: 端口协议组ID
        :type ParamTemplateId: str
        :param _ParamTemplateName: 端口协议组名称
        :type ParamTemplateName: str
        :param _TargetName: 访问目的名称
        :type TargetName: str
        :param _SourceName: 访问源名称
        :type SourceName: str
        :param _IpVersion: Ip版本，0：IPv4，1：IPv6，默认为IPv4
        :type IpVersion: int
        :param _Invalid: 是否是无效规则，0 表示有效规则，1 表示无效规则，出参场景返回使用
        :type Invalid: int
        """
        self._SourceContent = None
        self._SourceType = None
        self._DestContent = None
        self._DestType = None
        self._Protocol = None
        self._RuleAction = None
        self._Port = None
        self._Description = None
        self._OrderIndex = None
        self._Enable = None
        self._EdgeId = None
        self._Uuid = None
        self._DetectedTimes = None
        self._EdgeName = None
        self._InternalUuid = None
        self._Deleted = None
        self._FwGroupId = None
        self._FwGroupName = None
        self._BetaList = None
        self._ParamTemplateId = None
        self._ParamTemplateName = None
        self._TargetName = None
        self._SourceName = None
        self._IpVersion = None
        self._Invalid = None

    @property
    def SourceContent(self):
        """访问源示例：
net：IP/CIDR(192.168.0.2)
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        """访问源类型，类型可以为：net
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DestContent(self):
        """访问目的示例：
net：IP/CIDR(192.168.0.2)
domain：域名规则，例如*.qq.com
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def DestType(self):
        """访问目的类型，类型可以为：net，domain，dnsparse
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def Protocol(self):
        """协议，可选的值：
TCP
UDP
ICMP
ANY
HTTP
HTTPS
HTTP/HTTPS
SMTP
SMTPS
SMTP/SMTPS
FTP
DNS
TLS/SSL
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        """访问控制策略中设置的流量通过云防火墙的方式。取值：
accept：放行
drop：拒绝
log：观察
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Port(self):
        """访问控制策略的端口。取值：
-1/-1：全部端口
80：80端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

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
    def OrderIndex(self):
        """规则顺序，-1表示最低，1表示最高
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Enable(self):
        """规则状态，true表示启用，false表示禁用
        :rtype: str
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def EdgeId(self):
        """规则生效的范围，是在哪对vpc之间还是针对所有vpc间生效
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def Uuid(self):
        """规则对应的唯一id，添加规则时忽略该字段，修改该规则时需要填写Uuid;查询返回时会返回该参数
        :rtype: int
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def DetectedTimes(self):
        """规则的命中次数，增删改查规则时无需传入此参数，主要用于返回查询结果数据
        :rtype: int
        """
        return self._DetectedTimes

    @DetectedTimes.setter
    def DetectedTimes(self, DetectedTimes):
        self._DetectedTimes = DetectedTimes

    @property
    def EdgeName(self):
        """EdgeId对应的这对VPC间防火墙的描述
        :rtype: str
        """
        return self._EdgeName

    @EdgeName.setter
    def EdgeName(self, EdgeName):
        self._EdgeName = EdgeName

    @property
    def InternalUuid(self):
        """内部使用的uuid，一般情况下不会使用到该字段
        :rtype: int
        """
        return self._InternalUuid

    @InternalUuid.setter
    def InternalUuid(self, InternalUuid):
        self._InternalUuid = InternalUuid

    @property
    def Deleted(self):
        """规则被删除：1，已删除；0，未删除
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def FwGroupId(self):
        """规则生效的防火墙实例ID
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def FwGroupName(self):
        """防火墙名称
        :rtype: str
        """
        return self._FwGroupName

    @FwGroupName.setter
    def FwGroupName(self, FwGroupName):
        self._FwGroupName = FwGroupName

    @property
    def BetaList(self):
        """beta任务详情
        :rtype: list of BetaInfoByACL
        """
        return self._BetaList

    @BetaList.setter
    def BetaList(self, BetaList):
        self._BetaList = BetaList

    @property
    def ParamTemplateId(self):
        """端口协议组ID
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def ParamTemplateName(self):
        """端口协议组名称
        :rtype: str
        """
        return self._ParamTemplateName

    @ParamTemplateName.setter
    def ParamTemplateName(self, ParamTemplateName):
        self._ParamTemplateName = ParamTemplateName

    @property
    def TargetName(self):
        """访问目的名称
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def SourceName(self):
        """访问源名称
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def IpVersion(self):
        """Ip版本，0：IPv4，1：IPv6，默认为IPv4
        :rtype: int
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def Invalid(self):
        """是否是无效规则，0 表示有效规则，1 表示无效规则，出参场景返回使用
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._DestContent = params.get("DestContent")
        self._DestType = params.get("DestType")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Port = params.get("Port")
        self._Description = params.get("Description")
        self._OrderIndex = params.get("OrderIndex")
        self._Enable = params.get("Enable")
        self._EdgeId = params.get("EdgeId")
        self._Uuid = params.get("Uuid")
        self._DetectedTimes = params.get("DetectedTimes")
        self._EdgeName = params.get("EdgeName")
        self._InternalUuid = params.get("InternalUuid")
        self._Deleted = params.get("Deleted")
        self._FwGroupId = params.get("FwGroupId")
        self._FwGroupName = params.get("FwGroupName")
        if params.get("BetaList") is not None:
            self._BetaList = []
            for item in params.get("BetaList"):
                obj = BetaInfoByACL()
                obj._deserialize(item)
                self._BetaList.append(obj)
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._ParamTemplateName = params.get("ParamTemplateName")
        self._TargetName = params.get("TargetName")
        self._SourceName = params.get("SourceName")
        self._IpVersion = params.get("IpVersion")
        self._Invalid = params.get("Invalid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcZoneData(AbstractModel):
    """vpc区域数据详情

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _Region: vpc节点地域
        :type Region: str
        """
        self._Zone = None
        self._Region = None

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
    def Region(self):
        """vpc节点地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        