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


class CHPRequest(AbstractModel):
    """终端骚扰保护请求内容

    """

    def __init__(self):
        r"""
        :param _PhoneNumber: 电话号码
        :type PhoneNumber: str
        """
        self._PhoneNumber = None

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber


    def _deserialize(self, params):
        self._PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CHPResponse(AbstractModel):
    """终端骚扰保护

    """

    def __init__(self):
        r"""
        :param _TagType: 标记类型
 0: 无标记
 50:骚扰电话
 51:房产中介
 52:保险理财
 53:广告推销
 54:诈骗电话
 55:快递电话
 56:出租车专车
        :type TagType: int
        :param _TagCount: 标记次数
        :type TagCount: int
        """
        self._TagType = None
        self._TagCount = None

    @property
    def TagType(self):
        return self._TagType

    @TagType.setter
    def TagType(self, TagType):
        self._TagType = TagType

    @property
    def TagCount(self):
        return self._TagCount

    @TagCount.setter
    def TagCount(self, TagCount):
        self._TagCount = TagCount


    def _deserialize(self, params):
        self._TagType = params.get("TagType")
        self._TagCount = params.get("TagCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSmpnEpaRequest(AbstractModel):
    """CreateSmpnEpa请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestData: 企业号码认证请求内容
        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.EPARequest`
        :param _ResourceId: 用于计费的资源ID
        :type ResourceId: str
        """
        self._RequestData = None
        self._ResourceId = None

    @property
    def RequestData(self):
        return self._RequestData

    @RequestData.setter
    def RequestData(self, RequestData):
        self._RequestData = RequestData

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self._RequestData = EPARequest()
            self._RequestData._deserialize(params.get("RequestData"))
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSmpnEpaResponse(AbstractModel):
    """CreateSmpnEpa返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResponseData: 业号码认证回应内容
        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.EPAResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self._ResponseData = EPAResponse()
            self._ResponseData._deserialize(params.get("ResponseData"))
        self._RequestId = params.get("RequestId")


class DescribeSmpnChpRequest(AbstractModel):
    """DescribeSmpnChp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 客户用于计费的资源Id
        :type ResourceId: str
        :param _RequestData: 终端骚扰保护请求
        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.CHPRequest`
        """
        self._ResourceId = None
        self._RequestData = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RequestData(self):
        return self._RequestData

    @RequestData.setter
    def RequestData(self, RequestData):
        self._RequestData = RequestData


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        if params.get("RequestData") is not None:
            self._RequestData = CHPRequest()
            self._RequestData._deserialize(params.get("RequestData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnChpResponse(AbstractModel):
    """DescribeSmpnChp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResponseData: 终端骚扰保护回应
        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.CHPResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self._ResponseData = CHPResponse()
            self._ResponseData._deserialize(params.get("ResponseData"))
        self._RequestId = params.get("RequestId")


class DescribeSmpnFnrRequest(AbstractModel):
    """DescribeSmpnFnr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestData: 虚假号码识别请求内容
        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.FNRRequest`
        :param _ResourceId: 用于计费的资源ID
        :type ResourceId: str
        """
        self._RequestData = None
        self._ResourceId = None

    @property
    def RequestData(self):
        return self._RequestData

    @RequestData.setter
    def RequestData(self, RequestData):
        self._RequestData = RequestData

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self._RequestData = FNRRequest()
            self._RequestData._deserialize(params.get("RequestData"))
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnFnrResponse(AbstractModel):
    """DescribeSmpnFnr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResponseData: 虚假号码识别回应内容
        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.FNRResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self._ResponseData = FNRResponse()
            self._ResponseData._deserialize(params.get("ResponseData"))
        self._RequestId = params.get("RequestId")


class DescribeSmpnMhmRequest(AbstractModel):
    """DescribeSmpnMhm请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestData: 号码营销监控请求内容
        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.MHMRequest`
        :param _ResourceId: 用于计费的资源ID
        :type ResourceId: str
        """
        self._RequestData = None
        self._ResourceId = None

    @property
    def RequestData(self):
        return self._RequestData

    @RequestData.setter
    def RequestData(self, RequestData):
        self._RequestData = RequestData

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self._RequestData = MHMRequest()
            self._RequestData._deserialize(params.get("RequestData"))
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnMhmResponse(AbstractModel):
    """DescribeSmpnMhm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResponseData: 号码营销监控回应内容
        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.MHMResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self._ResponseData = MHMResponse()
            self._ResponseData._deserialize(params.get("ResponseData"))
        self._RequestId = params.get("RequestId")


class DescribeSmpnMrlRequest(AbstractModel):
    """DescribeSmpnMrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestData: 恶意标记等级请求内容
        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.MRLRequest`
        :param _ResourceId: 用于计费的资源ID
        :type ResourceId: str
        """
        self._RequestData = None
        self._ResourceId = None

    @property
    def RequestData(self):
        return self._RequestData

    @RequestData.setter
    def RequestData(self, RequestData):
        self._RequestData = RequestData

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self._RequestData = MRLRequest()
            self._RequestData._deserialize(params.get("RequestData"))
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnMrlResponse(AbstractModel):
    """DescribeSmpnMrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResponseData: 恶意标记等级回应内容
        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.MRLResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self._ResponseData = MRLResponse()
            self._ResponseData._deserialize(params.get("ResponseData"))
        self._RequestId = params.get("RequestId")


class EPARequest(AbstractModel):
    """企业号码认证请求

    """

    def __init__(self):
        r"""
        :param _PhoneNumber: 电话号码
        :type PhoneNumber: str
        :param _Name: 黄页名称
        :type Name: str
        """
        self._PhoneNumber = None
        self._Name = None

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._PhoneNumber = params.get("PhoneNumber")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EPAResponse(AbstractModel):
    """企业号码认证回应

    """

    def __init__(self):
        r"""
        :param _RetCode: 0成功 其他失败
        :type RetCode: int
        """
        self._RetCode = None

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode


    def _deserialize(self, params):
        self._RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FNRRequest(AbstractModel):
    """虚假号码识别请求

    """

    def __init__(self):
        r"""
        :param _PhoneNumber: 电话号码
        :type PhoneNumber: str
        """
        self._PhoneNumber = None

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber


    def _deserialize(self, params):
        self._PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FNRResponse(AbstractModel):
    """虚假号码识别回应

    """

    def __init__(self):
        r"""
        :param _Status: 虚假号码描述
        :type Status: int
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
        


class MHMRequest(AbstractModel):
    """号码营销监控请求

    """

    def __init__(self):
        r"""
        :param _PhoneNumber: 电话号码
        :type PhoneNumber: str
        """
        self._PhoneNumber = None

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber


    def _deserialize(self, params):
        self._PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MHMResponse(AbstractModel):
    """号码营销监控回应

    """

    def __init__(self):
        r"""
        :param _TagType: 标记类型
 0: 无标记
 50:骚扰电话
 51:房产中介
 52:保险理财
 53:广告推销
 54:诈骗电话
 55:快递电话
 56:出租车专车
        :type TagType: int
        :param _TagCount: 标记次数
        :type TagCount: int
        """
        self._TagType = None
        self._TagCount = None

    @property
    def TagType(self):
        return self._TagType

    @TagType.setter
    def TagType(self, TagType):
        self._TagType = TagType

    @property
    def TagCount(self):
        return self._TagCount

    @TagCount.setter
    def TagCount(self, TagCount):
        self._TagCount = TagCount


    def _deserialize(self, params):
        self._TagType = params.get("TagType")
        self._TagCount = params.get("TagCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MRLRequest(AbstractModel):
    """号码恶意标记等级请求

    """

    def __init__(self):
        r"""
        :param _PhoneNumber: 电话号码
        :type PhoneNumber: str
        """
        self._PhoneNumber = None

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber


    def _deserialize(self, params):
        self._PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MRLResponse(AbstractModel):
    """号码恶意标记等级

    """

    def __init__(self):
        r"""
        :param _DisturbLevel: 骚扰电话恶意标记等级
        :type DisturbLevel: int
        :param _HouseAgentLevel: 房产中介恶意标记等级
        :type HouseAgentLevel: int
        :param _InsuranceLevel: 保险理财恶意标记等级
        :type InsuranceLevel: int
        :param _SalesLevel: 广告推销恶意标记等级
        :type SalesLevel: int
        :param _CheatLevel: 诈骗电话恶意标记等级
        :type CheatLevel: int
        """
        self._DisturbLevel = None
        self._HouseAgentLevel = None
        self._InsuranceLevel = None
        self._SalesLevel = None
        self._CheatLevel = None

    @property
    def DisturbLevel(self):
        return self._DisturbLevel

    @DisturbLevel.setter
    def DisturbLevel(self, DisturbLevel):
        self._DisturbLevel = DisturbLevel

    @property
    def HouseAgentLevel(self):
        return self._HouseAgentLevel

    @HouseAgentLevel.setter
    def HouseAgentLevel(self, HouseAgentLevel):
        self._HouseAgentLevel = HouseAgentLevel

    @property
    def InsuranceLevel(self):
        return self._InsuranceLevel

    @InsuranceLevel.setter
    def InsuranceLevel(self, InsuranceLevel):
        self._InsuranceLevel = InsuranceLevel

    @property
    def SalesLevel(self):
        return self._SalesLevel

    @SalesLevel.setter
    def SalesLevel(self, SalesLevel):
        self._SalesLevel = SalesLevel

    @property
    def CheatLevel(self):
        return self._CheatLevel

    @CheatLevel.setter
    def CheatLevel(self, CheatLevel):
        self._CheatLevel = CheatLevel


    def _deserialize(self, params):
        self._DisturbLevel = params.get("DisturbLevel")
        self._HouseAgentLevel = params.get("HouseAgentLevel")
        self._InsuranceLevel = params.get("InsuranceLevel")
        self._SalesLevel = params.get("SalesLevel")
        self._CheatLevel = params.get("CheatLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        