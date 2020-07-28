# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AuthDomain(AbstractModel):
    """合法域名

    """

    def __init__(self):
        """
        :param Id: 域名ID
        :type Id: str
        :param Domain: 域名
        :type Domain: str
        :param Type: 域名类型。包含以下取值：
<li>SYSTEM</li>
<li>USER</li>
        :type Type: str
        :param Status: 状态。包含以下取值：
<li>ENABLE</li>
<li>DISABLE</li>
        :type Status: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.Domain = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class CheckTcbServiceRequest(AbstractModel):
    """CheckTcbService请求参数结构体

    """


class CheckTcbServiceResponse(AbstractModel):
    """CheckTcbService返回参数结构体

    """

    def __init__(self):
        """
        :param Initialized: true表示已开通
        :type Initialized: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Initialized = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Initialized = params.get("Initialized")
        self.RequestId = params.get("RequestId")


class CommonServiceAPIRequest(AbstractModel):
    """CommonServiceAPI请求参数结构体

    """

    def __init__(self):
        """
        :param Service: Service名，需要转发访问的接口名
        :type Service: str
        :param JSONData: 需要转发的云API参数，要转成JSON格式
        :type JSONData: str
        """
        self.Service = None
        self.JSONData = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.JSONData = params.get("JSONData")


class CommonServiceAPIResponse(AbstractModel):
    """CommonServiceAPI返回参数结构体

    """

    def __init__(self):
        """
        :param JSONResp: json格式response
        :type JSONResp: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JSONResp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JSONResp = params.get("JSONResp")
        self.RequestId = params.get("RequestId")


class CreateAuthDomainRequest(AbstractModel):
    """CreateAuthDomain请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param Domains: 安全域名
        :type Domains: list of str
        """
        self.EnvId = None
        self.Domains = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domains = params.get("Domains")


class CreateAuthDomainResponse(AbstractModel):
    """CreateAuthDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateHostingDomainRequest(AbstractModel):
    """CreateHostingDomain请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param Domain: 域名
        :type Domain: str
        :param CertId: 证书ID
        :type CertId: str
        """
        self.EnvId = None
        self.Domain = None
        self.CertId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")


class CreateHostingDomainResponse(AbstractModel):
    """CreateHostingDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePostpayPackageRequest(AbstractModel):
    """CreatePostpayPackage请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param WxAppId: 微信 AppId，微信必传
        :type WxAppId: str
        :param Source: 付费来源
<li>miniapp</li>
<li>qcloud</li>
        :type Source: str
        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
        :type FreeQuota: str
        :param Alias: 环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        :param EnvSource: 环境创建来源，取值：
<li>miniapp</li>
<li>qcloud</li>
用法同CreateEnv接口的Source参数
和 Channel 参数同时传，或者同时不传；EnvId 为空时必传。
        :type EnvSource: str
        :param Channel: 如果envsource为miniapp, channel可以为ide或api;
如果envsource为qcloud, channel可以为qc_console,cocos, qq, cloudgame,dcloud
和 EnvSource 参数同时传，或者同时不传；EnvId 为空时必传。
        :type Channel: str
        :param ExtensionId: 扩展ID
        :type ExtensionId: str
        """
        self.EnvId = None
        self.WxAppId = None
        self.Source = None
        self.FreeQuota = None
        self.Alias = None
        self.EnvSource = None
        self.Channel = None
        self.ExtensionId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.WxAppId = params.get("WxAppId")
        self.Source = params.get("Source")
        self.FreeQuota = params.get("FreeQuota")
        self.Alias = params.get("Alias")
        self.EnvSource = params.get("EnvSource")
        self.Channel = params.get("Channel")
        self.ExtensionId = params.get("ExtensionId")


class CreatePostpayPackageResponse(AbstractModel):
    """CreatePostpayPackage返回参数结构体

    """

    def __init__(self):
        """
        :param TranId: 后付费订单号
        :type TranId: str
        :param EnvId: 环境ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateStaticStoreRequest(AbstractModel):
    """CreateStaticStore请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class CreateStaticStoreResponse(AbstractModel):
    """CreateStaticStore返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建静态资源结果(succ/fail)
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DatabasesInfo(AbstractModel):
    """数据库资源信息

    """

    def __init__(self):
        """
        :param InstanceId: 数据库唯一标识
        :type InstanceId: str
        :param Status: 状态。包含以下取值：
<li>INITIALIZING：资源初始化中</li>
<li>RUNNING：运行中，可正常使用的状态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：资源过期</li>
        :type Status: str
        :param Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        """
        self.InstanceId = None
        self.Status = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.Region = params.get("Region")


class DeleteEndUserRequest(AbstractModel):
    """DeleteEndUser请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param UserList: 用户列表，每一项都是uuid
        :type UserList: list of str
        """
        self.EnvId = None
        self.UserList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UserList = params.get("UserList")


class DeleteEndUserResponse(AbstractModel):
    """DeleteEndUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuthDomainsRequest(AbstractModel):
    """DescribeAuthDomains请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeAuthDomainsResponse(AbstractModel):
    """DescribeAuthDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 安全域名列表列表
        :type Domains: list of AuthDomain
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = AuthDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabaseACLRequest(AbstractModel):
    """DescribeDatabaseACL请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param CollectionName: 集合名称
        :type CollectionName: str
        """
        self.EnvId = None
        self.CollectionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")


class DescribeDatabaseACLResponse(AbstractModel):
    """DescribeDatabaseACL返回参数结构体

    """

    def __init__(self):
        """
        :param AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :type AclTag: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AclTag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AclTag = params.get("AclTag")
        self.RequestId = params.get("RequestId")


class DescribeEndUserLoginStatisticRequest(AbstractModel):
    """DescribeEndUserLoginStatistic请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        :param Source: 终端用户来源
<li> qcloud </li>
<li>miniapp</li>
        :type Source: str
        """
        self.EnvId = None
        self.Source = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")


class DescribeEndUserLoginStatisticResponse(AbstractModel):
    """DescribeEndUserLoginStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param LoginStatistics: 环境终端用户新增与登录统计
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginStatistics: list of LoginStatistic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LoginStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginStatistics") is not None:
            self.LoginStatistics = []
            for item in params.get("LoginStatistics"):
                obj = LoginStatistic()
                obj._deserialize(item)
                self.LoginStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEndUserStatisticRequest(AbstractModel):
    """DescribeEndUserStatistic请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境id
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeEndUserStatisticResponse(AbstractModel):
    """DescribeEndUserStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param PlatformStatistics: 终端用户各平台统计
注意：此字段可能返回 null，表示取不到有效值。
        :type PlatformStatistics: list of PlatformStatistic
        :param TotalCount: 终端用户总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlatformStatistics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlatformStatistics") is not None:
            self.PlatformStatistics = []
            for item in params.get("PlatformStatistics"):
                obj = PlatformStatistic()
                obj._deserialize(item)
                self.PlatformStatistics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEndUsersRequest(AbstractModel):
    """DescribeEndUsers请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 开发者的环境ID
        :type EnvId: str
        :param Offset: 可选参数，偏移量，默认 0
        :type Offset: int
        :param Limit: 可选参数，拉取数量，默认 20
        :type Limit: int
        :param UUIds: 按照 uuid 列表过滤，最大个数为100
        :type UUIds: list of str
        """
        self.EnvId = None
        self.Offset = None
        self.Limit = None
        self.UUIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UUIds = params.get("UUIds")


class DescribeEndUsersResponse(AbstractModel):
    """DescribeEndUsers返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 用户总数
        :type Total: int
        :param Users: 用户列表
        :type Users: list of EndUserInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = EndUserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvFreeQuotaRequest(AbstractModel):
    """DescribeEnvFreeQuota请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param ResourceTypes: 资源类型：可选值：CDN, COS, FLEXDB, HOSTING, SCF
不传则返回全部资源指标
        :type ResourceTypes: list of str
        """
        self.EnvId = None
        self.ResourceTypes = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ResourceTypes = params.get("ResourceTypes")


class DescribeEnvFreeQuotaResponse(AbstractModel):
    """DescribeEnvFreeQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaItems: 免费抵扣配额详情
注意：此字段可能返回 null，表示取不到有效值。
        :type QuotaItems: list of PostpayEnvQuota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaItems") is not None:
            self.QuotaItems = []
            for item in params.get("QuotaItems"):
                obj = PostpayEnvQuota()
                obj._deserialize(item)
                self.QuotaItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvLimitRequest(AbstractModel):
    """DescribeEnvLimit请求参数结构体

    """


class DescribeEnvLimitResponse(AbstractModel):
    """DescribeEnvLimit返回参数结构体

    """

    def __init__(self):
        """
        :param MaxEnvNum: 环境总数上限
        :type MaxEnvNum: int
        :param CurrentEnvNum: 目前环境总数
        :type CurrentEnvNum: int
        :param MaxFreeEnvNum: 免费环境数量上限
        :type MaxFreeEnvNum: int
        :param CurrentFreeEnvNum: 目前免费环境数量
        :type CurrentFreeEnvNum: int
        :param MaxDeleteTotal: 总计允许销毁环境次数上限
        :type MaxDeleteTotal: int
        :param CurrentDeleteTotal: 目前已销毁环境次数
        :type CurrentDeleteTotal: int
        :param MaxDeleteMonthly: 每月允许销毁环境次数上限
        :type MaxDeleteMonthly: int
        :param CurrentDeleteMonthly: 本月已销毁环境次数
        :type CurrentDeleteMonthly: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaxEnvNum = None
        self.CurrentEnvNum = None
        self.MaxFreeEnvNum = None
        self.CurrentFreeEnvNum = None
        self.MaxDeleteTotal = None
        self.CurrentDeleteTotal = None
        self.MaxDeleteMonthly = None
        self.CurrentDeleteMonthly = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxEnvNum = params.get("MaxEnvNum")
        self.CurrentEnvNum = params.get("CurrentEnvNum")
        self.MaxFreeEnvNum = params.get("MaxFreeEnvNum")
        self.CurrentFreeEnvNum = params.get("CurrentFreeEnvNum")
        self.MaxDeleteTotal = params.get("MaxDeleteTotal")
        self.CurrentDeleteTotal = params.get("CurrentDeleteTotal")
        self.MaxDeleteMonthly = params.get("MaxDeleteMonthly")
        self.CurrentDeleteMonthly = params.get("CurrentDeleteMonthly")
        self.RequestId = params.get("RequestId")


class DescribeEnvsRequest(AbstractModel):
    """DescribeEnvs请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID，如果传了这个参数则只返回该环境的相关信息
        :type EnvId: str
        :param IsVisible: 指定Channels字段为可见渠道列表或不可见渠道列表
如只想获取渠道A的环境 就填写IsVisible= true,Channels = ["A"], 过滤渠道A拉取其他渠道环境时填写IsVisible= false,Channels = ["A"]
        :type IsVisible: bool
        :param Channels: 渠道列表，代表可见或不可见渠道由IsVisible参数指定
        :type Channels: list of str
        """
        self.EnvId = None
        self.IsVisible = None
        self.Channels = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsVisible = params.get("IsVisible")
        self.Channels = params.get("Channels")


class DescribeEnvsResponse(AbstractModel):
    """DescribeEnvs返回参数结构体

    """

    def __init__(self):
        """
        :param EnvList: 环境信息列表
        :type EnvList: list of EnvInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnvList") is not None:
            self.EnvList = []
            for item in params.get("EnvList"):
                obj = EnvInfo()
                obj._deserialize(item)
                self.EnvList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExtraPkgBillingInfoRequest(AbstractModel):
    """DescribeExtraPkgBillingInfo请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 已购买增值包的环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeExtraPkgBillingInfoResponse(AbstractModel):
    """DescribeExtraPkgBillingInfo返回参数结构体

    """

    def __init__(self):
        """
        :param EnvInfoList: 增值包计费信息列表
        :type EnvInfoList: list of EnvBillingInfoItem
        :param Total: 增值包数目
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvInfoList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnvInfoList") is not None:
            self.EnvInfoList = []
            for item in params.get("EnvInfoList"):
                obj = EnvBillingInfoItem()
                obj._deserialize(item)
                self.EnvInfoList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePostpayPackageFreeQuotasRequest(AbstractModel):
    """DescribePostpayPackageFreeQuotas请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param FreeQuotaType: 免费额度类型标识
        :type FreeQuotaType: str
        """
        self.EnvId = None
        self.FreeQuotaType = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.FreeQuotaType = params.get("FreeQuotaType")


class DescribePostpayPackageFreeQuotasResponse(AbstractModel):
    """DescribePostpayPackageFreeQuotas返回参数结构体

    """

    def __init__(self):
        """
        :param PackageFreeQuotaInfos: 免费量资源信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageFreeQuotaInfos: list of PackageFreeQuotaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PackageFreeQuotaInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PackageFreeQuotaInfos") is not None:
            self.PackageFreeQuotaInfos = []
            for item in params.get("PackageFreeQuotaInfos"):
                obj = PackageFreeQuotaInfo()
                obj._deserialize(item)
                self.PackageFreeQuotaInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQuotaDataRequest(AbstractModel):
    """DescribeQuotaData请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param MetricName: <li> 指标名: </li>
<li> StorageSizepkg: 当月存储空间容量, 单位MB </li>
<li> StorageReadpkg: 当月存储读请求次数 </li>
<li> StorageWritepkg: 当月存储写请求次数 </li>
<li> StorageCdnOriginFluxpkg: 当月CDN回源流量, 单位字节 </li>
<li> StorageCdnOriginFluxpkgDay: 当日CDN回源流量, 单位字节 </li>
<li> StorageReadpkgDay: 当日存储读请求次数 </li>
<li> StorageWritepkgDay: 当日写请求次数 </li>
<li> CDNFluxpkg: 当月CDN流量, 单位为字节 </li>
<li> CDNFluxpkgDay: 当日CDN流量, 单位为字节 </li>
<li> FunctionInvocationpkg: 当月云函数调用次数 </li>
<li> FunctionGBspkg: 当月云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFluxpkg: 当月云函数流量, 单位千字节(KB) </li>
<li> FunctionInvocationpkgDay: 当日云函数调用次数 </li>
<li> FunctionGBspkgDay: 当日云函数资源使用量, 单位Mb*Ms </li>
<li> FunctionFluxpkgDay: 当日云函数流量, 单位千字节(KB) </li>
<li> DbSizepkg: 当月数据库容量大小, 单位MB </li>
<li> DbReadpkg: 当日数据库读请求数 </li>
<li> DbWritepkg: 当日数据库写请求数 </li>
<li> StaticFsFluxPkgDay: 当日静态托管流量 </li>
<li> StaticFsFluxPkg: 当月静态托管流量</li>
<li> StaticFsSizePkg: 当月静态托管容量 </li>
<li> TkeCpuUsedPkg: 当月容器托管CPU使用量，单位核 </li>
<li> TkeMemUsedPkg: 当月容器托管内存使用量，单位MB </li>
        :type MetricName: str
        :param ResourceID: 资源ID, 目前仅对云函数、容器托管相关的指标有意义。云函数(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)、容器托管（服务名称）。如果想查询某个云函数的指标则在ResourceId中传入函数名; 如果只想查询整个namespace的指标, 则留空或不传。
        :type ResourceID: str
        """
        self.EnvId = None
        self.MetricName = None
        self.ResourceID = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.MetricName = params.get("MetricName")
        self.ResourceID = params.get("ResourceID")


class DescribeQuotaDataResponse(AbstractModel):
    """DescribeQuotaData返回参数结构体

    """

    def __init__(self):
        """
        :param MetricName: 指标名
        :type MetricName: str
        :param Value: 指标的值
        :type Value: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricName = None
        self.Value = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        self.RequestId = params.get("RequestId")


class DestroyEnvRequest(AbstractModel):
    """DestroyEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境Id
        :type EnvId: str
        :param IsForce: 针对预付费 删除隔离中的环境时要传true 正常环境直接跳过隔离期删除
        :type IsForce: bool
        """
        self.EnvId = None
        self.IsForce = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsForce = params.get("IsForce")


class DestroyEnvResponse(AbstractModel):
    """DestroyEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DestroyStaticStoreRequest(AbstractModel):
    """DestroyStaticStore请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param CdnDomain: cdn域名
        :type CdnDomain: str
        """
        self.EnvId = None
        self.CdnDomain = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CdnDomain = params.get("CdnDomain")


class DestroyStaticStoreResponse(AbstractModel):
    """DestroyStaticStore返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 条件任务结果(succ/fail)
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EndUserInfo(AbstractModel):
    """终端用户信息

    """

    def __init__(self):
        """
        :param UUId: 用户唯一ID
        :type UUId: str
        :param WXOpenId: 微信ID
        :type WXOpenId: str
        :param QQOpenId: qq ID
        :type QQOpenId: str
        :param Phone: 手机号
        :type Phone: str
        :param Email: 邮箱
        :type Email: str
        :param NickName: 昵称
        :type NickName: str
        :param Gender: 性别
        :type Gender: str
        :param AvatarUrl: 头像地址
        :type AvatarUrl: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param IsAnonymous: 是否为匿名用户
        :type IsAnonymous: bool
        :param IsDisabled: 是否禁用账户
        :type IsDisabled: bool
        :param HasPassword: 是否设置过密码
        :type HasPassword: bool
        :param UserName: 用户名
        :type UserName: str
        """
        self.UUId = None
        self.WXOpenId = None
        self.QQOpenId = None
        self.Phone = None
        self.Email = None
        self.NickName = None
        self.Gender = None
        self.AvatarUrl = None
        self.UpdateTime = None
        self.CreateTime = None
        self.IsAnonymous = None
        self.IsDisabled = None
        self.HasPassword = None
        self.UserName = None


    def _deserialize(self, params):
        self.UUId = params.get("UUId")
        self.WXOpenId = params.get("WXOpenId")
        self.QQOpenId = params.get("QQOpenId")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.NickName = params.get("NickName")
        self.Gender = params.get("Gender")
        self.AvatarUrl = params.get("AvatarUrl")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.IsAnonymous = params.get("IsAnonymous")
        self.IsDisabled = params.get("IsDisabled")
        self.HasPassword = params.get("HasPassword")
        self.UserName = params.get("UserName")


class EnvBillingInfoItem(AbstractModel):
    """环境计费信息

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
        :type PackageId: str
        :param IsAutoRenew: 自动续费标记
        :type IsAutoRenew: bool
        :param Status: 状态。包含以下取值：
<li> 空字符串：初始化中</li>
<li> NORMAL：正常</li>
<li> ISOLATE：隔离</li>
        :type Status: str
        :param PayMode: 支付方式。包含以下取值：
<li> PREPAYMENT：预付费</li>
<li> POSTPAID：后付费</li>
        :type PayMode: str
        :param IsolatedTime: 隔离时间，最近一次隔离的时间
        :type IsolatedTime: str
        :param ExpireTime: 过期时间，套餐即将到期的时间
        :type ExpireTime: str
        :param CreateTime: 创建时间，第一次接入计费方案的时间。
        :type CreateTime: str
        :param UpdateTime: 更新时间，计费信息最近一次更新的时间。
        :type UpdateTime: str
        :param IsAlwaysFree: true表示从未升级过付费版。
        :type IsAlwaysFree: bool
        :param PaymentChannel: 付费渠道。
<li> miniapp：小程序</li>
<li> qcloud：腾讯云</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentChannel: str
        :param OrderInfo: 最新的订单信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderInfo: :class:`tencentcloud.tcb.v20180608.models.OrderInfo`
        :param FreeQuota: 免费配额信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: str
        """
        self.EnvId = None
        self.PackageId = None
        self.IsAutoRenew = None
        self.Status = None
        self.PayMode = None
        self.IsolatedTime = None
        self.ExpireTime = None
        self.CreateTime = None
        self.UpdateTime = None
        self.IsAlwaysFree = None
        self.PaymentChannel = None
        self.OrderInfo = None
        self.FreeQuota = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.PackageId = params.get("PackageId")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.Status = params.get("Status")
        self.PayMode = params.get("PayMode")
        self.IsolatedTime = params.get("IsolatedTime")
        self.ExpireTime = params.get("ExpireTime")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.IsAlwaysFree = params.get("IsAlwaysFree")
        self.PaymentChannel = params.get("PaymentChannel")
        if params.get("OrderInfo") is not None:
            self.OrderInfo = OrderInfo()
            self.OrderInfo._deserialize(params.get("OrderInfo"))
        self.FreeQuota = params.get("FreeQuota")


class EnvInfo(AbstractModel):
    """环境信息

    """

    def __init__(self):
        """
        :param EnvId: 账户下该环境唯一标识
        :type EnvId: str
        :param Source: 环境来源。包含以下取值：
<li>miniapp：微信小程序</li>
<li>qcloud ：腾讯云</li>
        :type Source: str
        :param Alias: 环境别名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 最后修改时间
        :type UpdateTime: str
        :param Status: 环境状态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>UNAVAILABLE：服务不可用，可能是尚未初始化或者初始化过程中</li>
        :type Status: str
        :param Databases: 数据库列表
        :type Databases: list of DatabasesInfo
        :param Storages: 存储列表
        :type Storages: list of StorageInfo
        :param Functions: 函数列表
        :type Functions: list of FunctionInfo
        :param PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param LogServices: 云日志服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogServices: list of LogServiceInfo
        :param StaticStorages: 静态资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticStorages: list of StaticStorageInfo
        :param IsAutoDegrade: 是否到期自动降为免费版
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoDegrade: bool
        :param EnvChannel: 环境渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvChannel: str
        """
        self.EnvId = None
        self.Source = None
        self.Alias = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Status = None
        self.Databases = None
        self.Storages = None
        self.Functions = None
        self.PackageId = None
        self.PackageName = None
        self.LogServices = None
        self.StaticStorages = None
        self.IsAutoDegrade = None
        self.EnvChannel = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = DatabasesInfo()
                obj._deserialize(item)
                self.Databases.append(obj)
        if params.get("Storages") is not None:
            self.Storages = []
            for item in params.get("Storages"):
                obj = StorageInfo()
                obj._deserialize(item)
                self.Storages.append(obj)
        if params.get("Functions") is not None:
            self.Functions = []
            for item in params.get("Functions"):
                obj = FunctionInfo()
                obj._deserialize(item)
                self.Functions.append(obj)
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")
        if params.get("LogServices") is not None:
            self.LogServices = []
            for item in params.get("LogServices"):
                obj = LogServiceInfo()
                obj._deserialize(item)
                self.LogServices.append(obj)
        if params.get("StaticStorages") is not None:
            self.StaticStorages = []
            for item in params.get("StaticStorages"):
                obj = StaticStorageInfo()
                obj._deserialize(item)
                self.StaticStorages.append(obj)
        self.IsAutoDegrade = params.get("IsAutoDegrade")
        self.EnvChannel = params.get("EnvChannel")


class FunctionInfo(AbstractModel):
    """函数的信息

    """

    def __init__(self):
        """
        :param Namespace: 命名空间
        :type Namespace: str
        :param Region: 所属地域。
当前支持ap-shanghai
        :type Region: str
        """
        self.Namespace = None
        self.Region = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Region = params.get("Region")


class LogServiceInfo(AbstractModel):
    """云日志服务相关信息

    """

    def __init__(self):
        """
        :param LogsetName: log名
        :type LogsetName: str
        :param LogsetId: log-id
        :type LogsetId: str
        :param TopicName: topic名
        :type TopicName: str
        :param TopicId: topic-id
        :type TopicId: str
        :param Region: cls日志所属地域
        :type Region: str
        """
        self.LogsetName = None
        self.LogsetId = None
        self.TopicName = None
        self.TopicId = None
        self.Region = None


    def _deserialize(self, params):
        self.LogsetName = params.get("LogsetName")
        self.LogsetId = params.get("LogsetId")
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
        self.Region = params.get("Region")


class LoginStatistic(AbstractModel):
    """终端用户登录新增统计

    """

    def __init__(self):
        """
        :param StatisticalType: 统计类型 新增NEWUSER 和登录 LOGIN
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticalType: str
        :param StatisticalCycle: 统计周期：日DAY，周WEEK，月MONTH
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticalCycle: str
        :param Count: 统计总量
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.StatisticalType = None
        self.StatisticalCycle = None
        self.Count = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.StatisticalType = params.get("StatisticalType")
        self.StatisticalCycle = params.get("StatisticalCycle")
        self.Count = params.get("Count")
        self.UpdateTime = params.get("UpdateTime")


class ModifyDatabaseACLRequest(AbstractModel):
    """ModifyDatabaseACL请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param CollectionName: 集合名称
        :type CollectionName: str
        :param AclTag: 权限标签。包含以下取值：
<li> READONLY：所有用户可读，仅创建者和管理员可写</li>
<li> PRIVATE：仅创建者及管理员可读写</li>
<li> ADMINWRITE：所有用户可读，仅管理员可写</li>
<li> ADMINONLY：仅管理员可读写</li>
        :type AclTag: str
        """
        self.EnvId = None
        self.CollectionName = None
        self.AclTag = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")
        self.AclTag = params.get("AclTag")


class ModifyDatabaseACLResponse(AbstractModel):
    """ModifyDatabaseACL返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEndUserRequest(AbstractModel):
    """ModifyEndUser请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param UUId: C端用户端的唯一ID
        :type UUId: str
        :param Status: 帐号的状态
        :type Status: str
        """
        self.EnvId = None
        self.UUId = None
        self.Status = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UUId = params.get("UUId")
        self.Status = params.get("Status")


class ModifyEndUserResponse(AbstractModel):
    """ModifyEndUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEnvRequest(AbstractModel):
    """ModifyEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        :param Alias: 环境备注名，要以a-z开头，不能包含 a-zA-z0-9- 以外的字符
        :type Alias: str
        """
        self.EnvId = None
        self.Alias = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Alias = params.get("Alias")


class ModifyEnvResponse(AbstractModel):
    """ModifyEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrderInfo(AbstractModel):
    """订单信息

    """

    def __init__(self):
        """
        :param TranId: 订单号
        :type TranId: str
        :param PackageId: 订单要切换的套餐ID
        :type PackageId: str
        :param TranType: 订单类型
<li>1 购买</li>
<li>2 续费</li>
<li>3 变配</li>
        :type TranType: str
        :param TranStatus: 订单状态。
<li>1未支付</li>
<li>2 支付中</li>
<li>3 发货中</li>
<li>4 发货成功</li>
<li>5 发货失败</li>
<li>6 已退款</li>
<li>7 已取消</li>
<li>100 已删除</li>
        :type TranStatus: str
        :param UpdateTime: 订单更新时间
        :type UpdateTime: str
        :param CreateTime: 订单创建时间
        :type CreateTime: str
        :param PayMode: 付费模式.
<li>prepayment 预付费</li>
<li>postpaid 后付费</li>
        :type PayMode: str
        :param ExtensionId: 订单绑定的扩展ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionId: str
        :param ResourceReady: 资源初始化结果(仅当ExtensionId不为空时有效): successful(初始化成功), failed(初始化失败), doing(初始化进行中), init(准备初始化)
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceReady: str
        """
        self.TranId = None
        self.PackageId = None
        self.TranType = None
        self.TranStatus = None
        self.UpdateTime = None
        self.CreateTime = None
        self.PayMode = None
        self.ExtensionId = None
        self.ResourceReady = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.PackageId = params.get("PackageId")
        self.TranType = params.get("TranType")
        self.TranStatus = params.get("TranStatus")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.ExtensionId = params.get("ExtensionId")
        self.ResourceReady = params.get("ResourceReady")


class PackageFreeQuotaInfo(AbstractModel):
    """后付费免费额度

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型
<li>COS</li>
<li>CDN</li>
<li>FLEXDB</li>
<li>SCF</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param ResourceMetric: 资源指标名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceMetric: str
        :param FreeQuota: 资源指标免费量
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuota: int
        :param MetricUnit: 指标单位
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricUnit: str
        :param DeductType: 免费量抵扣周期
<li>sum-month:以月为单位抵扣</li>
<li>sum-day:以天为单位抵扣</li>
<li>totalize:总容量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type DeductType: str
        :param FreeQuotaType: 免费量类型
<li>basic:通用量抵扣</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeQuotaType: str
        """
        self.ResourceType = None
        self.ResourceMetric = None
        self.FreeQuota = None
        self.MetricUnit = None
        self.DeductType = None
        self.FreeQuotaType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceMetric = params.get("ResourceMetric")
        self.FreeQuota = params.get("FreeQuota")
        self.MetricUnit = params.get("MetricUnit")
        self.DeductType = params.get("DeductType")
        self.FreeQuotaType = params.get("FreeQuotaType")


class PlatformStatistic(AbstractModel):
    """终端用户平台统计信息

    """

    def __init__(self):
        """
        :param Platform: 终端用户从属平台
注意：此字段可能返回 null，表示取不到有效值。
        :type Platform: str
        :param Count: 平台终端用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Platform = None
        self.Count = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Count = params.get("Count")
        self.UpdateTime = params.get("UpdateTime")


class PostpayEnvQuota(AbstractModel):
    """按量付费免费配额信息

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型
        :type ResourceType: str
        :param MetricName: 指标名
        :type MetricName: str
        :param Value: 配额值
        :type Value: int
        :param StartTime: 配额生效时间
为空表示没有时间限制
        :type StartTime: str
        :param EndTime: 配额失效时间
为空表示没有时间限制
        :type EndTime: str
        """
        self.ResourceType = None
        self.MetricName = None
        self.Value = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ReinstateEnvRequest(AbstractModel):
    """ReinstateEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class ReinstateEnvResponse(AbstractModel):
    """ReinstateEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StaticStorageInfo(AbstractModel):
    """静态CDN资源信息

    """

    def __init__(self):
        """
        :param StaticDomain: 静态CDN域名
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticDomain: str
        :param DefaultDirName: 静态CDN默认文件夹，当前为根目录
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultDirName: str
        :param Status: 资源状态(process/online/offline/init)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Region: cos所属区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Bucket: bucket信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self.StaticDomain = None
        self.DefaultDirName = None
        self.Status = None
        self.Region = None
        self.Bucket = None


    def _deserialize(self, params):
        self.StaticDomain = params.get("StaticDomain")
        self.DefaultDirName = params.get("DefaultDirName")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")


class StorageInfo(AbstractModel):
    """StorageInfo 资源信息

    """

    def __init__(self):
        """
        :param Region: 资源所属地域。
当前支持ap-shanghai
        :type Region: str
        :param Bucket: 桶名，存储资源的唯一标识
        :type Bucket: str
        :param CdnDomain: cdn 域名
        :type CdnDomain: str
        :param AppId: 资源所属用户的腾讯云appId
        :type AppId: str
        """
        self.Region = None
        self.Bucket = None
        self.CdnDomain = None
        self.AppId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.CdnDomain = params.get("CdnDomain")
        self.AppId = params.get("AppId")