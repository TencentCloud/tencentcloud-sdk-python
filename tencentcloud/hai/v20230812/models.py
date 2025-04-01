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


class ApplicationInfo(AbstractModel):
    """应用信息

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用id

        :type ApplicationId: str
        :param _ApplicationName: 应用名称
        :type ApplicationName: str
        :param _Description: 应用描述

        :type Description: str
        :param _ConfigEnvironment: 应用的环境配置
        :type ConfigEnvironment: str
        :param _MinSystemDiskSize: 系统盘大小下限
        :type MinSystemDiskSize: int
        :param _ApplicationType: 应用类型，目前该项取值可以为PRIVATE_APPLICATION或者PUBLIC_APPLICATION
        :type ApplicationType: str
        :param _ApplicationState: 应用状态：CREATING-创建中；ONLINE -正常在线；DELETING -删除中；ARREARS - 欠费隔离
示例值：ONLINE
        :type ApplicationState: str
        :param _CreateTime: 应用创建时间
        :type CreateTime: str
        :param _ApplicationSize: 应用大小
        :type ApplicationSize: int
        """
        self._ApplicationId = None
        self._ApplicationName = None
        self._Description = None
        self._ConfigEnvironment = None
        self._MinSystemDiskSize = None
        self._ApplicationType = None
        self._ApplicationState = None
        self._CreateTime = None
        self._ApplicationSize = None

    @property
    def ApplicationId(self):
        """应用id

        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """应用名称
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Description(self):
        """应用描述

        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConfigEnvironment(self):
        """应用的环境配置
        :rtype: str
        """
        return self._ConfigEnvironment

    @ConfigEnvironment.setter
    def ConfigEnvironment(self, ConfigEnvironment):
        self._ConfigEnvironment = ConfigEnvironment

    @property
    def MinSystemDiskSize(self):
        """系统盘大小下限
        :rtype: int
        """
        return self._MinSystemDiskSize

    @MinSystemDiskSize.setter
    def MinSystemDiskSize(self, MinSystemDiskSize):
        self._MinSystemDiskSize = MinSystemDiskSize

    @property
    def ApplicationType(self):
        """应用类型，目前该项取值可以为PRIVATE_APPLICATION或者PUBLIC_APPLICATION
        :rtype: str
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationState(self):
        """应用状态：CREATING-创建中；ONLINE -正常在线；DELETING -删除中；ARREARS - 欠费隔离
示例值：ONLINE
        :rtype: str
        """
        return self._ApplicationState

    @ApplicationState.setter
    def ApplicationState(self, ApplicationState):
        self._ApplicationState = ApplicationState

    @property
    def CreateTime(self):
        """应用创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ApplicationSize(self):
        """应用大小
        :rtype: int
        """
        return self._ApplicationSize

    @ApplicationSize.setter
    def ApplicationSize(self, ApplicationSize):
        self._ApplicationSize = ApplicationSize


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._Description = params.get("Description")
        self._ConfigEnvironment = params.get("ConfigEnvironment")
        self._MinSystemDiskSize = params.get("MinSystemDiskSize")
        self._ApplicationType = params.get("ApplicationType")
        self._ApplicationState = params.get("ApplicationState")
        self._CreateTime = params.get("CreateTime")
        self._ApplicationSize = params.get("ApplicationSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMuskPromptRequest(AbstractModel):
    """CreateMuskPrompt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkgroupId: workgroup id
        :type WorkgroupId: str
        :param _WorkflowId: workflow id
        :type WorkflowId: str
        :param _PromptParams: prompt 参数
        :type PromptParams: str
        """
        self._WorkgroupId = None
        self._WorkflowId = None
        self._PromptParams = None

    @property
    def WorkgroupId(self):
        """workgroup id
        :rtype: str
        """
        return self._WorkgroupId

    @WorkgroupId.setter
    def WorkgroupId(self, WorkgroupId):
        self._WorkgroupId = WorkgroupId

    @property
    def WorkflowId(self):
        """workflow id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def PromptParams(self):
        """prompt 参数
        :rtype: str
        """
        return self._PromptParams

    @PromptParams.setter
    def PromptParams(self, PromptParams):
        self._PromptParams = PromptParams


    def _deserialize(self, params):
        self._WorkgroupId = params.get("WorkgroupId")
        self._WorkflowId = params.get("WorkflowId")
        self._PromptParams = params.get("PromptParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMuskPromptResponse(AbstractModel):
    """CreateMuskPrompt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PromptId: prompt id
        :type PromptId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PromptId = None
        self._RequestId = None

    @property
    def PromptId(self):
        """prompt id
        :rtype: str
        """
        return self._PromptId

    @PromptId.setter
    def PromptId(self, PromptId):
        self._PromptId = PromptId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PromptId = params.get("PromptId")
        self._RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationIds: 应用id列表
        :type ApplicationIds: list of str
        :param _Filters: 过滤器，跟ApplicationIds不能共用，支持的filter主要有：
application-id: 精确匹配;
scene-id: 精确匹配;
application-name: 模糊匹配;
application-type: 精确匹配;
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回量，默认为20
MC：1000
用户：100

        :type Limit: int
        :param _OrderField: 应用列表排序的依据字段。取值范围："CREATED_TIME"：依据应用的创建时间排序。 "APPLICATION_SIZE"：依据应用的大小排序。默认按应用的创建时间排序。
        :type OrderField: str
        :param _Order: 输出应用列表的排列顺序。取值范围："ASC"：升序排列。 "DESC"：降序排列。默认按降序排列。
        :type Order: str
        """
        self._ApplicationIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None

    @property
    def ApplicationIds(self):
        """应用id列表
        :rtype: list of str
        """
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

    @property
    def Filters(self):
        """过滤器，跟ApplicationIds不能共用，支持的filter主要有：
application-id: 精确匹配;
scene-id: 精确匹配;
application-name: 模糊匹配;
application-type: 精确匹配;
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回量，默认为20
MC：1000
用户：100

        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        """应用列表排序的依据字段。取值范围："CREATED_TIME"：依据应用的创建时间排序。 "APPLICATION_SIZE"：依据应用的大小排序。默认按应用的创建时间排序。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        """输出应用列表的排列顺序。取值范围："ASC"：升序排列。 "DESC"：降序排列。默认按降序排列。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._ApplicationIds = params.get("ApplicationIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 应用总数
        :type TotalCount: int
        :param _ApplicationSet: 分页返回的应用列表
        :type ApplicationSet: list of ApplicationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """应用总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationSet(self):
        """分页返回的应用列表
        :rtype: list of ApplicationInfo
        """
        return self._ApplicationSet

    @ApplicationSet.setter
    def ApplicationSet(self, ApplicationSet):
        self._ApplicationSet = ApplicationSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApplicationSet") is not None:
            self._ApplicationSet = []
            for item in params.get("ApplicationSet"):
                obj = ApplicationInfo()
                obj._deserialize(item)
                self._ApplicationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceNetworkStatusRequest(AbstractModel):
    """DescribeInstanceNetworkStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID数组，单次请求最多不超过100个实例
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        """实例ID数组，单次请求最多不超过100个实例
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNetworkStatusResponse(AbstractModel):
    """DescribeInstanceNetworkStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果集长度
        :type TotalCount: int
        :param _NetworkStatusSet: 查询结果集
        :type NetworkStatusSet: list of NetworkStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NetworkStatusSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询结果集长度
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NetworkStatusSet(self):
        """查询结果集
        :rtype: list of NetworkStatus
        """
        return self._NetworkStatusSet

    @NetworkStatusSet.setter
    def NetworkStatusSet(self, NetworkStatusSet):
        self._NetworkStatusSet = NetworkStatusSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NetworkStatusSet") is not None:
            self._NetworkStatusSet = []
            for item in params.get("NetworkStatusSet"):
                obj = NetworkStatus()
                obj._deserialize(item)
                self._NetworkStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例元组
        :type InstanceIds: list of str
        :param _Filters: 描述键值对过滤器，用于条件过滤查询。目前支持的过滤器有：instance-id，实例id；instance-state，实例状态；charge-type，付费方式；public-ip-address，公网IP过滤
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0

        :type Offset: int
        :param _Limit: 返回量，默认为20
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        """实例元组
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        """描述键值对过滤器，用于条件过滤查询。目前支持的过滤器有：instance-id，实例id；instance-state，实例状态；charge-type，付费方式；public-ip-address，公网IP过滤
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0

        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回量，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数

        :type TotalCount: int
        :param _InstanceSet: 分页实例详情

        :type InstanceSet: list of Instance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """实例总数

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        """分页实例详情

        :rtype: list of Instance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMuskPromptsRequest(AbstractModel):
    """DescribeMuskPrompts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkgroupId: workgroup id
        :type WorkgroupId: str
        :param _WorkflowId: workflow id
        :type WorkflowId: str
        :param _Offset: offset 
        :type Offset: int
        :param _Limit: limit
        :type Limit: int
        :param _Filters: 过滤参数 支持过滤的键值： PromptId，Status
        :type Filters: list of Filter
        """
        self._WorkgroupId = None
        self._WorkflowId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def WorkgroupId(self):
        """workgroup id
        :rtype: str
        """
        return self._WorkgroupId

    @WorkgroupId.setter
    def WorkgroupId(self, WorkgroupId):
        self._WorkgroupId = WorkgroupId

    @property
    def WorkflowId(self):
        """workflow id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def Offset(self):
        """offset 
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤参数 支持过滤的键值： PromptId，Status
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._WorkgroupId = params.get("WorkgroupId")
        self._WorkflowId = params.get("WorkflowId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMuskPromptsResponse(AbstractModel):
    """DescribeMuskPrompts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: total count
        :type TotalCount: int
        :param _MuskPromptInfos: prompt列表详情
        :type MuskPromptInfos: list of MuskPromptInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MuskPromptInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MuskPromptInfos(self):
        """prompt列表详情
        :rtype: list of MuskPromptInfo
        """
        return self._MuskPromptInfos

    @MuskPromptInfos.setter
    def MuskPromptInfos(self, MuskPromptInfos):
        self._MuskPromptInfos = MuskPromptInfos

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MuskPromptInfos") is not None:
            self._MuskPromptInfos = []
            for item in params.get("MuskPromptInfos"):
                obj = MuskPromptInfo()
                obj._deserialize(item)
                self._MuskPromptInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 地域列表
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        """地域列表
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    """DescribeScenes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneIds: 场景id列表
        :type SceneIds: list of str
        """
        self._SceneIds = None

    @property
    def SceneIds(self):
        """场景id列表
        :rtype: list of str
        """
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenesResponse(AbstractModel):
    """DescribeScenes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneSet: 场景详情
        :type SceneSet: list of SceneInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SceneSet = None
        self._RequestId = None

    @property
    def SceneSet(self):
        """场景详情
        :rtype: list of SceneInfo
        """
        return self._SceneSet

    @SceneSet.setter
    def SceneSet(self, SceneSet):
        self._SceneSet = SceneSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SceneSet") is not None:
            self._SceneSet = []
            for item in params.get("SceneSet"):
                obj = SceneInfo()
                obj._deserialize(item)
                self._SceneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceLoginSettingsRequest(AbstractModel):
    """DescribeServiceLoginSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        """
        self._InstanceId = None
        self._ServiceName = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        """服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceLoginSettingsResponse(AbstractModel):
    """DescribeServiceLoginSettings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginSettings: 服务登录配置详情
        :type LoginSettings: list of LoginSetting
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginSettings = None
        self._RequestId = None

    @property
    def LoginSettings(self):
        """服务登录配置详情
        :rtype: list of LoginSetting
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoginSettings") is not None:
            self._LoginSettings = []
            for item in params.get("LoginSettings"):
                obj = LoginSetting()
                obj._deserialize(item)
                self._LoginSettings.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    - 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    - 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。	
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """需要过滤的字段。	
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRunInstancesRequest(AbstractModel):
    """InquirePriceRunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _BundleType: 算力套餐类型
        :type BundleType: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        :param _InstanceCount: 购买实例数量。
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称
        :type InstanceName: str
        :param _ClientToken: 幂等请求token
        :type ClientToken: str
        :param _DryRun: DryRun为True就是只验接口连通性，默认为False
        :type DryRun: bool
        :param _InstanceChargeType: 付费方式，POSTPAID_BY_HOUR按量后付费，PREPAID_BY_MONTH预付费按月，PREPAID_BY_DAY预付费按天
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费参数
        :type InstanceChargePrepaid: :class:`tencentcloud.hai.v20230812.models.InstanceChargePrepaid`
        """
        self._ApplicationId = None
        self._BundleType = None
        self._SystemDisk = None
        self._InstanceCount = None
        self._InstanceName = None
        self._ClientToken = None
        self._DryRun = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None

    @property
    def ApplicationId(self):
        """应用ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def BundleType(self):
        """算力套餐类型
        :rtype: str
        """
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def SystemDisk(self):
        """实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceCount(self):
        """购买实例数量。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        """实例显示名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClientToken(self):
        """幂等请求token
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        """DryRun为True就是只验接口连通性，默认为False
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def InstanceChargeType(self):
        """付费方式，POSTPAID_BY_HOUR按量后付费，PREPAID_BY_MONTH预付费按月，PREPAID_BY_DAY预付费按天
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """预付费参数
        :rtype: :class:`tencentcloud.hai.v20230812.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._BundleType = params.get("BundleType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRunInstancesResponse(AbstractModel):
    """InquirePriceRunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 发货参数对应的价格组合，当DryRun=True，会返回空
        :type Price: :class:`tencentcloud.hai.v20230812.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        """发货参数对应的价格组合，当DryRun=True，会返回空
        :rtype: :class:`tencentcloud.hai.v20230812.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceState: 实例状态：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
ARREARS：表示待回收
STOPPED_NO_CHARGE：表示关机不收费
TERMINATING：表示销毁中
TERMINATED：表示已销毁
        :type InstanceState: str
        :param _ApplicationName: 应用名称

        :type ApplicationName: str
        :param _BundleName: 算力套餐名称

        :type BundleName: str
        :param _GPUCount: 实例所包含的GPU卡数
        :type GPUCount: int
        :param _GPUPerformance: 算力

        :type GPUPerformance: str
        :param _GPUMemory: 显存
        :type GPUMemory: str
        :param _CPU: CPU核数
        :type CPU: str
        :param _Memory: 内存

        :type Memory: str
        :param _SystemDisk: 系统盘数据
        :type SystemDisk: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        :param _PrivateIpAddresses: 内网ip地址
        :type PrivateIpAddresses: list of str
        :param _PublicIpAddresses: 公网ip地址
        :type PublicIpAddresses: list of str
        :param _SecurityGroupIds: 安全组ID

        :type SecurityGroupIds: list of str
        :param _LatestOperation: 实例最新操作
        :type LatestOperation: str
        :param _LatestOperationState: 实例最新操作状态：
SUCCESS：表示操作成功
OPERATING：表示操作执行中
FAILED：表示操作失败

        :type LatestOperationState: str
        :param _CreateTime: 实例创建时间
        :type CreateTime: str
        :param _MaxOutBandwidth: 公网出带宽上限，默认10Mbps
        :type MaxOutBandwidth: str
        :param _MaxFreeTraffic: 每月免费流量，默认500G
        :type MaxFreeTraffic: str
        :param _ConfigurationEnvironment: 应用配置环境
        :type ConfigurationEnvironment: str
        :param _LoginServices: 实例包含的登录服务详情
        :type LoginServices: list of LoginService
        :param _OSType: 应用服务的操作系统类型
        :type OSType: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceState = None
        self._ApplicationName = None
        self._BundleName = None
        self._GPUCount = None
        self._GPUPerformance = None
        self._GPUMemory = None
        self._CPU = None
        self._Memory = None
        self._SystemDisk = None
        self._PrivateIpAddresses = None
        self._PublicIpAddresses = None
        self._SecurityGroupIds = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._CreateTime = None
        self._MaxOutBandwidth = None
        self._MaxFreeTraffic = None
        self._ConfigurationEnvironment = None
        self._LoginServices = None
        self._OSType = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceState(self):
        """实例状态：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
ARREARS：表示待回收
STOPPED_NO_CHARGE：表示关机不收费
TERMINATING：表示销毁中
TERMINATED：表示已销毁
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def ApplicationName(self):
        """应用名称

        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def BundleName(self):
        """算力套餐名称

        :rtype: str
        """
        return self._BundleName

    @BundleName.setter
    def BundleName(self, BundleName):
        self._BundleName = BundleName

    @property
    def GPUCount(self):
        """实例所包含的GPU卡数
        :rtype: int
        """
        return self._GPUCount

    @GPUCount.setter
    def GPUCount(self, GPUCount):
        self._GPUCount = GPUCount

    @property
    def GPUPerformance(self):
        """算力

        :rtype: str
        """
        return self._GPUPerformance

    @GPUPerformance.setter
    def GPUPerformance(self, GPUPerformance):
        self._GPUPerformance = GPUPerformance

    @property
    def GPUMemory(self):
        """显存
        :rtype: str
        """
        return self._GPUMemory

    @GPUMemory.setter
    def GPUMemory(self, GPUMemory):
        self._GPUMemory = GPUMemory

    @property
    def CPU(self):
        """CPU核数
        :rtype: str
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        """内存

        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def SystemDisk(self):
        """系统盘数据
        :rtype: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def PrivateIpAddresses(self):
        """内网ip地址
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def PublicIpAddresses(self):
        """公网ip地址
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def SecurityGroupIds(self):
        """安全组ID

        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LatestOperation(self):
        """实例最新操作
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        """实例最新操作状态：
SUCCESS：表示操作成功
OPERATING：表示操作执行中
FAILED：表示操作失败

        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def CreateTime(self):
        """实例创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxOutBandwidth(self):
        """公网出带宽上限，默认10Mbps
        :rtype: str
        """
        return self._MaxOutBandwidth

    @MaxOutBandwidth.setter
    def MaxOutBandwidth(self, MaxOutBandwidth):
        self._MaxOutBandwidth = MaxOutBandwidth

    @property
    def MaxFreeTraffic(self):
        """每月免费流量，默认500G
        :rtype: str
        """
        return self._MaxFreeTraffic

    @MaxFreeTraffic.setter
    def MaxFreeTraffic(self, MaxFreeTraffic):
        self._MaxFreeTraffic = MaxFreeTraffic

    @property
    def ConfigurationEnvironment(self):
        """应用配置环境
        :rtype: str
        """
        return self._ConfigurationEnvironment

    @ConfigurationEnvironment.setter
    def ConfigurationEnvironment(self, ConfigurationEnvironment):
        self._ConfigurationEnvironment = ConfigurationEnvironment

    @property
    def LoginServices(self):
        """实例包含的登录服务详情
        :rtype: list of LoginService
        """
        return self._LoginServices

    @LoginServices.setter
    def LoginServices(self, LoginServices):
        self._LoginServices = LoginServices

    @property
    def OSType(self):
        """应用服务的操作系统类型
        :rtype: str
        """
        return self._OSType

    @OSType.setter
    def OSType(self, OSType):
        self._OSType = OSType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceState = params.get("InstanceState")
        self._ApplicationName = params.get("ApplicationName")
        self._BundleName = params.get("BundleName")
        self._GPUCount = params.get("GPUCount")
        self._GPUPerformance = params.get("GPUPerformance")
        self._GPUMemory = params.get("GPUMemory")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._CreateTime = params.get("CreateTime")
        self._MaxOutBandwidth = params.get("MaxOutBandwidth")
        self._MaxFreeTraffic = params.get("MaxFreeTraffic")
        self._ConfigurationEnvironment = params.get("ConfigurationEnvironment")
        if params.get("LoginServices") is not None:
            self._LoginServices = []
            for item in params.get("LoginServices"):
                obj = LoginService()
                obj._deserialize(item)
                self._LoginServices.append(obj)
        self._OSType = params.get("OSType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """实例预付费入参

    """

    def __init__(self):
        r"""
        :param _Period: 时长，默认值：1
        :type Period: int
        :param _RenewFlag: 续费标志可选参数：
NOTIFY_AND_MANUAL_RENEW：表示默认状态(用户未设置，即初始状态：若用户有预付费不停服特权，也会对该值进行自动续费)
NOTIFY_AND_AUTO_RENEW：表示自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：表示明确不自动续费(用户设置)
默认值：NOTIFY_AND_MANUAL_RENEW

        :type RenewFlag: str
        :param _TimeUnit: 时长单位，默认值MONTH
        :type TimeUnit: str
        """
        self._Period = None
        self._RenewFlag = None
        self._TimeUnit = None

    @property
    def Period(self):
        """时长，默认值：1
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        """续费标志可选参数：
NOTIFY_AND_MANUAL_RENEW：表示默认状态(用户未设置，即初始状态：若用户有预付费不停服特权，也会对该值进行自动续费)
NOTIFY_AND_AUTO_RENEW：表示自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：表示明确不自动续费(用户设置)
默认值：NOTIFY_AND_MANUAL_RENEW

        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeUnit(self):
        """时长单位，默认值MONTH
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """套餐价格

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 原单价
        :type UnitPrice: float
        :param _DiscountUnitPrice: 折扣后单价
        :type DiscountUnitPrice: float
        :param _Discount: 折扣
        :type Discount: float
        :param _ChargeUnit: 单位：时/月

        :type ChargeUnit: str
        :param _Amount: 商品数量
        :type Amount: int
        """
        self._UnitPrice = None
        self._DiscountUnitPrice = None
        self._Discount = None
        self._ChargeUnit = None
        self._Amount = None

    @property
    def UnitPrice(self):
        """原单价
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def DiscountUnitPrice(self):
        """折扣后单价
        :rtype: float
        """
        return self._DiscountUnitPrice

    @DiscountUnitPrice.setter
    def DiscountUnitPrice(self, DiscountUnitPrice):
        self._DiscountUnitPrice = DiscountUnitPrice

    @property
    def Discount(self):
        """折扣
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ChargeUnit(self):
        """单位：时/月

        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def Amount(self):
        """商品数量
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._DiscountUnitPrice = params.get("DiscountUnitPrice")
        self._Discount = params.get("Discount")
        self._ChargeUnit = params.get("ChargeUnit")
        self._Amount = params.get("Amount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPriceDetail(AbstractModel):
    """分实例价格

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstancePrice: 实例价格详情
        :type InstancePrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _CloudDiskPrice: 磁盘价格详情
        :type CloudDiskPrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _InstanceTotalPrice: 该实例的总价钱
        :type InstanceTotalPrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        self._InstanceId = None
        self._InstancePrice = None
        self._CloudDiskPrice = None
        self._InstanceTotalPrice = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstancePrice(self):
        """实例价格详情
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def CloudDiskPrice(self):
        """磁盘价格详情
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._CloudDiskPrice

    @CloudDiskPrice.setter
    def CloudDiskPrice(self, CloudDiskPrice):
        self._CloudDiskPrice = CloudDiskPrice

    @property
    def InstanceTotalPrice(self):
        """该实例的总价钱
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._InstanceTotalPrice

    @InstanceTotalPrice.setter
    def InstanceTotalPrice(self, InstanceTotalPrice):
        self._InstanceTotalPrice = InstanceTotalPrice


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("CloudDiskPrice") is not None:
            self._CloudDiskPrice = ItemPrice()
            self._CloudDiskPrice._deserialize(params.get("CloudDiskPrice"))
        if params.get("InstanceTotalPrice") is not None:
            self._InstanceTotalPrice = ItemPrice()
            self._InstanceTotalPrice._deserialize(params.get("InstanceTotalPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginService(AbstractModel):
    """登录服务详情

    """

    def __init__(self):
        r"""
        :param _ServiceName: 登录方式名称
        :type ServiceName: str
        """
        self._ServiceName = None

    @property
    def ServiceName(self):
        """登录方式名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSetting(AbstractModel):
    """某服务的登录配置

    """

    def __init__(self):
        r"""
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _Url: 服务登录url
        :type Url: str
        """
        self._ServiceName = None
        self._Url = None

    @property
    def ServiceName(self):
        """服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Url(self):
        """服务登录url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MuskPromptInfo(AbstractModel):
    """musk prompt详情

    """

    def __init__(self):
        r"""
        :param _WorkflowId: workflow id
        :type WorkflowId: str
        :param _WorkgroupId: workgroup id
        :type WorkgroupId: str
        :param _PromptId: prompt id
        :type PromptId: str
        :param _OutputResource: 生成的内容
        :type OutputResource: list of str
        :param _Status: prompt status 
0: 执行中
1: 执行成功
2: 执行失败
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Cost: 任务执行耗时，单位毫秒
        :type Cost: int
        :param _ErrorMessage: 任务执行失败错误信息
        :type ErrorMessage: str
        """
        self._WorkflowId = None
        self._WorkgroupId = None
        self._PromptId = None
        self._OutputResource = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Cost = None
        self._ErrorMessage = None

    @property
    def WorkflowId(self):
        """workflow id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkgroupId(self):
        """workgroup id
        :rtype: str
        """
        return self._WorkgroupId

    @WorkgroupId.setter
    def WorkgroupId(self, WorkgroupId):
        self._WorkgroupId = WorkgroupId

    @property
    def PromptId(self):
        """prompt id
        :rtype: str
        """
        return self._PromptId

    @PromptId.setter
    def PromptId(self, PromptId):
        self._PromptId = PromptId

    @property
    def OutputResource(self):
        """生成的内容
        :rtype: list of str
        """
        return self._OutputResource

    @OutputResource.setter
    def OutputResource(self, OutputResource):
        self._OutputResource = OutputResource

    @property
    def Status(self):
        """prompt status 
0: 执行中
1: 执行成功
2: 执行失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Cost(self):
        """任务执行耗时，单位毫秒
        :rtype: int
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def ErrorMessage(self):
        """任务执行失败错误信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkgroupId = params.get("WorkgroupId")
        self._PromptId = params.get("PromptId")
        self._OutputResource = params.get("OutputResource")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Cost = params.get("Cost")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkStatus(AbstractModel):
    """HAI 实例的网络配置和消耗情况

    """

    def __init__(self):
        r"""
        :param _InstanceId: HAI 的实例 ID
        :type InstanceId: str
        :param _AddressIp: 公网 IP 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIp: str
        :param _Bandwidth: 出带宽上限，单位Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type Bandwidth: int
        :param _TotalTrafficAmount: 流量包总量，单位GB
        :type TotalTrafficAmount: float
        :param _RemainingTrafficAmount: 流量包剩余量，单位GB
        :type RemainingTrafficAmount: float
        """
        self._InstanceId = None
        self._AddressIp = None
        self._Bandwidth = None
        self._TotalTrafficAmount = None
        self._RemainingTrafficAmount = None

    @property
    def InstanceId(self):
        """HAI 的实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AddressIp(self):
        """公网 IP 地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddressIp

    @AddressIp.setter
    def AddressIp(self, AddressIp):
        self._AddressIp = AddressIp

    @property
    def Bandwidth(self):
        """出带宽上限，单位Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def TotalTrafficAmount(self):
        """流量包总量，单位GB
        :rtype: float
        """
        return self._TotalTrafficAmount

    @TotalTrafficAmount.setter
    def TotalTrafficAmount(self, TotalTrafficAmount):
        self._TotalTrafficAmount = TotalTrafficAmount

    @property
    def RemainingTrafficAmount(self):
        """流量包剩余量，单位GB
        :rtype: float
        """
        return self._RemainingTrafficAmount

    @RemainingTrafficAmount.setter
    def RemainingTrafficAmount(self, RemainingTrafficAmount):
        self._RemainingTrafficAmount = RemainingTrafficAmount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AddressIp = params.get("AddressIp")
        self._Bandwidth = params.get("Bandwidth")
        self._TotalTrafficAmount = params.get("TotalTrafficAmount")
        self._RemainingTrafficAmount = params.get("RemainingTrafficAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """费用数据结构体

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 实例价格信息
        :type InstancePrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _CloudDiskPrice: 云盘价格信息
        :type CloudDiskPrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _PriceDetailSet: 分实例价格
        :type PriceDetailSet: list of ItemPriceDetail
        """
        self._InstancePrice = None
        self._CloudDiskPrice = None
        self._PriceDetailSet = None

    @property
    def InstancePrice(self):
        """实例价格信息
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def CloudDiskPrice(self):
        """云盘价格信息
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._CloudDiskPrice

    @CloudDiskPrice.setter
    def CloudDiskPrice(self, CloudDiskPrice):
        self._CloudDiskPrice = CloudDiskPrice

    @property
    def PriceDetailSet(self):
        """分实例价格
        :rtype: list of ItemPriceDetail
        """
        return self._PriceDetailSet

    @PriceDetailSet.setter
    def PriceDetailSet(self, PriceDetailSet):
        self._PriceDetailSet = PriceDetailSet


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("CloudDiskPrice") is not None:
            self._CloudDiskPrice = ItemPrice()
            self._CloudDiskPrice._deserialize(params.get("CloudDiskPrice"))
        if params.get("PriceDetailSet") is not None:
            self._PriceDetailSet = []
            for item in params.get("PriceDetailSet"):
                obj = ItemPriceDetail()
                obj._deserialize(item)
                self._PriceDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """地域列表

    """

    def __init__(self):
        r"""
        :param _Region: ap-guangzhou

        :type Region: str
        :param _RegionName: 华南地区(广州)
        :type RegionName: str
        :param _RegionState: 地域是否可用状态
AVAILABLE：可用

        :type RegionState: str
        :param _ScholarRocketSupportState: 学术加速是否支持：
NO_NEED_SUPPORT表示不需支持；NOT_SUPPORT_YET表示暂未支持；ALREADY_SUPPORT表示已经支持。对于ALREADY_SUPPORT的地域才需进一步调用DescribeScholarRocketStatus查看学术加速是开启还是关闭
        :type ScholarRocketSupportState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None
        self._ScholarRocketSupportState = None

    @property
    def Region(self):
        """ap-guangzhou

        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        """华南地区(广州)
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        """地域是否可用状态
AVAILABLE：可用

        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def ScholarRocketSupportState(self):
        """学术加速是否支持：
NO_NEED_SUPPORT表示不需支持；NOT_SUPPORT_YET表示暂未支持；ALREADY_SUPPORT表示已经支持。对于ALREADY_SUPPORT的地域才需进一步调用DescribeScholarRocketStatus查看学术加速是开启还是关闭
        :rtype: str
        """
        return self._ScholarRocketSupportState

    @ScholarRocketSupportState.setter
    def ScholarRocketSupportState(self, ScholarRocketSupportState):
        self._ScholarRocketSupportState = ScholarRocketSupportState


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        self._ScholarRocketSupportState = params.get("ScholarRocketSupportState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _BundleType: 算力套餐类型
        :type BundleType: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        :param _InstanceCount: 购买实例数量。
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称
        :type InstanceName: str
        :param _ClientToken: 幂等请求的token
        :type ClientToken: str
        :param _DryRun: DryRun为True就是只验接口连通性，默认为False
        :type DryRun: bool
        """
        self._ApplicationId = None
        self._BundleType = None
        self._SystemDisk = None
        self._InstanceCount = None
        self._InstanceName = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def ApplicationId(self):
        """应用ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def BundleType(self):
        """算力套餐类型
        :rtype: str
        """
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def SystemDisk(self):
        """实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceCount(self):
        """购买实例数量。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        """实例显示名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClientToken(self):
        """幂等请求的token
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        """DryRun为True就是只验接口连通性，默认为False
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._BundleType = params.get("BundleType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        """实例ID列表
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    """场景详情

    """

    def __init__(self):
        r"""
        :param _SceneId: 场景id

        :type SceneId: str
        :param _SceneName: 场景名

        :type SceneName: str
        """
        self._SceneId = None
        self._SceneName = None

    @property
    def SceneId(self):
        """场景id

        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def SceneName(self):
        """场景名

        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._SceneName = params.get("SceneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceRequest(AbstractModel):
    """StartInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _DryRun: 默认为False，True代表只验证接口连通性
        :type DryRun: bool
        """
        self._InstanceId = None
        self._DryRun = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DryRun(self):
        """默认为False，True代表只验证接口连通性
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceResponse(AbstractModel):
    """StartInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: task任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """task任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopInstanceRequest(AbstractModel):
    """StopInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _StopMode: hai实例关机的模式，目前仅支持关机不收费：
STOP_CHARGE -- 关闭hai实例，释放计算资源，停止收取计算资源的费用。
注意：默认值为STOP_CHARGE
        :type StopMode: str
        :param _DryRun: 默认为False，True代表只验证接口连通性
        :type DryRun: bool
        """
        self._InstanceId = None
        self._StopMode = None
        self._DryRun = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StopMode(self):
        """hai实例关机的模式，目前仅支持关机不收费：
STOP_CHARGE -- 关闭hai实例，释放计算资源，停止收取计算资源的费用。
注意：默认值为STOP_CHARGE
        :rtype: str
        """
        return self._StopMode

    @StopMode.setter
    def StopMode(self, StopMode):
        self._StopMode = StopMode

    @property
    def DryRun(self):
        """默认为False，True代表只验证接口连通性
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StopMode = params.get("StopMode")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceResponse(AbstractModel):
    """StopInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: task任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """task任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。取值范围：<li>CLOUD_PREMIUM：高性能云硬盘</li><li>CLOUD_HSSD：增强型SSD云盘</li>默认取值：当前有库存的硬盘类型。
        :type DiskType: str
        :param _DiskSize: 系统盘大小，单位：GB。默认值为 80
        :type DiskSize: int
        :param _DiskName: 系统盘分区盘符
        :type DiskName: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskName = None

    @property
    def DiskType(self):
        """系统盘类型。取值范围：<li>CLOUD_PREMIUM：高性能云硬盘</li><li>CLOUD_HSSD：增强型SSD云盘</li>默认取值：当前有库存的硬盘类型。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """系统盘大小，单位：GB。默认值为 80
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskName(self):
        """系统盘分区盘符
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskName = params.get("DiskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _DryRun: 默认为False，True代表只验证接口连通性
        :type DryRun: bool
        """
        self._InstanceIds = None
        self._DryRun = None

    @property
    def InstanceIds(self):
        """实例ID列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DryRun(self):
        """默认为False，True代表只验证接口连通性
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")