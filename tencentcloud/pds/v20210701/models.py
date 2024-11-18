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


class DescribeNewUserAcquisitionRequest(AbstractModel):
    """DescribeNewUserAcquisition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceParams: 用户信息
        :type ServiceParams: :class:`tencentcloud.pds.v20210701.models.UserInfos`
        """
        self._ServiceParams = None

    @property
    def ServiceParams(self):
        """用户信息
        :rtype: :class:`tencentcloud.pds.v20210701.models.UserInfos`
        """
        return self._ServiceParams

    @ServiceParams.setter
    def ServiceParams(self, ServiceParams):
        self._ServiceParams = ServiceParams


    def _deserialize(self, params):
        if params.get("ServiceParams") is not None:
            self._ServiceParams = UserInfos()
            self._ServiceParams._deserialize(params.get("ServiceParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewUserAcquisitionResponse(AbstractModel):
    """DescribeNewUserAcquisition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceRsp: 用户信誉分，1-5从低到高
        :type ServiceRsp: :class:`tencentcloud.pds.v20210701.models.Score`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceRsp = None
        self._RequestId = None

    @property
    def ServiceRsp(self):
        """用户信誉分，1-5从低到高
        :rtype: :class:`tencentcloud.pds.v20210701.models.Score`
        """
        return self._ServiceRsp

    @ServiceRsp.setter
    def ServiceRsp(self, ServiceRsp):
        self._ServiceRsp = ServiceRsp

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceRsp") is not None:
            self._ServiceRsp = Score()
            self._ServiceRsp._deserialize(params.get("ServiceRsp"))
        self._RequestId = params.get("RequestId")


class DescribeStockEstimationRequest(AbstractModel):
    """DescribeStockEstimation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceParams: 用户信息
        :type ServiceParams: :class:`tencentcloud.pds.v20210701.models.UserInfos`
        """
        self._ServiceParams = None

    @property
    def ServiceParams(self):
        """用户信息
        :rtype: :class:`tencentcloud.pds.v20210701.models.UserInfos`
        """
        return self._ServiceParams

    @ServiceParams.setter
    def ServiceParams(self, ServiceParams):
        self._ServiceParams = ServiceParams


    def _deserialize(self, params):
        if params.get("ServiceParams") is not None:
            self._ServiceParams = UserInfos()
            self._ServiceParams._deserialize(params.get("ServiceParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStockEstimationResponse(AbstractModel):
    """DescribeStockEstimation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceRsp: 用户信誉分，1-5从低到高
        :type ServiceRsp: :class:`tencentcloud.pds.v20210701.models.Score`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceRsp = None
        self._RequestId = None

    @property
    def ServiceRsp(self):
        """用户信誉分，1-5从低到高
        :rtype: :class:`tencentcloud.pds.v20210701.models.Score`
        """
        return self._ServiceRsp

    @ServiceRsp.setter
    def ServiceRsp(self, ServiceRsp):
        self._ServiceRsp = ServiceRsp

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceRsp") is not None:
            self._ServiceRsp = Score()
            self._ServiceRsp._deserialize(params.get("ServiceRsp"))
        self._RequestId = params.get("RequestId")


class Score(AbstractModel):
    """信誉分，1-5从低到高

    """

    def __init__(self):
        r"""
        :param _Star: 信誉分，1-5从低到高
        :type Star: int
        """
        self._Star = None

    @property
    def Star(self):
        """信誉分，1-5从低到高
        :rtype: int
        """
        return self._Star

    @Star.setter
    def Star(self, Star):
        self._Star = Star


    def _deserialize(self, params):
        self._Star = params.get("Star")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfos(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _PhoneNum: 用户的手机号
        :type PhoneNum: str
        :param _Openid: 用户的微信OpenID
        :type Openid: str
        :param _IP: 用户移动设备的客户端IP
        :type IP: str
        :param _WiFiBssid: 用户WiFi的BSSID
        :type WiFiBssid: str
        :param _IMEI: 用户Android设备的IMEI
        :type IMEI: str
        :param _OAID: 用户Android设备的OAID
        :type OAID: str
        :param _IDFA: 用户iOS设备的IDFA
        :type IDFA: str
        """
        self._PhoneNum = None
        self._Openid = None
        self._IP = None
        self._WiFiBssid = None
        self._IMEI = None
        self._OAID = None
        self._IDFA = None

    @property
    def PhoneNum(self):
        """用户的手机号
        :rtype: str
        """
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def Openid(self):
        """用户的微信OpenID
        :rtype: str
        """
        return self._Openid

    @Openid.setter
    def Openid(self, Openid):
        self._Openid = Openid

    @property
    def IP(self):
        """用户移动设备的客户端IP
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def WiFiBssid(self):
        """用户WiFi的BSSID
        :rtype: str
        """
        return self._WiFiBssid

    @WiFiBssid.setter
    def WiFiBssid(self, WiFiBssid):
        self._WiFiBssid = WiFiBssid

    @property
    def IMEI(self):
        """用户Android设备的IMEI
        :rtype: str
        """
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI

    @property
    def OAID(self):
        """用户Android设备的OAID
        :rtype: str
        """
        return self._OAID

    @OAID.setter
    def OAID(self, OAID):
        self._OAID = OAID

    @property
    def IDFA(self):
        """用户iOS设备的IDFA
        :rtype: str
        """
        return self._IDFA

    @IDFA.setter
    def IDFA(self, IDFA):
        self._IDFA = IDFA


    def _deserialize(self, params):
        self._PhoneNum = params.get("PhoneNum")
        self._Openid = params.get("Openid")
        self._IP = params.get("IP")
        self._WiFiBssid = params.get("WiFiBssid")
        self._IMEI = params.get("IMEI")
        self._OAID = params.get("OAID")
        self._IDFA = params.get("IDFA")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        