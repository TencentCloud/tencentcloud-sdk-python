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


class CreateWeappQRUrlRequest(AbstractModel):
    """CreateWeappQRUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionKey: 代理角色临时密钥的Token
        :type SessionKey: str
        """
        self.SessionKey = None


    def _deserialize(self, params):
        self.SessionKey = params.get("SessionKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWeappQRUrlResponse(AbstractModel):
    """CreateWeappQRUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 渠道备案小程序二维码
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class DescribeGetAuthInfoRequest(AbstractModel):
    """DescribeGetAuthInfo请求参数结构体

    """


class DescribeGetAuthInfoResponse(AbstractModel):
    """DescribeGetAuthInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsTenPayMasked: 实名认证状态：0未实名，1已实名
        :type IsTenPayMasked: str
        :param IsAuthenticated: 实名认证类型：0个人，1企业
        :type IsAuthenticated: str
        :param Type: 认证类型，个人0，企业1
        :type Type: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsTenPayMasked = None
        self.IsAuthenticated = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsTenPayMasked = params.get("IsTenPayMasked")
        self.IsAuthenticated = params.get("IsAuthenticated")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class SyncIcpOrderWebInfoRequest(AbstractModel):
    """SyncIcpOrderWebInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param IcpOrderId: 备案ICP订单号
        :type IcpOrderId: str
        :param SourceWebId: 订单里的webId
        :type SourceWebId: str
        :param TargetWebIds: 订单里的webId 数组(如果传入的webIds含有 订单中不包含的webId，会自动跳过)
        :type TargetWebIds: list of str
        :param SyncFields: 网站信息字段名 数组
        :type SyncFields: list of str
        :param CheckSamePerson: 是否先判断同步的网站负责人是否一致 (这里会判断 sitePersonName, sitePersonCerType,sitePersonCerNum三个字段完全一致)  默认:true. 非必要 不建议关闭修改该参数默认值
        :type CheckSamePerson: bool
        """
        self.IcpOrderId = None
        self.SourceWebId = None
        self.TargetWebIds = None
        self.SyncFields = None
        self.CheckSamePerson = None


    def _deserialize(self, params):
        self.IcpOrderId = params.get("IcpOrderId")
        self.SourceWebId = params.get("SourceWebId")
        self.TargetWebIds = params.get("TargetWebIds")
        self.SyncFields = params.get("SyncFields")
        self.CheckSamePerson = params.get("CheckSamePerson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncIcpOrderWebInfoResponse(AbstractModel):
    """SyncIcpOrderWebInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")