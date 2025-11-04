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


class AccountVpcInfo(AbstractModel):
    r"""私有域解析账号Vpc信息

    """

    def __init__(self):
        r"""
        :param _UniqVpcId: VpcId
        :type UniqVpcId: str
        :param _Region: Vpc所属地区
        :type Region: str
        :param _Uin: Vpc所属账号
        :type Uin: str
        :param _VpcName: vpc资源名称
        :type VpcName: str
        """
        self._UniqVpcId = None
        self._Region = None
        self._Uin = None
        self._VpcName = None

    @property
    def UniqVpcId(self):
        r"""VpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        r"""Vpc所属地区
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        r"""Vpc所属账号
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        r"""vpc资源名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        self._Uin = params.get("Uin")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOut(AbstractModel):
    r"""查询关联账号VPC列表出参

    """

    def __init__(self):
        r"""
        :param _VpcId: VpcId
        :type VpcId: str
        :param _Region: Vpc所属地区: ap-guangzhou, ap-shanghai
        :type Region: str
        :param _Uin: Vpc所属账号: 123456789
        :type Uin: str
        :param _VpcName: vpc资源名称：testname
        :type VpcName: str
        """
        self._VpcId = None
        self._Region = None
        self._Uin = None
        self._VpcName = None

    @property
    def VpcId(self):
        r"""VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Region(self):
        r"""Vpc所属地区: ap-guangzhou, ap-shanghai
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        r"""Vpc所属账号: 123456789
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        r"""vpc资源名称：testname
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Region = params.get("Region")
        self._Uin = params.get("Uin")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOutput(AbstractModel):
    r"""关联的VPC出参

    """

    def __init__(self):
        r"""
        :param _Uin: 关联账户的uin
        :type Uin: str
        :param _UniqVpcId: vpcid
        :type UniqVpcId: str
        :param _Region: 地域
        :type Region: str
        """
        self._Uin = None
        self._UniqVpcId = None
        self._Region = None

    @property
    def Uin(self):
        r"""关联账户的uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def UniqVpcId(self):
        r"""vpcid
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSpecifyPrivateZoneVpcRequest(AbstractModel):
    r"""AddSpecifyPrivateZoneVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域id
        :type ZoneId: str
        :param _VpcSet: 本次新增的vpc信息
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 本次新增关联账户vpc信息
        :type AccountVpcSet: list of AccountVpcInfo
        :param _Sync: 是否为同步操作
        :type Sync: bool
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._Sync = None

    @property
    def ZoneId(self):
        r"""私有域id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""本次新增的vpc信息
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""本次新增关联账户vpc信息
        :rtype: list of AccountVpcInfo
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def Sync(self):
        r"""是否为同步操作
        :rtype: bool
        """
        return self._Sync

    @Sync.setter
    def Sync(self, Sync):
        self._Sync = Sync


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._Sync = params.get("Sync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSpecifyPrivateZoneVpcResponse(AbstractModel):
    r"""AddSpecifyPrivateZoneVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: zone id
        :type ZoneId: str
        :param _VpcSet: 本次新增的vpc
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 本次新增的关联账号vpc
        :type AccountVpcSet: list of AccountVpcInfo
        :param _UniqId: 唯一id
        :type UniqId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._UniqId = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""zone id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""本次新增的vpc
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""本次新增的关联账号vpc
        :rtype: list of AccountVpcInfo
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def UniqId(self):
        r"""唯一id
        :rtype: str
        """
        return self._UniqId

    @UniqId.setter
    def UniqId(self, UniqId):
        self._UniqId = UniqId

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
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._UniqId = params.get("UniqId")
        self._RequestId = params.get("RequestId")


class AuditLog(AbstractModel):
    r"""操作日志

    """

    def __init__(self):
        r"""
        :param _Resource: 日志类型
        :type Resource: str
        :param _Metric: 日志表名
        :type Metric: str
        :param _TotalCount: 日志总数
        :type TotalCount: int
        :param _DataSet: 日志列表
        :type DataSet: list of AuditLogInfo
        """
        self._Resource = None
        self._Metric = None
        self._TotalCount = None
        self._DataSet = None

    @property
    def Resource(self):
        r"""日志类型
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        r"""日志表名
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def TotalCount(self):
        r"""日志总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataSet(self):
        r"""日志列表
        :rtype: list of AuditLogInfo
        """
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Metric = params.get("Metric")
        self._TotalCount = params.get("TotalCount")
        if params.get("DataSet") is not None:
            self._DataSet = []
            for item in params.get("DataSet"):
                obj = AuditLogInfo()
                obj._deserialize(item)
                self._DataSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogInfo(AbstractModel):
    r"""日志详情

    """

    def __init__(self):
        r"""
        :param _Date: 时间
        :type Date: str
        :param _OperatorUin: 操作人uin
        :type OperatorUin: str
        :param _Content: 日志内容
        :type Content: str
        """
        self._Date = None
        self._OperatorUin = None
        self._Content = None

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
    def OperatorUin(self):
        r"""操作人uin
        :rtype: str
        """
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def Content(self):
        r"""日志内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._OperatorUin = params.get("OperatorUin")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExtendEndpointRequest(AbstractModel):
    r"""CreateExtendEndpoint请求参数结构体

    """


class CreateExtendEndpointResponse(AbstractModel):
    r"""CreateExtendEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EndpointId: 终端节点id
        :type EndpointId: str
        :param _EndpointName: 终端节点名称
        :type EndpointName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EndpointId = None
        self._EndpointName = None
        self._RequestId = None

    @property
    def EndpointId(self):
        r"""终端节点id
        :rtype: str
        """
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def EndpointName(self):
        r"""终端节点名称
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

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
        self._EndpointId = params.get("EndpointId")
        self._EndpointName = params.get("EndpointName")
        self._RequestId = params.get("RequestId")


class CreateForwardRuleRequest(AbstractModel):
    r"""CreateForwardRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleName: 转发规则名称
        :type RuleName: str
        :param _RuleType: 转发规则类型：云上到云下DOWN，云下到云上UP
        :type RuleType: str
        :param _ZoneId: 私有域ID，可在私有域列表页面查看
        :type ZoneId: str
        :param _EndPointId: 终端节点ID
        :type EndPointId: str
        """
        self._RuleName = None
        self._RuleType = None
        self._ZoneId = None
        self._EndPointId = None

    @property
    def RuleName(self):
        r"""转发规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleType(self):
        r"""转发规则类型：云上到云下DOWN，云下到云上UP
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def ZoneId(self):
        r"""私有域ID，可在私有域列表页面查看
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EndPointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._RuleType = params.get("RuleType")
        self._ZoneId = params.get("ZoneId")
        self._EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardRuleResponse(AbstractModel):
    r"""CreateForwardRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 转发规则ID
        :type RuleId: str
        :param _RuleName: 转发规则名称
        :type RuleName: str
        :param _RuleType: 转发规则类型
        :type RuleType: str
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _EndPointId: 终端节点ID
        :type EndPointId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RuleName = None
        self._RuleType = None
        self._ZoneId = None
        self._EndPointId = None
        self._RequestId = None

    @property
    def RuleId(self):
        r"""转发规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""转发规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleType(self):
        r"""转发规则类型
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EndPointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

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
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._RuleType = params.get("RuleType")
        self._ZoneId = params.get("ZoneId")
        self._EndPointId = params.get("EndPointId")
        self._RequestId = params.get("RequestId")


class CreateInboundEndpointRequest(AbstractModel):
    r"""CreateInboundEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndpointName: 名称
        :type EndpointName: str
        :param _EndpointRegion: 地域
        :type EndpointRegion: str
        :param _EndpointVpc: vpcid
        :type EndpointVpc: str
        :param _SubnetIp: 子网信息
        :type SubnetIp: list of SubnetIpInfo
        """
        self._EndpointName = None
        self._EndpointRegion = None
        self._EndpointVpc = None
        self._SubnetIp = None

    @property
    def EndpointName(self):
        r"""名称
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def EndpointRegion(self):
        r"""地域
        :rtype: str
        """
        return self._EndpointRegion

    @EndpointRegion.setter
    def EndpointRegion(self, EndpointRegion):
        self._EndpointRegion = EndpointRegion

    @property
    def EndpointVpc(self):
        r"""vpcid
        :rtype: str
        """
        return self._EndpointVpc

    @EndpointVpc.setter
    def EndpointVpc(self, EndpointVpc):
        self._EndpointVpc = EndpointVpc

    @property
    def SubnetIp(self):
        r"""子网信息
        :rtype: list of SubnetIpInfo
        """
        return self._SubnetIp

    @SubnetIp.setter
    def SubnetIp(self, SubnetIp):
        self._SubnetIp = SubnetIp


    def _deserialize(self, params):
        self._EndpointName = params.get("EndpointName")
        self._EndpointRegion = params.get("EndpointRegion")
        self._EndpointVpc = params.get("EndpointVpc")
        if params.get("SubnetIp") is not None:
            self._SubnetIp = []
            for item in params.get("SubnetIp"):
                obj = SubnetIpInfo()
                obj._deserialize(item)
                self._SubnetIp.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInboundEndpointResponse(AbstractModel):
    r"""CreateInboundEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EndpointId: 终端节点ID
        :type EndpointId: str
        :param _EndpointName: 名称
        :type EndpointName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EndpointId = None
        self._EndpointName = None
        self._RequestId = None

    @property
    def EndpointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def EndpointName(self):
        r"""名称
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

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
        self._EndpointId = params.get("EndpointId")
        self._EndpointName = params.get("EndpointName")
        self._RequestId = params.get("RequestId")


class CreatePrivateDNSAccountRequest(AbstractModel):
    r"""CreatePrivateDNSAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Account: 私有域解析账号，该账号不能与主账号一致且需要子账号授权
        :type Account: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        self._Account = None

    @property
    def Account(self):
        r"""私有域解析账号，该账号不能与主账号一致且需要子账号授权
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self._Account = PrivateDNSAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateDNSAccountResponse(AbstractModel):
    r"""CreatePrivateDNSAccount返回参数结构体

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


class CreatePrivateZoneRecordRequest(AbstractModel):
    r"""CreatePrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _SubDomain: 子域名，例如 "www", "m", "@"
        :type SubDomain: str
        :param _RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :type RecordValue: str
        :param _Weight: 记录权重，值为1-100
        :type Weight: int
        :param _MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param _TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        :param _Remark: 备注
        :type Remark: str
        """
        self._ZoneId = None
        self._RecordType = None
        self._SubDomain = None
        self._RecordValue = None
        self._Weight = None
        self._MX = None
        self._TTL = None
        self._Remark = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordType(self):
        r"""记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        r"""子域名，例如 "www", "m", "@"
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        r"""记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def Weight(self):
        r"""记录权重，值为1-100
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        r"""MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        r"""记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

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
        self._ZoneId = params.get("ZoneId")
        self._RecordType = params.get("RecordType")
        self._SubDomain = params.get("SubDomain")
        self._RecordValue = params.get("RecordValue")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneRecordResponse(AbstractModel):
    r"""CreatePrivateZoneRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录Id
        :type RecordId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        r"""记录Id
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

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
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class CreatePrivateZoneRequest(AbstractModel):
    r"""CreatePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名，格式必须是标准的TLD
        :type Domain: str
        :param _TagSet: 创建私有域的同时，为其打上标签
        :type TagSet: list of TagInfo
        :param _VpcSet: 创建私有域的同时，将其关联至VPC
        :type VpcSet: list of VpcInfo
        :param _Remark: 备注
        :type Remark: str
        :param _DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED。默认值为ENABLED
        :type DnsForwardStatus: str
        :param _Vpcs: 创建私有域的同时，将其关联至VPC
        :type Vpcs: list of VpcInfo
        :param _AccountVpcSet: 创建私有域同时绑定关联账号的VPC
        :type AccountVpcSet: list of AccountVpcInfo
        :param _CnameSpeedupStatus: 是否CNAME加速：ENABLED，DISABLED，默认值为ENABLED
        :type CnameSpeedupStatus: str
        """
        self._Domain = None
        self._TagSet = None
        self._VpcSet = None
        self._Remark = None
        self._DnsForwardStatus = None
        self._Vpcs = None
        self._AccountVpcSet = None
        self._CnameSpeedupStatus = None

    @property
    def Domain(self):
        r"""域名，格式必须是标准的TLD
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def TagSet(self):
        r"""创建私有域的同时，为其打上标签
        :rtype: list of TagInfo
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def VpcSet(self):
        r"""创建私有域的同时，将其关联至VPC
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

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
    def DnsForwardStatus(self):
        r"""是否开启子域名递归, ENABLED， DISABLED。默认值为ENABLED
        :rtype: str
        """
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def Vpcs(self):
        warnings.warn("parameter `Vpcs` is deprecated", DeprecationWarning) 

        r"""创建私有域的同时，将其关联至VPC
        :rtype: list of VpcInfo
        """
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        warnings.warn("parameter `Vpcs` is deprecated", DeprecationWarning) 

        self._Vpcs = Vpcs

    @property
    def AccountVpcSet(self):
        r"""创建私有域同时绑定关联账号的VPC
        :rtype: list of AccountVpcInfo
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def CnameSpeedupStatus(self):
        r"""是否CNAME加速：ENABLED，DISABLED，默认值为ENABLED
        :rtype: str
        """
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._Remark = params.get("Remark")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneResponse(AbstractModel):
    r"""CreatePrivateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID, zone-12sa5ce78
        :type ZoneId: str
        :param _Domain: 私有域名
        :type Domain: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._Domain = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""私有域ID, zone-12sa5ce78
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Domain(self):
        r"""私有域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
        self._ZoneId = params.get("ZoneId")
        self._Domain = params.get("Domain")
        self._RequestId = params.get("RequestId")


class DatePoint(AbstractModel):
    r"""时间统计值

    """

    def __init__(self):
        r"""
        :param _Date: 时间
        :type Date: str
        :param _Value: 值
        :type Value: int
        """
        self._Date = None
        self._Value = None

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
    def Value(self):
        r"""值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndPointRequest(AbstractModel):
    r"""DeleteEndPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndPointId: 终端节点ID
        :type EndPointId: str
        """
        self._EndPointId = None

    @property
    def EndPointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId


    def _deserialize(self, params):
        self._EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndPointResponse(AbstractModel):
    r"""DeleteEndPoint返回参数结构体

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


class DeleteForwardRuleRequest(AbstractModel):
    r"""DeleteForwardRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIdSet: 转发规则ID数组
        :type RuleIdSet: list of str
        """
        self._RuleIdSet = None

    @property
    def RuleIdSet(self):
        r"""转发规则ID数组
        :rtype: list of str
        """
        return self._RuleIdSet

    @RuleIdSet.setter
    def RuleIdSet(self, RuleIdSet):
        self._RuleIdSet = RuleIdSet


    def _deserialize(self, params):
        self._RuleIdSet = params.get("RuleIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardRuleResponse(AbstractModel):
    r"""DeleteForwardRule返回参数结构体

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


class DeleteInboundEndpointRequest(AbstractModel):
    r"""DeleteInboundEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndpointId: 终端节点ID
        :type EndpointId: str
        """
        self._EndpointId = None

    @property
    def EndpointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId


    def _deserialize(self, params):
        self._EndpointId = params.get("EndpointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInboundEndpointResponse(AbstractModel):
    r"""DeleteInboundEndpoint返回参数结构体

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


class DeletePrivateDNSAccountRequest(AbstractModel):
    r"""DeletePrivateDNSAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Account: 私有域解析账号
        :type Account: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        self._Account = None

    @property
    def Account(self):
        r"""私有域解析账号
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self._Account = PrivateDNSAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateDNSAccountResponse(AbstractModel):
    r"""DeletePrivateDNSAccount返回参数结构体

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


class DeletePrivateZoneRecordRequest(AbstractModel):
    r"""DeletePrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordId: 记录ID（调用DescribePrivateZoneRecordList可获取到RecordId）
        :type RecordId: str
        :param _RecordIdSet: 记录ID数组，RecordId 优先
        :type RecordIdSet: list of str
        """
        self._ZoneId = None
        self._RecordId = None
        self._RecordIdSet = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        r"""记录ID（调用DescribePrivateZoneRecordList可获取到RecordId）
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordIdSet(self):
        r"""记录ID数组，RecordId 优先
        :rtype: list of str
        """
        return self._RecordIdSet

    @RecordIdSet.setter
    def RecordIdSet(self, RecordIdSet):
        self._RecordIdSet = RecordIdSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        self._RecordIdSet = params.get("RecordIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneRecordResponse(AbstractModel):
    r"""DeletePrivateZoneRecord返回参数结构体

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


class DeletePrivateZoneRequest(AbstractModel):
    r"""DeletePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _ZoneIdSet: 私有域ID数组，ZoneId 优先
        :type ZoneIdSet: list of str
        """
        self._ZoneId = None
        self._ZoneIdSet = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneIdSet(self):
        r"""私有域ID数组，ZoneId 优先
        :rtype: list of str
        """
        return self._ZoneIdSet

    @ZoneIdSet.setter
    def ZoneIdSet(self, ZoneIdSet):
        self._ZoneIdSet = ZoneIdSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneIdSet = params.get("ZoneIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneResponse(AbstractModel):
    r"""DeletePrivateZone返回参数结构体

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


class DeleteSpecifyPrivateZoneVpcRequest(AbstractModel):
    r"""DeleteSpecifyPrivateZoneVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域id
        :type ZoneId: str
        :param _VpcSet: 本次删除的VPC
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 本次删除的关联账户VPC
        :type AccountVpcSet: list of AccountVpcInfo
        :param _Sync: 是否为同步操作
        :type Sync: bool
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._Sync = None

    @property
    def ZoneId(self):
        r"""私有域id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""本次删除的VPC
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""本次删除的关联账户VPC
        :rtype: list of AccountVpcInfo
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def Sync(self):
        r"""是否为同步操作
        :rtype: bool
        """
        return self._Sync

    @Sync.setter
    def Sync(self, Sync):
        self._Sync = Sync


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._Sync = params.get("Sync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSpecifyPrivateZoneVpcResponse(AbstractModel):
    r"""DeleteSpecifyPrivateZoneVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域id
        :type ZoneId: str
        :param _VpcSet: 本次删除的VPC
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 本次删除的关联账户的VPC
        :type AccountVpcSet: list of AccountVpcInfo
        :param _UniqId: 唯一id
        :type UniqId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._UniqId = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""私有域id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""本次删除的VPC
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""本次删除的关联账户的VPC
        :rtype: list of AccountVpcInfo
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def UniqId(self):
        r"""唯一id
        :rtype: str
        """
        return self._UniqId

    @UniqId.setter
    def UniqId(self, UniqId):
        self._UniqId = UniqId

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
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._UniqId = params.get("UniqId")
        self._RequestId = params.get("RequestId")


class DescribeAccountVpcListRequest(AbstractModel):
    r"""DescribeAccountVpcList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountUin: 关联账号的uin
        :type AccountUin: str
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._AccountUin = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def AccountUin(self):
        r"""关联账号的uin
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大100，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤参数
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AccountUin = params.get("AccountUin")
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
        


class DescribeAccountVpcListResponse(AbstractModel):
    r"""DescribeAccountVpcList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: VPC数量
        :type TotalCount: int
        :param _VpcSet: VPC 列表
        :type VpcSet: list of AccountVpcInfoOut
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""VPC数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSet(self):
        r"""VPC 列表
        :rtype: list of AccountVpcInfoOut
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

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
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = AccountVpcInfoOut()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogRequest(AbstractModel):
    r"""DescribeAuditLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeRangeBegin: 请求量统计起始时间
        :type TimeRangeBegin: str
        :param _Filters: 筛选参数：ZoneId：私有域ID；Domain：私有域；OperatorUin：操作者账号ID
        :type Filters: list of Filter
        :param _TimeRangeEnd: 请求量统计结束时间
        :type TimeRangeEnd: str
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        """
        self._TimeRangeBegin = None
        self._Filters = None
        self._TimeRangeEnd = None
        self._Offset = None
        self._Limit = None

    @property
    def TimeRangeBegin(self):
        r"""请求量统计起始时间
        :rtype: str
        """
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        r"""筛选参数：ZoneId：私有域ID；Domain：私有域；OperatorUin：操作者账号ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        r"""请求量统计结束时间
        :rtype: str
        """
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大100，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogResponse(AbstractModel):
    r"""DescribeAuditLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 操作日志列表
        :type Data: list of AuditLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""操作日志列表
        :rtype: list of AuditLog
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
                obj = AuditLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDashboardRequest(AbstractModel):
    r"""DescribeDashboard请求参数结构体

    """


class DescribeDashboardResponse(AbstractModel):
    r"""DescribeDashboard返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneTotal: 私有域解析总数
        :type ZoneTotal: int
        :param _ZoneVpcCount: 私有域关联VPC数量
        :type ZoneVpcCount: int
        :param _RequestTotalCount: 历史请求量总数
        :type RequestTotalCount: int
        :param _FlowUsage: 流量包用量
        :type FlowUsage: list of FlowUsage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneTotal = None
        self._ZoneVpcCount = None
        self._RequestTotalCount = None
        self._FlowUsage = None
        self._RequestId = None

    @property
    def ZoneTotal(self):
        r"""私有域解析总数
        :rtype: int
        """
        return self._ZoneTotal

    @ZoneTotal.setter
    def ZoneTotal(self, ZoneTotal):
        self._ZoneTotal = ZoneTotal

    @property
    def ZoneVpcCount(self):
        r"""私有域关联VPC数量
        :rtype: int
        """
        return self._ZoneVpcCount

    @ZoneVpcCount.setter
    def ZoneVpcCount(self, ZoneVpcCount):
        self._ZoneVpcCount = ZoneVpcCount

    @property
    def RequestTotalCount(self):
        r"""历史请求量总数
        :rtype: int
        """
        return self._RequestTotalCount

    @RequestTotalCount.setter
    def RequestTotalCount(self, RequestTotalCount):
        self._RequestTotalCount = RequestTotalCount

    @property
    def FlowUsage(self):
        r"""流量包用量
        :rtype: list of FlowUsage
        """
        return self._FlowUsage

    @FlowUsage.setter
    def FlowUsage(self, FlowUsage):
        self._FlowUsage = FlowUsage

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
        self._ZoneTotal = params.get("ZoneTotal")
        self._ZoneVpcCount = params.get("ZoneVpcCount")
        self._RequestTotalCount = params.get("RequestTotalCount")
        if params.get("FlowUsage") is not None:
            self._FlowUsage = []
            for item in params.get("FlowUsage"):
                obj = FlowUsage()
                obj._deserialize(item)
                self._FlowUsage.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeExtendEndpointListRequest(AbstractModel):
    r"""DescribeExtendEndpointList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数，支持EndpointName,EndpointId
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大100，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤参数，支持EndpointName,EndpointId
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeExtendEndpointListResponse(AbstractModel):
    r"""DescribeExtendEndpointList返回参数结构体

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


class DescribeForwardRuleListRequest(AbstractModel):
    r"""DescribeForwardRuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大100，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤参数
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeForwardRuleListResponse(AbstractModel):
    r"""DescribeForwardRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 私有域数量
        :type TotalCount: int
        :param _ForwardRuleSet: 私有域列表
        :type ForwardRuleSet: list of ForwardRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ForwardRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""私有域数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ForwardRuleSet(self):
        r"""私有域列表
        :rtype: list of ForwardRule
        """
        return self._ForwardRuleSet

    @ForwardRuleSet.setter
    def ForwardRuleSet(self, ForwardRuleSet):
        self._ForwardRuleSet = ForwardRuleSet

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
        if params.get("ForwardRuleSet") is not None:
            self._ForwardRuleSet = []
            for item in params.get("ForwardRuleSet"):
                obj = ForwardRule()
                obj._deserialize(item)
                self._ForwardRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInboundEndpointListRequest(AbstractModel):
    r"""DescribeInboundEndpointList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数，支持EndPointName，EndpointName，EndpointId
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大100，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤参数，支持EndPointName，EndpointName，EndpointId
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeInboundEndpointListResponse(AbstractModel):
    r"""DescribeInboundEndpointList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _InboundEndpointSet: 终端节点信息
        :type InboundEndpointSet: list of InboundEndpointSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InboundEndpointSet = None
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
    def InboundEndpointSet(self):
        r"""终端节点信息
        :rtype: list of InboundEndpointSet
        """
        return self._InboundEndpointSet

    @InboundEndpointSet.setter
    def InboundEndpointSet(self, InboundEndpointSet):
        self._InboundEndpointSet = InboundEndpointSet

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
        if params.get("InboundEndpointSet") is not None:
            self._InboundEndpointSet = []
            for item in params.get("InboundEndpointSet"):
                obj = InboundEndpointSet()
                obj._deserialize(item)
                self._InboundEndpointSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateDNSAccountListRequest(AbstractModel):
    r"""DescribePrivateDNSAccountList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大100，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤参数
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribePrivateDNSAccountListResponse(AbstractModel):
    r"""DescribePrivateDNSAccountList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 私有域解析账号数量
        :type TotalCount: int
        :param _AccountSet: 私有域解析账号列表
        :type AccountSet: list of PrivateDNSAccount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""私有域解析账号数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountSet(self):
        r"""私有域解析账号列表
        :rtype: list of PrivateDNSAccount
        """
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

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
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = PrivateDNSAccount()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneListRequest(AbstractModel):
    r"""DescribePrivateZoneList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大100，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤参数
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribePrivateZoneListResponse(AbstractModel):
    r"""DescribePrivateZoneList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 私有域数量
        :type TotalCount: int
        :param _PrivateZoneSet: 私有域列表
        :type PrivateZoneSet: list of PrivateZone
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PrivateZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""私有域数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PrivateZoneSet(self):
        r"""私有域列表
        :rtype: list of PrivateZone
        """
        return self._PrivateZoneSet

    @PrivateZoneSet.setter
    def PrivateZoneSet(self, PrivateZoneSet):
        self._PrivateZoneSet = PrivateZoneSet

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
        if params.get("PrivateZoneSet") is not None:
            self._PrivateZoneSet = []
            for item in params.get("PrivateZoneSet"):
                obj = PrivateZone()
                obj._deserialize(item)
                self._PrivateZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneRecordListRequest(AbstractModel):
    r"""DescribePrivateZoneRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID: zone-12c5a6e8
        :type ZoneId: str
        :param _Filters: 过滤参数（支持使用Value、RecordType过滤）
        :type Filters: list of Filter
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大200，默认20
        :type Limit: int
        """
        self._ZoneId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        r"""私有域ID: zone-12c5a6e8
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        r"""过滤参数（支持使用Value、RecordType过滤）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""分页偏移量，从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页限制数目， 最大200，默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
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
        


class DescribePrivateZoneRecordListResponse(AbstractModel):
    r"""DescribePrivateZoneRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 解析记录数量
        :type TotalCount: int
        :param _RecordSet: 解析记录列表
        :type RecordSet: list of PrivateZoneRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""解析记录数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordSet(self):
        r"""解析记录列表
        :rtype: list of PrivateZoneRecord
        """
        return self._RecordSet

    @RecordSet.setter
    def RecordSet(self, RecordSet):
        self._RecordSet = RecordSet

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
        if params.get("RecordSet") is not None:
            self._RecordSet = []
            for item in params.get("RecordSet"):
                obj = PrivateZoneRecord()
                obj._deserialize(item)
                self._RecordSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneRequest(AbstractModel):
    r"""DescribePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域id
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        r"""私有域id
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneResponse(AbstractModel):
    r"""DescribePrivateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivateZone: 私有域详情
        :type PrivateZone: :class:`tencentcloud.privatedns.v20201028.models.PrivateZone`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrivateZone = None
        self._RequestId = None

    @property
    def PrivateZone(self):
        r"""私有域详情
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.PrivateZone`
        """
        return self._PrivateZone

    @PrivateZone.setter
    def PrivateZone(self, PrivateZone):
        self._PrivateZone = PrivateZone

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
        if params.get("PrivateZone") is not None:
            self._PrivateZone = PrivateZone()
            self._PrivateZone._deserialize(params.get("PrivateZone"))
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneServiceRequest(AbstractModel):
    r"""DescribePrivateZoneService请求参数结构体

    """


class DescribePrivateZoneServiceResponse(AbstractModel):
    r"""DescribePrivateZoneService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceStatus: 私有域解析服务开通状态。ENABLED已开通，DISABLED未开通
        :type ServiceStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        r"""私有域解析服务开通状态。ENABLED已开通，DISABLED未开通
        :rtype: str
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

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
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class DescribeQuotaUsageRequest(AbstractModel):
    r"""DescribeQuotaUsage请求参数结构体

    """


class DescribeQuotaUsageResponse(AbstractModel):
    r"""DescribeQuotaUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TldQuota: Tld额度使用情况
        :type TldQuota: :class:`tencentcloud.privatedns.v20201028.models.TldQuota`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TldQuota = None
        self._RequestId = None

    @property
    def TldQuota(self):
        r"""Tld额度使用情况
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.TldQuota`
        """
        return self._TldQuota

    @TldQuota.setter
    def TldQuota(self, TldQuota):
        self._TldQuota = TldQuota

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
        if params.get("TldQuota") is not None:
            self._TldQuota = TldQuota()
            self._TldQuota._deserialize(params.get("TldQuota"))
        self._RequestId = params.get("RequestId")


class DescribeRecordRequest(AbstractModel):
    r"""DescribeRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordId: 记录ID
        :type RecordId: str
        """
        self._ZoneId = None
        self._RecordId = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        r"""记录ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordResponse(AbstractModel):
    r"""DescribeRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordInfo: 记录信息
        :type RecordInfo: :class:`tencentcloud.privatedns.v20201028.models.RecordInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordInfo = None
        self._RequestId = None

    @property
    def RecordInfo(self):
        r"""记录信息
        :rtype: :class:`tencentcloud.privatedns.v20201028.models.RecordInfo`
        """
        return self._RecordInfo

    @RecordInfo.setter
    def RecordInfo(self, RecordInfo):
        self._RecordInfo = RecordInfo

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
        if params.get("RecordInfo") is not None:
            self._RecordInfo = RecordInfo()
            self._RecordInfo._deserialize(params.get("RecordInfo"))
        self._RequestId = params.get("RequestId")


class DescribeRequestDataRequest(AbstractModel):
    r"""DescribeRequestData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeRangeBegin: 请求量统计起始时间，格式：2020-11-22 00:00:00
        :type TimeRangeBegin: str
        :param _Filters: 筛选参数：
        :type Filters: list of Filter
        :param _TimeRangeEnd: 请求量统计结束时间，格式：2020-11-22 23:59:59
        :type TimeRangeEnd: str
        :param _Export: 是否导出：true导出，false不导出
        :type Export: bool
        """
        self._TimeRangeBegin = None
        self._Filters = None
        self._TimeRangeEnd = None
        self._Export = None

    @property
    def TimeRangeBegin(self):
        r"""请求量统计起始时间，格式：2020-11-22 00:00:00
        :rtype: str
        """
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        r"""筛选参数：
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        r"""请求量统计结束时间，格式：2020-11-22 23:59:59
        :rtype: str
        """
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def Export(self):
        r"""是否导出：true导出，false不导出
        :rtype: bool
        """
        return self._Export

    @Export.setter
    def Export(self, Export):
        self._Export = Export


    def _deserialize(self, params):
        self._TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        self._Export = params.get("Export")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRequestDataResponse(AbstractModel):
    r"""DescribeRequestData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 请求量统计表
        :type Data: list of MetricData
        :param _Interval: 请求量单位时间: Day：天，Hour：小时
        :type Interval: str
        :param _Url: 导出数据下载地址
        :type Url: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._Url = None
        self._RequestId = None

    @property
    def Data(self):
        r"""请求量统计表
        :rtype: list of MetricData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        r"""请求量单位时间: Day：天，Hour：小时
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Url(self):
        r"""导出数据下载地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

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
                obj = MetricData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class EndPointServiceInfo(AbstractModel):
    r"""终端节点信息

    """

    def __init__(self):
        r"""
        :param _EndPointVip: ip
        :type EndPointVip: str
        :param _UniqSubnetId: 子网id
        :type UniqSubnetId: str
        :param _EndPointState: 网络侧状态，0 可用，1 待接受，3 拒绝
        :type EndPointState: int
        :param _EndPointStatus: 状态，1表示可用，0表示删除
        :type EndPointStatus: int
        :param _EndPointRemark: 备注信息
        :type EndPointRemark: str
        :param _EndPointIsolateFlag: 网络侧隔离状态，1：已隔离，0：未隔离
        :type EndPointIsolateFlag: int
        """
        self._EndPointVip = None
        self._UniqSubnetId = None
        self._EndPointState = None
        self._EndPointStatus = None
        self._EndPointRemark = None
        self._EndPointIsolateFlag = None

    @property
    def EndPointVip(self):
        r"""ip
        :rtype: str
        """
        return self._EndPointVip

    @EndPointVip.setter
    def EndPointVip(self, EndPointVip):
        self._EndPointVip = EndPointVip

    @property
    def UniqSubnetId(self):
        r"""子网id
        :rtype: str
        """
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def EndPointState(self):
        r"""网络侧状态，0 可用，1 待接受，3 拒绝
        :rtype: int
        """
        return self._EndPointState

    @EndPointState.setter
    def EndPointState(self, EndPointState):
        self._EndPointState = EndPointState

    @property
    def EndPointStatus(self):
        r"""状态，1表示可用，0表示删除
        :rtype: int
        """
        return self._EndPointStatus

    @EndPointStatus.setter
    def EndPointStatus(self, EndPointStatus):
        self._EndPointStatus = EndPointStatus

    @property
    def EndPointRemark(self):
        r"""备注信息
        :rtype: str
        """
        return self._EndPointRemark

    @EndPointRemark.setter
    def EndPointRemark(self, EndPointRemark):
        self._EndPointRemark = EndPointRemark

    @property
    def EndPointIsolateFlag(self):
        r"""网络侧隔离状态，1：已隔离，0：未隔离
        :rtype: int
        """
        return self._EndPointIsolateFlag

    @EndPointIsolateFlag.setter
    def EndPointIsolateFlag(self, EndPointIsolateFlag):
        self._EndPointIsolateFlag = EndPointIsolateFlag


    def _deserialize(self, params):
        self._EndPointVip = params.get("EndPointVip")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._EndPointState = params.get("EndPointState")
        self._EndPointStatus = params.get("EndPointStatus")
        self._EndPointRemark = params.get("EndPointRemark")
        self._EndPointIsolateFlag = params.get("EndPointIsolateFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""筛选参数

    """

    def __init__(self):
        r"""
        :param _Name: 参数名
        :type Name: str
        :param _Values: 参数值数组
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""参数名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""参数值数组
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
        


class FlowUsage(AbstractModel):
    r"""流量包用量

    """

    def __init__(self):
        r"""
        :param _FlowType: 流量包类型：ZONE 私有域；TRAFFIC 解析流量包
        :type FlowType: str
        :param _TotalQuantity: 流量包总额度
        :type TotalQuantity: int
        :param _AvailableQuantity: 流量包可用额度
        :type AvailableQuantity: int
        """
        self._FlowType = None
        self._TotalQuantity = None
        self._AvailableQuantity = None

    @property
    def FlowType(self):
        r"""流量包类型：ZONE 私有域；TRAFFIC 解析流量包
        :rtype: str
        """
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def TotalQuantity(self):
        r"""流量包总额度
        :rtype: int
        """
        return self._TotalQuantity

    @TotalQuantity.setter
    def TotalQuantity(self, TotalQuantity):
        self._TotalQuantity = TotalQuantity

    @property
    def AvailableQuantity(self):
        r"""流量包可用额度
        :rtype: int
        """
        return self._AvailableQuantity

    @AvailableQuantity.setter
    def AvailableQuantity(self, AvailableQuantity):
        self._AvailableQuantity = AvailableQuantity


    def _deserialize(self, params):
        self._FlowType = params.get("FlowType")
        self._TotalQuantity = params.get("TotalQuantity")
        self._AvailableQuantity = params.get("AvailableQuantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardRule(AbstractModel):
    r"""转发规则详情

    """

    def __init__(self):
        r"""
        :param _Domain: 私有域名
        :type Domain: str
        :param _RuleName: 转发规则名称
        :type RuleName: str
        :param _RuleId: 规则id
        :type RuleId: str
        :param _RuleType: 转发规则类型：云上到云下DOWN、云下到云上DOWN
        :type RuleType: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _EndPointName: 终端节点名称
        :type EndPointName: str
        :param _EndPointId: 终端节点ID
        :type EndPointId: str
        :param _ForwardAddress: 转发地址
        :type ForwardAddress: list of str
        :param _VpcSet: 私有域绑定的vpc列表
        :type VpcSet: list of VpcInfo
        :param _ZoneId: 绑定的私有域ID
        :type ZoneId: str
        :param _Tags: 标签
        :type Tags: list of TagInfo
        """
        self._Domain = None
        self._RuleName = None
        self._RuleId = None
        self._RuleType = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._EndPointName = None
        self._EndPointId = None
        self._ForwardAddress = None
        self._VpcSet = None
        self._ZoneId = None
        self._Tags = None

    @property
    def Domain(self):
        r"""私有域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleName(self):
        r"""转发规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleId(self):
        r"""规则id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleType(self):
        r"""转发规则类型：云上到云下DOWN、云下到云上DOWN
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def EndPointName(self):
        r"""终端节点名称
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def EndPointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def ForwardAddress(self):
        r"""转发地址
        :rtype: list of str
        """
        return self._ForwardAddress

    @ForwardAddress.setter
    def ForwardAddress(self, ForwardAddress):
        self._ForwardAddress = ForwardAddress

    @property
    def VpcSet(self):
        r"""私有域绑定的vpc列表
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def ZoneId(self):
        r"""绑定的私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Tags(self):
        r"""标签
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RuleName = params.get("RuleName")
        self._RuleId = params.get("RuleId")
        self._RuleType = params.get("RuleType")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._EndPointName = params.get("EndPointName")
        self._EndPointId = params.get("EndPointId")
        self._ForwardAddress = params.get("ForwardAddress")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._ZoneId = params.get("ZoneId")
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
        


class InboundEndpointSet(AbstractModel):
    r"""终端节点信息列表

    """

    def __init__(self):
        r"""
        :param _EndPointId: 终端节点ID
        :type EndPointId: str
        :param _EndPointName: 名称
        :type EndPointName: str
        :param _UniqVpcId: vpcid
        :type UniqVpcId: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _EndPointService: 终端节点信息
        :type EndPointService: list of EndPointServiceInfo
        """
        self._EndPointId = None
        self._EndPointName = None
        self._UniqVpcId = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._EndPointService = None

    @property
    def EndPointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId

    @property
    def EndPointName(self):
        r"""名称
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def UniqVpcId(self):
        r"""vpcid
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def EndPointService(self):
        r"""终端节点信息
        :rtype: list of EndPointServiceInfo
        """
        return self._EndPointService

    @EndPointService.setter
    def EndPointService(self, EndPointService):
        self._EndPointService = EndPointService


    def _deserialize(self, params):
        self._EndPointId = params.get("EndPointId")
        self._EndPointName = params.get("EndPointName")
        self._UniqVpcId = params.get("UniqVpcId")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("EndPointService") is not None:
            self._EndPointService = []
            for item in params.get("EndPointService"):
                obj = EndPointServiceInfo()
                obj._deserialize(item)
                self._EndPointService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    r"""统计数据表

    """

    def __init__(self):
        r"""
        :param _Resource: 资源描述
        :type Resource: str
        :param _Metric: 表名
        :type Metric: str
        :param _DataSet: 表数据
        :type DataSet: list of DatePoint
        :param _MetricCount: 查询范围内的请求总量
        :type MetricCount: int
        """
        self._Resource = None
        self._Metric = None
        self._DataSet = None
        self._MetricCount = None

    @property
    def Resource(self):
        r"""资源描述
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        r"""表名
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def DataSet(self):
        r"""表数据
        :rtype: list of DatePoint
        """
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet

    @property
    def MetricCount(self):
        r"""查询范围内的请求总量
        :rtype: int
        """
        return self._MetricCount

    @MetricCount.setter
    def MetricCount(self, MetricCount):
        self._MetricCount = MetricCount


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Metric = params.get("Metric")
        if params.get("DataSet") is not None:
            self._DataSet = []
            for item in params.get("DataSet"):
                obj = DatePoint()
                obj._deserialize(item)
                self._DataSet.append(obj)
        self._MetricCount = params.get("MetricCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardRuleRequest(AbstractModel):
    r"""ModifyForwardRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 转发规则ID
        :type RuleId: str
        :param _RuleName: 转发规则名称
        :type RuleName: str
        :param _EndPointId: 终端节点ID
        :type EndPointId: str
        """
        self._RuleId = None
        self._RuleName = None
        self._EndPointId = None

    @property
    def RuleId(self):
        r"""转发规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""转发规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def EndPointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardRuleResponse(AbstractModel):
    r"""ModifyForwardRule返回参数结构体

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


class ModifyInboundEndpointRequest(AbstractModel):
    r"""ModifyInboundEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndpointId: 终端节点ID
        :type EndpointId: str
        :param _EndpointName: 终端节点名称
        :type EndpointName: str
        """
        self._EndpointId = None
        self._EndpointName = None

    @property
    def EndpointId(self):
        r"""终端节点ID
        :rtype: str
        """
        return self._EndpointId

    @EndpointId.setter
    def EndpointId(self, EndpointId):
        self._EndpointId = EndpointId

    @property
    def EndpointName(self):
        r"""终端节点名称
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName


    def _deserialize(self, params):
        self._EndpointId = params.get("EndpointId")
        self._EndpointName = params.get("EndpointName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInboundEndpointResponse(AbstractModel):
    r"""ModifyInboundEndpoint返回参数结构体

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


class ModifyPrivateZoneRecordRequest(AbstractModel):
    r"""ModifyPrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordId: 记录ID
        :type RecordId: str
        :param _RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _SubDomain: 子域名，例如 "www", "m", "@"
        :type SubDomain: str
        :param _RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :type RecordValue: str
        :param _Weight: 记录权重，值为1-100
        :type Weight: int
        :param _MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param _TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        :param _Remark: 备注
        :type Remark: str
        """
        self._ZoneId = None
        self._RecordId = None
        self._RecordType = None
        self._SubDomain = None
        self._RecordValue = None
        self._Weight = None
        self._MX = None
        self._TTL = None
        self._Remark = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        r"""记录ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordType(self):
        r"""记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        r"""子域名，例如 "www", "m", "@"
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        r"""记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def Weight(self):
        r"""记录权重，值为1-100
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        r"""MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        r"""记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

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
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        self._RecordType = params.get("RecordType")
        self._SubDomain = params.get("SubDomain")
        self._RecordValue = params.get("RecordValue")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordResponse(AbstractModel):
    r"""ModifyPrivateZoneRecord返回参数结构体

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


class ModifyPrivateZoneRequest(AbstractModel):
    r"""ModifyPrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _Remark: 备注
        :type Remark: str
        :param _DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED
        :type DnsForwardStatus: str
        :param _CnameSpeedupStatus: 是否开启CNAME加速：ENABLED， DISABLED
        :type CnameSpeedupStatus: str
        """
        self._ZoneId = None
        self._Remark = None
        self._DnsForwardStatus = None
        self._CnameSpeedupStatus = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
    def DnsForwardStatus(self):
        r"""是否开启子域名递归, ENABLED， DISABLED
        :rtype: str
        """
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def CnameSpeedupStatus(self):
        r"""是否开启CNAME加速：ENABLED， DISABLED
        :rtype: str
        """
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Remark = params.get("Remark")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneResponse(AbstractModel):
    r"""ModifyPrivateZone返回参数结构体

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


class ModifyPrivateZoneVpcRequest(AbstractModel):
    r"""ModifyPrivateZoneVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _VpcSet: 私有域关联的全部VPC列表
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 私有域账号关联的全部VPC列表
        :type AccountVpcSet: list of AccountVpcInfo
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""私有域关联的全部VPC列表
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""私有域账号关联的全部VPC列表
        :rtype: list of AccountVpcInfo
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneVpcResponse(AbstractModel):
    r"""ModifyPrivateZoneVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID, zone-12e45ds6
        :type ZoneId: str
        :param _VpcSet: 解析域关联的VPC列表
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 私有域账号关联的全部VPC列表
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""私有域ID, zone-12e45ds6
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        r"""解析域关联的VPC列表
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        r"""私有域账号关联的全部VPC列表
        :rtype: list of AccountVpcInfoOutput
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

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
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyRecordsStatusRequest(AbstractModel):
    r"""ModifyRecordsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordIds: 解析记录ID列表
        :type RecordIds: list of int
        :param _Status: enabled：生效，disabled：失效
        :type Status: str
        """
        self._ZoneId = None
        self._RecordIds = None
        self._Status = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        r"""解析记录ID列表
        :rtype: list of int
        """
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        r"""enabled：生效，disabled：失效
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordIds = params.get("RecordIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordsStatusResponse(AbstractModel):
    r"""ModifyRecordsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordIds: 解析记录ID列表
        :type RecordIds: list of int
        :param _Status: enabled：生效，disabled：失效
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._RecordIds = None
        self._Status = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""私有域ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        r"""解析记录ID列表
        :rtype: list of int
        """
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        r"""enabled：生效，disabled：失效
        :rtype: str
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
        self._ZoneId = params.get("ZoneId")
        self._RecordIds = params.get("RecordIds")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class PrivateDNSAccount(AbstractModel):
    r"""私有域解析账号

    """

    def __init__(self):
        r"""
        :param _Uin: 主账号Uin
        :type Uin: str
        :param _Account: 主账号名称
        :type Account: str
        :param _Nickname: 用户昵称
        :type Nickname: str
        """
        self._Uin = None
        self._Account = None
        self._Nickname = None

    @property
    def Uin(self):
        r"""主账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Account(self):
        r"""主账号名称
        :rtype: str
        """
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Nickname(self):
        r"""用户昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Account = params.get("Account")
        self._Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZone(AbstractModel):
    r"""私有域信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域id: zone-xxxxxxxx
        :type ZoneId: str
        :param _OwnerUin: 域名所有者uin
        :type OwnerUin: int
        :param _Domain: 私有域名
        :type Domain: str
        :param _CreatedOn: 创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 修改时间
        :type UpdatedOn: str
        :param _RecordCount: 记录数
        :type RecordCount: int
        :param _Remark: 备注
        :type Remark: str
        :param _VpcSet: 绑定的Vpc列表
        :type VpcSet: list of VpcInfo
        :param _Status: 私有域绑定VPC状态，未关联vpc：SUSPEND，已关联VPC：ENABLED
，关联VPC失败：FAILED
        :type Status: str
        :param _DnsForwardStatus: 域名递归解析状态：开通：ENABLED, 关闭，DISABLED
        :type DnsForwardStatus: str
        :param _Tags: 标签键值对集合
        :type Tags: list of TagInfo
        :param _AccountVpcSet: 绑定的关联账号的vpc列表
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param _IsCustomTld: 是否自定义TLD
        :type IsCustomTld: bool
        :param _CnameSpeedupStatus: CNAME加速状态：开通：ENABLED, 关闭，DISABLED
        :type CnameSpeedupStatus: str
        :param _ForwardRuleName: 转发规则名称
        :type ForwardRuleName: str
        :param _ForwardRuleType: 转发规则类型：云上到云下，DOWN；云下到云上，UP，目前只支持DOWN
        :type ForwardRuleType: str
        :param _ForwardAddress: 转发的地址
        :type ForwardAddress: str
        :param _EndPointName: 终端节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPointName: str
        :param _DeletedVpcSet: 已删除的vpc
        :type DeletedVpcSet: list of VpcInfo
        """
        self._ZoneId = None
        self._OwnerUin = None
        self._Domain = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._RecordCount = None
        self._Remark = None
        self._VpcSet = None
        self._Status = None
        self._DnsForwardStatus = None
        self._Tags = None
        self._AccountVpcSet = None
        self._IsCustomTld = None
        self._CnameSpeedupStatus = None
        self._ForwardRuleName = None
        self._ForwardRuleType = None
        self._ForwardAddress = None
        self._EndPointName = None
        self._DeletedVpcSet = None

    @property
    def ZoneId(self):
        r"""私有域id: zone-xxxxxxxx
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def OwnerUin(self):
        r"""域名所有者uin
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Domain(self):
        r"""私有域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CreatedOn(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        r"""修改时间
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def RecordCount(self):
        r"""记录数
        :rtype: int
        """
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

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
    def VpcSet(self):
        r"""绑定的Vpc列表
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def Status(self):
        r"""私有域绑定VPC状态，未关联vpc：SUSPEND，已关联VPC：ENABLED
，关联VPC失败：FAILED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DnsForwardStatus(self):
        r"""域名递归解析状态：开通：ENABLED, 关闭，DISABLED
        :rtype: str
        """
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def Tags(self):
        r"""标签键值对集合
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AccountVpcSet(self):
        r"""绑定的关联账号的vpc列表
        :rtype: list of AccountVpcInfoOutput
        """
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def IsCustomTld(self):
        r"""是否自定义TLD
        :rtype: bool
        """
        return self._IsCustomTld

    @IsCustomTld.setter
    def IsCustomTld(self, IsCustomTld):
        self._IsCustomTld = IsCustomTld

    @property
    def CnameSpeedupStatus(self):
        r"""CNAME加速状态：开通：ENABLED, 关闭，DISABLED
        :rtype: str
        """
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus

    @property
    def ForwardRuleName(self):
        r"""转发规则名称
        :rtype: str
        """
        return self._ForwardRuleName

    @ForwardRuleName.setter
    def ForwardRuleName(self, ForwardRuleName):
        self._ForwardRuleName = ForwardRuleName

    @property
    def ForwardRuleType(self):
        r"""转发规则类型：云上到云下，DOWN；云下到云上，UP，目前只支持DOWN
        :rtype: str
        """
        return self._ForwardRuleType

    @ForwardRuleType.setter
    def ForwardRuleType(self, ForwardRuleType):
        self._ForwardRuleType = ForwardRuleType

    @property
    def ForwardAddress(self):
        r"""转发的地址
        :rtype: str
        """
        return self._ForwardAddress

    @ForwardAddress.setter
    def ForwardAddress(self, ForwardAddress):
        self._ForwardAddress = ForwardAddress

    @property
    def EndPointName(self):
        r"""终端节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName

    @property
    def DeletedVpcSet(self):
        r"""已删除的vpc
        :rtype: list of VpcInfo
        """
        return self._DeletedVpcSet

    @DeletedVpcSet.setter
    def DeletedVpcSet(self, DeletedVpcSet):
        self._DeletedVpcSet = DeletedVpcSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._OwnerUin = params.get("OwnerUin")
        self._Domain = params.get("Domain")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._RecordCount = params.get("RecordCount")
        self._Remark = params.get("Remark")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._Status = params.get("Status")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._IsCustomTld = params.get("IsCustomTld")
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        self._ForwardRuleName = params.get("ForwardRuleName")
        self._ForwardRuleType = params.get("ForwardRuleType")
        self._ForwardAddress = params.get("ForwardAddress")
        self._EndPointName = params.get("EndPointName")
        if params.get("DeletedVpcSet") is not None:
            self._DeletedVpcSet = []
            for item in params.get("DeletedVpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._DeletedVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZoneRecord(AbstractModel):
    r"""私有域信息

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录id
        :type RecordId: str
        :param _ZoneId: 私有域id: zone-xxxxxxxx
        :type ZoneId: str
        :param _SubDomain: 子域名
        :type SubDomain: str
        :param _RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _RecordValue: 记录值
        :type RecordValue: str
        :param _TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        :param _MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param _Status: 记录状态：ENABLED
        :type Status: str
        :param _Weight: 记录权重，值为1-100
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _CreatedOn: 记录创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 记录更新时间
        :type UpdatedOn: str
        :param _Extra: 附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Enabled: 0暂停，1启用
        :type Enabled: int
        :param _Remark: 备注
        :type Remark: str
        """
        self._RecordId = None
        self._ZoneId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordValue = None
        self._TTL = None
        self._MX = None
        self._Status = None
        self._Weight = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Extra = None
        self._Enabled = None
        self._Remark = None

    @property
    def RecordId(self):
        r"""记录id
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ZoneId(self):
        r"""私有域id: zone-xxxxxxxx
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubDomain(self):
        r"""子域名
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        r"""记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        r"""记录值
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def TTL(self):
        r"""记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def MX(self):
        r"""MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Status(self):
        r"""记录状态：ENABLED
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        r"""记录权重，值为1-100
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreatedOn(self):
        r"""记录创建时间
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        r"""记录更新时间
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Extra(self):
        r"""附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Enabled(self):
        r"""0暂停，1启用
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

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
        self._RecordId = params.get("RecordId")
        self._ZoneId = params.get("ZoneId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        self._TTL = params.get("TTL")
        self._MX = params.get("MX")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Extra = params.get("Extra")
        self._Enabled = params.get("Enabled")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAsyncBindVpcStatusRequest(AbstractModel):
    r"""QueryAsyncBindVpcStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UniqId: 唯一ID
        :type UniqId: str
        """
        self._UniqId = None

    @property
    def UniqId(self):
        r"""唯一ID
        :rtype: str
        """
        return self._UniqId

    @UniqId.setter
    def UniqId(self, UniqId):
        self._UniqId = UniqId


    def _deserialize(self, params):
        self._UniqId = params.get("UniqId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAsyncBindVpcStatusResponse(AbstractModel):
    r"""QueryAsyncBindVpcStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: processing 处理中，success 执行成功，
failed 执行失败
        :type Status: str
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Status(self):
        r"""processing 处理中，success 执行成功，
failed 执行失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        r"""错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class RecordInfo(AbstractModel):
    r"""私有域信息

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录id
        :type RecordId: str
        :param _ZoneId: 私有域id: zone-xxxxxxxx
        :type ZoneId: str
        :param _SubDomain: 子域名
        :type SubDomain: str
        :param _RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _RecordValue: 记录值
        :type RecordValue: str
        :param _TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        :param _MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param _Weight: 记录权重，值为1-100
        :type Weight: int
        :param _CreatedOn: 记录创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 记录更新时间
        :type UpdatedOn: str
        :param _Enabled: 0暂停，1启用
        :type Enabled: int
        :param _Remark: 备注
        :type Remark: str
        """
        self._RecordId = None
        self._ZoneId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordValue = None
        self._TTL = None
        self._MX = None
        self._Weight = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Enabled = None
        self._Remark = None

    @property
    def RecordId(self):
        r"""记录id
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ZoneId(self):
        r"""私有域id: zone-xxxxxxxx
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubDomain(self):
        r"""子域名
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        r"""记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        r"""记录值
        :rtype: str
        """
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def TTL(self):
        r"""记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def MX(self):
        r"""MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :rtype: int
        """
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Weight(self):
        r"""记录权重，值为1-100
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreatedOn(self):
        r"""记录创建时间
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        r"""记录更新时间
        :rtype: str
        """
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Enabled(self):
        r"""0暂停，1启用
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

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
        self._RecordId = params.get("RecordId")
        self._ZoneId = params.get("ZoneId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        self._TTL = params.get("TTL")
        self._MX = params.get("MX")
        self._Weight = params.get("Weight")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Enabled = params.get("Enabled")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetIpInfo(AbstractModel):
    r"""终端节点信息

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _SubnetVip: ip
        :type SubnetVip: str
        """
        self._SubnetId = None
        self._SubnetVip = None

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
    def SubnetVip(self):
        r"""ip
        :rtype: str
        """
        return self._SubnetVip

    @SubnetVip.setter
    def SubnetVip(self, SubnetVip):
        self._SubnetVip = SubnetVip


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._SubnetVip = params.get("SubnetVip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribePrivateZoneServiceRequest(AbstractModel):
    r"""SubscribePrivateZoneService请求参数结构体

    """


class SubscribePrivateZoneServiceResponse(AbstractModel):
    r"""SubscribePrivateZoneService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceStatus: 私有域解析服务开通状态
        :type ServiceStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        r"""私有域解析服务开通状态
        :rtype: str
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

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
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
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
        


class TldQuota(AbstractModel):
    r"""Tld额度

    """

    def __init__(self):
        r"""
        :param _Total: 总共额度
        :type Total: int
        :param _Used: 已使用额度
        :type Used: int
        :param _Stock: 库存
        :type Stock: int
        :param _Quota: 用户限额
        :type Quota: int
        """
        self._Total = None
        self._Used = None
        self._Stock = None
        self._Quota = None

    @property
    def Total(self):
        r"""总共额度
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        r"""已使用额度
        :rtype: int
        """
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Stock(self):
        r"""库存
        :rtype: int
        """
        return self._Stock

    @Stock.setter
    def Stock(self, Stock):
        self._Stock = Stock

    @property
    def Quota(self):
        r"""用户限额
        :rtype: int
        """
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Stock = params.get("Stock")
        self._Quota = params.get("Quota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    r"""Vpc信息

    """

    def __init__(self):
        r"""
        :param _UniqVpcId: VpcId
        :type UniqVpcId: str
        :param _Region: Vpc所属地区: ap-guangzhou, ap-shanghai
        :type Region: str
        """
        self._UniqVpcId = None
        self._Region = None

    @property
    def UniqVpcId(self):
        r"""VpcId
        :rtype: str
        """
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        r"""Vpc所属地区: ap-guangzhou, ap-shanghai
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        