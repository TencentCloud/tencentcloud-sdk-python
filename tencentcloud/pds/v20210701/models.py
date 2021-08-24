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
        :param ServiceParams: 用户信息
        :type ServiceParams: :class:`tencentcloud.pds.v20210701.models.UserInfos`
        """
        self.ServiceParams = None


    def _deserialize(self, params):
        if params.get("ServiceParams") is not None:
            self.ServiceParams = UserInfos()
            self.ServiceParams._deserialize(params.get("ServiceParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewUserAcquisitionResponse(AbstractModel):
    """DescribeNewUserAcquisition返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceRsp: 用户信誉分，1-5从低到高
        :type ServiceRsp: :class:`tencentcloud.pds.v20210701.models.Score`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceRsp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceRsp") is not None:
            self.ServiceRsp = Score()
            self.ServiceRsp._deserialize(params.get("ServiceRsp"))
        self.RequestId = params.get("RequestId")


class DescribeStockEstimationRequest(AbstractModel):
    """DescribeStockEstimation请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceParams: 用户信息
        :type ServiceParams: :class:`tencentcloud.pds.v20210701.models.UserInfos`
        """
        self.ServiceParams = None


    def _deserialize(self, params):
        if params.get("ServiceParams") is not None:
            self.ServiceParams = UserInfos()
            self.ServiceParams._deserialize(params.get("ServiceParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStockEstimationResponse(AbstractModel):
    """DescribeStockEstimation返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceRsp: 用户信誉分，1-5从低到高
        :type ServiceRsp: :class:`tencentcloud.pds.v20210701.models.Score`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceRsp = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceRsp") is not None:
            self.ServiceRsp = Score()
            self.ServiceRsp._deserialize(params.get("ServiceRsp"))
        self.RequestId = params.get("RequestId")


class Score(AbstractModel):
    """信誉分，1-5从低到高

    """

    def __init__(self):
        r"""
        :param Star: 信誉分，1-5从低到高
        :type Star: int
        """
        self.Star = None


    def _deserialize(self, params):
        self.Star = params.get("Star")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfos(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param PhoneNum: 用户的手机号
        :type PhoneNum: str
        :param Openid: 用户的微信OpenID
        :type Openid: str
        :param IP: 用户移动设备的客户端IP
        :type IP: str
        :param WiFiBssid: 用户WiFi的BSSID
        :type WiFiBssid: str
        :param IMEI: 用户Android设备的IMEI
        :type IMEI: str
        :param OAID: 用户Android设备的OAID
        :type OAID: str
        :param IDFA: 用户iOS设备的IDFA
        :type IDFA: str
        """
        self.PhoneNum = None
        self.Openid = None
        self.IP = None
        self.WiFiBssid = None
        self.IMEI = None
        self.OAID = None
        self.IDFA = None


    def _deserialize(self, params):
        self.PhoneNum = params.get("PhoneNum")
        self.Openid = params.get("Openid")
        self.IP = params.get("IP")
        self.WiFiBssid = params.get("WiFiBssid")
        self.IMEI = params.get("IMEI")
        self.OAID = params.get("OAID")
        self.IDFA = params.get("IDFA")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        