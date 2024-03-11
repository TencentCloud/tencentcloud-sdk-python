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
        :param _ProjectId: 目标删除设备所属项目ID
        :type ProjectId: str
        :param _DeviceIds: 目标删除设备的设备ID数组
        :type DeviceIds: list of str
        """
        self._ProjectId = None
        self._DeviceIds = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceIds(self):
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteDevicesResponse(AbstractModel):
    """BatchDeleteDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedDeviceIds: 删除失败的设备ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedDeviceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedDeviceIds = None
        self._RequestId = None

    @property
    def FailedDeviceIds(self):
        return self._FailedDeviceIds

    @FailedDeviceIds.setter
    def FailedDeviceIds(self, FailedDeviceIds):
        self._FailedDeviceIds = FailedDeviceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedDeviceIds = params.get("FailedDeviceIds")
        self._RequestId = params.get("RequestId")


class BatchDeletePolicyRequest(AbstractModel):
    """BatchDeletePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 删除权限配置的项目ID
        :type ProjectId: str
        :param _RemoteDeviceIds: 删除权限配置的远端设备ID列表
        :type RemoteDeviceIds: list of str
        :param _PolicyMode: 删除权限配置的权限模式, black为黑名单，white为白名单
        :type PolicyMode: str
        """
        self._ProjectId = None
        self._RemoteDeviceIds = None
        self._PolicyMode = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RemoteDeviceIds(self):
        return self._RemoteDeviceIds

    @RemoteDeviceIds.setter
    def RemoteDeviceIds(self, RemoteDeviceIds):
        self._RemoteDeviceIds = RemoteDeviceIds

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RemoteDeviceIds = params.get("RemoteDeviceIds")
        self._PolicyMode = params.get("PolicyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeletePolicyResponse(AbstractModel):
    """BatchDeletePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedRemoteDeviceIds: 删除权限配置失败的远端设备ID列表
        :type FailedRemoteDeviceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedRemoteDeviceIds = None
        self._RequestId = None

    @property
    def FailedRemoteDeviceIds(self):
        return self._FailedRemoteDeviceIds

    @FailedRemoteDeviceIds.setter
    def FailedRemoteDeviceIds(self, FailedRemoteDeviceIds):
        self._FailedRemoteDeviceIds = FailedRemoteDeviceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedRemoteDeviceIds = params.get("FailedRemoteDeviceIds")
        self._RequestId = params.get("RequestId")


class BoundLicensesRequest(AbstractModel):
    """BoundLicenses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: license数量
        :type Count: int
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._Count = None
        self._DeviceId = None
        self._ProjectId = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._DeviceId = params.get("DeviceId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundLicensesResponse(AbstractModel):
    """BoundLicenses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 创建设备所归属的项目ID
        :type ProjectId: str
        :param _DeviceId: 创建设备ID，项目内需要唯一，由小写英文字母、数字和下划线构成，长度不超过18
        :type DeviceId: str
        :param _DeviceName: 创建设备名称，长度小于24, 可包含中文、数字、英文字母和下划线
        :type DeviceName: str
        :param _DeviceType: 设备类型，field为现场设备（受控设备），remote为远端设备（操控设备），不填默认为field
        :type DeviceType: str
        :param _DeviceToken: 设备认证口令，由大小写英文字母和数字构成，须为16位
        :type DeviceToken: str
        """
        self._ProjectId = None
        self._DeviceId = None
        self._DeviceName = None
        self._DeviceType = None
        self._DeviceToken = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceType = params.get("DeviceType")
        self._DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称，长度不超过24个字符
        :type ProjectName: str
        :param _ProjectDescription: 项目描述，长度不超过120个字符，不填默认为空
        :type ProjectDescription: str
        :param _PolicyMode: 权限模式，black为黑名单，white为白名单，不填默认为black
        :type PolicyMode: str
        """
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID，长度为16位
        :type ProjectId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceInfoRequest(AbstractModel):
    """DescribeDeviceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标设备所属项目ID
        :type ProjectId: str
        :param _DeviceId: 目标设备ID
        :type DeviceId: str
        """
        self._ProjectId = None
        self._DeviceId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceInfoResponse(AbstractModel):
    """DescribeDeviceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceType: 设备类型，field为现场设备（被控方），remote为远端设备（操控方）
        :type DeviceType: str
        :param _DeviceStatus: 设备状态，offline为离线，ready为在线准备，connected为会话中
        :type DeviceStatus: str
        :param _LastReportTime: 设备状态最后更新时间
        :type LastReportTime: str
        :param _ModifyTime: 设备信息最后修改时间
        :type ModifyTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceName = None
        self._DeviceType = None
        self._DeviceStatus = None
        self._LastReportTime = None
        self._ModifyTime = None
        self._RequestId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def DeviceStatus(self):
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus

    @property
    def LastReportTime(self):
        return self._LastReportTime

    @LastReportTime.setter
    def LastReportTime(self, LastReportTime):
        self._LastReportTime = LastReportTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._DeviceType = params.get("DeviceType")
        self._DeviceStatus = params.get("DeviceStatus")
        self._LastReportTime = params.get("LastReportTime")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    """DescribeDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 设备所属项目ID
        :type ProjectId: str
        :param _DeviceType: 设备类型筛选，不填默认为全部设备类型
        :type DeviceType: str
        :param _SearchWords: 对设备ID或Name按关键字进行模糊匹配，不填则不进行模糊匹配
        :type SearchWords: str
        :param _PageSize: 每页返回的最大设备数，不填默认为10
        :type PageSize: int
        :param _PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self._ProjectId = None
        self._DeviceType = None
        self._SearchWords = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def SearchWords(self):
        return self._SearchWords

    @SearchWords.setter
    def SearchWords(self, SearchWords):
        self._SearchWords = SearchWords

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceType = params.get("DeviceType")
        self._SearchWords = params.get("SearchWords")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceListResponse(AbstractModel):
    """DescribeDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 设备信息列表
        :type Devices: list of DeviceInfo
        :param _Total: 设备总数
        :type Total: int
        :param _Num: 本次返回的设备数
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._Total = None
        self._Num = None
        self._RequestId = None

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._Total = params.get("Total")
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribeDeviceSessionDetailsRequest(AbstractModel):
    """DescribeDeviceSessionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceSessionDetailsResponse(AbstractModel):
    """DescribeDeviceSessionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Details: 按设备区分的会话详细数据
        :type Details: list of SessionDeviceDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Details = None
        self._RequestId = None

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = SessionDeviceDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceSessionListRequest(AbstractModel):
    """DescribeDeviceSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PageNumber: 页码，从1开始
        :type PageNumber: int
        :param _PageSize: 每页个数
        :type PageSize: int
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceSessionListResponse(AbstractModel):
    """DescribeDeviceSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总个数
        :type Total: int
        :param _DeviceSessionList: 会话列表
        :type DeviceSessionList: list of SessionInfo
        :param _Num: 本页数量
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DeviceSessionList = None
        self._Num = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DeviceSessionList(self):
        return self._DeviceSessionList

    @DeviceSessionList.setter
    def DeviceSessionList(self, DeviceSessionList):
        self._DeviceSessionList = DeviceSessionList

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DeviceSessionList") is not None:
            self._DeviceSessionList = []
            for item in params.get("DeviceSessionList"):
                obj = SessionInfo()
                obj._deserialize(item)
                self._DeviceSessionList.append(obj)
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribePolicyRequest(AbstractModel):
    """DescribePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 查看权限的项目ID
        :type ProjectId: str
        :param _PolicyMode: 查看的权限模式，black为黑名单，white为白名单，不填默认为当前项目生效的权限模式
        :type PolicyMode: str
        :param _SearchMode: 模糊匹配模式，remoteMatch为远端设备ID匹配，fieldMatch为现场ID匹配，不填默认为remoteMatch
        :type SearchMode: str
        :param _SearchWords: 模糊匹配关键字，不填默认不进行模糊匹配
        :type SearchWords: str
        :param _PageSize: 每页返回的最大数量，不填默认为10
        :type PageSize: int
        :param _PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self._ProjectId = None
        self._PolicyMode = None
        self._SearchMode = None
        self._SearchWords = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def SearchMode(self):
        return self._SearchMode

    @SearchMode.setter
    def SearchMode(self, SearchMode):
        self._SearchMode = SearchMode

    @property
    def SearchWords(self):
        return self._SearchWords

    @SearchWords.setter
    def SearchWords(self, SearchWords):
        self._SearchWords = SearchWords

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PolicyMode = params.get("PolicyMode")
        self._SearchMode = params.get("SearchMode")
        self._SearchWords = params.get("SearchWords")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyResponse(AbstractModel):
    """DescribePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyMode: 权限模式
        :type PolicyMode: str
        :param _PolicyEnabled: 返回的权限模式是否为当前生效的权限模式
        :type PolicyEnabled: bool
        :param _PolicyInfo: 权限信息列表
        :type PolicyInfo: list of PolicyInfo
        :param _Num: 本次返回的权限信息数量
        :type Num: int
        :param _Total: 权限信息总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyMode = None
        self._PolicyEnabled = None
        self._PolicyInfo = None
        self._Num = None
        self._Total = None
        self._RequestId = None

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def PolicyEnabled(self):
        return self._PolicyEnabled

    @PolicyEnabled.setter
    def PolicyEnabled(self, PolicyEnabled):
        self._PolicyEnabled = PolicyEnabled

    @property
    def PolicyInfo(self):
        return self._PolicyInfo

    @PolicyInfo.setter
    def PolicyInfo(self, PolicyInfo):
        self._PolicyInfo = PolicyInfo

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PolicyMode = params.get("PolicyMode")
        self._PolicyEnabled = params.get("PolicyEnabled")
        if params.get("PolicyInfo") is not None:
            self._PolicyInfo = []
            for item in params.get("PolicyInfo"):
                obj = PolicyInfo()
                obj._deserialize(item)
                self._PolicyInfo.append(obj)
        self._Num = params.get("Num")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProjectInfoRequest(AbstractModel):
    """DescribeProjectInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectInfoResponse(AbstractModel):
    """DescribeProjectInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDescription: 项目描述
        :type ProjectDescription: str
        :param _PolicyMode: 项目权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param _ModifyTime: 项目信息修改时间
        :type ModifyTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None
        self._ModifyTime = None
        self._RequestId = None

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestId = params.get("RequestId")


class DescribeProjectListRequest(AbstractModel):
    """DescribeProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页返回的最大项目数量，不填默认为10
        :type PageSize: int
        :param _PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self._PageSize = None
        self._PageNumber = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectListResponse(AbstractModel):
    """DescribeProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Projects: 项目信息数组
        :type Projects: list of ProjectInfo
        :param _Total: 项目总数
        :type Total: int
        :param _Num: 本次返回的项目数
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Projects = None
        self._Total = None
        self._Num = None
        self._RequestId = None

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._Total = params.get("Total")
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribeRecentSessionListRequest(AbstractModel):
    """DescribeRecentSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PageNumber: 页码，从1开始
        :type PageNumber: int
        :param _PageSize: 每页个数
        :type PageSize: int
        :param _DeviceId: 设备ID，支持过滤远端设备或现场设备
        :type DeviceId: str
        :param _StartTime: 时间范围的起始时间。时间范围最大为最近两小时，若不传或超出范围，则起始时间按两小时前计算
        :type StartTime: int
        :param _EndTime: 时间范围的结束时间。时间范围最大为最近两小时，若不传或超出范围，则结束时间按当前时间计算
        :type EndTime: int
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecentSessionListResponse(AbstractModel):
    """DescribeRecentSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总个数
        :type Total: int
        :param _RecentSessionList: 会话列表
        :type RecentSessionList: list of RecentSessionInfo
        :param _Num: 本页数量
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RecentSessionList = None
        self._Num = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RecentSessionList(self):
        return self._RecentSessionList

    @RecentSessionList.setter
    def RecentSessionList(self, RecentSessionList):
        self._RecentSessionList = RecentSessionList

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("RecentSessionList") is not None:
            self._RecentSessionList = []
            for item in params.get("RecentSessionList"):
                obj = RecentSessionInfo()
                obj._deserialize(item)
                self._RecentSessionList.append(obj)
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribeSessionStatisticsByIntervalRequest(AbstractModel):
    """DescribeSessionStatisticsByInterval请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _StatisticInterval: 统计时间间隔：hour|day|month
        :type StatisticInterval: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param _EndTime: 结束时间，单位：秒
        :type EndTime: int
        """
        self._ProjectId = None
        self._StatisticInterval = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def StatisticInterval(self):
        return self._StatisticInterval

    @StatisticInterval.setter
    def StatisticInterval(self, StatisticInterval):
        self._StatisticInterval = StatisticInterval

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._StatisticInterval = params.get("StatisticInterval")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionStatisticsByIntervalResponse(AbstractModel):
    """DescribeSessionStatisticsByInterval返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionStatistics: 各时间段的会话统计数据
        :type SessionStatistics: list of SessionIntervalStatistic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionStatistics = None
        self._RequestId = None

    @property
    def SessionStatistics(self):
        return self._SessionStatistics

    @SessionStatistics.setter
    def SessionStatistics(self, SessionStatistics):
        self._SessionStatistics = SessionStatistics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SessionStatistics") is not None:
            self._SessionStatistics = []
            for item in params.get("SessionStatistics"):
                obj = SessionIntervalStatistic()
                obj._deserialize(item)
                self._SessionStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSessionStatisticsRequest(AbstractModel):
    """DescribeSessionStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param _EndTime: 结束时间，单位：秒
        :type EndTime: int
        """
        self._ProjectId = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionStatisticsResponse(AbstractModel):
    """DescribeSessionStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionNum: 会话数量
        :type SessionNum: int
        :param _TotalDuration: 通话时长，单位：分钟
        :type TotalDuration: int
        :param _ActiveFieldDeviceNum: 活跃现场设备数
        :type ActiveFieldDeviceNum: int
        :param _ActiveRemoteDeviceNum: 活跃远端设备数
        :type ActiveRemoteDeviceNum: int
        :param _NotBadSessionRatio: 优良会话占比，单位：%
        :type NotBadSessionRatio: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionNum = None
        self._TotalDuration = None
        self._ActiveFieldDeviceNum = None
        self._ActiveRemoteDeviceNum = None
        self._NotBadSessionRatio = None
        self._RequestId = None

    @property
    def SessionNum(self):
        return self._SessionNum

    @SessionNum.setter
    def SessionNum(self, SessionNum):
        self._SessionNum = SessionNum

    @property
    def TotalDuration(self):
        return self._TotalDuration

    @TotalDuration.setter
    def TotalDuration(self, TotalDuration):
        self._TotalDuration = TotalDuration

    @property
    def ActiveFieldDeviceNum(self):
        return self._ActiveFieldDeviceNum

    @ActiveFieldDeviceNum.setter
    def ActiveFieldDeviceNum(self, ActiveFieldDeviceNum):
        self._ActiveFieldDeviceNum = ActiveFieldDeviceNum

    @property
    def ActiveRemoteDeviceNum(self):
        return self._ActiveRemoteDeviceNum

    @ActiveRemoteDeviceNum.setter
    def ActiveRemoteDeviceNum(self, ActiveRemoteDeviceNum):
        self._ActiveRemoteDeviceNum = ActiveRemoteDeviceNum

    @property
    def NotBadSessionRatio(self):
        return self._NotBadSessionRatio

    @NotBadSessionRatio.setter
    def NotBadSessionRatio(self, NotBadSessionRatio):
        self._NotBadSessionRatio = NotBadSessionRatio

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionNum = params.get("SessionNum")
        self._TotalDuration = params.get("TotalDuration")
        self._ActiveFieldDeviceNum = params.get("ActiveFieldDeviceNum")
        self._ActiveRemoteDeviceNum = params.get("ActiveRemoteDeviceNum")
        self._NotBadSessionRatio = params.get("NotBadSessionRatio")
        self._RequestId = params.get("RequestId")


class Device(AbstractModel):
    """查询用户设备的授权绑定情况

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceId: str
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _LicenseCount: 已经绑定license数量
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseCount: int
        :param _RemainDay: 剩余天数：天
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainDay: int
        :param _ExpireTime: 过期时间：s
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _Duration: 服务时长：s
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _LicenseIds: 已经绑定licenseId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseIds: list of str
        :param _MonthlyRemainTime: 每月license的限定时长
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthlyRemainTime: int
        """
        self._DeviceId = None
        self._DeviceName = None
        self._LicenseCount = None
        self._RemainDay = None
        self._ExpireTime = None
        self._Duration = None
        self._LicenseIds = None
        self._MonthlyRemainTime = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LicenseCount(self):
        return self._LicenseCount

    @LicenseCount.setter
    def LicenseCount(self, LicenseCount):
        self._LicenseCount = LicenseCount

    @property
    def RemainDay(self):
        return self._RemainDay

    @RemainDay.setter
    def RemainDay(self, RemainDay):
        self._RemainDay = RemainDay

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def LicenseIds(self):
        return self._LicenseIds

    @LicenseIds.setter
    def LicenseIds(self, LicenseIds):
        self._LicenseIds = LicenseIds

    @property
    def MonthlyRemainTime(self):
        return self._MonthlyRemainTime

    @MonthlyRemainTime.setter
    def MonthlyRemainTime(self, MonthlyRemainTime):
        self._MonthlyRemainTime = MonthlyRemainTime


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._LicenseCount = params.get("LicenseCount")
        self._RemainDay = params.get("RemainDay")
        self._ExpireTime = params.get("ExpireTime")
        self._Duration = params.get("Duration")
        self._LicenseIds = params.get("LicenseIds")
        self._MonthlyRemainTime = params.get("MonthlyRemainTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceStatus: 设备状态，offline为离线，ready为在线准备，connected为会话中
        :type DeviceStatus: str
        :param _DeviceType: 设备类型，field为现场设备（受控方），remote为远端设备（操控方）
        :type DeviceType: str
        :param _ModifyTime: 设备信息最近修改时间
        :type ModifyTime: str
        :param _LastReportTime: 设备状态最近更新时间
        :type LastReportTime: str
        :param _ProjectId: 设备所属项目Id
        :type ProjectId: str
        """
        self._DeviceId = None
        self._DeviceName = None
        self._DeviceStatus = None
        self._DeviceType = None
        self._ModifyTime = None
        self._LastReportTime = None
        self._ProjectId = None

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceStatus(self):
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def LastReportTime(self):
        return self._LastReportTime

    @LastReportTime.setter
    def LastReportTime(self, LastReportTime):
        self._LastReportTime = LastReportTime

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceStatus = params.get("DeviceStatus")
        self._DeviceType = params.get("DeviceType")
        self._ModifyTime = params.get("ModifyTime")
        self._LastReportTime = params.get("LastReportTime")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLicenseRequest(AbstractModel):
    """GetDeviceLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标设备所属项目ID
        :type ProjectId: str
        :param _DeviceId: 目标设备ID
        :type DeviceId: str
        """
        self._ProjectId = None
        self._DeviceId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLicenseResponse(AbstractModel):
    """GetDeviceLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableCount: 指定设备已经绑定的可用license数量
        :type AvailableCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableCount = None
        self._RequestId = None

    @property
    def AvailableCount(self):
        return self._AvailableCount

    @AvailableCount.setter
    def AvailableCount(self, AvailableCount):
        self._AvailableCount = AvailableCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AvailableCount = params.get("AvailableCount")
        self._RequestId = params.get("RequestId")


class GetDevicesRequest(AbstractModel):
    """GetDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 页码
        :type PageNum: int
        :param _PageSize: 页面数量
        :type PageSize: int
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        """
        self._PageNum = None
        self._PageSize = None
        self._ProjectId = None
        self._DeviceId = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicesResponse(AbstractModel):
    """GetDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 设备授权列表
        :type Devices: list of Device
        :param _TotalCount: 列表数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = Device()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetLicenseStatRequest(AbstractModel):
    """GetLicenseStat请求参数结构体

    """


class GetLicenseStatResponse(AbstractModel):
    """GetLicenseStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Valid: 有效授权
        :type Valid: int
        :param _Bound: 已绑定授权
        :type Bound: int
        :param _UnBound: 未绑定授权
        :type UnBound: int
        :param _Expire: 过期授权
        :type Expire: int
        :param _MonthlyExpire: 当月用量超时授权个数
        :type MonthlyExpire: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Valid = None
        self._Bound = None
        self._UnBound = None
        self._Expire = None
        self._MonthlyExpire = None
        self._RequestId = None

    @property
    def Valid(self):
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid

    @property
    def Bound(self):
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def UnBound(self):
        return self._UnBound

    @UnBound.setter
    def UnBound(self, UnBound):
        self._UnBound = UnBound

    @property
    def Expire(self):
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def MonthlyExpire(self):
        return self._MonthlyExpire

    @MonthlyExpire.setter
    def MonthlyExpire(self, MonthlyExpire):
        self._MonthlyExpire = MonthlyExpire

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Valid = params.get("Valid")
        self._Bound = params.get("Bound")
        self._UnBound = params.get("UnBound")
        self._Expire = params.get("Expire")
        self._MonthlyExpire = params.get("MonthlyExpire")
        self._RequestId = params.get("RequestId")


class GetLicensesRequest(AbstractModel):
    """GetLicenses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 页码
        :type PageNum: int
        :param _PageSize: 页面数量
        :type PageSize: int
        :param _ProjectId: projectId
        :type ProjectId: str
        :param _DeviceId: DeviceId
        :type DeviceId: str
        :param _Status: license状态：0:未绑定；1:已绑定；2:已停服；3:已退费
        :type Status: int
        """
        self._PageNum = None
        self._PageSize = None
        self._ProjectId = None
        self._DeviceId = None
        self._Status = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLicensesResponse(AbstractModel):
    """GetLicenses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Licenses: license列表
        :type Licenses: list of License
        :param _TotalCount: license列表项数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Licenses = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Licenses(self):
        return self._Licenses

    @Licenses.setter
    def Licenses(self, Licenses):
        self._Licenses = Licenses

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Licenses") is not None:
            self._Licenses = []
            for item in params.get("Licenses"):
                obj = License()
                obj._deserialize(item)
                self._Licenses.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class License(AbstractModel):
    """按授权查看的license列表

    """

    def __init__(self):
        r"""
        :param _Count: 该类型的license个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Status: license状态：0:未绑定；1:已绑定；2:已停服；3:已退费
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _ExpireTime: 到期时间戳：s
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _Duration: 服务时长：s
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _RemainDay: 剩余天数：天
注意：此字段可能返回 null，表示取不到有效值。
        :type RemainDay: int
        :param _LicenseIds: 该类型的licenseId列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseIds: list of str
        """
        self._Count = None
        self._Status = None
        self._ExpireTime = None
        self._Duration = None
        self._RemainDay = None
        self._LicenseIds = None

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RemainDay(self):
        return self._RemainDay

    @RemainDay.setter
    def RemainDay(self, RemainDay):
        self._RemainDay = RemainDay

    @property
    def LicenseIds(self):
        return self._LicenseIds

    @LicenseIds.setter
    def LicenseIds(self, LicenseIds):
        self._LicenseIds = LicenseIds


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._Duration = params.get("Duration")
        self._RemainDay = params.get("RemainDay")
        self._LicenseIds = params.get("LicenseIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 要修改设备归属项目的项目ID
        :type ProjectId: str
        :param _DeviceId: 要修改设备的设备ID
        :type DeviceId: str
        :param _DeviceName: 修改后的设备名称，不填则不修改
        :type DeviceName: str
        :param _DeviceToken: 修改后的设备认证口令，不填则不修改
        :type DeviceToken: str
        """
        self._ProjectId = None
        self._DeviceId = None
        self._DeviceName = None
        self._DeviceToken = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceToken(self):
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPolicyRequest(AbstractModel):
    """ModifyPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 修改权限配置的项目ID
        :type ProjectId: str
        :param _RemoteDeviceId: 修改权限配置的远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceIds: 权限修改涉及的现场设备ID数组
        :type FieldDeviceIds: list of str
        :param _PolicyMode: 修改的目标权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param _ModifyMode: 修改模式，add为新增（添加现场设备I关联），remove为删除（解除现场设备关联），set为设置（更新现场设备关联）
        :type ModifyMode: str
        """
        self._ProjectId = None
        self._RemoteDeviceId = None
        self._FieldDeviceIds = None
        self._PolicyMode = None
        self._ModifyMode = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RemoteDeviceId(self):
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceIds(self):
        return self._FieldDeviceIds

    @FieldDeviceIds.setter
    def FieldDeviceIds(self, FieldDeviceIds):
        self._FieldDeviceIds = FieldDeviceIds

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def ModifyMode(self):
        return self._ModifyMode

    @ModifyMode.setter
    def ModifyMode(self, ModifyMode):
        self._ModifyMode = ModifyMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceIds = params.get("FieldDeviceIds")
        self._PolicyMode = params.get("PolicyMode")
        self._ModifyMode = params.get("ModifyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyResponse(AbstractModel):
    """ModifyPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedInsertIds: 添加关联失败的现场设备ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedInsertIds: list of str
        :param _FailedDeleteIds: 解除关联失败的现场设备ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedDeleteIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedInsertIds = None
        self._FailedDeleteIds = None
        self._RequestId = None

    @property
    def FailedInsertIds(self):
        return self._FailedInsertIds

    @FailedInsertIds.setter
    def FailedInsertIds(self, FailedInsertIds):
        self._FailedInsertIds = FailedInsertIds

    @property
    def FailedDeleteIds(self):
        return self._FailedDeleteIds

    @FailedDeleteIds.setter
    def FailedDeleteIds(self, FailedDeleteIds):
        self._FailedDeleteIds = FailedDeleteIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedInsertIds = params.get("FailedInsertIds")
        self._FailedDeleteIds = params.get("FailedDeleteIds")
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标修改项目的项目ID
        :type ProjectId: str
        :param _ProjectName: 修改后的项目名称，不填则不修改
        :type ProjectName: str
        :param _ProjectDescription: 修改后的项目描述，不填则不修改
        :type ProjectDescription: str
        :param _PolicyMode: 修改后的权限模式，black为黑名单，white为白名单,不填则不修改
        :type PolicyMode: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PolicyInfo(AbstractModel):
    """权限信息

    """

    def __init__(self):
        r"""
        :param _RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceIds: 关联的现场设备ID
        :type FieldDeviceIds: list of str
        :param _ModifyTime: 最近添加时间
        :type ModifyTime: str
        """
        self._RemoteDeviceId = None
        self._FieldDeviceIds = None
        self._ModifyTime = None

    @property
    def RemoteDeviceId(self):
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceIds(self):
        return self._FieldDeviceIds

    @FieldDeviceIds.setter
    def FieldDeviceIds(self, FieldDeviceIds):
        self._FieldDeviceIds = FieldDeviceIds

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceIds = params.get("FieldDeviceIds")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """项目信息

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDescription: 项目描述
        :type ProjectDescription: str
        :param _PolicyMode: 项目权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param _ModifyTime: 项目信息修改时间
        :type ModifyTime: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None
        self._ModifyTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecentSessionInfo(AbstractModel):
    """最新会话信息

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceId: 现场设备ID
        :type FieldDeviceId: str
        :param _Resolution: 分辨率
        :type Resolution: str
        :param _StartTime: 会话开始时间
        :type StartTime: int
        :param _LatestUpdateTime: 最后更新时间
        :type LatestUpdateTime: int
        """
        self._SessionId = None
        self._RemoteDeviceId = None
        self._FieldDeviceId = None
        self._Resolution = None
        self._StartTime = None
        self._LatestUpdateTime = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RemoteDeviceId(self):
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceId(self):
        return self._FieldDeviceId

    @FieldDeviceId.setter
    def FieldDeviceId(self, FieldDeviceId):
        self._FieldDeviceId = FieldDeviceId

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def LatestUpdateTime(self):
        return self._LatestUpdateTime

    @LatestUpdateTime.setter
    def LatestUpdateTime(self, LatestUpdateTime):
        self._LatestUpdateTime = LatestUpdateTime


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceId = params.get("FieldDeviceId")
        self._Resolution = params.get("Resolution")
        self._StartTime = params.get("StartTime")
        self._LatestUpdateTime = params.get("LatestUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionDeviceDetail(AbstractModel):
    """会话数据详单（按设备区分）

    """

    def __init__(self):
        r"""
        :param _DeviceType: 设备类型：field或remote
        :type DeviceType: str
        :param _StartTime: 起始点位时间，单位：秒
        :type StartTime: int
        :param _EndTime: 结束点位时间，单位：秒
        :type EndTime: int
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _Rate: 码率，单位：kbps
        :type Rate: list of int
        :param _Fps: 帧率
        :type Fps: list of int
        :param _Lost: 丢包率，单位：%
        :type Lost: list of float
        :param _NetworkLatency: 网络时延，单位：ms
        :type NetworkLatency: list of int
        :param _VideoLatency: 视频时延，单位：ms
        :type VideoLatency: list of int
        :param _CpuUsed: CPU使用率，单位：%
        :type CpuUsed: list of float
        :param _MemUsed: 内存使用率，单位：%
        :type MemUsed: list of float
        :param _TimeOffset: 时间偏移量，单位：秒
        :type TimeOffset: list of int non-negative
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _Ver: sdk版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Ver: str
        :param _SdkMode: 模式(p2p/server)
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkMode: str
        :param _DecodeCost: 解码耗时，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type DecodeCost: list of int
        :param _RenderConst: 渲染耗时，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type RenderConst: list of int
        :param _K100: 卡顿k100
注意：此字段可能返回 null，表示取不到有效值。
        :type K100: list of float
        :param _K150: 卡顿k150
注意：此字段可能返回 null，表示取不到有效值。
        :type K150: list of float
        :param _NACK: nack请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type NACK: list of int
        :param _BitRateEstimate: 服务端调控码率,单位：kbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BitRateEstimate: list of int
        :param _Width: 宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _EncodeCost: 编码耗时，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type EncodeCost: list of int
        :param _CaptureCost: 采集耗时，单位：ms
注意：此字段可能返回 null，表示取不到有效值。
        :type CaptureCost: list of int
        """
        self._DeviceType = None
        self._StartTime = None
        self._EndTime = None
        self._SessionId = None
        self._Rate = None
        self._Fps = None
        self._Lost = None
        self._NetworkLatency = None
        self._VideoLatency = None
        self._CpuUsed = None
        self._MemUsed = None
        self._TimeOffset = None
        self._ProjectId = None
        self._DeviceId = None
        self._Ver = None
        self._SdkMode = None
        self._DecodeCost = None
        self._RenderConst = None
        self._K100 = None
        self._K150 = None
        self._NACK = None
        self._BitRateEstimate = None
        self._Width = None
        self._Height = None
        self._EncodeCost = None
        self._CaptureCost = None

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Lost(self):
        return self._Lost

    @Lost.setter
    def Lost(self, Lost):
        self._Lost = Lost

    @property
    def NetworkLatency(self):
        return self._NetworkLatency

    @NetworkLatency.setter
    def NetworkLatency(self, NetworkLatency):
        self._NetworkLatency = NetworkLatency

    @property
    def VideoLatency(self):
        return self._VideoLatency

    @VideoLatency.setter
    def VideoLatency(self, VideoLatency):
        self._VideoLatency = VideoLatency

    @property
    def CpuUsed(self):
        return self._CpuUsed

    @CpuUsed.setter
    def CpuUsed(self, CpuUsed):
        self._CpuUsed = CpuUsed

    @property
    def MemUsed(self):
        return self._MemUsed

    @MemUsed.setter
    def MemUsed(self, MemUsed):
        self._MemUsed = MemUsed

    @property
    def TimeOffset(self):
        return self._TimeOffset

    @TimeOffset.setter
    def TimeOffset(self, TimeOffset):
        self._TimeOffset = TimeOffset

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Ver(self):
        return self._Ver

    @Ver.setter
    def Ver(self, Ver):
        self._Ver = Ver

    @property
    def SdkMode(self):
        return self._SdkMode

    @SdkMode.setter
    def SdkMode(self, SdkMode):
        self._SdkMode = SdkMode

    @property
    def DecodeCost(self):
        return self._DecodeCost

    @DecodeCost.setter
    def DecodeCost(self, DecodeCost):
        self._DecodeCost = DecodeCost

    @property
    def RenderConst(self):
        return self._RenderConst

    @RenderConst.setter
    def RenderConst(self, RenderConst):
        self._RenderConst = RenderConst

    @property
    def K100(self):
        return self._K100

    @K100.setter
    def K100(self, K100):
        self._K100 = K100

    @property
    def K150(self):
        return self._K150

    @K150.setter
    def K150(self, K150):
        self._K150 = K150

    @property
    def NACK(self):
        return self._NACK

    @NACK.setter
    def NACK(self, NACK):
        self._NACK = NACK

    @property
    def BitRateEstimate(self):
        return self._BitRateEstimate

    @BitRateEstimate.setter
    def BitRateEstimate(self, BitRateEstimate):
        self._BitRateEstimate = BitRateEstimate

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def EncodeCost(self):
        return self._EncodeCost

    @EncodeCost.setter
    def EncodeCost(self, EncodeCost):
        self._EncodeCost = EncodeCost

    @property
    def CaptureCost(self):
        return self._CaptureCost

    @CaptureCost.setter
    def CaptureCost(self, CaptureCost):
        self._CaptureCost = CaptureCost


    def _deserialize(self, params):
        self._DeviceType = params.get("DeviceType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SessionId = params.get("SessionId")
        self._Rate = params.get("Rate")
        self._Fps = params.get("Fps")
        self._Lost = params.get("Lost")
        self._NetworkLatency = params.get("NetworkLatency")
        self._VideoLatency = params.get("VideoLatency")
        self._CpuUsed = params.get("CpuUsed")
        self._MemUsed = params.get("MemUsed")
        self._TimeOffset = params.get("TimeOffset")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._Ver = params.get("Ver")
        self._SdkMode = params.get("SdkMode")
        self._DecodeCost = params.get("DecodeCost")
        self._RenderConst = params.get("RenderConst")
        self._K100 = params.get("K100")
        self._K150 = params.get("K150")
        self._NACK = params.get("NACK")
        self._BitRateEstimate = params.get("BitRateEstimate")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._EncodeCost = params.get("EncodeCost")
        self._CaptureCost = params.get("CaptureCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionInfo(AbstractModel):
    """会话信息

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceId: 现场设备ID
        :type FieldDeviceId: str
        :param _Resolution: 分辨率
        :type Resolution: str
        :param _StartTime: 会话开始时间
        :type StartTime: int
        :param _EndTime: 会话结束时间
        :type EndTime: int
        :param _Quality: 通话质量：good|normal|bad，对应优良差
        :type Quality: str
        """
        self._SessionId = None
        self._RemoteDeviceId = None
        self._FieldDeviceId = None
        self._Resolution = None
        self._StartTime = None
        self._EndTime = None
        self._Quality = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RemoteDeviceId(self):
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceId(self):
        return self._FieldDeviceId

    @FieldDeviceId.setter
    def FieldDeviceId(self, FieldDeviceId):
        self._FieldDeviceId = FieldDeviceId

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Quality(self):
        return self._Quality

    @Quality.setter
    def Quality(self, Quality):
        self._Quality = Quality


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceId = params.get("FieldDeviceId")
        self._Resolution = params.get("Resolution")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionIntervalStatistic(AbstractModel):
    """单位时间间隔的会话统计数据

    """

    def __init__(self):
        r"""
        :param _ActiveFieldDeviceNum: 活跃现场设备数
        :type ActiveFieldDeviceNum: int
        :param _ActiveRemoteDeviceNum: 活跃远端设备数
        :type ActiveRemoteDeviceNum: int
        :param _SessionNum: 会话数量
        :type SessionNum: int
        :param _TotalDuration: 会话时长，单位：分钟
        :type TotalDuration: int
        :param _StartTime: 时间戳，单位：秒
        :type StartTime: int
        :param _EndTime: 时间戳，单位：秒
        :type EndTime: int
        :param _NotBadSessionRatio: 优良会话占比，单位：%
        :type NotBadSessionRatio: int
        """
        self._ActiveFieldDeviceNum = None
        self._ActiveRemoteDeviceNum = None
        self._SessionNum = None
        self._TotalDuration = None
        self._StartTime = None
        self._EndTime = None
        self._NotBadSessionRatio = None

    @property
    def ActiveFieldDeviceNum(self):
        return self._ActiveFieldDeviceNum

    @ActiveFieldDeviceNum.setter
    def ActiveFieldDeviceNum(self, ActiveFieldDeviceNum):
        self._ActiveFieldDeviceNum = ActiveFieldDeviceNum

    @property
    def ActiveRemoteDeviceNum(self):
        return self._ActiveRemoteDeviceNum

    @ActiveRemoteDeviceNum.setter
    def ActiveRemoteDeviceNum(self, ActiveRemoteDeviceNum):
        self._ActiveRemoteDeviceNum = ActiveRemoteDeviceNum

    @property
    def SessionNum(self):
        return self._SessionNum

    @SessionNum.setter
    def SessionNum(self, SessionNum):
        self._SessionNum = SessionNum

    @property
    def TotalDuration(self):
        return self._TotalDuration

    @TotalDuration.setter
    def TotalDuration(self, TotalDuration):
        self._TotalDuration = TotalDuration

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NotBadSessionRatio(self):
        return self._NotBadSessionRatio

    @NotBadSessionRatio.setter
    def NotBadSessionRatio(self, NotBadSessionRatio):
        self._NotBadSessionRatio = NotBadSessionRatio


    def _deserialize(self, params):
        self._ActiveFieldDeviceNum = params.get("ActiveFieldDeviceNum")
        self._ActiveRemoteDeviceNum = params.get("ActiveRemoteDeviceNum")
        self._SessionNum = params.get("SessionNum")
        self._TotalDuration = params.get("TotalDuration")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NotBadSessionRatio = params.get("NotBadSessionRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        