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


class CreateLogExportRequest(AbstractModel):
    """CreateLogExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目ID
        :type ID: int
        :param StartTime: 日志导出起始时间
        :type StartTime: str
        :param EndTime: 日志导出结束时间
        :type EndTime: str
        :param Query: 日志导出检索语句
        :type Query: str
        :param Count: 日志导出数量, 最大值1000万
        :type Count: int
        :param Order: 日志导出时间排序。desc，asc，默认为desc
        :type Order: str
        :param Format: 日志导出数据格式。json，csv，默认为json
        :type Format: str
        """
        self.ID = None
        self.StartTime = None
        self.EndTime = None
        self.Query = None
        self.Count = None
        self.Order = None
        self.Format = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Query = params.get("Query")
        self.Count = params.get("Count")
        self.Order = params.get("Order")
        self.Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogExportResponse(AbstractModel):
    """CreateLogExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param ExportID: 日志导出ID
        :type ExportID: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExportID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExportID = params.get("ExportID")
        self.RequestId = params.get("RequestId")


class CreateOfflineLogConfigRequest(AbstractModel):
    """CreateOfflineLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectKey: 项目唯一上报 key
        :type ProjectKey: str
        :param UniqueID: 需要监听的用户唯一标示(aid 或 uin)
        :type UniqueID: str
        """
        self.ProjectKey = None
        self.UniqueID = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.UniqueID = params.get("UniqueID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOfflineLogConfigResponse(AbstractModel):
    """CreateOfflineLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 创建的项目名(不为空且最长为 200)
        :type Name: str
        :param InstanceID: 业务系统 ID
        :type InstanceID: str
        :param Rate: 项目抽样率(大于等于 0)
        :type Rate: str
        :param EnableURLGroup: 是否开启聚类
        :type EnableURLGroup: int
        :param Type: 项目类型("web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param Repo: 项目对应仓库地址(可选，最长为 256)
        :type Repo: str
        :param URL: 项目对应网页地址(可选，最长为 256)
        :type URL: str
        :param Desc: 创建的项目描述(可选，最长为 1000)
        :type Desc: str
        """
        self.Name = None
        self.InstanceID = None
        self.Rate = None
        self.EnableURLGroup = None
        self.Type = None
        self.Repo = None
        self.URL = None
        self.Desc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.InstanceID = params.get("InstanceID")
        self.Rate = params.get("Rate")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.Type = params.get("Type")
        self.Repo = params.get("Repo")
        self.URL = params.get("URL")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目 id
        :type ID: int
        :param Key: 项目唯一key
        :type Key: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.Key = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Key = params.get("Key")
        self.RequestId = params.get("RequestId")


class CreateReleaseFileRequest(AbstractModel):
    """CreateReleaseFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectID: 项目 id
        :type ProjectID: int
        :param Files: 文件信息列表
        :type Files: list of ReleaseFile
        """
        self.ProjectID = None
        self.Files = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self.Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseFileResponse(AbstractModel):
    """CreateReleaseFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 调用结果
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class CreateStarProjectRequest(AbstractModel):
    """CreateStarProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param ID: 项目ID
        :type ID: int
        """
        self.InstanceID = None
        self.ID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStarProjectResponse(AbstractModel):
    """CreateStarProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口返回信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class CreateTawInstanceRequest(AbstractModel):
    """CreateTawInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param AreaId: 片区Id，(至少大于0)
        :type AreaId: int
        :param ChargeType: 计费类型, (1=后付费)
        :type ChargeType: int
        :param DataRetentionDays: 数据保存时间，(至少大于0)
        :type DataRetentionDays: int
        :param InstanceName: 实例名称，(最大长度不超过255字节)
        :type InstanceName: str
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param InstanceDesc: 实例描述，(最大长度不超过1024字节)
        :type InstanceDesc: str
        :param CountNum: 每天数据上报量
        :type CountNum: str
        :param PeriodRetain: 数据存储时长计费
        :type PeriodRetain: str
        :param BuyingChannel: 实例购买渠道("cdn" 等)
        :type BuyingChannel: str
        :param ResourcePackageType: 预付费资源包类型(仅预付费需要)
        :type ResourcePackageType: int
        :param ResourcePackageNum: 预付费资源包数量(仅预付费需要)
        :type ResourcePackageNum: int
        """
        self.AreaId = None
        self.ChargeType = None
        self.DataRetentionDays = None
        self.InstanceName = None
        self.Tags = None
        self.InstanceDesc = None
        self.CountNum = None
        self.PeriodRetain = None
        self.BuyingChannel = None
        self.ResourcePackageType = None
        self.ResourcePackageNum = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.ChargeType = params.get("ChargeType")
        self.DataRetentionDays = params.get("DataRetentionDays")
        self.InstanceName = params.get("InstanceName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceDesc = params.get("InstanceDesc")
        self.CountNum = params.get("CountNum")
        self.PeriodRetain = params.get("PeriodRetain")
        self.BuyingChannel = params.get("BuyingChannel")
        self.ResourcePackageType = params.get("ResourcePackageType")
        self.ResourcePackageNum = params.get("ResourcePackageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTawInstanceResponse(AbstractModel):
    """CreateTawInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param DealName: 预付费订单 id
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class CreateWhitelistRequest(AbstractModel):
    """CreateWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param Remark: 备注
        :type Remark: str
        :param WhitelistUin: uin：业务方标识
        :type WhitelistUin: str
        :param Aid: 业务方标识
        :type Aid: str
        """
        self.InstanceID = None
        self.Remark = None
        self.WhitelistUin = None
        self.Aid = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.Remark = params.get("Remark")
        self.WhitelistUin = params.get("WhitelistUin")
        self.Aid = params.get("Aid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhitelistResponse(AbstractModel):
    """CreateWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 消息
        :type Msg: str
        :param ID: 白名单ID
        :type ID: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.ID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.ID = params.get("ID")
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 需要删除的实例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLogExportRequest(AbstractModel):
    """DeleteLogExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目ID
        :type ID: int
        :param ExportID: 日志导出ID
        :type ExportID: str
        """
        self.ID = None
        self.ExportID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ExportID = params.get("ExportID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogExportResponse(AbstractModel):
    """DeleteLogExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 是否成功，成功则为success；失败则直接返回Error，不返回该参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteOfflineLogConfigRequest(AbstractModel):
    """DeleteOfflineLogConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectKey: 项目唯一上报 key
        :type ProjectKey: str
        :param UniqueID: 用户唯一标示(uin or aid)
        :type UniqueID: str
        """
        self.ProjectKey = None
        self.UniqueID = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.UniqueID = params.get("UniqueID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOfflineLogConfigResponse(AbstractModel):
    """DeleteOfflineLogConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口调用信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteOfflineLogRecordRequest(AbstractModel):
    """DeleteOfflineLogRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectKey: 项目唯一上报 key
        :type ProjectKey: str
        :param FileID: 离线日志文件 id
        :type FileID: str
        """
        self.ProjectKey = None
        self.FileID = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.FileID = params.get("FileID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOfflineLogRecordResponse(AbstractModel):
    """DeleteOfflineLogRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口调用信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 需要删除的项目 ID
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 操作信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteReleaseFileRequest(AbstractModel):
    """DeleteReleaseFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 文件 id
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReleaseFileResponse(AbstractModel):
    """DeleteReleaseFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口请求返回字符串
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteStarProjectRequest(AbstractModel):
    """DeleteStarProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param ID: 项目ID
        :type ID: int
        """
        self.InstanceID = None
        self.ID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStarProjectResponse(AbstractModel):
    """DeleteStarProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DeleteWhitelistRequest(AbstractModel):
    """DeleteWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceID: 实例ID
        :type InstanceID: str
        :param ID: 名单ID
        :type ID: str
        """
        self.InstanceID = None
        self.ID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhitelistResponse(AbstractModel):
    """DeleteWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 消息success
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeDataCustomUrlRequest(AbstractModel):
    """DescribeDataCustomUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: top：资源top视图，allcount：性能视图，day：14天数据，condition：条件列表，pagepv：性能视图，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 自定义测速的key的值
        :type Url: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataCustomUrlResponse(AbstractModel):
    """DescribeDataCustomUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataEventUrlRequest(AbstractModel):
    """DescribeDataEventUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: allcount：性能视图，day：14天数据，condition：条件列表，ckuv：获取uv趋势，ckpv：获取pv趋势，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param Name: 筛选条件
        :type Name: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Name = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Name = params.get("Name")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEventUrlResponse(AbstractModel):
    """DescribeDataEventUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataFetchProjectRequest(AbstractModel):
    """DescribeDataFetchProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 来源
        :type Url: str
        :param Env: 环境
        :type Env: str
        :param Status: httpcode响应码
        :type Status: str
        :param Ret: retcode
        :type Ret: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None
        self.Status = None
        self.Ret = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        self.Status = params.get("Status")
        self.Ret = params.get("Ret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchProjectResponse(AbstractModel):
    """DescribeDataFetchProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataFetchUrlInfoRequest(AbstractModel):
    """DescribeDataFetchUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: 类型
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 来源
        :type Url: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlInfoResponse(AbstractModel):
    """DescribeDataFetchUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataFetchUrlRequest(AbstractModel):
    """DescribeDataFetchUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: allcount：性能视图，day：14天数据，count40x：40X视图，count50x：50X视图，count5xand4x：40∑50视图，top：资源top视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 来源
        :type Url: str
        :param Env: 环境
        :type Env: str
        :param Status: httpcode响应码
        :type Status: str
        :param Ret: retcode
        :type Ret: str
        :param NetStatus: 网络状态
        :type NetStatus: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None
        self.Status = None
        self.Ret = None
        self.NetStatus = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        self.Status = params.get("Status")
        self.Ret = params.get("Ret")
        self.NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlResponse(AbstractModel):
    """DescribeDataFetchUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataLogUrlInfoRequest(AbstractModel):
    """DescribeDataLogUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目ID
        :type ID: int
        :param StartTime: 时间戳
        :type StartTime: int
        :param EndTime: 时间戳
        :type EndTime: int
        """
        self.ID = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlInfoResponse(AbstractModel):
    """DescribeDataLogUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataLogUrlStatisticsRequest(AbstractModel):
    """DescribeDataLogUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: analysis：异常分析，compare：异常列表对比，allcount：性能视图，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param Env: 环境区分
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlStatisticsResponse(AbstractModel):
    """DescribeDataLogUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPerformancePageRequest(AbstractModel):
    """DescribeDataPerformancePage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目ID
        :type ID: int
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        :param Type: pagepv：性能视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param Level: 日志等级
        :type Level: str
        :param Isp: 运营商
        :type Isp: str
        :param Area: 地区
        :type Area: str
        :param NetType: 网络类型
        :type NetType: str
        :param Platform: 平台
        :type Platform: str
        :param Device: 机型
        :type Device: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Browser: 浏览器
        :type Browser: str
        :param Os: 操作系统
        :type Os: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Brand: 品牌
        :type Brand: str
        :param From: 来源页面
        :type From: str
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Env: 环境变量
        :type Env: str
        :param NetStatus: 网络状态
        :type NetStatus: str
        """
        self.ID = None
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.Level = None
        self.Isp = None
        self.Area = None
        self.NetType = None
        self.Platform = None
        self.Device = None
        self.VersionNum = None
        self.ExtFirst = None
        self.ExtSecond = None
        self.ExtThird = None
        self.IsAbroad = None
        self.Browser = None
        self.Os = None
        self.Engine = None
        self.Brand = None
        self.From = None
        self.CostType = None
        self.Env = None
        self.NetStatus = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.Level = params.get("Level")
        self.Isp = params.get("Isp")
        self.Area = params.get("Area")
        self.NetType = params.get("NetType")
        self.Platform = params.get("Platform")
        self.Device = params.get("Device")
        self.VersionNum = params.get("VersionNum")
        self.ExtFirst = params.get("ExtFirst")
        self.ExtSecond = params.get("ExtSecond")
        self.ExtThird = params.get("ExtThird")
        self.IsAbroad = params.get("IsAbroad")
        self.Browser = params.get("Browser")
        self.Os = params.get("Os")
        self.Engine = params.get("Engine")
        self.Brand = params.get("Brand")
        self.From = params.get("From")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        self.NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformancePageResponse(AbstractModel):
    """DescribeDataPerformancePage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPerformanceProjectRequest(AbstractModel):
    """DescribeDataPerformanceProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，condition：条件列表，area：请求速度分布，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算
        :type CostType: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformanceProjectResponse(AbstractModel):
    """DescribeDataPerformanceProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPvUrlInfoRequest(AbstractModel):
    """DescribeDataPvUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: 类型
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlInfoResponse(AbstractModel):
    """DescribeDataPvUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataPvUrlStatisticsRequest(AbstractModel):
    """DescribeDataPvUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: allcount：性能视图，day：14天数据，vp：性能，ckuv：uv，ckpv：pv，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlStatisticsResponse(AbstractModel):
    """DescribeDataPvUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataReportCountRequest(AbstractModel):
    """DescribeDataReportCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ReportType: 上报类型
        :type ReportType: str
        :param InstanceID: 实例ID
        :type InstanceID: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ID = None
        self.ReportType = None
        self.InstanceID = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ReportType = params.get("ReportType")
        self.InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataReportCountResponse(AbstractModel):
    """DescribeDataReportCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    """DescribeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param Query: 查询字符串
        :type Query: str
        :param ID: 项目ID
        :type ID: int
        """
        self.Query = None
        self.ID = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataSetUrlStatisticsRequest(AbstractModel):
    """DescribeDataSetUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: allcount：性能视图，data：小程序，component：小程序相关，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算
        :type CostType: str
        :param Env: 环境
        :type Env: str
        :param PackageType: 获取package
        :type PackageType: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Env = None
        self.PackageType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        self.PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSetUrlStatisticsResponse(AbstractModel):
    """DescribeDataSetUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataStaticProjectRequest(AbstractModel):
    """DescribeDataStaticProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算
        :type CostType: str
        :param Url: 来源
        :type Url: list of str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticProjectResponse(AbstractModel):
    """DescribeDataStaticProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataStaticResourceRequest(AbstractModel):
    """DescribeDataStaticResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: top：资源top视图，count40x：40X视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 来源
        :type Url: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticResourceResponse(AbstractModel):
    """DescribeDataStaticResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataStaticUrlRequest(AbstractModel):
    """DescribeDataStaticUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param Type: pagepv：性能视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :type Type: str
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算方式
        :type CostType: str
        :param Url: 来源
        :type Url: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.Type = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Url = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Url = params.get("Url")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticUrlResponse(AbstractModel):
    """DescribeDataStaticUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeDataWebVitalsPageRequest(AbstractModel):
    """DescribeDataWebVitalsPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        :param ID: 项目ID
        :type ID: int
        :param ExtSecond: 自定义2
        :type ExtSecond: str
        :param Engine: 浏览器引擎
        :type Engine: str
        :param Isp: 运营商
        :type Isp: str
        :param From: 来源页面
        :type From: str
        :param Level: 日志等级
        :type Level: str
        :param Type: 类型暂无
        :type Type: str
        :param Brand: 品牌
        :type Brand: str
        :param Area: 地区
        :type Area: str
        :param VersionNum: 版本
        :type VersionNum: str
        :param Platform: 平台
        :type Platform: str
        :param ExtThird: 自定义3
        :type ExtThird: str
        :param ExtFirst: 自定义1
        :type ExtFirst: str
        :param NetType: 网络类型
        :type NetType: str
        :param Device: 机型
        :type Device: str
        :param IsAbroad: 是否海外
        :type IsAbroad: str
        :param Os: 操作系统
        :type Os: str
        :param Browser: 浏览器
        :type Browser: str
        :param CostType: 耗时计算
        :type CostType: str
        :param Env: 环境
        :type Env: str
        """
        self.StartTime = None
        self.EndTime = None
        self.ID = None
        self.ExtSecond = None
        self.Engine = None
        self.Isp = None
        self.From = None
        self.Level = None
        self.Type = None
        self.Brand = None
        self.Area = None
        self.VersionNum = None
        self.Platform = None
        self.ExtThird = None
        self.ExtFirst = None
        self.NetType = None
        self.Device = None
        self.IsAbroad = None
        self.Os = None
        self.Browser = None
        self.CostType = None
        self.Env = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.ExtSecond = params.get("ExtSecond")
        self.Engine = params.get("Engine")
        self.Isp = params.get("Isp")
        self.From = params.get("From")
        self.Level = params.get("Level")
        self.Type = params.get("Type")
        self.Brand = params.get("Brand")
        self.Area = params.get("Area")
        self.VersionNum = params.get("VersionNum")
        self.Platform = params.get("Platform")
        self.ExtThird = params.get("ExtThird")
        self.ExtFirst = params.get("ExtFirst")
        self.NetType = params.get("NetType")
        self.Device = params.get("Device")
        self.IsAbroad = params.get("IsAbroad")
        self.Os = params.get("Os")
        self.Browser = params.get("Browser")
        self.CostType = params.get("CostType")
        self.Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataWebVitalsPageResponse(AbstractModel):
    """DescribeDataWebVitalsPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回值
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeErrorRequest(AbstractModel):
    """DescribeError请求参数结构体

    """

    def __init__(self):
        r"""
        :param Date: 日期
        :type Date: str
        :param ID: 项目ID
        :type ID: int
        """
        self.Date = None
        self.ID = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorResponse(AbstractModel):
    """DescribeError返回参数结构体

    """

    def __init__(self):
        r"""
        :param Content: 内容
        :type Content: str
        :param ID: 项目ID
        :type ID: int
        :param CreateTime: 时间
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.ID = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.ID = params.get("ID")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DescribeLogExportsRequest(AbstractModel):
    """DescribeLogExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目ID
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogExportsResponse(AbstractModel):
    """DescribeLogExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogExportSet: 日志导出记录列表
        :type LogExportSet: list of LogExport
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogExportSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogExportSet") is not None:
            self.LogExportSet = []
            for item in params.get("LogExportSet"):
                obj = LogExport()
                obj._deserialize(item)
                self.LogExportSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogListRequest(AbstractModel):
    """DescribeLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sort: 排序方式  desc  asc（必填）
        :type Sort: str
        :param ActionType: searchlog  histogram（必填）
        :type ActionType: str
        :param ID: 项目ID（必填）
        :type ID: int
        :param StartTime: 开始时间（必填）
        :type StartTime: str
        :param Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param Context: 上下文，加载更多日志时使用，透传上次返回的 Context 值，获取后续的日志内容，总计最多可获取1万条原始日志。过期时间1小时
        :type Context: str
        :param Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）例："id:120001 AND type:\"log\""
        :type Query: str
        :param EndTime: 结束时间（必填）
        :type EndTime: str
        """
        self.Sort = None
        self.ActionType = None
        self.ID = None
        self.StartTime = None
        self.Limit = None
        self.Context = None
        self.Query = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Sort = params.get("Sort")
        self.ActionType = params.get("ActionType")
        self.ID = params.get("ID")
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogListResponse(AbstractModel):
    """DescribeLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeOfflineLogConfigsRequest(AbstractModel):
    """DescribeOfflineLogConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectKey: 项目唯一上报 key
        :type ProjectKey: str
        """
        self.ProjectKey = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogConfigsResponse(AbstractModel):
    """DescribeOfflineLogConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口调用信息
        :type Msg: str
        :param UniqueIDSet: 用户唯一标示数组
        :type UniqueIDSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.UniqueIDSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.UniqueIDSet = params.get("UniqueIDSet")
        self.RequestId = params.get("RequestId")


class DescribeOfflineLogRecordsRequest(AbstractModel):
    """DescribeOfflineLogRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectKey: 项目唯一上报 key
        :type ProjectKey: str
        """
        self.ProjectKey = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogRecordsResponse(AbstractModel):
    """DescribeOfflineLogRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口调用信息
        :type Msg: str
        :param RecordSet: 记录 ID 数组
        :type RecordSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RecordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RecordSet = params.get("RecordSet")
        self.RequestId = params.get("RequestId")


class DescribeOfflineLogsRequest(AbstractModel):
    """DescribeOfflineLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectKey: 项目唯一上报 key
        :type ProjectKey: str
        :param FileIDs: 离线日志文件 id 列表
        :type FileIDs: list of str
        """
        self.ProjectKey = None
        self.FileIDs = None


    def _deserialize(self, params):
        self.ProjectKey = params.get("ProjectKey")
        self.FileIDs = params.get("FileIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogsResponse(AbstractModel):
    """DescribeOfflineLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 接口调用返回信息
        :type Msg: str
        :param LogSet: 日志列表
        :type LogSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.LogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.LogSet = params.get("LogSet")
        self.RequestId = params.get("RequestId")


class DescribeProjectLimitsRequest(AbstractModel):
    """DescribeProjectLimits请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectID: 项目ID
        :type ProjectID: int
        """
        self.ProjectID = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectLimitsResponse(AbstractModel):
    """DescribeProjectLimits返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectLimitSet: 上报率数组列表
        :type ProjectLimitSet: list of ProjectLimit
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectLimitSet") is not None:
            self.ProjectLimitSet = []
            for item in params.get("ProjectLimitSet"):
                obj = ProjectLimit()
                obj._deserialize(item)
                self.ProjectLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页每页数目，整型
        :type Limit: int
        :param Offset: 分页页码，整型
        :type Offset: int
        :param Filters: 过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :type Filters: list of Filter
        :param IsDemo: 该参数已废弃，demo模式请在Filters内注明
        :type IsDemo: int
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.IsDemo = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 列表总数
        :type TotalCount: int
        :param ProjectSet: 项目列表
        :type ProjectSet: list of RumProject
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProjectSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProjectSet") is not None:
            self.ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = RumProject()
                obj._deserialize(item)
                self.ProjectSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePvListRequest(AbstractModel):
    """DescribePvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: ID
        :type ProjectId: int
        :param EndTime: 结束时间
        :type EndTime: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param Dimension: 获取day：d，   获取min则不填
        :type Dimension: str
        """
        self.ProjectId = None
        self.EndTime = None
        self.StartTime = None
        self.Dimension = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePvListResponse(AbstractModel):
    """DescribePvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectPvSet: pv列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectPvSet: list of RumPvInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectPvSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectPvSet") is not None:
            self.ProjectPvSet = []
            for item in params.get("ProjectPvSet"):
                obj = RumPvInfo()
                obj._deserialize(item)
                self.ProjectPvSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReleaseFileSignRequest(AbstractModel):
    """DescribeReleaseFileSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param Timeout: 超时时间，不填默认是 5 分钟
        :type Timeout: int
        """
        self.Timeout = None


    def _deserialize(self, params):
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFileSignResponse(AbstractModel):
    """DescribeReleaseFileSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param SecretKey: 临时密钥key
        :type SecretKey: str
        :param SecretID: 临时密钥 id
        :type SecretID: str
        :param SessionToken: 临时密钥临时 token
        :type SessionToken: str
        :param StartTime: 开始时间戳
        :type StartTime: int
        :param ExpiredTime: 过期时间戳
        :type ExpiredTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretKey = None
        self.SecretID = None
        self.SessionToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SecretID = params.get("SecretID")
        self.SessionToken = params.get("SessionToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class DescribeReleaseFilesRequest(AbstractModel):
    """DescribeReleaseFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectID: 项目 id
        :type ProjectID: int
        :param FileVersion: 文件版本
        :type FileVersion: str
        """
        self.ProjectID = None
        self.FileVersion = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        self.FileVersion = params.get("FileVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFilesResponse(AbstractModel):
    """DescribeReleaseFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param Files: 文件信息列表
        :type Files: list of ReleaseFile
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Files = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self.Files.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRumGroupLogRequest(AbstractModel):
    """DescribeRumGroupLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param OrderBy: 排序方式  desc  asc（必填）
        :type OrderBy: str
        :param StartTime: 开始时间（必填）
        :type StartTime: str
        :param Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param Page: 页数，第几页
        :type Page: int
        :param Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param EndTime: 结束时间（必填）
        :type EndTime: str
        :param ID: 项目ID（必填）
        :type ID: int
        :param GroupField: 聚合字段
        :type GroupField: str
        """
        self.OrderBy = None
        self.StartTime = None
        self.Limit = None
        self.Page = None
        self.Query = None
        self.EndTime = None
        self.ID = None
        self.GroupField = None


    def _deserialize(self, params):
        self.OrderBy = params.get("OrderBy")
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Page = params.get("Page")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.GroupField = params.get("GroupField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumGroupLogResponse(AbstractModel):
    """DescribeRumGroupLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeRumLogExportRequest(AbstractModel):
    """DescribeRumLogExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 导出标识name
        :type Name: str
        :param StartTime: 开始时间（必填）
        :type StartTime: str
        :param Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param EndTime: 结束时间（必填）
        :type EndTime: str
        :param ID: 项目ID（必填）
        :type ID: int
        :param Fields: field条件
        :type Fields: list of str
        """
        self.Name = None
        self.StartTime = None
        self.Query = None
        self.EndTime = None
        self.ID = None
        self.Fields = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.StartTime = params.get("StartTime")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        self.Fields = params.get("Fields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportResponse(AbstractModel):
    """DescribeRumLogExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeRumLogExportsRequest(AbstractModel):
    """DescribeRumLogExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 页面大小
        :type PageSize: int
        :param PageNum: 页数，第几页
        :type PageNum: int
        :param ID: 项目ID（必填）
        :type ID: int
        """
        self.PageSize = None
        self.PageNum = None
        self.ID = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportsResponse(AbstractModel):
    """DescribeRumLogExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeRumLogListRequest(AbstractModel):
    """DescribeRumLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param OrderBy: 排序方式  desc  asc（必填）
        :type OrderBy: str
        :param StartTime: 开始时间（必填）格式为时间戳 毫秒
        :type StartTime: str
        :param Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param Page: 页数，第几页
        :type Page: int
        :param Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param EndTime: 结束时间（必填）格式为时间戳 毫秒
        :type EndTime: str
        :param ID: 项目ID（必填）
        :type ID: int
        """
        self.OrderBy = None
        self.StartTime = None
        self.Limit = None
        self.Page = None
        self.Query = None
        self.EndTime = None
        self.ID = None


    def _deserialize(self, params):
        self.OrderBy = params.get("OrderBy")
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Page = params.get("Page")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogListResponse(AbstractModel):
    """DescribeRumLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeRumStatsLogListRequest(AbstractModel):
    """DescribeRumStatsLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 开始时间（必填）
        :type StartTime: str
        :param Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param EndTime: 结束时间（必填）
        :type EndTime: str
        :param ID: 项目ID（必填）
        :type ID: int
        """
        self.StartTime = None
        self.Limit = None
        self.Query = None
        self.EndTime = None
        self.ID = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.Limit = params.get("Limit")
        self.Query = params.get("Query")
        self.EndTime = params.get("EndTime")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumStatsLogListResponse(AbstractModel):
    """DescribeRumStatsLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回字符串
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeScoresRequest(AbstractModel):
    """DescribeScores请求参数结构体

    """

    def __init__(self):
        r"""
        :param EndTime: 结束时间
        :type EndTime: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param ID: 项目ID
        :type ID: int
        :param IsDemo: 该参数已废弃
        :type IsDemo: int
        """
        self.EndTime = None
        self.StartTime = None
        self.ID = None
        self.IsDemo = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.ID = params.get("ID")
        self.IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoresResponse(AbstractModel):
    """DescribeScores返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScoreSet: 数组
        :type ScoreSet: list of ScoreInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScoreSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScoreSet") is not None:
            self.ScoreSet = []
            for item in params.get("ScoreSet"):
                obj = ScoreInfo()
                obj._deserialize(item)
                self.ScoreSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTawAreasRequest(AbstractModel):
    """DescribeTawAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param AreaIds: 片区Id
        :type AreaIds: list of int
        :param AreaKeys: 片区Key
        :type AreaKeys: list of str
        :param Limit: 分页Limit
        :type Limit: int
        :param AreaStatuses: 片区状态(1=有效，2=无效)
        :type AreaStatuses: list of int
        :param Offset: 分页Offset
        :type Offset: int
        """
        self.AreaIds = None
        self.AreaKeys = None
        self.Limit = None
        self.AreaStatuses = None
        self.Offset = None


    def _deserialize(self, params):
        self.AreaIds = params.get("AreaIds")
        self.AreaKeys = params.get("AreaKeys")
        self.Limit = params.get("Limit")
        self.AreaStatuses = params.get("AreaStatuses")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawAreasResponse(AbstractModel):
    """DescribeTawAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 片区总数
        :type TotalCount: int
        :param AreaSet: 片区列表
        :type AreaSet: list of RumAreaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AreaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AreaSet") is not None:
            self.AreaSet = []
            for item in params.get("AreaSet"):
                obj = RumAreaInfo()
                obj._deserialize(item)
                self.AreaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTawInstancesRequest(AbstractModel):
    """DescribeTawInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChargeStatuses: 计费状态
        :type ChargeStatuses: list of int
        :param ChargeTypes: 计费类型
        :type ChargeTypes: list of int
        :param Limit: 分页Limit
        :type Limit: int
        :param Offset: 分页Offset
        :type Offset: int
        :param AreaIds: 片区Id
        :type AreaIds: list of int
        :param InstanceStatuses: 实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=销毁中，8=已销毁), 该参数已废弃，请在Filters内注明
        :type InstanceStatuses: list of int
        :param InstanceIds: 实例Id, 该参数已废弃，请在Filters内注明
        :type InstanceIds: list of str
        :param Filters: 过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :type Filters: list of Filter
        :param IsDemo: 该参数已废弃，demo模式请在Filters内注明
        :type IsDemo: int
        """
        self.ChargeStatuses = None
        self.ChargeTypes = None
        self.Limit = None
        self.Offset = None
        self.AreaIds = None
        self.InstanceStatuses = None
        self.InstanceIds = None
        self.Filters = None
        self.IsDemo = None


    def _deserialize(self, params):
        self.ChargeStatuses = params.get("ChargeStatuses")
        self.ChargeTypes = params.get("ChargeTypes")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.AreaIds = params.get("AreaIds")
        self.InstanceStatuses = params.get("InstanceStatuses")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawInstancesResponse(AbstractModel):
    """DescribeTawInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceSet: 实例列表
        :type InstanceSet: list of RumInstanceInfo
        :param TotalCount: 实例总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = RumInstanceInfo()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUvListRequest(AbstractModel):
    """DescribeUvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: ID
        :type ProjectId: int
        :param EndTime: 结束时间
        :type EndTime: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param Dimension: 获取day：d，   min:m
        :type Dimension: str
        """
        self.ProjectId = None
        self.EndTime = None
        self.StartTime = None
        self.Dimension = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUvListResponse(AbstractModel):
    """DescribeUvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectUvSet: uv列表
        :type ProjectUvSet: list of RumUvInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectUvSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProjectUvSet") is not None:
            self.ProjectUvSet = []
            for item in params.get("ProjectUvSet"):
                obj = RumUvInfo()
                obj._deserialize(item)
                self.ProjectUvSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhitelistsRequest(AbstractModel):
    """DescribeWhitelists请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceID: 实例instance-ID
        :type InstanceID: str
        """
        self.InstanceID = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhitelistsResponse(AbstractModel):
    """DescribeWhitelists返回参数结构体

    """

    def __init__(self):
        r"""
        :param WhitelistSet: 白名单列表
        :type WhitelistSet: list of Whitelist
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WhitelistSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WhitelistSet") is not None:
            self.WhitelistSet = []
            for item in params.get("WhitelistSet"):
                obj = Whitelist()
                obj._deserialize(item)
                self.WhitelistSet.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    · 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    · 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param Name: 过滤键的名称。
        :type Name: str
        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogExport(AbstractModel):
    """日志导出记录

    """

    def __init__(self):
        r"""
        :param CosPath: 日志导出路径
        :type CosPath: str
        :param Count: 日志导出数量
        :type Count: int
        :param CreateTime: 日志导出任务创建时间
        :type CreateTime: str
        :param ExportID: 日志导出任务ID
        :type ExportID: str
        :param FileName: 日志导出文件名
        :type FileName: str
        :param FileSize: 日志文件大小
        :type FileSize: int
        :param Format: 日志导出格式
        :type Format: str
        :param Order: 日志导出时间排序
        :type Order: str
        :param Query: 日志导出查询语句
        :type Query: str
        :param StartTime: 日志导出起始时间
        :type StartTime: str
        :param EndTime: 日志导出结束时间
        :type EndTime: str
        :param Status: 日志下载状态。Queuing:导出正在排队中，Processing:导出正在进行中，Complete:导出完成，Failed:导出失败，Expired:日志导出已过期（三天有效期）。
        :type Status: str
        """
        self.CosPath = None
        self.Count = None
        self.CreateTime = None
        self.ExportID = None
        self.FileName = None
        self.FileSize = None
        self.Format = None
        self.Order = None
        self.Query = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.CosPath = params.get("CosPath")
        self.Count = params.get("Count")
        self.CreateTime = params.get("CreateTime")
        self.ExportID = params.get("ExportID")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.Format = params.get("Format")
        self.Order = params.get("Order")
        self.Query = params.get("Query")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 要修改的实例id
        :type InstanceId: str
        :param InstanceName: 新的实例名称(长度最大不超过255)
        :type InstanceName: str
        :param InstanceDesc: 新的实例描述(长度最大不超过1024)
        :type InstanceDesc: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceDesc = params.get("InstanceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectLimitRequest(AbstractModel):
    """ModifyProjectLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectID: 项目ID
        :type ProjectID: int
        :param ProjectInterface: 项目接口
        :type ProjectInterface: str
        :param ReportRate: 上报比例   10代表10%
        :type ReportRate: int
        :param ReportType: 上报类型 1：比例  2：上报量
        :type ReportType: int
        :param ID: 主键ID
        :type ID: int
        """
        self.ProjectID = None
        self.ProjectInterface = None
        self.ReportRate = None
        self.ReportType = None
        self.ID = None


    def _deserialize(self, params):
        self.ProjectID = params.get("ProjectID")
        self.ProjectInterface = params.get("ProjectInterface")
        self.ReportRate = params.get("ReportRate")
        self.ReportType = params.get("ReportType")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectLimitResponse(AbstractModel):
    """ModifyProjectLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 项目 id
        :type ID: int
        :param Name: 项目名(可选，不为空且最长为 200)
        :type Name: str
        :param URL: 项目网页地址(可选，最长为 256)
        :type URL: str
        :param Repo: 项目仓库地址(可选，最长为 256)
        :type Repo: str
        :param InstanceID: 项目需要转移到的实例 id(可选)
        :type InstanceID: str
        :param Rate: 项目采样率(可选)
        :type Rate: str
        :param EnableURLGroup: 是否开启聚类(可选)
        :type EnableURLGroup: int
        :param Type: 项目类型(可接受值为 "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param Desc: 项目描述(可选，最长为 1000)
        :type Desc: str
        """
        self.ID = None
        self.Name = None
        self.URL = None
        self.Repo = None
        self.InstanceID = None
        self.Rate = None
        self.EnableURLGroup = None
        self.Type = None
        self.Desc = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.URL = params.get("URL")
        self.Repo = params.get("Repo")
        self.InstanceID = params.get("InstanceID")
        self.Rate = params.get("Rate")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.Type = params.get("Type")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 操作信息
        :type Msg: str
        :param ID: 项目id
        :type ID: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.ID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.ID = params.get("ID")
        self.RequestId = params.get("RequestId")


class ProjectLimit(AbstractModel):
    """项目接口限制类型

    """

    def __init__(self):
        r"""
        :param ProjectInterface: 接口
        :type ProjectInterface: str
        :param ReportRate: 上报率
        :type ReportRate: int
        :param ReportType: 上报类型 1：上报率  2：上报量限制
        :type ReportType: int
        :param ID: 主键ID
        :type ID: int
        :param ProjectID: 项目ID
        :type ProjectID: int
        """
        self.ProjectInterface = None
        self.ReportRate = None
        self.ReportType = None
        self.ID = None
        self.ProjectID = None


    def _deserialize(self, params):
        self.ProjectInterface = params.get("ProjectInterface")
        self.ReportRate = params.get("ReportRate")
        self.ReportType = params.get("ReportType")
        self.ID = params.get("ID")
        self.ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseFile(AbstractModel):
    """发布文件列表(SOURCEMAP)

    """

    def __init__(self):
        r"""
        :param Version: 文件版本
        :type Version: str
        :param FileKey: 文件唯一 key
        :type FileKey: str
        :param FileName: 文件名
        :type FileName: str
        :param FileHash: 文件哈希值
        :type FileHash: str
        :param ID: 文件 id
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        """
        self.Version = None
        self.FileKey = None
        self.FileName = None
        self.FileHash = None
        self.ID = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.FileKey = params.get("FileKey")
        self.FileName = params.get("FileName")
        self.FileHash = params.get("FileHash")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceRequest(AbstractModel):
    """ResumeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 需要恢复的实例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceResponse(AbstractModel):
    """ResumeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeProjectRequest(AbstractModel):
    """ResumeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目 id
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProjectResponse(AbstractModel):
    """ResumeProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RumAreaInfo(AbstractModel):
    """Rum片区信息

    """

    def __init__(self):
        r"""
        :param AreaId: 片区Id
        :type AreaId: int
        :param AreaStatus: 片区状态(1=有效，2=无效)
        :type AreaStatus: int
        :param AreaName: 片区名称
        :type AreaName: str
        :param AreaKey: 片区Key
        :type AreaKey: str
        :param AreaRegionID: 地域码表 id
        :type AreaRegionID: str
        :param AreaRegionCode: 地域码表 code 如 ap-xxx（xxx 为地域词）
        :type AreaRegionCode: str
        :param AreaAbbr: 地域缩写
        :type AreaAbbr: str
        """
        self.AreaId = None
        self.AreaStatus = None
        self.AreaName = None
        self.AreaKey = None
        self.AreaRegionID = None
        self.AreaRegionCode = None
        self.AreaAbbr = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.AreaStatus = params.get("AreaStatus")
        self.AreaName = params.get("AreaName")
        self.AreaKey = params.get("AreaKey")
        self.AreaRegionID = params.get("AreaRegionID")
        self.AreaRegionCode = params.get("AreaRegionCode")
        self.AreaAbbr = params.get("AreaAbbr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumInstanceInfo(AbstractModel):
    """Rum实例信息

    """

    def __init__(self):
        r"""
        :param InstanceStatus: 实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=已删除)
        :type InstanceStatus: int
        :param AreaId: 片区Id
        :type AreaId: int
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param ClusterId: 集群Id
        :type ClusterId: int
        :param InstanceDesc: 实例描述
        :type InstanceDesc: str
        :param ChargeStatus: 计费状态(1=使用中，2=已过期，3=已销毁，4=分配中，5=分配失败)
        :type ChargeStatus: int
        :param ChargeType: 计费类型(1=免费版，2=预付费，3=后付费)
        :type ChargeType: int
        :param UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param DataRetentionDays: 数据保留时间(天)
        :type DataRetentionDays: int
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        """
        self.InstanceStatus = None
        self.AreaId = None
        self.Tags = None
        self.InstanceId = None
        self.ClusterId = None
        self.InstanceDesc = None
        self.ChargeStatus = None
        self.ChargeType = None
        self.UpdatedAt = None
        self.DataRetentionDays = None
        self.InstanceName = None
        self.CreatedAt = None


    def _deserialize(self, params):
        self.InstanceStatus = params.get("InstanceStatus")
        self.AreaId = params.get("AreaId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.ClusterId = params.get("ClusterId")
        self.InstanceDesc = params.get("InstanceDesc")
        self.ChargeStatus = params.get("ChargeStatus")
        self.ChargeType = params.get("ChargeType")
        self.UpdatedAt = params.get("UpdatedAt")
        self.DataRetentionDays = params.get("DataRetentionDays")
        self.InstanceName = params.get("InstanceName")
        self.CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumProject(AbstractModel):
    """Rum 项目信息

    """

    def __init__(self):
        r"""
        :param Name: 项目名
        :type Name: str
        :param Creator: 创建者 id
        :type Creator: str
        :param InstanceID: 实例 id
        :type InstanceID: str
        :param Type: 项目类型
        :type Type: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Repo: 项目仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Repo: str
        :param URL: 项目网址地址
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param Rate: 项目采样频率
        :type Rate: str
        :param Key: 项目唯一key（长度 12 位）
        :type Key: str
        :param EnableURLGroup: 是否开启url聚类
        :type EnableURLGroup: int
        :param InstanceName: 实例名
        :type InstanceName: str
        :param ID: 项目 ID
        :type ID: int
        :param InstanceKey: 实例 key
        :type InstanceKey: str
        :param Desc: 项目描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param IsStar: 是否星标  1:是 0:否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsStar: int
        :param ProjectStatus: 项目状态(1 创建中，2 运行中，3 异常，4 重启中，5 停止中，6 已停止， 7 销毁中，8 已销毁)
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectStatus: int
        """
        self.Name = None
        self.Creator = None
        self.InstanceID = None
        self.Type = None
        self.CreateTime = None
        self.Repo = None
        self.URL = None
        self.Rate = None
        self.Key = None
        self.EnableURLGroup = None
        self.InstanceName = None
        self.ID = None
        self.InstanceKey = None
        self.Desc = None
        self.IsStar = None
        self.ProjectStatus = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Creator = params.get("Creator")
        self.InstanceID = params.get("InstanceID")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.Repo = params.get("Repo")
        self.URL = params.get("URL")
        self.Rate = params.get("Rate")
        self.Key = params.get("Key")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.InstanceName = params.get("InstanceName")
        self.ID = params.get("ID")
        self.InstanceKey = params.get("InstanceKey")
        self.Desc = params.get("Desc")
        self.IsStar = params.get("IsStar")
        self.ProjectStatus = params.get("ProjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumPvInfo(AbstractModel):
    """rum 日志对象

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Pv: pv访问量
注意：此字段可能返回 null，表示取不到有效值。
        :type Pv: str
        :param CreateTime: 时间
        :type CreateTime: str
        """
        self.ProjectId = None
        self.Pv = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Pv = params.get("Pv")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumUvInfo(AbstractModel):
    """RumUv 访问量

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Uv: uv访问量
        :type Uv: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.ProjectId = None
        self.Uv = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Uv = params.get("Uv")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreInfo(AbstractModel):
    """project Score分数实体

    """

    def __init__(self):
        r"""
        :param StaticDuration: duration
        :type StaticDuration: str
        :param PagePv: pv
        :type PagePv: str
        :param ApiFail: 失败
        :type ApiFail: str
        :param ApiNum: 请求
        :type ApiNum: str
        :param StaticFail: fail
        :type StaticFail: str
        :param ProjectID: 项目id
        :type ProjectID: int
        :param PageUv: uv
        :type PageUv: str
        :param ApiDuration: 请求次数
        :type ApiDuration: str
        :param Score: 分数
        :type Score: str
        :param PageError: error
        :type PageError: str
        :param StaticNum: num
        :type StaticNum: str
        :param RecordNum: num
        :type RecordNum: int
        :param PageDuration: Duration
        :type PageDuration: str
        :param CreateTime: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.StaticDuration = None
        self.PagePv = None
        self.ApiFail = None
        self.ApiNum = None
        self.StaticFail = None
        self.ProjectID = None
        self.PageUv = None
        self.ApiDuration = None
        self.Score = None
        self.PageError = None
        self.StaticNum = None
        self.RecordNum = None
        self.PageDuration = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.StaticDuration = params.get("StaticDuration")
        self.PagePv = params.get("PagePv")
        self.ApiFail = params.get("ApiFail")
        self.ApiNum = params.get("ApiNum")
        self.StaticFail = params.get("StaticFail")
        self.ProjectID = params.get("ProjectID")
        self.PageUv = params.get("PageUv")
        self.ApiDuration = params.get("ApiDuration")
        self.Score = params.get("Score")
        self.PageError = params.get("PageError")
        self.StaticNum = params.get("StaticNum")
        self.RecordNum = params.get("RecordNum")
        self.PageDuration = params.get("PageDuration")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceRequest(AbstractModel):
    """StopInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 需要停止的实例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceResponse(AbstractModel):
    """StopInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopProjectRequest(AbstractModel):
    """StopProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目 id
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopProjectResponse(AbstractModel):
    """StopProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param Key: 标签key
        :type Key: str
        :param Value: 标签value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whitelist(AbstractModel):
    """白名单

    """

    def __init__(self):
        r"""
        :param Remark: 备注
        :type Remark: str
        :param InstanceID: 实例ID
        :type InstanceID: str
        :param Ttl: 截止时间
        :type Ttl: str
        :param ID: 白名单自增ID
        :type ID: str
        :param WhitelistUin: 业务唯一标识
        :type WhitelistUin: str
        :param CreateUser: 创建者ID
        :type CreateUser: str
        :param Aid: aid标识
        :type Aid: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.Remark = None
        self.InstanceID = None
        self.Ttl = None
        self.ID = None
        self.WhitelistUin = None
        self.CreateUser = None
        self.Aid = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Remark = params.get("Remark")
        self.InstanceID = params.get("InstanceID")
        self.Ttl = params.get("Ttl")
        self.ID = params.get("ID")
        self.WhitelistUin = params.get("WhitelistUin")
        self.CreateUser = params.get("CreateUser")
        self.Aid = params.get("Aid")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        