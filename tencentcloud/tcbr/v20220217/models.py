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


class BuildPacksInfo(AbstractModel):
    """BuildPacks信息

    """

    def __init__(self):
        r"""
        :param BaseImage: 基础镜像
        :type BaseImage: str
        :param EntryPoint: 启动命令
        :type EntryPoint: str
        :param RepoLanguage: 语言
        :type RepoLanguage: str
        :param UploadFilename: 上传文件名
        :type UploadFilename: str
        """
        self.BaseImage = None
        self.EntryPoint = None
        self.RepoLanguage = None
        self.UploadFilename = None


    def _deserialize(self, params):
        self.BaseImage = params.get("BaseImage")
        self.EntryPoint = params.get("EntryPoint")
        self.RepoLanguage = params.get("RepoLanguage")
        self.UploadFilename = params.get("UploadFilename")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsInfo(AbstractModel):
    """cls日志信息

    """

    def __init__(self):
        r"""
        :param ClsRegion: cls所属地域
        :type ClsRegion: str
        :param ClsLogsetId: cls日志集ID
        :type ClsLogsetId: str
        :param ClsTopicId: cls日志主题ID
        :type ClsTopicId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.ClsRegion = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ClsRegion = params.get("ClsRegion")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRunEnvRequest(AbstractModel):
    """CreateCloudRunEnv请求参数结构体

    """

    def __init__(self):
        r"""
        :param PackageType: Trial,Standard,Professional,Enterprise
        :type PackageType: str
        :param Alias: 环境别名，要以a-z开头，不能包含 a-z,0-9,- 以外的字符
        :type Alias: str
        :param FreeQuota: 用户享有的免费额度级别，目前只能为“basic”，不传该字段或该字段为空，标识不享受免费额度。
        :type FreeQuota: str
        :param Flag: 订单标记。建议使用方统一转大小写之后再判断。
QuickStart：快速启动来源
Activity：活动来源
        :type Flag: str
        :param VpcId: 私有网络Id
        :type VpcId: str
        :param SubNetIds: 子网列表
        :type SubNetIds: list of str
        :param ReqKey: 请求key 用于防重
        :type ReqKey: str
        :param Source: 来源：wechat | cloud
        :type Source: str
        :param Channel: 渠道：wechat | cloud
        :type Channel: str
        """
        self.PackageType = None
        self.Alias = None
        self.FreeQuota = None
        self.Flag = None
        self.VpcId = None
        self.SubNetIds = None
        self.ReqKey = None
        self.Source = None
        self.Channel = None


    def _deserialize(self, params):
        self.PackageType = params.get("PackageType")
        self.Alias = params.get("Alias")
        self.FreeQuota = params.get("FreeQuota")
        self.Flag = params.get("Flag")
        self.VpcId = params.get("VpcId")
        self.SubNetIds = params.get("SubNetIds")
        self.ReqKey = params.get("ReqKey")
        self.Source = params.get("Source")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRunEnvResponse(AbstractModel):
    """CreateCloudRunEnv返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param TranId: 后付费订单号
        :type TranId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.TranId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.TranId = params.get("TranId")
        self.RequestId = params.get("RequestId")


class CreateCloudRunServerRequest(AbstractModel):
    """CreateCloudRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param DeployInfo: 部署信息
        :type DeployInfo: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        :param ServerConfig: 服务配置信息
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        """
        self.EnvId = None
        self.ServerName = None
        self.DeployInfo = None
        self.ServerConfig = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        if params.get("DeployInfo") is not None:
            self.DeployInfo = DeployParam()
            self.DeployInfo._deserialize(params.get("DeployInfo"))
        if params.get("ServerConfig") is not None:
            self.ServerConfig = ServerBaseConfig()
            self.ServerConfig._deserialize(params.get("ServerConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRunServerResponse(AbstractModel):
    """CreateCloudRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 一键部署任务Id，微信云托管，暂时用不到
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DatabasesInfo(AbstractModel):
    """数据库资源信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployParam(AbstractModel):
    """部署参数

    """

    def __init__(self):
        r"""
        :param DeployType: 部署类型：package/image/repository/pipeline/jar/war
        :type DeployType: str
        :param ImageUrl: 部署类型为image时传入
        :type ImageUrl: str
        :param PackageName: 部署类型为package时传入
        :type PackageName: str
        :param PackageVersion: 部署类型为package时传入
        :type PackageVersion: str
        :param DeployRemark: 部署备注
        :type DeployRemark: str
        :param RepoInfo: 代码仓库信息
        :type RepoInfo: :class:`tencentcloud.tcbr.v20220217.models.RepositoryInfo`
        :param BuildPacks: 无Dockerfile时填写
        :type BuildPacks: :class:`tencentcloud.tcbr.v20220217.models.BuildPacksInfo`
        :param ReleaseType: 发布类型 GRAY | FULL
        :type ReleaseType: str
        """
        self.DeployType = None
        self.ImageUrl = None
        self.PackageName = None
        self.PackageVersion = None
        self.DeployRemark = None
        self.RepoInfo = None
        self.BuildPacks = None
        self.ReleaseType = None


    def _deserialize(self, params):
        self.DeployType = params.get("DeployType")
        self.ImageUrl = params.get("ImageUrl")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.DeployRemark = params.get("DeployRemark")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = RepositoryInfo()
            self.RepoInfo._deserialize(params.get("RepoInfo"))
        if params.get("BuildPacks") is not None:
            self.BuildPacks = BuildPacksInfo()
            self.BuildPacks._deserialize(params.get("BuildPacks"))
        self.ReleaseType = params.get("ReleaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunEnvsRequest(AbstractModel):
    """DescribeCloudRunEnvs请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunEnvsResponse(AbstractModel):
    """DescribeCloudRunEnvs返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeCloudRunServerDetailRequest(AbstractModel):
    """DescribeCloudRunServerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        """
        self.EnvId = None
        self.ServerName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunServerDetailResponse(AbstractModel):
    """DescribeCloudRunServerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param BaseInfo: 服务基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseInfo: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseInfo`
        :param ServerConfig: 服务配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        :param OnlineVersionInfos: 在线版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineVersionInfos: list of OnlineVersionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaseInfo = None
        self.ServerConfig = None
        self.OnlineVersionInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BaseInfo") is not None:
            self.BaseInfo = ServerBaseInfo()
            self.BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("ServerConfig") is not None:
            self.ServerConfig = ServerBaseConfig()
            self.ServerConfig._deserialize(params.get("ServerConfig"))
        if params.get("OnlineVersionInfos") is not None:
            self.OnlineVersionInfos = []
            for item in params.get("OnlineVersionInfos"):
                obj = OnlineVersionInfo()
                obj._deserialize(item)
                self.OnlineVersionInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudRunServersRequest(AbstractModel):
    """DescribeCloudRunServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRunServersResponse(AbstractModel):
    """DescribeCloudRunServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServerList: 服务列表
        :type ServerList: list of ServerBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServerList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServerList") is not None:
            self.ServerList = []
            for item in params.get("ServerList"):
                obj = ServerBaseInfo()
                obj._deserialize(item)
                self.ServerList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvBaseInfoRequest(AbstractModel):
    """DescribeEnvBaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境 Id
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvBaseInfoResponse(AbstractModel):
    """DescribeEnvBaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnvBaseInfo: 环境基础信息
        :type EnvBaseInfo: :class:`tencentcloud.tcbr.v20220217.models.EnvBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvBaseInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnvBaseInfo") is not None:
            self.EnvBaseInfo = EnvBaseInfo()
            self.EnvBaseInfo._deserialize(params.get("EnvBaseInfo"))
        self.RequestId = params.get("RequestId")


class DescribeServerManageTaskRequest(AbstractModel):
    """DescribeServerManageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param TaskId: 任务Id
        :type TaskId: int
        :param OperatorRemark: 操作标识
        :type OperatorRemark: str
        """
        self.EnvId = None
        self.ServerName = None
        self.TaskId = None
        self.OperatorRemark = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.TaskId = params.get("TaskId")
        self.OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerManageTaskResponse(AbstractModel):
    """DescribeServerManageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsExist: 是否存在
        :type IsExist: bool
        :param Task: 任务信息
        :type Task: :class:`tencentcloud.tcbr.v20220217.models.ServerManageTaskInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsExist = None
        self.Task = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsExist = params.get("IsExist")
        if params.get("Task") is not None:
            self.Task = ServerManageTaskInfo()
            self.Task._deserialize(params.get("Task"))
        self.RequestId = params.get("RequestId")


class EnvBaseInfo(AbstractModel):
    """环境基础信息

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param PackageType: 套餐类型：Trial ｜ Standard ｜ Professional ｜ Enterprise
        :type PackageType: str
        :param VpcId: VPC Id
        :type VpcId: str
        :param CreateTime: 环境创建时间
        :type CreateTime: str
        :param Alias: 环境别名
        :type Alias: str
        :param Status: 环境状态
        :type Status: str
        :param Region: 环境地域
        :type Region: str
        :param EnvType: 环境类型 tcbr ｜ run
        :type EnvType: str
        """
        self.EnvId = None
        self.PackageType = None
        self.VpcId = None
        self.CreateTime = None
        self.Alias = None
        self.Status = None
        self.Region = None
        self.EnvType = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.PackageType = params.get("PackageType")
        self.VpcId = params.get("VpcId")
        self.CreateTime = params.get("CreateTime")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境信息

    """

    def __init__(self):
        r"""
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
        :param IsAutoDegrade: 是否到期自动降为免费版
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAutoDegrade: bool
        :param EnvChannel: 环境渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvChannel: str
        :param PayMode: 支付方式。包含以下取值：
<li> prepayment：预付费</li>
<li> postpaid：后付费</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param IsDefault: 是否为默认环境
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        :param Region: 环境所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param EnvType: 环境类型：baas, run, hosting, weda,tcbr
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvType: str
        :param Databases: 数据库列表
        :type Databases: list of DatabasesInfo
        :param Storages: 存储列表
        :type Storages: list of StorageInfo
        :param Functions: 函数列表
        :type Functions: list of FunctionInfo
        :param LogServices: 云日志服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogServices: list of LogServiceInfo
        :param StaticStorages: 静态资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticStorages: list of StaticStorageInfo
        :param Tags: 环境标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param CustomLogServices: 自定义日志服务
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomLogServices: list of ClsInfo
        :param PackageId: tcb产品套餐ID，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 套餐中文名称，参考DescribePackages接口的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        """
        self.EnvId = None
        self.Source = None
        self.Alias = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Status = None
        self.IsAutoDegrade = None
        self.EnvChannel = None
        self.PayMode = None
        self.IsDefault = None
        self.Region = None
        self.EnvType = None
        self.Databases = None
        self.Storages = None
        self.Functions = None
        self.LogServices = None
        self.StaticStorages = None
        self.Tags = None
        self.CustomLogServices = None
        self.PackageId = None
        self.PackageName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.IsAutoDegrade = params.get("IsAutoDegrade")
        self.EnvChannel = params.get("EnvChannel")
        self.PayMode = params.get("PayMode")
        self.IsDefault = params.get("IsDefault")
        self.Region = params.get("Region")
        self.EnvType = params.get("EnvType")
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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("CustomLogServices") is not None:
            self.CustomLogServices = []
            for item in params.get("CustomLogServices"):
                obj = ClsInfo()
                obj._deserialize(item)
                self.CustomLogServices.append(obj)
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionInfo(AbstractModel):
    """函数的信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HpaPolicy(AbstractModel):
    """扩缩容入参

    """

    def __init__(self):
        r"""
        :param PolicyType: 扩缩容类型
        :type PolicyType: str
        :param PolicyThreshold: 扩缩容阈值
        :type PolicyThreshold: int
        """
        self.PolicyType = None
        self.PolicyThreshold = None


    def _deserialize(self, params):
        self.PolicyType = params.get("PolicyType")
        self.PolicyThreshold = params.get("PolicyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogServiceInfo(AbstractModel):
    """云日志服务相关信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectKV(AbstractModel):
    """通用Key Value

    """

    def __init__(self):
        r"""
        :param Key: 键值对Key
        :type Key: str
        :param Value: 键值对Value
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
        


class OnlineVersionInfo(AbstractModel):
    """在线版本信息

    """

    def __init__(self):
        r"""
        :param VersionName: 版本名
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param ImageUrl: 镜像url
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param FlowRatio: 流量
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowRatio: str
        """
        self.VersionName = None
        self.ImageUrl = None
        self.FlowRatio = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.ImageUrl = params.get("ImageUrl")
        self.FlowRatio = params.get("FlowRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateServerManageRequest(AbstractModel):
    """OperateServerManage请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param TaskId: 任报Id
        :type TaskId: int
        :param OperateType: 操作类型:cancel | go_back | done
        :type OperateType: str
        :param OperatorRemark: 操作标识
        :type OperatorRemark: str
        """
        self.EnvId = None
        self.ServerName = None
        self.TaskId = None
        self.OperateType = None
        self.OperatorRemark = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.TaskId = params.get("TaskId")
        self.OperateType = params.get("OperateType")
        self.OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperateServerManageResponse(AbstractModel):
    """OperateServerManage返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseGrayRequest(AbstractModel):
    """ReleaseGray请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param GrayType: 灰度类型
        :type GrayType: str
        :param TrafficType: 流量类型
        :type TrafficType: str
        :param VersionFlowItems: 流量策略
        :type VersionFlowItems: list of VersionFlowInfo
        :param OperatorRemark: 操作标识
        :type OperatorRemark: str
        :param GrayFlowRatio: 流量比例
        :type GrayFlowRatio: int
        """
        self.EnvId = None
        self.ServerName = None
        self.GrayType = None
        self.TrafficType = None
        self.VersionFlowItems = None
        self.OperatorRemark = None
        self.GrayFlowRatio = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.GrayType = params.get("GrayType")
        self.TrafficType = params.get("TrafficType")
        if params.get("VersionFlowItems") is not None:
            self.VersionFlowItems = []
            for item in params.get("VersionFlowItems"):
                obj = VersionFlowInfo()
                obj._deserialize(item)
                self.VersionFlowItems.append(obj)
        self.OperatorRemark = params.get("OperatorRemark")
        self.GrayFlowRatio = params.get("GrayFlowRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseGrayResponse(AbstractModel):
    """ReleaseGray返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RepositoryInfo(AbstractModel):
    """代码仓库信息

    """

    def __init__(self):
        r"""
        :param Source: git source
        :type Source: str
        :param Repo: 仓库名
        :type Repo: str
        :param Branch: 分支名
        :type Branch: str
        """
        self.Source = None
        self.Repo = None
        self.Branch = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Repo = params.get("Repo")
        self.Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerBaseConfig(AbstractModel):
    """服务基础配置信息

    """

    def __init__(self):
        r"""
        :param EnvId: 环境 Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param OpenAccessTypes: 是否开启公网访问
        :type OpenAccessTypes: list of str
        :param Cpu: Cpu 规格
        :type Cpu: float
        :param Mem: Mem 规格
        :type Mem: float
        :param MinNum: 最小副本数
        :type MinNum: int
        :param MaxNum: 最大副本数
        :type MaxNum: int
        :param PolicyDetails: 扩缩容配置
        :type PolicyDetails: list of HpaPolicy
        :param CustomLogs: 日志采集路径
        :type CustomLogs: str
        :param EnvParams: 环境变量
        :type EnvParams: str
        :param InitialDelaySeconds: 延迟检测时间
        :type InitialDelaySeconds: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Port: 服务端口
        :type Port: int
        :param HasDockerfile: 是否有Dockerfile
        :type HasDockerfile: bool
        :param Dockerfile: Dockerfile 文件名
        :type Dockerfile: str
        :param BuildDir: 构建目录
        :type BuildDir: str
        :param LogType: 日志类型: none | default | custom
        :type LogType: str
        :param LogSetId: cls setId
        :type LogSetId: str
        :param LogTopicId: cls 主题id
        :type LogTopicId: str
        :param LogParseType: 解析类型：json ｜ line
        :type LogParseType: str
        """
        self.EnvId = None
        self.ServerName = None
        self.OpenAccessTypes = None
        self.Cpu = None
        self.Mem = None
        self.MinNum = None
        self.MaxNum = None
        self.PolicyDetails = None
        self.CustomLogs = None
        self.EnvParams = None
        self.InitialDelaySeconds = None
        self.CreateTime = None
        self.Port = None
        self.HasDockerfile = None
        self.Dockerfile = None
        self.BuildDir = None
        self.LogType = None
        self.LogSetId = None
        self.LogTopicId = None
        self.LogParseType = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.OpenAccessTypes = params.get("OpenAccessTypes")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.MinNum = params.get("MinNum")
        self.MaxNum = params.get("MaxNum")
        if params.get("PolicyDetails") is not None:
            self.PolicyDetails = []
            for item in params.get("PolicyDetails"):
                obj = HpaPolicy()
                obj._deserialize(item)
                self.PolicyDetails.append(obj)
        self.CustomLogs = params.get("CustomLogs")
        self.EnvParams = params.get("EnvParams")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.CreateTime = params.get("CreateTime")
        self.Port = params.get("Port")
        self.HasDockerfile = params.get("HasDockerfile")
        self.Dockerfile = params.get("Dockerfile")
        self.BuildDir = params.get("BuildDir")
        self.LogType = params.get("LogType")
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")
        self.LogParseType = params.get("LogParseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerBaseInfo(AbstractModel):
    """服务基本信息

    """

    def __init__(self):
        r"""
        :param ServerName: 服务名
        :type ServerName: str
        :param DefaultDomainName: 默认服务域名
        :type DefaultDomainName: str
        :param CustomDomainName: 自定义域名
        :type CustomDomainName: str
        :param Status: 服务状态：running/deploying/deploy_failed
        :type Status: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.ServerName = None
        self.DefaultDomainName = None
        self.CustomDomainName = None
        self.Status = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ServerName = params.get("ServerName")
        self.DefaultDomainName = params.get("DefaultDomainName")
        self.CustomDomainName = params.get("CustomDomainName")
        self.Status = params.get("Status")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerManageTaskInfo(AbstractModel):
    """服务管理任务信息

    """

    def __init__(self):
        r"""
        :param Id: 任务Id
        :type Id: int
        :param EnvId: 环境Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ChangeType: 变更类型
        :type ChangeType: str
        :param ReleaseType: 发布类型
        :type ReleaseType: str
        :param DeployType: 部署类型
        :type DeployType: str
        :param PreVersionName: 上一个版本名
        :type PreVersionName: str
        :param VersionName: 版本名
        :type VersionName: str
        :param PipelineId: 流水线Id
        :type PipelineId: int
        :param PipelineTaskId: 流水线任务Id
        :type PipelineTaskId: int
        :param ReleaseId: 发布单Id
        :type ReleaseId: int
        :param Status: 状态
        :type Status: str
        :param Steps: 步骤信息
        :type Steps: list of TaskStepInfo
        :param FailReason: 失败原因
        :type FailReason: str
        :param OperatorRemark: 操作标识
        :type OperatorRemark: str
        """
        self.Id = None
        self.EnvId = None
        self.ServerName = None
        self.CreateTime = None
        self.ChangeType = None
        self.ReleaseType = None
        self.DeployType = None
        self.PreVersionName = None
        self.VersionName = None
        self.PipelineId = None
        self.PipelineTaskId = None
        self.ReleaseId = None
        self.Status = None
        self.Steps = None
        self.FailReason = None
        self.OperatorRemark = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        self.CreateTime = params.get("CreateTime")
        self.ChangeType = params.get("ChangeType")
        self.ReleaseType = params.get("ReleaseType")
        self.DeployType = params.get("DeployType")
        self.PreVersionName = params.get("PreVersionName")
        self.VersionName = params.get("VersionName")
        self.PipelineId = params.get("PipelineId")
        self.PipelineTaskId = params.get("PipelineTaskId")
        self.ReleaseId = params.get("ReleaseId")
        self.Status = params.get("Status")
        if params.get("Steps") is not None:
            self.Steps = []
            for item in params.get("Steps"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self.Steps.append(obj)
        self.FailReason = params.get("FailReason")
        self.OperatorRemark = params.get("OperatorRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticStorageInfo(AbstractModel):
    """静态CDN资源信息

    """

    def __init__(self):
        r"""
        :param StaticDomain: 静态CDN域名
        :type StaticDomain: str
        :param DefaultDirName: 静态CDN默认文件夹，当前为根目录
        :type DefaultDirName: str
        :param Status: 资源状态(process/online/offline/init)
        :type Status: str
        :param Region: cos所属区域
        :type Region: str
        :param Bucket: bucket信息
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """StorageInfo 资源信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param Key: 标签键
        :type Key: str
        :param Value: 标签值
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
        


class TaskStepInfo(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        r"""
        :param Name: 步骤名
        :type Name: str
        :param Status: 未启动："todo"
运行中："running"
失败："failed"
成功结束："finished"
        :type Status: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param CostTime: 消耗时间：秒
        :type CostTime: int
        :param FailReason: 失败原因
        :type FailReason: str
        """
        self.Name = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.CostTime = None
        self.FailReason = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CostTime = params.get("CostTime")
        self.FailReason = params.get("FailReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudRunServerRequest(AbstractModel):
    """UpdateCloudRunServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param ServerName: 服务名
        :type ServerName: str
        :param DeployInfo: 部署信息
        :type DeployInfo: :class:`tencentcloud.tcbr.v20220217.models.DeployParam`
        :param ServerConfig: 服务配置信息
        :type ServerConfig: :class:`tencentcloud.tcbr.v20220217.models.ServerBaseConfig`
        """
        self.EnvId = None
        self.ServerName = None
        self.DeployInfo = None
        self.ServerConfig = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ServerName = params.get("ServerName")
        if params.get("DeployInfo") is not None:
            self.DeployInfo = DeployParam()
            self.DeployInfo._deserialize(params.get("DeployInfo"))
        if params.get("ServerConfig") is not None:
            self.ServerConfig = ServerBaseConfig()
            self.ServerConfig._deserialize(params.get("ServerConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudRunServerResponse(AbstractModel):
    """UpdateCloudRunServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param EnvId: 环境Id
        :type EnvId: str
        :param TaskId: 一键部署任务Id，暂时用不到
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class VersionFlowInfo(AbstractModel):
    """版本流量信息

    """

    def __init__(self):
        r"""
        :param VersionName: 版本名
        :type VersionName: str
        :param IsDefaultPriority: 是否默认版本
        :type IsDefaultPriority: bool
        :param FlowRatio: 流量比例
        :type FlowRatio: int
        :param UrlParam: 测试KV值
        :type UrlParam: :class:`tencentcloud.tcbr.v20220217.models.ObjectKV`
        :param Priority: 权重
        :type Priority: int
        """
        self.VersionName = None
        self.IsDefaultPriority = None
        self.FlowRatio = None
        self.UrlParam = None
        self.Priority = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.IsDefaultPriority = params.get("IsDefaultPriority")
        self.FlowRatio = params.get("FlowRatio")
        if params.get("UrlParam") is not None:
            self.UrlParam = ObjectKV()
            self.UrlParam._deserialize(params.get("UrlParam"))
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        