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


class BatchDeleteDevicesRequest(AbstractModel):
    """BatchDeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 目标删除设备所属项目ID
        :type ProjectId: str
        :param DeviceIds: 目标删除设备的设备ID数组
        :type DeviceIds: list of str
        """
        self.ProjectId = None
        self.DeviceIds = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteDevicesResponse(AbstractModel):
    """BatchDeleteDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailedDeviceIds: 删除失败的设备ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedDeviceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedDeviceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedDeviceIds = params.get("FailedDeviceIds")
        self.RequestId = params.get("RequestId")


class BatchDeletePolicyRequest(AbstractModel):
    """BatchDeletePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 删除权限配置的项目ID
        :type ProjectId: str
        :param RemoteDeviceIds: 删除权限配置的远端设备ID列表
        :type RemoteDeviceIds: list of str
        :param PolicyMode: 删除权限配置的权限模式, black为黑名单，white为白名单
        :type PolicyMode: str
        """
        self.ProjectId = None
        self.RemoteDeviceIds = None
        self.PolicyMode = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RemoteDeviceIds = params.get("RemoteDeviceIds")
        self.PolicyMode = params.get("PolicyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeletePolicyResponse(AbstractModel):
    """BatchDeletePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailedRemoteDeviceIds: 删除权限配置失败的远端设备ID列表
        :type FailedRemoteDeviceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedRemoteDeviceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedRemoteDeviceIds = params.get("FailedRemoteDeviceIds")
        self.RequestId = params.get("RequestId")


class BoundLicensesRequest(AbstractModel):
    """BoundLicenses请求参数结构体

    """

    def __init__(self):
        r"""
        :param Count: license数量
        :type Count: int
        :param DeviceId: 设备id
        :type DeviceId: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        """
        self.Count = None
        self.DeviceId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.DeviceId = params.get("DeviceId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundLicensesResponse(AbstractModel):
    """BoundLicenses返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 创建设备所归属的项目ID
        :type ProjectId: str
        :param DeviceId: 创建设备ID，项目内需要唯一，由小写英文字母、数字和下划线构成，长度不超过18
        :type DeviceId: str
        :param DeviceName: 创建设备名称，长度小于24, 可包含中文、数字、英文字母和下划线
        :type DeviceName: str
        :param DeviceType: 设备类型，field为现场设备（受控设备），remote为远端设备（操控设备），不填默认为field
        :type DeviceType: str
        :param DeviceToken: 设备认证口令，由大小写英文字母和数字构成，须为16位
        :type DeviceToken: str
        """
        self.ProjectId = None
        self.DeviceId = None
        self.DeviceName = None
        self.DeviceType = None
        self.DeviceToken = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceType = params.get("DeviceType")
        self.DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectName: 项目名称，长度不超过24个字符
        :type ProjectName: str
        :param ProjectDescription: 项目描述，长度不超过120个字符，不填默认为空
        :type ProjectDescription: str
        :param PolicyMode: 权限模式，black为黑名单，white为白名单，不填默认为black
        :type PolicyMode: str
        """
        self.ProjectName = None
        self.ProjectDescription = None
        self.PolicyMode = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectDescription = params.get("ProjectDescription")
        self.PolicyMode = params.get("PolicyMode")
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
        :param ProjectId: 项目ID，长度为16位
        :type ProjectId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
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
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceInfoRequest(AbstractModel):
    """DescribeDeviceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 目标设备所属项目ID
        :type ProjectId: str
        :param DeviceId: 目标设备ID
        :type DeviceId: str
        """
        self.ProjectId = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceInfoResponse(AbstractModel):
    """DescribeDeviceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceType: 设备类型，field为现场设备（被控方），remote为远端设备（操控方）
        :type DeviceType: str
        :param DeviceStatus: 设备状态，offline为离线，ready为在线准备，connected为会话中
        :type DeviceStatus: str
        :param LastReportTime: 设备状态最后更新时间
        :type LastReportTime: str
        :param ModifyTime: 设备信息最后修改时间
        :type ModifyTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.DeviceType = None
        self.DeviceStatus = None
        self.LastReportTime = None
        self.ModifyTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DeviceType = params.get("DeviceType")
        self.DeviceStatus = params.get("DeviceStatus")
        self.LastReportTime = params.get("LastReportTime")
        self.ModifyTime = params.get("ModifyTime")
        self.RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    """DescribeDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 设备所属项目ID
        :type ProjectId: str
        :param DeviceType: 设备类型筛选，不填默认为全部设备类型
        :type DeviceType: str
        :param SearchWords: 对设备ID或Name按关键字进行模糊匹配，不填则不进行模糊匹配
        :type SearchWords: str
        :param PageSize: 每页返回的最大设备数，不填默认为10
        :type PageSize: int
        :param PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self.ProjectId = None
        self.DeviceType = None
        self.SearchWords = None
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DeviceType = params.get("DeviceType")
        self.SearchWords = params.get("SearchWords")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceListResponse(AbstractModel):
    """DescribeDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Devices: 设备信息列表
        :type Devices: list of DeviceInfo
        :param Total: 设备总数
        :type Total: int
        :param Num: 本次返回的设备数
        :type Num: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.Total = None
        self.Num = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.Total = params.get("Total")
        self.Num = params.get("Num")
        self.RequestId = params.get("RequestId")


class DescribeDeviceSessionDetailsRequest(AbstractModel):
    """DescribeDeviceSessionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: 会话ID
        :type SessionId: str
        """
        self.SessionId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceSessionDetailsResponse(AbstractModel):
    """DescribeDeviceSessionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param Details: 按设备区分的会话详细数据
        :type Details: list of SessionDeviceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = SessionDeviceDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceSessionListRequest(AbstractModel):
    """DescribeDeviceSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param PageNumber: 页码，从1开始
        :type PageNumber: int
        :param PageSize: 每页个数
        :type PageSize: int
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        """
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.DeviceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.DeviceId = params.get("DeviceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceSessionListResponse(AbstractModel):
    """DescribeDeviceSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总个数
        :type Total: int
        :param DeviceSessionList: 会话列表
        :type DeviceSessionList: list of SessionInfo
        :param Num: 本页数量
        :type Num: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.DeviceSessionList = None
        self.Num = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("DeviceSessionList") is not None:
            self.DeviceSessionList = []
            for item in params.get("DeviceSessionList"):
                obj = SessionInfo()
                obj._deserialize(item)
                self.DeviceSessionList.append(obj)
        self.Num = params.get("Num")
        self.RequestId = params.get("RequestId")


class DescribePolicyRequest(AbstractModel):
    """DescribePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 查看权限的项目ID
        :type ProjectId: str
        :param PolicyMode: 查看的权限模式，black为黑名单，white为白名单，不填默认为当前项目生效的权限模式
        :type PolicyMode: str
        :param SearchMode: 模糊匹配模式，remoteMatch为远端设备ID匹配，fieldMatch为现场ID匹配，不填默认为remoteMatch
        :type SearchMode: str
        :param SearchWords: 模糊匹配关键字，不填默认不进行模糊匹配
        :type SearchWords: str
        :param PageSize: 每页返回的最大数量，不填默认为10
        :type PageSize: int
        :param PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self.ProjectId = None
        self.PolicyMode = None
        self.SearchMode = None
        self.SearchWords = None
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PolicyMode = params.get("PolicyMode")
        self.SearchMode = params.get("SearchMode")
        self.SearchWords = params.get("SearchWords")
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyResponse(AbstractModel):
    """DescribePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyMode: 权限模式
        :type PolicyMode: str
        :param PolicyEnabled: 返回的权限模式是否为当前生效的权限模式
        :type PolicyEnabled: bool
        :param PolicyInfo: 权限信息列表
        :type PolicyInfo: list of PolicyInfo
        :param Num: 本次返回的权限信息数量
        :type Num: int
        :param Total: 权限信息总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyMode = None
        self.PolicyEnabled = None
        self.PolicyInfo = None
        self.Num = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyMode = params.get("PolicyMode")
        self.PolicyEnabled = params.get("PolicyEnabled")
        if params.get("PolicyInfo") is not None:
            self.PolicyInfo = []
            for item in params.get("PolicyInfo"):
                obj = PolicyInfo()
                obj._deserialize(item)
                self.PolicyInfo.append(obj)
        self.Num = params.get("Num")
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeProjectInfoRequest(AbstractModel):
    """DescribeProjectInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 目标项目ID
        :type ProjectId: str
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
        


class DescribeProjectInfoResponse(AbstractModel):
    """DescribeProjectInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDescription: 项目描述
        :type ProjectDescription: str
        :param PolicyMode: 项目权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param ModifyTime: 项目信息修改时间
        :type ModifyTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectName = None
        self.ProjectDescription = None
        self.PolicyMode = None
        self.ModifyTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectDescription = params.get("ProjectDescription")
        self.PolicyMode = params.get("PolicyMode")
        self.ModifyTime = params.get("ModifyTime")
        self.RequestId = params.get("RequestId")


class DescribeProjectListRequest(AbstractModel):
    """DescribeProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 每页返回的最大项目数量，不填默认为10
        :type PageSize: int
        :param PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self.PageSize = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectListResponse(AbstractModel):
    """DescribeProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Projects: 项目信息数组
        :type Projects: list of ProjectInfo
        :param Total: 项目总数
        :type Total: int
        :param Num: 本次返回的项目数
        :type Num: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Projects = None
        self.Total = None
        self.Num = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.Total = params.get("Total")
        self.Num = params.get("Num")
        self.RequestId = params.get("RequestId")


class DescribeRecentSessionListRequest(AbstractModel):
    """DescribeRecentSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param PageNumber: 页码，从1开始
        :type PageNumber: int
        :param PageSize: 每页个数
        :type PageSize: int
        :param DeviceId: 设备ID，支持过滤远端设备或现场设备
        :type DeviceId: str
        :param StartTime: 时间范围的起始时间。时间范围最大为最近两小时，若不传或超出范围，则起始时间按两小时前计算
        :type StartTime: int
        :param EndTime: 时间范围的结束时间。时间范围最大为最近两小时，若不传或超出范围，则结束时间按当前时间计算
        :type EndTime: int
        """
        self.ProjectId = None
        self.PageNumber = None
        self.PageSize = None
        self.DeviceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.DeviceId = params.get("DeviceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecentSessionListResponse(AbstractModel):
    """DescribeRecentSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总个数
        :type Total: int
        :param RecentSessionList: 会话列表
        :type RecentSessionList: list of RecentSessionInfo
        :param Num: 本页数量
        :type Num: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.RecentSessionList = None
        self.Num = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RecentSessionList") is not None:
            self.RecentSessionList = []
            for item in params.get("RecentSessionList"):
                obj = RecentSessionInfo()
                obj._deserialize(item)
                self.RecentSessionList.append(obj)
        self.Num = params.get("Num")
        self.RequestId = params.get("RequestId")


class DescribeSessionStatisticsByIntervalRequest(AbstractModel):
    """DescribeSessionStatisticsByInterval请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param StatisticInterval: 统计时间间隔：hour|day|month
        :type StatisticInterval: str
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param EndTime: 结束时间，单位：秒
        :type EndTime: int
        """
        self.ProjectId = None
        self.StatisticInterval = None
        self.DeviceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.StatisticInterval = params.get("StatisticInterval")
        self.DeviceId = params.get("DeviceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionStatisticsByIntervalResponse(AbstractModel):
    """DescribeSessionStatisticsByInterval返回参数结构体

    """

    def __init__(self):
        r"""
        :param SessionStatistics: 各时间段的会话统计数据
        :type SessionStatistics: list of SessionIntervalStatistic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SessionStatistics") is not None:
            self.SessionStatistics = []
            for item in params.get("SessionStatistics"):
                obj = SessionIntervalStatistic()
                obj._deserialize(item)
                self.SessionStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSessionStatisticsRequest(AbstractModel):
    """DescribeSessionStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param EndTime: 结束时间，单位：秒
        :type EndTime: int
        """
        self.ProjectId = None
        self.DeviceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionStatisticsResponse(AbstractModel):
    """DescribeSessionStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param SessionNum: 会话数量
        :type SessionNum: int
        :param TotalDuration: 通话时长，单位：分钟
        :type TotalDuration: int
        :param ActiveFieldDeviceNum: 活跃现场设备数
        :type ActiveFieldDeviceNum: int
        :param ActiveRemoteDeviceNum: 活跃远端设备数
        :type ActiveRemoteDeviceNum: int
        :param NotBadSessionRatio: 优良会话占比，单位：%
        :type NotBadSessionRatio: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionNum = None
        self.TotalDuration = None
        self.ActiveFieldDeviceNum = None
        self.ActiveRemoteDeviceNum = None
        self.NotBadSessionRatio = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionNum = params.get("SessionNum")
        self.TotalDuration = params.get("TotalDuration")
        self.ActiveFieldDeviceNum = params.get("ActiveFieldDeviceNum")
        self.ActiveRemoteDeviceNum = params.get("ActiveRemoteDeviceNum")
        self.NotBadSessionRatio = params.get("NotBadSessionRatio")
        self.RequestId = params.get("RequestId")


class Device(AbstractModel):
    """查询用户设备的授权绑定情况

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param LicenseCount: 已经绑定license数量
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseCount: int
        :param RemainDay: 剩余天数：天
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainDay: int
        :param ExpireTime: 过期时间：s
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param Duration: 服务时长：s
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param LicenseIds: 已经绑定licenseId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseIds: list of str
        """
        self.DeviceId = None
        self.DeviceName = None
        self.LicenseCount = None
        self.RemainDay = None
        self.ExpireTime = None
        self.Duration = None
        self.LicenseIds = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.DeviceName = params.get("DeviceName")
        self.LicenseCount = params.get("LicenseCount")
        self.RemainDay = params.get("RemainDay")
        self.ExpireTime = params.get("ExpireTime")
        self.Duration = params.get("Duration")
        self.LicenseIds = params.get("LicenseIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param DeviceId: 设备ID
        :type DeviceId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceStatus: 设备状态，offline为离线，ready为在线准备，connected为会话中
        :type DeviceStatus: str
        :param DeviceType: 设备类型，field为现场设备（受控方），remote为远端设备（操控方）
        :type DeviceType: str
        :param ModifyTime: 设备信息最近修改时间
        :type ModifyTime: str
        :param LastReportTime: 设备状态最近更新时间
        :type LastReportTime: str
        :param ProjectId: 设备所属项目Id
        :type ProjectId: str
        """
        self.DeviceId = None
        self.DeviceName = None
        self.DeviceStatus = None
        self.DeviceType = None
        self.ModifyTime = None
        self.LastReportTime = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceStatus = params.get("DeviceStatus")
        self.DeviceType = params.get("DeviceType")
        self.ModifyTime = params.get("ModifyTime")
        self.LastReportTime = params.get("LastReportTime")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLicenseRequest(AbstractModel):
    """GetDeviceLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 目标设备所属项目ID
        :type ProjectId: str
        :param DeviceId: 目标设备ID
        :type DeviceId: str
        """
        self.ProjectId = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLicenseResponse(AbstractModel):
    """GetDeviceLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param AvailableCount: 指定设备已经绑定的可用license数量
        :type AvailableCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AvailableCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AvailableCount = params.get("AvailableCount")
        self.RequestId = params.get("RequestId")


class GetDevicesRequest(AbstractModel):
    """GetDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNum: 页码
        :type PageNum: int
        :param PageSize: 页面数量
        :type PageSize: int
        :param ProjectId: 项目 ID
        :type ProjectId: str
        :param DeviceId: 设备ID
        :type DeviceId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.ProjectId = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicesResponse(AbstractModel):
    """GetDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param Devices: 设备授权列表
        :type Devices: list of Device
        :param TotalCount: 列表数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = Device()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GetLicenseStatRequest(AbstractModel):
    """GetLicenseStat请求参数结构体

    """


class GetLicenseStatResponse(AbstractModel):
    """GetLicenseStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param Valid: 有效授权
        :type Valid: int
        :param Bound: 已绑定授权
        :type Bound: int
        :param UnBound: 未绑定授权
        :type UnBound: int
        :param Expire: 过期授权
        :type Expire: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Valid = None
        self.Bound = None
        self.UnBound = None
        self.Expire = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Valid = params.get("Valid")
        self.Bound = params.get("Bound")
        self.UnBound = params.get("UnBound")
        self.Expire = params.get("Expire")
        self.RequestId = params.get("RequestId")


class GetLicensesRequest(AbstractModel):
    """GetLicenses请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageNum: 页码
        :type PageNum: int
        :param PageSize: 页面数量
        :type PageSize: int
        :param ProjectId: projectId
        :type ProjectId: str
        :param DeviceId: DeviceId
        :type DeviceId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.ProjectId = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLicensesResponse(AbstractModel):
    """GetLicenses返回参数结构体

    """

    def __init__(self):
        r"""
        :param Licenses: license列表
        :type Licenses: list of License
        :param TotalCount: license列表项数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Licenses = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Licenses") is not None:
            self.Licenses = []
            for item in params.get("Licenses"):
                obj = License()
                obj._deserialize(item)
                self.Licenses.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class License(AbstractModel):
    """按授权查看的license列表

    """

    def __init__(self):
        r"""
        :param Count: 该类型的license个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param Status: license状态：0:未绑定；1:已绑定；2:已停服；3:已退费
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param ExpireTime: 到期时间戳：s
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param Duration: 服务时长：s
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param RemainDay: 剩余天数：天
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainDay: int
        :param LicenseIds: 该类型的licenseId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseIds: list of str
        """
        self.Count = None
        self.Status = None
        self.ExpireTime = None
        self.Duration = None
        self.RemainDay = None
        self.LicenseIds = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Status = params.get("Status")
        self.ExpireTime = params.get("ExpireTime")
        self.Duration = params.get("Duration")
        self.RemainDay = params.get("RemainDay")
        self.LicenseIds = params.get("LicenseIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 要修改设备归属项目的项目ID
        :type ProjectId: str
        :param DeviceId: 要修改设备的设备ID
        :type DeviceId: str
        :param DeviceName: 修改后的设备名称，不填则不修改
        :type DeviceName: str
        :param DeviceToken: 修改后的设备认证口令，不填则不修改
        :type DeviceToken: str
        """
        self.ProjectId = None
        self.DeviceId = None
        self.DeviceName = None
        self.DeviceToken = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPolicyRequest(AbstractModel):
    """ModifyPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 修改权限配置的项目ID
        :type ProjectId: str
        :param RemoteDeviceId: 修改权限配置的远端设备ID
        :type RemoteDeviceId: str
        :param FieldDeviceIds: 权限修改涉及的现场设备ID数组
        :type FieldDeviceIds: list of str
        :param PolicyMode: 修改的目标权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param ModifyMode: 修改模式，add为新增（添加现场设备I关联），remove为删除（解除现场设备关联），set为设置（更新现场设备关联）
        :type ModifyMode: str
        """
        self.ProjectId = None
        self.RemoteDeviceId = None
        self.FieldDeviceIds = None
        self.PolicyMode = None
        self.ModifyMode = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RemoteDeviceId = params.get("RemoteDeviceId")
        self.FieldDeviceIds = params.get("FieldDeviceIds")
        self.PolicyMode = params.get("PolicyMode")
        self.ModifyMode = params.get("ModifyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyResponse(AbstractModel):
    """ModifyPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailedInsertIds: 添加关联失败的现场设备ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedInsertIds: list of str
        :param FailedDeleteIds: 解除关联失败的现场设备ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedDeleteIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedInsertIds = None
        self.FailedDeleteIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedInsertIds = params.get("FailedInsertIds")
        self.FailedDeleteIds = params.get("FailedDeleteIds")
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 目标修改项目的项目ID
        :type ProjectId: str
        :param ProjectName: 修改后的项目名称，不填则不修改
        :type ProjectName: str
        :param ProjectDescription: 修改后的项目描述，不填则不修改
        :type ProjectDescription: str
        :param PolicyMode: 修改后的权限模式，black为黑名单，white为白名单,不填则不修改
        :type PolicyMode: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDescription = None
        self.PolicyMode = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDescription = params.get("ProjectDescription")
        self.PolicyMode = params.get("PolicyMode")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PolicyInfo(AbstractModel):
    """权限信息

    """

    def __init__(self):
        r"""
        :param RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param FieldDeviceIds: 关联的现场设备ID
        :type FieldDeviceIds: list of str
        :param ModifyTime: 最近添加时间
        :type ModifyTime: str
        """
        self.RemoteDeviceId = None
        self.FieldDeviceIds = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.RemoteDeviceId = params.get("RemoteDeviceId")
        self.FieldDeviceIds = params.get("FieldDeviceIds")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """项目信息

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param ProjectDescription: 项目描述
        :type ProjectDescription: str
        :param PolicyMode: 项目权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param ModifyTime: 项目信息修改时间
        :type ModifyTime: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDescription = None
        self.PolicyMode = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDescription = params.get("ProjectDescription")
        self.PolicyMode = params.get("PolicyMode")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecentSessionInfo(AbstractModel):
    """最新会话信息

    """

    def __init__(self):
        r"""
        :param SessionId: 会话ID
        :type SessionId: str
        :param RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param FieldDeviceId: 现场设备ID
        :type FieldDeviceId: str
        :param Resolution: 分辨率
        :type Resolution: str
        :param StartTime: 会话开始时间
        :type StartTime: int
        :param LatestUpdateTime: 最后更新时间
        :type LatestUpdateTime: int
        """
        self.SessionId = None
        self.RemoteDeviceId = None
        self.FieldDeviceId = None
        self.Resolution = None
        self.StartTime = None
        self.LatestUpdateTime = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.RemoteDeviceId = params.get("RemoteDeviceId")
        self.FieldDeviceId = params.get("FieldDeviceId")
        self.Resolution = params.get("Resolution")
        self.StartTime = params.get("StartTime")
        self.LatestUpdateTime = params.get("LatestUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionDeviceDetail(AbstractModel):
    """会话数据详单（按设备区分）

    """

    def __init__(self):
        r"""
        :param DeviceType: 设备类型：field或remote
        :type DeviceType: str
        :param StartTime: 起始点位时间，单位：秒
        :type StartTime: int
        :param EndTime: 结束点位时间，单位：秒
        :type EndTime: int
        :param SessionId: 会话ID
        :type SessionId: str
        :param Rate: 码率，单位：kbps
        :type Rate: list of int
        :param Fps: 帧率
        :type Fps: list of int
        :param Lost: 丢包率，单位：%
        :type Lost: list of float
        :param NetworkLatency: 网络时延，单位：ms
        :type NetworkLatency: list of int
        :param VideoLatency: 视频时延，单位：ms
        :type VideoLatency: list of int
        :param CpuUsed: CPU使用率，单位：%
        :type CpuUsed: list of float
        :param MemUsed: 内存使用率，单位：%
        :type MemUsed: list of float
        :param TimeOffset: 时间偏移量，单位：秒
        :type TimeOffset: list of int non-negative
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param DeviceId: 设备ID
        :type DeviceId: str
        """
        self.DeviceType = None
        self.StartTime = None
        self.EndTime = None
        self.SessionId = None
        self.Rate = None
        self.Fps = None
        self.Lost = None
        self.NetworkLatency = None
        self.VideoLatency = None
        self.CpuUsed = None
        self.MemUsed = None
        self.TimeOffset = None
        self.ProjectId = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.DeviceType = params.get("DeviceType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SessionId = params.get("SessionId")
        self.Rate = params.get("Rate")
        self.Fps = params.get("Fps")
        self.Lost = params.get("Lost")
        self.NetworkLatency = params.get("NetworkLatency")
        self.VideoLatency = params.get("VideoLatency")
        self.CpuUsed = params.get("CpuUsed")
        self.MemUsed = params.get("MemUsed")
        self.TimeOffset = params.get("TimeOffset")
        self.ProjectId = params.get("ProjectId")
        self.DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionInfo(AbstractModel):
    """会话信息

    """

    def __init__(self):
        r"""
        :param SessionId: 会话ID
        :type SessionId: str
        :param RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param FieldDeviceId: 现场设备ID
        :type FieldDeviceId: str
        :param Resolution: 分辨率
        :type Resolution: str
        :param StartTime: 会话开始时间
        :type StartTime: int
        :param EndTime: 会话结束时间
        :type EndTime: int
        :param Quality: 通话质量：good|normal|bad，对应优良差
        :type Quality: str
        """
        self.SessionId = None
        self.RemoteDeviceId = None
        self.FieldDeviceId = None
        self.Resolution = None
        self.StartTime = None
        self.EndTime = None
        self.Quality = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.RemoteDeviceId = params.get("RemoteDeviceId")
        self.FieldDeviceId = params.get("FieldDeviceId")
        self.Resolution = params.get("Resolution")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionIntervalStatistic(AbstractModel):
    """单位时间间隔的会话统计数据

    """

    def __init__(self):
        r"""
        :param ActiveFieldDeviceNum: 活跃现场设备数
        :type ActiveFieldDeviceNum: int
        :param ActiveRemoteDeviceNum: 活跃远端设备数
        :type ActiveRemoteDeviceNum: int
        :param SessionNum: 会话数量
        :type SessionNum: int
        :param TotalDuration: 会话时长，单位：分钟
        :type TotalDuration: int
        :param StartTime: 时间戳，单位：秒
        :type StartTime: int
        :param EndTime: 时间戳，单位：秒
        :type EndTime: int
        :param NotBadSessionRatio: 优良会话占比，单位：%
        :type NotBadSessionRatio: int
        """
        self.ActiveFieldDeviceNum = None
        self.ActiveRemoteDeviceNum = None
        self.SessionNum = None
        self.TotalDuration = None
        self.StartTime = None
        self.EndTime = None
        self.NotBadSessionRatio = None


    def _deserialize(self, params):
        self.ActiveFieldDeviceNum = params.get("ActiveFieldDeviceNum")
        self.ActiveRemoteDeviceNum = params.get("ActiveRemoteDeviceNum")
        self.SessionNum = params.get("SessionNum")
        self.TotalDuration = params.get("TotalDuration")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NotBadSessionRatio = params.get("NotBadSessionRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        