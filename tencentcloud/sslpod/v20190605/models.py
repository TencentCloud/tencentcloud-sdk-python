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


class CertInfo(AbstractModel):
    """证书信息

    """

    def __init__(self):
        r"""
        :param _Hash: 证书sha1
        :type Hash: str
        :param _CN: 证书通用名称
        :type CN: str
        :param _SANs: 备用名称
        :type SANs: str
        :param _KeyAlgo: 公钥算法
        :type KeyAlgo: str
        :param _Issuer: 颁发者
        :type Issuer: str
        :param _BeginTime: 有效期开始
        :type BeginTime: str
        :param _EndTime: 有效期结束
        :type EndTime: str
        :param _Days: 剩余天数
        :type Days: int
        :param _Brand: 品牌
        :type Brand: str
        :param _TrustStatus: 信任状态
        :type TrustStatus: str
        :param _CertType: 证书类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CertType: str
        """
        self._Hash = None
        self._CN = None
        self._SANs = None
        self._KeyAlgo = None
        self._Issuer = None
        self._BeginTime = None
        self._EndTime = None
        self._Days = None
        self._Brand = None
        self._TrustStatus = None
        self._CertType = None

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash

    @property
    def CN(self):
        return self._CN

    @CN.setter
    def CN(self, CN):
        self._CN = CN

    @property
    def SANs(self):
        return self._SANs

    @SANs.setter
    def SANs(self, SANs):
        self._SANs = SANs

    @property
    def KeyAlgo(self):
        return self._KeyAlgo

    @KeyAlgo.setter
    def KeyAlgo(self, KeyAlgo):
        self._KeyAlgo = KeyAlgo

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Days(self):
        return self._Days

    @Days.setter
    def Days(self, Days):
        self._Days = Days

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def TrustStatus(self):
        return self._TrustStatus

    @TrustStatus.setter
    def TrustStatus(self, TrustStatus):
        self._TrustStatus = TrustStatus

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType


    def _deserialize(self, params):
        self._Hash = params.get("Hash")
        self._CN = params.get("CN")
        self._SANs = params.get("SANs")
        self._KeyAlgo = params.get("KeyAlgo")
        self._Issuer = params.get("Issuer")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Days = params.get("Days")
        self._Brand = params.get("Brand")
        self._TrustStatus = params.get("TrustStatus")
        self._CertType = params.get("CertType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChartHistogram(AbstractModel):
    """直方图数据结构

    """

    def __init__(self):
        r"""
        :param _Name: 项目名
        :type Name: str
        :param _Children: 项目值
        :type Children: list of ChartNameValue
        """
        self._Name = None
        self._Children = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Children(self):
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChartNameValue(AbstractModel):
    """通用图表键值对

    """

    def __init__(self):
        r"""
        :param _Name: 图表项名称
        :type Name: str
        :param _Value: 图表项值
        :type Value: int
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServerType: 监控的服务器类型（0：web，1：smtp，2：imap，3：pops）
        :type ServerType: int
        :param _Domain: 添加的域名
        :type Domain: str
        :param _Port: 添加的端口
        :type Port: str
        :param _IP: 指定域名的IP
        :type IP: str
        :param _Notice: 是否开启通知告警；true：开启通知告警，false：关闭通知告警
        :type Notice: bool
        :param _Tags: 给域名添加标签，多个以逗号隔开
        :type Tags: str
        """
        self._ServerType = None
        self._Domain = None
        self._Port = None
        self._IP = None
        self._Notice = None
        self._Tags = None

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ServerType = params.get("ServerType")
        self._Domain = params.get("Domain")
        self._Port = params.get("Port")
        self._IP = params.get("IP")
        self._Notice = params.get("Notice")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain返回参数结构体

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


class DashboardResult(AbstractModel):
    """面板数据

    """

    def __init__(self):
        r"""
        :param _SecurityLevelPie: 安全等级图表
        :type SecurityLevelPie: list of ChartNameValue
        :param _CertBrandsPie: 证书品牌图表
        :type CertBrandsPie: list of ChartNameValue
        :param _CertValidTimePie: 证书有效时间图表
        :type CertValidTimePie: list of ChartNameValue
        :param _CertTypePie: 证书类型图表
        :type CertTypePie: list of ChartNameValue
        :param _SSLBugsLoopholeHistogram: ssl bugs图表
        :type SSLBugsLoopholeHistogram: list of ChartHistogram
        :param _ComplianceHistogram: 合规图表
        :type ComplianceHistogram: list of ChartHistogram
        """
        self._SecurityLevelPie = None
        self._CertBrandsPie = None
        self._CertValidTimePie = None
        self._CertTypePie = None
        self._SSLBugsLoopholeHistogram = None
        self._ComplianceHistogram = None

    @property
    def SecurityLevelPie(self):
        return self._SecurityLevelPie

    @SecurityLevelPie.setter
    def SecurityLevelPie(self, SecurityLevelPie):
        self._SecurityLevelPie = SecurityLevelPie

    @property
    def CertBrandsPie(self):
        return self._CertBrandsPie

    @CertBrandsPie.setter
    def CertBrandsPie(self, CertBrandsPie):
        self._CertBrandsPie = CertBrandsPie

    @property
    def CertValidTimePie(self):
        return self._CertValidTimePie

    @CertValidTimePie.setter
    def CertValidTimePie(self, CertValidTimePie):
        self._CertValidTimePie = CertValidTimePie

    @property
    def CertTypePie(self):
        return self._CertTypePie

    @CertTypePie.setter
    def CertTypePie(self, CertTypePie):
        self._CertTypePie = CertTypePie

    @property
    def SSLBugsLoopholeHistogram(self):
        return self._SSLBugsLoopholeHistogram

    @SSLBugsLoopholeHistogram.setter
    def SSLBugsLoopholeHistogram(self, SSLBugsLoopholeHistogram):
        self._SSLBugsLoopholeHistogram = SSLBugsLoopholeHistogram

    @property
    def ComplianceHistogram(self):
        return self._ComplianceHistogram

    @ComplianceHistogram.setter
    def ComplianceHistogram(self, ComplianceHistogram):
        self._ComplianceHistogram = ComplianceHistogram


    def _deserialize(self, params):
        if params.get("SecurityLevelPie") is not None:
            self._SecurityLevelPie = []
            for item in params.get("SecurityLevelPie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self._SecurityLevelPie.append(obj)
        if params.get("CertBrandsPie") is not None:
            self._CertBrandsPie = []
            for item in params.get("CertBrandsPie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self._CertBrandsPie.append(obj)
        if params.get("CertValidTimePie") is not None:
            self._CertValidTimePie = []
            for item in params.get("CertValidTimePie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self._CertValidTimePie.append(obj)
        if params.get("CertTypePie") is not None:
            self._CertTypePie = []
            for item in params.get("CertTypePie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self._CertTypePie.append(obj)
        if params.get("SSLBugsLoopholeHistogram") is not None:
            self._SSLBugsLoopholeHistogram = []
            for item in params.get("SSLBugsLoopholeHistogram"):
                obj = ChartHistogram()
                obj._deserialize(item)
                self._SSLBugsLoopholeHistogram.append(obj)
        if params.get("ComplianceHistogram") is not None:
            self._ComplianceHistogram = []
            for item in params.get("ComplianceHistogram"):
                obj = ChartHistogram()
                obj._deserialize(item)
                self._ComplianceHistogram.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID，可通过<a href="https://cloud.tencent.com/document/api/1084/49339">搜索域名</a>接口获得
        :type DomainId: int
        """
        self._DomainId = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain返回参数结构体

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


class DescribeDashboardRequest(AbstractModel):
    """DescribeDashboard请求参数结构体

    """


class DescribeDashboardResponse(AbstractModel):
    """DescribeDashboard返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: dashboard面板数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.sslpod.v20190605.models.DashboardResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DashboardResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDomainCertsRequest(AbstractModel):
    """DescribeDomainCerts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID，可通过搜索域名接口获得
        :type DomainId: int
        """
        self._DomainId = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainCertsResponse(AbstractModel):
    """DescribeDomainCerts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 证书信息
        :type Data: list of CertInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CertInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainTagsRequest(AbstractModel):
    """DescribeDomainTags请求参数结构体

    """


class DescribeDomainTagsResponse(AbstractModel):
    """DescribeDomainTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: Tag数组
        :type Data: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDomains(AbstractModel):
    """监控域名列表

    """

    def __init__(self):
        r"""
        :param _Result: 列表数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of DomainSiteInfo
        :param _SearchTotal: 搜索出来的数量
        :type SearchTotal: int
        :param _Total: 总数
        :type Total: int
        :param _AllowMonitoringCount: 允许的监控数量
        :type AllowMonitoringCount: int
        :param _CurrentMonitoringCount: 当前监控的数量
        :type CurrentMonitoringCount: int
        :param _AllowMaxAddDomain: 允许添加域名总数
        :type AllowMaxAddDomain: int
        """
        self._Result = None
        self._SearchTotal = None
        self._Total = None
        self._AllowMonitoringCount = None
        self._CurrentMonitoringCount = None
        self._AllowMaxAddDomain = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def SearchTotal(self):
        return self._SearchTotal

    @SearchTotal.setter
    def SearchTotal(self, SearchTotal):
        self._SearchTotal = SearchTotal

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AllowMonitoringCount(self):
        return self._AllowMonitoringCount

    @AllowMonitoringCount.setter
    def AllowMonitoringCount(self, AllowMonitoringCount):
        self._AllowMonitoringCount = AllowMonitoringCount

    @property
    def CurrentMonitoringCount(self):
        return self._CurrentMonitoringCount

    @CurrentMonitoringCount.setter
    def CurrentMonitoringCount(self, CurrentMonitoringCount):
        self._CurrentMonitoringCount = CurrentMonitoringCount

    @property
    def AllowMaxAddDomain(self):
        return self._AllowMaxAddDomain

    @AllowMaxAddDomain.setter
    def AllowMaxAddDomain(self, AllowMaxAddDomain):
        self._AllowMaxAddDomain = AllowMaxAddDomain


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = DomainSiteInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._SearchTotal = params.get("SearchTotal")
        self._Total = params.get("Total")
        self._AllowMonitoringCount = params.get("AllowMonitoringCount")
        self._CurrentMonitoringCount = params.get("CurrentMonitoringCount")
        self._AllowMaxAddDomain = params.get("AllowMaxAddDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 获取数量
        :type Limit: int
        :param _SearchType: 搜索的类型有：none，tags，grade，brand，code，hash，limit，domain。
选tags，入参请填Tag，
选grade，入参请填Grade，
选brand，入参请填Brand，
选code，入参请填Code，
选hash，入参请填Hash
选limit，标识只返回数量信息
选domain，入参请填Domain
        :type SearchType: str
        :param _Tag: 标签，多个标签用逗号分隔
        :type Tag: str
        :param _Grade: 等级
        :type Grade: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Code: 混合搜索
        :type Code: str
        :param _Hash: 证书指纹
        :type Hash: str
        :param _Item: 搜索图标类型
        :type Item: str
        :param _Status: 搜索图标值
        :type Status: str
        :param _Domain: 搜索域名
        :type Domain: str
        """
        self._Offset = None
        self._Limit = None
        self._SearchType = None
        self._Tag = None
        self._Grade = None
        self._Brand = None
        self._Code = None
        self._Hash = None
        self._Item = None
        self._Status = None
        self._Domain = None

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
    def SearchType(self):
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Hash(self):
        return self._Hash

    @Hash.setter
    def Hash(self, Hash):
        self._Hash = Hash

    @property
    def Item(self):
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchType = params.get("SearchType")
        self._Tag = params.get("Tag")
        self._Grade = params.get("Grade")
        self._Brand = params.get("Brand")
        self._Code = params.get("Code")
        self._Hash = params.get("Hash")
        self._Item = params.get("Item")
        self._Status = params.get("Status")
        self._Domain = params.get("Domain")
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
        :param _Data: 列表数据
        :type Data: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomains`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeDomains()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeNoticeInfoRequest(AbstractModel):
    """DescribeNoticeInfo请求参数结构体

    """


class DescribeNoticeInfoResponse(AbstractModel):
    """DescribeNoticeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 通知信息结果
        :type Data: :class:`tencentcloud.sslpod.v20190605.models.NoticeInfoResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = NoticeInfoResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DomainSiteInfo(AbstractModel):
    """监控的域名站点信息

    """

    def __init__(self):
        r"""
        :param _Id: ID标识
        :type Id: int
        :param _Domain: 域名
        :type Domain: str
        :param _Ip: IP地址
        :type Ip: str
        :param _AutoIP: 是否自动获取IP：true：是，false:否
        :type AutoIP: bool
        :param _Grade: 评级
"A+"，
 "A"，
"A-"，
"B"，
"C"，
"D"，
 "E"，
 "F"，
"T"，
        :type Grade: str
        :param _Brand: 证书品牌
        :type Brand: str
        :param _ServerType: 监控服务类型
0 :Web
1: SMTP
2: IMAP
3: POP3
        :type ServerType: int
        :param _GradeCode: 评级Code
0："unknown"，
1："A+"，
2： "A"，
3："A-"，
4："B"，
5："C"，
6："D"，
7： "E"，
8： "F"，
9："T"，
        :type GradeCode: int
        :param _Notice: 是否监控告警；true：是，false:否
        :type Notice: bool
        :param _AccountDomainId: 账号域名关系ID
        :type AccountDomainId: int
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _Status: 域名状态:
连接异常，
证书已过期，
证书已吊销，
证书黑名单，
证书域名不匹配，
证书不可信，
证书密钥弱，
证书即将过期，少于7天，
证书即将过期，少于30天，
正常，
部分异常
        :type Status: str
        :param _Port: 域名端口
        :type Port: str
        """
        self._Id = None
        self._Domain = None
        self._Ip = None
        self._AutoIP = None
        self._Grade = None
        self._Brand = None
        self._ServerType = None
        self._GradeCode = None
        self._Notice = None
        self._AccountDomainId = None
        self._Tags = None
        self._Status = None
        self._Port = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def AutoIP(self):
        return self._AutoIP

    @AutoIP.setter
    def AutoIP(self, AutoIP):
        self._AutoIP = AutoIP

    @property
    def Grade(self):
        return self._Grade

    @Grade.setter
    def Grade(self, Grade):
        self._Grade = Grade

    @property
    def Brand(self):
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ServerType(self):
        return self._ServerType

    @ServerType.setter
    def ServerType(self, ServerType):
        self._ServerType = ServerType

    @property
    def GradeCode(self):
        return self._GradeCode

    @GradeCode.setter
    def GradeCode(self, GradeCode):
        self._GradeCode = GradeCode

    @property
    def Notice(self):
        return self._Notice

    @Notice.setter
    def Notice(self, Notice):
        self._Notice = Notice

    @property
    def AccountDomainId(self):
        return self._AccountDomainId

    @AccountDomainId.setter
    def AccountDomainId(self, AccountDomainId):
        self._AccountDomainId = AccountDomainId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        self._Ip = params.get("Ip")
        self._AutoIP = params.get("AutoIP")
        self._Grade = params.get("Grade")
        self._Brand = params.get("Brand")
        self._ServerType = params.get("ServerType")
        self._GradeCode = params.get("GradeCode")
        self._Notice = params.get("Notice")
        self._AccountDomainId = params.get("AccountDomainId")
        self._Tags = params.get("Tags")
        self._Status = params.get("Status")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitInfo(AbstractModel):
    """通知额度限制信息

    """

    def __init__(self):
        r"""
        :param _Type: 通知类型：
limit_emai：邮件
limit_wechat：微信
limit_phone：手机
        :type Type: str
        :param _Total: 总量
        :type Total: int
        :param _Sent: 已发送
        :type Sent: int
        """
        self._Type = None
        self._Total = None
        self._Sent = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Sent(self):
        return self._Sent

    @Sent.setter
    def Sent(self, Sent):
        self._Sent = Sent


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Total = params.get("Total")
        self._Sent = params.get("Sent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainTagsRequest(AbstractModel):
    """ModifyDomainTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountDomainId: 账号下域名ID
        :type AccountDomainId: int
        :param _Tags: 更新后的tag，多个以逗号隔开
        :type Tags: str
        """
        self._AccountDomainId = None
        self._Tags = None

    @property
    def AccountDomainId(self):
        return self._AccountDomainId

    @AccountDomainId.setter
    def AccountDomainId(self, AccountDomainId):
        self._AccountDomainId = AccountDomainId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AccountDomainId = params.get("AccountDomainId")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainTagsResponse(AbstractModel):
    """ModifyDomainTags返回参数结构体

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


class NoticeInfoResult(AbstractModel):
    """通知信息结果

    """

    def __init__(self):
        r"""
        :param _Id: 通知ID
        :type Id: int
        :param _NoticeType: 通知开关信息；0：关闭；15开启
        :type NoticeType: int
        :param _LimitInfos: 额度信息
        :type LimitInfos: list of LimitInfo
        """
        self._Id = None
        self._NoticeType = None
        self._LimitInfos = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def NoticeType(self):
        return self._NoticeType

    @NoticeType.setter
    def NoticeType(self, NoticeType):
        self._NoticeType = NoticeType

    @property
    def LimitInfos(self):
        return self._LimitInfos

    @LimitInfos.setter
    def LimitInfos(self, LimitInfos):
        self._LimitInfos = LimitInfos


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._NoticeType = params.get("NoticeType")
        if params.get("LimitInfos") is not None:
            self._LimitInfos = []
            for item in params.get("LimitInfos"):
                obj = LimitInfo()
                obj._deserialize(item)
                self._LimitInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshDomainRequest(AbstractModel):
    """RefreshDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名列表中的ID，可通过搜索域名接口获得
        :type DomainId: int
        """
        self._DomainId = None

    @property
    def DomainId(self):
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshDomainResponse(AbstractModel):
    """RefreshDomain返回参数结构体

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


class ResolveDomainRequest(AbstractModel):
    """ResolveDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResolveDomainResponse(AbstractModel):
    """ResolveDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 响应数据
        :type Data: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")