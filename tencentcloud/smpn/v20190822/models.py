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
        """电话号码
        :rtype: str
        """
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
        """标记类型
 0: 无标记
 50:骚扰电话
 51:房产中介
 52:保险理财
 53:广告推销
 54:诈骗电话
 55:快递电话
 56:出租车专车
        :rtype: int
        """
        return self._TagType

    @TagType.setter
    def TagType(self, TagType):
        self._TagType = TagType

    @property
    def TagCount(self):
        """标记次数
        :rtype: int
        """
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
        """客户用于计费的资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RequestData(self):
        """终端骚扰保护请求
        :rtype: :class:`tencentcloud.smpn.v20190822.models.CHPRequest`
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        """终端骚扰保护回应
        :rtype: :class:`tencentcloud.smpn.v20190822.models.CHPResponse`
        """
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

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
        """虚假号码识别请求内容
        :rtype: :class:`tencentcloud.smpn.v20190822.models.FNRRequest`
        """
        return self._RequestData

    @RequestData.setter
    def RequestData(self, RequestData):
        self._RequestData = RequestData

    @property
    def ResourceId(self):
        """用于计费的资源ID
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        """虚假号码识别回应内容
        :rtype: :class:`tencentcloud.smpn.v20190822.models.FNRResponse`
        """
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

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
        if params.get("ResponseData") is not None:
            self._ResponseData = FNRResponse()
            self._ResponseData._deserialize(params.get("ResponseData"))
        self._RequestId = params.get("RequestId")


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
        """电话号码
        :rtype: str
        """
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
        """虚假号码描述
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
        