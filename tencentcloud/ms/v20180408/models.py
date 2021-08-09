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


class AdInfo(AbstractModel):
    """广告信息

    """

    def __init__(self):
        """
        :param Spots: 插播广告列表\n        :type Spots: list of PluginInfo\n        :param BoutiqueRecommands: 精品推荐广告列表\n        :type BoutiqueRecommands: list of PluginInfo\n        :param FloatWindowses: 悬浮窗广告列表\n        :type FloatWindowses: list of PluginInfo\n        :param Banners: banner广告列表\n        :type Banners: list of PluginInfo\n        :param IntegralWalls: 积分墙广告列表\n        :type IntegralWalls: list of PluginInfo\n        :param NotifyBars: 通知栏广告列表\n        :type NotifyBars: list of PluginInfo\n        """
        self.Spots = None
        self.BoutiqueRecommands = None
        self.FloatWindowses = None
        self.Banners = None
        self.IntegralWalls = None
        self.NotifyBars = None


    def _deserialize(self, params):
        if params.get("Spots") is not None:
            self.Spots = []
            for item in params.get("Spots"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.Spots.append(obj)
        if params.get("BoutiqueRecommands") is not None:
            self.BoutiqueRecommands = []
            for item in params.get("BoutiqueRecommands"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.BoutiqueRecommands.append(obj)
        if params.get("FloatWindowses") is not None:
            self.FloatWindowses = []
            for item in params.get("FloatWindowses"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.FloatWindowses.append(obj)
        if params.get("Banners") is not None:
            self.Banners = []
            for item in params.get("Banners"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.Banners.append(obj)
        if params.get("IntegralWalls") is not None:
            self.IntegralWalls = []
            for item in params.get("IntegralWalls"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.IntegralWalls.append(obj)
        if params.get("NotifyBars") is not None:
            self.NotifyBars = []
            for item in params.get("NotifyBars"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.NotifyBars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppDetailInfo(AbstractModel):
    """app的详细基础信息

    """

    def __init__(self):
        """
        :param AppName: app的名称\n        :type AppName: str\n        :param AppPkgName: app的包名\n        :type AppPkgName: str\n        :param AppVersion: app的版本号\n        :type AppVersion: str\n        :param AppSize: app的大小\n        :type AppSize: int\n        :param AppMd5: app的md5\n        :type AppMd5: str\n        :param AppIconUrl: app的图标url\n        :type AppIconUrl: str\n        :param FileName: app的文件名称\n        :type FileName: str\n        """
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppSize = None
        self.AppMd5 = None
        self.AppIconUrl = None
        self.FileName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppSize = params.get("AppSize")
        self.AppMd5 = params.get("AppMd5")
        self.AppIconUrl = params.get("AppIconUrl")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppInfo(AbstractModel):
    """提交的app基本信息

    """

    def __init__(self):
        """
        :param AppUrl: app的url，必须保证不用权限校验就可以下载\n        :type AppUrl: str\n        :param AppMd5: app的md5，需要正确传递\n        :type AppMd5: str\n        :param AppSize: app的大小\n        :type AppSize: int\n        :param FileName: app的文件名\n        :type FileName: str\n        :param AppPkgName: app的包名，需要正确的传递此字段\n        :type AppPkgName: str\n        :param AppVersion: app的版本号\n        :type AppVersion: str\n        :param AppIconUrl: app的图标url\n        :type AppIconUrl: str\n        :param AppName: app的名称\n        :type AppName: str\n        """
        self.AppUrl = None
        self.AppMd5 = None
        self.AppSize = None
        self.FileName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppIconUrl = None
        self.AppName = None


    def _deserialize(self, params):
        self.AppUrl = params.get("AppUrl")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.FileName = params.get("FileName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppScanSet(AbstractModel):
    """扫描后app的信息，包含基本信息和扫描状态信息

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识\n        :type ItemId: str\n        :param AppName: app的名称\n        :type AppName: str\n        :param AppPkgName: app的包名\n        :type AppPkgName: str\n        :param AppVersion: app的版本号\n        :type AppVersion: str\n        :param AppMd5: app的md5\n        :type AppMd5: str\n        :param AppSize: app的大小\n        :type AppSize: int\n        :param ScanCode: 扫描结果返回码\n        :type ScanCode: int\n        :param TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type TaskStatus: int\n        :param TaskTime: 提交扫描时间\n        :type TaskTime: int\n        :param AppIconUrl: app的图标url\n        :type AppIconUrl: str\n        :param AppSid: 标识唯一该app，主要用于删除\n        :type AppSid: str\n        :param SafeType: 安全类型:1-安全软件，2-风险软件，3病毒软件\n        :type SafeType: int\n        :param VulCount: 漏洞个数\n        :type VulCount: int\n        """
        self.ItemId = None
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppMd5 = None
        self.AppSize = None
        self.ScanCode = None
        self.TaskStatus = None
        self.TaskTime = None
        self.AppIconUrl = None
        self.AppSid = None
        self.SafeType = None
        self.VulCount = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.ScanCode = params.get("ScanCode")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskTime = params.get("TaskTime")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppSid = params.get("AppSid")
        self.SafeType = params.get("SafeType")
        self.VulCount = params.get("VulCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSetInfo(AbstractModel):
    """加固后app的信息，包含基本信息和加固信息

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识\n        :type ItemId: str\n        :param AppName: app的名称\n        :type AppName: str\n        :param AppPkgName: app的包名\n        :type AppPkgName: str\n        :param AppVersion: app的版本号\n        :type AppVersion: str\n        :param AppMd5: app的md5\n        :type AppMd5: str\n        :param AppSize: app的大小\n        :type AppSize: int\n        :param ServiceEdition: 加固服务版本\n        :type ServiceEdition: str\n        :param ShieldCode: 加固结果返回码\n        :type ShieldCode: int\n        :param AppUrl: 加固后的APP下载地址\n        :type AppUrl: str\n        :param TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type TaskStatus: int\n        :param ClientIp: 请求的客户端ip\n        :type ClientIp: str\n        :param TaskTime: 提交加固时间\n        :type TaskTime: int\n        :param AppIconUrl: app的图标url\n        :type AppIconUrl: str\n        :param ShieldMd5: 加固后app的md5\n        :type ShieldMd5: str\n        :param ShieldSize: 加固后app的大小\n        :type ShieldSize: int\n        """
        self.ItemId = None
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppMd5 = None
        self.AppSize = None
        self.ServiceEdition = None
        self.ShieldCode = None
        self.AppUrl = None
        self.TaskStatus = None
        self.ClientIp = None
        self.TaskTime = None
        self.AppIconUrl = None
        self.ShieldMd5 = None
        self.ShieldSize = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.ServiceEdition = params.get("ServiceEdition")
        self.ShieldCode = params.get("ShieldCode")
        self.AppUrl = params.get("AppUrl")
        self.TaskStatus = params.get("TaskStatus")
        self.ClientIp = params.get("ClientIp")
        self.TaskTime = params.get("TaskTime")
        self.AppIconUrl = params.get("AppIconUrl")
        self.ShieldMd5 = params.get("ShieldMd5")
        self.ShieldSize = params.get("ShieldSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindInfo(AbstractModel):
    """用户绑定app的基本信息

    """

    def __init__(self):
        """
        :param AppIconUrl: app的icon的url\n        :type AppIconUrl: str\n        :param AppName: app的名称\n        :type AppName: str\n        :param AppPkgName: app的包名\n        :type AppPkgName: str\n        """
        self.AppIconUrl = None
        self.AppName = None
        self.AppPkgName = None


    def _deserialize(self, params):
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBindInstanceRequest(AbstractModel):
    """CreateBindInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 资源id，全局唯一\n        :type ResourceId: str\n        :param AppIconUrl: app的icon的url\n        :type AppIconUrl: str\n        :param AppName: app的名称\n        :type AppName: str\n        :param AppPkgName: app的包名\n        :type AppPkgName: str\n        """
        self.ResourceId = None
        self.AppIconUrl = None
        self.AppName = None
        self.AppPkgName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBindInstanceResponse(AbstractModel):
    """CreateBindInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class CreateCosSecKeyInstanceRequest(AbstractModel):
    """CreateCosSecKeyInstance请求参数结构体

    """

    def __init__(self):
        """
        :param CosRegion: 地域信息，例如广州：ap-guangzhou，上海：ap-shanghai，默认为广州。\n        :type CosRegion: str\n        :param Duration: 密钥有效时间，默认为1小时。\n        :type Duration: int\n        """
        self.CosRegion = None
        self.Duration = None


    def _deserialize(self, params):
        self.CosRegion = params.get("CosRegion")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosSecKeyInstanceResponse(AbstractModel):
    """CreateCosSecKeyInstance返回参数结构体

    """

    def __init__(self):
        """
        :param CosAppid: COS密钥对应的AppId\n        :type CosAppid: int\n        :param CosBucket: COS密钥对应的存储桶名\n        :type CosBucket: str\n        :param CosRegion: 存储桶对应的地域\n        :type CosRegion: str\n        :param ExpireTime: 密钥过期时间\n        :type ExpireTime: int\n        :param CosId: 密钥ID信息\n        :type CosId: str\n        :param CosKey: 密钥KEY信息\n        :type CosKey: str\n        :param CosTocken: 密钥TOCKEN信息\n        :type CosTocken: str\n        :param CosPrefix: 密钥可访问的文件前缀人。例如：CosPrefix=test/123/666，则该密钥只能操作test/123/666为前缀的文件，例如test/123/666/1.txt\n        :type CosPrefix: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CosAppid = None
        self.CosBucket = None
        self.CosRegion = None
        self.ExpireTime = None
        self.CosId = None
        self.CosKey = None
        self.CosTocken = None
        self.CosPrefix = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CosAppid = params.get("CosAppid")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.ExpireTime = params.get("ExpireTime")
        self.CosId = params.get("CosId")
        self.CosKey = params.get("CosKey")
        self.CosTocken = params.get("CosTocken")
        self.CosPrefix = params.get("CosPrefix")
        self.RequestId = params.get("RequestId")


class CreateResourceInstancesRequest(AbstractModel):
    """CreateResourceInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Pid: 资源类型id。13624：加固专业版。\n        :type Pid: int\n        :param TimeUnit: 时间单位，取值为d，m，y，分别表示天，月，年。\n        :type TimeUnit: str\n        :param TimeSpan: 时间数量。\n        :type TimeSpan: int\n        :param ResourceNum: 资源数量。\n        :type ResourceNum: int\n        """
        self.Pid = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.ResourceNum = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.ResourceNum = params.get("ResourceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceInstancesResponse(AbstractModel):
    """CreateResourceInstances返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceSet: 新创建的资源列表。\n        :type ResourceSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceSet = params.get("ResourceSet")
        self.RequestId = params.get("RequestId")


class CreateScanInstancesRequest(AbstractModel):
    """CreateScanInstances请求参数结构体

    """

    def __init__(self):
        """
        :param AppInfos: 待扫描的app信息列表，一次最多提交20个\n        :type AppInfos: list of AppInfo\n        :param ScanInfo: 扫描信息\n        :type ScanInfo: :class:`tencentcloud.ms.v20180408.models.ScanInfo`\n        """
        self.AppInfos = None
        self.ScanInfo = None


    def _deserialize(self, params):
        if params.get("AppInfos") is not None:
            self.AppInfos = []
            for item in params.get("AppInfos"):
                obj = AppInfo()
                obj._deserialize(item)
                self.AppInfos.append(obj)
        if params.get("ScanInfo") is not None:
            self.ScanInfo = ScanInfo()
            self.ScanInfo._deserialize(params.get("ScanInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScanInstancesResponse(AbstractModel):
    """CreateScanInstances返回参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识\n        :type ItemId: str\n        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type Progress: int\n        :param AppMd5s: 提交成功的app的md5集合\n        :type AppMd5s: list of str\n        :param LimitCount: 剩余可用次数\n        :type LimitCount: int\n        :param LimitTime: 到期时间\n        :type LimitTime: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ItemId = None
        self.Progress = None
        self.AppMd5s = None
        self.LimitCount = None
        self.LimitTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.Progress = params.get("Progress")
        self.AppMd5s = params.get("AppMd5s")
        self.LimitCount = params.get("LimitCount")
        self.LimitTime = params.get("LimitTime")
        self.RequestId = params.get("RequestId")


class CreateShieldInstanceRequest(AbstractModel):
    """CreateShieldInstance请求参数结构体

    """

    def __init__(self):
        """
        :param AppInfo: 待加固的应用信息\n        :type AppInfo: :class:`tencentcloud.ms.v20180408.models.AppInfo`\n        :param ServiceInfo: 加固服务信息\n        :type ServiceInfo: :class:`tencentcloud.ms.v20180408.models.ServiceInfo`\n        """
        self.AppInfo = None
        self.ServiceInfo = None


    def _deserialize(self, params):
        if params.get("AppInfo") is not None:
            self.AppInfo = AppInfo()
            self.AppInfo._deserialize(params.get("AppInfo"))
        if params.get("ServiceInfo") is not None:
            self.ServiceInfo = ServiceInfo()
            self.ServiceInfo._deserialize(params.get("ServiceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShieldInstanceResponse(AbstractModel):
    """CreateShieldInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type Progress: int\n        :param ItemId: 任务唯一标识\n        :type ItemId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Progress = None
        self.ItemId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.ItemId = params.get("ItemId")
        self.RequestId = params.get("RequestId")


class CreateShieldPlanInstanceRequest(AbstractModel):
    """CreateShieldPlanInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 资源id\n        :type ResourceId: str\n        :param PlanName: 策略名称\n        :type PlanName: str\n        :param PlanInfo: 策略具体信息\n        :type PlanInfo: :class:`tencentcloud.ms.v20180408.models.PlanInfo`\n        """
        self.ResourceId = None
        self.PlanName = None
        self.PlanInfo = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.PlanName = params.get("PlanName")
        if params.get("PlanInfo") is not None:
            self.PlanInfo = PlanInfo()
            self.PlanInfo._deserialize(params.get("PlanInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShieldPlanInstanceResponse(AbstractModel):
    """CreateShieldPlanInstance返回参数结构体

    """

    def __init__(self):
        """
        :param PlanId: 策略id\n        :type PlanId: int\n        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PlanId = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteScanInstancesRequest(AbstractModel):
    """DeleteScanInstances请求参数结构体

    """

    def __init__(self):
        """
        :param AppSids: 删除一个或多个扫描的app，最大支持20个\n        :type AppSids: list of str\n        """
        self.AppSids = None


    def _deserialize(self, params):
        self.AppSids = params.get("AppSids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScanInstancesResponse(AbstractModel):
    """DeleteScanInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteShieldInstancesRequest(AbstractModel):
    """DeleteShieldInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ItemIds: 任务唯一标识ItemId的列表\n        :type ItemIds: list of str\n        """
        self.ItemIds = None


    def _deserialize(self, params):
        self.ItemIds = params.get("ItemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShieldInstancesResponse(AbstractModel):
    """DeleteShieldInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeResourceInstancesRequest(AbstractModel):
    """DescribeResourceInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Pids: 资源类别id数组，13624：加固专业版，12750：企业版。空数组表示返回全部资源。\n        :type Pids: list of int non-negative\n        :param Filters: 支持通过资源id，pid进行查询\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 数量限制，默认为20，最大值为100。\n        :type Limit: int\n        :param OrderField: 按某个字段排序，目前支持CreateTime、ExpireTime其中的一个排序。\n        :type OrderField: str\n        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc。\n        :type OrderDirection: str\n        """
        self.Pids = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Pids = params.get("Pids")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceInstancesResponse(AbstractModel):
    """DescribeResourceInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的资源数量\n        :type TotalCount: int\n        :param ResourceSet: 符合要求的资源数组\n        :type ResourceSet: list of ResourceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanInstancesRequest(AbstractModel):
    """DescribeScanInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过app名称，app包名进行筛选\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 数量限制，默认为20，最大值为100。\n        :type Limit: int\n        :param ItemIds: 可以提供ItemId数组来查询一个或者多个结果。注意不可以同时指定ItemIds和Filters。\n        :type ItemIds: list of str\n        :param OrderField: 按某个字段排序，目前仅支持TaskTime排序。\n        :type OrderField: str\n        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc。\n        :type OrderDirection: str\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.ItemIds = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ItemIds = params.get("ItemIds")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanInstancesResponse(AbstractModel):
    """DescribeScanInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的app数量\n        :type TotalCount: int\n        :param ScanSet: 一个关于app详细信息的结构体，主要包括app的基本信息和扫描状态信息。\n        :type ScanSet: list of AppScanSet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ScanSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ScanSet") is not None:
            self.ScanSet = []
            for item in params.get("ScanSet"):
                obj = AppScanSet()
                obj._deserialize(item)
                self.ScanSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanResultsRequest(AbstractModel):
    """DescribeScanResults请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识\n        :type ItemId: str\n        :param AppMd5s: 批量查询一个或者多个app的扫描结果，如果不传表示查询该任务下所提交的所有app\n        :type AppMd5s: list of str\n        """
        self.ItemId = None
        self.AppMd5s = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppMd5s = params.get("AppMd5s")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanResultsResponse(AbstractModel):
    """DescribeScanResults返回参数结构体

    """

    def __init__(self):
        """
        :param ScanSet: 批量扫描的app结果集\n        :type ScanSet: list of ScanSetInfo\n        :param TotalCount: 批量扫描结果的个数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ScanSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScanSet") is not None:
            self.ScanSet = []
            for item in params.get("ScanSet"):
                obj = ScanSetInfo()
                obj._deserialize(item)
                self.ScanSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeShieldInstancesRequest(AbstractModel):
    """DescribeShieldInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过app名称，app包名，加固的服务版本，提交的渠道进行筛选。\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 数量限制，默认为20，最大值为100。\n        :type Limit: int\n        :param ItemIds: 可以提供ItemId数组来查询一个或者多个结果。注意不可以同时指定ItemIds和Filters。\n        :type ItemIds: list of str\n        :param OrderField: 按某个字段排序，目前仅支持TaskTime排序。\n        :type OrderField: str\n        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc。\n        :type OrderDirection: str\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.ItemIds = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ItemIds = params.get("ItemIds")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShieldInstancesResponse(AbstractModel):
    """DescribeShieldInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的app数量\n        :type TotalCount: int\n        :param AppSet: 一个关于app详细信息的结构体，主要包括app的基本信息和加固信息。\n        :type AppSet: list of AppSetInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AppSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AppSet") is not None:
            self.AppSet = []
            for item in params.get("AppSet"):
                obj = AppSetInfo()
                obj._deserialize(item)
                self.AppSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShieldPlanInstanceRequest(AbstractModel):
    """DescribeShieldPlanInstance请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceId: 资源id\n        :type ResourceId: str\n        :param Pid: 服务类别id\n        :type Pid: int\n        """
        self.ResourceId = None
        self.Pid = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShieldPlanInstanceResponse(AbstractModel):
    """DescribeShieldPlanInstance返回参数结构体

    """

    def __init__(self):
        """
        :param BindInfo: 绑定资源信息\n        :type BindInfo: :class:`tencentcloud.ms.v20180408.models.BindInfo`\n        :param ShieldPlanInfo: 加固策略信息\n        :type ShieldPlanInfo: :class:`tencentcloud.ms.v20180408.models.ShieldPlanInfo`\n        :param ResourceServiceInfo: 加固资源信息\n        :type ResourceServiceInfo: :class:`tencentcloud.ms.v20180408.models.ResourceServiceInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BindInfo = None
        self.ShieldPlanInfo = None
        self.ResourceServiceInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BindInfo") is not None:
            self.BindInfo = BindInfo()
            self.BindInfo._deserialize(params.get("BindInfo"))
        if params.get("ShieldPlanInfo") is not None:
            self.ShieldPlanInfo = ShieldPlanInfo()
            self.ShieldPlanInfo._deserialize(params.get("ShieldPlanInfo"))
        if params.get("ResourceServiceInfo") is not None:
            self.ResourceServiceInfo = ResourceServiceInfo()
            self.ResourceServiceInfo._deserialize(params.get("ResourceServiceInfo"))
        self.RequestId = params.get("RequestId")


class DescribeShieldResultRequest(AbstractModel):
    """DescribeShieldResult请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识\n        :type ItemId: str\n        """
        self.ItemId = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShieldResultResponse(AbstractModel):
    """DescribeShieldResult返回参数结构体

    """

    def __init__(self):
        """
        :param TaskStatus: 任务状态: 0-请返回,1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type TaskStatus: int\n        :param AppDetailInfo: app加固前的详细信息\n        :type AppDetailInfo: :class:`tencentcloud.ms.v20180408.models.AppDetailInfo`\n        :param ShieldInfo: app加固后的详细信息\n        :type ShieldInfo: :class:`tencentcloud.ms.v20180408.models.ShieldInfo`\n        :param StatusDesc: 状态描述\n        :type StatusDesc: str\n        :param StatusRef: 状态指引\n        :type StatusRef: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskStatus = None
        self.AppDetailInfo = None
        self.ShieldInfo = None
        self.StatusDesc = None
        self.StatusRef = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("AppDetailInfo") is not None:
            self.AppDetailInfo = AppDetailInfo()
            self.AppDetailInfo._deserialize(params.get("AppDetailInfo"))
        if params.get("ShieldInfo") is not None:
            self.ShieldInfo = ShieldInfo()
            self.ShieldInfo._deserialize(params.get("ShieldInfo"))
        self.StatusDesc = params.get("StatusDesc")
        self.StatusRef = params.get("StatusRef")
        self.RequestId = params.get("RequestId")


class DescribeUserBaseInfoInstanceRequest(AbstractModel):
    """DescribeUserBaseInfoInstance请求参数结构体

    """


class DescribeUserBaseInfoInstanceResponse(AbstractModel):
    """DescribeUserBaseInfoInstance返回参数结构体

    """

    def __init__(self):
        """
        :param UserUin: 用户uin信息\n        :type UserUin: int\n        :param UserAppid: 用户APPID信息\n        :type UserAppid: int\n        :param TimeStamp: 系统时间戳\n        :type TimeStamp: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.UserUin = None
        self.UserAppid = None
        self.TimeStamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.UserAppid = params.get("UserAppid")
        self.TimeStamp = params.get("TimeStamp")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """筛选数据结构

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段\n        :type Name: str\n        :param Value: 需要过滤字段的值\n        :type Value: str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanDetailInfo(AbstractModel):
    """加固策略具体信息

    """

    def __init__(self):
        """
        :param IsDefault: 默认策略，1为默认，0为非默认\n        :type IsDefault: int\n        :param PlanId: 策略id\n        :type PlanId: int\n        :param PlanName: 策略名称\n        :type PlanName: str\n        :param PlanInfo: 策略信息\n        :type PlanInfo: :class:`tencentcloud.ms.v20180408.models.PlanInfo`\n        """
        self.IsDefault = None
        self.PlanId = None
        self.PlanName = None
        self.PlanInfo = None


    def _deserialize(self, params):
        self.IsDefault = params.get("IsDefault")
        self.PlanId = params.get("PlanId")
        self.PlanName = params.get("PlanName")
        if params.get("PlanInfo") is not None:
            self.PlanInfo = PlanInfo()
            self.PlanInfo._deserialize(params.get("PlanInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanInfo(AbstractModel):
    """加固策略信息

    """

    def __init__(self):
        """
        :param ApkSizeOpt: apk大小优化，0关闭，1开启\n        :type ApkSizeOpt: int\n        :param Dex: Dex加固，0关闭，1开启\n        :type Dex: int\n        :param So: So加固，0关闭，1开启\n        :type So: int\n        :param Bugly: 数据收集，0关闭，1开启\n        :type Bugly: int\n        :param AntiRepack: 防止重打包，0关闭，1开启\n        :type AntiRepack: int\n        :param SeperateDex: Dex分离，0关闭，1开启\n        :type SeperateDex: int\n        :param Db: 内存保护，0关闭，1开启\n        :type Db: int\n        :param DexSig: Dex签名校验，0关闭，1开启\n        :type DexSig: int\n        :param SoInfo: So文件信息\n        :type SoInfo: :class:`tencentcloud.ms.v20180408.models.SoInfo`\n        :param AntiVMP: vmp，0关闭，1开启\n        :type AntiVMP: int\n        :param SoType: 保护so的强度，\n        :type SoType: list of str\n        :param AntiLogLeak: 防日志泄漏，0关闭，1开启\n        :type AntiLogLeak: int\n        :param AntiQemuRoot: root检测，0关闭，1开启\n        :type AntiQemuRoot: int\n        :param AntiAssets: 资源防篡改，0关闭，1开启\n        :type AntiAssets: int\n        :param AntiScreenshot: 防止截屏，0关闭，1开启\n        :type AntiScreenshot: int\n        :param AntiSSL: SSL证书防窃取，0关闭，1开启\n        :type AntiSSL: int\n        """
        self.ApkSizeOpt = None
        self.Dex = None
        self.So = None
        self.Bugly = None
        self.AntiRepack = None
        self.SeperateDex = None
        self.Db = None
        self.DexSig = None
        self.SoInfo = None
        self.AntiVMP = None
        self.SoType = None
        self.AntiLogLeak = None
        self.AntiQemuRoot = None
        self.AntiAssets = None
        self.AntiScreenshot = None
        self.AntiSSL = None


    def _deserialize(self, params):
        self.ApkSizeOpt = params.get("ApkSizeOpt")
        self.Dex = params.get("Dex")
        self.So = params.get("So")
        self.Bugly = params.get("Bugly")
        self.AntiRepack = params.get("AntiRepack")
        self.SeperateDex = params.get("SeperateDex")
        self.Db = params.get("Db")
        self.DexSig = params.get("DexSig")
        if params.get("SoInfo") is not None:
            self.SoInfo = SoInfo()
            self.SoInfo._deserialize(params.get("SoInfo"))
        self.AntiVMP = params.get("AntiVMP")
        self.SoType = params.get("SoType")
        self.AntiLogLeak = params.get("AntiLogLeak")
        self.AntiQemuRoot = params.get("AntiQemuRoot")
        self.AntiAssets = params.get("AntiAssets")
        self.AntiScreenshot = params.get("AntiScreenshot")
        self.AntiSSL = params.get("AntiSSL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginInfo(AbstractModel):
    """插件信息

    """

    def __init__(self):
        """
        :param PluginType: 插件类型，分别为 1-通知栏广告，2-积分墙广告，3-banner广告，4- 悬浮窗图标广告，5-精品推荐列表广告, 6-插播广告\n        :type PluginType: int\n        :param PluginName: 插件名称\n        :type PluginName: str\n        :param PluginDesc: 插件描述\n        :type PluginDesc: str\n        """
        self.PluginType = None
        self.PluginName = None
        self.PluginDesc = None


    def _deserialize(self, params):
        self.PluginType = params.get("PluginType")
        self.PluginName = params.get("PluginName")
        self.PluginDesc = params.get("PluginDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInfo(AbstractModel):
    """拉取某个用户的所有资源信息

    """

    def __init__(self):
        """
        :param ResourceId: 用户购买的资源id，全局唯一\n        :type ResourceId: str\n        :param Pid: 资源的pid，MTP加固-12767，应用加固-12750 MTP反作弊-12766 源代码混淆-12736\n        :type Pid: int\n        :param CreateTime: 购买时间戳\n        :type CreateTime: int\n        :param ExpireTime: 到期时间戳\n        :type ExpireTime: int\n        :param IsBind: 0-未绑定，1-已绑定\n        :type IsBind: int\n        :param BindInfo: 用户绑定app的基本信息\n        :type BindInfo: :class:`tencentcloud.ms.v20180408.models.BindInfo`\n        :param ResourceName: 资源名称，如应用加固，漏洞扫描\n        :type ResourceName: str\n        """
        self.ResourceId = None
        self.Pid = None
        self.CreateTime = None
        self.ExpireTime = None
        self.IsBind = None
        self.BindInfo = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Pid = params.get("Pid")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsBind = params.get("IsBind")
        if params.get("BindInfo") is not None:
            self.BindInfo = BindInfo()
            self.BindInfo._deserialize(params.get("BindInfo"))
        self.ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceServiceInfo(AbstractModel):
    """资源服务信息

    """

    def __init__(self):
        """
        :param CreateTime: 创建时间戳\n        :type CreateTime: int\n        :param ExpireTime: 到期时间戳\n        :type ExpireTime: int\n        :param ResourceName: 资源名称，如应用加固，源码混淆\n        :type ResourceName: str\n        """
        self.CreateTime = None
        self.ExpireTime = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanInfo(AbstractModel):
    """需要扫描的应用的服务信息

    """

    def __init__(self):
        """
        :param CallbackUrl: 任务处理完成后的反向通知回调地址,批量提交app每扫描完成一个会通知一次,通知为POST请求，post信息{ItemId:\n        :type CallbackUrl: str\n        :param ScanTypes: VULSCAN-漏洞扫描信息，VIRUSSCAN-返回病毒扫描信息， ADSCAN-广告扫描信息，PLUGINSCAN-插件扫描信息，PERMISSION-系统权限信息，SENSITIVE-敏感词信息，可以自由组合\n        :type ScanTypes: list of str\n        """
        self.CallbackUrl = None
        self.ScanTypes = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.ScanTypes = params.get("ScanTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanPermissionInfo(AbstractModel):
    """安全扫描系统权限信息

    """

    def __init__(self):
        """
        :param Permission: 系统权限\n        :type Permission: str\n        """
        self.Permission = None


    def _deserialize(self, params):
        self.Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanPermissionList(AbstractModel):
    """安全扫描系统权限信息

    """

    def __init__(self):
        """
        :param PermissionList: 系统权限信息\n        :type PermissionList: list of ScanPermissionInfo\n        """
        self.PermissionList = None


    def _deserialize(self, params):
        if params.get("PermissionList") is not None:
            self.PermissionList = []
            for item in params.get("PermissionList"):
                obj = ScanPermissionInfo()
                obj._deserialize(item)
                self.PermissionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanSensitiveInfo(AbstractModel):
    """安全扫描敏感词

    """

    def __init__(self):
        """
        :param WordList: 敏感词\n        :type WordList: list of str\n        :param FilePath: 敏感词对应的文件信息\n        :type FilePath: str\n        :param FileSha: 文件sha1值\n        :type FileSha: str\n        """
        self.WordList = None
        self.FilePath = None
        self.FileSha = None


    def _deserialize(self, params):
        self.WordList = params.get("WordList")
        self.FilePath = params.get("FilePath")
        self.FileSha = params.get("FileSha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanSensitiveList(AbstractModel):
    """安全扫描敏感词列表

    """

    def __init__(self):
        """
        :param SensitiveList: 敏感词列表\n        :type SensitiveList: list of ScanSensitiveInfo\n        """
        self.SensitiveList = None


    def _deserialize(self, params):
        if params.get("SensitiveList") is not None:
            self.SensitiveList = []
            for item in params.get("SensitiveList"):
                obj = ScanSensitiveInfo()
                obj._deserialize(item)
                self.SensitiveList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanSetInfo(AbstractModel):
    """app扫描结果集

    """

    def __init__(self):
        """
        :param TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时\n        :type TaskStatus: int\n        :param AppDetailInfo: app信息\n        :type AppDetailInfo: :class:`tencentcloud.ms.v20180408.models.AppDetailInfo`\n        :param VirusInfo: 病毒信息\n        :type VirusInfo: :class:`tencentcloud.ms.v20180408.models.VirusInfo`\n        :param VulInfo: 漏洞信息\n        :type VulInfo: :class:`tencentcloud.ms.v20180408.models.VulInfo`\n        :param AdInfo: 广告插件信息\n        :type AdInfo: :class:`tencentcloud.ms.v20180408.models.AdInfo`\n        :param TaskTime: 提交扫描的时间\n        :type TaskTime: int\n        :param StatusCode: 状态码，成功返回0，失败返回错误码\n        :type StatusCode: int\n        :param StatusDesc: 状态描述\n        :type StatusDesc: str\n        :param StatusRef: 状态操作指引\n        :type StatusRef: str\n        :param PermissionInfo: 系统权限信息\n        :type PermissionInfo: :class:`tencentcloud.ms.v20180408.models.ScanPermissionList`\n        :param SensitiveInfo: 敏感词列表\n        :type SensitiveInfo: :class:`tencentcloud.ms.v20180408.models.ScanSensitiveList`\n        """
        self.TaskStatus = None
        self.AppDetailInfo = None
        self.VirusInfo = None
        self.VulInfo = None
        self.AdInfo = None
        self.TaskTime = None
        self.StatusCode = None
        self.StatusDesc = None
        self.StatusRef = None
        self.PermissionInfo = None
        self.SensitiveInfo = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("AppDetailInfo") is not None:
            self.AppDetailInfo = AppDetailInfo()
            self.AppDetailInfo._deserialize(params.get("AppDetailInfo"))
        if params.get("VirusInfo") is not None:
            self.VirusInfo = VirusInfo()
            self.VirusInfo._deserialize(params.get("VirusInfo"))
        if params.get("VulInfo") is not None:
            self.VulInfo = VulInfo()
            self.VulInfo._deserialize(params.get("VulInfo"))
        if params.get("AdInfo") is not None:
            self.AdInfo = AdInfo()
            self.AdInfo._deserialize(params.get("AdInfo"))
        self.TaskTime = params.get("TaskTime")
        self.StatusCode = params.get("StatusCode")
        self.StatusDesc = params.get("StatusDesc")
        self.StatusRef = params.get("StatusRef")
        if params.get("PermissionInfo") is not None:
            self.PermissionInfo = ScanPermissionList()
            self.PermissionInfo._deserialize(params.get("PermissionInfo"))
        if params.get("SensitiveInfo") is not None:
            self.SensitiveInfo = ScanSensitiveList()
            self.SensitiveInfo._deserialize(params.get("SensitiveInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    """提交app加固的服务信息

    """

    def __init__(self):
        """
        :param ServiceEdition: 服务版本，基础版basic，专业版professional，企业版enterprise。\n        :type ServiceEdition: str\n        :param CallbackUrl: 任务处理完成后的反向通知回调地址，如果不需要通知请传递空字符串。通知为POST请求，post包体数据示例{"Response":{"ItemId":"4cdad8fb86f036b06bccb3f58971c306","ShieldCode":0,"ShieldMd5":"78701576793c4a5f04e1c9660de0aa0b","ShieldSize":11997354,"TaskStatus":1,"TaskTime":1539148141}}，调用方需要返回如下信息，{"Result":"ok","Reason":"xxxxx"}，如果Result字段值不等于ok会继续回调。\n        :type CallbackUrl: str\n        :param SubmitSource: 提交来源 YYB-应用宝 RDM-rdm MC-控制台 MAC_TOOL-mac工具 WIN_TOOL-window工具。\n        :type SubmitSource: str\n        :param PlanId: 加固策略编号，如果不传则使用系统默认加固策略。如果指定的plan不存在会返回错误。\n        :type PlanId: int\n        """
        self.ServiceEdition = None
        self.CallbackUrl = None
        self.SubmitSource = None
        self.PlanId = None


    def _deserialize(self, params):
        self.ServiceEdition = params.get("ServiceEdition")
        self.CallbackUrl = params.get("CallbackUrl")
        self.SubmitSource = params.get("SubmitSource")
        self.PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShieldInfo(AbstractModel):
    """加固后app的信息

    """

    def __init__(self):
        """
        :param ShieldCode: 加固结果的返回码\n        :type ShieldCode: int\n        :param ShieldSize: 加固后app的大小\n        :type ShieldSize: int\n        :param ShieldMd5: 加固后app的md5\n        :type ShieldMd5: str\n        :param AppUrl: 加固后的APP下载地址，该地址有效期为20分钟，请及时下载\n        :type AppUrl: str\n        :param TaskTime: 加固的提交时间\n        :type TaskTime: int\n        :param ItemId: 任务唯一标识\n        :type ItemId: str\n        :param ServiceEdition: 加固版本，basic基础版，professional专业版，enterprise企业版\n        :type ServiceEdition: str\n        """
        self.ShieldCode = None
        self.ShieldSize = None
        self.ShieldMd5 = None
        self.AppUrl = None
        self.TaskTime = None
        self.ItemId = None
        self.ServiceEdition = None


    def _deserialize(self, params):
        self.ShieldCode = params.get("ShieldCode")
        self.ShieldSize = params.get("ShieldSize")
        self.ShieldMd5 = params.get("ShieldMd5")
        self.AppUrl = params.get("AppUrl")
        self.TaskTime = params.get("TaskTime")
        self.ItemId = params.get("ItemId")
        self.ServiceEdition = params.get("ServiceEdition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShieldPlanInfo(AbstractModel):
    """加固策略信息

    """

    def __init__(self):
        """
        :param TotalCount: 加固策略数量\n        :type TotalCount: int\n        :param PlanSet: 加固策略具体信息数组\n        :type PlanSet: list of PlanDetailInfo\n        """
        self.TotalCount = None
        self.PlanSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PlanSet") is not None:
            self.PlanSet = []
            for item in params.get("PlanSet"):
                obj = PlanDetailInfo()
                obj._deserialize(item)
                self.PlanSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoInfo(AbstractModel):
    """so加固信息

    """

    def __init__(self):
        """
        :param SoFileNames: so文件列表\n        :type SoFileNames: list of str\n        """
        self.SoFileNames = None


    def _deserialize(self, params):
        self.SoFileNames = params.get("SoFileNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirusInfo(AbstractModel):
    """病毒信息

    """

    def __init__(self):
        """
        :param SafeType: 软件安全类型，分别为0-未知、 1-安全软件、2-风险软件、3-病毒软件\n        :type SafeType: int\n        :param VirusName: 病毒名称， utf8编码，非病毒时值为空\n        :type VirusName: str\n        :param VirusDesc: 病毒描述，utf8编码，非病毒时值为空\n        :type VirusDesc: str\n        """
        self.SafeType = None
        self.VirusName = None
        self.VirusDesc = None


    def _deserialize(self, params):
        self.SafeType = params.get("SafeType")
        self.VirusName = params.get("VirusName")
        self.VirusDesc = params.get("VirusDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulInfo(AbstractModel):
    """漏洞信息

    """

    def __init__(self):
        """
        :param VulList: 漏洞列表\n        :type VulList: list of VulList\n        :param VulFileScore: 漏洞文件评分\n        :type VulFileScore: int\n        """
        self.VulList = None
        self.VulFileScore = None


    def _deserialize(self, params):
        if params.get("VulList") is not None:
            self.VulList = []
            for item in params.get("VulList"):
                obj = VulList()
                obj._deserialize(item)
                self.VulList.append(obj)
        self.VulFileScore = params.get("VulFileScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulList(AbstractModel):
    """漏洞信息

    """

    def __init__(self):
        """
        :param VulId: 漏洞id\n        :type VulId: str\n        :param VulName: 漏洞名称\n        :type VulName: str\n        :param VulCode: 漏洞代码\n        :type VulCode: str\n        :param VulDesc: 漏洞描述\n        :type VulDesc: str\n        :param VulSolution: 漏洞解决方案\n        :type VulSolution: str\n        :param VulSrcType: 漏洞来源类别，0默认自身，1第三方插件\n        :type VulSrcType: int\n        :param VulFilepath: 漏洞位置\n        :type VulFilepath: str\n        :param RiskLevel: 风险级别：1 低风险 ；2中等风险；3 高风险\n        :type RiskLevel: int\n        """
        self.VulId = None
        self.VulName = None
        self.VulCode = None
        self.VulDesc = None
        self.VulSolution = None
        self.VulSrcType = None
        self.VulFilepath = None
        self.RiskLevel = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulCode = params.get("VulCode")
        self.VulDesc = params.get("VulDesc")
        self.VulSolution = params.get("VulSolution")
        self.VulSrcType = params.get("VulSrcType")
        self.VulFilepath = params.get("VulFilepath")
        self.RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        