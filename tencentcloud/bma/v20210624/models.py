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
        :param CompanyIDType: 企业认证号码类型 1：社会信用代码 2：组织机构代码 3：企业工商注册码 4：其他 默认为1
        :type CompanyIDType: str
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
        :param Type: xxx
        :type Type: str
        """
        self.CompanyName = None
        self.CompanyIDType = None
        self.CompanyID = None
        self.CompanyLegalName = None
        self.ManagerName = None
        self.ManagerPhone = None
        self.VerificationCode = None
        self.Type = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.CompanyIDType = params.get("CompanyIDType")
        self.CompanyID = params.get("CompanyID")
        self.CompanyLegalName = params.get("CompanyLegalName")
        self.ManagerName = params.get("ManagerName")
        self.ManagerPhone = params.get("ManagerPhone")
        self.VerificationCode = params.get("VerificationCode")
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


class CreateCRWorkRequest(AbstractModel):
    """CreateCRWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkName: 作品名称
        :type WorkName: str
        :param WorkCategory: 作品分类
        :type WorkCategory: str
        :param WorkType: 作品内容类型
        :type WorkType: str
        :param WorkSign: 作品标签
        :type WorkSign: str
        :param WorkPic: 作品图片
        :type WorkPic: str
        :param WorkDesc: 创作描述
        :type WorkDesc: str
        :param IsOriginal: 是否原创 0:否 1:是
        :type IsOriginal: str
        :param IsRelease: 是否发布 0：未发布 1：已发布
        :type IsRelease: str
        :param ProducerID: 著作权人ID
        :type ProducerID: int
        :param ProduceTime: 创作时间
        :type ProduceTime: str
        :param SampleContentURL: 样品文件路径
        :type SampleContentURL: str
        :param SampleDownloadURL: 样本下载Url
        :type SampleDownloadURL: str
        :param GrantType: 授予类型
        :type GrantType: str
        :param SamplePublicURL: 作品发布Url
        :type SamplePublicURL: str
        :param IsMonitor: 是否启用监测 0：不启用 1：启用 默认为0
        :type IsMonitor: str
        :param IsCert: 是否启用存证0：不启用 1：启用 默认为1
        :type IsCert: str
        :param CertUrl: 存证回调地址
        :type CertUrl: str
        :param MonitorUrl: 监测回调地址
        :type MonitorUrl: str
        :param ProduceType: 创作性质（原创,改编,翻译,汇编,注释,整理,其他)
        :type ProduceType: str
        :param WhiteLists: xxx
        :type WhiteLists: list of str
        :param WorkId: x
        :type WorkId: int
        :param ProducerName: xx
        :type ProducerName: str
        :param Nickname: xx
        :type Nickname: str
        :param Authorization: x
        :type Authorization: str
        :param AuthorizationStartTime: x
        :type AuthorizationStartTime: str
        :param AuthorizationEndTime: x
        :type AuthorizationEndTime: str
        :param ContentType: x
        :type ContentType: str
        :param Content: x
        :type Content: str
        """
        self.WorkName = None
        self.WorkCategory = None
        self.WorkType = None
        self.WorkSign = None
        self.WorkPic = None
        self.WorkDesc = None
        self.IsOriginal = None
        self.IsRelease = None
        self.ProducerID = None
        self.ProduceTime = None
        self.SampleContentURL = None
        self.SampleDownloadURL = None
        self.GrantType = None
        self.SamplePublicURL = None
        self.IsMonitor = None
        self.IsCert = None
        self.CertUrl = None
        self.MonitorUrl = None
        self.ProduceType = None
        self.WhiteLists = None
        self.WorkId = None
        self.ProducerName = None
        self.Nickname = None
        self.Authorization = None
        self.AuthorizationStartTime = None
        self.AuthorizationEndTime = None
        self.ContentType = None
        self.Content = None


    def _deserialize(self, params):
        self.WorkName = params.get("WorkName")
        self.WorkCategory = params.get("WorkCategory")
        self.WorkType = params.get("WorkType")
        self.WorkSign = params.get("WorkSign")
        self.WorkPic = params.get("WorkPic")
        self.WorkDesc = params.get("WorkDesc")
        self.IsOriginal = params.get("IsOriginal")
        self.IsRelease = params.get("IsRelease")
        self.ProducerID = params.get("ProducerID")
        self.ProduceTime = params.get("ProduceTime")
        self.SampleContentURL = params.get("SampleContentURL")
        self.SampleDownloadURL = params.get("SampleDownloadURL")
        self.GrantType = params.get("GrantType")
        self.SamplePublicURL = params.get("SamplePublicURL")
        self.IsMonitor = params.get("IsMonitor")
        self.IsCert = params.get("IsCert")
        self.CertUrl = params.get("CertUrl")
        self.MonitorUrl = params.get("MonitorUrl")
        self.ProduceType = params.get("ProduceType")
        self.WhiteLists = params.get("WhiteLists")
        self.WorkId = params.get("WorkId")
        self.ProducerName = params.get("ProducerName")
        self.Nickname = params.get("Nickname")
        self.Authorization = params.get("Authorization")
        self.AuthorizationStartTime = params.get("AuthorizationStartTime")
        self.AuthorizationEndTime = params.get("AuthorizationEndTime")
        self.ContentType = params.get("ContentType")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCRWorkResponse(AbstractModel):
    """CreateCRWork返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param EvidenceId: x
        :type EvidenceId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")


class DescribeCRMonitorDetailRequest(AbstractModel):
    """DescribeCRMonitorDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param PageSize: 页数
        :type PageSize: int
        :param PageNumber: 页码
        :type PageNumber: int
        :param Filters: x
        :type Filters: list of Filter
        """
        self.WorkId = None
        self.PageSize = None
        self.PageNumber = None
        self.Filters = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRMonitorDetailResponse(AbstractModel):
    """DescribeCRMonitorDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Torts: MonitorTort数组
        :type Torts: list of MonitorTort
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param MonitorStatus: x
        :type MonitorStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Torts = None
        self.TotalCount = None
        self.MonitorStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Torts") is not None:
            self.Torts = []
            for item in params.get("Torts"):
                obj = MonitorTort()
                obj._deserialize(item)
                self.Torts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.MonitorStatus = params.get("MonitorStatus")
        self.RequestId = params.get("RequestId")


class DescribeCRMonitorsRequest(AbstractModel):
    """DescribeCRMonitors请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param PageSize: 页数
        :type PageSize: int
        :param PageNumber: 页码
        :type PageNumber: int
        """
        self.Filters = None
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCRMonitorsResponse(AbstractModel):
    """DescribeCRMonitors返回参数结构体

    """

    def __init__(self):
        r"""
        :param Monitors: 监测结果
        :type Monitors: list of Monitor
        :param TotalCount: 记录总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Monitors = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Monitors") is not None:
            self.Monitors = []
            for item in params.get("Monitors"):
                obj = Monitor()
                obj._deserialize(item)
                self.Monitors.append(obj)
        self.TotalCount = params.get("TotalCount")
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


class Filter(AbstractModel):
    """过滤参数

    """


class ModifyCRBlockStatusRequest(AbstractModel):
    """ModifyCRBlockStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param BlockUrl: 拦截结果回调地址
        :type BlockUrl: str
        """
        self.TortId = None
        self.BlockUrl = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.BlockUrl = params.get("BlockUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRBlockStatusResponse(AbstractModel):
    """ModifyCRBlockStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRMonitorRequest(AbstractModel):
    """ModifyCRMonitor请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param MonitorStatus: 监测状态 1-开启监测 2-关闭监测 默认为1
        :type MonitorStatus: str
        """
        self.WorkId = None
        self.MonitorStatus = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.MonitorStatus = params.get("MonitorStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRMonitorResponse(AbstractModel):
    """ModifyCRMonitor返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRObtainStatusRequest(AbstractModel):
    """ModifyCRObtainStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: xxx
        :type TortId: int
        :param ObtainType: xxx
        :type ObtainType: int
        :param ObtainDuration: xxx
        :type ObtainDuration: int
        :param ObtainUrl: xxx
        :type ObtainUrl: str
        """
        self.TortId = None
        self.ObtainType = None
        self.ObtainDuration = None
        self.ObtainUrl = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.ObtainType = params.get("ObtainType")
        self.ObtainDuration = params.get("ObtainDuration")
        self.ObtainUrl = params.get("ObtainUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRObtainStatusResponse(AbstractModel):
    """ModifyCRObtainStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCRRightStatusRequest(AbstractModel):
    """ModifyCRRightStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TortId: 侵权ID
        :type TortId: int
        :param RightUrl: 发函结果回调地址
        :type RightUrl: str
        """
        self.TortId = None
        self.RightUrl = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.RightUrl = params.get("RightUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCRRightStatusResponse(AbstractModel):
    """ModifyCRRightStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Monitor(AbstractModel):
    """版权保护-监测结果

    """

    def __init__(self):
        r"""
        :param WorkId: 作品ID
        :type WorkId: int
        :param WorkName: 作品名称
        :type WorkName: str
        :param WorkType: 作品内容类型 01-视频 02-音频 03-文本 04-图片
        :type WorkType: str
        :param TortPlatNum: 侵权平台数量
        :type TortPlatNum: int
        :param TortURLNum: 侵权链接数量
        :type TortURLNum: int
        :param MonitorTime: 监测时间
        :type MonitorTime: str
        :param MonitorStatus: 0-待监测 1-监测中 2-不监测 3-暂停监测
        :type MonitorStatus: int
        :param WorkCategory: 作品类型
        :type WorkCategory: str
        :param InsertTime: xx
        :type InsertTime: str
        :param MonitorNote: xx
        :type MonitorNote: str
        """
        self.WorkId = None
        self.WorkName = None
        self.WorkType = None
        self.TortPlatNum = None
        self.TortURLNum = None
        self.MonitorTime = None
        self.MonitorStatus = None
        self.WorkCategory = None
        self.InsertTime = None
        self.MonitorNote = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.WorkName = params.get("WorkName")
        self.WorkType = params.get("WorkType")
        self.TortPlatNum = params.get("TortPlatNum")
        self.TortURLNum = params.get("TortURLNum")
        self.MonitorTime = params.get("MonitorTime")
        self.MonitorStatus = params.get("MonitorStatus")
        self.WorkCategory = params.get("WorkCategory")
        self.InsertTime = params.get("InsertTime")
        self.MonitorNote = params.get("MonitorNote")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorTort(AbstractModel):
    """监测侵权信息详情

    """

    def __init__(self):
        r"""
        :param TortId: 侵权信息ID
        :type TortId: int
        :param TortTitle: 侵权标题
        :type TortTitle: str
        :param TortPlat: 侵权平台
        :type TortPlat: str
        :param TortURL: 侵权链接
        :type TortURL: str
        :param PubTime: 侵权链接发布时间
        :type PubTime: str
        :param Author: 作者
        :type Author: str
        :param DetectTime: xxx
        :type DetectTime: str
        :param ObtainStatus: 1
        :type ObtainStatus: int
        :param RightStatus: 1
        :type RightStatus: int
        :param BlockStatus: 1
        :type BlockStatus: int
        :param TortNum: 1
        :type TortNum: str
        :param ObtainNote: 1
        :type ObtainNote: str
        :param WorkTitle: 1
        :type WorkTitle: str
        """
        self.TortId = None
        self.TortTitle = None
        self.TortPlat = None
        self.TortURL = None
        self.PubTime = None
        self.Author = None
        self.DetectTime = None
        self.ObtainStatus = None
        self.RightStatus = None
        self.BlockStatus = None
        self.TortNum = None
        self.ObtainNote = None
        self.WorkTitle = None


    def _deserialize(self, params):
        self.TortId = params.get("TortId")
        self.TortTitle = params.get("TortTitle")
        self.TortPlat = params.get("TortPlat")
        self.TortURL = params.get("TortURL")
        self.PubTime = params.get("PubTime")
        self.Author = params.get("Author")
        self.DetectTime = params.get("DetectTime")
        self.ObtainStatus = params.get("ObtainStatus")
        self.RightStatus = params.get("RightStatus")
        self.BlockStatus = params.get("BlockStatus")
        self.TortNum = params.get("TortNum")
        self.ObtainNote = params.get("ObtainNote")
        self.WorkTitle = params.get("WorkTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCRWorkRequest(AbstractModel):
    """UpdateCRWork请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: xx
        :type WorkId: int
        :param ContentType: xx
        :type ContentType: str
        :param Content: xx
        :type Content: str
        :param CertType: xx
        :type CertType: str
        """
        self.WorkId = None
        self.ContentType = None
        self.Content = None
        self.CertType = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.ContentType = params.get("ContentType")
        self.Content = params.get("Content")
        self.CertType = params.get("CertType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCRWorkResponse(AbstractModel):
    """UpdateCRWork返回参数结构体

    """

    def __init__(self):
        r"""
        :param WorkId: xx
        :type WorkId: int
        :param EvidenceId: xx
        :type EvidenceId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WorkId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkId = params.get("WorkId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")