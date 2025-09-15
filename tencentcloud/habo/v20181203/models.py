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


class DescribeStatusRequest(AbstractModel):
    r"""DescribeStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Pk: 购买服务后获得的授权帐号，用于保证请求有效性
        :type Pk: str
        :param _Md5: 需要获取分析结果的样本md5
        :type Md5: str
        """
        self._Pk = None
        self._Md5 = None

    @property
    def Pk(self):
        r"""购买服务后获得的授权帐号，用于保证请求有效性
        :rtype: str
        """
        return self._Pk

    @Pk.setter
    def Pk(self, Pk):
        self._Pk = Pk

    @property
    def Md5(self):
        r"""需要获取分析结果的样本md5
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5


    def _deserialize(self, params):
        self._Pk = params.get("Pk")
        self._Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStatusResponse(AbstractModel):
    r"""DescribeStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 接口调用状态，1表示成功，非1表示失败
        :type Status: int
        :param _Info: 成功时返回success，失败时返回具体的失败原因，如样本分析未完成
        :type Info: str
        :param _Data: 成功时返回样本日志下载地址，该地址10分钟内有效
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._Data = None
        self._RequestId = None

    @property
    def Status(self):
        r"""接口调用状态，1表示成功，非1表示失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        r"""成功时返回success，失败时返回具体的失败原因，如样本分析未完成
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Data(self):
        r"""成功时返回样本日志下载地址，该地址10分钟内有效
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class StartAnalyseRequest(AbstractModel):
    r"""StartAnalyse请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Pk: 购买服务后获得的授权帐号，用于保证请求有效性
        :type Pk: str
        :param _Md5: 样本md5，用于对下载获得的样本完整性进行校验
        :type Md5: str
        :param _DlUrl: 待分析样本下载地址
        :type DlUrl: str
        """
        self._Pk = None
        self._Md5 = None
        self._DlUrl = None

    @property
    def Pk(self):
        r"""购买服务后获得的授权帐号，用于保证请求有效性
        :rtype: str
        """
        return self._Pk

    @Pk.setter
    def Pk(self, Pk):
        self._Pk = Pk

    @property
    def Md5(self):
        r"""样本md5，用于对下载获得的样本完整性进行校验
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def DlUrl(self):
        r"""待分析样本下载地址
        :rtype: str
        """
        return self._DlUrl

    @DlUrl.setter
    def DlUrl(self, DlUrl):
        self._DlUrl = DlUrl


    def _deserialize(self, params):
        self._Pk = params.get("Pk")
        self._Md5 = params.get("Md5")
        self._DlUrl = params.get("DlUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAnalyseResponse(AbstractModel):
    r"""StartAnalyse返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 接口调用状态，1表示成功，非1表示失败
        :type Status: int
        :param _Info: 成功时返回success，失败时返回具体的失败原因
        :type Info: str
        :param _Data: 保留字段
        :type Data: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Info = None
        self._Data = None
        self._RequestId = None

    @property
    def Status(self):
        r"""接口调用状态，1表示成功，非1表示失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Info(self):
        r"""成功时返回success，失败时返回具体的失败原因
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Data(self):
        r"""保留字段
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Info = params.get("Info")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")