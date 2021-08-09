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
        """
        :param PhoneNumber: 电话号码\n        :type PhoneNumber: str\n        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CHPResponse(AbstractModel):
    """终端骚扰保护

    """

    def __init__(self):
        """
        :param TagType: 标记类型
 0: 无标记
 50:骚扰电话
 51:房产中介
 52:保险理财
 53:广告推销
 54:诈骗电话
 55:快递电话
 56:出租车专车\n        :type TagType: int\n        :param TagCount: 标记次数\n        :type TagCount: int\n        """
        self.TagType = None
        self.TagCount = None


    def _deserialize(self, params):
        self.TagType = params.get("TagType")
        self.TagCount = params.get("TagCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSmpnEpaRequest(AbstractModel):
    """CreateSmpnEpa请求参数结构体

    """

    def __init__(self):
        """
        :param RequestData: 企业号码认证请求内容\n        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.EPARequest`\n        :param ResourceId: 用于计费的资源ID\n        :type ResourceId: str\n        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = EPARequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSmpnEpaResponse(AbstractModel):
    """CreateSmpnEpa返回参数结构体

    """

    def __init__(self):
        """
        :param ResponseData: 业号码认证回应内容\n        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.EPAResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = EPAResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnChpRequest(AbstractModel):
    """DescribeSmpnChp请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 客户用于计费的资源Id\n        :type ResourceId: str\n        :param RequestData: 终端骚扰保护请求\n        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.CHPRequest`\n        """
        self.ResourceId = None
        self.RequestData = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        if params.get("RequestData") is not None:
            self.RequestData = CHPRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnChpResponse(AbstractModel):
    """DescribeSmpnChp返回参数结构体

    """

    def __init__(self):
        """
        :param ResponseData: 终端骚扰保护回应\n        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.CHPResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = CHPResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnFnrRequest(AbstractModel):
    """DescribeSmpnFnr请求参数结构体

    """

    def __init__(self):
        """
        :param RequestData: 虚假号码识别请求内容\n        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.FNRRequest`\n        :param ResourceId: 用于计费的资源ID\n        :type ResourceId: str\n        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = FNRRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnFnrResponse(AbstractModel):
    """DescribeSmpnFnr返回参数结构体

    """

    def __init__(self):
        """
        :param ResponseData: 虚假号码识别回应内容\n        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.FNRResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = FNRResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnMhmRequest(AbstractModel):
    """DescribeSmpnMhm请求参数结构体

    """

    def __init__(self):
        """
        :param RequestData: 号码营销监控请求内容\n        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.MHMRequest`\n        :param ResourceId: 用于计费的资源ID\n        :type ResourceId: str\n        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = MHMRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnMhmResponse(AbstractModel):
    """DescribeSmpnMhm返回参数结构体

    """

    def __init__(self):
        """
        :param ResponseData: 号码营销监控回应内容\n        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.MHMResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = MHMResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnMrlRequest(AbstractModel):
    """DescribeSmpnMrl请求参数结构体

    """

    def __init__(self):
        """
        :param RequestData: 恶意标记等级请求内容\n        :type RequestData: :class:`tencentcloud.smpn.v20190822.models.MRLRequest`\n        :param ResourceId: 用于计费的资源ID\n        :type ResourceId: str\n        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = MRLRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmpnMrlResponse(AbstractModel):
    """DescribeSmpnMrl返回参数结构体

    """

    def __init__(self):
        """
        :param ResponseData: 恶意标记等级回应内容\n        :type ResponseData: :class:`tencentcloud.smpn.v20190822.models.MRLResponse`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = MRLResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class EPARequest(AbstractModel):
    """企业号码认证请求

    """

    def __init__(self):
        """
        :param PhoneNumber: 电话号码\n        :type PhoneNumber: str\n        :param Name: 黄页名称\n        :type Name: str\n        """
        self.PhoneNumber = None
        self.Name = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EPAResponse(AbstractModel):
    """企业号码认证回应

    """

    def __init__(self):
        """
        :param RetCode: 0成功 其他失败\n        :type RetCode: int\n        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FNRRequest(AbstractModel):
    """虚假号码识别请求

    """

    def __init__(self):
        """
        :param PhoneNumber: 电话号码\n        :type PhoneNumber: str\n        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FNRResponse(AbstractModel):
    """虚假号码识别回应

    """

    def __init__(self):
        """
        :param Status: 虚假号码描述\n        :type Status: int\n        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MHMRequest(AbstractModel):
    """号码营销监控请求

    """

    def __init__(self):
        """
        :param PhoneNumber: 电话号码\n        :type PhoneNumber: str\n        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MHMResponse(AbstractModel):
    """号码营销监控回应

    """

    def __init__(self):
        """
        :param TagType: 标记类型
 0: 无标记
 50:骚扰电话
 51:房产中介
 52:保险理财
 53:广告推销
 54:诈骗电话
 55:快递电话
 56:出租车专车\n        :type TagType: int\n        :param TagCount: 标记次数\n        :type TagCount: int\n        """
        self.TagType = None
        self.TagCount = None


    def _deserialize(self, params):
        self.TagType = params.get("TagType")
        self.TagCount = params.get("TagCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MRLRequest(AbstractModel):
    """号码恶意标记等级请求

    """

    def __init__(self):
        """
        :param PhoneNumber: 电话号码\n        :type PhoneNumber: str\n        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MRLResponse(AbstractModel):
    """号码恶意标记等级

    """

    def __init__(self):
        """
        :param DisturbLevel: 骚扰电话恶意标记等级\n        :type DisturbLevel: int\n        :param HouseAgentLevel: 房产中介恶意标记等级\n        :type HouseAgentLevel: int\n        :param InsuranceLevel: 保险理财恶意标记等级\n        :type InsuranceLevel: int\n        :param SalesLevel: 广告推销恶意标记等级\n        :type SalesLevel: int\n        :param CheatLevel: 诈骗电话恶意标记等级\n        :type CheatLevel: int\n        """
        self.DisturbLevel = None
        self.HouseAgentLevel = None
        self.InsuranceLevel = None
        self.SalesLevel = None
        self.CheatLevel = None


    def _deserialize(self, params):
        self.DisturbLevel = params.get("DisturbLevel")
        self.HouseAgentLevel = params.get("HouseAgentLevel")
        self.InsuranceLevel = params.get("InsuranceLevel")
        self.SalesLevel = params.get("SalesLevel")
        self.CheatLevel = params.get("CheatLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        