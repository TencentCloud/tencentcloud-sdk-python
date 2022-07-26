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


class CreateCRBlockRequest(AbstractModel):
    """CreateCRBlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 已存证的作品ID
        :type WorkId: int
        :param TortUrl: 侵权链接
        :type TortUrl: str
        :param TortTitle: 侵权标题
        :type TortTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param BlockUrl: 拦截结果回调地址
        :type BlockUrl: str
        :param FileUrl: x
        :type FileUrl: str
        :param ValidStartDate: x
        :type ValidStartDate: str
        :param ValidEndDate: x
        :type ValidEndDate: str
        :param TortPic: xx
        :type TortPic: str
        :param CommFileUrl: x
        :type CommFileUrl: str
        :param CommValidStartDate: x
        :type CommValidStartDate: str
        :param CommValidEndDate: x
        :type CommValidEndDate: str
        :param IsProducer: x
        :type IsProducer: str
        """
        self.WorkId = None
        self.TortUrl = None
        self.TortTitle = None
        self.TortPlat = None
        self.BlockUrl = None
        self.FileUrl = None
        self.ValidStartDate = None
        self.ValidEndDate = None
        self.TortPic = None
        self.CommFileUrl = None
        self.CommValidStartDate = None
        self.CommValidEndDate = None
        self.IsProducer = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.TortUrl = params.get("TortUrl")
        self.TortTitle = params.get("TortTitle")
        self.TortPlat = params.get("TortPlat")
        self.BlockUrl = params.get("BlockUrl")
        self.FileUrl = params.get("FileUrl")
        self.ValidStartDate = params.get("ValidStartDate")
        self.ValidEndDate = params.get("ValidEndDate")
        self.TortPic = params.get("TortPic")
        self.CommFileUrl = params.get("CommFileUrl")
        self.CommValidStartDate = params.get("CommValidStartDate")
        self.CommValidEndDate = params.get("CommValidEndDate")
        self.IsProducer = params.get("IsProducer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRBlockResponse(AbstractModel):
    """CreateCRBlock返回参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param TortNum: xxx
        :type TortNum: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TortId = None
        self.TortNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.TortNum = params.get("TortNum")
        self.RequestId = params.get("RequestId")


class CreateCRCompanyVerifyRequest(AbstractModel):
    """CreateCRCompanyVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyName: 企业名称
        :type CompanyName: str
        :param CompanyID: 企业证件号码
        :type CompanyID: str
        :param CompanyLegalName: 企业法人姓名
        :type CompanyLegalName: str
        :param ManagerName: 管理员名称
        :type ManagerName: str
        :param ManagerPhone: 管理员手机号
        :type ManagerPhone: str
        :param VerificationCode: 手机验证码
        :type VerificationCode: str
        :param CompanyIDType: 企业认证号码类型 1：社会信用代码 2：组织机构代码 3：企业工商注册码 4：其他 默认为1
        :type CompanyIDType: str
        :param Type: xxx
        :type Type: str
        """
        self.CompanyName = None
        self.CompanyID = None
        self.CompanyLegalName = None
        self.ManagerName = None
        self.ManagerPhone = None
        self.VerificationCode = None
        self.CompanyIDType = None
        self.Type = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.CompanyID = params.get("CompanyID")
        self.CompanyLegalName = params.get("CompanyLegalName")
        self.ManagerName = params.get("ManagerName")
        self.ManagerPhone = params.get("ManagerPhone")
        self.VerificationCode = params.get("VerificationCode")
        self.CompanyIDType = params.get("CompanyIDType")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRCompanyVerifyResponse(AbstractModel):
    """CreateCRCompanyVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 认证状态 0-认证成功 1-认证失败
        :type Status: int
        :param Note: 认证结果返回
        :type Note: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Note = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Note = params.get("Note")
        self.RequestId = params.get("RequestId")


class CreateCRRightRequest(AbstractModel):
    """CreateCRRight请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 已存证的作品ID
        :type WorkId: int
        :param TortUrl: 侵权链接
        :type TortUrl: str
        :param TortTitle: 侵权标题
        :type TortTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param RightUrl: 发函结果回调地址
        :type RightUrl: str
        :param FileUrl: x
        :type FileUrl: str
        :param ValidStartDate: x
        :type ValidStartDate: str
        :param ValidEndDate: x
        :type ValidEndDate: str
        :param CommFileUrl: x
        :type CommFileUrl: str
        :param CommValidStartDate: x
        :type CommValidStartDate: str
        :param CommValidEndDate: x
        :type CommValidEndDate: str
        :param HomeFileUrl: x
        :type HomeFileUrl: str
        :param HomeValidStartDate: x
        :type HomeValidStartDate: str
        :param HomeValidEndDate: x
        :type HomeValidEndDate: str
        :param IsProducer: x
        :type IsProducer: str
        """
        self.WorkId = None
        self.TortUrl = None
        self.TortTitle = None
        self.TortPlat = None
        self.RightUrl = None
        self.FileUrl = None
        self.ValidStartDate = None
        self.ValidEndDate = None
        self.CommFileUrl = None
        self.CommValidStartDate = None
        self.CommValidEndDate = None
        self.HomeFileUrl = None
        self.HomeValidStartDate = None
        self.HomeValidEndDate = None
        self.IsProducer = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.TortUrl = params.get("TortUrl")
        self.TortTitle = params.get("TortTitle")
        self.TortPlat = params.get("TortPlat")
        self.RightUrl = params.get("RightUrl")
        self.FileUrl = params.get("FileUrl")
        self.ValidStartDate = params.get("ValidStartDate")
        self.ValidEndDate = params.get("ValidEndDate")
        self.CommFileUrl = params.get("CommFileUrl")
        self.CommValidStartDate = params.get("CommValidStartDate")
        self.CommValidEndDate = params.get("CommValidEndDate")
        self.HomeFileUrl = params.get("HomeFileUrl")
        self.HomeValidStartDate = params.get("HomeValidStartDate")
        self.HomeValidEndDate = params.get("HomeValidEndDate")
        self.IsProducer = params.get("IsProducer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRRightResponse(AbstractModel):
    """CreateCRRight返回参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param TortNum: xxx
        :type TortNum: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TortId = None
        self.TortNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.TortNum = params.get("TortNum")
        self.RequestId = params.get("RequestId")


class DescribeCRWorkInfoRequest(AbstractModel):
    """DescribeCRWorkInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: xxx
        :type WorkId: int
        """
        self.WorkId = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRWorkInfoResponse(AbstractModel):
    """DescribeCRWorkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkName: x
        :type WorkName: str
        :param MonitorStatus: x
        :type MonitorStatus: int
        :param AuthStatus: x
        :type AuthStatus: int
        :param CommStatus: x
        :type CommStatus: int
        :param IsProducer: x
        :type IsProducer: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkName = None
        self.MonitorStatus = None
        self.AuthStatus = None
        self.CommStatus = None
        self.IsProducer = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkName = params.get("WorkName")
        self.MonitorStatus = params.get("MonitorStatus")
        self.AuthStatus = params.get("AuthStatus")
        self.CommStatus = params.get("CommStatus")
        self.IsProducer = params.get("IsProducer")
        self.RequestId = params.get("RequestId")