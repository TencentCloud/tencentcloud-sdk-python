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


class AccountStatistics(AbstractModel):
    """帐号统计数据。

    """

    def __init__(self):
        r"""
        :param Username: 用户名。
        :type Username: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.Username = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetAppBaseInfo(AbstractModel):
    """资源管理进程基本信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param Name: 应用名称
        :type Name: str
        :param Type: 应用类型	
1: 运维
2 : 数据库
3 : 安全
4 : 可疑应用
5 : 系统架构
6 : 系统应用
7 : WEB服务
99: 其他
        :type Type: int
        :param BinPath: 二进制路径
        :type BinPath: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param ProcessCount: 关联进程数
        :type ProcessCount: int
        :param Desc: 应用描述
        :type Desc: str
        :param Version: 版本号
        :type Version: str
        :param ConfigPath: 配置文件路径
        :type ConfigPath: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param IsNew: 是否新增[0:否|1:是]
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNew: int
        """
        self.MachineIp = None
        self.MachineName = None
        self.MachineWanIp = None
        self.Uuid = None
        self.Quuid = None
        self.ProjectId = None
        self.Tag = None
        self.Name = None
        self.Type = None
        self.BinPath = None
        self.OsInfo = None
        self.ProcessCount = None
        self.Desc = None
        self.Version = None
        self.ConfigPath = None
        self.FirstTime = None
        self.UpdateTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.BinPath = params.get("BinPath")
        self.OsInfo = params.get("OsInfo")
        self.ProcessCount = params.get("ProcessCount")
        self.Desc = params.get("Desc")
        self.Version = params.get("Version")
        self.ConfigPath = params.get("ConfigPath")
        self.FirstTime = params.get("FirstTime")
        self.UpdateTime = params.get("UpdateTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetAppProcessInfo(AbstractModel):
    """软件应用关联进程信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Status: 进程状态
        :type Status: str
        :param Version: 进程版本
        :type Version: str
        :param Path: 路径
        :type Path: str
        :param User: 用户
        :type User: str
        :param StartTime: 启动时间
        :type StartTime: str
        """
        self.Name = None
        self.Status = None
        self.Version = None
        self.Path = None
        self.User = None
        self.StartTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Version = params.get("Version")
        self.Path = params.get("Path")
        self.User = params.get("User")
        self.StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetCoreModuleBaseInfo(AbstractModel):
    """资产管理内核模块列表

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Path: 路径
        :type Path: str
        :param Version: 版本
        :type Version: str
        :param MachineIp: 服务器IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param Size: 模块大小
        :type Size: int
        :param ProcessCount: 依赖进程数
        :type ProcessCount: int
        :param ModuleCount: 依赖模块数
        :type ModuleCount: int
        :param Id: 模块ID
        :type Id: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机uuid
        :type Uuid: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        :param MachineWanIp: 服务器外网IP
        :type MachineWanIp: str
        """
        self.Name = None
        self.Desc = None
        self.Path = None
        self.Version = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Size = None
        self.ProcessCount = None
        self.ModuleCount = None
        self.Id = None
        self.Quuid = None
        self.Uuid = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None
        self.MachineWanIp = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Path = params.get("Path")
        self.Version = params.get("Version")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Size = params.get("Size")
        self.ProcessCount = params.get("ProcessCount")
        self.ModuleCount = params.get("ModuleCount")
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        self.MachineWanIp = params.get("MachineWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetCoreModuleDetail(AbstractModel):
    """资产管理内核模块详情

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Path: 路径
        :type Path: str
        :param Version: 版本
        :type Version: str
        :param Size: 大小
        :type Size: int
        :param Processes: 依赖进程
        :type Processes: str
        :param Modules: 被依赖模块
        :type Modules: str
        :param Params: 参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of AssetCoreModuleParam
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Name = None
        self.Desc = None
        self.Path = None
        self.Version = None
        self.Size = None
        self.Processes = None
        self.Modules = None
        self.Params = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Path = params.get("Path")
        self.Version = params.get("Version")
        self.Size = params.get("Size")
        self.Processes = params.get("Processes")
        self.Modules = params.get("Modules")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = AssetCoreModuleParam()
                obj._deserialize(item)
                self.Params.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetCoreModuleParam(AbstractModel):
    """资产管理内核模块参数

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Data: 数据
        :type Data: str
        """
        self.Name = None
        self.Data = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetDatabaseBaseInfo(AbstractModel):
    """资源管理数据库列表信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param Name: 数据库名
        :type Name: str
        :param Version: 版本
        :type Version: str
        :param Port: 监听端口
        :type Port: str
        :param Proto: 协议
        :type Proto: str
        :param User: 运行用户
        :type User: str
        :param Ip: 绑定IP
        :type Ip: str
        :param ConfigPath: 配置文件路径
        :type ConfigPath: str
        :param LogPath: 日志文件路径
        :type LogPath: str
        :param DataPath: 数据路径
        :type DataPath: str
        :param Permission: 运行权限
        :type Permission: str
        :param ErrorLogPath: 错误日志路径
        :type ErrorLogPath: str
        :param PlugInPath: 插件路径
        :type PlugInPath: str
        :param BinPath: 二进制路径
        :type BinPath: str
        :param Param: 启动参数
        :type Param: str
        :param Id: 数据库ID
        :type Id: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        :param MachineName: 主机名称
        :type MachineName: str
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.OsInfo = None
        self.ProjectId = None
        self.Tag = None
        self.Name = None
        self.Version = None
        self.Port = None
        self.Proto = None
        self.User = None
        self.Ip = None
        self.ConfigPath = None
        self.LogPath = None
        self.DataPath = None
        self.Permission = None
        self.ErrorLogPath = None
        self.PlugInPath = None
        self.BinPath = None
        self.Param = None
        self.Id = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None
        self.MachineName = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.OsInfo = params.get("OsInfo")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")
        self.User = params.get("User")
        self.Ip = params.get("Ip")
        self.ConfigPath = params.get("ConfigPath")
        self.LogPath = params.get("LogPath")
        self.DataPath = params.get("DataPath")
        self.Permission = params.get("Permission")
        self.ErrorLogPath = params.get("ErrorLogPath")
        self.PlugInPath = params.get("PlugInPath")
        self.BinPath = params.get("BinPath")
        self.Param = params.get("Param")
        self.Id = params.get("Id")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        self.MachineName = params.get("MachineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetDatabaseDetail(AbstractModel):
    """资源管理数据库列表信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param Name: 数据库名
        :type Name: str
        :param Version: 版本
        :type Version: str
        :param Port: 监听端口
        :type Port: str
        :param Proto: 协议
        :type Proto: str
        :param User: 运行用户
        :type User: str
        :param Ip: 绑定IP
        :type Ip: str
        :param ConfigPath: 配置文件路径
        :type ConfigPath: str
        :param LogPath: 日志文件路径
        :type LogPath: str
        :param DataPath: 数据路径
        :type DataPath: str
        :param Permission: 运行权限
        :type Permission: str
        :param ErrorLogPath: 错误日志路径
        :type ErrorLogPath: str
        :param PlugInPath: 插件路径
        :type PlugInPath: str
        :param BinPath: 二进制路径
        :type BinPath: str
        :param Param: 启动参数
        :type Param: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.OsInfo = None
        self.Name = None
        self.Version = None
        self.Port = None
        self.Proto = None
        self.User = None
        self.Ip = None
        self.ConfigPath = None
        self.LogPath = None
        self.DataPath = None
        self.Permission = None
        self.ErrorLogPath = None
        self.PlugInPath = None
        self.BinPath = None
        self.Param = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.OsInfo = params.get("OsInfo")
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")
        self.User = params.get("User")
        self.Ip = params.get("Ip")
        self.ConfigPath = params.get("ConfigPath")
        self.LogPath = params.get("LogPath")
        self.DataPath = params.get("DataPath")
        self.Permission = params.get("Permission")
        self.ErrorLogPath = params.get("ErrorLogPath")
        self.PlugInPath = params.get("PlugInPath")
        self.BinPath = params.get("BinPath")
        self.Param = params.get("Param")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetDiskPartitionInfo(AbstractModel):
    """资产管理磁盘分区信息

    """

    def __init__(self):
        r"""
        :param Name: 分区名
        :type Name: str
        :param Size: 分区大小：单位G
        :type Size: int
        :param Percent: 分区使用率
        :type Percent: float
        :param Type: 文件系统类型
        :type Type: str
        :param Path: 挂载目录
        :type Path: str
        :param Used: 已使用空间：单位G
        :type Used: int
        """
        self.Name = None
        self.Size = None
        self.Percent = None
        self.Type = None
        self.Path = None
        self.Used = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Percent = params.get("Percent")
        self.Type = params.get("Type")
        self.Path = params.get("Path")
        self.Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetEnvBaseInfo(AbstractModel):
    """资产管理环境变量列表

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Type: 类型：
0:用户变量
1:系统变量
        :type Type: int
        :param User: 启动用户
        :type User: str
        :param Value: 环境变量值
        :type Value: str
        :param MachineIp: 服务器IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机uuid
        :type Uuid: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        :param MachineWanIp: 服务器外网IP
        :type MachineWanIp: str
        """
        self.Name = None
        self.Type = None
        self.User = None
        self.Value = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Quuid = None
        self.Uuid = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None
        self.MachineWanIp = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.User = params.get("User")
        self.Value = params.get("Value")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        self.MachineWanIp = params.get("MachineWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetFilters(AbstractModel):
    """容器安全
    描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否模糊查询
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetInitServiceBaseInfo(AbstractModel):
    """资产管理启动服务列表

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Type: 类型：
1:编码器
2:IE插件
3:网络提供者
4:镜像劫持
5:LSA提供者
6:KnownDLLs
7:启动执行
8:WMI
9:计划任务
10:Winsock提供者
11:打印监控器
12:资源管理器
13:驱动服务
14:登录
        :type Type: int
        :param Status: 默认启用状态：0未启用，1启用
        :type Status: int
        :param User: 启动用户
        :type User: str
        :param Path: 路径
        :type Path: str
        :param MachineIp: 服务器IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机uuid
        :type Uuid: str
        :param UpdateTime: 数据更新时间
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        :param MachineWanIp: 服务器外网IP
        :type MachineWanIp: str
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.User = None
        self.Path = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Quuid = None
        self.Uuid = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None
        self.MachineWanIp = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.User = params.get("User")
        self.Path = params.get("Path")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        self.MachineWanIp = params.get("MachineWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetJarBaseInfo(AbstractModel):
    """资产管理jar包列表

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Type: 类型：1应用程序，2系统类库，3Web服务自带库，8:其他，
        :type Type: int
        :param Status: 是否可执行：0未知，1是，2否
        :type Status: int
        :param Version: 版本
        :type Version: str
        :param Path: 路径
        :type Path: str
        :param MachineIp: 服务器IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param Id: Jar包ID
        :type Id: str
        :param Md5: Jar包Md5
        :type Md5: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机uuid
        :type Uuid: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        :param MachineWanIp: 服务器外网IP
        :type MachineWanIp: str
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.Version = None
        self.Path = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Id = None
        self.Md5 = None
        self.Quuid = None
        self.Uuid = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None
        self.MachineWanIp = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Version = params.get("Version")
        self.Path = params.get("Path")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Id = params.get("Id")
        self.Md5 = params.get("Md5")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        self.MachineWanIp = params.get("MachineWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetJarDetail(AbstractModel):
    """资产管理jar包详情

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Type: 类型：1应用程序，2系统类库，3Web服务自带库，8:其他，
        :type Type: int
        :param Status: 是否可执行：0未知，1是，2否
        :type Status: int
        :param Version: 版本
        :type Version: str
        :param Path: 路径
        :type Path: str
        :param MachineIp: 服务器IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param Process: 引用进程列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: list of AssetAppProcessInfo
        :param Md5: Jar包Md5
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.Version = None
        self.Path = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Process = None
        self.Md5 = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Version = params.get("Version")
        self.Path = params.get("Path")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        if params.get("Process") is not None:
            self.Process = []
            for item in params.get("Process"):
                obj = AssetAppProcessInfo()
                obj._deserialize(item)
                self.Process.append(obj)
        self.Md5 = params.get("Md5")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetKeyVal(AbstractModel):
    """key-val类型的通用数据结构

    """

    def __init__(self):
        r"""
        :param Key: 标签
        :type Key: str
        :param Value: 数量
        :type Value: int
        :param Desc: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param NewCount: 今日新增数量
注意：此字段可能返回 null，表示取不到有效值。
        :type NewCount: int
        """
        self.Key = None
        self.Value = None
        self.Desc = None
        self.NewCount = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Desc = params.get("Desc")
        self.NewCount = params.get("NewCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetMachineBaseInfo(AbstractModel):
    """资产指纹中服务器列表的基本信息

    """

    def __init__(self):
        r"""
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Uuid: 服务器uuid
        :type Uuid: str
        :param MachineIp: 服务器内网IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统名称
        :type OsInfo: str
        :param Cpu: CPU信息
        :type Cpu: str
        :param MemSize: 内存容量：单位G
        :type MemSize: int
        :param MemLoad: 内存使用率百分比
        :type MemLoad: str
        :param DiskSize: 硬盘容量：单位G
        :type DiskSize: int
        :param DiskLoad: 硬盘使用率百分比
        :type DiskLoad: str
        :param PartitionCount: 分区数
        :type PartitionCount: int
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param ProjectId: 业务组ID
        :type ProjectId: int
        :param CpuSize: Cpu数量
        :type CpuSize: int
        :param CpuLoad: Cpu使用率百分比
        :type CpuLoad: str
        :param Tag: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        """
        self.Quuid = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Cpu = None
        self.MemSize = None
        self.MemLoad = None
        self.DiskSize = None
        self.DiskLoad = None
        self.PartitionCount = None
        self.MachineWanIp = None
        self.ProjectId = None
        self.CpuSize = None
        self.CpuLoad = None
        self.Tag = None
        self.UpdateTime = None
        self.IsNew = None
        self.FirstTime = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Cpu = params.get("Cpu")
        self.MemSize = params.get("MemSize")
        self.MemLoad = params.get("MemLoad")
        self.DiskSize = params.get("DiskSize")
        self.DiskLoad = params.get("DiskLoad")
        self.PartitionCount = params.get("PartitionCount")
        self.MachineWanIp = params.get("MachineWanIp")
        self.ProjectId = params.get("ProjectId")
        self.CpuSize = params.get("CpuSize")
        self.CpuLoad = params.get("CpuLoad")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.IsNew = params.get("IsNew")
        self.FirstTime = params.get("FirstTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetMachineDetail(AbstractModel):
    """资产指纹中服务器列表的基本信息

    """

    def __init__(self):
        r"""
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Uuid: 服务器uuid
        :type Uuid: str
        :param MachineIp: 服务器内网IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统名称
        :type OsInfo: str
        :param Cpu: CPU信息
        :type Cpu: str
        :param MemSize: 内存容量：单位G
        :type MemSize: int
        :param MemLoad: 内存使用率百分比
        :type MemLoad: str
        :param DiskSize: 硬盘容量：单位G
        :type DiskSize: int
        :param DiskLoad: 硬盘使用率百分比
        :type DiskLoad: str
        :param PartitionCount: 分区数
        :type PartitionCount: int
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param CpuSize: Cpu数量
        :type CpuSize: int
        :param CpuLoad: Cpu使用率百分比
        :type CpuLoad: str
        :param ProtectLevel: 防护级别：0基础版，1专业版
        :type ProtectLevel: int
        :param RiskStatus: 风险状态：UNKNOW-未知，RISK-风险，SAFT-安全
        :type RiskStatus: str
        :param ProtectDays: 已防护天数
        :type ProtectDays: int
        :param BuyTime: 专业版开通时间
        :type BuyTime: str
        :param EndTime: 专业版到期时间
        :type EndTime: str
        :param CoreVersion: 内核版本
        :type CoreVersion: str
        :param OsType: linux/windows
        :type OsType: str
        :param AgentVersion: agent版本
        :type AgentVersion: str
        :param InstallTime: 安装时间
        :type InstallTime: str
        :param BootTime: 系统启动时间
        :type BootTime: str
        :param LastLiveTime: 最后上线时间
        :type LastLiveTime: str
        :param Producer: 生产商
        :type Producer: str
        :param SerialNumber: 序列号
        :type SerialNumber: str
        :param NetCards: 网卡
        :type NetCards: list of AssetNetworkCardInfo
        :param Disks: 分区
        :type Disks: list of AssetDiskPartitionInfo
        :param Status: 0在线，1已离线
        :type Status: int
        :param ProjectId: 业务组ID
        :type ProjectId: int
        :param DeviceVersion: 设备型号
        :type DeviceVersion: str
        :param OfflineTime: 离线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineTime: str
        :param InstanceId: 主机ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Quuid = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Cpu = None
        self.MemSize = None
        self.MemLoad = None
        self.DiskSize = None
        self.DiskLoad = None
        self.PartitionCount = None
        self.MachineWanIp = None
        self.CpuSize = None
        self.CpuLoad = None
        self.ProtectLevel = None
        self.RiskStatus = None
        self.ProtectDays = None
        self.BuyTime = None
        self.EndTime = None
        self.CoreVersion = None
        self.OsType = None
        self.AgentVersion = None
        self.InstallTime = None
        self.BootTime = None
        self.LastLiveTime = None
        self.Producer = None
        self.SerialNumber = None
        self.NetCards = None
        self.Disks = None
        self.Status = None
        self.ProjectId = None
        self.DeviceVersion = None
        self.OfflineTime = None
        self.InstanceId = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Cpu = params.get("Cpu")
        self.MemSize = params.get("MemSize")
        self.MemLoad = params.get("MemLoad")
        self.DiskSize = params.get("DiskSize")
        self.DiskLoad = params.get("DiskLoad")
        self.PartitionCount = params.get("PartitionCount")
        self.MachineWanIp = params.get("MachineWanIp")
        self.CpuSize = params.get("CpuSize")
        self.CpuLoad = params.get("CpuLoad")
        self.ProtectLevel = params.get("ProtectLevel")
        self.RiskStatus = params.get("RiskStatus")
        self.ProtectDays = params.get("ProtectDays")
        self.BuyTime = params.get("BuyTime")
        self.EndTime = params.get("EndTime")
        self.CoreVersion = params.get("CoreVersion")
        self.OsType = params.get("OsType")
        self.AgentVersion = params.get("AgentVersion")
        self.InstallTime = params.get("InstallTime")
        self.BootTime = params.get("BootTime")
        self.LastLiveTime = params.get("LastLiveTime")
        self.Producer = params.get("Producer")
        self.SerialNumber = params.get("SerialNumber")
        if params.get("NetCards") is not None:
            self.NetCards = []
            for item in params.get("NetCards"):
                obj = AssetNetworkCardInfo()
                obj._deserialize(item)
                self.NetCards.append(obj)
        if params.get("Disks") is not None:
            self.Disks = []
            for item in params.get("Disks"):
                obj = AssetDiskPartitionInfo()
                obj._deserialize(item)
                self.Disks.append(obj)
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.DeviceVersion = params.get("DeviceVersion")
        self.OfflineTime = params.get("OfflineTime")
        self.InstanceId = params.get("InstanceId")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetNetworkCardInfo(AbstractModel):
    """资产管理网卡信息

    """

    def __init__(self):
        r"""
        :param Name: 网卡名称
        :type Name: str
        :param Ip: Ipv4对应IP
        :type Ip: str
        :param GateWay: 网关
        :type GateWay: str
        :param Mac: MAC地址
        :type Mac: str
        :param Ipv6: Ipv6对应IP
        :type Ipv6: str
        :param DnsServer: DNS服务器
        :type DnsServer: str
        """
        self.Name = None
        self.Ip = None
        self.GateWay = None
        self.Mac = None
        self.Ipv6 = None
        self.DnsServer = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Ip = params.get("Ip")
        self.GateWay = params.get("GateWay")
        self.Mac = params.get("Mac")
        self.Ipv6 = params.get("Ipv6")
        self.DnsServer = params.get("DnsServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetPlanTask(AbstractModel):
    """资产管理计划任务列表

    """

    def __init__(self):
        r"""
        :param Status: 默认启用状态：1启用，2未启用
        :type Status: int
        :param Cycle: 执行周期
        :type Cycle: str
        :param Command: 执行命令或脚本
        :type Command: str
        :param User: 启动用户
        :type User: str
        :param ConfigPath: 配置文件路径
        :type ConfigPath: str
        :param MachineIp: 服务器IP
        :type MachineIp: str
        :param MachineName: 服务器名称
        :type MachineName: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机uuid
        :type Uuid: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        :param MachineWanIp: 服务器外网IP
        :type MachineWanIp: str
        """
        self.Status = None
        self.Cycle = None
        self.Command = None
        self.User = None
        self.ConfigPath = None
        self.MachineIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Quuid = None
        self.Uuid = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None
        self.MachineWanIp = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Cycle = params.get("Cycle")
        self.Command = params.get("Command")
        self.User = params.get("User")
        self.ConfigPath = params.get("ConfigPath")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        self.MachineWanIp = params.get("MachineWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetPortBaseInfo(AbstractModel):
    """资源管理账号基本信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ProcessVersion: 进程版本
        :type ProcessVersion: str
        :param ProcessPath: 进程路径
        :type ProcessPath: str
        :param Pid: 进程ID
        :type Pid: str
        :param User: 运行用户
        :type User: str
        :param StartTime: 启动时间
        :type StartTime: str
        :param Param: 启动参数
        :type Param: str
        :param Teletype: 进程TTY
        :type Teletype: str
        :param Port: 端口
        :type Port: str
        :param GroupName: 所属用户组
        :type GroupName: str
        :param Md5: 进程MD5
        :type Md5: str
        :param Ppid: 父进程ID
        :type Ppid: str
        :param ParentProcessName: 父进程名称
        :type ParentProcessName: str
        :param Proto: 端口协议
        :type Proto: str
        :param BindIp: 绑定IP
        :type BindIp: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.OsInfo = None
        self.ProjectId = None
        self.Tag = None
        self.ProcessName = None
        self.ProcessVersion = None
        self.ProcessPath = None
        self.Pid = None
        self.User = None
        self.StartTime = None
        self.Param = None
        self.Teletype = None
        self.Port = None
        self.GroupName = None
        self.Md5 = None
        self.Ppid = None
        self.ParentProcessName = None
        self.Proto = None
        self.BindIp = None
        self.MachineName = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.OsInfo = params.get("OsInfo")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.ProcessName = params.get("ProcessName")
        self.ProcessVersion = params.get("ProcessVersion")
        self.ProcessPath = params.get("ProcessPath")
        self.Pid = params.get("Pid")
        self.User = params.get("User")
        self.StartTime = params.get("StartTime")
        self.Param = params.get("Param")
        self.Teletype = params.get("Teletype")
        self.Port = params.get("Port")
        self.GroupName = params.get("GroupName")
        self.Md5 = params.get("Md5")
        self.Ppid = params.get("Ppid")
        self.ParentProcessName = params.get("ParentProcessName")
        self.Proto = params.get("Proto")
        self.BindIp = params.get("BindIp")
        self.MachineName = params.get("MachineName")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetProcessBaseInfo(AbstractModel):
    """资源管理进程基本信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param Name: 进程名称
        :type Name: str
        :param Desc: 进程说明
        :type Desc: str
        :param Path: 进程路径
        :type Path: str
        :param Pid: 进程ID
        :type Pid: str
        :param User: 运行用户
        :type User: str
        :param StartTime: 启动时间
        :type StartTime: str
        :param Param: 启动参数
        :type Param: str
        :param Tty: 进程TTY
        :type Tty: str
        :param Version: 进程版本
        :type Version: str
        :param GroupName: 进程用户组
        :type GroupName: str
        :param Md5: 进程MD5
        :type Md5: str
        :param Ppid: 父进程ID
        :type Ppid: str
        :param ParentProcessName: 父进程名称
        :type ParentProcessName: str
        :param Status: 进程状态
        :type Status: str
        :param HasSign: 数字签名:0无，1有， 999 空，仅windows
        :type HasSign: int
        :param InstallByPackage: 是否通过安装包安装：:0否，1是， 999 空，仅linux
        :type InstallByPackage: int
        :param PackageName: 软件包名
        :type PackageName: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.OsInfo = None
        self.ProjectId = None
        self.Tag = None
        self.Name = None
        self.Desc = None
        self.Path = None
        self.Pid = None
        self.User = None
        self.StartTime = None
        self.Param = None
        self.Tty = None
        self.Version = None
        self.GroupName = None
        self.Md5 = None
        self.Ppid = None
        self.ParentProcessName = None
        self.Status = None
        self.HasSign = None
        self.InstallByPackage = None
        self.PackageName = None
        self.MachineName = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.OsInfo = params.get("OsInfo")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Path = params.get("Path")
        self.Pid = params.get("Pid")
        self.User = params.get("User")
        self.StartTime = params.get("StartTime")
        self.Param = params.get("Param")
        self.Tty = params.get("Tty")
        self.Version = params.get("Version")
        self.GroupName = params.get("GroupName")
        self.Md5 = params.get("Md5")
        self.Ppid = params.get("Ppid")
        self.ParentProcessName = params.get("ParentProcessName")
        self.Status = params.get("Status")
        self.HasSign = params.get("HasSign")
        self.InstallByPackage = params.get("InstallByPackage")
        self.PackageName = params.get("PackageName")
        self.MachineName = params.get("MachineName")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetSystemPackageInfo(AbstractModel):
    """资源管理系统安装包列表信息

    """

    def __init__(self):
        r"""
        :param Name: 数据库名
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Version: 版本
        :type Version: str
        :param InstallTime: 安装时间
        :type InstallTime: str
        :param Type: 类型
        :type Type: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param MachineIp: 主机IP
        :type MachineIp: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        """
        self.Name = None
        self.Desc = None
        self.Version = None
        self.InstallTime = None
        self.Type = None
        self.MachineName = None
        self.MachineIp = None
        self.OsInfo = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Version = params.get("Version")
        self.InstallTime = params.get("InstallTime")
        self.Type = params.get("Type")
        self.MachineName = params.get("MachineName")
        self.MachineIp = params.get("MachineIp")
        self.OsInfo = params.get("OsInfo")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetUserBaseInfo(AbstractModel):
    """资源管理账号基本信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uid: 账号UID
        :type Uid: str
        :param Gid: 账号GID
        :type Gid: str
        :param Status: 账号状态：0-禁用；1-启用
        :type Status: int
        :param IsRoot: 是否有root权限：0-否；1是，999为空: 仅linux
        :type IsRoot: int
        :param LoginType: 登录方式：0-不可登录；1-只允许key登录；2只允许密码登录；3-允许key和密码，999为空，仅linux
        :type LoginType: int
        :param LastLoginTime: 上次登录时间
        :type LastLoginTime: str
        :param Name: 账号名称
        :type Name: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param UserType: 账号类型：0访客用户，1标准用户，2管理员用户 ,999为空,仅windows
        :type UserType: int
        :param IsDomain: 是否域账号：0否， 1是，2否, 999为空  仅windows
        :type IsDomain: int
        :param IsSudo: 是否有sudo权限，1是，0否, 999为空, 仅linux
        :type IsSudo: int
        :param IsSshLogin: 是否允许ssh登录，1是，0否, 999为空, 仅linux
        :type IsSshLogin: int
        :param HomePath: Home目录
        :type HomePath: str
        :param Shell: Shell路径  仅linux
        :type Shell: str
        :param ShellLoginStatus: 是否shell登录性，0不是；1是 仅linux
        :type ShellLoginStatus: int
        :param PasswordChangeTime: 密码修改时间
        :type PasswordChangeTime: str
        :param PasswordDueTime: 密码过期时间  仅linux
        :type PasswordDueTime: str
        :param PasswordLockDays: 密码锁定时间：单位天, -1为永不锁定 999为空，仅linux
        :type PasswordLockDays: int
        :param PasswordStatus: 密码状态：1正常 2即将过期 3已过期 4已锁定 999为空 仅linux
        :type PasswordStatus: int
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Uuid = None
        self.Quuid = None
        self.Uid = None
        self.Gid = None
        self.Status = None
        self.IsRoot = None
        self.LoginType = None
        self.LastLoginTime = None
        self.Name = None
        self.ProjectId = None
        self.UserType = None
        self.IsDomain = None
        self.IsSudo = None
        self.IsSshLogin = None
        self.HomePath = None
        self.Shell = None
        self.ShellLoginStatus = None
        self.PasswordChangeTime = None
        self.PasswordDueTime = None
        self.PasswordLockDays = None
        self.PasswordStatus = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Uid = params.get("Uid")
        self.Gid = params.get("Gid")
        self.Status = params.get("Status")
        self.IsRoot = params.get("IsRoot")
        self.LoginType = params.get("LoginType")
        self.LastLoginTime = params.get("LastLoginTime")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.UserType = params.get("UserType")
        self.IsDomain = params.get("IsDomain")
        self.IsSudo = params.get("IsSudo")
        self.IsSshLogin = params.get("IsSshLogin")
        self.HomePath = params.get("HomePath")
        self.Shell = params.get("Shell")
        self.ShellLoginStatus = params.get("ShellLoginStatus")
        self.PasswordChangeTime = params.get("PasswordChangeTime")
        self.PasswordDueTime = params.get("PasswordDueTime")
        self.PasswordLockDays = params.get("PasswordLockDays")
        self.PasswordStatus = params.get("PasswordStatus")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetUserDetail(AbstractModel):
    """资源管理账号基本信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uid: 账号UID
        :type Uid: str
        :param Gid: 账号GID
        :type Gid: str
        :param Status: 账号状态：0-禁用；1-启用
        :type Status: int
        :param IsRoot: 是否有root权限：0-否；1是，999为空: 仅linux
        :type IsRoot: int
        :param LastLoginTime: 上次登录时间
        :type LastLoginTime: str
        :param Name: 账号名称
        :type Name: str
        :param UserType: 账号类型：0访客用户，1标准用户，2管理员用户 ,999为空,仅windows
        :type UserType: int
        :param IsDomain: 是否域账号：0否， 1是, 999为空  仅windows
        :type IsDomain: int
        :param IsSshLogin: 是否允许ssh登录，1是，0否, 999为空, 仅linux
        :type IsSshLogin: int
        :param HomePath: Home目录
        :type HomePath: str
        :param Shell: Shell路径  仅linux
        :type Shell: str
        :param ShellLoginStatus: 是否shell登录性，0不是；1是 仅linux
        :type ShellLoginStatus: int
        :param PasswordChangeTime: 密码修改时间
        :type PasswordChangeTime: str
        :param PasswordDueTime: 密码过期时间  仅linux
        :type PasswordDueTime: str
        :param PasswordLockDays: 密码锁定时间：单位天, -1为永不锁定 999为空，仅linux
        :type PasswordLockDays: int
        :param Remark: 备注
        :type Remark: str
        :param GroupName: 用户组名
        :type GroupName: str
        :param DisableTime: 账号到期时间
        :type DisableTime: str
        :param LastLoginTerminal: 最近登录终端
        :type LastLoginTerminal: str
        :param LastLoginLoc: 最近登录位置
        :type LastLoginLoc: str
        :param LastLoginIp: 最近登录IP
        :type LastLoginIp: str
        :param PasswordWarnDays: 密码过期提醒：单位天
        :type PasswordWarnDays: int
        :param PasswordChangeType: 密码修改设置：0-不可修改，1-可修改
        :type PasswordChangeType: int
        :param Keys: 用户公钥列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of AssetUserKeyInfo
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.MachineIp = None
        self.MachineName = None
        self.Uuid = None
        self.Quuid = None
        self.Uid = None
        self.Gid = None
        self.Status = None
        self.IsRoot = None
        self.LastLoginTime = None
        self.Name = None
        self.UserType = None
        self.IsDomain = None
        self.IsSshLogin = None
        self.HomePath = None
        self.Shell = None
        self.ShellLoginStatus = None
        self.PasswordChangeTime = None
        self.PasswordDueTime = None
        self.PasswordLockDays = None
        self.Remark = None
        self.GroupName = None
        self.DisableTime = None
        self.LastLoginTerminal = None
        self.LastLoginLoc = None
        self.LastLoginIp = None
        self.PasswordWarnDays = None
        self.PasswordChangeType = None
        self.Keys = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Uid = params.get("Uid")
        self.Gid = params.get("Gid")
        self.Status = params.get("Status")
        self.IsRoot = params.get("IsRoot")
        self.LastLoginTime = params.get("LastLoginTime")
        self.Name = params.get("Name")
        self.UserType = params.get("UserType")
        self.IsDomain = params.get("IsDomain")
        self.IsSshLogin = params.get("IsSshLogin")
        self.HomePath = params.get("HomePath")
        self.Shell = params.get("Shell")
        self.ShellLoginStatus = params.get("ShellLoginStatus")
        self.PasswordChangeTime = params.get("PasswordChangeTime")
        self.PasswordDueTime = params.get("PasswordDueTime")
        self.PasswordLockDays = params.get("PasswordLockDays")
        self.Remark = params.get("Remark")
        self.GroupName = params.get("GroupName")
        self.DisableTime = params.get("DisableTime")
        self.LastLoginTerminal = params.get("LastLoginTerminal")
        self.LastLoginLoc = params.get("LastLoginLoc")
        self.LastLoginIp = params.get("LastLoginIp")
        self.PasswordWarnDays = params.get("PasswordWarnDays")
        self.PasswordChangeType = params.get("PasswordChangeType")
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = AssetUserKeyInfo()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetUserKeyInfo(AbstractModel):
    """资产管理账号key详情

    """

    def __init__(self):
        r"""
        :param Value: 公钥值
        :type Value: str
        :param Comment: 公钥备注
        :type Comment: str
        :param EncryptType: 加密方式
        :type EncryptType: str
        """
        self.Value = None
        self.Comment = None
        self.EncryptType = None


    def _deserialize(self, params):
        self.Value = params.get("Value")
        self.Comment = params.get("Comment")
        self.EncryptType = params.get("EncryptType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetWebAppBaseInfo(AbstractModel):
    """资源管理Web应用列表信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param Name: 应用名
        :type Name: str
        :param Version: 版本
        :type Version: str
        :param RootPath: 根路径
        :type RootPath: str
        :param ServiceType: 服务类型
        :type ServiceType: str
        :param Domain: 站点域名
        :type Domain: str
        :param VirtualPath: 虚拟路径
        :type VirtualPath: str
        :param PluginCount: 插件数
        :type PluginCount: int
        :param Id: 应用ID
        :type Id: str
        :param Desc: 应用描述
        :type Desc: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.OsInfo = None
        self.ProjectId = None
        self.Tag = None
        self.Name = None
        self.Version = None
        self.RootPath = None
        self.ServiceType = None
        self.Domain = None
        self.VirtualPath = None
        self.PluginCount = None
        self.Id = None
        self.Desc = None
        self.MachineName = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.OsInfo = params.get("OsInfo")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.RootPath = params.get("RootPath")
        self.ServiceType = params.get("ServiceType")
        self.Domain = params.get("Domain")
        self.VirtualPath = params.get("VirtualPath")
        self.PluginCount = params.get("PluginCount")
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        self.MachineName = params.get("MachineName")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetWebAppPluginInfo(AbstractModel):
    """资产管理Web应用插件详情

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Version: 版本
        :type Version: str
        :param Link: 链接
        :type Link: str
        """
        self.Name = None
        self.Desc = None
        self.Version = None
        self.Link = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Version = params.get("Version")
        self.Link = params.get("Link")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetWebFrameBaseInfo(AbstractModel):
    """资源管理Web应用列表信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param Name: 数据库名
        :type Name: str
        :param Version: 版本
        :type Version: str
        :param Lang: 语言
        :type Lang: str
        :param ServiceType: 服务类型
        :type ServiceType: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.OsInfo = None
        self.ProjectId = None
        self.Tag = None
        self.Name = None
        self.Version = None
        self.Lang = None
        self.ServiceType = None
        self.MachineName = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.OsInfo = params.get("OsInfo")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Lang = params.get("Lang")
        self.ServiceType = params.get("ServiceType")
        self.MachineName = params.get("MachineName")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetWebLocationBaseInfo(AbstractModel):
    """资产管理Web站点列表信息

    """

    def __init__(self):
        r"""
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param MachineIp: 内网IP
        :type MachineIp: str
        :param MachineWanIp: 外网IP
        :type MachineWanIp: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param OsInfo: 操作系统
        :type OsInfo: str
        :param Name: 域名
        :type Name: str
        :param Port: 站点端口
        :type Port: str
        :param Proto: 站点协议
        :type Proto: str
        :param ServiceType: 服务类型
        :type ServiceType: str
        :param PathCount: 站点路经数
        :type PathCount: int
        :param User: 运行用户
        :type User: str
        :param MainPath: 主目录
        :type MainPath: str
        :param MainPathOwner: 主目录所有者
        :type MainPathOwner: str
        :param Permission: 拥有者权限
        :type Permission: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
        :type Tag: list of MachineTag
        :param Id: Web站点Id
        :type Id: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNew: int
        """
        self.Uuid = None
        self.Quuid = None
        self.MachineIp = None
        self.MachineWanIp = None
        self.MachineName = None
        self.OsInfo = None
        self.Name = None
        self.Port = None
        self.Proto = None
        self.ServiceType = None
        self.PathCount = None
        self.User = None
        self.MainPath = None
        self.MainPathOwner = None
        self.Permission = None
        self.ProjectId = None
        self.Tag = None
        self.Id = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineName = params.get("MachineName")
        self.OsInfo = params.get("OsInfo")
        self.Name = params.get("Name")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")
        self.ServiceType = params.get("ServiceType")
        self.PathCount = params.get("PathCount")
        self.User = params.get("User")
        self.MainPath = params.get("MainPath")
        self.MainPathOwner = params.get("MainPathOwner")
        self.Permission = params.get("Permission")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Id = params.get("Id")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetWebLocationInfo(AbstractModel):
    """资产管理Web站点列表信息

    """

    def __init__(self):
        r"""
        :param Name: 域名
        :type Name: str
        :param Port: 站点端口
        :type Port: str
        :param Proto: 站点协议
        :type Proto: str
        :param ServiceType: 服务类型
        :type ServiceType: str
        :param SafeStatus: 安全模块状态：0未启用，1启用，999空，仅nginx
        :type SafeStatus: int
        :param User: 运行用户
        :type User: str
        :param MainPath: 主目录
        :type MainPath: str
        :param Command: 启动命令
        :type Command: str
        :param Ip: 绑定IP
        :type Ip: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Name = None
        self.Port = None
        self.Proto = None
        self.ServiceType = None
        self.SafeStatus = None
        self.User = None
        self.MainPath = None
        self.Command = None
        self.Ip = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")
        self.ServiceType = params.get("ServiceType")
        self.SafeStatus = params.get("SafeStatus")
        self.User = params.get("User")
        self.MainPath = params.get("MainPath")
        self.Command = params.get("Command")
        self.Ip = params.get("Ip")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetWebServiceBaseInfo(AbstractModel):
    """资源管理Web服务列表信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param OsInfo: 操作系统信息
        :type OsInfo: str
        :param ProjectId: 主机业务组ID
        :type ProjectId: int
        :param Tag: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of MachineTag
        :param Name: 数据库名
        :type Name: str
        :param Version: 版本
        :type Version: str
        :param BinPath: 二进制路径
        :type BinPath: str
        :param User: 启动用户
        :type User: str
        :param InstallPath: 安装路径
        :type InstallPath: str
        :param ConfigPath: 配置路径
        :type ConfigPath: str
        :param ProcessCount: 关联进程数
        :type ProcessCount: int
        :param Id: Web服务ID
        :type Id: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param Desc: 描述
        :type Desc: str
        :param UpdateTime: 数据更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param FirstTime: 首次采集时间
        :type FirstTime: str
        :param IsNew: 是否新增[0:否|1:是]
        :type IsNew: int
        """
        self.MachineIp = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.OsInfo = None
        self.ProjectId = None
        self.Tag = None
        self.Name = None
        self.Version = None
        self.BinPath = None
        self.User = None
        self.InstallPath = None
        self.ConfigPath = None
        self.ProcessCount = None
        self.Id = None
        self.MachineName = None
        self.Desc = None
        self.UpdateTime = None
        self.FirstTime = None
        self.IsNew = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.OsInfo = params.get("OsInfo")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.BinPath = params.get("BinPath")
        self.User = params.get("User")
        self.InstallPath = params.get("InstallPath")
        self.ConfigPath = params.get("ConfigPath")
        self.ProcessCount = params.get("ProcessCount")
        self.Id = params.get("Id")
        self.MachineName = params.get("MachineName")
        self.Desc = params.get("Desc")
        self.UpdateTime = params.get("UpdateTime")
        self.FirstTime = params.get("FirstTime")
        self.IsNew = params.get("IsNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BanWhiteListDetail(AbstractModel):
    """阻断白名单展示列表，包含了机器的信息

    """

    def __init__(self):
        r"""
        :param Id: 白名单ID
        :type Id: str
        :param Remark: 白名单别名
        :type Remark: str
        :param SrcIp: 阻断来源IP
        :type SrcIp: str
        :param ModifyTime: 修改白名单时间
        :type ModifyTime: str
        :param CreateTime: 创建白名单时间
        :type CreateTime: str
        :param IsGlobal: 白名单是否全局
        :type IsGlobal: bool
        :param Quuid: 机器的UUID
        :type Quuid: str
        :param Uuid: 主机安全程序的UUID
        :type Uuid: str
        :param MachineIp: 机器IP
        :type MachineIp: str
        :param MachineName: 机器名称
        :type MachineName: str
        """
        self.Id = None
        self.Remark = None
        self.SrcIp = None
        self.ModifyTime = None
        self.CreateTime = None
        self.IsGlobal = None
        self.Quuid = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Remark = params.get("Remark")
        self.SrcIp = params.get("SrcIp")
        self.ModifyTime = params.get("ModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.IsGlobal = params.get("IsGlobal")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineBasicInfo(AbstractModel):
    """基线基础信息

    """

    def __init__(self):
        r"""
        :param Name: 基线名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param BaselineId: 基线id
注意：此字段可能返回 null，表示取不到有效值。
        :type BaselineId: int
        :param ParentId: 父级id
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: int
        """
        self.Name = None
        self.BaselineId = None
        self.ParentId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BaselineId = params.get("BaselineId")
        self.ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineDetail(AbstractModel):
    """基线详情

    """

    def __init__(self):
        r"""
        :param Description: 基线描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Level: 危害等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param PackageName: package名
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param ParentId: 父级id
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentId: int
        :param Name: 基线名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Description = None
        self.Level = None
        self.PackageName = None
        self.ParentId = None
        self.Name = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.Level = params.get("Level")
        self.PackageName = params.get("PackageName")
        self.ParentId = params.get("ParentId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineEffectHost(AbstractModel):
    """基线影响主机信息

    """

    def __init__(self):
        r"""
        :param PassCount: 通过项
注意：此字段可能返回 null，表示取不到有效值。
        :type PassCount: int
        :param FailCount: 风险项
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCount: int
        :param FirstScanTime: 首次检测事件
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstScanTime: str
        :param LastScanTime: 最后检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param Status: 风险项处理状态状态：0-未通过，1-通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Quuid: 主机Quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param HostIp: 主机IP
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIp: str
        :param AliasName: 主机别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param Uuid: 主机Uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param MaxStatus: 检测中状态
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStatus: int
        """
        self.PassCount = None
        self.FailCount = None
        self.FirstScanTime = None
        self.LastScanTime = None
        self.Status = None
        self.Quuid = None
        self.HostIp = None
        self.AliasName = None
        self.Uuid = None
        self.MaxStatus = None


    def _deserialize(self, params):
        self.PassCount = params.get("PassCount")
        self.FailCount = params.get("FailCount")
        self.FirstScanTime = params.get("FirstScanTime")
        self.LastScanTime = params.get("LastScanTime")
        self.Status = params.get("Status")
        self.Quuid = params.get("Quuid")
        self.HostIp = params.get("HostIp")
        self.AliasName = params.get("AliasName")
        self.Uuid = params.get("Uuid")
        self.MaxStatus = params.get("MaxStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineEventLevelInfo(AbstractModel):
    """服务器风险Top的主机信息

    """

    def __init__(self):
        r"""
        :param EventLevel: 危害等级：1-低危；2-中危；3-高危；4-严重
注意：此字段可能返回 null，表示取不到有效值。
        :type EventLevel: int
        :param EventCount: 漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCount: int
        """
        self.EventLevel = None
        self.EventCount = None


    def _deserialize(self, params):
        self.EventLevel = params.get("EventLevel")
        self.EventCount = params.get("EventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineHostTopList(AbstractModel):
    """基线影响服务器列表数据

    """

    def __init__(self):
        r"""
        :param EventLevelList: 事件等级与次数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventLevelList: list of BaselineEventLevelInfo
        :param HostName: 主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param Quuid: 主机Quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param Score: 计算权重的分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self.EventLevelList = None
        self.HostName = None
        self.Quuid = None
        self.Score = None


    def _deserialize(self, params):
        if params.get("EventLevelList") is not None:
            self.EventLevelList = []
            for item in params.get("EventLevelList"):
                obj = BaselineEventLevelInfo()
                obj._deserialize(item)
                self.EventLevelList.append(obj)
        self.HostName = params.get("HostName")
        self.Quuid = params.get("Quuid")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineInfo(AbstractModel):
    """基线信息

    """

    def __init__(self):
        r"""
        :param Name: 基线名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Level: 危害等级：1-低危；2-中危；3-高危；4-严重
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param RuleCount: 检测项数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCount: int
        :param HostCount: 影响服务器数量
注意：此字段可能返回 null，表示取不到有效值。
        :type HostCount: int
        :param Status: 通过状态:0:未通过,1:已通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CategoryId: 基线id
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryId: int
        :param LastScanTime: 最后检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param MaxStatus: 检测中状态: 5
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStatus: int
        :param BaselineFailCount: 基线风险项
注意：此字段可能返回 null，表示取不到有效值。
        :type BaselineFailCount: int
        """
        self.Name = None
        self.Level = None
        self.RuleCount = None
        self.HostCount = None
        self.Status = None
        self.CategoryId = None
        self.LastScanTime = None
        self.MaxStatus = None
        self.BaselineFailCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.RuleCount = params.get("RuleCount")
        self.HostCount = params.get("HostCount")
        self.Status = params.get("Status")
        self.CategoryId = params.get("CategoryId")
        self.LastScanTime = params.get("LastScanTime")
        self.MaxStatus = params.get("MaxStatus")
        self.BaselineFailCount = params.get("BaselineFailCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineRuleInfo(AbstractModel):
    """基线检测信息

    """

    def __init__(self):
        r"""
        :param RuleName: 检测项名称
        :type RuleName: str
        :param Description: 检测项描述
        :type Description: str
        :param FixMessage: 修复建议
        :type FixMessage: str
        :param Level: 危害等级
        :type Level: int
        :param Status: 状态
        :type Status: int
        :param RuleId: 检测项id
        :type RuleId: int
        :param LastScanAt: 最后检测时间
        :type LastScanAt: str
        :param RuleRemark: 具体原因说明
        :type RuleRemark: str
        :param Uuid: 唯一Uuid
        :type Uuid: str
        :param EventId: 唯一事件ID
        :type EventId: int
        """
        self.RuleName = None
        self.Description = None
        self.FixMessage = None
        self.Level = None
        self.Status = None
        self.RuleId = None
        self.LastScanAt = None
        self.RuleRemark = None
        self.Uuid = None
        self.EventId = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Description = params.get("Description")
        self.FixMessage = params.get("FixMessage")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.RuleId = params.get("RuleId")
        self.LastScanAt = params.get("LastScanAt")
        self.RuleRemark = params.get("RuleRemark")
        self.Uuid = params.get("Uuid")
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineRuleTopInfo(AbstractModel):
    """基线检测项TOP信息

    """

    def __init__(self):
        r"""
        :param RuleName: 基线检测项名
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param Level: 检测项危害等级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param EventCount: 事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type EventCount: int
        :param RuleId: 检测项id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        """
        self.RuleName = None
        self.Level = None
        self.EventCount = None
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.Level = params.get("Level")
        self.EventCount = params.get("EventCount")
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BashEvent(AbstractModel):
    """高危命令数据

    """

    def __init__(self):
        r"""
        :param Id: 数据ID
        :type Id: int
        :param Uuid: 云镜ID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param User: 执行用户名
        :type User: str
        :param Platform: 平台类型
        :type Platform: int
        :param BashCmd: 执行命令
        :type BashCmd: str
        :param RuleId: 规则ID
        :type RuleId: int
        :param RuleName: 规则名称
        :type RuleName: str
        :param RuleLevel: 规则等级：1-高 2-中 3-低
        :type RuleLevel: int
        :param Status: 处理状态： 0 = 待处理 1= 已处理, 2 = 已加白， 3 = 已忽略
        :type Status: int
        :param CreateTime: 发生时间
        :type CreateTime: str
        :param MachineName: 主机名
        :type MachineName: str
        :param DetectBy: 0: bash日志 1: 实时监控(雷霆版)
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectBy: int
        :param Pid: 进程id
注意：此字段可能返回 null，表示取不到有效值。
        :type Pid: str
        :param Exe: 进程名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Exe: str
        :param ModifyTime: 处理时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param RuleCategory: 规则类别  0=系统规则，1=用户规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCategory: int
        :param RegexBashCmd: 自动生成的正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type RegexBashCmd: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.User = None
        self.Platform = None
        self.BashCmd = None
        self.RuleId = None
        self.RuleName = None
        self.RuleLevel = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None
        self.DetectBy = None
        self.Pid = None
        self.Exe = None
        self.ModifyTime = None
        self.RuleCategory = None
        self.RegexBashCmd = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.User = params.get("User")
        self.Platform = params.get("Platform")
        self.BashCmd = params.get("BashCmd")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RuleLevel = params.get("RuleLevel")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.DetectBy = params.get("DetectBy")
        self.Pid = params.get("Pid")
        self.Exe = params.get("Exe")
        self.ModifyTime = params.get("ModifyTime")
        self.RuleCategory = params.get("RuleCategory")
        self.RegexBashCmd = params.get("RegexBashCmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BashRule(AbstractModel):
    """高危命令规则

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param Name: 规则名称
        :type Name: str
        :param Level: 危险等级(0 ：无 1: 高危 2:中危 3: 低危)
        :type Level: int
        :param Rule: 正则表达式
        :type Rule: str
        :param Decription: 规则描述
        :type Decription: str
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        :param Uuids: 生效服务器的uuid数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuids: list of str
        :param White: 0=黑名单 1=白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type White: int
        :param DealOldEvents: 是否处理之前的事件 0: 不处理 1:处理
注意：此字段可能返回 null，表示取不到有效值。
        :type DealOldEvents: int
        """
        self.Id = None
        self.Uuid = None
        self.Name = None
        self.Level = None
        self.Rule = None
        self.Decription = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None
        self.Uuids = None
        self.White = None
        self.DealOldEvents = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Rule = params.get("Rule")
        self.Decription = params.get("Decription")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")
        self.Uuids = params.get("Uuids")
        self.White = params.get("White")
        self.DealOldEvents = params.get("DealOldEvents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BruteAttackInfo(AbstractModel):
    """密码破解列表实体

    """

    def __init__(self):
        r"""
        :param Id: 唯一Id
        :type Id: int
        :param Uuid: 云镜客户端唯一标识UUID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param MachineIp: 主机ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineIp: str
        :param MachineName: 主机名
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineName: str
        :param UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param SrcIp: 来源ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcIp: str
        :param Status: SUCCESS：破解成功；FAILED：破解失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Country: 国家id
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: int
        :param City: 城市id
注意：此字段可能返回 null，表示取不到有效值。
        :type City: int
        :param Province: 省份id
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param BanStatus: 阻断状态：1-阻断成功；非1-阻断失败
注意：此字段可能返回 null，表示取不到有效值。
        :type BanStatus: int
        :param EventType: 事件类型：200-暴力破解事件，300-暴力破解成功事件（页面展示），400-暴力破解不存在的帐号事件
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType: int
        :param Count: 发生次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param Quuid: 机器UUID
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param IsProVersion: 是否为专业版（true/false）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsProVersion: bool
        :param Protocol: 被攻击的服务的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param ModifyTime: 最近攻击时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param DataStatus: 0：待处理，1：忽略，5：已处理，6：加入白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type DataStatus: int
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.UserName = None
        self.SrcIp = None
        self.Status = None
        self.Country = None
        self.City = None
        self.Province = None
        self.CreateTime = None
        self.BanStatus = None
        self.EventType = None
        self.Count = None
        self.Quuid = None
        self.IsProVersion = None
        self.Protocol = None
        self.Port = None
        self.ModifyTime = None
        self.InstanceId = None
        self.DataStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.Status = params.get("Status")
        self.Country = params.get("Country")
        self.City = params.get("City")
        self.Province = params.get("Province")
        self.CreateTime = params.get("CreateTime")
        self.BanStatus = params.get("BanStatus")
        self.EventType = params.get("EventType")
        self.Count = params.get("Count")
        self.Quuid = params.get("Quuid")
        self.IsProVersion = params.get("IsProVersion")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.ModifyTime = params.get("ModifyTime")
        self.InstanceId = params.get("InstanceId")
        self.DataStatus = params.get("DataStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BruteAttackRule(AbstractModel):
    """标准阻断模式规则

    """

    def __init__(self):
        r"""
        :param TimeRange: 爆破事件发生的时间范围，单位：秒
        :type TimeRange: int
        :param LoginFailTimes: 爆破事件失败次数
        :type LoginFailTimes: int
        """
        self.TimeRange = None
        self.LoginFailTimes = None


    def _deserialize(self, params):
        self.TimeRange = params.get("TimeRange")
        self.LoginFailTimes = params.get("LoginFailTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BruteAttackRuleList(AbstractModel):
    """暴力破解判定规则列表

    """

    def __init__(self):
        r"""
        :param TimeRange: 爆破事件发生的时间范围，单位：秒
        :type TimeRange: int
        :param LoginFailTimes: 爆破事件失败次数
        :type LoginFailTimes: int
        :param Enable: 规则是否为空，为空则填充默认规则
        :type Enable: bool
        :param TimeRangeDefault: 爆破事件发生的时间范围，单位：秒（默认规则）
        :type TimeRangeDefault: int
        :param LoginFailTimesDefault: 爆破事件失败次数（默认规则）
        :type LoginFailTimesDefault: int
        """
        self.TimeRange = None
        self.LoginFailTimes = None
        self.Enable = None
        self.TimeRangeDefault = None
        self.LoginFailTimesDefault = None


    def _deserialize(self, params):
        self.TimeRange = params.get("TimeRange")
        self.LoginFailTimes = params.get("LoginFailTimes")
        self.Enable = params.get("Enable")
        self.TimeRangeDefault = params.get("TimeRangeDefault")
        self.LoginFailTimesDefault = params.get("LoginFailTimesDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelIgnoreVulRequest(AbstractModel):
    """CancelIgnoreVul请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIds: 漏洞事件id串，多个用英文逗号分隔
        :type EventIds: str
        """
        self.EventIds = None


    def _deserialize(self, params):
        self.EventIds = params.get("EventIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelIgnoreVulResponse(AbstractModel):
    """CancelIgnoreVul返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChangeRuleEventsIgnoreStatusRequest(AbstractModel):
    """ChangeRuleEventsIgnoreStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param IgnoreStatus: 忽略状态 0:取消忽略 ； 1:忽略
        :type IgnoreStatus: int
        :param RuleIdList: 检测项id数组
        :type RuleIdList: list of int non-negative
        :param EventIdList: 事件id数组
        :type EventIdList: list of int non-negative
        """
        self.IgnoreStatus = None
        self.RuleIdList = None
        self.EventIdList = None


    def _deserialize(self, params):
        self.IgnoreStatus = params.get("IgnoreStatus")
        self.RuleIdList = params.get("RuleIdList")
        self.EventIdList = params.get("EventIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeRuleEventsIgnoreStatusResponse(AbstractModel):
    """ChangeRuleEventsIgnoreStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckBashRuleParamsRequest(AbstractModel):
    """CheckBashRuleParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param CheckField: 校验内容 Name或Rule ，两个都要校验时逗号分割
        :type CheckField: str
        :param EventId: 在事件列表中新增白名时需要提交事件ID
        :type EventId: int
        :param Name: 填入的规则名称
        :type Name: str
        :param Rule: 用户填入的正则表达式："正则表达式" 需与 "提交EventId对应的命令内容" 相匹配
        :type Rule: str
        :param Id: 编辑时传的规则id
        :type Id: int
        """
        self.CheckField = None
        self.EventId = None
        self.Name = None
        self.Rule = None
        self.Id = None


    def _deserialize(self, params):
        self.CheckField = params.get("CheckField")
        self.EventId = params.get("EventId")
        self.Name = params.get("Name")
        self.Rule = params.get("Rule")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBashRuleParamsResponse(AbstractModel):
    """CheckBashRuleParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 0=校验通过  1=规则名称校验不通过 2=正则表达式校验不通过
        :type ErrCode: int
        :param ErrMsg: 校验信息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class ComponentStatistics(AbstractModel):
    """组件统计数据。

    """

    def __init__(self):
        r"""
        :param Id: 组件ID。
        :type Id: int
        :param MachineNum: 主机数量。
        :type MachineNum: int
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ComponentType: 组件类型。
<li>WEB：Web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param Description: 组件描述。
        :type Description: str
        """
        self.Id = None
        self.MachineNum = None
        self.ComponentName = None
        self.ComponentType = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineNum = params.get("MachineNum")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaselineStrategyRequest(AbstractModel):
    """CreateBaselineStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param StrategyName: 策略名称
        :type StrategyName: str
        :param ScanCycle: 检测周期, 表示每隔多少天进行检测.示例: 2, 表示每2天进行检测一次.
        :type ScanCycle: int
        :param ScanAt: 定期检测时间，该时间下发扫描. 示例:“22:00”, 表示在22:00下发检测
        :type ScanAt: str
        :param CategoryIds: 该策略下选择的基线id数组. 示例: [1,3,5,7]
        :type CategoryIds: list of int non-negative
        :param IsGlobal: 扫描范围是否全部服务器, 1:是  0:否, 为1则为全部专业版主机
        :type IsGlobal: int
        :param MachineType: 云主机类型：
CVM：虚拟主机
BM：裸金属
ECM：边缘计算主机
LH：轻量应用服务器
Other：混合云机器
        :type MachineType: str
        :param RegionCode: 主机地域. 示例: "ap-guangzhou"
        :type RegionCode: str
        :param Quuids: 主机id数组. 示例: ["quuid1","quuid2"]
        :type Quuids: list of str
        """
        self.StrategyName = None
        self.ScanCycle = None
        self.ScanAt = None
        self.CategoryIds = None
        self.IsGlobal = None
        self.MachineType = None
        self.RegionCode = None
        self.Quuids = None


    def _deserialize(self, params):
        self.StrategyName = params.get("StrategyName")
        self.ScanCycle = params.get("ScanCycle")
        self.ScanAt = params.get("ScanAt")
        self.CategoryIds = params.get("CategoryIds")
        self.IsGlobal = params.get("IsGlobal")
        self.MachineType = params.get("MachineType")
        self.RegionCode = params.get("RegionCode")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaselineStrategyResponse(AbstractModel):
    """CreateBaselineStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEmergencyVulScanRequest(AbstractModel):
    """CreateEmergencyVulScan请求参数结构体

    """

    def __init__(self):
        r"""
        :param VulId: 漏洞id
        :type VulId: int
        :param Uuids: 自选服务器时生效，主机uuid的string数组
        :type Uuids: list of str
        """
        self.VulId = None
        self.Uuids = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Uuids = params.get("Uuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmergencyVulScanResponse(AbstractModel):
    """CreateEmergencyVulScan返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLicenseOrderRequest(AbstractModel):
    """CreateLicenseOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param Tags: 标签数组, 空则表示不需要绑定标签
        :type Tags: list of Tags
        :param LicenseType: 授权类型, 0 专业版-按量计费, 1专业版-包年包月 , 2 旗舰版-包年包月
默认为0
        :type LicenseType: int
        :param LicenseNum: 授权数量 , 需要购买的数量.
默认为1
        :type LicenseNum: int
        :param RegionId: 购买订单地域,这里仅支持 1 广州,9 新加坡. 推荐选择广州. 新加坡地域为白名单用户购买.
默认为1
        :type RegionId: int
        :param ProjectId: 项目ID .
默认为0
        :type ProjectId: int
        :param TimeSpan: 购买时间长度,默认1 , 可选值为1,2,3,4,5,6,7,8,9,10,11,12,24,36
该参数仅包年包月生效
        :type TimeSpan: int
        :param AutoRenewFlag: 是否自动续费, 默认不自动续费.
该参数仅包年包月生效
        :type AutoRenewFlag: bool
        :param AutoProtectOpenConfig: 自动防护授权配置值, 不空则表示开启
        :type AutoProtectOpenConfig: str
        """
        self.Tags = None
        self.LicenseType = None
        self.LicenseNum = None
        self.RegionId = None
        self.ProjectId = None
        self.TimeSpan = None
        self.AutoRenewFlag = None
        self.AutoProtectOpenConfig = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.LicenseType = params.get("LicenseType")
        self.LicenseNum = params.get("LicenseNum")
        self.RegionId = params.get("RegionId")
        self.ProjectId = params.get("ProjectId")
        self.TimeSpan = params.get("TimeSpan")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoProtectOpenConfig = params.get("AutoProtectOpenConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLicenseOrderResponse(AbstractModel):
    """CreateLicenseOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param DealNames: 订单号列表
        :type DealNames: list of str
        :param ResourceIds: 资源ID列表,预付费订单该字段空值
        :type ResourceIds: list of str
        :param BigDealId: 大订单号 , 后付费该字段空值
        :type BigDealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.ResourceIds = None
        self.BigDealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.ResourceIds = params.get("ResourceIds")
        self.BigDealId = params.get("BigDealId")
        self.RequestId = params.get("RequestId")


class CreateProtectServerRequest(AbstractModel):
    """CreateProtectServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProtectDir: 防护目录地址
        :type ProtectDir: str
        :param ProtectHostConfig: 防护机器 信息
        :type ProtectHostConfig: list of ProtectHostConfig
        """
        self.ProtectDir = None
        self.ProtectHostConfig = None


    def _deserialize(self, params):
        self.ProtectDir = params.get("ProtectDir")
        if params.get("ProtectHostConfig") is not None:
            self.ProtectHostConfig = []
            for item in params.get("ProtectHostConfig"):
                obj = ProtectHostConfig()
                obj._deserialize(item)
                self.ProtectHostConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProtectServerResponse(AbstractModel):
    """CreateProtectServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateScanMalwareSettingRequest(AbstractModel):
    """CreateScanMalwareSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ScanPattern: 扫描模式 0 全盘扫描, 1 快速扫描
        :type ScanPattern: int
        :param HostType: 服务器分类：1:专业版服务器；2:自选服务器
        :type HostType: int
        :param QuuidList: 自选服务器时生效，主机quuid的string数组
        :type QuuidList: list of str
        :param TimeoutPeriod: 超时时间单位 秒 默认3600 秒
        :type TimeoutPeriod: int
        :param EngineType: 1标准模式（只报严重、高危）、2增强模式（报严重、高危、中危）、3严格模式（报严重、高、中、低、提示）
        :type EngineType: int
        """
        self.ScanPattern = None
        self.HostType = None
        self.QuuidList = None
        self.TimeoutPeriod = None
        self.EngineType = None


    def _deserialize(self, params):
        self.ScanPattern = params.get("ScanPattern")
        self.HostType = params.get("HostType")
        self.QuuidList = params.get("QuuidList")
        self.TimeoutPeriod = params.get("TimeoutPeriod")
        self.EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScanMalwareSettingResponse(AbstractModel):
    """CreateScanMalwareSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSearchLogRequest(AbstractModel):
    """CreateSearchLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchContent: 搜索内容
        :type SearchContent: str
        """
        self.SearchContent = None


    def _deserialize(self, params):
        self.SearchContent = params.get("SearchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSearchLogResponse(AbstractModel):
    """CreateSearchLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 0：成功，非0：失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CreateSearchTemplateRequest(AbstractModel):
    """CreateSearchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param SearchTemplate: 搜索模板
        :type SearchTemplate: :class:`tencentcloud.cwp.v20180228.models.SearchTemplate`
        """
        self.SearchTemplate = None


    def _deserialize(self, params):
        if params.get("SearchTemplate") is not None:
            self.SearchTemplate = SearchTemplate()
            self.SearchTemplate._deserialize(params.get("SearchTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSearchTemplateResponse(AbstractModel):
    """CreateSearchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 0：成功，非0：失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DefendAttackLog(AbstractModel):
    """网络攻击日志

    """

    def __init__(self):
        r"""
        :param Id: 日志ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param SrcIp: 来源IP
        :type SrcIp: str
        :param SrcPort: 来源端口
        :type SrcPort: int
        :param HttpMethod: 攻击方式
        :type HttpMethod: str
        :param HttpCgi: 攻击描述
        :type HttpCgi: str
        :param HttpParam: 攻击参数
        :type HttpParam: str
        :param VulType: 威胁类型
        :type VulType: str
        :param CreatedAt: 攻击时间
        :type CreatedAt: str
        :param MachineIp: 目标服务器IP
        :type MachineIp: str
        :param MachineName: 目标服务器名称
        :type MachineName: str
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: int
        :param HttpContent: 攻击内容
        :type HttpContent: str
        """
        self.Id = None
        self.Uuid = None
        self.SrcIp = None
        self.SrcPort = None
        self.HttpMethod = None
        self.HttpCgi = None
        self.HttpParam = None
        self.VulType = None
        self.CreatedAt = None
        self.MachineIp = None
        self.MachineName = None
        self.DstIp = None
        self.DstPort = None
        self.HttpContent = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.SrcIp = params.get("SrcIp")
        self.SrcPort = params.get("SrcPort")
        self.HttpMethod = params.get("HttpMethod")
        self.HttpCgi = params.get("HttpCgi")
        self.HttpParam = params.get("HttpParam")
        self.VulType = params.get("VulType")
        self.CreatedAt = params.get("CreatedAt")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.HttpContent = params.get("HttpContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttackLogsRequest(AbstractModel):
    """DeleteAttackLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 日志ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttackLogsResponse(AbstractModel):
    """DeleteAttackLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBaselineStrategyRequest(AbstractModel):
    """DeleteBaselineStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param StrategyId: 基线策略id
        :type StrategyId: int
        """
        self.StrategyId = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBaselineStrategyResponse(AbstractModel):
    """DeleteBaselineStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBashEventsRequest(AbstractModel):
    """DeleteBashEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBashEventsResponse(AbstractModel):
    """DeleteBashEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBashRulesRequest(AbstractModel):
    """DeleteBashRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBashRulesResponse(AbstractModel):
    """DeleteBashRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 暴力破解事件Id数组。(最大 100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLicenseRecordRequest(AbstractModel):
    """DeleteLicenseRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param LicenseId: 授权ID ,可以用授权订单列表获取.
        :type LicenseId: int
        :param LicenseType: 授权类型
        :type LicenseType: int
        :param ResourceId: 资源ID
        :type ResourceId: str
        """
        self.LicenseId = None
        self.LicenseType = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.LicenseId = params.get("LicenseId")
        self.LicenseType = params.get("LicenseType")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLicenseRecordResponse(AbstractModel):
    """DeleteLicenseRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoginWhiteListRequest(AbstractModel):
    """DeleteLoginWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 白名单ID (最大 100 条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoginWhiteListResponse(AbstractModel):
    """DeleteLoginWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 云镜客户端Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineTagRequest(AbstractModel):
    """DeleteMachineTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param Rid: 关联的标签ID
        :type Rid: int
        """
        self.Rid = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineTagResponse(AbstractModel):
    """DeleteMachineTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 恶意请求记录ID数组，(最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwareScanTaskRequest(AbstractModel):
    """DeleteMalwareScanTask请求参数结构体

    """


class DeleteMalwareScanTaskResponse(AbstractModel):
    """DeleteMalwareScanTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 木马记录ID数组 (最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param DelType: 删除异地登录事件的方式，可选值："Ids"、"Ip"、"All"，默认为Ids
        :type DelType: str
        :param Ids: 异地登录事件ID数组。DelType为Ids或DelType未填时此项必填
        :type Ids: list of int non-negative
        :param Ip: 异地登录事件的Ip。DelType为Ip时必填
        :type Ip: list of str
        :param Uuid: 主机Uuid
        :type Uuid: str
        """
        self.DelType = None
        self.Ids = None
        self.Ip = None
        self.Uuid = None


    def _deserialize(self, params):
        self.DelType = params.get("DelType")
        self.Ids = params.get("Ids")
        self.Ip = params.get("Ip")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivilegeEventsRequest(AbstractModel):
    """DeletePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: ID数组. (最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivilegeEventsResponse(AbstractModel):
    """DeletePrivilegeEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivilegeRulesRequest(AbstractModel):
    """DeletePrivilegeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivilegeRulesResponse(AbstractModel):
    """DeletePrivilegeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProtectDirRequest(AbstractModel):
    """DeleteProtectDir请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 删除的目录ID 最大100条
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProtectDirResponse(AbstractModel):
    """DeleteProtectDir返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReverseShellEventsRequest(AbstractModel):
    """DeleteReverseShellEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: ID数组. (最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellEventsResponse(AbstractModel):
    """DeleteReverseShellEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReverseShellRulesRequest(AbstractModel):
    """DeleteReverseShellRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: ID数组. (最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellRulesResponse(AbstractModel):
    """DeleteReverseShellRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSearchTemplateRequest(AbstractModel):
    """DeleteSearchTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 模板ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSearchTemplateResponse(AbstractModel):
    """DeleteSearchTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 0：成功，非0：失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 标签ID (最大100 条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagsResponse(AbstractModel):
    """DeleteTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWebPageEventLogRequest(AbstractModel):
    """DeleteWebPageEventLog请求参数结构体

    """


class DeleteWebPageEventLogResponse(AbstractModel):
    """DeleteWebPageEventLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号用户名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 帐号统计列表记录总数。
        :type TotalCount: int
        :param AccountStatistics: 帐号统计列表。
        :type AccountStatistics: list of AccountStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self.AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self.AccountStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetAppListRequest(AbstractModel):
    """DescribeAssetAppList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>AppName- string - 是否必填：否 - 应用名搜索</li>
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Type - int - 是否必填：否 - 类型	: 仅linux
0: 全部
1: 运维
2 : 数据库
3 : 安全
4 : 可疑应用
5 : 系统架构
6 : 系统应用
7 : WEB服务
99:其他</li>
<li>OsType - uint64 - 是否必填：否 - windows/linux</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of AssetFilters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime|ProcessCount]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetAppListResponse(AbstractModel):
    """DescribeAssetAppList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Apps: 应用列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Apps: list of AssetAppBaseInfo
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Apps = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Apps") is not None:
            self.Apps = []
            for item in params.get("Apps"):
                obj = AssetAppBaseInfo()
                obj._deserialize(item)
                self.Apps.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetAppProcessListRequest(AbstractModel):
    """DescribeAssetAppProcessList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Name: App名
        :type Name: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        """
        self.Quuid = None
        self.Uuid = None
        self.Name = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetAppProcessListResponse(AbstractModel):
    """DescribeAssetAppProcessList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Process: 进程列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: list of AssetAppProcessInfo
        :param Total: 分区总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Process = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Process") is not None:
            self.Process = []
            for item in params.get("Process"):
                obj = AssetAppProcessInfo()
                obj._deserialize(item)
                self.Process.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetCoreModuleInfoRequest(AbstractModel):
    """DescribeAssetCoreModuleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Id: 内核模块ID
        :type Id: str
        """
        self.Quuid = None
        self.Uuid = None
        self.Id = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetCoreModuleInfoResponse(AbstractModel):
    """DescribeAssetCoreModuleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Module: 内核模块详情
        :type Module: :class:`tencentcloud.cwp.v20180228.models.AssetCoreModuleDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Module = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Module") is not None:
            self.Module = AssetCoreModuleDetail()
            self.Module._deserialize(params.get("Module"))
        self.RequestId = params.get("RequestId")


class DescribeAssetCoreModuleListRequest(AbstractModel):
    """DescribeAssetCoreModuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name- string - 是否必填：否 - 包名</li>
<li>User- string - 是否必填：否 - 用户</li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序依据[Size|FirstTime|ProcessCount|ModuleCount]
        :type By: str
        """
        self.Uuid = None
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetCoreModuleListResponse(AbstractModel):
    """DescribeAssetCoreModuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Modules: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Modules: list of AssetCoreModuleBaseInfo
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Modules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Modules") is not None:
            self.Modules = []
            for item in params.get("Modules"):
                obj = AssetCoreModuleBaseInfo()
                obj._deserialize(item)
                self.Modules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetDatabaseInfoRequest(AbstractModel):
    """DescribeAssetDatabaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Id: 数据库ID
        :type Id: str
        """
        self.Quuid = None
        self.Uuid = None
        self.Id = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDatabaseInfoResponse(AbstractModel):
    """DescribeAssetDatabaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Database: 数据库详情
        :type Database: :class:`tencentcloud.cwp.v20180228.models.AssetDatabaseDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Database = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Database") is not None:
            self.Database = AssetDatabaseDetail()
            self.Database._deserialize(params.get("Database"))
        self.RequestId = params.get("RequestId")


class DescribeAssetDatabaseListRequest(AbstractModel):
    """DescribeAssetDatabaseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>User- string - 是否必填：否 - 运行用户</li>
<li>Ip - String - 是否必填：否 - 绑定IP</li>
<li>Port - Int - 是否必填：否 - 端口</li>
<li>Name - Int - 是否必填：否 - 数据库名称
0:全部
1:MySQL
2:Redis
3:Oracle
4:MongoDB
5:MemCache
6:PostgreSQL
7:HBase
8:DB2
9:Sybase
10:TiDB</li>
<li>Proto - String - 是否必填：否 - 协议：1:TCP, 2:UDP, 3:未知</li>
<li>OsType - String - 是否必填：否 - 操作系统: linux/windows</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetDatabaseListResponse(AbstractModel):
    """DescribeAssetDatabaseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Databases: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of AssetDatabaseBaseInfo
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Databases = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = AssetDatabaseBaseInfo()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetEnvListRequest(AbstractModel):
    """DescribeAssetEnvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Type: 该字段已废弃，由Filters代替
        :type Type: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name- string - 是否必填：否 - 环境变量名</li>
<li>Type- int - 是否必填：否 - 类型：0用户变量，1系统变量</li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime]
        :type By: str
        """
        self.Uuid = None
        self.Quuid = None
        self.Type = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Type = params.get("Type")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetEnvListResponse(AbstractModel):
    """DescribeAssetEnvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Envs: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Envs: list of AssetEnvBaseInfo
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Envs = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = AssetEnvBaseInfo()
                obj._deserialize(item)
                self.Envs.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetInfoRequest(AbstractModel):
    """DescribeAssetInfo请求参数结构体

    """


class DescribeAssetInfoResponse(AbstractModel):
    """DescribeAssetInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param MachineCount: 主机数
        :type MachineCount: int
        :param AccountCount: 账号数
        :type AccountCount: int
        :param PortCount: 端口数
        :type PortCount: int
        :param ProcessCount: 进程数
        :type ProcessCount: int
        :param SoftwareCount: 软件数
        :type SoftwareCount: int
        :param DatabaseCount: 数据库数
        :type DatabaseCount: int
        :param WebAppCount: Web应用数
        :type WebAppCount: int
        :param WebFrameCount: Web框架数
        :type WebFrameCount: int
        :param WebServiceCount: Web服务数
        :type WebServiceCount: int
        :param WebLocationCount: Web站点数
        :type WebLocationCount: int
        :param AccountNewCount: 账号今日新增
        :type AccountNewCount: int
        :param PortNewCount: 端口今日新增
        :type PortNewCount: int
        :param ProcessNewCount: 进程今日新增
        :type ProcessNewCount: int
        :param SoftwareNewCount: 软件今日新增
        :type SoftwareNewCount: int
        :param DatabaseNewCount: 数据库今日新增
        :type DatabaseNewCount: int
        :param WebAppNewCount: Web应用今日新增
        :type WebAppNewCount: int
        :param WebFrameNewCount: Web框架今日新增
        :type WebFrameNewCount: int
        :param WebServiceNewCount: Web服务今日新增
        :type WebServiceNewCount: int
        :param WebLocationNewCount: Web站点今日新增
        :type WebLocationNewCount: int
        :param MachineNewCount: 主机今日新增
        :type MachineNewCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineCount = None
        self.AccountCount = None
        self.PortCount = None
        self.ProcessCount = None
        self.SoftwareCount = None
        self.DatabaseCount = None
        self.WebAppCount = None
        self.WebFrameCount = None
        self.WebServiceCount = None
        self.WebLocationCount = None
        self.AccountNewCount = None
        self.PortNewCount = None
        self.ProcessNewCount = None
        self.SoftwareNewCount = None
        self.DatabaseNewCount = None
        self.WebAppNewCount = None
        self.WebFrameNewCount = None
        self.WebServiceNewCount = None
        self.WebLocationNewCount = None
        self.MachineNewCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineCount = params.get("MachineCount")
        self.AccountCount = params.get("AccountCount")
        self.PortCount = params.get("PortCount")
        self.ProcessCount = params.get("ProcessCount")
        self.SoftwareCount = params.get("SoftwareCount")
        self.DatabaseCount = params.get("DatabaseCount")
        self.WebAppCount = params.get("WebAppCount")
        self.WebFrameCount = params.get("WebFrameCount")
        self.WebServiceCount = params.get("WebServiceCount")
        self.WebLocationCount = params.get("WebLocationCount")
        self.AccountNewCount = params.get("AccountNewCount")
        self.PortNewCount = params.get("PortNewCount")
        self.ProcessNewCount = params.get("ProcessNewCount")
        self.SoftwareNewCount = params.get("SoftwareNewCount")
        self.DatabaseNewCount = params.get("DatabaseNewCount")
        self.WebAppNewCount = params.get("WebAppNewCount")
        self.WebFrameNewCount = params.get("WebFrameNewCount")
        self.WebServiceNewCount = params.get("WebServiceNewCount")
        self.WebLocationNewCount = params.get("WebLocationNewCount")
        self.MachineNewCount = params.get("MachineNewCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetInitServiceListRequest(AbstractModel):
    """DescribeAssetInitServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name- string - 是否必填：否 - 包名</li>
<li>User- string - 是否必填：否 - 用户</li>
<li>Status- string - 是否必填：否 - 默认启用状态：0未启用， 1启用 仅linux</li>
<li>Type- string - 是否必填：否 - 类型：类型 仅windows：
1:编码器
2:IE插件
3:网络提供者
4:镜像劫持
5:LSA提供者
6:KnownDLLs
7:启动执行
8:WMI
9:计划任务
10:Winsock提供者
11:打印监控器
12:资源管理器
13:驱动服务
14:登录</li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime]
        :type By: str
        """
        self.Uuid = None
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetInitServiceListResponse(AbstractModel):
    """DescribeAssetInitServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Services: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of AssetInitServiceBaseInfo
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Services = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Services") is not None:
            self.Services = []
            for item in params.get("Services"):
                obj = AssetInitServiceBaseInfo()
                obj._deserialize(item)
                self.Services.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetJarInfoRequest(AbstractModel):
    """DescribeAssetJarInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Id: Jar包ID
        :type Id: str
        """
        self.Quuid = None
        self.Uuid = None
        self.Id = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetJarInfoResponse(AbstractModel):
    """DescribeAssetJarInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Jar: Jar包详情
        :type Jar: :class:`tencentcloud.cwp.v20180228.models.AssetJarDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Jar = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Jar") is not None:
            self.Jar = AssetJarDetail()
            self.Jar._deserialize(params.get("Jar"))
        self.RequestId = params.get("RequestId")


class DescribeAssetJarListRequest(AbstractModel):
    """DescribeAssetJarList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name- string - 是否必填：否 - 包名</li>
<li>Type- uint - 是否必填：否 - 类型	
1: 应用程序
2 : 系统类库
3 : Web服务自带库
4 : 其他依赖包</li>
<li>Status- string - 是否必填：否 - 是否可执行：0否，1是</li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime]
        :type By: str
        """
        self.Uuid = None
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetJarListResponse(AbstractModel):
    """DescribeAssetJarList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Jars: 应用列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Jars: list of AssetJarBaseInfo
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Jars = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Jars") is not None:
            self.Jars = []
            for item in params.get("Jars"):
                obj = AssetJarBaseInfo()
                obj._deserialize(item)
                self.Jars.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetMachineDetailRequest(AbstractModel):
    """DescribeAssetMachineDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Uuid: 服务器Uuid
        :type Uuid: str
        """
        self.Quuid = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetMachineDetailResponse(AbstractModel):
    """DescribeAssetMachineDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param MachineDetail: 主机详情
        :type MachineDetail: :class:`tencentcloud.cwp.v20180228.models.AssetMachineDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MachineDetail") is not None:
            self.MachineDetail = AssetMachineDetail()
            self.MachineDetail._deserialize(params.get("MachineDetail"))
        self.RequestId = params.get("RequestId")


class DescribeAssetMachineListRequest(AbstractModel):
    """DescribeAssetMachineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>OsType - String - 是否必填：否 - windows或linux</li>
<li>CpuLoad - Int - 是否必填：否 - 
0: 未知  1: 低负载
2: 中负载  3: 高负载</li>
<li>DiskLoad - Int - 是否必填：否 - 
0: 0%或未知  1: 0%～20%
2: 20%～50%  3: 50%～80%
4: 80%～100%</li>
<li>MemLoad - Int - 是否必填：否 - 
0: 0%或未知  1: 0%～20%
2: 20%～50%  3: 50%～80%
4: 80%～100%</li>
<li>Quuid：主机Quuid</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of Filter
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 可选排序[FirstTime|PartitionCount]
        :type By: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetMachineListResponse(AbstractModel):
    """DescribeAssetMachineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param Machines: 记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Machines: list of AssetMachineBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Machines = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = AssetMachineBaseInfo()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetPlanTaskListRequest(AbstractModel):
    """DescribeAssetPlanTaskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>User- string - 是否必填：否 - 用户</li>
<li>Status- int - 是否必填：否 - 默认启用状态：0未启用， 1启用 </li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime]
        :type By: str
        """
        self.Uuid = None
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetPlanTaskListResponse(AbstractModel):
    """DescribeAssetPlanTaskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tasks: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of AssetPlanTask
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tasks = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = AssetPlanTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetPortInfoListRequest(AbstractModel):
    """DescribeAssetPortInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>Port - uint64 - 是否必填：否 - 端口</li>
<li>Ip - String - 是否必填：否 - 绑定IP</li>
<li>ProcessName - String - 是否必填：否 - 监听进程</li>
<li>Pid - uint64 - 是否必填：否 - PID</li>
<li>User - String - 是否必填：否 - 运行用户</li>
<li>Group - String - 是否必填：否 - 所属用户组</li>
<li>Ppid - uint64 - 是否必填：否 - PPID</li>
<li>Proto - string - 是否必填：否 - tcp/udp或“”(空字符串筛选未知状态)</li>
<li>OsType - uint64 - 是否必填：否 - windows/linux</li>
<li>RunTimeStart - String - 是否必填：否 - 运行开始时间</li>
<li>RunTimeEnd - String - 是否必填：否 - 运行结束时间</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of Filter
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime|StartTime]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetPortInfoListResponse(AbstractModel):
    """DescribeAssetPortInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param Ports: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Ports: list of AssetPortBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Ports = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Ports") is not None:
            self.Ports = []
            for item in params.get("Ports"):
                obj = AssetPortBaseInfo()
                obj._deserialize(item)
                self.Ports.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetProcessInfoListRequest(AbstractModel):
    """DescribeAssetProcessInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name - String - 是否必填：否 - 进程名</li>
<li>User - String - 是否必填：否 - 进程用户</li>
<li>Group - String - 是否必填：否 - 进程用户组</li>
<li>Pid - uint64 - 是否必填：否 - 进程ID</li>
<li>Ppid - uint64 - 是否必填：否 - 父进程ID</li>
<li>OsType - uint64 - 是否必填：否 - windows/linux</li>
<li>Status - string - 是否必填：否 - 进程状态：
1:R 可执行
2:S 可中断
3:D 不可中断
4:T 暂停状态或跟踪状态
5:Z 僵尸状态
6:X 将被销毁</li>
<li>RunTimeStart - String - 是否必填：否 - 运行开始时间</li>
<li>RunTimeEnd - String - 是否必填：否 - 运行结束时间</li>
<li>InstallByPackage - uint64 - 是否必填：否 - 是否包安装：0否，1是</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of Filter
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序方式：[FirstTime|StartTime]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetProcessInfoListResponse(AbstractModel):
    """DescribeAssetProcessInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param Process: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: list of AssetProcessBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Process = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Process") is not None:
            self.Process = []
            for item in params.get("Process"):
                obj = AssetProcessBaseInfo()
                obj._deserialize(item)
                self.Process.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetRecentMachineInfoRequest(AbstractModel):
    """DescribeAssetRecentMachineInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginDate: 开始时间，如：2020-09-22
        :type BeginDate: str
        :param EndDate: 结束时间，如：2020-09-22
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetRecentMachineInfoResponse(AbstractModel):
    """DescribeAssetRecentMachineInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalList: 总数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalList: list of AssetKeyVal
        :param LiveList: 在线数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveList: list of AssetKeyVal
        :param OfflineList: 离线数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineList: list of AssetKeyVal
        :param RiskList: 风险数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskList: list of AssetKeyVal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalList = None
        self.LiveList = None
        self.OfflineList = None
        self.RiskList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TotalList") is not None:
            self.TotalList = []
            for item in params.get("TotalList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.TotalList.append(obj)
        if params.get("LiveList") is not None:
            self.LiveList = []
            for item in params.get("LiveList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.LiveList.append(obj)
        if params.get("OfflineList") is not None:
            self.OfflineList = []
            for item in params.get("OfflineList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.OfflineList.append(obj)
        if params.get("RiskList") is not None:
            self.RiskList = []
            for item in params.get("RiskList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.RiskList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetSystemPackageListRequest(AbstractModel):
    """DescribeAssetSystemPackageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Filters: 过滤条件。
<li>Name - String - 是否必填：否 - 包 名</li>
<li>StartTime - String - 是否必填：否 - 安装开始时间</li>
<li>EndTime - String - 是否必填：否 - 安装开始时间</li>
<li>Type - int - 是否必填：否 - 安装包类型：
1:rmp
2:dpkg
3:java
4:system</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc-升序 或 desc-降序。默认：desc-降序
        :type Order: str
        :param By: 排序方式可选：[FistTime|InstallTime:安装时间]
        :type By: str
        """
        self.Uuid = None
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetSystemPackageListResponse(AbstractModel):
    """DescribeAssetSystemPackageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param Packages: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Packages: list of AssetSystemPackageInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Packages = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Packages") is not None:
            self.Packages = []
            for item in params.get("Packages"):
                obj = AssetSystemPackageInfo()
                obj._deserialize(item)
                self.Packages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetUserInfoRequest(AbstractModel):
    """DescribeAssetUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 云服务器UUID
        :type Quuid: str
        :param Uuid: 主机安全UUID
        :type Uuid: str
        :param Name: 账户名
        :type Name: str
        """
        self.Quuid = None
        self.Uuid = None
        self.Name = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetUserInfoResponse(AbstractModel):
    """DescribeAssetUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param User: 用户详细信息
        :type User: :class:`tencentcloud.cwp.v20180228.models.AssetUserDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = AssetUserDetail()
            self.User._deserialize(params.get("User"))
        self.RequestId = params.get("RequestId")


class DescribeAssetUserListRequest(AbstractModel):
    """DescribeAssetUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name - String - 是否必填：否 - 账户名（模糊匹配）</li>
<li>NameStrict - String - 是否必填：否 - 账户名（严格匹配）</li>
<li>Uid - uint64 - 是否必填：否 - Uid</li>
<li>Guid - uint64 - 是否必填：否 - Guid</li>
<li>LoginTimeStart - String - 是否必填：否 - 开始时间，如：2021-01-11</li>
<li>LoginTimeEnd - String - 是否必填：否 - 结束时间，如：2021-01-11</li>
<li>LoginType - uint64 - 是否必填：否 - 0-不可登录；1-只允许key登录；2只允许密码登录；3-允许key和密码 仅linux</li>
<li>OsType - String - 是否必填：否 - windows或linux</li>
<li>Status - uint64 - 是否必填：否 - 账号状态：0-禁用；1-启用</li>
<li>UserType - uint64 - 是否必填：否 - 账号类型：0访客用户，1标准用户，2管理员用户 仅windows</li>
<li>IsDomain - uint64 - 是否必填：否 - 是否域账号：0 不是，1是 仅windows
<li>IsRoot - uint64 - 是否必填：否 - 是否Root权限：0 不是，1是 仅linux
<li>IsSudo - uint64 - 是否必填：否 - 是否Sudo权限：0 不是，1是 仅linux</li>
<li>IsSshLogin - uint64 - 是否必填：否 - 是否ssh登录：0 不是，1是 仅linux</li>
<li>ShellLoginStatus - uint64 - 是否必填：否 - 是否shell登录性，0不是；1是 仅linux</li>
<li>PasswordStatus - uint64 - 是否必填：否 - 密码状态：1正常 2即将过期 3已过期 4已锁定 仅linux</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of Filter
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 可选排序：[FirstTime|LoginTime|PasswordChangeTime|PasswordDuaTime]
PasswordLockDays
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetUserListResponse(AbstractModel):
    """DescribeAssetUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param Users: 账号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of AssetUserBaseInfo
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
                obj = AssetUserBaseInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetWebAppListRequest(AbstractModel):
    """DescribeAssetWebAppList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name - String - 是否必填：否 - 应用名</li>
<li>Domain - String - 是否必填：否 - 站点域名</li>
<li>Type - int - 是否必填：否 - 服务类型：
0：全部
1:Tomcat
2:Apache
3:Nginx
4:WebLogic
5:Websphere
6:JBoss
7:Jetty
8:IHS
9:Tengine</li>
<li>OsType - String - 是否必填：否 - windows/linux</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 可选排序：[FirstTime|PluginCount]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebAppListResponse(AbstractModel):
    """DescribeAssetWebAppList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param WebApps: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WebApps: list of AssetWebAppBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.WebApps = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("WebApps") is not None:
            self.WebApps = []
            for item in params.get("WebApps"):
                obj = AssetWebAppBaseInfo()
                obj._deserialize(item)
                self.WebApps.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetWebAppPluginListRequest(AbstractModel):
    """DescribeAssetWebAppPluginList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Id: Web应用ID
        :type Id: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        """
        self.Quuid = None
        self.Uuid = None
        self.Id = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Id = params.get("Id")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebAppPluginListResponse(AbstractModel):
    """DescribeAssetWebAppPluginList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Plugins: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Plugins: list of AssetWebAppPluginInfo
        :param Total: 分区总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Plugins = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Plugins") is not None:
            self.Plugins = []
            for item in params.get("Plugins"):
                obj = AssetWebAppPluginInfo()
                obj._deserialize(item)
                self.Plugins.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetWebFrameListRequest(AbstractModel):
    """DescribeAssetWebFrameList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name - String - 是否必填：否 - 框架名</li>
<li>NameStrict - String - 是否必填：否 - 框架名（严格匹配）</li>
<li>Lang - String - 是否必填：否 - 框架语言:java/python</li>
<li>Type - String - 是否必填：否 - 服务类型：
0：全部
1:Tomcat
2:Apache
3:Nginx
4:WebLogic
5:Websphere
6:JBoss
7:WildFly
8:Jetty
9:IHS
10:Tengine</li>
<li>OsType - String - 是否必填：否 - windows/linux</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 可选排序：[FirstTime|JarCount]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebFrameListResponse(AbstractModel):
    """DescribeAssetWebFrameList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param WebFrames: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WebFrames: list of AssetWebFrameBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.WebFrames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("WebFrames") is not None:
            self.WebFrames = []
            for item in params.get("WebFrames"):
                obj = AssetWebFrameBaseInfo()
                obj._deserialize(item)
                self.WebFrames.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetWebLocationInfoRequest(AbstractModel):
    """DescribeAssetWebLocationInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Id: 站点Id
        :type Id: str
        """
        self.Quuid = None
        self.Uuid = None
        self.Id = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebLocationInfoResponse(AbstractModel):
    """DescribeAssetWebLocationInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param WebLocation: 站点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type WebLocation: :class:`tencentcloud.cwp.v20180228.models.AssetWebLocationInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WebLocation = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WebLocation") is not None:
            self.WebLocation = AssetWebLocationInfo()
            self.WebLocation._deserialize(params.get("WebLocation"))
        self.RequestId = params.get("RequestId")


class DescribeAssetWebLocationListRequest(AbstractModel):
    """DescribeAssetWebLocationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Name - String - 是否必填：否 - 域名</li>
<li>User - String - 是否必填：否 - 运行用户</li>
<li>Port - uint64 - 是否必填：否 - 站点端口</li>
<li>Proto - uint64 - 是否必填：否 - 站点协议：1:HTTP,2:HTTPS</li>
<li>ServiceType - uint64 - 是否必填：否 - 服务类型：
1:Tomcat
2：Apache
3:Nginx
4:WebLogic
5:Websphere
6:JBoss
7:WildFly
8:Jetty
9:IHS
10:Tengine</li>
<li>OsType - String - 是否必填：否 - windows/linux</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 可选排序：[FirstTime|PathCount]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebLocationListResponse(AbstractModel):
    """DescribeAssetWebLocationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param Locations: 站点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Locations: list of AssetWebLocationBaseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Locations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Locations") is not None:
            self.Locations = []
            for item in params.get("Locations"):
                obj = AssetWebLocationBaseInfo()
                obj._deserialize(item)
                self.Locations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetWebServiceInfoListRequest(AbstractModel):
    """DescribeAssetWebServiceInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>User- string - 是否必填：否 - 运行用户</li>
<li>Name- string - 是否必填：否 - Web服务名：
1:Tomcat
2:Apache
3:Nginx
4:WebLogic
5:Websphere
6:JBoss
7:WildFly
8:Jetty
9:IHS
10:Tengine</li>
<li>OsType- string - 是否必填：否 - Windows/linux</li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )</li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 可选排序：[FirstTime|ProcessCount]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebServiceInfoListResponse(AbstractModel):
    """DescribeAssetWebServiceInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param WebServices: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WebServices: list of AssetWebServiceBaseInfo
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WebServices = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WebServices") is not None:
            self.WebServices = []
            for item in params.get("WebServices"):
                obj = AssetWebServiceBaseInfo()
                obj._deserialize(item)
                self.WebServices.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAssetWebServiceProcessListRequest(AbstractModel):
    """DescribeAssetWebServiceProcessList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 主机Quuid
        :type Quuid: str
        :param Uuid: 主机Uuid
        :type Uuid: str
        :param Id: Web服务ID
        :type Id: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        """
        self.Quuid = None
        self.Uuid = None
        self.Id = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Id = params.get("Id")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetWebServiceProcessListResponse(AbstractModel):
    """DescribeAssetWebServiceProcessList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Process: 进程列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: list of AssetAppProcessInfo
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Process = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Process") is not None:
            self.Process = []
            for item in params.get("Process"):
                obj = AssetAppProcessInfo()
                obj._deserialize(item)
                self.Process.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeAttackLogInfoRequest(AbstractModel):
    """DescribeAttackLogInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 日志ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttackLogInfoResponse(AbstractModel):
    """DescribeAttackLogInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 日志ID
        :type Id: int
        :param Quuid: 主机ID
        :type Quuid: str
        :param SrcPort: 攻击来源端口
        :type SrcPort: int
        :param SrcIp: 攻击来源IP
        :type SrcIp: str
        :param DstPort: 攻击目标端口
        :type DstPort: int
        :param DstIp: 攻击目标IP
        :type DstIp: str
        :param HttpMethod: 攻击方法
        :type HttpMethod: str
        :param HttpHost: 攻击目标主机
        :type HttpHost: str
        :param HttpHead: 攻击头信息
        :type HttpHead: str
        :param HttpUserAgent: 攻击者浏览器标识
        :type HttpUserAgent: str
        :param HttpReferer: 请求源
        :type HttpReferer: str
        :param VulType: 威胁类型
        :type VulType: str
        :param HttpCgi: 攻击路径
        :type HttpCgi: str
        :param HttpParam: 攻击参数
        :type HttpParam: str
        :param CreatedAt: 攻击时间
        :type CreatedAt: str
        :param HttpContent: 攻击内容
        :type HttpContent: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Quuid = None
        self.SrcPort = None
        self.SrcIp = None
        self.DstPort = None
        self.DstIp = None
        self.HttpMethod = None
        self.HttpHost = None
        self.HttpHead = None
        self.HttpUserAgent = None
        self.HttpReferer = None
        self.VulType = None
        self.HttpCgi = None
        self.HttpParam = None
        self.CreatedAt = None
        self.HttpContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.SrcPort = params.get("SrcPort")
        self.SrcIp = params.get("SrcIp")
        self.DstPort = params.get("DstPort")
        self.DstIp = params.get("DstIp")
        self.HttpMethod = params.get("HttpMethod")
        self.HttpHost = params.get("HttpHost")
        self.HttpHead = params.get("HttpHead")
        self.HttpUserAgent = params.get("HttpUserAgent")
        self.HttpReferer = params.get("HttpReferer")
        self.VulType = params.get("VulType")
        self.HttpCgi = params.get("HttpCgi")
        self.HttpParam = params.get("HttpParam")
        self.CreatedAt = params.get("CreatedAt")
        self.HttpContent = params.get("HttpContent")
        self.RequestId = params.get("RequestId")


class DescribeAttackLogsRequest(AbstractModel):
    """DescribeAttackLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>HttpMethod - String - 是否必填：否 - 攻击方法(POST|GET)</li>
<li>DateRange - String - 是否必填：否 - 时间范围(存储最近3个月的数据)，如最近一个月["2019-11-17", "2019-12-17"]</li>
<li>VulType - String 威胁类型 - 是否必填: 否</li>
<li>SrcIp - String 攻击源IP - 是否必填: 否</li>
<li>DstIp - String 攻击目标IP - 是否必填: 否</li>
<li>SrcPort - String 攻击源端口 - 是否必填: 否</li>
<li>DstPort - String 攻击目标端口 - 是否必填: 否</li>
        :type Filters: list of Filter
        :param Uuid: 主机安全客户端ID
        :type Uuid: str
        :param Quuid: 云主机机器ID
        :type Quuid: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttackLogsResponse(AbstractModel):
    """DescribeAttackLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param AttackLogs: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackLogs: list of DefendAttackLog
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AttackLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttackLogs") is not None:
            self.AttackLogs = []
            for item in params.get("AttackLogs"):
                obj = DefendAttackLog()
                obj._deserialize(item)
                self.AttackLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAttackVulTypeListRequest(AbstractModel):
    """DescribeAttackVulTypeList请求参数结构体

    """


class DescribeAttackVulTypeListResponse(AbstractModel):
    """DescribeAttackVulTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 威胁类型列表
        :type List: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.List = params.get("List")
        self.RequestId = params.get("RequestId")


class DescribeAvailableExpertServiceDetailRequest(AbstractModel):
    """DescribeAvailableExpertServiceDetail请求参数结构体

    """


class DescribeAvailableExpertServiceDetailResponse(AbstractModel):
    """DescribeAvailableExpertServiceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ExpertService: 安全管家订单
        :type ExpertService: list of ExpertServiceOrderInfo
        :param EmergencyResponse: 应急响应可用次数
        :type EmergencyResponse: int
        :param ProtectNet: 旗舰护网可用次数
        :type ProtectNet: int
        :param ExpertServiceBuy: 是否购买过安全管家
        :type ExpertServiceBuy: bool
        :param EmergencyResponseBuy: 是否购买过应急响应
        :type EmergencyResponseBuy: bool
        :param ProtectNetBuy: 是否购买过旗舰护网
        :type ProtectNetBuy: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExpertService = None
        self.EmergencyResponse = None
        self.ProtectNet = None
        self.ExpertServiceBuy = None
        self.EmergencyResponseBuy = None
        self.ProtectNetBuy = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ExpertService") is not None:
            self.ExpertService = []
            for item in params.get("ExpertService"):
                obj = ExpertServiceOrderInfo()
                obj._deserialize(item)
                self.ExpertService.append(obj)
        self.EmergencyResponse = params.get("EmergencyResponse")
        self.ProtectNet = params.get("ProtectNet")
        self.ExpertServiceBuy = params.get("ExpertServiceBuy")
        self.EmergencyResponseBuy = params.get("EmergencyResponseBuy")
        self.ProtectNetBuy = params.get("ProtectNetBuy")
        self.RequestId = params.get("RequestId")


class DescribeBanModeRequest(AbstractModel):
    """DescribeBanMode请求参数结构体

    """


class DescribeBanModeResponse(AbstractModel):
    """DescribeBanMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Mode: 阻断模式，STANDARD_MODE：标准阻断，DEEP_MODE：深度阻断
        :type Mode: str
        :param StandardModeConfig: 标准阻断模式的配置
        :type StandardModeConfig: :class:`tencentcloud.cwp.v20180228.models.StandardModeConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Mode = None
        self.StandardModeConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        if params.get("StandardModeConfig") is not None:
            self.StandardModeConfig = StandardModeConfig()
            self.StandardModeConfig._deserialize(params.get("StandardModeConfig"))
        self.RequestId = params.get("RequestId")


class DescribeBanRegionsRequest(AbstractModel):
    """DescribeBanRegions请求参数结构体

    """

    def __init__(self):
        r"""
        :param Mode: 阻断模式，STANDARD_MODE：标准阻断，DEEP_MODE：深度阻断
        :type Mode: str
        """
        self.Mode = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBanRegionsResponse(AbstractModel):
    """DescribeBanRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionSet: 地域信息列表
        :type RegionSet: list of RegionSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionSet()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBanStatusRequest(AbstractModel):
    """DescribeBanStatus请求参数结构体

    """


class DescribeBanStatusResponse(AbstractModel):
    """DescribeBanStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 阻断开关状态 0:关闭 1:开启
        :type Status: int
        :param ShowTips: 是否弹窗提示信息 false: 关闭，true: 开启
        :type ShowTips: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ShowTips = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ShowTips = params.get("ShowTips")
        self.RequestId = params.get("RequestId")


class DescribeBanWhiteListRequest(AbstractModel):
    """DescribeBanWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeBanWhiteListResponse(AbstractModel):
    """DescribeBanWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总记录数
        :type TotalCount: int
        :param WhiteList: 白名单列表
        :type WhiteList: list of BanWhiteListDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WhiteList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WhiteList") is not None:
            self.WhiteList = []
            for item in params.get("WhiteList"):
                obj = BanWhiteListDetail()
                obj._deserialize(item)
                self.WhiteList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaselineAnalysisDataRequest(AbstractModel):
    """DescribeBaselineAnalysisData请求参数结构体

    """

    def __init__(self):
        r"""
        :param StrategyId: 基线策略id
        :type StrategyId: int
        """
        self.StrategyId = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineAnalysisDataResponse(AbstractModel):
    """DescribeBaselineAnalysisData返回参数结构体

    """

    def __init__(self):
        r"""
        :param LatestScanTime: 最后检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestScanTime: str
        :param IsGlobal: 是否全部服务器：1-是 0-否
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGlobal: int
        :param ScanHostCount: 服务器总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanHostCount: int
        :param ScanRuleCount: 检测项总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanRuleCount: int
        :param IfFirstScan: 是否是第一次检测  1是 0不是
注意：此字段可能返回 null，表示取不到有效值。
        :type IfFirstScan: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LatestScanTime = None
        self.IsGlobal = None
        self.ScanHostCount = None
        self.ScanRuleCount = None
        self.IfFirstScan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LatestScanTime = params.get("LatestScanTime")
        self.IsGlobal = params.get("IsGlobal")
        self.ScanHostCount = params.get("ScanHostCount")
        self.ScanRuleCount = params.get("ScanRuleCount")
        self.IfFirstScan = params.get("IfFirstScan")
        self.RequestId = params.get("RequestId")


class DescribeBaselineBasicInfoRequest(AbstractModel):
    """DescribeBaselineBasicInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineName: 基线名称
        :type BaselineName: str
        """
        self.BaselineName = None


    def _deserialize(self, params):
        self.BaselineName = params.get("BaselineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineBasicInfoResponse(AbstractModel):
    """DescribeBaselineBasicInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineBasicInfoList: 基线基础信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BaselineBasicInfoList: list of BaselineBasicInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaselineBasicInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BaselineBasicInfoList") is not None:
            self.BaselineBasicInfoList = []
            for item in params.get("BaselineBasicInfoList"):
                obj = BaselineBasicInfo()
                obj._deserialize(item)
                self.BaselineBasicInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaselineDetailRequest(AbstractModel):
    """DescribeBaselineDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineId: 基线id
        :type BaselineId: int
        """
        self.BaselineId = None


    def _deserialize(self, params):
        self.BaselineId = params.get("BaselineId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineDetailResponse(AbstractModel):
    """DescribeBaselineDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineDetail: 基线详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BaselineDetail: :class:`tencentcloud.cwp.v20180228.models.BaselineDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaselineDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BaselineDetail") is not None:
            self.BaselineDetail = BaselineDetail()
            self.BaselineDetail._deserialize(params.get("BaselineDetail"))
        self.RequestId = params.get("RequestId")


class DescribeBaselineEffectHostListRequest(AbstractModel):
    """DescribeBaselineEffectHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页参数 最大100条
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param BaselineId: 基线id
        :type BaselineId: int
        :param Filters: 过滤条件。
<li>AliasName- String- 主机别名</li>
<li>Status- Uint- 1已通过  0未通过 5检测中</li>
        :type Filters: list of Filters
        :param StrategyId: 策略id
        :type StrategyId: int
        :param UuidList: 主机uuid数组
        :type UuidList: list of str
        """
        self.Limit = None
        self.Offset = None
        self.BaselineId = None
        self.Filters = None
        self.StrategyId = None
        self.UuidList = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BaselineId = params.get("BaselineId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.StrategyId = params.get("StrategyId")
        self.UuidList = params.get("UuidList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineEffectHostListResponse(AbstractModel):
    """DescribeBaselineEffectHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param EffectHostList: 影响服务器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectHostList: list of BaselineEffectHost
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EffectHostList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EffectHostList") is not None:
            self.EffectHostList = []
            for item in params.get("EffectHostList"):
                obj = BaselineEffectHost()
                obj._deserialize(item)
                self.EffectHostList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaselineHostTopRequest(AbstractModel):
    """DescribeBaselineHostTop请求参数结构体

    """

    def __init__(self):
        r"""
        :param Top: 动态top值
        :type Top: int
        :param StrategyId: 策略id
        :type StrategyId: int
        """
        self.Top = None
        self.StrategyId = None


    def _deserialize(self, params):
        self.Top = params.get("Top")
        self.StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineHostTopResponse(AbstractModel):
    """DescribeBaselineHostTop返回参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineHostTopList: 主机基线策略事件Top
注意：此字段可能返回 null，表示取不到有效值。
        :type BaselineHostTopList: list of BaselineHostTopList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaselineHostTopList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BaselineHostTopList") is not None:
            self.BaselineHostTopList = []
            for item in params.get("BaselineHostTopList"):
                obj = BaselineHostTopList()
                obj._deserialize(item)
                self.BaselineHostTopList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaselineListRequest(AbstractModel):
    """DescribeBaselineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页参数 最大100条
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param Filters: 过滤条件。
<li>StrategyId- Uint64 - 基线策略id</li>
<li>Status - Uint64 - 处理状态1已通过 0未通过</li>
<li>Level - Uint64[] - 处理状态1已通过 0未通过</li>BaselineName 
<li>BaselineName  - String - 基线名称</li>
<li>Quuid- String - 主机quuid</li>
<li>Uuid- String - 主机uuid</li>
        :type Filters: list of Filters
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineListResponse(AbstractModel):
    """DescribeBaselineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineList: 基线信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BaselineList: list of BaselineInfo
        :param TotalCount: 分页查询记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaselineList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BaselineList") is not None:
            self.BaselineList = []
            for item in params.get("BaselineList"):
                obj = BaselineInfo()
                obj._deserialize(item)
                self.BaselineList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBaselineRuleRequest(AbstractModel):
    """DescribeBaselineRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineId: 基线id
        :type BaselineId: int
        :param Limit: 分页参数 最大100条
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param Level: 危害等级
        :type Level: list of int non-negative
        :param Status: 状态
        :type Status: int
        :param Quuid: 主机quuid
        :type Quuid: str
        :param Uuid: 主机uuid
        :type Uuid: str
        """
        self.BaselineId = None
        self.Limit = None
        self.Offset = None
        self.Level = None
        self.Status = None
        self.Quuid = None
        self.Uuid = None


    def _deserialize(self, params):
        self.BaselineId = params.get("BaselineId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Level = params.get("Level")
        self.Status = params.get("Status")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineRuleResponse(AbstractModel):
    """DescribeBaselineRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 分页查询记录总数
        :type TotalCount: int
        :param BaselineRuleList: 基线检测项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BaselineRuleList: list of BaselineRuleInfo
        :param ShowRuleRemark: 是否显示说明列：true-是，false-否
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowRuleRemark: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BaselineRuleList = None
        self.ShowRuleRemark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BaselineRuleList") is not None:
            self.BaselineRuleList = []
            for item in params.get("BaselineRuleList"):
                obj = BaselineRuleInfo()
                obj._deserialize(item)
                self.BaselineRuleList.append(obj)
        self.ShowRuleRemark = params.get("ShowRuleRemark")
        self.RequestId = params.get("RequestId")


class DescribeBaselineScanScheduleRequest(AbstractModel):
    """DescribeBaselineScanSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineScanScheduleResponse(AbstractModel):
    """DescribeBaselineScanSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Schedule: 检测进度(百分比)
注意：此字段可能返回 null，表示取不到有效值。
        :type Schedule: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Schedule = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Schedule = params.get("Schedule")
        self.RequestId = params.get("RequestId")


class DescribeBaselineStrategyDetailRequest(AbstractModel):
    """DescribeBaselineStrategyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param StrategyId: 用户基线策略id
        :type StrategyId: int
        """
        self.StrategyId = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineStrategyDetailResponse(AbstractModel):
    """DescribeBaselineStrategyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param PassRate: 策略扫描通过率
注意：此字段可能返回 null，表示取不到有效值。
        :type PassRate: int
        :param StrategyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param ScanCycle: 策略扫描周期(天)
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanCycle: str
        :param ScanAt: 定期检测时间, 该时间下发扫描
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanAt: str
        :param IsGlobal: 扫描范围是否全部服务器, 1:是  0:否, 为1则为全部专业版主机
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGlobal: int
        :param MachineType: 云服务器类型：
cvm：腾讯云服务器
bm：裸金属
ecm：边缘计算主机
lh: 轻量应用服务器
ohter: 混合云机器
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineType: str
        :param Region: 主机地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Quuids: 用户该策略下的所有主机id
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuids: list of str
        :param CategoryIds: 用户该策略下所有的基线id
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryIds: list of str
        :param IfScanned: 1 表示扫描过, 0没扫描过
注意：此字段可能返回 null，表示取不到有效值。
        :type IfScanned: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PassRate = None
        self.StrategyName = None
        self.ScanCycle = None
        self.ScanAt = None
        self.IsGlobal = None
        self.MachineType = None
        self.Region = None
        self.Quuids = None
        self.CategoryIds = None
        self.IfScanned = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PassRate = params.get("PassRate")
        self.StrategyName = params.get("StrategyName")
        self.ScanCycle = params.get("ScanCycle")
        self.ScanAt = params.get("ScanAt")
        self.IsGlobal = params.get("IsGlobal")
        self.MachineType = params.get("MachineType")
        self.Region = params.get("Region")
        self.Quuids = params.get("Quuids")
        self.CategoryIds = params.get("CategoryIds")
        self.IfScanned = params.get("IfScanned")
        self.RequestId = params.get("RequestId")


class DescribeBaselineStrategyListRequest(AbstractModel):
    """DescribeBaselineStrategyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页参数 最大100
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param Enabled: 规则开关，1：打开 0：关闭  2:全部
        :type Enabled: int
        """
        self.Limit = None
        self.Offset = None
        self.Enabled = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineStrategyListResponse(AbstractModel):
    """DescribeBaselineStrategyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 分页查询记录的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param StrategyList: 用户策略信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyList: list of Strategy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.StrategyList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("StrategyList") is not None:
            self.StrategyList = []
            for item in params.get("StrategyList"):
                obj = Strategy()
                obj._deserialize(item)
                self.StrategyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaselineTopRequest(AbstractModel):
    """DescribeBaselineTop请求参数结构体

    """

    def __init__(self):
        r"""
        :param Top: 动态top值
        :type Top: int
        :param StrategyId: 策略id
        :type StrategyId: int
        """
        self.Top = None
        self.StrategyId = None


    def _deserialize(self, params):
        self.Top = params.get("Top")
        self.StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBaselineTopResponse(AbstractModel):
    """DescribeBaselineTop返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleTopList: 检测项Top列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTopList: list of BaselineRuleTopInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleTopList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleTopList") is not None:
            self.RuleTopList = []
            for item in params.get("RuleTopList"):
                obj = BaselineRuleTopInfo()
                obj._deserialize(item)
                self.RuleTopList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBashEventsRequest(AbstractModel):
    """DescribeBashEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机内网IP)</li>
        :type Filters: list of Filter
        :param Order: 排序方式：根据请求次数排序：asc-升序/desc-降序
        :type Order: str
        :param By: 排序字段：CreateTime-发生时间。ModifyTime-处理时间
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBashEventsResponse(AbstractModel):
    """DescribeBashEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 高危命令事件列表
        :type List: list of BashEvent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BashEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBashRulesRequest(AbstractModel):
    """DescribeBashRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 0-系统规则; 1-用户规则
        :type Type: int
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(规则名称)</li>
        :type Filters: list of Filter
        """
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeBashRulesResponse(AbstractModel):
    """DescribeBashRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 列表内容
        :type List: list of BashRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BashRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBruteAttackListRequest(AbstractModel):
    """DescribeBruteAttackList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Uuid - String - 是否必填：否 - 云镜唯一Uuid</li>
<li>Quuid - String - 是否必填：否 - 云服务器uuid</li>
<li>Status - String - 是否必填：否 - 状态筛选：失败：FAILED 成功：SUCCESS</li>
<li>UserName - String - 是否必填：否 - UserName筛选</li>
<li>SrcIp - String - 是否必填：否 - 来源ip筛选</li>
<li>CreateBeginTime - String - 是否必填：否 - 首次攻击时间筛选，开始时间</li>
<li>CreateEndTime - String - 是否必填：否 - 首次攻击时间筛选，结束时间</li>
<li>ModifyBeginTime - String - 是否必填：否 - 最近攻击时间筛选，开始时间</li>
<li>ModifyEndTime - String - 是否必填：否 - 最近攻击时间筛选，结束时间</li>
<li>Banned - String - 是否必填：否 - 阻断状态筛选，多个用","分割：0-未阻断（全局ZK开关关闭），82-未阻断(非专业版)，83-未阻断(已加白名单)，1-已阻断，2-未阻断-程序异常，3-未阻断-内网攻击暂不支持阻断，4-未阻断-安平暂不支持阻断</li>
        :type Filters: list of Filter
        :param Order: 排序方式：根据请求次数排序：asc-升序/desc-降序
        :type Order: str
        :param By: 排序字段：CreateTime-首次攻击时间
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBruteAttackListResponse(AbstractModel):
    """DescribeBruteAttackList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param BruteAttackList: 密码破解列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BruteAttackList: list of BruteAttackInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BruteAttackList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BruteAttackList") is not None:
            self.BruteAttackList = []
            for item in params.get("BruteAttackList"):
                obj = BruteAttackInfo()
                obj._deserialize(item)
                self.BruteAttackList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBruteAttackRulesRequest(AbstractModel):
    """DescribeBruteAttackRules请求参数结构体

    """


class DescribeBruteAttackRulesResponse(AbstractModel):
    """DescribeBruteAttackRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Rules: 爆破阻断规则列表
        :type Rules: list of BruteAttackRuleList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = BruteAttackRuleList()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
ComponentName - String - 是否必填：否 - 组件名称
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 组件统计列表记录总数。
        :type TotalCount: int
        :param ComponentStatistics: 组件统计列表数据数组。
        :type ComponentStatistics: list of ComponentStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComponentStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self.ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self.ComponentStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeESAggregationsRequest(AbstractModel):
    """DescribeESAggregations请求参数结构体

    """

    def __init__(self):
        r"""
        :param Query: ES聚合条件JSON
        :type Query: str
        """
        self.Query = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeESAggregationsResponse(AbstractModel):
    """DescribeESAggregations返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: ES聚合结果JSON
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeESHitsRequest(AbstractModel):
    """DescribeESHits请求参数结构体

    """

    def __init__(self):
        r"""
        :param Query: ES查询条件JSON
        :type Query: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        """
        self.Query = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeESHitsResponse(AbstractModel):
    """DescribeESHits返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: ES查询结果JSON
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeEmergencyResponseListRequest(AbstractModel):
    """DescribeEmergencyResponseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Keyword- String - 是否必填：否 - 关键词过滤，</li>
<li>Uuids - String - 是否必填：否 - 主机id过滤</li>
        :type Filters: list of Filters
        :param Limit: 需要返回的数量，最大值为100
        :type Limit: int
        :param Offset: 排序步长
        :type Offset: int
        :param Order: 排序方法
        :type Order: str
        :param By: 排序字段 StartTime，EndTime
        :type By: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEmergencyResponseListResponse(AbstractModel):
    """DescribeEmergencyResponseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 应急响应列表
        :type List: list of EmergencyResponseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = EmergencyResponseInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEmergencyVulListRequest(AbstractModel):
    """DescribeEmergencyVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：是 - 漏洞状态筛选，0//未检测 1有风险 ，2无风险 ，3 检查中展示progress</li>
<li>Level - String - 是否必填：否 - 漏洞等级筛选 1:低 2:中 3:高 4:提示</li>
<li>VulName- String - 是否必填：否 - 漏洞名称搜索</li>
<li>Uuids- String - 是否必填：否 - 主机uuid</li>
<li>IsSupportDefense - int- 是否必填：否 - 是否支持防御 0:不支持 1:支持</li>
        :type Filters: list of Filters
        :param Order: 排序方式 desc , asc
        :type Order: str
        :param By: 排序字段 PublishDate  LastScanTime HostCount
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEmergencyVulListResponse(AbstractModel):
    """DescribeEmergencyVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 漏洞列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of EmergencyVul
        :param TotalCount: 漏洞总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ExistsRisk: 是否存在风险
注意：此字段可能返回 null，表示取不到有效值。
        :type ExistsRisk: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.ExistsRisk = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = EmergencyVul()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.ExistsRisk = params.get("ExistsRisk")
        self.RequestId = params.get("RequestId")


class DescribeExpertServiceListRequest(AbstractModel):
    """DescribeExpertServiceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Keyword- String - 是否必填：否 - 关键词过滤，</li>
<li>Uuids - String - 是否必填：否 - 主机id过滤</li>
        :type Filters: list of Filters
        :param Limit: 需要返回的数量，最大值为100
        :type Limit: int
        :param Offset: 排序步长
        :type Offset: int
        :param Order: 排序方法
        :type Order: str
        :param By: 排序字段 StartTime，EndTime
        :type By: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExpertServiceListResponse(AbstractModel):
    """DescribeExpertServiceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 安全管家数据
        :type List: list of SecurityButlerInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SecurityButlerInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExpertServiceOrderListRequest(AbstractModel):
    """DescribeExpertServiceOrderList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <li>InquireType- String - 是否必填：否 - 订单类型过滤，</li>
        :type Filters: list of Filters
        :param Limit: 分页条数 最大100条
        :type Limit: int
        :param Offset: 分页步长
        :type Offset: int
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExpertServiceOrderListResponse(AbstractModel):
    """DescribeExpertServiceOrderList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 订单列表
        :type List: list of ExpertServiceOrderInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ExpertServiceOrderInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExportMachinesRequest(AbstractModel):
    """DescribeExportMachines请求参数结构体

    """

    def __init__(self):
        r"""
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filter
        :param ProjectIds: 机器所属业务ID列表
        :type ProjectIds: list of int non-negative
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ProjectIds = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProjectIds = params.get("ProjectIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportMachinesResponse(AbstractModel):
    """DescribeExportMachines返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeGeneralStatRequest(AbstractModel):
    """DescribeGeneralStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param MachineType: 云主机类型。
<li>CVM：表示腾讯云服务器</li>
<li>BM:  表示黑石物理机</li>
<li>ECM:  表示边缘计算服务器</li>
<li>LH:  表示轻量应用服务器</li>
<li>Other:  表示混合云机器</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        """
        self.MachineType = None
        self.MachineRegion = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralStatResponse(AbstractModel):
    """DescribeGeneralStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param MachinesAll: 云主机总数
        :type MachinesAll: int
        :param MachinesUninstalled: 云主机没有安装主机安全客户端的总数
        :type MachinesUninstalled: int
        :param AgentsAll: 主机安全客户端总数的总数
        :type AgentsAll: int
        :param AgentsOnline: 主机安全客户端在线的总数
        :type AgentsOnline: int
        :param AgentsOffline: 主机安全客户端 离线+关机 的总数
        :type AgentsOffline: int
        :param AgentsPro: 主机安全客户端专业版的总数
        :type AgentsPro: int
        :param AgentsBasic: 主机安全客户端基础版的总数
        :type AgentsBasic: int
        :param AgentsProExpireWithInSevenDays: 7天内到期的预付费专业版总数
        :type AgentsProExpireWithInSevenDays: int
        :param RiskMachine: 风险主机总数
        :type RiskMachine: int
        :param Shutdown: 已关机总数
        :type Shutdown: int
        :param Offline: 已离线总数
        :type Offline: int
        :param FlagshipMachineCnt: 旗舰版主机数
注意：此字段可能返回 null，表示取不到有效值。
        :type FlagshipMachineCnt: int
        :param ProtectDays: 保护天数
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectDays: int
        :param AddedOnTheFifteen: 15天内新增的主机数
注意：此字段可能返回 null，表示取不到有效值。
        :type AddedOnTheFifteen: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachinesAll = None
        self.MachinesUninstalled = None
        self.AgentsAll = None
        self.AgentsOnline = None
        self.AgentsOffline = None
        self.AgentsPro = None
        self.AgentsBasic = None
        self.AgentsProExpireWithInSevenDays = None
        self.RiskMachine = None
        self.Shutdown = None
        self.Offline = None
        self.FlagshipMachineCnt = None
        self.ProtectDays = None
        self.AddedOnTheFifteen = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachinesAll = params.get("MachinesAll")
        self.MachinesUninstalled = params.get("MachinesUninstalled")
        self.AgentsAll = params.get("AgentsAll")
        self.AgentsOnline = params.get("AgentsOnline")
        self.AgentsOffline = params.get("AgentsOffline")
        self.AgentsPro = params.get("AgentsPro")
        self.AgentsBasic = params.get("AgentsBasic")
        self.AgentsProExpireWithInSevenDays = params.get("AgentsProExpireWithInSevenDays")
        self.RiskMachine = params.get("RiskMachine")
        self.Shutdown = params.get("Shutdown")
        self.Offline = params.get("Offline")
        self.FlagshipMachineCnt = params.get("FlagshipMachineCnt")
        self.ProtectDays = params.get("ProtectDays")
        self.AddedOnTheFifteen = params.get("AddedOnTheFifteen")
        self.RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 帐号变更历史列表记录总数。
        :type TotalCount: int
        :param HistoryAccounts: 帐号变更历史数据数组。
        :type HistoryAccounts: list of HistoryAccount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HistoryAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self.HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self.HistoryAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryServiceRequest(AbstractModel):
    """DescribeHistoryService请求参数结构体

    """


class DescribeHistoryServiceResponse(AbstractModel):
    """DescribeHistoryService返回参数结构体

    """

    def __init__(self):
        r"""
        :param BuyStatus: 1 可购买 2 只能升降配 3 只能跳到续费管理页
        :type BuyStatus: int
        :param InquireNum: 用户已购容量 单位 G
        :type InquireNum: int
        :param EndTime: 到期时间
        :type EndTime: str
        :param IsAutoOpenRenew: 是否自动续费,0 初始值, 1 开通 2 没开通
        :type IsAutoOpenRenew: int
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Status: 0 没开通 1 正常 2隔离 3销毁
        :type Status: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BuyStatus = None
        self.InquireNum = None
        self.EndTime = None
        self.IsAutoOpenRenew = None
        self.ResourceId = None
        self.Status = None
        self.StartTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BuyStatus = params.get("BuyStatus")
        self.InquireNum = params.get("InquireNum")
        self.EndTime = params.get("EndTime")
        self.IsAutoOpenRenew = params.get("IsAutoOpenRenew")
        self.ResourceId = params.get("ResourceId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.RequestId = params.get("RequestId")


class DescribeHostLoginListRequest(AbstractModel):
    """DescribeHostLoginList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Uuid - String - 是否必填：否 - 云镜唯一Uuid</li>
<li>Quuid - String - 是否必填：否 - 云服务器uuid</li>
<li>UserName - String - 是否必填：否 - 用户名筛选</li>
<li>LoginTimeBegin - String - 是否必填：否 - 按照修改时间段筛选，开始时间</li>
<li>LoginTimeEnd - String - 是否必填：否 - 按照修改时间段筛选，结束时间</li>
<li>SrcIp - String - 是否必填：否 - 来源ip筛选</li>
<li>Status - int - 是否必填：否 - 状态筛选1:正常登录；5：已加白,14:已处理，15：已忽略</li>
<li>RiskLevel - int - 是否必填：否 - 状态筛选0:高危；1：可疑</li>
        :type Filters: list of Filter
        :param Order: 排序方式：根据请求次数排序：asc-升序/desc-降序
        :type Order: str
        :param By: 排序字段：LoginTime-发生时间
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostLoginListResponse(AbstractModel):
    """DescribeHostLoginList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param HostLoginList: 登录审计列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HostLoginList: list of HostLoginList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HostLoginList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HostLoginList") is not None:
            self.HostLoginList = []
            for item in params.get("HostLoginList"):
                obj = HostLoginList()
                obj._deserialize(item)
                self.HostLoginList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIgnoreBaselineRuleRequest(AbstractModel):
    """DescribeIgnoreBaselineRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页参数 最大100条
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param RuleName: 检测项名称
        :type RuleName: str
        """
        self.Limit = None
        self.Offset = None
        self.RuleName = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIgnoreBaselineRuleResponse(AbstractModel):
    """DescribeIgnoreBaselineRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param IgnoreBaselineRuleList: 忽略基线检测项列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreBaselineRuleList: list of IgnoreBaselineRule
        :param TotalCount: 分页查询记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IgnoreBaselineRuleList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IgnoreBaselineRuleList") is not None:
            self.IgnoreBaselineRuleList = []
            for item in params.get("IgnoreBaselineRuleList"):
                obj = IgnoreBaselineRule()
                obj._deserialize(item)
                self.IgnoreBaselineRuleList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIgnoreRuleEffectHostListRequest(AbstractModel):
    """DescribeIgnoreRuleEffectHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页参数 最大100条
        :type Limit: int
        :param Offset: 分页参数
        :type Offset: int
        :param RuleId: 检测项id
        :type RuleId: int
        :param Filters: 过滤条件。
<li>AliasName- String- 主机别名</li>
        :type Filters: list of Filters
        :param TagNames: 主机标签名
        :type TagNames: list of str
        """
        self.Limit = None
        self.Offset = None
        self.RuleId = None
        self.Filters = None
        self.TagNames = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RuleId = params.get("RuleId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagNames = params.get("TagNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIgnoreRuleEffectHostListResponse(AbstractModel):
    """DescribeIgnoreRuleEffectHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param IgnoreRuleEffectHostList: 忽略检测项影响主机列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreRuleEffectHostList: list of IgnoreRuleEffectHostInfo
        :param TotalCount: 分页查询记录总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IgnoreRuleEffectHostList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IgnoreRuleEffectHostList") is not None:
            self.IgnoreRuleEffectHostList = []
            for item in params.get("IgnoreRuleEffectHostList"):
                obj = IgnoreRuleEffectHostInfo()
                obj._deserialize(item)
                self.IgnoreRuleEffectHostList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImportMachineInfoRequest(AbstractModel):
    """DescribeImportMachineInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param MachineList: 服务器内网IP（默认）/ 服务器名称 / 服务器ID 数组 (最大 1000条)
        :type MachineList: list of str
        :param ImportType: 批量导入的数据类型：Ip、Name、Id 三选一
        :type ImportType: str
        :param IsQueryProMachine: 该参数已作废.
        :type IsQueryProMachine: bool
        :param Filters: 过滤条件：
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版 | Flagship：旗舰版 | ProtectedMachines：专业版+旗舰版） | BASIC_PROPOST_GENERAL_DISCOUNT：普惠版+专业版按量计费+基础版主机 | UnFlagship：专业版预付费+专业版后付费+基础版+普惠版</li>
        :type Filters: list of Filters
        """
        self.MachineList = None
        self.ImportType = None
        self.IsQueryProMachine = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineList = params.get("MachineList")
        self.ImportType = params.get("ImportType")
        self.IsQueryProMachine = params.get("IsQueryProMachine")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImportMachineInfoResponse(AbstractModel):
    """DescribeImportMachineInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param EffectiveMachineInfoList: 有效的机器信息列表：机器名称、机器公网/内网ip、机器标签
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectiveMachineInfoList: list of EffectiveMachineInfo
        :param InvalidMachineList: 用户批量导入失败的机器列表（例如机器不存在等...）
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidMachineList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EffectiveMachineInfoList = None
        self.InvalidMachineList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EffectiveMachineInfoList") is not None:
            self.EffectiveMachineInfoList = []
            for item in params.get("EffectiveMachineInfoList"):
                obj = EffectiveMachineInfo()
                obj._deserialize(item)
                self.EffectiveMachineInfoList.append(obj)
        self.InvalidMachineList = params.get("InvalidMachineList")
        self.RequestId = params.get("RequestId")


class DescribeIndexListRequest(AbstractModel):
    """DescribeIndexList请求参数结构体

    """


class DescribeIndexListResponse(AbstractModel):
    """DescribeIndexList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: ES 索引信息
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeLicenseBindListRequest(AbstractModel):
    """DescribeLicenseBindList请求参数结构体

    """

    def __init__(self):
        r"""
        :param LicenseId: 授权ID
        :type LicenseId: int
        :param LicenseType: 授权类型
        :type LicenseType: int
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Filters: <li>Keywords 机器别名/公私IP 模糊查询</li>
        :type Filters: list of Filters
        :param Limit: 限制条数,默认10.
        :type Limit: int
        :param Offset: 偏移量,默认0.
        :type Offset: int
        """
        self.LicenseId = None
        self.LicenseType = None
        self.ResourceId = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LicenseId = params.get("LicenseId")
        self.LicenseType = params.get("LicenseType")
        self.ResourceId = params.get("ResourceId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLicenseBindListResponse(AbstractModel):
    """DescribeLicenseBindList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 绑定机器列表信息
        :type List: list of LicenseBindDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = LicenseBindDetail()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLicenseBindScheduleRequest(AbstractModel):
    """DescribeLicenseBindSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param Limit: 限制条数,默认10.
        :type Limit: int
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Filters: 过滤参数
Status 绑定进度状态 0 进行中 1 已完成 2 失败
        :type Filters: list of Filter
        """
        self.TaskId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeLicenseBindScheduleResponse(AbstractModel):
    """DescribeLicenseBindSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Schedule: 进度
        :type Schedule: int
        :param List: 绑定任务详情
        :type List: list of LicenseBindTaskDetail
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Schedule = None
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Schedule = params.get("Schedule")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = LicenseBindTaskDetail()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLicenseGeneralRequest(AbstractModel):
    """DescribeLicenseGeneral请求参数结构体

    """


class DescribeLicenseGeneralResponse(AbstractModel):
    """DescribeLicenseGeneral返回参数结构体

    """

    def __init__(self):
        r"""
        :param LicenseCnt: 总授权数 (包含隔离,过期等不可用状态)
        :type LicenseCnt: int
        :param AvailableLicenseCnt: 可用授权数
        :type AvailableLicenseCnt: int
        :param AvailableProVersionLicenseCnt: 可用专业版授权数(包含后付费).
        :type AvailableProVersionLicenseCnt: int
        :param AvailableFlagshipVersionLicenseCnt: 可用旗舰版授权数
        :type AvailableFlagshipVersionLicenseCnt: int
        :param NearExpiryLicenseCnt: 即将到期授权数 (15天内到期的)
        :type NearExpiryLicenseCnt: int
        :param ExpireLicenseCnt: 已到期授权数(不包含已删除的记录)
        :type ExpireLicenseCnt: int
        :param AutoOpenStatus: 自动升级开关状态,默认 false,  ture 开启, false 关闭
        :type AutoOpenStatus: bool
        :param ProtectType: PROVERSION_POSTPAY 专业版-后付费, PROVERSION_PREPAY 专业版-预付费, FLAGSHIP_PREPAY 旗舰版-预付费
        :type ProtectType: str
        :param IsOpenStatusHistory: 历史是否开通过自动升级开关
        :type IsOpenStatusHistory: bool
        :param UsedLicenseCnt: 已使用授权数
        :type UsedLicenseCnt: int
        :param NotExpiredLicenseCnt: 未到期授权数
        :type NotExpiredLicenseCnt: int
        :param FlagshipVersionLicenseCnt: 旗舰版总授权数(有效订单)
        :type FlagshipVersionLicenseCnt: int
        :param ProVersionLicenseCnt: 专业版总授权数(有效订单)
        :type ProVersionLicenseCnt: int
        :param CwpVersionLicenseCnt: 普惠版总授权数(有效订单的授权数)
        :type CwpVersionLicenseCnt: int
        :param AvailableLHLicenseCnt: 可用惠普版授权数
        :type AvailableLHLicenseCnt: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LicenseCnt = None
        self.AvailableLicenseCnt = None
        self.AvailableProVersionLicenseCnt = None
        self.AvailableFlagshipVersionLicenseCnt = None
        self.NearExpiryLicenseCnt = None
        self.ExpireLicenseCnt = None
        self.AutoOpenStatus = None
        self.ProtectType = None
        self.IsOpenStatusHistory = None
        self.UsedLicenseCnt = None
        self.NotExpiredLicenseCnt = None
        self.FlagshipVersionLicenseCnt = None
        self.ProVersionLicenseCnt = None
        self.CwpVersionLicenseCnt = None
        self.AvailableLHLicenseCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LicenseCnt = params.get("LicenseCnt")
        self.AvailableLicenseCnt = params.get("AvailableLicenseCnt")
        self.AvailableProVersionLicenseCnt = params.get("AvailableProVersionLicenseCnt")
        self.AvailableFlagshipVersionLicenseCnt = params.get("AvailableFlagshipVersionLicenseCnt")
        self.NearExpiryLicenseCnt = params.get("NearExpiryLicenseCnt")
        self.ExpireLicenseCnt = params.get("ExpireLicenseCnt")
        self.AutoOpenStatus = params.get("AutoOpenStatus")
        self.ProtectType = params.get("ProtectType")
        self.IsOpenStatusHistory = params.get("IsOpenStatusHistory")
        self.UsedLicenseCnt = params.get("UsedLicenseCnt")
        self.NotExpiredLicenseCnt = params.get("NotExpiredLicenseCnt")
        self.FlagshipVersionLicenseCnt = params.get("FlagshipVersionLicenseCnt")
        self.ProVersionLicenseCnt = params.get("ProVersionLicenseCnt")
        self.CwpVersionLicenseCnt = params.get("CwpVersionLicenseCnt")
        self.AvailableLHLicenseCnt = params.get("AvailableLHLicenseCnt")
        self.RequestId = params.get("RequestId")


class DescribeLicenseListRequest(AbstractModel):
    """DescribeLicenseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 多个条件筛选时 LicenseStatus,DeadlineStatus,ResourceId,Keywords 取交集
<li> LicenseStatus 授权状态信息,0 未使用,1 部分使用, 2 已用完, 3 不可用  4 可使用</li>
<li> BuyTime 购买时间</li>
<li> LicenseType  授权类型, 0 专业版-按量计费, 1专业版-包年包月 , 2 旗舰版-包年包月</li>
<li>DeadlineStatus 到期状态 NotExpired 未过期, Expire 已过期(包含已销毁) NearExpiry 即将到期</li>
<li>ResourceId 资源ID</li>
<li>Keywords IP筛选</li>
<li>PayMode 付费模式 0 按量计费 , 1 包年包月</li>
<li>OrderStatus 订单状态 1 正常 2 隔离 3 销毁</li>
        :type Filters: list of Filters
        :param Limit: 限制条数,默认10.
        :type Limit: int
        :param Offset: 偏移量,默认0.
        :type Offset: int
        :param Tags: 标签筛选,平台标签能力,这里传入 标签键,标签值作为一个对象
        :type Tags: list of Tags
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLicenseListResponse(AbstractModel):
    """DescribeLicenseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 授权数列表信息
        :type List: list of LicenseDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = LicenseDetail()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogStorageStatisticRequest(AbstractModel):
    """DescribeLogStorageStatistic请求参数结构体

    """


class DescribeLogStorageStatisticResponse(AbstractModel):
    """DescribeLogStorageStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalSize: 总容量（单位：GB）
        :type TotalSize: int
        :param UsedSize: 已使用容量（单位：GB）
        :type UsedSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalSize = None
        self.UsedSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalSize = params.get("TotalSize")
        self.UsedSize = params.get("UsedSize")
        self.RequestId = params.get("RequestId")


class DescribeLoginWhiteCombinedListRequest(AbstractModel):
    """DescribeLoginWhiteCombinedList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>UserName - String - 是否必填：否 - 用户名筛选</li>
<li>ModifyBeginTime - String - 是否必填：否 - 按照修改时间段筛选，开始时间</li>
<li>ModifyEndTime - String - 是否必填：否 - 按照修改时间段筛选，结束时间</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeLoginWhiteCombinedListResponse(AbstractModel):
    """DescribeLoginWhiteCombinedList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param LoginWhiteCombinedInfos: 合并后的白名单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginWhiteCombinedInfos: list of LoginWhiteCombinedInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoginWhiteCombinedInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoginWhiteCombinedInfos") is not None:
            self.LoginWhiteCombinedInfos = []
            for item in params.get("LoginWhiteCombinedInfos"):
                obj = LoginWhiteCombinedInfo()
                obj._deserialize(item)
                self.LoginWhiteCombinedInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoginWhiteListRequest(AbstractModel):
    """DescribeLoginWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 查询关键字 </li>
<li>UserName - String - 是否必填：否 - 用户名筛选 </li>
<li>ModifyBeginTime - String - 是否必填：否 - 按照修改时间段筛选，开始时间 </li>
<li>ModifyEndTime - String - 是否必填：否 - 按照修改时间段筛选，结束时间 </li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeLoginWhiteListResponse(AbstractModel):
    """DescribeLoginWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param LoginWhiteLists: 异地登录白名单数组
        :type LoginWhiteLists: list of LoginWhiteLists
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoginWhiteLists = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoginWhiteLists") is not None:
            self.LoginWhiteLists = []
            for item in params.get("LoginWhiteLists"):
                obj = LoginWhiteLists()
                obj._deserialize(item)
                self.LoginWhiteLists.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param Quuid: Quuid , Uuid 必填一项
        :type Quuid: str
        """
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param MachineIp: 机器ip。
        :type MachineIp: str
        :param ProtectDays: 受云镜保护天数。
        :type ProtectDays: int
        :param MachineOs: 操作系统。
        :type MachineOs: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineStatus: 在线状态。
<li>ONLINE： 在线</li>
<li>OFFLINE：离线</li>
        :type MachineStatus: str
        :param InstanceId: CVM或BM主机唯一标识。
        :type InstanceId: str
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param Quuid: CVM或BM主机唯一Uuid。
        :type Quuid: str
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param IsProVersion: 是否开通专业版。
<li>true：是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param ProVersionOpenDate: 专业版开通时间。
        :type ProVersionOpenDate: str
        :param MachineType: 云服务器类型。
<li>CVM: 腾讯云服务器</li>
<li>BM: 黑石物理机</li>
<li>ECM: 边缘计算服务器</li>
<li>LH: 轻量应用服务器</li>
<li>Other: 混合云机器</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param FreeMalwaresLeft: 免费木马剩余检测数量。
        :type FreeMalwaresLeft: int
        :param FreeVulsLeft: 免费漏洞剩余检测数量。
        :type FreeVulsLeft: int
        :param AgentVersion: agent版本号
        :type AgentVersion: str
        :param ProVersionDeadline: 专业版到期时间(仅预付费)
        :type ProVersionDeadline: str
        :param HasAssetScan: 是否有资产扫描记录，0无，1有
        :type HasAssetScan: int
        :param ProtectType: 防护版本 BASIC_VERSION 基础版, PRO_VERSION 专业版 Flagship 旗舰版.
        :type ProtectType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineIp = None
        self.ProtectDays = None
        self.MachineOs = None
        self.MachineName = None
        self.MachineStatus = None
        self.InstanceId = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.IsProVersion = None
        self.ProVersionOpenDate = None
        self.MachineType = None
        self.MachineRegion = None
        self.PayMode = None
        self.FreeMalwaresLeft = None
        self.FreeVulsLeft = None
        self.AgentVersion = None
        self.ProVersionDeadline = None
        self.HasAssetScan = None
        self.ProtectType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.ProtectDays = params.get("ProtectDays")
        self.MachineOs = params.get("MachineOs")
        self.MachineName = params.get("MachineName")
        self.MachineStatus = params.get("MachineStatus")
        self.InstanceId = params.get("InstanceId")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.ProVersionOpenDate = params.get("ProVersionOpenDate")
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.PayMode = params.get("PayMode")
        self.FreeMalwaresLeft = params.get("FreeMalwaresLeft")
        self.FreeVulsLeft = params.get("FreeVulsLeft")
        self.AgentVersion = params.get("AgentVersion")
        self.ProVersionDeadline = params.get("ProVersionDeadline")
        self.HasAssetScan = params.get("HasAssetScan")
        self.ProtectType = params.get("ProtectType")
        self.RequestId = params.get("RequestId")


class DescribeMachineListRequest(AbstractModel):
    """DescribeMachineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
<li>ECM:  表示边缘计算服务器</li>
<li>LH:  表示轻量应用服务器</li>
<li>Other:  表示混合云机器</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of AssetFilters
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineListResponse(AbstractModel):
    """DescribeMachineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Machines: 主机列表
        :type Machines: list of Machine
        :param TotalCount: 主机数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMachineOsListRequest(AbstractModel):
    """DescribeMachineOsList请求参数结构体

    """


class DescribeMachineOsListResponse(AbstractModel):
    """DescribeMachineOsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 操作系统列表
        :type List: list of OsName
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = OsName()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineRegionsRequest(AbstractModel):
    """DescribeMachineRegions请求参数结构体

    """


class DescribeMachineRegionsResponse(AbstractModel):
    """DescribeMachineRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param CVM: CVM 云服务器地域列表
        :type CVM: list of RegionInfo
        :param BM: BM 黑石机器地域列表
        :type BM: list of RegionInfo
        :param LH: LH 轻量应用服务器地域列表
        :type LH: list of RegionInfo
        :param ECM: ECM 边缘计算服务器地域列表
        :type ECM: list of RegionInfo
        :param Other: Other 混合云地域列表
        :type Other: list of RegionInfo
        :param ALL: 所有地域列表(包含以上所有地域)
        :type ALL: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CVM = None
        self.BM = None
        self.LH = None
        self.ECM = None
        self.Other = None
        self.ALL = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CVM") is not None:
            self.CVM = []
            for item in params.get("CVM"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.CVM.append(obj)
        if params.get("BM") is not None:
            self.BM = []
            for item in params.get("BM"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.BM.append(obj)
        if params.get("LH") is not None:
            self.LH = []
            for item in params.get("LH"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.LH.append(obj)
        if params.get("ECM") is not None:
            self.ECM = []
            for item in params.get("ECM"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.ECM.append(obj)
        if params.get("Other") is not None:
            self.Other = []
            for item in params.get("Other"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.Other.append(obj)
        if params.get("ALL") is not None:
            self.ALL = []
            for item in params.get("ALL"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.ALL.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        r"""
        :param MachineType: 机器所属专区类型 
CVM 云服务器
BM 黑石
ECM 边缘计算
LH 轻量应用服务器
Other 混合云专区
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线/关机 | ONLINE: 在线 | UNINSTALLED：未安装 | AGENT_OFFLINE 离线| AGENT_SHUTDOWN 已关机）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版 | Flagship : 旗舰版 | ProtectedMachines: 专业版+旗舰版）</li>
<li>Risk - String 是否必填: 否 - 风险主机( yes ) </li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
<li>Quuid - String - 是否必填: 否 - 云服务器uuid  最大100条.</li>
<li>AddedOnTheFifteen- String 是否必填: 否 - 是否只查询15天内新增的主机( 1：是) </li>
        :type Filters: list of Filter
        :param ProjectIds: 机器所属业务ID列表
        :type ProjectIds: list of int non-negative
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ProjectIds = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProjectIds = params.get("ProjectIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        r"""
        :param Machines: 主机列表
        :type Machines: list of Machine
        :param TotalCount: 主机数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMalWareListRequest(AbstractModel):
    """DescribeMalWareList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>FilePath - String - 是否必填：否 - 路径筛选</li>
<li>VirusName - String - 是否必填：否 - 描述筛选</li>
<li>CreateBeginTime - String - 是否必填：否 - 创建时间筛选-开始时间</li>
<li>CreateEndTime - String - 是否必填：否 - 创建时间筛选-结束时间</li>
<li>Status - String - 是否必填：否 - 状态筛选 4待处理,5信任,6已隔离,10隔离中,11恢复隔离中</li>
        :type Filters: list of Filter
        :param By: 检测排序 CreateTime
        :type By: str
        :param Order: 排序方式 ASC,DESC
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMalWareListResponse(AbstractModel):
    """DescribeMalWareList返回参数结构体

    """

    def __init__(self):
        r"""
        :param MalWareList: 木马列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MalWareList: list of MalWareList
        :param TotalCount: 总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MalWareList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MalWareList") is not None:
            self.MalWareList = []
            for item in params.get("MalWareList"):
                obj = MalWareList()
                obj._deserialize(item)
                self.MalWareList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMaliciousRequestWhiteListRequest(AbstractModel):
    """DescribeMaliciousRequestWhiteList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。

<li>Domain  - String - 基线名称</li>
        :type Filters: list of Filters
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaliciousRequestWhiteListResponse(AbstractModel):
    """DescribeMaliciousRequestWhiteList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 白名单信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of MaliciousRequestWhiteListInfo
        :param TotalCount: 分页查询记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = MaliciousRequestWhiteListInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMalwareFileRequest(AbstractModel):
    """DescribeMalwareFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 木马记录ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMalwareFileResponse(AbstractModel):
    """DescribeMalwareFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrl: 木马文件下载地址
        :type FileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.RequestId = params.get("RequestId")


class DescribeMalwareInfoRequest(AbstractModel):
    """DescribeMalwareInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 唯一ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMalwareInfoResponse(AbstractModel):
    """DescribeMalwareInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param MalwareInfo: 恶意文件详情信息
        :type MalwareInfo: :class:`tencentcloud.cwp.v20180228.models.MalwareInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MalwareInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MalwareInfo") is not None:
            self.MalwareInfo = MalwareInfo()
            self.MalwareInfo._deserialize(params.get("MalwareInfo"))
        self.RequestId = params.get("RequestId")


class DescribeMalwareRiskWarningRequest(AbstractModel):
    """DescribeMalwareRiskWarning请求参数结构体

    """


class DescribeMalwareRiskWarningResponse(AbstractModel):
    """DescribeMalwareRiskWarning返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsCheckRisk: 是否开启自动扫描：true-开启，false-未开启
        :type IsCheckRisk: bool
        :param List: 风险文件列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of MalwareRisk
        :param IsPop: 是否弹出提示 true 弹出, false不弹
        :type IsPop: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsCheckRisk = None
        self.List = None
        self.IsPop = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsCheckRisk = params.get("IsCheckRisk")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = MalwareRisk()
                obj._deserialize(item)
                self.List.append(obj)
        self.IsPop = params.get("IsPop")
        self.RequestId = params.get("RequestId")


class DescribeMalwareTimingScanSettingRequest(AbstractModel):
    """DescribeMalwareTimingScanSetting请求参数结构体

    """


class DescribeMalwareTimingScanSettingResponse(AbstractModel):
    """DescribeMalwareTimingScanSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckPattern: 检测模式 0 全盘检测  1快速检测
        :type CheckPattern: int
        :param StartTime: 检测周期 开始时间
        :type StartTime: str
        :param EndTime: 检测周期 超时结束时间
        :type EndTime: str
        :param IsGlobal: 是否全部服务器 1 全部 2 自选
        :type IsGlobal: int
        :param QuuidList: 自选服务器时必须 主机quuid的string数组
注意：此字段可能返回 null，表示取不到有效值。
        :type QuuidList: list of str
        :param MonitoringPattern: 监控模式 0 标准 1深度
        :type MonitoringPattern: int
        :param Cycle: 周期 1每天
        :type Cycle: int
        :param EnableScan: 定时检测开关 0 关闭1 开启
        :type EnableScan: int
        :param Id: 唯一ID
        :type Id: int
        :param RealTimeMonitoring: 实时监控0 关闭 1开启
        :type RealTimeMonitoring: int
        :param AutoIsolation: 是否自动隔离：1-是，0-否
        :type AutoIsolation: int
        :param ClickTimeout: 一键扫描超时时长，如：1800秒（s）
        :type ClickTimeout: int
        :param KillProcess: 是否杀掉进程 1杀掉 0不杀掉 只有开启自动隔离才生效
        :type KillProcess: int
        :param EngineType: 1标准模式（只报严重、高危）、2增强模式（报严重、高危、中危）、3严格模式（报严重、高、中、低、提示）
        :type EngineType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckPattern = None
        self.StartTime = None
        self.EndTime = None
        self.IsGlobal = None
        self.QuuidList = None
        self.MonitoringPattern = None
        self.Cycle = None
        self.EnableScan = None
        self.Id = None
        self.RealTimeMonitoring = None
        self.AutoIsolation = None
        self.ClickTimeout = None
        self.KillProcess = None
        self.EngineType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckPattern = params.get("CheckPattern")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsGlobal = params.get("IsGlobal")
        self.QuuidList = params.get("QuuidList")
        self.MonitoringPattern = params.get("MonitoringPattern")
        self.Cycle = params.get("Cycle")
        self.EnableScan = params.get("EnableScan")
        self.Id = params.get("Id")
        self.RealTimeMonitoring = params.get("RealTimeMonitoring")
        self.AutoIsolation = params.get("AutoIsolation")
        self.ClickTimeout = params.get("ClickTimeout")
        self.KillProcess = params.get("KillProcess")
        self.EngineType = params.get("EngineType")
        self.RequestId = params.get("RequestId")


class DescribeMonthInspectionReportRequest(AbstractModel):
    """DescribeMonthInspectionReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页大小
        :type Limit: int
        :param Offset: 分页步长
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonthInspectionReportResponse(AbstractModel):
    """DescribeMonthInspectionReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 巡检报告列表
        :type List: list of MonthInspectionReport
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = MonthInspectionReport()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 端口统计列表总数
        :type TotalCount: int
        :param OpenPortStatistics: 端口统计数据列表
        :type OpenPortStatistics: list of OpenPortStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPortStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self.OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self.OpenPortStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics请求参数结构体

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param OnlineMachineNum: 服务器在线数。
        :type OnlineMachineNum: int
        :param ProVersionMachineNum: 专业服务器数。
        :type ProVersionMachineNum: int
        :param MalwareNum: 木马文件数。
        :type MalwareNum: int
        :param NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 暴力破解成功数。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param BaseLineNum: 安全基线数。
        :type BaseLineNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OnlineMachineNum = None
        self.ProVersionMachineNum = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.BaseLineNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.BaseLineNum = params.get("BaseLineNum")
        self.RequestId = params.get("RequestId")


class DescribePrivilegeEventsRequest(AbstractModel):
    """DescribePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机IP)</li>
        :type Filters: list of Filter
        :param Order: 排序方式：根据请求次数排序：asc-升序/desc-降序
        :type Order: str
        :param By: 排序字段：CreateTime-发现时间
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivilegeEventsResponse(AbstractModel):
    """DescribePrivilegeEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 数据列表
        :type List: list of PrivilegeEscalationProcess
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PrivilegeEscalationProcess()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePrivilegeRulesRequest(AbstractModel):
    """DescribePrivilegeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribePrivilegeRulesResponse(AbstractModel):
    """DescribePrivilegeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 列表内容
        :type List: list of PrivilegeRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PrivilegeRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo请求参数结构体

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param PostPayCost: 后付费昨日扣费
        :type PostPayCost: int
        :param IsAutoOpenProVersion: 新增主机是否自动开通专业版
        :type IsAutoOpenProVersion: bool
        :param ProVersionNum: 开通专业版主机数
        :type ProVersionNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PostPayCost = None
        self.IsAutoOpenProVersion = None
        self.ProVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostPayCost = params.get("PostPayCost")
        self.IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self.ProVersionNum = params.get("ProVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeProVersionStatusRequest(AbstractModel):
    """DescribeProVersionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 云镜客户端UUID、填写"all"表示所有主机。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProVersionStatusResponse(AbstractModel):
    """DescribeProVersionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 进程统计列表记录总数。
        :type TotalCount: int
        :param ProcessStatistics: 进程统计列表数据数组。
        :type ProcessStatistics: list of ProcessStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProcessStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self.ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self.ProcessStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProtectDirListRequest(AbstractModel):
    """DescribeProtectDirList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页条数 最大100条
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param Filters: DirName 网站名称
DirPath 网站防护目录地址
        :type Filters: list of AssetFilters
        :param Order: asc：升序/desc：降序
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectDirListResponse(AbstractModel):
    """DescribeProtectDirList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 防护目录列表信息
        :type List: list of ProtectDirInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ProtectDirInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProtectDirRelatedServerRequest(AbstractModel):
    """DescribeProtectDirRelatedServer请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 唯一ID
        :type Id: str
        :param Limit: 分页条数 最大100条
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param Filters: 过滤参数 ProtectStatus
        :type Filters: list of Filter
        :param Order: 排序方式
        :type Order: str
        :param By: 排序值
        :type By: str
        """
        self.Id = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectDirRelatedServerResponse(AbstractModel):
    """DescribeProtectDirRelatedServer返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 网站关联服务器列表信息
        :type List: list of ProtectDirRelatedServer
        :param TotalCount: 总数
        :type TotalCount: int
        :param ProtectServerCount: 已开启防护总数
        :type ProtectServerCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.ProtectServerCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ProtectDirRelatedServer()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.ProtectServerCount = params.get("ProtectServerCount")
        self.RequestId = params.get("RequestId")


class DescribeProtectNetListRequest(AbstractModel):
    """DescribeProtectNetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>Keyword- String - 是否必填：否 - 关键词过滤，</li>
<li>Uuids - String - 是否必填：否 - 主机id过滤</li>
        :type Filters: list of Filters
        :param Limit: 需要返回的数量，最大值为100
        :type Limit: int
        :param Offset: 排序步长
        :type Offset: int
        :param Order: 排序方法
        :type Order: str
        :param By: 排序字段 StartTime，EndTime
        :type By: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectNetListResponse(AbstractModel):
    """DescribeProtectNetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 安全管家数据
        :type List: list of ProtectNetInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ProtectNetInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReverseShellEventsRequest(AbstractModel):
    """DescribeReverseShellEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(主机内网IP|进程名)</li>
        :type Filters: list of Filter
        :param Order: 排序方式：根据请求次数排序：asc-升序/desc-降序
        :type Order: str
        :param By: 排序字段：CreateTime-发生时间
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellEventsResponse(AbstractModel):
    """DescribeReverseShellEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 列表内容
        :type List: list of ReverseShell
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ReverseShell()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeReverseShellRulesRequest(AbstractModel):
    """DescribeReverseShellRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeReverseShellRulesResponse(AbstractModel):
    """DescribeReverseShellRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 列表内容
        :type List: list of ReverseShellRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ReverseShellRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRiskDnsListRequest(AbstractModel):
    """DescribeRiskDnsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Url - String - 是否必填：否 - Url筛选</li>
<li>Status - String - 是否必填：否 - 状态筛选0:待处理；2:信任；3:不信任</li>
<li>MergeBeginTime - String - 是否必填：否 - 最近访问开始时间</li>
<li>MergeEndTime - String - 是否必填：否 - 最近访问结束时间</li>
        :type Filters: list of Filter
        :param Order: 排序方式：根据请求次数排序：asc-升序/desc-降序
        :type Order: str
        :param By: 排序字段：AccessCount-请求次数。MergeTime-最近请求时间
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskDnsListResponse(AbstractModel):
    """DescribeRiskDnsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RiskDnsList: 恶意请求列表数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskDnsList: list of RiskDnsList
        :param TotalCount: 总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RiskDnsList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RiskDnsList") is not None:
            self.RiskDnsList = []
            for item in params.get("RiskDnsList"):
                obj = RiskDnsList()
                obj._deserialize(item)
                self.RiskDnsList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSaveOrUpdateWarningsRequest(AbstractModel):
    """DescribeSaveOrUpdateWarnings请求参数结构体

    """

    def __init__(self):
        r"""
        :param WarningObjects: 告警设置的修改内容
        :type WarningObjects: list of WarningObject
        """
        self.WarningObjects = None


    def _deserialize(self, params):
        if params.get("WarningObjects") is not None:
            self.WarningObjects = []
            for item in params.get("WarningObjects"):
                obj = WarningObject()
                obj._deserialize(item)
                self.WarningObjects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSaveOrUpdateWarningsResponse(AbstractModel):
    """DescribeSaveOrUpdateWarnings返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeScanMalwareScheduleRequest(AbstractModel):
    """DescribeScanMalwareSchedule请求参数结构体

    """


class DescribeScanMalwareScheduleResponse(AbstractModel):
    """DescribeScanMalwareSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Schedule: 扫描进度（单位：%）
        :type Schedule: int
        :param RiskFileNumber: 风险文件数,当进度满了以后才有该值
        :type RiskFileNumber: int
        :param IsSchedule: 是否正在扫描中
        :type IsSchedule: bool
        :param ScanStatus: 0 从未扫描过、 1 扫描中、 2扫描完成、 3停止中、 4停止完成
        :type ScanStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Schedule = None
        self.RiskFileNumber = None
        self.IsSchedule = None
        self.ScanStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Schedule = params.get("Schedule")
        self.RiskFileNumber = params.get("RiskFileNumber")
        self.IsSchedule = params.get("IsSchedule")
        self.ScanStatus = params.get("ScanStatus")
        self.RequestId = params.get("RequestId")


class DescribeScanScheduleRequest(AbstractModel):
    """DescribeScanSchedule请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanScheduleResponse(AbstractModel):
    """DescribeScanSchedule返回参数结构体

    """

    def __init__(self):
        r"""
        :param Schedule: 检测进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Schedule: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Schedule = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Schedule = params.get("Schedule")
        self.RequestId = params.get("RequestId")


class DescribeScanStateRequest(AbstractModel):
    """DescribeScanState请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModuleType: 模块类型 当前提供 Malware 木马 , Vul 漏洞 , Baseline 基线
        :type ModuleType: str
        :param Filters: 过滤参数;
<li>StrategyId 基线策略ID ,仅ModuleType 为 Baseline 时需要<li/>
        :type Filters: list of Filters
        """
        self.ModuleType = None
        self.Filters = None


    def _deserialize(self, params):
        self.ModuleType = params.get("ModuleType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanStateResponse(AbstractModel):
    """DescribeScanState返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScanState: 0 从未扫描过、 1 扫描中、 2扫描完成、 3停止中、 4停止完成
        :type ScanState: int
        :param Schedule: 扫描进度
        :type Schedule: int
        :param TaskId: 任务Id
        :type TaskId: int
        :param VulId: 任务扫描的漏洞id
        :type VulId: list of int non-negative
        :param Type: 0一键检测 1定时检测
        :type Type: int
        :param ScanBeginTime: 开始扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanBeginTime: str
        :param RiskEventCount: 扫描漏洞数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskEventCount: int
        :param ScanEndTime: 扫描结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanEndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScanState = None
        self.Schedule = None
        self.TaskId = None
        self.VulId = None
        self.Type = None
        self.ScanBeginTime = None
        self.RiskEventCount = None
        self.ScanEndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScanState = params.get("ScanState")
        self.Schedule = params.get("Schedule")
        self.TaskId = params.get("TaskId")
        self.VulId = params.get("VulId")
        self.Type = params.get("Type")
        self.ScanBeginTime = params.get("ScanBeginTime")
        self.RiskEventCount = params.get("RiskEventCount")
        self.ScanEndTime = params.get("ScanEndTime")
        self.RequestId = params.get("RequestId")


class DescribeScanTaskDetailsRequest(AbstractModel):
    """DescribeScanTaskDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModuleType: 模块类型 当前提供 Malware 木马 , Vul 漏洞 , Baseline 基线
        :type ModuleType: str
        :param TaskId: 任务ID
        :type TaskId: int
        :param Filters: 过滤参数
        :type Filters: list of Filters
        :param Limit: 需要返回的数量，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.ModuleType = None
        self.TaskId = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ModuleType = params.get("ModuleType")
        self.TaskId = params.get("TaskId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskDetailsResponse(AbstractModel):
    """DescribeScanTaskDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScanTaskDetailList: 扫描任务信息列表
        :type ScanTaskDetailList: list of ScanTaskDetails
        :param TotalCount: 总数
        :type TotalCount: int
        :param ScanMachineCount: 扫描机器总数
        :type ScanMachineCount: int
        :param RiskMachineCount: 发现风险机器数
        :type RiskMachineCount: int
        :param ScanBeginTime: 扫描开始时间
        :type ScanBeginTime: str
        :param ScanEndTime: 扫描结束时间
        :type ScanEndTime: str
        :param ScanTime: 检测时间
        :type ScanTime: int
        :param ScanProgress: 扫描进度
        :type ScanProgress: int
        :param ScanLeftTime: 扫描剩余时间
        :type ScanLeftTime: int
        :param ScanContent: 扫描内容
        :type ScanContent: list of str
        :param VulInfo: 漏洞信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VulInfo: list of VulDetailInfo
        :param RiskEventCount: 风险事件个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskEventCount: int
        :param Type: 0一键检测 1定时检测
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param StoppingAll: 任务是否全部正在被停止 ture是
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingAll: bool
        :param VulCount: 扫描出漏洞个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScanTaskDetailList = None
        self.TotalCount = None
        self.ScanMachineCount = None
        self.RiskMachineCount = None
        self.ScanBeginTime = None
        self.ScanEndTime = None
        self.ScanTime = None
        self.ScanProgress = None
        self.ScanLeftTime = None
        self.ScanContent = None
        self.VulInfo = None
        self.RiskEventCount = None
        self.Type = None
        self.StoppingAll = None
        self.VulCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScanTaskDetailList") is not None:
            self.ScanTaskDetailList = []
            for item in params.get("ScanTaskDetailList"):
                obj = ScanTaskDetails()
                obj._deserialize(item)
                self.ScanTaskDetailList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.ScanMachineCount = params.get("ScanMachineCount")
        self.RiskMachineCount = params.get("RiskMachineCount")
        self.ScanBeginTime = params.get("ScanBeginTime")
        self.ScanEndTime = params.get("ScanEndTime")
        self.ScanTime = params.get("ScanTime")
        self.ScanProgress = params.get("ScanProgress")
        self.ScanLeftTime = params.get("ScanLeftTime")
        self.ScanContent = params.get("ScanContent")
        if params.get("VulInfo") is not None:
            self.VulInfo = []
            for item in params.get("VulInfo"):
                obj = VulDetailInfo()
                obj._deserialize(item)
                self.VulInfo.append(obj)
        self.RiskEventCount = params.get("RiskEventCount")
        self.Type = params.get("Type")
        self.StoppingAll = params.get("StoppingAll")
        self.VulCount = params.get("VulCount")
        self.RequestId = params.get("RequestId")


class DescribeScanTaskStatusRequest(AbstractModel):
    """DescribeScanTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModuleType: 模块类型 当前提供 Malware 木马 , Vul 漏洞 , Baseline 基线
        :type ModuleType: str
        """
        self.ModuleType = None


    def _deserialize(self, params):
        self.ModuleType = params.get("ModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskStatusResponse(AbstractModel):
    """DescribeScanTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param State: 任务扫描状态列表
        :type State: :class:`tencentcloud.cwp.v20180228.models.TaskStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("State") is not None:
            self.State = TaskStatus()
            self.State._deserialize(params.get("State"))
        self.RequestId = params.get("RequestId")


class DescribeScanVulSettingRequest(AbstractModel):
    """DescribeScanVulSetting请求参数结构体

    """


class DescribeScanVulSettingResponse(AbstractModel):
    """DescribeScanVulSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulCategories: 漏洞类型：1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞
        :type VulCategories: str
        :param VulLevels: 危害等级：1-低危；2-中危；3-高危；4-严重 (多选英文逗号分隔)
        :type VulLevels: str
        :param TimerInterval: 定期检测间隔时间（天）
        :type TimerInterval: int
        :param TimerTime: 定期检测时间，如：00:00
        :type TimerTime: str
        :param VulEmergency: 是否紧急漏洞：0-否 1-是
        :type VulEmergency: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param EnableScan: 是否开启
        :type EnableScan: int
        :param EndTime: 结束时间
        :type EndTime: str
        :param ClickTimeout: 一键扫描超时时长，如：1800秒（s）
        :type ClickTimeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulCategories = None
        self.VulLevels = None
        self.TimerInterval = None
        self.TimerTime = None
        self.VulEmergency = None
        self.StartTime = None
        self.EnableScan = None
        self.EndTime = None
        self.ClickTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulCategories = params.get("VulCategories")
        self.VulLevels = params.get("VulLevels")
        self.TimerInterval = params.get("TimerInterval")
        self.TimerTime = params.get("TimerTime")
        self.VulEmergency = params.get("VulEmergency")
        self.StartTime = params.get("StartTime")
        self.EnableScan = params.get("EnableScan")
        self.EndTime = params.get("EndTime")
        self.ClickTimeout = params.get("ClickTimeout")
        self.RequestId = params.get("RequestId")


class DescribeSearchExportListRequest(AbstractModel):
    """DescribeSearchExportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Query: ES查询条件JSON
        :type Query: str
        """
        self.Query = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchExportListResponse(AbstractModel):
    """DescribeSearchExportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 导出的任务号
        :type TaskId: int
        :param DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeSearchLogsRequest(AbstractModel):
    """DescribeSearchLogs请求参数结构体

    """


class DescribeSearchLogsResponse(AbstractModel):
    """DescribeSearchLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 历史搜索记录 保留最新的10条
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeSearchTemplatesRequest(AbstractModel):
    """DescribeSearchTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchTemplatesResponse(AbstractModel):
    """DescribeSearchTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 模板列表
        :type List: list of SearchTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SearchTemplate()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics返回参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityDynamics: 安全事件消息数组。
        :type SecurityDynamics: list of SecurityDynamic
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityDynamics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityDynamics") is not None:
            self.SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self.SecurityDynamics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityEventStatRequest(AbstractModel):
    """DescribeSecurityEventStat请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 该接口无过滤条件
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
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
        


class DescribeSecurityEventStatResponse(AbstractModel):
    """DescribeSecurityEventStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param MalwareStat: 木马事件统计
        :type MalwareStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param HostLoginStat: 异地事件统计
        :type HostLoginStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param BruteAttackStat: 爆破事件统计
        :type BruteAttackStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param MaliciousRequestStat: 恶意请求事件统计
        :type MaliciousRequestStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param PrivilegeStat: 本地提权事件统计
        :type PrivilegeStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param ReverseShellStat: 反弹Shell事件统计
        :type ReverseShellStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param HighRiskBashStat: 高危命令事件统计
        :type HighRiskBashStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param AttackLogsStat: 网络攻击事件统计
        :type AttackLogsStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param VulHighStat: 高危漏洞事件统计
        :type VulHighStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param VulNormalStat: 中危漏洞事件统计
        :type VulNormalStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param VulLowStat: 低危漏洞事件统计
        :type VulLowStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param BaselineHighStat: 高危基线漏洞事件统计
        :type BaselineHighStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param BaselineNormalStat: 中危基线漏事件统计
        :type BaselineNormalStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param BaselineLowStat: 低危基线漏事件统计
        :type BaselineLowStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param MachineTotalAffectNum: 有未处理安全事件的机器总数
        :type MachineTotalAffectNum: int
        :param InvasionTotalAffectNum: 有未处理入侵安全事件的机器总数
        :type InvasionTotalAffectNum: int
        :param VulTotalAffectNum: 有未处理漏洞安全事件的机器总数
        :type VulTotalAffectNum: int
        :param BaseLineTotalAffectNum: 有未处理基线安全事件的机器总数
        :type BaseLineTotalAffectNum: int
        :param CyberAttackTotalAffectNum: 有未处理网络攻击安全事件的机器总数
        :type CyberAttackTotalAffectNum: int
        :param VulRiskStat: 严重漏洞事件统计
        :type VulRiskStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param BaselineRiskStat: 严重基线漏洞事件统计
        :type BaselineRiskStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param VulStat: 漏洞数统计
        :type VulStat: :class:`tencentcloud.cwp.v20180228.models.EventStat`
        :param Score: 安全得分
        :type Score: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MalwareStat = None
        self.HostLoginStat = None
        self.BruteAttackStat = None
        self.MaliciousRequestStat = None
        self.PrivilegeStat = None
        self.ReverseShellStat = None
        self.HighRiskBashStat = None
        self.AttackLogsStat = None
        self.VulHighStat = None
        self.VulNormalStat = None
        self.VulLowStat = None
        self.BaselineHighStat = None
        self.BaselineNormalStat = None
        self.BaselineLowStat = None
        self.MachineTotalAffectNum = None
        self.InvasionTotalAffectNum = None
        self.VulTotalAffectNum = None
        self.BaseLineTotalAffectNum = None
        self.CyberAttackTotalAffectNum = None
        self.VulRiskStat = None
        self.BaselineRiskStat = None
        self.VulStat = None
        self.Score = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MalwareStat") is not None:
            self.MalwareStat = EventStat()
            self.MalwareStat._deserialize(params.get("MalwareStat"))
        if params.get("HostLoginStat") is not None:
            self.HostLoginStat = EventStat()
            self.HostLoginStat._deserialize(params.get("HostLoginStat"))
        if params.get("BruteAttackStat") is not None:
            self.BruteAttackStat = EventStat()
            self.BruteAttackStat._deserialize(params.get("BruteAttackStat"))
        if params.get("MaliciousRequestStat") is not None:
            self.MaliciousRequestStat = EventStat()
            self.MaliciousRequestStat._deserialize(params.get("MaliciousRequestStat"))
        if params.get("PrivilegeStat") is not None:
            self.PrivilegeStat = EventStat()
            self.PrivilegeStat._deserialize(params.get("PrivilegeStat"))
        if params.get("ReverseShellStat") is not None:
            self.ReverseShellStat = EventStat()
            self.ReverseShellStat._deserialize(params.get("ReverseShellStat"))
        if params.get("HighRiskBashStat") is not None:
            self.HighRiskBashStat = EventStat()
            self.HighRiskBashStat._deserialize(params.get("HighRiskBashStat"))
        if params.get("AttackLogsStat") is not None:
            self.AttackLogsStat = EventStat()
            self.AttackLogsStat._deserialize(params.get("AttackLogsStat"))
        if params.get("VulHighStat") is not None:
            self.VulHighStat = EventStat()
            self.VulHighStat._deserialize(params.get("VulHighStat"))
        if params.get("VulNormalStat") is not None:
            self.VulNormalStat = EventStat()
            self.VulNormalStat._deserialize(params.get("VulNormalStat"))
        if params.get("VulLowStat") is not None:
            self.VulLowStat = EventStat()
            self.VulLowStat._deserialize(params.get("VulLowStat"))
        if params.get("BaselineHighStat") is not None:
            self.BaselineHighStat = EventStat()
            self.BaselineHighStat._deserialize(params.get("BaselineHighStat"))
        if params.get("BaselineNormalStat") is not None:
            self.BaselineNormalStat = EventStat()
            self.BaselineNormalStat._deserialize(params.get("BaselineNormalStat"))
        if params.get("BaselineLowStat") is not None:
            self.BaselineLowStat = EventStat()
            self.BaselineLowStat._deserialize(params.get("BaselineLowStat"))
        self.MachineTotalAffectNum = params.get("MachineTotalAffectNum")
        self.InvasionTotalAffectNum = params.get("InvasionTotalAffectNum")
        self.VulTotalAffectNum = params.get("VulTotalAffectNum")
        self.BaseLineTotalAffectNum = params.get("BaseLineTotalAffectNum")
        self.CyberAttackTotalAffectNum = params.get("CyberAttackTotalAffectNum")
        if params.get("VulRiskStat") is not None:
            self.VulRiskStat = EventStat()
            self.VulRiskStat._deserialize(params.get("VulRiskStat"))
        if params.get("BaselineRiskStat") is not None:
            self.BaselineRiskStat = EventStat()
            self.BaselineRiskStat._deserialize(params.get("BaselineRiskStat"))
        if params.get("VulStat") is not None:
            self.VulStat = EventStat()
            self.VulStat._deserialize(params.get("VulStat"))
        self.Score = params.get("Score")
        self.RequestId = params.get("RequestId")


class DescribeSecurityEventsCntRequest(AbstractModel):
    """DescribeSecurityEventsCnt请求参数结构体

    """


class DescribeSecurityEventsCntResponse(AbstractModel):
    """DescribeSecurityEventsCnt返回参数结构体

    """

    def __init__(self):
        r"""
        :param Malware: 木马文件相关风险事件
        :type Malware: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param HostLogin: 登录审计相关风险事件
        :type HostLogin: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param BruteAttack: 密码破解相关风险事件
        :type BruteAttack: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param RiskDns: 恶意请求相关风险事件
        :type RiskDns: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param Bash: 高危命令相关风险事件
        :type Bash: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param PrivilegeRules: 本地提权相关风险事件
        :type PrivilegeRules: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param ReverseShell: 反弹Shell相关风险事件
        :type ReverseShell: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param SysVul: 应用漏洞风险事件
        :type SysVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param WebVul: Web应用漏洞相关风险事件
        :type WebVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param EmergencyVul: 应急漏洞相关风险事件
        :type EmergencyVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param BaseLine: 安全基线相关风险事件
        :type BaseLine: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param AttackLogs: 攻击检测相关风险事件
        :type AttackLogs: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param EffectMachineCount: 受影响机器数
        :type EffectMachineCount: int
        :param EventsCount: 所有事件总数
        :type EventsCount: int
        :param WindowVul: window 系统漏洞事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type WindowVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param LinuxVul: linux系统漏洞事件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type LinuxVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Malware = None
        self.HostLogin = None
        self.BruteAttack = None
        self.RiskDns = None
        self.Bash = None
        self.PrivilegeRules = None
        self.ReverseShell = None
        self.SysVul = None
        self.WebVul = None
        self.EmergencyVul = None
        self.BaseLine = None
        self.AttackLogs = None
        self.EffectMachineCount = None
        self.EventsCount = None
        self.WindowVul = None
        self.LinuxVul = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malware") is not None:
            self.Malware = SecurityEventInfo()
            self.Malware._deserialize(params.get("Malware"))
        if params.get("HostLogin") is not None:
            self.HostLogin = SecurityEventInfo()
            self.HostLogin._deserialize(params.get("HostLogin"))
        if params.get("BruteAttack") is not None:
            self.BruteAttack = SecurityEventInfo()
            self.BruteAttack._deserialize(params.get("BruteAttack"))
        if params.get("RiskDns") is not None:
            self.RiskDns = SecurityEventInfo()
            self.RiskDns._deserialize(params.get("RiskDns"))
        if params.get("Bash") is not None:
            self.Bash = SecurityEventInfo()
            self.Bash._deserialize(params.get("Bash"))
        if params.get("PrivilegeRules") is not None:
            self.PrivilegeRules = SecurityEventInfo()
            self.PrivilegeRules._deserialize(params.get("PrivilegeRules"))
        if params.get("ReverseShell") is not None:
            self.ReverseShell = SecurityEventInfo()
            self.ReverseShell._deserialize(params.get("ReverseShell"))
        if params.get("SysVul") is not None:
            self.SysVul = SecurityEventInfo()
            self.SysVul._deserialize(params.get("SysVul"))
        if params.get("WebVul") is not None:
            self.WebVul = SecurityEventInfo()
            self.WebVul._deserialize(params.get("WebVul"))
        if params.get("EmergencyVul") is not None:
            self.EmergencyVul = SecurityEventInfo()
            self.EmergencyVul._deserialize(params.get("EmergencyVul"))
        if params.get("BaseLine") is not None:
            self.BaseLine = SecurityEventInfo()
            self.BaseLine._deserialize(params.get("BaseLine"))
        if params.get("AttackLogs") is not None:
            self.AttackLogs = SecurityEventInfo()
            self.AttackLogs._deserialize(params.get("AttackLogs"))
        self.EffectMachineCount = params.get("EffectMachineCount")
        self.EventsCount = params.get("EventsCount")
        if params.get("WindowVul") is not None:
            self.WindowVul = SecurityEventInfo()
            self.WindowVul._deserialize(params.get("WindowVul"))
        if params.get("LinuxVul") is not None:
            self.LinuxVul = SecurityEventInfo()
            self.LinuxVul._deserialize(params.get("LinuxVul"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginDate: 开始时间，如：2021-07-10
        :type BeginDate: str
        :param EndDate: 结束时间，如：2021-07-10
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends返回参数结构体

    """

    def __init__(self):
        r"""
        :param Malwares: 木马事件统计数据数组。
        :type Malwares: list of SecurityTrend
        :param NonLocalLoginPlaces: 异地登录事件统计数据数组。
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param BruteAttacks: 密码破解事件统计数据数组。
        :type BruteAttacks: list of SecurityTrend
        :param Vuls: 漏洞统计数据数组。
        :type Vuls: list of SecurityTrend
        :param BaseLines: 基线统计数据数组。
        :type BaseLines: list of SecurityTrend
        :param MaliciousRequests: 恶意请求统计数据数组。
        :type MaliciousRequests: list of SecurityTrend
        :param HighRiskBashs: 高危命令统计数据数组。
        :type HighRiskBashs: list of SecurityTrend
        :param ReverseShells: 反弹shell统计数据数组。
        :type ReverseShells: list of SecurityTrend
        :param PrivilegeEscalations: 本地提权统计数据数组。
        :type PrivilegeEscalations: list of SecurityTrend
        :param CyberAttacks: 网络攻击统计数据数组。
        :type CyberAttacks: list of SecurityTrend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Malwares = None
        self.NonLocalLoginPlaces = None
        self.BruteAttacks = None
        self.Vuls = None
        self.BaseLines = None
        self.MaliciousRequests = None
        self.HighRiskBashs = None
        self.ReverseShells = None
        self.PrivilegeEscalations = None
        self.CyberAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self.BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BaseLines.append(obj)
        if params.get("MaliciousRequests") is not None:
            self.MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.MaliciousRequests.append(obj)
        if params.get("HighRiskBashs") is not None:
            self.HighRiskBashs = []
            for item in params.get("HighRiskBashs"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.HighRiskBashs.append(obj)
        if params.get("ReverseShells") is not None:
            self.ReverseShells = []
            for item in params.get("ReverseShells"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.ReverseShells.append(obj)
        if params.get("PrivilegeEscalations") is not None:
            self.PrivilegeEscalations = []
            for item in params.get("PrivilegeEscalations"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.PrivilegeEscalations.append(obj)
        if params.get("CyberAttacks") is not None:
            self.CyberAttacks = []
            for item in params.get("CyberAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.CyberAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServerRelatedDirInfoRequest(AbstractModel):
    """DescribeServerRelatedDirInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 唯一ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServerRelatedDirInfoResponse(AbstractModel):
    """DescribeServerRelatedDirInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param HostName: 服务器名称
        :type HostName: str
        :param HostIp: 服务器IP
        :type HostIp: str
        :param ProtectDirNum: 防护目录数量
        :type ProtectDirNum: int
        :param ProtectFileNum: 防护文件数量
        :type ProtectFileNum: int
        :param ProtectTamperNum: 防篡改数量
        :type ProtectTamperNum: int
        :param ProtectLinkNum: 防护软链数量
        :type ProtectLinkNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HostName = None
        self.HostIp = None
        self.ProtectDirNum = None
        self.ProtectFileNum = None
        self.ProtectTamperNum = None
        self.ProtectLinkNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.HostIp = params.get("HostIp")
        self.ProtectDirNum = params.get("ProtectDirNum")
        self.ProtectFileNum = params.get("ProtectFileNum")
        self.ProtectTamperNum = params.get("ProtectTamperNum")
        self.ProtectLinkNum = params.get("ProtectLinkNum")
        self.RequestId = params.get("RequestId")


class DescribeServersAndRiskAndFirstInfoRequest(AbstractModel):
    """DescribeServersAndRiskAndFirstInfo请求参数结构体

    """


class DescribeServersAndRiskAndFirstInfoResponse(AbstractModel):
    """DescribeServersAndRiskAndFirstInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RiskFileCount: 风险文件数
        :type RiskFileCount: int
        :param AddRiskFileCount: 今日新增风险文件数
        :type AddRiskFileCount: int
        :param ServersCount: 受影响服务器台数
        :type ServersCount: int
        :param IsFirstCheck: 是否试用：true-是，false-否
        :type IsFirstCheck: bool
        :param ScanTime: 木马最近检测时间
        :type ScanTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RiskFileCount = None
        self.AddRiskFileCount = None
        self.ServersCount = None
        self.IsFirstCheck = None
        self.ScanTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RiskFileCount = params.get("RiskFileCount")
        self.AddRiskFileCount = params.get("AddRiskFileCount")
        self.ServersCount = params.get("ServersCount")
        self.IsFirstCheck = params.get("IsFirstCheck")
        self.ScanTime = params.get("ScanTime")
        self.RequestId = params.get("RequestId")


class DescribeStrategyExistRequest(AbstractModel):
    """DescribeStrategyExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param StrategyName: 策略名
        :type StrategyName: str
        """
        self.StrategyName = None


    def _deserialize(self, params):
        self.StrategyName = params.get("StrategyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategyExistResponse(AbstractModel):
    """DescribeStrategyExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param IfExist: 策略是否存在, 1是 0否
注意：此字段可能返回 null，表示取不到有效值。
        :type IfExist: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IfExist = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IfExist = params.get("IfExist")
        self.RequestId = params.get("RequestId")


class DescribeTagMachinesRequest(AbstractModel):
    """DescribeTagMachines请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 标签ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagMachinesResponse(AbstractModel):
    """DescribeTagMachines返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 列表数据
        :type List: list of TagMachine
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = TagMachine()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param MachineType: 云主机类型。
<li>CVM：表示云服务器</li>
<li>BM:  表示黑石物理机</li>
<li>ECM:  表示边缘计算服务器</li>
<li>LH:  表示轻量应用服务器</li>
<li>Other:  表示混合云服务器</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou
        :type MachineRegion: str
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字(机器名称/机器IP </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装 | SHUTDOWN 已关机）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
<li>Risk - String 是否必填: 否 - 风险主机( yes ) </li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filters
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 列表信息
        :type List: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUndoVulCountsRequest(AbstractModel):
    """DescribeUndoVulCounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param VulCategory: 漏洞分类，1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞
        :type VulCategory: int
        :param IfEmergency: 是否应急漏洞筛选, 是 : yes
        :type IfEmergency: str
        """
        self.VulCategory = None
        self.IfEmergency = None


    def _deserialize(self, params):
        self.VulCategory = params.get("VulCategory")
        self.IfEmergency = params.get("IfEmergency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUndoVulCountsResponse(AbstractModel):
    """DescribeUndoVulCounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param UndoVulCount: 未处理的漏洞数
注意：此字段可能返回 null，表示取不到有效值。
        :type UndoVulCount: int
        :param UndoHostCount: 未处理的主机数
注意：此字段可能返回 null，表示取不到有效值。
        :type UndoHostCount: int
        :param NotProfessionCount: 普通版主机数
注意：此字段可能返回 null，表示取不到有效值。
        :type NotProfessionCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UndoVulCount = None
        self.UndoHostCount = None
        self.NotProfessionCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UndoVulCount = params.get("UndoVulCount")
        self.UndoHostCount = params.get("UndoHostCount")
        self.NotProfessionCount = params.get("NotProfessionCount")
        self.RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 云镜客户端UUID
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param UsualLoginPlaces: 常用登录地数组
        :type UsualLoginPlaces: list of UsualPlace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UsualLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self.UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self.UsualLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVersionStatisticsRequest(AbstractModel):
    """DescribeVersionStatistics请求参数结构体

    """


class DescribeVersionStatisticsResponse(AbstractModel):
    """DescribeVersionStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param BasicVersionNum: 基础版数量
        :type BasicVersionNum: int
        :param ProVersionNum: 专业版数量
        :type ProVersionNum: int
        :param UltimateVersionNum: 旗舰版数量
        :type UltimateVersionNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BasicVersionNum = None
        self.ProVersionNum = None
        self.UltimateVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BasicVersionNum = params.get("BasicVersionNum")
        self.ProVersionNum = params.get("ProVersionNum")
        self.UltimateVersionNum = params.get("UltimateVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeVulCountByDatesRequest(AbstractModel):
    """DescribeVulCountByDates请求参数结构体

    """

    def __init__(self):
        r"""
        :param LastDays: 需要查询最近几天的数据，需要都 -1后传入
        :type LastDays: list of int non-negative
        :param VulCategory: 漏洞的分类: 1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞
        :type VulCategory: int
        :param IfEmergency: 是否为应急漏洞筛选  是: yes
        :type IfEmergency: str
        """
        self.LastDays = None
        self.VulCategory = None
        self.IfEmergency = None


    def _deserialize(self, params):
        self.LastDays = params.get("LastDays")
        self.VulCategory = params.get("VulCategory")
        self.IfEmergency = params.get("IfEmergency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulCountByDatesResponse(AbstractModel):
    """DescribeVulCountByDates返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulCount: 批量获得对应天数的漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCount: list of int non-negative
        :param HostCount: 批量获得对应天数的主机数量
        :type HostCount: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulCount = None
        self.HostCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulCount = params.get("VulCount")
        self.HostCount = params.get("HostCount")
        self.RequestId = params.get("RequestId")


class DescribeVulEffectHostListRequest(AbstractModel):
    """DescribeVulEffectHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页limit 最大100
        :type Limit: int
        :param Offset: 分页Offset
        :type Offset: int
        :param VulId: 漏洞id
        :type VulId: int
        :param Filters: 过滤条件：
<li>AliasName - String - 主机名筛选</li>
<li>TagIds - String - 主机标签id串，多个用英文用逗号分隔</li>
<li>Status - String - 状态：0-待处理 1-忽略  3-已修复  5-检测中  6-修复中  8-修复失败</li>
<li>Uuid - String数组 - Uuid串数组</li>
<li>Version - String数组 - 付费版本数组："Flagship"-旗舰版 "PRO_VERSION"-专业版 "BASIC_VERSION"-基础版</li>
<li>InstanceState - String数组 - 实例状态数组："PENDING"-创建中 "LAUNCH_FAILED"-创建失败 "RUNNING"-运行中 "STOPPED"-关机 "STARTING"-开机中 "STOPPING"-关机中 "REBOOTING"-重启中 "SHUTDOWN"-待销毁 "TERMINATING"-销毁中 "UNKNOWN"-未知（针对非腾讯云机器，且客户端离线的场景） </li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.VulId = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.VulId = params.get("VulId")
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
        


class DescribeVulEffectHostListResponse(AbstractModel):
    """DescribeVulEffectHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 列表总数量
        :type TotalCount: int
        :param VulEffectHostList: 影响主机列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulEffectHostList: list of VulEffectHostList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VulEffectHostList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VulEffectHostList") is not None:
            self.VulEffectHostList = []
            for item in params.get("VulEffectHostList"):
                obj = VulEffectHostList()
                obj._deserialize(item)
                self.VulEffectHostList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulHostCountScanTimeRequest(AbstractModel):
    """DescribeVulHostCountScanTime请求参数结构体

    """


class DescribeVulHostCountScanTimeResponse(AbstractModel):
    """DescribeVulHostCountScanTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalVulCount: 总漏洞数
        :type TotalVulCount: int
        :param VulHostCount: 漏洞影响主机数
        :type VulHostCount: int
        :param ScanTime: 扫描时间
        :type ScanTime: str
        :param IfFirstScan: 是否第一次检测
        :type IfFirstScan: bool
        :param TaskId: 运行中的任务号, 没有任务则为0
        :type TaskId: int
        :param LastFixTime: 最后一次修复漏洞的时间
        :type LastFixTime: str
        :param hadAutoFixVul: 是否有支持自动修复的漏洞事件
        :type hadAutoFixVul: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalVulCount = None
        self.VulHostCount = None
        self.ScanTime = None
        self.IfFirstScan = None
        self.TaskId = None
        self.LastFixTime = None
        self.hadAutoFixVul = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalVulCount = params.get("TotalVulCount")
        self.VulHostCount = params.get("VulHostCount")
        self.ScanTime = params.get("ScanTime")
        self.IfFirstScan = params.get("IfFirstScan")
        self.TaskId = params.get("TaskId")
        self.LastFixTime = params.get("LastFixTime")
        self.hadAutoFixVul = params.get("hadAutoFixVul")
        self.RequestId = params.get("RequestId")


class DescribeVulHostTopRequest(AbstractModel):
    """DescribeVulHostTop请求参数结构体

    """

    def __init__(self):
        r"""
        :param Top: 获取top值，1-100
        :type Top: int
        :param VulCategory: 1:web-cms 漏洞，2.应用漏洞   4: Linux软件漏洞 5: windows系统漏洞 6:应急漏洞，不填或者填0时返回 1，2，4，5 的总统计数据
        :type VulCategory: int
        :param IsFollowVul: 是否仅统计重点关注漏洞 1=仅统计重点关注漏洞, 0=统计全部漏洞
        :type IsFollowVul: int
        """
        self.Top = None
        self.VulCategory = None
        self.IsFollowVul = None


    def _deserialize(self, params):
        self.Top = params.get("Top")
        self.VulCategory = params.get("VulCategory")
        self.IsFollowVul = params.get("IsFollowVul")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulHostTopResponse(AbstractModel):
    """DescribeVulHostTop返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulHostTopList: 服务器风险top列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulHostTopList: list of VulHostTopInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulHostTopList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulHostTopList") is not None:
            self.VulHostTopList = []
            for item in params.get("VulHostTopList"):
                obj = VulHostTopInfo()
                obj._deserialize(item)
                self.VulHostTopList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulInfoCvssRequest(AbstractModel):
    """DescribeVulInfoCvss请求参数结构体

    """

    def __init__(self):
        r"""
        :param VulId: 漏洞id
        :type VulId: int
        """
        self.VulId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulInfoCvssResponse(AbstractModel):
    """DescribeVulInfoCvss返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulId: 漏洞id
注意：此字段可能返回 null，表示取不到有效值。
        :type VulId: int
        :param VulName: 漏洞名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VulName: str
        :param VulLevel: 危害等级：1-低危；2-中危；3-高危；4-严重
注意：此字段可能返回 null，表示取不到有效值。
        :type VulLevel: int
        :param VulType: 漏洞分类 1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type VulType: int
        :param Description: 漏洞描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param RepairPlan: 修复方案
注意：此字段可能返回 null，表示取不到有效值。
        :type RepairPlan: str
        :param CveId: 漏洞CVEID
注意：此字段可能返回 null，表示取不到有效值。
        :type CveId: str
        :param Reference: 参考链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: str
        :param CVSS: CVSS信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CVSS: str
        :param PublicDate: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicDate: str
        :param CvssScore: Cvss分数
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssScore: int
        :param CveInfo: cvss详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CveInfo: str
        :param CvssScoreFloat: cvss 分数 浮点型
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssScoreFloat: float
        :param Labels: 漏洞标签 多个逗号分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: str
        :param DefenseAttackCount: 已防御的攻击次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseAttackCount: int
        :param SuccessFixCount: 全网修复成功次数, 不支持自动修复的漏洞默认返回0
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessFixCount: int
        :param FixSwitch: 修复是否支持：0-windows/linux均不支持修复 ;1-windows/linux 均支持修复 ;2-仅linux支持修复;3-仅windows支持修复
注意：此字段可能返回 null，表示取不到有效值。
        :type FixSwitch: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.VulType = None
        self.Description = None
        self.RepairPlan = None
        self.CveId = None
        self.Reference = None
        self.CVSS = None
        self.PublicDate = None
        self.CvssScore = None
        self.CveInfo = None
        self.CvssScoreFloat = None
        self.Labels = None
        self.DefenseAttackCount = None
        self.SuccessFixCount = None
        self.FixSwitch = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.RepairPlan = params.get("RepairPlan")
        self.CveId = params.get("CveId")
        self.Reference = params.get("Reference")
        self.CVSS = params.get("CVSS")
        self.PublicDate = params.get("PublicDate")
        self.CvssScore = params.get("CvssScore")
        self.CveInfo = params.get("CveInfo")
        self.CvssScoreFloat = params.get("CvssScoreFloat")
        self.Labels = params.get("Labels")
        self.DefenseAttackCount = params.get("DefenseAttackCount")
        self.SuccessFixCount = params.get("SuccessFixCount")
        self.FixSwitch = params.get("FixSwitch")
        self.RequestId = params.get("RequestId")


class DescribeVulLevelCountRequest(AbstractModel):
    """DescribeVulLevelCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param VulCategory: 1:web-cms 漏洞，2.应用漏洞 3:安全基线 4: Linux软件漏洞 5: windows系统漏洞 6:应急漏洞，不填或者填0时返回 1，2，4，5 的总统计数据
        :type VulCategory: int
        :param IsFollowVul: 是否仅统计重点关注漏洞 1=仅统计重点关注漏洞, 0=统计全部漏洞
        :type IsFollowVul: int
        """
        self.VulCategory = None
        self.IsFollowVul = None


    def _deserialize(self, params):
        self.VulCategory = params.get("VulCategory")
        self.IsFollowVul = params.get("IsFollowVul")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulLevelCountResponse(AbstractModel):
    """DescribeVulLevelCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulLevelList: 统计结果
注意：此字段可能返回 null，表示取不到有效值。
        :type VulLevelList: list of VulLevelInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulLevelList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulLevelList") is not None:
            self.VulLevelList = []
            for item in params.get("VulLevelList"):
                obj = VulLevelInfo()
                obj._deserialize(item)
                self.VulLevelList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulListRequest(AbstractModel):
    """DescribeVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Status - String - 是否必填：否 - 处理状态  0 -- 待处理 1 -- 已加白 2 -- 已删除 3 - 已忽略</li>
<li>ModifyTime - String - 是否必填：否 - 最近发生时间</li>
<li>Uuid- String - 是否必填：否 - 主机uuid查询</li>
<li>VulName- string -</li>
<li>VulCategory- string - 是否必填：否 - 漏洞类别 1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞</li>
<li>IsSupportDefense - int- 是否必填：否 - 是否支持防御 0:不支持 1:支持</li>
<li>Labels- string- 是否必填：否 - 标签搜索</li>
        :type Filters: list of Filters
        :param By: 可选排序字段 Level，LastTime，HostCount
        :type By: str
        :param Order: 排序顺序：desc  默认asc
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulListResponse(AbstractModel):
    """DescribeVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulInfoList: 漏洞列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulInfoList: list of VulInfoList
        :param TotalCount: 漏洞总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param FollowVulCount: 重点关注漏洞总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowVulCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulInfoList = None
        self.TotalCount = None
        self.FollowVulCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulInfoList") is not None:
            self.VulInfoList = []
            for item in params.get("VulInfoList"):
                obj = VulInfoList()
                obj._deserialize(item)
                self.VulInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.FollowVulCount = params.get("FollowVulCount")
        self.RequestId = params.get("RequestId")


class DescribeVulTopRequest(AbstractModel):
    """DescribeVulTop请求参数结构体

    """

    def __init__(self):
        r"""
        :param Top: 漏洞风险服务器top，1-100
        :type Top: int
        :param VulCategory: 1:web-cms 漏洞，2.应用漏洞 4: Linux软件漏洞 5: windows系统漏洞 6:应急漏洞，不填或者填0时返回 1，2，4，5 的总统计数据
        :type VulCategory: int
        :param IsFollowVul: 是否仅统计重点关注漏洞 1=仅统计重点关注漏洞, 0=统计全部漏洞
        :type IsFollowVul: int
        """
        self.Top = None
        self.VulCategory = None
        self.IsFollowVul = None


    def _deserialize(self, params):
        self.Top = params.get("Top")
        self.VulCategory = params.get("VulCategory")
        self.IsFollowVul = params.get("IsFollowVul")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulTopResponse(AbstractModel):
    """DescribeVulTop返回参数结构体

    """

    def __init__(self):
        r"""
        :param VulTopList: 漏洞top列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulTopList: list of VulTopInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulTopList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VulTopList") is not None:
            self.VulTopList = []
            for item in params.get("VulTopList"):
                obj = VulTopInfo()
                obj._deserialize(item)
                self.VulTopList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWarningListRequest(AbstractModel):
    """DescribeWarningList请求参数结构体

    """


class DescribeWarningListResponse(AbstractModel):
    """DescribeWarningList返回参数结构体

    """

    def __init__(self):
        r"""
        :param WarningInfoList: 获取告警列表
        :type WarningInfoList: list of WarningInfoObj
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WarningInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WarningInfoList") is not None:
            self.WarningInfoList = []
            for item in params.get("WarningInfoList"):
                obj = WarningInfoObj()
                obj._deserialize(item)
                self.WarningInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebPageEventListRequest(AbstractModel):
    """DescribeWebPageEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>EventType - String - 是否必填：否 - 事件类型</li>
<li>EventStatus - String - 是否必填：否 - 事件状态</li>
        :type Filters: list of AssetFilters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param By: 排序方式：CreateTime 或 RestoreTime，默认为CreateTime
        :type By: str
        :param Order: 排序方式，0降序，1升序，默认为0
        :type Order: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebPageEventListResponse(AbstractModel):
    """DescribeWebPageEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 防护事件列表信息
        :type List: list of ProtectEventLists
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ProtectEventLists()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWebPageGeneralizeRequest(AbstractModel):
    """DescribeWebPageGeneralize请求参数结构体

    """


class DescribeWebPageGeneralizeResponse(AbstractModel):
    """DescribeWebPageGeneralize返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProtectMonitor: 防护监测 0 未开启 1 已开启 2 异常
        :type ProtectMonitor: int
        :param ProtectDirNum: 防护目录数
        :type ProtectDirNum: int
        :param ProtectFileNum: 防护文件数
        :type ProtectFileNum: int
        :param TamperFileNum: 篡改文件数
        :type TamperFileNum: int
        :param TamperNum: 篡改数
        :type TamperNum: int
        :param ProtectToday: 今日防护数
        :type ProtectToday: int
        :param ProtectHostNum: 防护主机数
        :type ProtectHostNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProtectMonitor = None
        self.ProtectDirNum = None
        self.ProtectFileNum = None
        self.TamperFileNum = None
        self.TamperNum = None
        self.ProtectToday = None
        self.ProtectHostNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProtectMonitor = params.get("ProtectMonitor")
        self.ProtectDirNum = params.get("ProtectDirNum")
        self.ProtectFileNum = params.get("ProtectFileNum")
        self.TamperFileNum = params.get("TamperFileNum")
        self.TamperNum = params.get("TamperNum")
        self.ProtectToday = params.get("ProtectToday")
        self.ProtectHostNum = params.get("ProtectHostNum")
        self.RequestId = params.get("RequestId")


class DescribeWebPageProtectStatRequest(AbstractModel):
    """DescribeWebPageProtectStat请求参数结构体

    """


class DescribeWebPageProtectStatResponse(AbstractModel):
    """DescribeWebPageProtectStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileTamperNum: 文件篡改信息
        :type FileTamperNum: list of ProtectStat
        :param ProtectFileType: 防护文件分类信息
        :type ProtectFileType: list of ProtectStat
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileTamperNum = None
        self.ProtectFileType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileTamperNum") is not None:
            self.FileTamperNum = []
            for item in params.get("FileTamperNum"):
                obj = ProtectStat()
                obj._deserialize(item)
                self.FileTamperNum.append(obj)
        if params.get("ProtectFileType") is not None:
            self.ProtectFileType = []
            for item in params.get("ProtectFileType"):
                obj = ProtectStat()
                obj._deserialize(item)
                self.ProtectFileType.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebPageServiceInfoRequest(AbstractModel):
    """DescribeWebPageServiceInfo请求参数结构体

    """


class DescribeWebPageServiceInfoResponse(AbstractModel):
    """DescribeWebPageServiceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 是否已购服务：true-是，false-否
        :type Status: bool
        :param UsedNum: 已使用授权数
        :type UsedNum: int
        :param ResidueNum: 剩余授权数
        :type ResidueNum: int
        :param BuyNum: 已购授权数
        :type BuyNum: int
        :param ExpireNum: 临近到期数量
        :type ExpireNum: int
        :param AllAuthorizedMachines: 所有授权机器信息
        :type AllAuthorizedMachines: list of ProtectMachineInfo
        :param ExpireAuthorizedMachines: 临近到期授权机器信息
        :type ExpireAuthorizedMachines: list of ProtectMachine
        :param ExpiredNum: 已过期授权数
        :type ExpiredNum: int
        :param ProtectDirNum: 防护目录数
        :type ProtectDirNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.UsedNum = None
        self.ResidueNum = None
        self.BuyNum = None
        self.ExpireNum = None
        self.AllAuthorizedMachines = None
        self.ExpireAuthorizedMachines = None
        self.ExpiredNum = None
        self.ProtectDirNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.UsedNum = params.get("UsedNum")
        self.ResidueNum = params.get("ResidueNum")
        self.BuyNum = params.get("BuyNum")
        self.ExpireNum = params.get("ExpireNum")
        if params.get("AllAuthorizedMachines") is not None:
            self.AllAuthorizedMachines = []
            for item in params.get("AllAuthorizedMachines"):
                obj = ProtectMachineInfo()
                obj._deserialize(item)
                self.AllAuthorizedMachines.append(obj)
        if params.get("ExpireAuthorizedMachines") is not None:
            self.ExpireAuthorizedMachines = []
            for item in params.get("ExpireAuthorizedMachines"):
                obj = ProtectMachine()
                obj._deserialize(item)
                self.ExpireAuthorizedMachines.append(obj)
        self.ExpiredNum = params.get("ExpiredNum")
        self.ProtectDirNum = params.get("ProtectDirNum")
        self.RequestId = params.get("RequestId")


class DestroyOrderRequest(AbstractModel):
    """DestroyOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param LicenseType: 授权类型 0 专业版-按量计费, 1专业版-包年包月 , 2 旗舰版-包年包月
        :type LicenseType: int
        """
        self.ResourceId = None
        self.LicenseType = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyOrderResponse(AbstractModel):
    """DestroyOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditBashRulesRequest(AbstractModel):
    """EditBashRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 规则ID（新增时不填）
        :type Id: int
        :param Uuids: 客户端ID数组
        :type Uuids: list of str
        :param HostIp: 主机IP
        :type HostIp: str
        :param Name: 规则名称，编辑时不可修改规则名称
        :type Name: str
        :param Level: 危险等级(0:无，1: 高危 2:中危 3: 低危)
        :type Level: int
        :param Rule: 正则表达式 ，编辑时不可修改正则表达式，需要对内容QueryEscape后再base64
        :type Rule: str
        :param IsGlobal: 是否全局规则(默认否)：1-全局，0-非全局
        :type IsGlobal: int
        :param White: 0=黑名单， 1=白名单
        :type White: int
        :param EventId: 事件列表点击“加入白名单”时,需要传EventId 事件的id
        :type EventId: int
        :param DealOldEvents: 是否处理旧事件为白名单 0=不处理 1=处理
        :type DealOldEvents: int
        """
        self.Id = None
        self.Uuids = None
        self.HostIp = None
        self.Name = None
        self.Level = None
        self.Rule = None
        self.IsGlobal = None
        self.White = None
        self.EventId = None
        self.DealOldEvents = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuids = params.get("Uuids")
        self.HostIp = params.get("HostIp")
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Rule = params.get("Rule")
        self.IsGlobal = params.get("IsGlobal")
        self.White = params.get("White")
        self.EventId = params.get("EventId")
        self.DealOldEvents = params.get("DealOldEvents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditBashRulesResponse(AbstractModel):
    """EditBashRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditTagsRequest(AbstractModel):
    """EditTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 标签名
        :type Name: str
        :param Id: 标签ID
        :type Id: int
        :param Quuids: Quuid
        :type Quuids: list of str
        """
        self.Name = None
        self.Id = None
        self.Quuids = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditTagsResponse(AbstractModel):
    """EditTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EffectiveMachineInfo(AbstractModel):
    """批量导入机器信息.

    """

    def __init__(self):
        r"""
        :param MachineName: 机器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineName: str
        :param MachinePublicIp: 机器公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachinePublicIp: str
        :param MachinePrivateIp: 机器内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachinePrivateIp: str
        :param MachineTag: 机器标签
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineTag: list of MachineTag
        :param Quuid: 机器Quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param Uuid: 云镜Uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param KernelVersion: 内核版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type KernelVersion: str
        :param MachineStatus: 在线状态 OFFLINE，ONLINE
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineStatus: str
        :param LicenseOrder: 授权订单对象
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseOrder: :class:`tencentcloud.cwp.v20180228.models.LicenseOrder`
        :param VulNum: 漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :type VulNum: int
        """
        self.MachineName = None
        self.MachinePublicIp = None
        self.MachinePrivateIp = None
        self.MachineTag = None
        self.Quuid = None
        self.Uuid = None
        self.KernelVersion = None
        self.MachineStatus = None
        self.LicenseOrder = None
        self.VulNum = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachinePublicIp = params.get("MachinePublicIp")
        self.MachinePrivateIp = params.get("MachinePrivateIp")
        if params.get("MachineTag") is not None:
            self.MachineTag = []
            for item in params.get("MachineTag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.MachineTag.append(obj)
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.KernelVersion = params.get("KernelVersion")
        self.MachineStatus = params.get("MachineStatus")
        if params.get("LicenseOrder") is not None:
            self.LicenseOrder = LicenseOrder()
            self.LicenseOrder._deserialize(params.get("LicenseOrder"))
        self.VulNum = params.get("VulNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmergencyResponseInfo(AbstractModel):
    """专家服务-应急响应信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param HostNum: 主机个数
        :type HostNum: int
        :param Status: 服务状态 0未启动，·响应中，2响应完成
        :type Status: int
        :param StartTime: 服务开始时间
        :type StartTime: str
        :param EndTime: 服务结束时间
        :type EndTime: str
        :param ReportPath: 报告下载地址
        :type ReportPath: str
        """
        self.TaskId = None
        self.HostNum = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.ReportPath = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.HostNum = params.get("HostNum")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReportPath = params.get("ReportPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmergencyVul(AbstractModel):
    """应急漏洞信息

    """

    def __init__(self):
        r"""
        :param VulId: 漏洞id
        :type VulId: int
        :param Level: 漏洞级别
        :type Level: int
        :param VulName: 漏洞名称
        :type VulName: str
        :param PublishDate: 发布日期
        :type PublishDate: str
        :param Category: 漏洞分类
        :type Category: int
        :param Status: 漏洞状态 0未检测 1有风险 ，2无风险 ，3 检查中展示progress
        :type Status: int
        :param LastScanTime: 最后扫描时间
        :type LastScanTime: str
        :param Progress: 扫描进度
        :type Progress: int
        :param CveId: cve编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CveId: str
        :param CvssScore: CVSS评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssScore: float
        :param Labels: 漏洞标签 多个逗号分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: str
        :param HostCount: 影响机器数
注意：此字段可能返回 null，表示取不到有效值。
        :type HostCount: int
        :param IsSupportDefense: 是否支持防御， 0:不支持 1:支持
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportDefense: int
        :param DefenseAttackCount: 已防御的攻击次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseAttackCount: int
        """
        self.VulId = None
        self.Level = None
        self.VulName = None
        self.PublishDate = None
        self.Category = None
        self.Status = None
        self.LastScanTime = None
        self.Progress = None
        self.CveId = None
        self.CvssScore = None
        self.Labels = None
        self.HostCount = None
        self.IsSupportDefense = None
        self.DefenseAttackCount = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Level = params.get("Level")
        self.VulName = params.get("VulName")
        self.PublishDate = params.get("PublishDate")
        self.Category = params.get("Category")
        self.Status = params.get("Status")
        self.LastScanTime = params.get("LastScanTime")
        self.Progress = params.get("Progress")
        self.CveId = params.get("CveId")
        self.CvssScore = params.get("CvssScore")
        self.Labels = params.get("Labels")
        self.HostCount = params.get("HostCount")
        self.IsSupportDefense = params.get("IsSupportDefense")
        self.DefenseAttackCount = params.get("DefenseAttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventStat(AbstractModel):
    """未处理的安全事件统计信息

    """

    def __init__(self):
        r"""
        :param EventsNum: 事件数
        :type EventsNum: int
        :param MachineAffectNum: 受影响的主机数
        :type MachineAffectNum: int
        """
        self.EventsNum = None
        self.MachineAffectNum = None


    def _deserialize(self, params):
        self.EventsNum = params.get("EventsNum")
        self.MachineAffectNum = params.get("MachineAffectNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpertServiceOrderInfo(AbstractModel):
    """专家服务订单信息

    """

    def __init__(self):
        r"""
        :param OrderId: 订单id
        :type OrderId: int
        :param InquireType: 订单类型 1应急 2 旗舰重保 3 安全管家
        :type InquireType: int
        :param InquireNum: 服务数量
        :type InquireNum: int
        :param BeginTime: 服务开始时间
        :type BeginTime: str
        :param EndTime: 服务结束时间
        :type EndTime: str
        :param ServiceTime: 服务时长几个月
        :type ServiceTime: int
        :param Status: 订单状态 0 未启动 1 服务中 2已过期 3完成，4退费销毁
        :type Status: int
        """
        self.OrderId = None
        self.InquireType = None
        self.InquireNum = None
        self.BeginTime = None
        self.EndTime = None
        self.ServiceTime = None
        self.Status = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.InquireType = params.get("InquireType")
        self.InquireNum = params.get("InquireNum")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.ServiceTime = params.get("ServiceTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAssetCoreModuleListRequest(AbstractModel):
    """ExportAssetCoreModuleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Quuid: 服务器Quuid
        :type Quuid: str
        :param Filters: 过滤条件。
<li>Name- string - 是否必填：否 - 包名</li>
<li>User- string - 是否必填：否 - 用户</li>
        :type Filters: list of AssetFilters
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序依据[FirstTime|Size|ProcessCount|ModuleCount]
        :type By: str
        """
        self.Uuid = None
        self.Quuid = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAssetCoreModuleListResponse(AbstractModel):
    """ExportAssetCoreModuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 异步下载任务ID，需要配合ExportTasks接口使用
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportAssetWebServiceInfoListRequest(AbstractModel):
    """ExportAssetWebServiceInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 查询指定Quuid主机的信息
        :type Quuid: str
        :param Filters: 过滤条件。
<li>User- string - 是否必填：否 - 运行用户</li>
<li>Name- string - 是否必填：否 - Web服务名：
1:Tomcat
2:Apache
3:Nginx
4:WebLogic
5:Websphere
6:JBoss
7:WildFly
8:Jetty
9:IHS
10:Tengine</li>
<li>OsType- string - 是否必填：否 - Windows/linux</li>
        :type Filters: list of AssetFilters
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 可选排序：[FirstTime|ProcessCount]
        :type By: str
        """
        self.Quuid = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAssetWebServiceInfoListResponse(AbstractModel):
    """ExportAssetWebServiceInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 异步下载任务ID，需要配合ExportTasks接口使用
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportAttackLogsRequest(AbstractModel):
    """ExportAttackLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>HttpMethod - String - 是否必填：否 - 攻击方法(POST|GET)</li>
<li>DateRange - String - 是否必填：否 - 时间范围(存储最近3个月的数据)，如最近一个月["2019-11-17", "2019-12-17"]</li>
<li>VulType - String 威胁类型 - 是否必填: 否</li>
<li>SrcIp - String 攻击源IP - 是否必填: 否</li>
<li>DstIp - String 攻击目标IP - 是否必填: 否</li>
<li>SrcPort - String 攻击源端口 - 是否必填: 否</li>
<li>DstPort - String 攻击目标端口 - 是否必填: 否</li>
        :type Filters: list of Filters
        :param Uuid: 主机安全客户端ID
        :type Uuid: str
        :param Quuid: 云主机机器ID
        :type Quuid: str
        """
        self.Filters = None
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttackLogsResponse(AbstractModel):
    """ExportAttackLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 已废弃
        :type DownloadUrl: str
        :param TaskId: 导出任务ID 可通过ExportTasks接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportBaselineEffectHostListRequest(AbstractModel):
    """ExportBaselineEffectHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param BaselineId: 基线id
        :type BaselineId: int
        :param Filters: 筛选条件
<li>AliasName- String- 主机别名</li>
        :type Filters: list of Filters
        :param StrategyId: 策略id
        :type StrategyId: int
        :param UuidList: 主机uuid数组
        :type UuidList: list of str
        :param BaselineName: 基线名称
        :type BaselineName: str
        """
        self.BaselineId = None
        self.Filters = None
        self.StrategyId = None
        self.UuidList = None
        self.BaselineName = None


    def _deserialize(self, params):
        self.BaselineId = params.get("BaselineId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.StrategyId = params.get("StrategyId")
        self.UuidList = params.get("UuidList")
        self.BaselineName = params.get("BaselineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBaselineEffectHostListResponse(AbstractModel):
    """ExportBaselineEffectHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param TaskId: 导出任务id 可通过 ExportTasks接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportBaselineListRequest(AbstractModel):
    """ExportBaselineList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件：
<li>StrategyId- Uint64 - 基线策略id</li>
<li>Status - Uint64 - 事件状态：0-未通过，1-忽略，3-通过，5-检测中</li>
<li>BaselineName  - String - 基线名称</li>
<li>AliasName- String - 服务器名称/服务器ip</li>
<li>Uuid- String - 主机uuid</li>
        :type Filters: list of Filters
        :param IfDetail: 已废弃
        :type IfDetail: int
        """
        self.Filters = None
        self.IfDetail = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.IfDetail = params.get("IfDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBaselineListResponse(AbstractModel):
    """ExportBaselineList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载地址（已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param TaskId: 导出文件Id 可通过ExportTasks接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportBashEventsRequest(AbstractModel):
    """ExportBashEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBashEventsResponse(AbstractModel):
    """ExportBashEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportBruteAttacksRequest(AbstractModel):
    """ExportBruteAttacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBruteAttacksResponse(AbstractModel):
    """ExportBruteAttacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportIgnoreBaselineRuleRequest(AbstractModel):
    """ExportIgnoreBaselineRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleName: 检测项名称
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportIgnoreBaselineRuleResponse(AbstractModel):
    """ExportIgnoreBaselineRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 文件下载地址
        :type DownloadUrl: str
        :param TaskId: 导出任务Id , 可通过ExportTasks 接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportIgnoreRuleEffectHostListRequest(AbstractModel):
    """ExportIgnoreRuleEffectHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 检测项id
        :type RuleId: int
        :param Filters: 过滤条件。
<li>AliasName- String- 主机别名</li>
        :type Filters: list of Filters
        """
        self.RuleId = None
        self.Filters = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportIgnoreRuleEffectHostListResponse(AbstractModel):
    """ExportIgnoreRuleEffectHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载地址
        :type DownloadUrl: str
        :param TaskId: 导出任务Id , 可通过ExportTasks 接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportLicenseDetailRequest(AbstractModel):
    """ExportLicenseDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 多个条件筛选时 LicenseStatus,DeadlineStatus,ResourceId,Keywords 取交集
<li> LicenseType  授权类型, 0 专业版-按量计费, 1专业版-包年包月 , 2 旗舰版-包年包月</li>
<li>ResourceId 资源ID</li>
        :type Filters: list of Filters
        :param IsHistory: 是否导出全部授权详情
        :type IsHistory: bool
        :param Tags: 标签筛选,平台标签能力,这里传入 标签键,标签值作为一个对象
        :type Tags: list of Tags
        :param ExportMonth: 导出月份, 该参数仅在IsHistory 时可选.
        :type ExportMonth: str
        """
        self.Filters = None
        self.IsHistory = None
        self.Tags = None
        self.ExportMonth = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.IsHistory = params.get("IsHistory")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ExportMonth = params.get("ExportMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportLicenseDetailResponse(AbstractModel):
    """ExportLicenseDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 下载地址,该字段废弃
        :type DownloadUrl: str
        :param TaskId: 任务ID,可通过任务ID去查下载任务
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportMaliciousRequestsRequest(AbstractModel):
    """ExportMaliciousRequests请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportMaliciousRequestsResponse(AbstractModel):
    """ExportMaliciousRequests返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务Id , 可通过ExportTasks 接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportMalwaresRequest(AbstractModel):
    """ExportMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 限制条数,默认10
        :type Limit: int
        :param Offset: 偏移量 默认0
        :type Offset: int
        :param Filters: 过滤参数。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>FilePath - String - 是否必填：否 - 路径筛选</li>
<li>VirusName - String - 是否必填：否 - 描述筛选</li>
<li>CreateBeginTime - String - 是否必填：否 - 创建时间筛选-开始时间</li>
<li>CreateEndTime - String - 是否必填：否 - 创建时间筛选-结束时间</li>
<li>Status - String - 是否必填：否 - 状态筛选</li>
        :type Filters: list of Filters
        :param By: 排序值 CreateTime
        :type By: str
        :param Order: 排序 方式 ，ASC，DESC
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportMalwaresResponse(AbstractModel):
    """ExportMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportNonlocalLoginPlacesRequest(AbstractModel):
    """ExportNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: <li>Status - int - 是否必填：否 - 状态筛选1:正常登录；2：异地登录</li>
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
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
        


class ExportNonlocalLoginPlacesResponse(AbstractModel):
    """ExportNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportPrivilegeEventsRequest(AbstractModel):
    """ExportPrivilegeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportPrivilegeEventsResponse(AbstractModel):
    """ExportPrivilegeEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportProtectDirListRequest(AbstractModel):
    """ExportProtectDirList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: DirName 网站名称
DirPath 网站防护目录地址
        :type Filters: list of AssetFilters
        :param Order: asc：升序/desc：降序
        :type Order: str
        :param By: 排序字段
        :type By: str
        """
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportProtectDirListResponse(AbstractModel):
    """ExportProtectDirList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportReverseShellEventsRequest(AbstractModel):
    """ExportReverseShellEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportReverseShellEventsResponse(AbstractModel):
    """ExportReverseShellEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportScanTaskDetailsRequest(AbstractModel):
    """ExportScanTaskDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 本次检测的任务id（不同于出参的导出本次检测Excel的任务Id）
        :type TaskId: int
        :param ModuleType: 模块类型，当前提供：Malware 木马 , Vul 漏洞 , Baseline 基线
        :type ModuleType: str
        :param Filters: 过滤参数：ipOrAlias（服务器名/ip）
        :type Filters: list of Filters
        """
        self.TaskId = None
        self.ModuleType = None
        self.Filters = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ModuleType = params.get("ModuleType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportScanTaskDetailsResponse(AbstractModel):
    """ExportScanTaskDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 导出本次检测Excel的任务Id（不同于入参的本次检测任务id）
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportSecurityTrendsRequest(AbstractModel):
    """ExportSecurityTrends请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginDate: 开始时间。
        :type BeginDate: str
        :param EndDate: 结束时间。
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportSecurityTrendsResponse(AbstractModel):
    """ExportSecurityTrends返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportTasksRequest(AbstractModel):
    """ExportTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportTasksResponse(AbstractModel):
    """ExportTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: PENDING：正在生成下载链接，FINISHED：下载链接已生成，ERROR：网络异常等异常情况
        :type Status: str
        :param DownloadUrl: 下载链接
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportVulDetectionExcelRequest(AbstractModel):
    """ExportVulDetectionExcel请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 本次漏洞检测任务id（不同于出参的导出本次漏洞检测Excel的任务Id）
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVulDetectionExcelResponse(AbstractModel):
    """ExportVulDetectionExcel返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址
        :type DownloadUrl: str
        :param TaskId: 导出本次漏洞检测Excel的任务Id（不同于入参的本次漏洞检测任务id）
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportVulDetectionReportRequest(AbstractModel):
    """ExportVulDetectionReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 漏洞扫描任务id（不同于出参的导出检测报告的任务Id）
        :type TaskId: int
        :param Filters: 过滤参数
        :type Filters: list of Filters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.TaskId = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVulDetectionReportResponse(AbstractModel):
    """ExportVulDetectionReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出文件下载链接地址
        :type DownloadUrl: str
        :param TaskId: 导出检测报告的任务Id（不同于入参的漏洞扫描任务id）
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportVulEffectHostListRequest(AbstractModel):
    """ExportVulEffectHostList请求参数结构体

    """

    def __init__(self):
        r"""
        :param VulId: 漏洞id
        :type VulId: int
        :param Filters: 过滤条件。
<li>AliasName - String - 主机名筛选</li>
        :type Filters: list of Filter
        """
        self.VulId = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
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
        


class ExportVulEffectHostListResponse(AbstractModel):
    """ExportVulEffectHostList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param TaskId: 导出任务Id , 可通过ExportTasks 接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportVulListRequest(AbstractModel):
    """ExportVulList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件。
<li>VulCategory - int - 是否必填：否 - 漏洞分类筛选1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞</li>
<li>IfEmergency - String - 是否必填：否 - 是否为应急漏洞，查询应急漏洞传:yes</li>
<li>Status - String - 是否必填：是 - 漏洞状态筛选，0: 待处理 1:忽略  3:已修复  5:检测中， 控制台仅处理0,1,3,5四种状态</li>
<li>Level - String - 是否必填：否 - 漏洞等级筛选 1:低 2:中 3:高 4:提示</li>
<li>VulName- String - 是否必填：否 - 漏洞名称搜索</li>
        :type Filters: list of Filter
        :param IfDetail: 是否导出详情,1是 0不是
        :type IfDetail: int
        """
        self.Filters = None
        self.IfDetail = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.IfDetail = params.get("IfDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVulListResponse(AbstractModel):
    """ExportVulList返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 导出的文件下载url（已弃用！）
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param TaskId: 导出文件Id 可通过ExportTasks接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportWebPageEventListRequest(AbstractModel):
    """ExportWebPageEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>EventType - String - 是否必填：否 - 事件类型</li>
<li>EventStatus - String - 是否必填：否 - 事件状态</li>
        :type Filters: list of AssetFilters
        :param By: 排序方式：CreateTime 或 RestoreTime，默认为CreateTime
        :type By: str
        :param Order: 排序方式，0降序，1升序，默认为0
        :type Order: int
        """
        self.Filters = None
        self.By = None
        self.Order = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.By = params.get("By")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportWebPageEventListResponse(AbstractModel):
    """ExportWebPageEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id 可通过 ExportTasks接口下载
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    * 最多只能有5个Filter
    * 同一个Filter存在多个Values，Values值数量最多不能超过5个。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 模糊搜索
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否模糊匹配，前端框架会带上，可以不管
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistoryAccount(AbstractModel):
    """账号变更历史数据。

    """

    def __init__(self):
        r"""
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param Username: 帐号名。
        :type Username: str
        :param ModifyType: 帐号变更类型。
<li>CREATE：表示新增帐号</li>
<li>MODIFY：表示修改帐号</li>
<li>DELETE：表示删除帐号</li>
        :type ModifyType: str
        :param ModifyTime: 变更时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.ModifyType = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.ModifyType = params.get("ModifyType")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostLoginList(AbstractModel):
    """登录审计列表实体

    """

    def __init__(self):
        r"""
        :param Id: 记录Id
        :type Id: int
        :param Uuid: Uuid串
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param MachineIp: 主机ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineIp: str
        :param MachineName: 主机名
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineName: str
        :param UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param SrcIp: 来源ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcIp: str
        :param Status: 1:正常登录；2异地登录； 5已加白； 14：已处理；15：已忽略。
        :type Status: int
        :param Country: 国家id
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: int
        :param City: 城市id
注意：此字段可能返回 null，表示取不到有效值。
        :type City: int
        :param Province: 省份id
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: int
        :param LoginTime: 登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginTime: str
        :param ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param IsRiskArea: 是否命中异地登录异常  1表示命中此类异常, 0表示未命中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRiskArea: int
        :param IsRiskUser: 是否命中异常用户异常 1表示命中此类异常, 0表示未命中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRiskUser: int
        :param IsRiskTime: 是否命中异常时间异常 1表示命中此类异常, 0表示未命中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRiskTime: int
        :param IsRiskSrcIp: 是否命中异常IP异常 1表示命中此类异常, 0表示未命中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRiskSrcIp: int
        :param RiskLevel: 危险等级：
0 高危
1 可疑
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param Location: 位置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param Quuid: 主机quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.UserName = None
        self.SrcIp = None
        self.Status = None
        self.Country = None
        self.City = None
        self.Province = None
        self.LoginTime = None
        self.ModifyTime = None
        self.IsRiskArea = None
        self.IsRiskUser = None
        self.IsRiskTime = None
        self.IsRiskSrcIp = None
        self.RiskLevel = None
        self.Location = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.Status = params.get("Status")
        self.Country = params.get("Country")
        self.City = params.get("City")
        self.Province = params.get("Province")
        self.LoginTime = params.get("LoginTime")
        self.ModifyTime = params.get("ModifyTime")
        self.IsRiskArea = params.get("IsRiskArea")
        self.IsRiskUser = params.get("IsRiskUser")
        self.IsRiskTime = params.get("IsRiskTime")
        self.IsRiskSrcIp = params.get("IsRiskSrcIp")
        self.RiskLevel = params.get("RiskLevel")
        self.Location = params.get("Location")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreBaselineRule(AbstractModel):
    """忽略的基线检测项信息

    """

    def __init__(self):
        r"""
        :param RuleName: 基线检测项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param RuleId: 基线检测项id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: int
        :param ModifyTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param Fix: 修复建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Fix: str
        :param EffectHostCount: 影响主机数
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectHostCount: int
        """
        self.RuleName = None
        self.RuleId = None
        self.ModifyTime = None
        self.Fix = None
        self.EffectHostCount = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.RuleId = params.get("RuleId")
        self.ModifyTime = params.get("ModifyTime")
        self.Fix = params.get("Fix")
        self.EffectHostCount = params.get("EffectHostCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 漏洞ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IgnoreRuleEffectHostInfo(AbstractModel):
    """忽略检测项影响主机信息

    """

    def __init__(self):
        r"""
        :param HostName: 主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param Level: 危害等级：1-低位，2-中危，3-高危，4-严重
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param TagList: 主机标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TagList: list of str
        :param Status: 状态：0-未通过，1-忽略，3-已通过，5-检测中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param LastScanTime: 最后检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastScanTime: str
        :param EventId: 事件id
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: int
        :param Quuid: 主机quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        """
        self.HostName = None
        self.Level = None
        self.TagList = None
        self.Status = None
        self.LastScanTime = None
        self.EventId = None
        self.Quuid = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.Level = params.get("Level")
        self.TagList = params.get("TagList")
        self.Status = params.get("Status")
        self.LastScanTime = params.get("LastScanTime")
        self.EventId = params.get("EventId")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseBindDetail(AbstractModel):
    """授权绑定详情信息

    """

    def __init__(self):
        r"""
        :param MachineName: 机器别名
        :type MachineName: str
        :param MachineWanIp: 机器公网IP
        :type MachineWanIp: str
        :param MachineIp: 机器内网IP
        :type MachineIp: str
        :param Quuid: 云服务器UUID
        :type Quuid: str
        :param Uuid: 云镜客户端UUID
        :type Uuid: str
        :param Tags: 标签信息
        :type Tags: list of str
        :param AgentStatus: 云镜客户端状态,OFFLINE 离线,ONLINE 在线,UNINSTALL 未安装
        :type AgentStatus: str
        :param IsUnBind: 是否允许解绑,false 不允许解绑
        :type IsUnBind: bool
        :param IsSwitchBind: 是否允许换绑,false 不允许换绑
        :type IsSwitchBind: bool
        """
        self.MachineName = None
        self.MachineWanIp = None
        self.MachineIp = None
        self.Quuid = None
        self.Uuid = None
        self.Tags = None
        self.AgentStatus = None
        self.IsUnBind = None
        self.IsSwitchBind = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineIp = params.get("MachineIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.Tags = params.get("Tags")
        self.AgentStatus = params.get("AgentStatus")
        self.IsUnBind = params.get("IsUnBind")
        self.IsSwitchBind = params.get("IsSwitchBind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseBindTaskDetail(AbstractModel):
    """授权绑定任务详情

    """

    def __init__(self):
        r"""
        :param Quuid: 云服务器UUID
        :type Quuid: str
        :param ErrMsg: 错误信息
        :type ErrMsg: str
        :param Status: 0 执行中, 1 成功,2失败
        :type Status: int
        """
        self.Quuid = None
        self.ErrMsg = None
        self.Status = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.ErrMsg = params.get("ErrMsg")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseDetail(AbstractModel):
    """授权订单列表对象

    """

    def __init__(self):
        r"""
        :param LicenseId: 授权ID
        :type LicenseId: int
        :param LicenseType: 授权类型,0 专业版-按量计费, 1专业版-包年包月 , 2 旗舰版-包年包月
        :type LicenseType: int
        :param LicenseStatus: 授权状态 0 未使用,1 部分使用, 2 已用完, 3 不可用
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseStatus: int
        :param LicenseCnt: 总授权数
        :type LicenseCnt: int
        :param UsedLicenseCnt: 已使用授权数
        :type UsedLicenseCnt: int
        :param OrderStatus: 订单状态 1 正常 2隔离, 3销毁
        :type OrderStatus: int
        :param Deadline: 截止日期
        :type Deadline: str
        :param ResourceId: 订单资源ID
        :type ResourceId: str
        :param AutoRenewFlag: 0 初始化,1 自动续费,2 不自动续费
        :type AutoRenewFlag: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param TaskId: 任务ID ,默认0 ,查询绑定进度用
        :type TaskId: int
        :param BuyTime: 购买时间
        :type BuyTime: str
        :param SourceType: 是否试用订单.
        :type SourceType: int
        :param Alias: 资源别名
        :type Alias: str
        :param Tags: 平台标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        """
        self.LicenseId = None
        self.LicenseType = None
        self.LicenseStatus = None
        self.LicenseCnt = None
        self.UsedLicenseCnt = None
        self.OrderStatus = None
        self.Deadline = None
        self.ResourceId = None
        self.AutoRenewFlag = None
        self.ProjectId = None
        self.TaskId = None
        self.BuyTime = None
        self.SourceType = None
        self.Alias = None
        self.Tags = None


    def _deserialize(self, params):
        self.LicenseId = params.get("LicenseId")
        self.LicenseType = params.get("LicenseType")
        self.LicenseStatus = params.get("LicenseStatus")
        self.LicenseCnt = params.get("LicenseCnt")
        self.UsedLicenseCnt = params.get("UsedLicenseCnt")
        self.OrderStatus = params.get("OrderStatus")
        self.Deadline = params.get("Deadline")
        self.ResourceId = params.get("ResourceId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ProjectId = params.get("ProjectId")
        self.TaskId = params.get("TaskId")
        self.BuyTime = params.get("BuyTime")
        self.SourceType = params.get("SourceType")
        self.Alias = params.get("Alias")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseOrder(AbstractModel):
    """授权订单对象内容

    """

    def __init__(self):
        r"""
        :param LicenseId: 授权ID
        :type LicenseId: int
        :param LicenseType: 授权类型
        :type LicenseType: int
        :param Status: 授权订单资源状态
        :type Status: int
        :param SourceType: 订单类型
        :type SourceType: int
        :param ResourceId: 资源ID
        :type ResourceId: str
        """
        self.LicenseId = None
        self.LicenseType = None
        self.Status = None
        self.SourceType = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.LicenseId = params.get("LicenseId")
        self.LicenseType = params.get("LicenseType")
        self.Status = params.get("Status")
        self.SourceType = params.get("SourceType")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseUnBindRsp(AbstractModel):
    """授权解绑信息

    """

    def __init__(self):
        r"""
        :param Quuid: QUUID 云服务器uuid,轻量服务器uuid,边缘计算 uuid
        :type Quuid: str
        :param ErrMsg: 失败原因
        :type ErrMsg: str
        """
        self.Quuid = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginWhiteCombinedInfo(AbstractModel):
    """异地登录合并后白名单

    """

    def __init__(self):
        r"""
        :param Places: 白名单地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Places: list of Place
        :param UserName: 白名单用户（多个用户逗号隔开）
        :type UserName: str
        :param SrcIp: 白名单IP（多个IP逗号隔开）
        :type SrcIp: str
        :param Locale: 地域字符串
        :type Locale: str
        :param Remark: 备注
        :type Remark: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param IsGlobal: 是否对全局生效, 1：全局有效 0: 对指定主机列表生效'
        :type IsGlobal: int
        :param Name: 白名单名字：IsLocal=1时固定为：全部服务器；单台机器时为机器内网IP，多台服务器时为服务器数量，如：11台
        :type Name: str
        :param Desc: 仅在单台服务器时，返回服务器名称
        :type Desc: str
        :param Id: 白名单ID
        :type Id: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 最近修改时间
        :type ModifyTime: str
        :param Uuid: 服务器Uuid
        :type Uuid: str
        """
        self.Places = None
        self.UserName = None
        self.SrcIp = None
        self.Locale = None
        self.Remark = None
        self.StartTime = None
        self.EndTime = None
        self.IsGlobal = None
        self.Name = None
        self.Desc = None
        self.Id = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Uuid = None


    def _deserialize(self, params):
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.Locale = params.get("Locale")
        self.Remark = params.get("Remark")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsGlobal = params.get("IsGlobal")
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Id = params.get("Id")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginWhiteLists(AbstractModel):
    """异地登录白名单

    """

    def __init__(self):
        r"""
        :param Id: 记录ID
        :type Id: int
        :param Uuid: 云镜客户端ID
        :type Uuid: str
        :param Places: 白名单地域
        :type Places: list of Place
        :param UserName: 白名单用户（多个用户逗号隔开）
        :type UserName: str
        :param SrcIp: 白名单IP（多个IP逗号隔开）
        :type SrcIp: str
        :param IsGlobal: 是否为全局规则
        :type IsGlobal: bool
        :param CreateTime: 创建白名单时间
        :type CreateTime: str
        :param ModifyTime: 修改白名单时间
        :type ModifyTime: str
        :param MachineName: 机器名
        :type MachineName: str
        :param HostIp: 机器IP
        :type HostIp: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Id = None
        self.Uuid = None
        self.Places = None
        self.UserName = None
        self.SrcIp = None
        self.IsGlobal = None
        self.CreateTime = None
        self.ModifyTime = None
        self.MachineName = None
        self.HostIp = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.IsGlobal = params.get("IsGlobal")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.MachineName = params.get("MachineName")
        self.HostIp = params.get("HostIp")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Machine(AbstractModel):
    """主机列表

    """

    def __init__(self):
        r"""
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineOs: 主机系统。
        :type MachineOs: str
        :param MachineStatus: 主机状态。
<li>OFFLINE: 离线  </li>
<li>ONLINE: 在线</li>
<li>SHUTDOWN: 已关机</li>
<li>UNINSTALLED: 未防护</li>
        :type MachineStatus: str
        :param Uuid: 云镜客户端唯一Uuid，若客户端长时间不在线将返回空字符。
        :type Uuid: str
        :param Quuid: CVM或BM机器唯一Uuid。
        :type Quuid: str
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param IsProVersion: 是否是专业版。
<li>true： 是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param MalwareNum: 木马数。
        :type MalwareNum: int
        :param Tag: 标签信息
        :type Tag: list of MachineTag
        :param BaselineNum: 基线风险数。
        :type BaselineNum: int
        :param CyberAttackNum: 网络风险数。
        :type CyberAttackNum: int
        :param SecurityStatus: 风险状态。
<li>SAFE：安全</li>
<li>RISK：风险</li>
<li>UNKNOWN：未知</li>
        :type SecurityStatus: str
        :param InvasionNum: 入侵事件数
        :type InvasionNum: int
        :param RegionInfo: 地域信息
        :type RegionInfo: :class:`tencentcloud.cwp.v20180228.models.RegionInfo`
        :param InstanceState: 实例状态 TERMINATED_PRO_VERSION 已销毁
        :type InstanceState: str
        :param LicenseStatus: 防篡改 授权状态 1 授权 0 未授权
        :type LicenseStatus: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param HasAssetScan: 是否有资产扫描接口，0无，1有
        :type HasAssetScan: int
        :param MachineType: 机器所属专区类型 CVM 云服务器, BM 黑石, ECM 边缘计算, LH 轻量应用服务器 ,Other 混合云专区
        :type MachineType: str
        :param KernelVersion: 内核版本
        :type KernelVersion: str
        :param ProtectType: 防护版本：BASIC_VERSION 基础版， PRO_VERSION 专业版，Flagship 旗舰版，GENERAL_DISCOUNT 普惠版
        :type ProtectType: str
        :param CloudTags: 云标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudTags: list of Tags
        :param IsAddedOnTheFifteen: 是否15天内新增的主机 0：非15天内新增的主机，1：15天内增加的主机
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAddedOnTheFifteen: int
        """
        self.MachineName = None
        self.MachineOs = None
        self.MachineStatus = None
        self.Uuid = None
        self.Quuid = None
        self.VulNum = None
        self.MachineIp = None
        self.IsProVersion = None
        self.MachineWanIp = None
        self.PayMode = None
        self.MalwareNum = None
        self.Tag = None
        self.BaselineNum = None
        self.CyberAttackNum = None
        self.SecurityStatus = None
        self.InvasionNum = None
        self.RegionInfo = None
        self.InstanceState = None
        self.LicenseStatus = None
        self.ProjectId = None
        self.HasAssetScan = None
        self.MachineType = None
        self.KernelVersion = None
        self.ProtectType = None
        self.CloudTags = None
        self.IsAddedOnTheFifteen = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachineOs = params.get("MachineOs")
        self.MachineStatus = params.get("MachineStatus")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.VulNum = params.get("VulNum")
        self.MachineIp = params.get("MachineIp")
        self.IsProVersion = params.get("IsProVersion")
        self.MachineWanIp = params.get("MachineWanIp")
        self.PayMode = params.get("PayMode")
        self.MalwareNum = params.get("MalwareNum")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.BaselineNum = params.get("BaselineNum")
        self.CyberAttackNum = params.get("CyberAttackNum")
        self.SecurityStatus = params.get("SecurityStatus")
        self.InvasionNum = params.get("InvasionNum")
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        self.InstanceState = params.get("InstanceState")
        self.LicenseStatus = params.get("LicenseStatus")
        self.ProjectId = params.get("ProjectId")
        self.HasAssetScan = params.get("HasAssetScan")
        self.MachineType = params.get("MachineType")
        self.KernelVersion = params.get("KernelVersion")
        self.ProtectType = params.get("ProtectType")
        if params.get("CloudTags") is not None:
            self.CloudTags = []
            for item in params.get("CloudTags"):
                obj = Tags()
                obj._deserialize(item)
                self.CloudTags.append(obj)
        self.IsAddedOnTheFifteen = params.get("IsAddedOnTheFifteen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineTag(AbstractModel):
    """服务器标签信息

    """

    def __init__(self):
        r"""
        :param Rid: 关联标签ID
        :type Rid: int
        :param Name: 标签名
        :type Name: str
        :param TagId: 标签ID
        :type TagId: int
        """
        self.Rid = None
        self.Name = None
        self.TagId = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        self.Name = params.get("Name")
        self.TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MalWareList(AbstractModel):
    """木马列表集合

    """

    def __init__(self):
        r"""
        :param HostIp: 服务器ip
        :type HostIp: str
        :param Uuid: 唯一UUID
        :type Uuid: str
        :param FilePath: 路径
        :type FilePath: str
        :param VirusName: 描述
        :type VirusName: str
        :param Status: 状态；4-:待处理，5-已信任，6-已隔离，8-文件已删除
        :type Status: int
        :param Id: 唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Alias: 主机别名
        :type Alias: str
        :param Tags: 特性标签，已废弃字段，不会再返回标签，详情中才会返回标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param FileCreateTime: 首次运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FileCreateTime: str
        :param FileModifierTime: 最近运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FileModifierTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param LatestScanTime: 最近扫描时间
        :type LatestScanTime: str
        :param Level: 风险等级 0未知、1低、2中、3高、4严重
        :type Level: int
        :param CheckPlatform: '木马检测平台用,分割 1云查杀引擎、2TAV、3binaryAi、4异常行为、5威胁情报
        :type CheckPlatform: str
        :param ProcessExists: 木马进程是否存在 0:不存在，1:存在
        :type ProcessExists: int
        :param FileExists: 木马文件是否存在 0:不存在，1:存在
        :type FileExists: int
        :param Quuid: cvm quuid
        :type Quuid: str
        :param MD5: 木马样本md5
        :type MD5: str
        """
        self.HostIp = None
        self.Uuid = None
        self.FilePath = None
        self.VirusName = None
        self.Status = None
        self.Id = None
        self.Alias = None
        self.Tags = None
        self.FileCreateTime = None
        self.FileModifierTime = None
        self.CreateTime = None
        self.LatestScanTime = None
        self.Level = None
        self.CheckPlatform = None
        self.ProcessExists = None
        self.FileExists = None
        self.Quuid = None
        self.MD5 = None


    def _deserialize(self, params):
        self.HostIp = params.get("HostIp")
        self.Uuid = params.get("Uuid")
        self.FilePath = params.get("FilePath")
        self.VirusName = params.get("VirusName")
        self.Status = params.get("Status")
        self.Id = params.get("Id")
        self.Alias = params.get("Alias")
        self.Tags = params.get("Tags")
        self.FileCreateTime = params.get("FileCreateTime")
        self.FileModifierTime = params.get("FileModifierTime")
        self.CreateTime = params.get("CreateTime")
        self.LatestScanTime = params.get("LatestScanTime")
        self.Level = params.get("Level")
        self.CheckPlatform = params.get("CheckPlatform")
        self.ProcessExists = params.get("ProcessExists")
        self.FileExists = params.get("FileExists")
        self.Quuid = params.get("Quuid")
        self.MD5 = params.get("MD5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaliciousRequestWhiteListInfo(AbstractModel):
    """恶意请求白名单列表信息

    """

    def __init__(self):
        r"""
        :param Id: 白名单id
        :type Id: int
        :param Domain: 域名
        :type Domain: str
        :param Mark: 备注
        :type Mark: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 更新时间
        :type ModifyTime: str
        """
        self.Id = None
        self.Domain = None
        self.Mark = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Mark = params.get("Mark")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MalwareInfo(AbstractModel):
    """恶意文件详情

    """

    def __init__(self):
        r"""
        :param VirusName: 病毒名称
        :type VirusName: str
        :param FileSize: 文件大小
        :type FileSize: int
        :param MD5: 文件MD5
        :type MD5: str
        :param FilePath: 文件地址
        :type FilePath: str
        :param FileCreateTime: 首次运行时间
        :type FileCreateTime: str
        :param FileModifierTime: 最近一次运行时间
        :type FileModifierTime: str
        :param HarmDescribe: 危害描述
        :type HarmDescribe: str
        :param SuggestScheme: 建议方案
        :type SuggestScheme: str
        :param ServersName: 服务器名称
        :type ServersName: str
        :param HostIp: 服务器IP
        :type HostIp: str
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ProcessID: 进程ID
        :type ProcessID: str
        :param Tags: 标签特性
        :type Tags: list of str
        :param Breadth: 影响广度 // 暂时不提供
注意：此字段可能返回 null，表示取不到有效值。
        :type Breadth: str
        :param Heat: 查询热度 // 暂时不提供
注意：此字段可能返回 null，表示取不到有效值。
        :type Heat: str
        :param Id: 唯一ID
        :type Id: int
        :param FileName: 文件名称
        :type FileName: str
        :param CreateTime: 首次发现时间
        :type CreateTime: str
        :param LatestScanTime: 最近扫描时间
        :type LatestScanTime: str
        :param Reference: 参考链接
        :type Reference: str
        :param MachineWanIp: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineWanIp: str
        :param PsTree: 进程树 json  pid:进程id，exe:文件路径 ，account:进程所属用组和用户 ,cmdline:执行命令，ssh_service: SSH服务ip, ssh_soure:登录源
注意：此字段可能返回 null，表示取不到有效值。
        :type PsTree: str
        :param MachineStatus: 主机在线状态 OFFLINE  ONLINE
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineStatus: str
        :param Status: 状态；4-:待处理，5-已信任，6-已隔离
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Level: 风险等级 0提示、1低、2中、3高、4严重
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param CheckPlatform: 木马检测平台用,分割 1云查杀引擎、2TAV、3binaryAi、4异常行为、5威胁情报
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPlatform: str
        :param Uuid: 主机uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param ModifyTime: 最近修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param StrFileAccessTime: 最近访问时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StrFileAccessTime: str
        """
        self.VirusName = None
        self.FileSize = None
        self.MD5 = None
        self.FilePath = None
        self.FileCreateTime = None
        self.FileModifierTime = None
        self.HarmDescribe = None
        self.SuggestScheme = None
        self.ServersName = None
        self.HostIp = None
        self.ProcessName = None
        self.ProcessID = None
        self.Tags = None
        self.Breadth = None
        self.Heat = None
        self.Id = None
        self.FileName = None
        self.CreateTime = None
        self.LatestScanTime = None
        self.Reference = None
        self.MachineWanIp = None
        self.PsTree = None
        self.MachineStatus = None
        self.Status = None
        self.Level = None
        self.CheckPlatform = None
        self.Uuid = None
        self.ModifyTime = None
        self.StrFileAccessTime = None


    def _deserialize(self, params):
        self.VirusName = params.get("VirusName")
        self.FileSize = params.get("FileSize")
        self.MD5 = params.get("MD5")
        self.FilePath = params.get("FilePath")
        self.FileCreateTime = params.get("FileCreateTime")
        self.FileModifierTime = params.get("FileModifierTime")
        self.HarmDescribe = params.get("HarmDescribe")
        self.SuggestScheme = params.get("SuggestScheme")
        self.ServersName = params.get("ServersName")
        self.HostIp = params.get("HostIp")
        self.ProcessName = params.get("ProcessName")
        self.ProcessID = params.get("ProcessID")
        self.Tags = params.get("Tags")
        self.Breadth = params.get("Breadth")
        self.Heat = params.get("Heat")
        self.Id = params.get("Id")
        self.FileName = params.get("FileName")
        self.CreateTime = params.get("CreateTime")
        self.LatestScanTime = params.get("LatestScanTime")
        self.Reference = params.get("Reference")
        self.MachineWanIp = params.get("MachineWanIp")
        self.PsTree = params.get("PsTree")
        self.MachineStatus = params.get("MachineStatus")
        self.Status = params.get("Status")
        self.Level = params.get("Level")
        self.CheckPlatform = params.get("CheckPlatform")
        self.Uuid = params.get("Uuid")
        self.ModifyTime = params.get("ModifyTime")
        self.StrFileAccessTime = params.get("StrFileAccessTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MalwareRisk(AbstractModel):
    """恶意文件风险提示列表信息

    """

    def __init__(self):
        r"""
        :param MachineIp: 机器IP
        :type MachineIp: str
        :param VirusName: 病毒名
        :type VirusName: str
        :param CreateTime: 发现时间
        :type CreateTime: str
        :param Id: 唯一ID
        :type Id: int
        """
        self.MachineIp = None
        self.VirusName = None
        self.CreateTime = None
        self.Id = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.VirusName = params.get("VirusName")
        self.CreateTime = params.get("CreateTime")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 设置自动开通状态。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBanModeRequest(AbstractModel):
    """ModifyBanMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Mode: 阻断模式，STANDARD_MODE：标准阻断，DEEP_MODE：深度阻断
        :type Mode: str
        :param Ttl: 阻断时间，用于标准阻断模式
        :type Ttl: int
        """
        self.Mode = None
        self.Ttl = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Ttl = params.get("Ttl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBanModeResponse(AbstractModel):
    """ModifyBanMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBanStatusRequest(AbstractModel):
    """ModifyBanStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 阻断状态 0:关闭 1:开启
        :type Status: int
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBanStatusResponse(AbstractModel):
    """ModifyBanStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBruteAttackRulesRequest(AbstractModel):
    """ModifyBruteAttackRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Rules: 暴力破解判断规则
        :type Rules: list of BruteAttackRule
        """
        self.Rules = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = BruteAttackRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBruteAttackRulesResponse(AbstractModel):
    """ModifyBruteAttackRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLicenseBindsRequest(AbstractModel):
    """ModifyLicenseBinds请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param LicenseType: 授权类型
        :type LicenseType: int
        :param IsAll: 是否全部机器(当全部机器数大于当前订单可用授权数时,多余机器会被跳过)
        :type IsAll: bool
        :param QuuidList: 需要绑定的机器quuid列表, 当IsAll = false 时必填,反之忽略该参数. 最大长度=2000
        :type QuuidList: list of str
        """
        self.ResourceId = None
        self.LicenseType = None
        self.IsAll = None
        self.QuuidList = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.LicenseType = params.get("LicenseType")
        self.IsAll = params.get("IsAll")
        self.QuuidList = params.get("QuuidList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLicenseBindsResponse(AbstractModel):
    """ModifyLicenseBinds返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyLicenseUnBindsRequest(AbstractModel):
    """ModifyLicenseUnBinds请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param LicenseType: 授权类型
        :type LicenseType: int
        :param IsAll: 是否全部机器(当全部机器数大于当前订单可用授权数时,多余机器会被跳过)
        :type IsAll: bool
        :param QuuidList: 需要绑定的机器quuid列表, 当IsAll = false 时必填,反之忽略该参数.
最大长度=100
        :type QuuidList: list of str
        """
        self.ResourceId = None
        self.LicenseType = None
        self.IsAll = None
        self.QuuidList = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.LicenseType = params.get("LicenseType")
        self.IsAll = params.get("IsAll")
        self.QuuidList = params.get("QuuidList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLicenseUnBindsResponse(AbstractModel):
    """ModifyLicenseUnBinds返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMsg: 只有解绑失败的才有该值.
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: list of LicenseUnBindRsp
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ErrMsg") is not None:
            self.ErrMsg = []
            for item in params.get("ErrMsg"):
                obj = LicenseUnBindRsp()
                obj._deserialize(item)
                self.ErrMsg.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyMalwareTimingScanSettingsRequest(AbstractModel):
    """ModifyMalwareTimingScanSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param CheckPattern: 检测模式 0 全盘检测  1快速检测
        :type CheckPattern: int
        :param StartTime: 检测周期 开始时间，如：02:00:00
        :type StartTime: str
        :param EndTime: 检测周期 超时结束时间，如：04:00:00
        :type EndTime: str
        :param IsGlobal: 是否全部服务器 1 全部 2 自选
        :type IsGlobal: int
        :param EnableScan: 定时检测开关 0 关闭 1开启
        :type EnableScan: int
        :param MonitoringPattern: 监控模式 0 标准 1深度
        :type MonitoringPattern: int
        :param Cycle: 扫描周期 默认每天 1
        :type Cycle: int
        :param RealTimeMonitoring: 实时监控 0 关闭 1开启
        :type RealTimeMonitoring: int
        :param QuuidList: 自选服务器时必须 主机quuid的string数组
        :type QuuidList: list of str
        :param AutoIsolation: 是否自动隔离 1隔离 0 不隔离
        :type AutoIsolation: int
        :param KillProcess: 是否杀掉进程 1杀掉 0不杀掉
        :type KillProcess: int
        :param EngineType: 1标准模式（只报严重、高危）、2增强模式（报严重、高危、中危）、3严格模式（报严重、高、中、低、提示）
        :type EngineType: int
        """
        self.CheckPattern = None
        self.StartTime = None
        self.EndTime = None
        self.IsGlobal = None
        self.EnableScan = None
        self.MonitoringPattern = None
        self.Cycle = None
        self.RealTimeMonitoring = None
        self.QuuidList = None
        self.AutoIsolation = None
        self.KillProcess = None
        self.EngineType = None


    def _deserialize(self, params):
        self.CheckPattern = params.get("CheckPattern")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsGlobal = params.get("IsGlobal")
        self.EnableScan = params.get("EnableScan")
        self.MonitoringPattern = params.get("MonitoringPattern")
        self.Cycle = params.get("Cycle")
        self.RealTimeMonitoring = params.get("RealTimeMonitoring")
        self.QuuidList = params.get("QuuidList")
        self.AutoIsolation = params.get("AutoIsolation")
        self.KillProcess = params.get("KillProcess")
        self.EngineType = params.get("EngineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMalwareTimingScanSettingsResponse(AbstractModel):
    """ModifyMalwareTimingScanSettings返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyOrderAttributeRequest(AbstractModel):
    """ModifyOrderAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param LicenseType: 授权类型 0 专业版-按量计费, 1专业版-包年包月 , 2 旗舰版-包年包月
        :type LicenseType: int
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param AttrName: 可编辑的属性名称 ,当前支持的有: alias 资源别名
        :type AttrName: str
        :param AttrValue: 属性值
        :type AttrValue: str
        """
        self.LicenseType = None
        self.ResourceId = None
        self.AttrName = None
        self.AttrValue = None


    def _deserialize(self, params):
        self.LicenseType = params.get("LicenseType")
        self.ResourceId = params.get("ResourceId")
        self.AttrName = params.get("AttrName")
        self.AttrValue = params.get("AttrValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOrderAttributeResponse(AbstractModel):
    """ModifyOrderAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWarningSettingRequest(AbstractModel):
    """ModifyWarningSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param WarningObjects: 告警设置的修改内容
        :type WarningObjects: list of WarningObject
        """
        self.WarningObjects = None


    def _deserialize(self, params):
        if params.get("WarningObjects") is not None:
            self.WarningObjects = []
            for item in params.get("WarningObjects"):
                obj = WarningObject()
                obj._deserialize(item)
                self.WarningObjects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWarningSettingResponse(AbstractModel):
    """ModifyWarningSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebPageProtectDirRequest(AbstractModel):
    """ModifyWebPageProtectDir请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProtectDirAddr: 网站防护目录地址
        :type ProtectDirAddr: str
        :param ProtectDirName: 网站防护目录名称
        :type ProtectDirName: str
        :param ProtectFileType: 防护文件类型,分号分割 ;
        :type ProtectFileType: str
        :param HostConfig: 防护机器列表信息
        :type HostConfig: list of ProtectHostConfig
        """
        self.ProtectDirAddr = None
        self.ProtectDirName = None
        self.ProtectFileType = None
        self.HostConfig = None


    def _deserialize(self, params):
        self.ProtectDirAddr = params.get("ProtectDirAddr")
        self.ProtectDirName = params.get("ProtectDirName")
        self.ProtectFileType = params.get("ProtectFileType")
        if params.get("HostConfig") is not None:
            self.HostConfig = []
            for item in params.get("HostConfig"):
                obj = ProtectHostConfig()
                obj._deserialize(item)
                self.HostConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebPageProtectDirResponse(AbstractModel):
    """ModifyWebPageProtectDir返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebPageProtectSettingRequest(AbstractModel):
    """ModifyWebPageProtectSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModifyType: 需要操作的类型1 目录名称 2 防护文件类型
        :type ModifyType: int
        :param Value: 提交值
        :type Value: str
        :param Id: 配置对应的protect_path
        :type Id: str
        """
        self.ModifyType = None
        self.Value = None
        self.Id = None


    def _deserialize(self, params):
        self.ModifyType = params.get("ModifyType")
        self.Value = params.get("Value")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebPageProtectSettingResponse(AbstractModel):
    """ModifyWebPageProtectSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebPageProtectSwitchRequest(AbstractModel):
    """ModifyWebPageProtectSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param SwitchType: 开关类型 1 防护开关  2 自动恢复开关 3 移除防护目录
        :type SwitchType: int
        :param Ids: 需要操作开关的网站 最大100条
        :type Ids: list of str
        :param Status: 1 开启 0 关闭 SwitchType 为 1 | 2 必填;
        :type Status: int
        """
        self.SwitchType = None
        self.Ids = None
        self.Status = None


    def _deserialize(self, params):
        self.SwitchType = params.get("SwitchType")
        self.Ids = params.get("Ids")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebPageProtectSwitchResponse(AbstractModel):
    """ModifyWebPageProtectSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonthInspectionReport(AbstractModel):
    """专家服务-月巡检报告

    """

    def __init__(self):
        r"""
        :param ReportName: 巡检报告名称
        :type ReportName: str
        :param ReportPath: 巡检报告下载地址
        :type ReportPath: str
        :param ModifyTime: 巡检报告更新时间
        :type ModifyTime: str
        """
        self.ReportName = None
        self.ReportPath = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.ReportName = params.get("ReportName")
        self.ReportPath = params.get("ReportPath")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenPortStatistics(AbstractModel):
    """端口统计列表

    """

    def __init__(self):
        r"""
        :param Port: 端口号
        :type Port: int
        :param MachineNum: 主机数量
        :type MachineNum: int
        """
        self.Port = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsName(AbstractModel):
    """操作系统名称

    """

    def __init__(self):
        r"""
        :param Name: 系统名称
        :type Name: str
        :param MachineOSType: 操作系统类型枚举值
        :type MachineOSType: int
        """
        self.Name = None
        self.MachineOSType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MachineOSType = params.get("MachineOSType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Place(AbstractModel):
    """登录地信息

    """

    def __init__(self):
        r"""
        :param CityId: 城市 ID。
        :type CityId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CountryId: 国家ID，暂只支持国内：1。
        :type CountryId: int
        :param Location: 位置名称
        :type Location: str
        """
        self.CityId = None
        self.ProvinceId = None
        self.CountryId = None
        self.Location = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.ProvinceId = params.get("ProvinceId")
        self.CountryId = params.get("CountryId")
        self.Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivilegeEscalationProcess(AbstractModel):
    """本地提权数据

    """

    def __init__(self):
        r"""
        :param Id: 数据ID
        :type Id: int
        :param Uuid: 云镜ID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param FullPath: 进程路径
        :type FullPath: str
        :param CmdLine: 执行命令
        :type CmdLine: str
        :param UserName: 用户名
        :type UserName: str
        :param UserGroup: 用户组
        :type UserGroup: str
        :param ProcFilePrivilege: 进程文件权限
        :type ProcFilePrivilege: str
        :param ParentProcName: 父进程名
        :type ParentProcName: str
        :param ParentProcUser: 父进程用户名
        :type ParentProcUser: str
        :param ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param ProcTree: 进程树
        :type ProcTree: str
        :param Status: 处理状态：0-待处理 2-白名单 3-已处理 4-已忽略
        :type Status: int
        :param CreateTime: 发生时间
        :type CreateTime: str
        :param MachineName: 机器名
        :type MachineName: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.ProcessName = None
        self.FullPath = None
        self.CmdLine = None
        self.UserName = None
        self.UserGroup = None
        self.ProcFilePrivilege = None
        self.ParentProcName = None
        self.ParentProcUser = None
        self.ParentProcGroup = None
        self.ParentProcPath = None
        self.ProcTree = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.ProcessName = params.get("ProcessName")
        self.FullPath = params.get("FullPath")
        self.CmdLine = params.get("CmdLine")
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.ProcFilePrivilege = params.get("ProcFilePrivilege")
        self.ParentProcName = params.get("ParentProcName")
        self.ParentProcUser = params.get("ParentProcUser")
        self.ParentProcGroup = params.get("ParentProcGroup")
        self.ParentProcPath = params.get("ParentProcPath")
        self.ProcTree = params.get("ProcTree")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivilegeRule(AbstractModel):
    """本地提权规则

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param SMode: 是否S权限
        :type SMode: int
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态(0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        """
        self.Id = None
        self.Uuid = None
        self.ProcessName = None
        self.SMode = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.SMode = params.get("SMode")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStatistics(AbstractModel):
    """进程数据统计数据。

    """

    def __init__(self):
        r"""
        :param ProcessName: 进程名。
        :type ProcessName: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.ProcessName = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectDirInfo(AbstractModel):
    """防护目录列表集

    """

    def __init__(self):
        r"""
        :param DirName: 网站名称
        :type DirName: str
        :param DirPath: 网站防护目录地址
        :type DirPath: str
        :param RelatedServerNum: 关联服务器数
        :type RelatedServerNum: int
        :param ProtectServerNum: 防护服务器数
        :type ProtectServerNum: int
        :param NoProtectServerNum: 未防护服务器数
        :type NoProtectServerNum: int
        :param Id: 唯一ID
        :type Id: str
        :param ProtectStatus: 防护状态
        :type ProtectStatus: int
        :param ProtectException: 防护异常
        :type ProtectException: int
        :param AutoRestoreSwitchStatus: 自动恢复开关 (Filters 过滤Quuid 时 返回) 默认0
        :type AutoRestoreSwitchStatus: int
        """
        self.DirName = None
        self.DirPath = None
        self.RelatedServerNum = None
        self.ProtectServerNum = None
        self.NoProtectServerNum = None
        self.Id = None
        self.ProtectStatus = None
        self.ProtectException = None
        self.AutoRestoreSwitchStatus = None


    def _deserialize(self, params):
        self.DirName = params.get("DirName")
        self.DirPath = params.get("DirPath")
        self.RelatedServerNum = params.get("RelatedServerNum")
        self.ProtectServerNum = params.get("ProtectServerNum")
        self.NoProtectServerNum = params.get("NoProtectServerNum")
        self.Id = params.get("Id")
        self.ProtectStatus = params.get("ProtectStatus")
        self.ProtectException = params.get("ProtectException")
        self.AutoRestoreSwitchStatus = params.get("AutoRestoreSwitchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectDirRelatedServer(AbstractModel):
    """防护目录关联服务器列表信息

    """

    def __init__(self):
        r"""
        :param Id: 唯一ID
        :type Id: str
        :param HostName: 服务器名称
        :type HostName: str
        :param HostIp: 服务器IP
        :type HostIp: str
        :param MachineOs: 服务器系统
        :type MachineOs: str
        :param RelateDirNum: 关联目录数
        :type RelateDirNum: int
        :param ProtectStatus: 防护状态
        :type ProtectStatus: int
        :param ProtectSwitch: 防护开关
        :type ProtectSwitch: int
        :param AutoRestoreSwitchStatus: 自动恢复开关
        :type AutoRestoreSwitchStatus: int
        :param Quuid: 服务器唯一ID
        :type Quuid: str
        :param Authorization: 是否已经授权
        :type Authorization: bool
        :param Exception: 异常状态
        :type Exception: int
        :param Progress: 过渡进度
        :type Progress: int
        :param ExceptionMessage: 异常信息
        :type ExceptionMessage: str
        """
        self.Id = None
        self.HostName = None
        self.HostIp = None
        self.MachineOs = None
        self.RelateDirNum = None
        self.ProtectStatus = None
        self.ProtectSwitch = None
        self.AutoRestoreSwitchStatus = None
        self.Quuid = None
        self.Authorization = None
        self.Exception = None
        self.Progress = None
        self.ExceptionMessage = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.HostName = params.get("HostName")
        self.HostIp = params.get("HostIp")
        self.MachineOs = params.get("MachineOs")
        self.RelateDirNum = params.get("RelateDirNum")
        self.ProtectStatus = params.get("ProtectStatus")
        self.ProtectSwitch = params.get("ProtectSwitch")
        self.AutoRestoreSwitchStatus = params.get("AutoRestoreSwitchStatus")
        self.Quuid = params.get("Quuid")
        self.Authorization = params.get("Authorization")
        self.Exception = params.get("Exception")
        self.Progress = params.get("Progress")
        self.ExceptionMessage = params.get("ExceptionMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectEventLists(AbstractModel):
    """防护事件列表信息

    """

    def __init__(self):
        r"""
        :param HostName: 服务器名称
        :type HostName: str
        :param HostIp: 服务器ip
        :type HostIp: str
        :param EventDir: 事件地址
        :type EventDir: str
        :param EventType: 事件类型 0-内容被修改恢复；1-权限被修改恢复；2-归属被修改恢复；3-被删除恢复；4-新增删除
        :type EventType: int
        :param EventStatus: 事件状态 1 已恢复 0 未恢复
        :type EventStatus: int
        :param CreateTime: 发现时间
        :type CreateTime: str
        :param RestoreTime: 恢复时间
        :type RestoreTime: str
        :param Id: 唯一ID
        :type Id: int
        :param FileType: 文件类型 0-常规文件；1-目录；2-软链
        :type FileType: int
        """
        self.HostName = None
        self.HostIp = None
        self.EventDir = None
        self.EventType = None
        self.EventStatus = None
        self.CreateTime = None
        self.RestoreTime = None
        self.Id = None
        self.FileType = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.HostIp = params.get("HostIp")
        self.EventDir = params.get("EventDir")
        self.EventType = params.get("EventType")
        self.EventStatus = params.get("EventStatus")
        self.CreateTime = params.get("CreateTime")
        self.RestoreTime = params.get("RestoreTime")
        self.Id = params.get("Id")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectHostConfig(AbstractModel):
    """防护机器信息

    """

    def __init__(self):
        r"""
        :param Quuid: 机器唯一ID
        :type Quuid: str
        :param ProtectSwitch: 防护开关 0  关闭 1开启
        :type ProtectSwitch: int
        :param AutoRecovery: 自动恢复开关 0 关闭 1开启
        :type AutoRecovery: int
        """
        self.Quuid = None
        self.ProtectSwitch = None
        self.AutoRecovery = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.ProtectSwitch = params.get("ProtectSwitch")
        self.AutoRecovery = params.get("AutoRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectMachine(AbstractModel):
    """机器授权到期信息

    """

    def __init__(self):
        r"""
        :param HostName: 机器名称
        :type HostName: str
        :param HostIp: 机器IP
        :type HostIp: str
        :param SafeguardDirNum: 防护目录数
        :type SafeguardDirNum: int
        """
        self.HostName = None
        self.HostIp = None
        self.SafeguardDirNum = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.HostIp = params.get("HostIp")
        self.SafeguardDirNum = params.get("SafeguardDirNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectMachineInfo(AbstractModel):
    """授权机器信息

    """

    def __init__(self):
        r"""
        :param HostName: 机器名称
        :type HostName: str
        :param HostIp: 机器IP
        :type HostIp: str
        :param CreateTime: 开通时间
        :type CreateTime: str
        :param ExpireTime: 到期时间
        :type ExpireTime: str
        """
        self.HostName = None
        self.HostIp = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.HostIp = params.get("HostIp")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectNetInfo(AbstractModel):
    """专家服务-旗舰护网信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param ProtectDays: 护网天数
        :type ProtectDays: int
        :param Status: 护网状态 0未启动，1护网中，2已完成
        :type Status: int
        :param StartTime: 护网启动时间
        :type StartTime: str
        :param EndTime: 护网完成时间
        :type EndTime: str
        :param ReportPath: 报告下载地址
        :type ReportPath: str
        """
        self.TaskId = None
        self.ProtectDays = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.ReportPath = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProtectDays = params.get("ProtectDays")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReportPath = params.get("ReportPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectStat(AbstractModel):
    """防护信息统计

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Num: 数量
        :type Num: int
        """
        self.Name = None
        self.Num = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 木马Id数组（最大100条）
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessIds: 恢复成功id数组，若无则返回空数组
        :type SuccessIds: list of int non-negative
        :param FailedIds: 恢复失败id数组，若无则返回空数组
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param Region: 地域标志，如 ap-guangzhou，ap-shanghai，ap-beijing
        :type Region: str
        :param RegionName: 地域中文名，如华南地区（广州），华东地区（上海金融），华北地区（北京）
        :type RegionName: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param RegionCode: 地域代码，如 gz，sh，bj
        :type RegionCode: str
        :param RegionNameEn: 地域英文名
        :type RegionNameEn: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionCode = None
        self.RegionNameEn = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionCode = params.get("RegionCode")
        self.RegionNameEn = params.get("RegionNameEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionSet(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param RegionName: 地域名称
        :type RegionName: str
        :param ZoneSet: 可用区信息
        :type ZoneSet: list of ZoneInfo
        """
        self.RegionName = None
        self.ZoneSet = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReverseShell(AbstractModel):
    """反弹Shell数据

    """

    def __init__(self):
        r"""
        :param Id: ID 主键
        :type Id: int
        :param Uuid: 云镜UUID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: int
        :param ProcessName: 进程名
        :type ProcessName: str
        :param FullPath: 进程路径
        :type FullPath: str
        :param CmdLine: 命令详情
        :type CmdLine: str
        :param UserName: 执行用户
        :type UserName: str
        :param UserGroup: 执行用户组
        :type UserGroup: str
        :param ParentProcName: 父进程名
        :type ParentProcName: str
        :param ParentProcUser: 父进程用户
        :type ParentProcUser: str
        :param ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param Status: 处理状态：0-待处理 2-白名单 3-已处理 4-已忽略
        :type Status: int
        :param CreateTime: 产生时间
        :type CreateTime: str
        :param MachineName: 主机名
        :type MachineName: str
        :param ProcTree: 进程树
        :type ProcTree: str
        :param DetectBy: 检测方法
        :type DetectBy: int
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.DstIp = None
        self.DstPort = None
        self.ProcessName = None
        self.FullPath = None
        self.CmdLine = None
        self.UserName = None
        self.UserGroup = None
        self.ParentProcName = None
        self.ParentProcUser = None
        self.ParentProcGroup = None
        self.ParentProcPath = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None
        self.ProcTree = None
        self.DetectBy = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.ProcessName = params.get("ProcessName")
        self.FullPath = params.get("FullPath")
        self.CmdLine = params.get("CmdLine")
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.ParentProcName = params.get("ParentProcName")
        self.ParentProcUser = params.get("ParentProcUser")
        self.ParentProcGroup = params.get("ParentProcGroup")
        self.ParentProcPath = params.get("ParentProcPath")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.ProcTree = params.get("ProcTree")
        self.DetectBy = params.get("DetectBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReverseShellRule(AbstractModel):
    """反弹Shell规则

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param DestIp: 目标IP
        :type DestIp: str
        :param DestPort: 目标端口
        :type DestPort: str
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        """
        self.Id = None
        self.Uuid = None
        self.ProcessName = None
        self.DestIp = None
        self.DestPort = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.DestIp = params.get("DestIp")
        self.DestPort = params.get("DestPort")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDnsList(AbstractModel):
    """恶意请求列表

    """

    def __init__(self):
        r"""
        :param Url: 对外访问域名
        :type Url: str
        :param AccessCount: 访问次数
        :type AccessCount: int
        :param ProcessName: 进程名
        :type ProcessName: str
        :param ProcessMd5: 进程MD5
        :type ProcessMd5: str
        :param GlobalRuleId: 是否为全局规则，0否，1是
        :type GlobalRuleId: int
        :param UserRuleId: 用户规则id
        :type UserRuleId: int
        :param Status: 状态；0-待处理，2-已加白，3-非信任状态，4-已处理，5-已忽略
        :type Status: int
        :param CreateTime: 首次访问时间
        :type CreateTime: str
        :param MergeTime: 最近访问时间
        :type MergeTime: str
        :param Quuid: 唯一 Quuid
        :type Quuid: str
        :param HostIp: 主机ip
        :type HostIp: str
        :param Alias: 别名
        :type Alias: str
        :param Description: 描述
        :type Description: str
        :param Id: 唯一ID
        :type Id: int
        :param Reference: 参考
        :type Reference: str
        :param CmdLine: 命令行
        :type CmdLine: str
        :param Pid: 进程号
        :type Pid: int
        :param Uuid: 唯一UUID
        :type Uuid: str
        :param SuggestScheme: 建议方案
        :type SuggestScheme: str
        :param Tags: 标签特性
        :type Tags: list of str
        :param MachineWanIp: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineWanIp: str
        :param MachineStatus: 主机在线状态 OFFLINE  ONLINE
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineStatus: str
        """
        self.Url = None
        self.AccessCount = None
        self.ProcessName = None
        self.ProcessMd5 = None
        self.GlobalRuleId = None
        self.UserRuleId = None
        self.Status = None
        self.CreateTime = None
        self.MergeTime = None
        self.Quuid = None
        self.HostIp = None
        self.Alias = None
        self.Description = None
        self.Id = None
        self.Reference = None
        self.CmdLine = None
        self.Pid = None
        self.Uuid = None
        self.SuggestScheme = None
        self.Tags = None
        self.MachineWanIp = None
        self.MachineStatus = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.AccessCount = params.get("AccessCount")
        self.ProcessName = params.get("ProcessName")
        self.ProcessMd5 = params.get("ProcessMd5")
        self.GlobalRuleId = params.get("GlobalRuleId")
        self.UserRuleId = params.get("UserRuleId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MergeTime = params.get("MergeTime")
        self.Quuid = params.get("Quuid")
        self.HostIp = params.get("HostIp")
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.Id = params.get("Id")
        self.Reference = params.get("Reference")
        self.CmdLine = params.get("CmdLine")
        self.Pid = params.get("Pid")
        self.Uuid = params.get("Uuid")
        self.SuggestScheme = params.get("SuggestScheme")
        self.Tags = params.get("Tags")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineStatus = params.get("MachineStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanAssetRequest(AbstractModel):
    """ScanAsset请求参数结构体

    """

    def __init__(self):
        r"""
        :param AssetTypeIds: 资产指纹类型id列表
        :type AssetTypeIds: list of int non-negative
        :param Quuids: Quuid列表
        :type Quuids: list of str
        """
        self.AssetTypeIds = None
        self.Quuids = None


    def _deserialize(self, params):
        self.AssetTypeIds = params.get("AssetTypeIds")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanAssetResponse(AbstractModel):
    """ScanAsset返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ScanTaskDetails(AbstractModel):
    """扫描任务详情列表信息

    """

    def __init__(self):
        r"""
        :param HostIp: 服务器IP
        :type HostIp: str
        :param HostName: 服务器名称
        :type HostName: str
        :param OsName: 操作系统
        :type OsName: str
        :param RiskNum: 风险数量
        :type RiskNum: int
        :param ScanBeginTime: 扫描开始时间
        :type ScanBeginTime: str
        :param ScanEndTime: 扫描结束时间
        :type ScanEndTime: str
        :param Uuid: 唯一Uuid
        :type Uuid: str
        :param Quuid: 唯一Quuid
        :type Quuid: str
        :param Status: 状态码
        :type Status: str
        :param Description: 描述
        :type Description: str
        :param Id: id唯一
        :type Id: int
        :param FailType: 失败详情
        :type FailType: int
        :param MachineWanIp: 外网ip
        :type MachineWanIp: str
        """
        self.HostIp = None
        self.HostName = None
        self.OsName = None
        self.RiskNum = None
        self.ScanBeginTime = None
        self.ScanEndTime = None
        self.Uuid = None
        self.Quuid = None
        self.Status = None
        self.Description = None
        self.Id = None
        self.FailType = None
        self.MachineWanIp = None


    def _deserialize(self, params):
        self.HostIp = params.get("HostIp")
        self.HostName = params.get("HostName")
        self.OsName = params.get("OsName")
        self.RiskNum = params.get("RiskNum")
        self.ScanBeginTime = params.get("ScanBeginTime")
        self.ScanEndTime = params.get("ScanEndTime")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Id = params.get("Id")
        self.FailType = params.get("FailType")
        self.MachineWanIp = params.get("MachineWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulAgainRequest(AbstractModel):
    """ScanVulAgain请求参数结构体

    """

    def __init__(self):
        r"""
        :param EventIds: 漏洞事件id串，多个用英文逗号分隔
        :type EventIds: str
        :param Uuids: 重新检查的机器uuid,多个逗号分隔
        :type Uuids: str
        """
        self.EventIds = None
        self.Uuids = None


    def _deserialize(self, params):
        self.EventIds = params.get("EventIds")
        self.Uuids = params.get("Uuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulAgainResponse(AbstractModel):
    """ScanVulAgain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ScanVulRequest(AbstractModel):
    """ScanVul请求参数结构体

    """

    def __init__(self):
        r"""
        :param VulLevels: 危害等级：1-低危；2-中危；3-高危；4-严重 (多选英文;分隔)
        :type VulLevels: str
        :param HostType: 服务器分类：1:专业版服务器；2:自选服务器
        :type HostType: int
        :param VulCategories: 漏洞类型：1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞 (多选英文;分隔)
        :type VulCategories: str
        :param QuuidList: 自选服务器时生效，主机quuid的string数组
        :type QuuidList: list of str
        :param VulEmergency: 是否是应急漏洞 0 否 1 是
        :type VulEmergency: int
        :param TimeoutPeriod: 超时时长 单位秒 默认 3600 秒
        :type TimeoutPeriod: int
        :param VulIds: 需要扫描的漏洞id
        :type VulIds: list of int non-negative
        """
        self.VulLevels = None
        self.HostType = None
        self.VulCategories = None
        self.QuuidList = None
        self.VulEmergency = None
        self.TimeoutPeriod = None
        self.VulIds = None


    def _deserialize(self, params):
        self.VulLevels = params.get("VulLevels")
        self.HostType = params.get("HostType")
        self.VulCategories = params.get("VulCategories")
        self.QuuidList = params.get("QuuidList")
        self.VulEmergency = params.get("VulEmergency")
        self.TimeoutPeriod = params.get("TimeoutPeriod")
        self.VulIds = params.get("VulIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulResponse(AbstractModel):
    """ScanVul返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ScanVulSettingRequest(AbstractModel):
    """ScanVulSetting请求参数结构体

    """

    def __init__(self):
        r"""
        :param TimerInterval: 定期检测间隔时间（天）
        :type TimerInterval: int
        :param VulCategories: 漏洞类型：1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞, 以数组方式传参[1,2]
        :type VulCategories: list of int non-negative
        :param VulLevels: 危害等级：1-低危；2-中危；3-高危；4-严重,以数组方式传参[1,2,3]
        :type VulLevels: list of int non-negative
        :param TimerTime: 定期检测时间，如：02:10:50
        :type TimerTime: str
        :param VulEmergency: 是否是应急漏洞 0 否 1 是
        :type VulEmergency: int
        :param StartTime: 扫描开始时间，如：00:00
        :type StartTime: str
        :param EndTime: 扫描结束时间，如：08:00
        :type EndTime: str
        :param EnableScan: 是否开启扫描 1开启 0不开启
        :type EnableScan: int
        """
        self.TimerInterval = None
        self.VulCategories = None
        self.VulLevels = None
        self.TimerTime = None
        self.VulEmergency = None
        self.StartTime = None
        self.EndTime = None
        self.EnableScan = None


    def _deserialize(self, params):
        self.TimerInterval = params.get("TimerInterval")
        self.VulCategories = params.get("VulCategories")
        self.VulLevels = params.get("VulLevels")
        self.TimerTime = params.get("TimerTime")
        self.VulEmergency = params.get("VulEmergency")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EnableScan = params.get("EnableScan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulSettingResponse(AbstractModel):
    """ScanVulSetting返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchTemplate(AbstractModel):
    """快速搜索模板

    """

    def __init__(self):
        r"""
        :param Name: 检索名称
        :type Name: str
        :param LogType: 检索索引类型
        :type LogType: str
        :param Condition: 检索语句
        :type Condition: str
        :param TimeRange: 时间范围
        :type TimeRange: str
        :param Query: 转换的检索语句内容
        :type Query: str
        :param Flag: 检索方式。输入框检索：standard,过滤，检索：simple
        :type Flag: str
        :param DisplayData: 展示数据
        :type DisplayData: str
        :param Id: 规则ID
        :type Id: int
        """
        self.Name = None
        self.LogType = None
        self.Condition = None
        self.TimeRange = None
        self.Query = None
        self.Flag = None
        self.DisplayData = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.LogType = params.get("LogType")
        self.Condition = params.get("Condition")
        self.TimeRange = params.get("TimeRange")
        self.Query = params.get("Query")
        self.Flag = params.get("Flag")
        self.DisplayData = params.get("DisplayData")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityButlerInfo(AbstractModel):
    """安全管家列表信息

    """

    def __init__(self):
        r"""
        :param Id: 数据id
        :type Id: int
        :param OrderId: 订单id
        :type OrderId: int
        :param Quuid: cvm id
        :type Quuid: str
        :param Status: 服务状态 0-服务中,1-已到期 2已销毁
        :type Status: int
        :param StartTime: 服务开始时间
        :type StartTime: str
        :param EndTime: 服务结束时间
        :type EndTime: str
        :param HostName: 主机名称
        :type HostName: str
        :param HostIp: 主机Ip
        :type HostIp: str
        :param Uuid: 主机 uuid
        :type Uuid: str
        :param RiskCount: 主机风险数
        :type RiskCount: int
        """
        self.Id = None
        self.OrderId = None
        self.Quuid = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.HostName = None
        self.HostIp = None
        self.Uuid = None
        self.RiskCount = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.OrderId = params.get("OrderId")
        self.Quuid = params.get("Quuid")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.HostName = params.get("HostName")
        self.HostIp = params.get("HostIp")
        self.Uuid = params.get("Uuid")
        self.RiskCount = params.get("RiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityDynamic(AbstractModel):
    """安全事件消息数据。

    """

    def __init__(self):
        r"""
        :param Uuid: 云镜客户端UUID。
        :type Uuid: str
        :param EventTime: 安全事件发生时间。
        :type EventTime: str
        :param EventType: 安全事件类型。
<li>MALWARE：木马事件</li>
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>BRUTEATTACK_SUCCESS：密码破解成功</li>
<li>VUL：漏洞</li>
<li>BASELINE：安全基线</li>
        :type EventType: str
        :param Message: 安全事件消息。
        :type Message: str
        :param SecurityLevel: 安全事件等级。
<li>RISK: 严重</li>
<li>HIGH: 高危</li>
<li>NORMAL: 中危</li>
<li>LOW: 低危</li>
        :type SecurityLevel: str
        """
        self.Uuid = None
        self.EventTime = None
        self.EventType = None
        self.Message = None
        self.SecurityLevel = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Message = params.get("Message")
        self.SecurityLevel = params.get("SecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityEventInfo(AbstractModel):
    """安全事件统计列表

    """

    def __init__(self):
        r"""
        :param EventCnt: 安全事件数
        :type EventCnt: int
        :param UuidCnt: 受影响机器数
        :type UuidCnt: int
        """
        self.EventCnt = None
        self.UuidCnt = None


    def _deserialize(self, params):
        self.EventCnt = params.get("EventCnt")
        self.UuidCnt = params.get("UuidCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityTrend(AbstractModel):
    """安全趋势统计数据。

    """

    def __init__(self):
        r"""
        :param Date: 事件时间。
        :type Date: str
        :param EventNum: 事件数量。
        :type EventNum: int
        """
        self.Date = None
        self.EventNum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventNum = params.get("EventNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 木马事件ID数组。(最大100条)
        :type Ids: list of int non-negative
        :param KillProcess: 是否杀掉进程
        :type KillProcess: bool
        """
        self.Ids = None
        self.KillProcess = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.KillProcess = params.get("KillProcess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessIds: 隔离成功的id数组，若无则返回空数组
        :type SuccessIds: list of int non-negative
        :param FailedIds: 隔离失败的id数组，若无则返回空数组
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class SetBashEventsStatusRequest(AbstractModel):
    """SetBashEventsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        :param Status: 新状态(0-待处理 1-高危 2-正常)
        :type Status: int
        """
        self.Ids = None
        self.Status = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetBashEventsStatusResponse(AbstractModel):
    """SetBashEventsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StandardModeConfig(AbstractModel):
    """标准模式阻断配置

    """

    def __init__(self):
        r"""
        :param Ttl: 阻断时长，单位：秒
        :type Ttl: int
        """
        self.Ttl = None


    def _deserialize(self, params):
        self.Ttl = params.get("Ttl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopNoticeBanTipsRequest(AbstractModel):
    """StopNoticeBanTips请求参数结构体

    """


class StopNoticeBanTipsResponse(AbstractModel):
    """StopNoticeBanTips返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Strategy(AbstractModel):
    """基线安全用户策略信息

    """

    def __init__(self):
        r"""
        :param StrategyName: 策略名
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param StrategyId: 策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: int
        :param RuleCount: 基线检测项总数
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCount: int
        :param HostCount: 主机数量
注意：此字段可能返回 null，表示取不到有效值。
        :type HostCount: int
        :param ScanCycle: 扫描周期
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanCycle: int
        :param ScanAt: 扫描时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScanAt: str
        :param Enabled: 是否可用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: int
        :param PassRate: 通过率
注意：此字段可能返回 null，表示取不到有效值。
        :type PassRate: int
        :param CategoryIds: 基线id
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryIds: str
        :param IsDefault: 是否默认策略
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: int
        """
        self.StrategyName = None
        self.StrategyId = None
        self.RuleCount = None
        self.HostCount = None
        self.ScanCycle = None
        self.ScanAt = None
        self.Enabled = None
        self.PassRate = None
        self.CategoryIds = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.StrategyName = params.get("StrategyName")
        self.StrategyId = params.get("StrategyId")
        self.RuleCount = params.get("RuleCount")
        self.HostCount = params.get("HostCount")
        self.ScanCycle = params.get("ScanCycle")
        self.ScanAt = params.get("ScanAt")
        self.Enabled = params.get("Enabled")
        self.PassRate = params.get("PassRate")
        self.CategoryIds = params.get("CategoryIds")
        self.IsDefault = params.get("IsDefault")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchBashRulesRequest(AbstractModel):
    """SwitchBashRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 规则ID
        :type Id: int
        :param Disabled: 是否禁用
        :type Disabled: int
        """
        self.Id = None
        self.Disabled = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchBashRulesResponse(AbstractModel):
    """SwitchBashRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncAssetScanRequest(AbstractModel):
    """SyncAssetScan请求参数结构体

    """

    def __init__(self):
        r"""
        :param Sync: 是否同步：true-是 false-否；默认false
        :type Sync: bool
        """
        self.Sync = None


    def _deserialize(self, params):
        self.Sync = params.get("Sync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncAssetScanResponse(AbstractModel):
    """SyncAssetScan返回参数结构体

    """

    def __init__(self):
        r"""
        :param State: 枚举值有(大写)：NOTASK（没有同步任务），SYNCING（同步中），FINISHED（同步完成）
        :type State: str
        :param LatestStartTime: 最新开始同步时间
        :type LatestStartTime: str
        :param LatestEndTime: 最新结束同步时间
        :type LatestEndTime: str
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.LatestStartTime = None
        self.LatestEndTime = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.LatestStartTime = params.get("LatestStartTime")
        self.LatestEndTime = params.get("LatestEndTime")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param Id: 标签ID
        :type Id: int
        :param Name: 标签名
        :type Name: str
        :param Count: 服务器数
        :type Count: int
        """
        self.Id = None
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagMachine(AbstractModel):
    """标签相关服务器信息

    """

    def __init__(self):
        r"""
        :param Id: ID
        :type Id: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param MachineRegion: 主机区域
        :type MachineRegion: str
        :param MachineType: 主机区域类型
        :type MachineType: str
        """
        self.Id = None
        self.Quuid = None
        self.MachineName = None
        self.MachineIp = None
        self.MachineWanIp = None
        self.MachineRegion = None
        self.MachineType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.MachineName = params.get("MachineName")
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineRegion = params.get("MachineRegion")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    """平台标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatus(AbstractModel):
    """任务扫描状态列表

    """

    def __init__(self):
        r"""
        :param Scanning: 扫描中（包含初始化）
        :type Scanning: str
        :param Ok: 扫描终止（包含终止中）
        :type Ok: str
        :param Fail: 扫描失败
        :type Fail: str
        :param Stop: 扫描失败（提示具体原因：扫描超时、客户端版本低、客户端离线）
注意：此字段可能返回 null，表示取不到有效值。
        :type Stop: str
        """
        self.Scanning = None
        self.Ok = None
        self.Fail = None
        self.Stop = None


    def _deserialize(self, params):
        self.Scanning = params.get("Scanning")
        self.Ok = params.get("Ok")
        self.Fail = params.get("Fail")
        self.Stop = params.get("Stop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 木马ID数组（单次不超过的最大条数：100）
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param Ids: 木马ID数组 (最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateBaselineStrategyRequest(AbstractModel):
    """UpdateBaselineStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param StrategyId: 策略id
        :type StrategyId: int
        :param StrategyName: 策略名称
        :type StrategyName: str
        :param ScanCycle: 检测周期
        :type ScanCycle: int
        :param ScanAt: 定期检测时间，该时间下发扫描
        :type ScanAt: str
        :param CategoryIds: 该策略下选择的基线id数组
        :type CategoryIds: list of str
        :param IsGlobal: 扫描范围是否全部服务器, 1:是  0:否, 为1则为全部专业版主机
        :type IsGlobal: int
        :param MachineType: 云主机类型：
cvm：腾讯云服务器
bm：裸金属
ecm：边缘计算主机
lh:轻量应用服务器
other:混合云机器
        :type MachineType: str
        :param RegionCode: 主机地域 ap-guangzhou
        :type RegionCode: str
        :param Quuids: 主机id数组
        :type Quuids: list of str
        """
        self.StrategyId = None
        self.StrategyName = None
        self.ScanCycle = None
        self.ScanAt = None
        self.CategoryIds = None
        self.IsGlobal = None
        self.MachineType = None
        self.RegionCode = None
        self.Quuids = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        self.StrategyName = params.get("StrategyName")
        self.ScanCycle = params.get("ScanCycle")
        self.ScanAt = params.get("ScanAt")
        self.CategoryIds = params.get("CategoryIds")
        self.IsGlobal = params.get("IsGlobal")
        self.MachineType = params.get("MachineType")
        self.RegionCode = params.get("RegionCode")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBaselineStrategyResponse(AbstractModel):
    """UpdateBaselineStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateMachineTagsRequest(AbstractModel):
    """UpdateMachineTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param Quuid: 机器 Quuid
        :type Quuid: str
        :param MachineRegion: 服务器地区 如: ap-guangzhou
        :type MachineRegion: str
        :param MachineArea: 服务器类型(CVM|BM|ECM|LH|Other)
        :type MachineArea: str
        :param TagIds: 标签ID，该操作会覆盖原有的标签列表
        :type TagIds: list of int non-negative
        """
        self.Quuid = None
        self.MachineRegion = None
        self.MachineArea = None
        self.TagIds = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.MachineRegion = params.get("MachineRegion")
        self.MachineArea = params.get("MachineArea")
        self.TagIds = params.get("TagIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateMachineTagsResponse(AbstractModel):
    """UpdateMachineTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """常用登录地

    """

    def __init__(self):
        r"""
        :param Id: ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param CountryId: 国家 ID。
        :type CountryId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CityId: 城市 ID。
        :type CityId: int
        """
        self.Id = None
        self.Uuid = None
        self.CountryId = None
        self.ProvinceId = None
        self.CityId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.CountryId = params.get("CountryId")
        self.ProvinceId = params.get("ProvinceId")
        self.CityId = params.get("CityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDetailInfo(AbstractModel):
    """漏洞详细信息

    """

    def __init__(self):
        r"""
        :param VulId: 漏洞ID
        :type VulId: int
        :param Level: 漏洞级别
        :type Level: int
        :param Name: 漏洞名称
        :type Name: str
        :param CveId: cve编号
        :type CveId: str
        :param VulCategory: 1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞 0= 应急漏洞
        :type VulCategory: int
        :param Descript: 漏洞描述
        :type Descript: str
        :param Fix: 修复建议
        :type Fix: str
        :param Reference: 参考链接
        :type Reference: str
        :param CvssScore: CVSS评分
        :type CvssScore: float
        :param Cvss: CVSS详情
        :type Cvss: str
        :param PublishTime: 发布时间
        :type PublishTime: str
        """
        self.VulId = None
        self.Level = None
        self.Name = None
        self.CveId = None
        self.VulCategory = None
        self.Descript = None
        self.Fix = None
        self.Reference = None
        self.CvssScore = None
        self.Cvss = None
        self.PublishTime = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Level = params.get("Level")
        self.Name = params.get("Name")
        self.CveId = params.get("CveId")
        self.VulCategory = params.get("VulCategory")
        self.Descript = params.get("Descript")
        self.Fix = params.get("Fix")
        self.Reference = params.get("Reference")
        self.CvssScore = params.get("CvssScore")
        self.Cvss = params.get("Cvss")
        self.PublishTime = params.get("PublishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulEffectHostList(AbstractModel):
    """漏洞影响主机列表

    """

    def __init__(self):
        r"""
        :param EventId: 事件id
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: int
        :param Status: 状态：0: 待处理 1:忽略  3:已修复  5:检测中 6:修复中 7: 回滚中 8:修复失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param LastTime: 最后检测时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTime: str
        :param Level: 危害等级：1-低危；2-中危；3-高危；4-严重
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param Quuid: 主机Quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param Uuid: 主机Uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param HostIp: 主机HostIp
注意：此字段可能返回 null，表示取不到有效值。
        :type HostIp: str
        :param AliasName: 主机别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param Tags: 主机标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Description: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param HostVersion: 版本信息：0-基础版 1-专业版 2-旗舰版 3-普惠版
注意：此字段可能返回 null，表示取不到有效值。
        :type HostVersion: int
        :param IsSupportAutoFix: 是否能自动修复 0 :漏洞不可自动修复，  1：可自动修复， 2：客户端已离线， 3：主机不是旗舰版只能手动修复， 4：机型不允许 ，5：修复中 ，6：已修复， 7：检测中  9:修复失败，10:已忽略 11:漏洞只支持linux不支持Windows 12：漏洞只支持Windows不支持linux，13:修复失败但此时主机已离线，14:修复失败但此时主机不是旗舰版， 15:已手动修复
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportAutoFix: int
        :param FixStatusMsg: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FixStatusMsg: str
        :param FirstDiscoveryTime: 首次发现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstDiscoveryTime: str
        :param InstanceState: 实例状态："PENDING"-创建中 "LAUNCH_FAILED"-创建失败 "RUNNING"-运行中 "STOPPED"-关机 "STARTING"-表示开机中 "STOPPING"-表示关机中 "REBOOTING"-重启中 "SHUTDOWN"-表示停止待销毁 "TERMINATING"-表示销毁中 "
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param PublicIpAddresses: 外网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: str
        """
        self.EventId = None
        self.Status = None
        self.LastTime = None
        self.Level = None
        self.Quuid = None
        self.Uuid = None
        self.HostIp = None
        self.AliasName = None
        self.Tags = None
        self.Description = None
        self.HostVersion = None
        self.IsSupportAutoFix = None
        self.FixStatusMsg = None
        self.FirstDiscoveryTime = None
        self.InstanceState = None
        self.PublicIpAddresses = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.Status = params.get("Status")
        self.LastTime = params.get("LastTime")
        self.Level = params.get("Level")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.HostIp = params.get("HostIp")
        self.AliasName = params.get("AliasName")
        self.Tags = params.get("Tags")
        self.Description = params.get("Description")
        self.HostVersion = params.get("HostVersion")
        self.IsSupportAutoFix = params.get("IsSupportAutoFix")
        self.FixStatusMsg = params.get("FixStatusMsg")
        self.FirstDiscoveryTime = params.get("FirstDiscoveryTime")
        self.InstanceState = params.get("InstanceState")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulHostTopInfo(AbstractModel):
    """服务器风险top5实体

    """

    def __init__(self):
        r"""
        :param HostName: 主机名
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param VulLevelList: 漏洞等级与数量统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulLevelList: list of VulLevelCountInfo
        :param Quuid: 主机Quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param Score: top评分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self.HostName = None
        self.VulLevelList = None
        self.Quuid = None
        self.Score = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        if params.get("VulLevelList") is not None:
            self.VulLevelList = []
            for item in params.get("VulLevelList"):
                obj = VulLevelCountInfo()
                obj._deserialize(item)
                self.VulLevelList.append(obj)
        self.Quuid = params.get("Quuid")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulInfoList(AbstractModel):
    """主机安全-漏洞管理-漏洞列表

    """

    def __init__(self):
        r"""
        :param Ids: 漏洞包含的事件id串，多个用“,”分割
        :type Ids: str
        :param Name: 漏洞名
        :type Name: str
        :param Status: 0: 待处理 1:忽略  3:已修复  5:检测中 6:修复中  8:修复失败
        :type Status: int
        :param VulId: 漏洞id
        :type VulId: int
        :param PublishTime: 漏洞披露事件
        :type PublishTime: str
        :param LastTime: 最后检测时间
        :type LastTime: str
        :param HostCount: 影响主机数
        :type HostCount: int
        :param Level: 漏洞等级 1:低 2:中 3:高 4:严重
        :type Level: int
        :param From: 废弃字段
注意：此字段可能返回 null，表示取不到有效值。
        :type From: int
        :param Descript: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Descript: str
        :param PublishTimeWisteria: 废弃字段
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishTimeWisteria: str
        :param NameWisteria: 废弃字段
注意：此字段可能返回 null，表示取不到有效值。
        :type NameWisteria: str
        :param DescriptWisteria: 废弃字段
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptWisteria: str
        :param StatusStr: 聚合后事件状态串
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusStr: str
        :param CveId: cve编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CveId: str
        :param CvssScore: CVSS评分
注意：此字段可能返回 null，表示取不到有效值。
        :type CvssScore: float
        :param Labels: 漏洞标签 多个逗号分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: str
        :param FixSwitch: 是否能自动修复且包含能自动修复的主机， 0=否  1=是
注意：此字段可能返回 null，表示取不到有效值。
        :type FixSwitch: int
        :param TaskId: 最后扫描任务的id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param IsSupportDefense: 是否支持防御， 0:不支持 1:支持
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportDefense: int
        :param DefenseAttackCount: 已防御的攻击次数
注意：此字段可能返回 null，表示取不到有效值。
        :type DefenseAttackCount: int
        :param FirstAppearTime: 首次出现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstAppearTime: str
        :param VulCategory: 漏洞类别 1: web-cms漏洞 2:应用漏洞  4: Linux软件漏洞 5: Windows系统漏洞
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCategory: int
        """
        self.Ids = None
        self.Name = None
        self.Status = None
        self.VulId = None
        self.PublishTime = None
        self.LastTime = None
        self.HostCount = None
        self.Level = None
        self.From = None
        self.Descript = None
        self.PublishTimeWisteria = None
        self.NameWisteria = None
        self.DescriptWisteria = None
        self.StatusStr = None
        self.CveId = None
        self.CvssScore = None
        self.Labels = None
        self.FixSwitch = None
        self.TaskId = None
        self.IsSupportDefense = None
        self.DefenseAttackCount = None
        self.FirstAppearTime = None
        self.VulCategory = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.VulId = params.get("VulId")
        self.PublishTime = params.get("PublishTime")
        self.LastTime = params.get("LastTime")
        self.HostCount = params.get("HostCount")
        self.Level = params.get("Level")
        self.From = params.get("From")
        self.Descript = params.get("Descript")
        self.PublishTimeWisteria = params.get("PublishTimeWisteria")
        self.NameWisteria = params.get("NameWisteria")
        self.DescriptWisteria = params.get("DescriptWisteria")
        self.StatusStr = params.get("StatusStr")
        self.CveId = params.get("CveId")
        self.CvssScore = params.get("CvssScore")
        self.Labels = params.get("Labels")
        self.FixSwitch = params.get("FixSwitch")
        self.TaskId = params.get("TaskId")
        self.IsSupportDefense = params.get("IsSupportDefense")
        self.DefenseAttackCount = params.get("DefenseAttackCount")
        self.FirstAppearTime = params.get("FirstAppearTime")
        self.VulCategory = params.get("VulCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulLevelCountInfo(AbstractModel):
    """漏洞等级数量实体

    """

    def __init__(self):
        r"""
        :param VulLevel: 漏洞等级
        :type VulLevel: int
        :param VulCount: 漏洞数量
        :type VulCount: int
        """
        self.VulLevel = None
        self.VulCount = None


    def _deserialize(self, params):
        self.VulLevel = params.get("VulLevel")
        self.VulCount = params.get("VulCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulLevelInfo(AbstractModel):
    """漏洞数量按等级分布统计结果实体

    """

    def __init__(self):
        r"""
        :param VulLevel: // 危害等级：1-低危；2-中危；3-高危；4-严重
        :type VulLevel: int
        :param Count: 数量
        :type Count: int
        """
        self.VulLevel = None
        self.Count = None


    def _deserialize(self, params):
        self.VulLevel = params.get("VulLevel")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulTopInfo(AbstractModel):
    """漏洞top统计实体

    """

    def __init__(self):
        r"""
        :param VulName: 漏洞 名
注意：此字段可能返回 null，表示取不到有效值。
        :type VulName: str
        :param VulLevel: 危害等级：1-低危；2-中危；3-高危；4-严重
注意：此字段可能返回 null，表示取不到有效值。
        :type VulLevel: int
        :param VulCount: 漏洞数量
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCount: int
        :param VulId: 漏洞id
注意：此字段可能返回 null，表示取不到有效值。
        :type VulId: int
        """
        self.VulName = None
        self.VulLevel = None
        self.VulCount = None
        self.VulId = None


    def _deserialize(self, params):
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.VulCount = params.get("VulCount")
        self.VulId = params.get("VulId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WarningInfoObj(AbstractModel):
    """告警设置列表

    """

    def __init__(self):
        r"""
        :param Type: 事件告警类型；1：离线，2：木马，3：异常登录，4：爆破，5：漏洞（已拆分为9-12四种类型）6：高危命令，7：反弹sell，8：本地提权，9：应用漏洞，10：web-cms漏洞，11：应急漏洞，12：安全基线 ,13: 防篡改，14：恶意请求，15: 网络攻击，16：Windows系统漏洞，17：Linux软件漏洞，18：核心文件监控告警，19：客户端卸载告警。20：客户端离线告警
        :type Type: int
        :param DisablePhoneWarning: 1: 关闭告警 0: 开启告警
        :type DisablePhoneWarning: int
        :param BeginTime: 开始时间，格式: HH:mm
        :type BeginTime: str
        :param EndTime: 结束时间，格式: HH:mm
        :type EndTime: str
        :param TimeZone: 时区信息
        :type TimeZone: str
        :param ControlBit: 漏洞等级控制位（对应DB的十进制存储）
        :type ControlBit: int
        :param ControlBits: 漏洞等级控制位二进制，每一位对应页面漏洞等级的开启关闭：低中高（0:关闭；1：开启），例如：101 → 同时勾选低+高
        :type ControlBits: str
        """
        self.Type = None
        self.DisablePhoneWarning = None
        self.BeginTime = None
        self.EndTime = None
        self.TimeZone = None
        self.ControlBit = None
        self.ControlBits = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.DisablePhoneWarning = params.get("DisablePhoneWarning")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TimeZone = params.get("TimeZone")
        self.ControlBit = params.get("ControlBit")
        self.ControlBits = params.get("ControlBits")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WarningObject(AbstractModel):
    """告警更新或插入的参数

    """

    def __init__(self):
        r"""
        :param Type: 事件告警类型；1：离线，2：木马，3：异常登录，4：爆破，5：漏洞（已拆分为9-12四种类型）6：高位命令，7：反弹sell，8：本地提权，9：系统组件漏洞，10：web应用漏洞，11：应急漏洞，12：安全基线
        :type Type: int
        :param DisablePhoneWarning: 1: 关闭告警 0: 开启告警
        :type DisablePhoneWarning: int
        :param BeginTime: 开始时间，格式: HH:mm
        :type BeginTime: str
        :param EndTime: 结束时间，格式: HH:mm
        :type EndTime: str
        :param ControlBits: 漏洞等级控制位二进制，每一位对应页面漏洞等级的开启关闭：低中高（0:关闭；1：开启），例如：101 → 同时勾选低+高；01→(登录审计)疑似不告警，高危告警
        :type ControlBits: str
        """
        self.Type = None
        self.DisablePhoneWarning = None
        self.BeginTime = None
        self.EndTime = None
        self.ControlBits = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.DisablePhoneWarning = params.get("DisablePhoneWarning")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.ControlBits = params.get("ControlBits")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """可用区信息

    """

    def __init__(self):
        r"""
        :param ZoneName: 可用区名称
        :type ZoneName: str
        """
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        