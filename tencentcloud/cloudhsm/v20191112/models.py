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


class AlarmPolicy(AbstractModel):
    """告警策略

    """

    def __init__(self):
        r"""
        :param _Uin: 用户账号
        :type Uin: str
        :param _Event: 告警事件
        :type Event: str
        :param _Limit: 告警阈值
        :type Limit: int
        :param _Status: 告警策略是否生效，0：停用，1：启用
        :type Status: int
        :param _BeginTime: 在这个时间后才允许发送告警
        :type BeginTime: str
        :param _EndTime: 在这个时间前才允许发送告警
        :type EndTime: str
        """
        self._Uin = None
        self._Event = None
        self._Limit = None
        self._Status = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def Uin(self):
        """用户账号
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Event(self):
        """告警事件
        :rtype: str
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def Limit(self):
        """告警阈值
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """告警策略是否生效，0：停用，1：启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BeginTime(self):
        """在这个时间后才允许发送告警
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """在这个时间前才允许发送告警
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Event = params.get("Event")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHSMBySubnetIdRequest(AbstractModel):
    """DescribeHSMBySubnetId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetId: Subnet标识符
        :type SubnetId: str
        """
        self._SubnetId = None

    @property
    def SubnetId(self):
        """Subnet标识符
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHSMBySubnetIdResponse(AbstractModel):
    """DescribeHSMBySubnetId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: HSM数量
        :type TotalCount: int
        :param _SubnetId: 作为查询条件的SubnetId
        :type SubnetId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SubnetId = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """HSM数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SubnetId(self):
        """作为查询条件的SubnetId
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
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
        self._SubnetId = params.get("SubnetId")
        self._RequestId = params.get("RequestId")


class DescribeHSMByVpcIdRequest(AbstractModel):
    """DescribeHSMByVpcId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC标识符
        :type VpcId: str
        """
        self._VpcId = None

    @property
    def VpcId(self):
        """VPC标识符
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHSMByVpcIdResponse(AbstractModel):
    """DescribeHSMByVpcId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: HSM数量
        :type TotalCount: int
        :param _VpcId: 作为查询条件的VpcId
        :type VpcId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcId = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """HSM数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcId(self):
        """作为查询条件的VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
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
        self._VpcId = params.get("VpcId")
        self._RequestId = params.get("RequestId")


class DescribeSubnetRequest(AbstractModel):
    """DescribeSubnet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量。Limit需要在[1, 100]之间。
        :type Limit: int
        :param _Offset: 偏移量。偏移量最小为0。
        :type Offset: int
        :param _VpcId: 查询指定VpcId下的子网信息。
        :type VpcId: str
        :param _SearchWord: 过滤条件
        :type SearchWord: str
        """
        self._Limit = None
        self._Offset = None
        self._VpcId = None
        self._SearchWord = None

    @property
    def Limit(self):
        """返回数量。Limit需要在[1, 100]之间。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量。偏移量最小为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def VpcId(self):
        """查询指定VpcId下的子网信息。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SearchWord(self):
        """过滤条件
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._VpcId = params.get("VpcId")
        self._SearchWord = params.get("SearchWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetResponse(AbstractModel):
    """DescribeSubnet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的子网数量。
        :type TotalCount: int
        :param _SubnetList: 返回的子网实例列表。
        :type SubnetList: list of Subnet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SubnetList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的子网数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SubnetList(self):
        """返回的子网实例列表。
        :rtype: list of Subnet
        """
        return self._SubnetList

    @SubnetList.setter
    def SubnetList(self, SubnetList):
        self._SubnetList = SubnetList

    @property
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
        if params.get("SubnetList") is not None:
            self._SubnetList = []
            for item in params.get("SubnetList"):
                obj = Subnet()
                obj._deserialize(item)
                self._SubnetList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSupportedHsmRequest(AbstractModel):
    """DescribeSupportedHsm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HsmType: Hsm类型，可选值all、virtulization、GHSM、EHSM、SHSM
        :type HsmType: str
        """
        self._HsmType = None

    @property
    def HsmType(self):
        """Hsm类型，可选值all、virtulization、GHSM、EHSM、SHSM
        :rtype: str
        """
        return self._HsmType

    @HsmType.setter
    def HsmType(self, HsmType):
        self._HsmType = HsmType


    def _deserialize(self, params):
        self._HsmType = params.get("HsmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupportedHsmResponse(AbstractModel):
    """DescribeSupportedHsm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceTypes: 当前地域所支持的设备列表
        :type DeviceTypes: list of DeviceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceTypes = None
        self._RequestId = None

    @property
    def DeviceTypes(self):
        """当前地域所支持的设备列表
        :rtype: list of DeviceInfo
        """
        return self._DeviceTypes

    @DeviceTypes.setter
    def DeviceTypes(self, DeviceTypes):
        self._DeviceTypes = DeviceTypes

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceTypes") is not None:
            self._DeviceTypes = []
            for item in params.get("DeviceTypes"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._DeviceTypes.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsgRequest(AbstractModel):
    """DescribeUsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。
        :type Offset: int
        :param _Limit: 返回量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。
        :type Limit: int
        :param _SearchWord: 过滤条件，支持安全组id
        :type SearchWord: str
        """
        self._Offset = None
        self._Limit = None
        self._SearchWord = None

    @property
    def Offset(self):
        """偏移量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回量，当Offset和Limit均为0时将一次性返回用户所有的安全组列表。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """过滤条件，支持安全组id
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord


    def _deserialize(self, params):
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
        


class DescribeUsgResponse(AbstractModel):
    """DescribeUsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SgList: 用户的安全组列表
        :type SgList: list of SgUnit
        :param _TotalCount: 返回的安全组数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SgList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SgList(self):
        """用户的安全组列表
        :rtype: list of SgUnit
        """
        return self._SgList

    @SgList.setter
    def SgList(self, SgList):
        self._SgList = SgList

    @property
    def TotalCount(self):
        """返回的安全组数量
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
        if params.get("SgList") is not None:
            self._SgList = []
            for item in params.get("SgList"):
                obj = SgUnit()
                obj._deserialize(item)
                self._SgList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUsgRuleRequest(AbstractModel):
    """DescribeUsgRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SgIds: 安全组Id列表
        :type SgIds: list of str
        """
        self._SgIds = None

    @property
    def SgIds(self):
        """安全组Id列表
        :rtype: list of str
        """
        return self._SgIds

    @SgIds.setter
    def SgIds(self, SgIds):
        self._SgIds = SgIds


    def _deserialize(self, params):
        self._SgIds = params.get("SgIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsgRuleResponse(AbstractModel):
    """DescribeUsgRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SgRules: 安全组详情
        :type SgRules: list of UsgRuleDetail
        :param _TotalCount: 安全组详情数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SgRules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SgRules(self):
        """安全组详情
        :rtype: list of UsgRuleDetail
        """
        return self._SgRules

    @SgRules.setter
    def SgRules(self, SgRules):
        self._SgRules = SgRules

    @property
    def TotalCount(self):
        """安全组详情数量
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
        if params.get("SgRules") is not None:
            self._SgRules = []
            for item in params.get("SgRules"):
                obj = UsgRuleDetail()
                obj._deserialize(item)
                self._SgRules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeVpcRequest(AbstractModel):
    """DescribeVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 返回偏移量。Offset最小为0。
        :type Offset: int
        :param _Limit: 返回数量。Limit需要在[1, 100]之间。
        :type Limit: int
        :param _SearchWord: 搜索关键字
        :type SearchWord: str
        """
        self._Offset = None
        self._Limit = None
        self._SearchWord = None

    @property
    def Offset(self):
        """返回偏移量。Offset最小为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量。Limit需要在[1, 100]之间。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """搜索关键字
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord


    def _deserialize(self, params):
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
        


class DescribeVpcResponse(AbstractModel):
    """DescribeVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可查询到的所有Vpc实例总数。
        :type TotalCount: int
        :param _VpcList: Vpc对象列表
        :type VpcList: list of Vpc
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """可查询到的所有Vpc实例总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcList(self):
        """Vpc对象列表
        :rtype: list of Vpc
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
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
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = Vpc()
                obj._deserialize(item)
                self._VpcList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVsmAttributesRequest(AbstractModel):
    """DescribeVsmAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        """
        self._ResourceId = None

    @property
    def ResourceId(self):
        """资源Id
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
        


class DescribeVsmAttributesResponse(AbstractModel):
    """DescribeVsmAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _Status: 资源状态，1表示资源为正常，2表示资源处于隔离状态
        :type Status: int
        :param _Vip: 资源IP
        :type Vip: str
        :param _VpcId: 资源所属Vpc
        :type VpcId: str
        :param _SubnetId: 资源所属子网
        :type SubnetId: str
        :param _Model: 资源所属HSM的规格
        :type Model: str
        :param _VsmType: 资源类型，17表示EVSM，33表示GVSM，49表示SVSM
        :type VsmType: int
        :param _RegionId: 地域Id，返回腾讯云地域代码，如广州为1，北京为8
        :type RegionId: int
        :param _ZoneId: 区域Id，返回腾讯云每个地域的可用区代码
        :type ZoneId: int
        :param _ExpireTime: 资源过期时间，以时间戳形式展示。
        :type ExpireTime: int
        :param _SgList: 安全组详情信息,如果未配置字段返回null
        :type SgList: list of UsgRuleDetail
        :param _SubnetName: 子网名
        :type SubnetName: str
        :param _RegionName: 地域名
        :type RegionName: str
        :param _ZoneName: 区域名
        :type ZoneName: str
        :param _Expired: 实例是否已经过期
        :type Expired: bool
        :param _RemainSeconds: 为正数表示实例距离过期时间剩余秒数，为负数表示实例已经过期多少秒
        :type RemainSeconds: int
        :param _VpcName: 私有虚拟网络名称
        :type VpcName: str
        :param _VpcCidrBlock: VPC的IPv4 CIDR
        :type VpcCidrBlock: str
        :param _SubnetCidrBlock: 子网的CIDR
        :type SubnetCidrBlock: str
        :param _Tags: 资源所关联的标签Tag
        :type Tags: list of Tag
        :param _RenewFlag: 资源续费标识，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :type RenewFlag: int
        :param _Manufacturer: 厂商
        :type Manufacturer: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._Status = None
        self._Vip = None
        self._VpcId = None
        self._SubnetId = None
        self._Model = None
        self._VsmType = None
        self._RegionId = None
        self._ZoneId = None
        self._ExpireTime = None
        self._SgList = None
        self._SubnetName = None
        self._RegionName = None
        self._ZoneName = None
        self._Expired = None
        self._RemainSeconds = None
        self._VpcName = None
        self._VpcCidrBlock = None
        self._SubnetCidrBlock = None
        self._Tags = None
        self._RenewFlag = None
        self._Manufacturer = None
        self._RequestId = None

    @property
    def ResourceId(self):
        """资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Status(self):
        """资源状态，1表示资源为正常，2表示资源处于隔离状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        """资源IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VpcId(self):
        """资源所属Vpc
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """资源所属子网
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Model(self):
        """资源所属HSM的规格
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def VsmType(self):
        """资源类型，17表示EVSM，33表示GVSM，49表示SVSM
        :rtype: int
        """
        return self._VsmType

    @VsmType.setter
    def VsmType(self, VsmType):
        self._VsmType = VsmType

    @property
    def RegionId(self):
        """地域Id，返回腾讯云地域代码，如广州为1，北京为8
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        """区域Id，返回腾讯云每个地域的可用区代码
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ExpireTime(self):
        """资源过期时间，以时间戳形式展示。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SgList(self):
        """安全组详情信息,如果未配置字段返回null
        :rtype: list of UsgRuleDetail
        """
        return self._SgList

    @SgList.setter
    def SgList(self, SgList):
        self._SgList = SgList

    @property
    def SubnetName(self):
        """子网名
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def RegionName(self):
        """地域名
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        """区域名
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Expired(self):
        """实例是否已经过期
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def RemainSeconds(self):
        """为正数表示实例距离过期时间剩余秒数，为负数表示实例已经过期多少秒
        :rtype: int
        """
        return self._RemainSeconds

    @RemainSeconds.setter
    def RemainSeconds(self, RemainSeconds):
        self._RemainSeconds = RemainSeconds

    @property
    def VpcName(self):
        """私有虚拟网络名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcCidrBlock(self):
        """VPC的IPv4 CIDR
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def SubnetCidrBlock(self):
        """子网的CIDR
        :rtype: str
        """
        return self._SubnetCidrBlock

    @SubnetCidrBlock.setter
    def SubnetCidrBlock(self, SubnetCidrBlock):
        self._SubnetCidrBlock = SubnetCidrBlock

    @property
    def Tags(self):
        """资源所关联的标签Tag
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RenewFlag(self):
        """资源续费标识，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Manufacturer(self):
        """厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
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
        self._ResourceName = params.get("ResourceName")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Model = params.get("Model")
        self._VsmType = params.get("VsmType")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._ExpireTime = params.get("ExpireTime")
        if params.get("SgList") is not None:
            self._SgList = []
            for item in params.get("SgList"):
                obj = UsgRuleDetail()
                obj._deserialize(item)
                self._SgList.append(obj)
        self._SubnetName = params.get("SubnetName")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        self._Expired = params.get("Expired")
        self._RemainSeconds = params.get("RemainSeconds")
        self._VpcName = params.get("VpcName")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._SubnetCidrBlock = params.get("SubnetCidrBlock")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RenewFlag = params.get("RenewFlag")
        self._Manufacturer = params.get("Manufacturer")
        self._RequestId = params.get("RequestId")


class DescribeVsmsRequest(AbstractModel):
    """DescribeVsms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移
        :type Offset: int
        :param _Limit: 最大数量
        :type Limit: int
        :param _SearchWord: 资源ID或者资源名字模糊查询的关键字
        :type SearchWord: str
        :param _TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        :param _Manufacturer: 设备所属的厂商名称，根据厂商来进行筛选
        :type Manufacturer: str
        :param _HsmType: Hsm服务类型，可选virtualization、physical、GHSM、EHSM、SHSM、all
        :type HsmType: str
        """
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._TagFilters = None
        self._Manufacturer = None
        self._HsmType = None

    @property
    def Offset(self):
        """偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """最大数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchWord(self):
        """资源ID或者资源名字模糊查询的关键字
        :rtype: str
        """
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def TagFilters(self):
        """标签过滤条件
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Manufacturer(self):
        """设备所属的厂商名称，根据厂商来进行筛选
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def HsmType(self):
        """Hsm服务类型，可选virtualization、physical、GHSM、EHSM、SHSM、all
        :rtype: str
        """
        return self._HsmType

    @HsmType.setter
    def HsmType(self, HsmType):
        self._HsmType = HsmType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._Manufacturer = params.get("Manufacturer")
        self._HsmType = params.get("HsmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVsmsResponse(AbstractModel):
    """DescribeVsms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 获取实例的总个数
        :type TotalCount: int
        :param _VsmList: 资源信息
        :type VsmList: list of ResourceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VsmList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """获取实例的总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VsmList(self):
        """资源信息
        :rtype: list of ResourceInfo
        """
        return self._VsmList

    @VsmList.setter
    def VsmList(self, VsmList):
        self._VsmList = VsmList

    @property
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
        if params.get("VsmList") is not None:
            self._VsmList = []
            for item in params.get("VsmList"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self._VsmList.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """设备厂商信息

    """

    def __init__(self):
        r"""
        :param _Manufacturer: 厂商名称
        :type Manufacturer: str
        :param _HsmTypes: 此厂商旗下的设备信息列表
        :type HsmTypes: list of HsmInfo
        """
        self._Manufacturer = None
        self._HsmTypes = None

    @property
    def Manufacturer(self):
        """厂商名称
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def HsmTypes(self):
        """此厂商旗下的设备信息列表
        :rtype: list of HsmInfo
        """
        return self._HsmTypes

    @HsmTypes.setter
    def HsmTypes(self, HsmTypes):
        self._HsmTypes = HsmTypes


    def _deserialize(self, params):
        self._Manufacturer = params.get("Manufacturer")
        if params.get("HsmTypes") is not None:
            self._HsmTypes = []
            for item in params.get("HsmTypes"):
                obj = HsmInfo()
                obj._deserialize(item)
                self._HsmTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAlarmEventRequest(AbstractModel):
    """GetAlarmEvent请求参数结构体

    """


class GetAlarmEventResponse(AbstractModel):
    """GetAlarmEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlarmConfig: 用户所有的告警策略
        :type AlarmConfig: list of AlarmPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlarmConfig = None
        self._RequestId = None

    @property
    def AlarmConfig(self):
        """用户所有的告警策略
        :rtype: list of AlarmPolicy
        """
        return self._AlarmConfig

    @AlarmConfig.setter
    def AlarmConfig(self, AlarmConfig):
        self._AlarmConfig = AlarmConfig

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AlarmConfig") is not None:
            self._AlarmConfig = []
            for item in params.get("AlarmConfig"):
                obj = AlarmPolicy()
                obj._deserialize(item)
                self._AlarmConfig.append(obj)
        self._RequestId = params.get("RequestId")


class GetVsmMonitorInfoRequest(AbstractModel):
    """GetVsmMonitorInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        """
        self._ResourceId = None
        self._ResourceName = None

    @property
    def ResourceId(self):
        """资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetVsmMonitorInfoResponse(AbstractModel):
    """GetVsmMonitorInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorInfo: VSM监控信息
        :type MonitorInfo: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonitorInfo = None
        self._RequestId = None

    @property
    def MonitorInfo(self):
        """VSM监控信息
        :rtype: list of str
        """
        return self._MonitorInfo

    @MonitorInfo.setter
    def MonitorInfo(self, MonitorInfo):
        self._MonitorInfo = MonitorInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MonitorInfo = params.get("MonitorInfo")
        self._RequestId = params.get("RequestId")


class HsmInfo(AbstractModel):
    """支持的加密机类型信息

    """

    def __init__(self):
        r"""
        :param _Model: 加密机型号
        :type Model: str
        :param _VsmTypes: 此类型的加密机所支持的VSM类型列表
        :type VsmTypes: list of VsmInfo
        :param _HsmType: 加密机母机类型：virtualization、GHSM、EHSM、SHSM
        :type HsmType: str
        """
        self._Model = None
        self._VsmTypes = None
        self._HsmType = None

    @property
    def Model(self):
        """加密机型号
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def VsmTypes(self):
        """此类型的加密机所支持的VSM类型列表
        :rtype: list of VsmInfo
        """
        return self._VsmTypes

    @VsmTypes.setter
    def VsmTypes(self, VsmTypes):
        self._VsmTypes = VsmTypes

    @property
    def HsmType(self):
        """加密机母机类型：virtualization、GHSM、EHSM、SHSM
        :rtype: str
        """
        return self._HsmType

    @HsmType.setter
    def HsmType(self, HsmType):
        self._HsmType = HsmType


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("VsmTypes") is not None:
            self._VsmTypes = []
            for item in params.get("VsmTypes"):
                obj = VsmInfo()
                obj._deserialize(item)
                self._VsmTypes.append(obj)
        self._HsmType = params.get("HsmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceBuyVsmRequest(AbstractModel):
    """InquiryPriceBuyVsm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GoodsNum: 需购买实例的数量
        :type GoodsNum: int
        :param _PayMode: 付费模式：0表示按需计费/后付费，1表示预付费
        :type PayMode: int
        :param _TimeSpan: 商品的时间大小，整型参数，举例：当TimeSpan为1，TImeUnit为m时，表示询价购买时长为1个月时的价格
        :type TimeSpan: str
        :param _TimeUnit: 商品的时间单位，m表示月，y表示年
        :type TimeUnit: str
        :param _Currency: 货币类型，默认为CNY
        :type Currency: str
        :param _Type: 默认为CREATE，可选RENEW
        :type Type: str
        :param _HsmType: Hsm服务类型，可选值virtualization、physical、GHSM、EHSM、SHSM
        :type HsmType: str
        """
        self._GoodsNum = None
        self._PayMode = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._Currency = None
        self._Type = None
        self._HsmType = None

    @property
    def GoodsNum(self):
        """需购买实例的数量
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def PayMode(self):
        """付费模式：0表示按需计费/后付费，1表示预付费
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def TimeSpan(self):
        """商品的时间大小，整型参数，举例：当TimeSpan为1，TImeUnit为m时，表示询价购买时长为1个月时的价格
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """商品的时间单位，m表示月，y表示年
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def Currency(self):
        """货币类型，默认为CNY
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def Type(self):
        """默认为CREATE，可选RENEW
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def HsmType(self):
        """Hsm服务类型，可选值virtualization、physical、GHSM、EHSM、SHSM
        :rtype: str
        """
        return self._HsmType

    @HsmType.setter
    def HsmType(self, HsmType):
        self._HsmType = HsmType


    def _deserialize(self, params):
        self._GoodsNum = params.get("GoodsNum")
        self._PayMode = params.get("PayMode")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._Currency = params.get("Currency")
        self._Type = params.get("Type")
        self._HsmType = params.get("HsmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceBuyVsmResponse(AbstractModel):
    """InquiryPriceBuyVsm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCost: 原始总金额，浮点型参数，精确到小数点后两位，如：2000.99
        :type TotalCost: float
        :param _GoodsNum: 购买的实例数量
        :type GoodsNum: int
        :param _TimeSpan: 商品的时间大小，整型参数，举例：当TimeSpan为1，TImeUnit为m时，表示询价购买时长为1个月时的价格
        :type TimeSpan: str
        :param _TimeUnit: 商品的时间单位，m表示月，y表示年
        :type TimeUnit: str
        :param _OriginalCost: 应付总金额，浮点型参数，精确到小数点后两位，如：2000.99
        :type OriginalCost: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCost = None
        self._GoodsNum = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._OriginalCost = None
        self._RequestId = None

    @property
    def TotalCost(self):
        """原始总金额，浮点型参数，精确到小数点后两位，如：2000.99
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def GoodsNum(self):
        """购买的实例数量
        :rtype: int
        """
        return self._GoodsNum

    @GoodsNum.setter
    def GoodsNum(self, GoodsNum):
        self._GoodsNum = GoodsNum

    @property
    def TimeSpan(self):
        """商品的时间大小，整型参数，举例：当TimeSpan为1，TImeUnit为m时，表示询价购买时长为1个月时的价格
        :rtype: str
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        """商品的时间单位，m表示月，y表示年
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def OriginalCost(self):
        """应付总金额，浮点型参数，精确到小数点后两位，如：2000.99
        :rtype: float
        """
        return self._OriginalCost

    @OriginalCost.setter
    def OriginalCost(self, OriginalCost):
        self._OriginalCost = OriginalCost

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCost = params.get("TotalCost")
        self._GoodsNum = params.get("GoodsNum")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._OriginalCost = params.get("OriginalCost")
        self._RequestId = params.get("RequestId")


class ModifyAlarmEventRequest(AbstractModel):
    """ModifyAlarmEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Event: 告警事件，支持CPU、MEM、TCP
        :type Event: str
        :param _Limit: 告警阈值
        :type Limit: int
        :param _Status: 告警状态，0表示停用，1表示启动
        :type Status: int
        :param _BeginTime: 告警开始时间，只有在这个时间后才会发送告警，当跟EndTime同时为空时表示全天告警
        :type BeginTime: str
        :param _EndTime: 告警结束时间，只有在这个时间前才会发送告警，当跟BeginTime同时为空时表示全天告警
        :type EndTime: str
        """
        self._Event = None
        self._Limit = None
        self._Status = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def Event(self):
        """告警事件，支持CPU、MEM、TCP
        :rtype: str
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def Limit(self):
        """告警阈值
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """告警状态，0表示停用，1表示启动
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BeginTime(self):
        """告警开始时间，只有在这个时间后才会发送告警，当跟EndTime同时为空时表示全天告警
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """告警结束时间，只有在这个时间前才会发送告警，当跟BeginTime同时为空时表示全天告警
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Event = params.get("Event")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAlarmEventResponse(AbstractModel):
    """ModifyAlarmEvent返回参数结构体

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


class ModifyVsmAttributesRequest(AbstractModel):
    """ModifyVsmAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _Type: UpdateResourceName-修改资源名称,
UpdateSgIds-修改安全组名称,
UpdateNetWork-修改网络,
Default-默认不修改
        :type Type: list of str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _SgIds: 安全组Id
        :type SgIds: list of str
        :param _VpcId: 虚拟专网Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _AlarmStatus: 告警开关，0表示关闭告警，1表示启用告警
        :type AlarmStatus: int
        """
        self._ResourceId = None
        self._Type = None
        self._ResourceName = None
        self._SgIds = None
        self._VpcId = None
        self._SubnetId = None
        self._AlarmStatus = None

    @property
    def ResourceId(self):
        """资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Type(self):
        """UpdateResourceName-修改资源名称,
UpdateSgIds-修改安全组名称,
UpdateNetWork-修改网络,
Default-默认不修改
        :rtype: list of str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def SgIds(self):
        """安全组Id
        :rtype: list of str
        """
        return self._SgIds

    @SgIds.setter
    def SgIds(self, SgIds):
        self._SgIds = SgIds

    @property
    def VpcId(self):
        """虚拟专网Id
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

    @property
    def AlarmStatus(self):
        """告警开关，0表示关闭告警，1表示启用告警
        :rtype: int
        """
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Type = params.get("Type")
        self._ResourceName = params.get("ResourceName")
        self._SgIds = params.get("SgIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AlarmStatus = params.get("AlarmStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVsmAttributesResponse(AbstractModel):
    """ModifyVsmAttributes返回参数结构体

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


class ResourceInfo(AbstractModel):
    """资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _Status: 资源状态，1-正常，2-隔离，3-销毁
        :type Status: int
        :param _Vip: 资源IP
        :type Vip: str
        :param _VpcId: 资源所属Vpc
        :type VpcId: str
        :param _SubnetId: 资源所属子网
        :type SubnetId: str
        :param _Model: 资源所属HSM规格
        :type Model: str
        :param _VsmType: 云加密机类型id
        :type VsmType: int
        :param _RegionId: 地域Id
        :type RegionId: int
        :param _ZoneId: 区域Id
        :type ZoneId: int
        :param _ExpireTime: 过期时间（Epoch Unix Timestamp）
        :type ExpireTime: int
        :param _RegionName: 地域名
        :type RegionName: str
        :param _ZoneName: 区域名
        :type ZoneName: str
        :param _SgList: 实例的安全组列表
        :type SgList: list of SgUnit
        :param _SubnetName: 子网名称
        :type SubnetName: str
        :param _Expired: 当前实例是否已经过期
        :type Expired: bool
        :param _RemainSeconds: 为正数表示实例距离过期时间还剩余多少秒，为负数表示已经过期多少秒
        :type RemainSeconds: int
        :param _VpcName: Vpc名称
        :type VpcName: str
        :param _CreateUin: 创建者Uin账号
        :type CreateUin: str
        :param _RenewFlag: 自动续费状态标识， 0-手动续费，1-自动续费，2-到期不续
        :type RenewFlag: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _Manufacturer: 厂商
        :type Manufacturer: str
        :param _AlarmStatus: 告警状态，0：停用，1：启用
        :type AlarmStatus: int
        """
        self._ResourceId = None
        self._ResourceName = None
        self._Status = None
        self._Vip = None
        self._VpcId = None
        self._SubnetId = None
        self._Model = None
        self._VsmType = None
        self._RegionId = None
        self._ZoneId = None
        self._ExpireTime = None
        self._RegionName = None
        self._ZoneName = None
        self._SgList = None
        self._SubnetName = None
        self._Expired = None
        self._RemainSeconds = None
        self._VpcName = None
        self._CreateUin = None
        self._RenewFlag = None
        self._Tags = None
        self._Manufacturer = None
        self._AlarmStatus = None

    @property
    def ResourceId(self):
        """资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def Status(self):
        """资源状态，1-正常，2-隔离，3-销毁
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vip(self):
        """资源IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VpcId(self):
        """资源所属Vpc
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """资源所属子网
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Model(self):
        """资源所属HSM规格
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def VsmType(self):
        """云加密机类型id
        :rtype: int
        """
        return self._VsmType

    @VsmType.setter
    def VsmType(self, VsmType):
        self._VsmType = VsmType

    @property
    def RegionId(self):
        """地域Id
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ZoneId(self):
        """区域Id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ExpireTime(self):
        """过期时间（Epoch Unix Timestamp）
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def RegionName(self):
        """地域名
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ZoneName(self):
        """区域名
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def SgList(self):
        """实例的安全组列表
        :rtype: list of SgUnit
        """
        return self._SgList

    @SgList.setter
    def SgList(self, SgList):
        self._SgList = SgList

    @property
    def SubnetName(self):
        """子网名称
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def Expired(self):
        """当前实例是否已经过期
        :rtype: bool
        """
        return self._Expired

    @Expired.setter
    def Expired(self, Expired):
        self._Expired = Expired

    @property
    def RemainSeconds(self):
        """为正数表示实例距离过期时间还剩余多少秒，为负数表示已经过期多少秒
        :rtype: int
        """
        return self._RemainSeconds

    @RemainSeconds.setter
    def RemainSeconds(self, RemainSeconds):
        self._RemainSeconds = RemainSeconds

    @property
    def VpcName(self):
        """Vpc名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def CreateUin(self):
        """创建者Uin账号
        :rtype: str
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def RenewFlag(self):
        """自动续费状态标识， 0-手动续费，1-自动续费，2-到期不续
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

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
    def Manufacturer(self):
        """厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def AlarmStatus(self):
        """告警状态，0：停用，1：启用
        :rtype: int
        """
        return self._AlarmStatus

    @AlarmStatus.setter
    def AlarmStatus(self, AlarmStatus):
        self._AlarmStatus = AlarmStatus


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._Status = params.get("Status")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Model = params.get("Model")
        self._VsmType = params.get("VsmType")
        self._RegionId = params.get("RegionId")
        self._ZoneId = params.get("ZoneId")
        self._ExpireTime = params.get("ExpireTime")
        self._RegionName = params.get("RegionName")
        self._ZoneName = params.get("ZoneName")
        if params.get("SgList") is not None:
            self._SgList = []
            for item in params.get("SgList"):
                obj = SgUnit()
                obj._deserialize(item)
                self._SgList.append(obj)
        self._SubnetName = params.get("SubnetName")
        self._Expired = params.get("Expired")
        self._RemainSeconds = params.get("RemainSeconds")
        self._VpcName = params.get("VpcName")
        self._CreateUin = params.get("CreateUin")
        self._RenewFlag = params.get("RenewFlag")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Manufacturer = params.get("Manufacturer")
        self._AlarmStatus = params.get("AlarmStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SgUnit(AbstractModel):
    """安全组基础信息

    """

    def __init__(self):
        r"""
        :param _SgId: 安全组Id
        :type SgId: str
        :param _SgName: 安全组名称
        :type SgName: str
        :param _SgRemark: 备注
        :type SgRemark: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._SgId = None
        self._SgName = None
        self._SgRemark = None
        self._CreateTime = None

    @property
    def SgId(self):
        """安全组Id
        :rtype: str
        """
        return self._SgId

    @SgId.setter
    def SgId(self, SgId):
        self._SgId = SgId

    @property
    def SgName(self):
        """安全组名称
        :rtype: str
        """
        return self._SgName

    @SgName.setter
    def SgName(self, SgName):
        self._SgName = SgName

    @property
    def SgRemark(self):
        """备注
        :rtype: str
        """
        return self._SgRemark

    @SgRemark.setter
    def SgRemark(self, SgRemark):
        self._SgRemark = SgRemark

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._SgId = params.get("SgId")
        self._SgName = params.get("SgName")
        self._SgRemark = params.get("SgRemark")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Subnet(AbstractModel):
    """Subnet对象

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。
        :type VpcId: str
        :param _SubnetId: 子网实例ID，例如：subnet-bthucmmy。
        :type SubnetId: str
        :param _SubnetName: 子网名称。
        :type SubnetName: str
        :param _CidrBlock: 子网的 IPv4 CIDR。
        :type CidrBlock: str
        :param _CreatedTime: 创建时间。
        :type CreatedTime: str
        :param _AvailableIpAddressCount: 可用IP数。
        :type AvailableIpAddressCount: int
        :param _Ipv6CidrBlock: 子网的 IPv6 CIDR。
        :type Ipv6CidrBlock: str
        :param _TotalIpAddressCount: 总IP数
        :type TotalIpAddressCount: int
        :param _IsDefault: 是否为默认Subnet
        :type IsDefault: bool
        """
        self._VpcId = None
        self._SubnetId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._CreatedTime = None
        self._AvailableIpAddressCount = None
        self._Ipv6CidrBlock = None
        self._TotalIpAddressCount = None
        self._IsDefault = None

    @property
    def VpcId(self):
        """VPC实例ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网实例ID，例如：subnet-bthucmmy。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        """子网名称。
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        """子网的 IPv4 CIDR。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def CreatedTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AvailableIpAddressCount(self):
        """可用IP数。
        :rtype: int
        """
        return self._AvailableIpAddressCount

    @AvailableIpAddressCount.setter
    def AvailableIpAddressCount(self, AvailableIpAddressCount):
        self._AvailableIpAddressCount = AvailableIpAddressCount

    @property
    def Ipv6CidrBlock(self):
        """子网的 IPv6 CIDR。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def TotalIpAddressCount(self):
        """总IP数
        :rtype: int
        """
        return self._TotalIpAddressCount

    @TotalIpAddressCount.setter
    def TotalIpAddressCount(self, TotalIpAddressCount):
        self._TotalIpAddressCount = TotalIpAddressCount

    @property
    def IsDefault(self):
        """是否为默认Subnet
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._CreatedTime = params.get("CreatedTime")
        self._AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self._TotalIpAddressCount = params.get("TotalIpAddressCount")
        self._IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

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
        


class TagFilter(AbstractModel):
    """标签过滤参数

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
        


class UsgPolicy(AbstractModel):
    """安全组策略

    """

    def __init__(self):
        r"""
        :param _Ip: cidr格式地址
        :type Ip: str
        :param _Id: 安全组id代表的地址集合
        :type Id: str
        :param _AddressModule: 地址组id代表的地址集合
        :type AddressModule: str
        :param _Proto: 协议
        :type Proto: str
        :param _Port: 端口
        :type Port: str
        :param _ServiceModule: 服务组id代表的协议和端口集合
        :type ServiceModule: str
        :param _Desc: 备注
        :type Desc: str
        :param _Action: 匹配后行为:ACCEPT/DROP
        :type Action: str
        """
        self._Ip = None
        self._Id = None
        self._AddressModule = None
        self._Proto = None
        self._Port = None
        self._ServiceModule = None
        self._Desc = None
        self._Action = None

    @property
    def Ip(self):
        """cidr格式地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Id(self):
        """安全组id代表的地址集合
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AddressModule(self):
        """地址组id代表的地址集合
        :rtype: str
        """
        return self._AddressModule

    @AddressModule.setter
    def AddressModule(self, AddressModule):
        self._AddressModule = AddressModule

    @property
    def Proto(self):
        """协议
        :rtype: str
        """
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto

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
    def ServiceModule(self):
        """服务组id代表的协议和端口集合
        :rtype: str
        """
        return self._ServiceModule

    @ServiceModule.setter
    def ServiceModule(self, ServiceModule):
        self._ServiceModule = ServiceModule

    @property
    def Desc(self):
        """备注
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Action(self):
        """匹配后行为:ACCEPT/DROP
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Id = params.get("Id")
        self._AddressModule = params.get("AddressModule")
        self._Proto = params.get("Proto")
        self._Port = params.get("Port")
        self._ServiceModule = params.get("ServiceModule")
        self._Desc = params.get("Desc")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsgRuleDetail(AbstractModel):
    """安全组规则详情

    """

    def __init__(self):
        r"""
        :param _InBound: 入站规则
        :type InBound: list of UsgPolicy
        :param _OutBound: 出站规则
        :type OutBound: list of UsgPolicy
        :param _SgId: 安全组Id
        :type SgId: str
        :param _SgName: 安全组名称
        :type SgName: str
        :param _SgRemark: 备注
        :type SgRemark: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Version: 版本
        :type Version: int
        """
        self._InBound = None
        self._OutBound = None
        self._SgId = None
        self._SgName = None
        self._SgRemark = None
        self._CreateTime = None
        self._Version = None

    @property
    def InBound(self):
        """入站规则
        :rtype: list of UsgPolicy
        """
        return self._InBound

    @InBound.setter
    def InBound(self, InBound):
        self._InBound = InBound

    @property
    def OutBound(self):
        """出站规则
        :rtype: list of UsgPolicy
        """
        return self._OutBound

    @OutBound.setter
    def OutBound(self, OutBound):
        self._OutBound = OutBound

    @property
    def SgId(self):
        """安全组Id
        :rtype: str
        """
        return self._SgId

    @SgId.setter
    def SgId(self, SgId):
        self._SgId = SgId

    @property
    def SgName(self):
        """安全组名称
        :rtype: str
        """
        return self._SgName

    @SgName.setter
    def SgName(self, SgName):
        self._SgName = SgName

    @property
    def SgRemark(self):
        """备注
        :rtype: str
        """
        return self._SgRemark

    @SgRemark.setter
    def SgRemark(self, SgRemark):
        self._SgRemark = SgRemark

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
    def Version(self):
        """版本
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        if params.get("InBound") is not None:
            self._InBound = []
            for item in params.get("InBound"):
                obj = UsgPolicy()
                obj._deserialize(item)
                self._InBound.append(obj)
        if params.get("OutBound") is not None:
            self._OutBound = []
            for item in params.get("OutBound"):
                obj = UsgPolicy()
                obj._deserialize(item)
                self._OutBound.append(obj)
        self._SgId = params.get("SgId")
        self._SgName = params.get("SgName")
        self._SgRemark = params.get("SgRemark")
        self._CreateTime = params.get("CreateTime")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Vpc(AbstractModel):
    """VPC对象

    """

    def __init__(self):
        r"""
        :param _VpcName: Vpc名称
        :type VpcName: str
        :param _VpcId: VpcId
        :type VpcId: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _IsDefault: 是否为默认VPC
        :type IsDefault: bool
        """
        self._VpcName = None
        self._VpcId = None
        self._CreatedTime = None
        self._IsDefault = None

    @property
    def VpcName(self):
        """Vpc名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcId(self):
        """VpcId
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CreatedTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def IsDefault(self):
        """是否为默认VPC
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        self._VpcName = params.get("VpcName")
        self._VpcId = params.get("VpcId")
        self._CreatedTime = params.get("CreatedTime")
        self._IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VsmInfo(AbstractModel):
    """支持的Vsm类型信息

    """

    def __init__(self):
        r"""
        :param _TypeName: VSM类型名称
        :type TypeName: str
        :param _TypeID: VSM类型值
        :type TypeID: int
        """
        self._TypeName = None
        self._TypeID = None

    @property
    def TypeName(self):
        """VSM类型名称
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def TypeID(self):
        """VSM类型值
        :rtype: int
        """
        return self._TypeID

    @TypeID.setter
    def TypeID(self, TypeID):
        self._TypeID = TypeID


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._TypeID = params.get("TypeID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        