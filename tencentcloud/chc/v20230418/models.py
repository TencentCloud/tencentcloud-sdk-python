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


class AvailableModelVersion(AbstractModel):
    """已通过设备型号评估的型号信息

    """

    def __init__(self):
        r"""
        :param _ModelVersion: 带有版本号的设备型号
        :type ModelVersion: str
        :param _DevHeight: 设备高度
        :type DevHeight: str
        :param _DeviceType: 设备类型，server 服务器，netDevice 网络设备
        :type DeviceType: str
        """
        self._ModelVersion = None
        self._DevHeight = None
        self._DeviceType = None

    @property
    def ModelVersion(self):
        """带有版本号的设备型号
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def DevHeight(self):
        """设备高度
        :rtype: str
        """
        return self._DevHeight

    @DevHeight.setter
    def DevHeight(self, DevHeight):
        self._DevHeight = DevHeight

    @property
    def DeviceType(self):
        """设备类型，server 服务器，netDevice 网络设备
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._ModelVersion = params.get("ModelVersion")
        self._DevHeight = params.get("DevHeight")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cage(AbstractModel):
    """围笼

    """

    def __init__(self):
        r"""
        :param _CageName: 围笼名称
        :type CageName: str
        :param _CheckerSet: 围笼审核人账号ID
        :type CheckerSet: list of str
        """
        self._CageName = None
        self._CheckerSet = None

    @property
    def CageName(self):
        """围笼名称
        :rtype: str
        """
        return self._CageName

    @CageName.setter
    def CageName(self, CageName):
        self._CageName = CageName

    @property
    def CheckerSet(self):
        """围笼审核人账号ID
        :rtype: list of str
        """
        return self._CheckerSet

    @CheckerSet.setter
    def CheckerSet(self, CheckerSet):
        self._CheckerSet = CheckerSet


    def _deserialize(self, params):
        self._CageName = params.get("CageName")
        self._CheckerSet = params.get("CheckerSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Campus(AbstractModel):
    """园区信息

    """

    def __init__(self):
        r"""
        :param _CampusId: 园区ID
        :type CampusId: int
        :param _CampusName: 园区名称
        :type CampusName: str
        """
        self._CampusId = None
        self._CampusName = None

    @property
    def CampusId(self):
        """园区ID
        :rtype: int
        """
        return self._CampusId

    @CampusId.setter
    def CampusId(self, CampusId):
        self._CampusId = CampusId

    @property
    def CampusName(self):
        """园区名称
        :rtype: str
        """
        return self._CampusName

    @CampusName.setter
    def CampusName(self, CampusName):
        self._CampusName = CampusName


    def _deserialize(self, params):
        self._CampusId = params.get("CampusId")
        self._CampusName = params.get("CampusName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonServiceBaseInfo(AbstractModel):
    """通用服务的基本信息

    """

    def __init__(self):
        r"""
        :param _IdcName: 机房名称
        :type IdcName: str
        :param _ContactName: 业务联系人
        :type ContactName: str
        :param _ContactPhone: 联系人电话
        :type ContactPhone: str
        :param _Instructions: 操作说明
        :type Instructions: str
        :param _ServiceLevel: 1 、2 、3 分别代表 L1、L2、L3
        :type ServiceLevel: int
        :param _PreAuthorization: 操作预授权
        :type PreAuthorization: bool
        """
        self._IdcName = None
        self._ContactName = None
        self._ContactPhone = None
        self._Instructions = None
        self._ServiceLevel = None
        self._PreAuthorization = None

    @property
    def IdcName(self):
        """机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def ContactName(self):
        """业务联系人
        :rtype: str
        """
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def ContactPhone(self):
        """联系人电话
        :rtype: str
        """
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def Instructions(self):
        """操作说明
        :rtype: str
        """
        return self._Instructions

    @Instructions.setter
    def Instructions(self, Instructions):
        self._Instructions = Instructions

    @property
    def ServiceLevel(self):
        """1 、2 、3 分别代表 L1、L2、L3
        :rtype: int
        """
        return self._ServiceLevel

    @ServiceLevel.setter
    def ServiceLevel(self, ServiceLevel):
        self._ServiceLevel = ServiceLevel

    @property
    def PreAuthorization(self):
        """操作预授权
        :rtype: bool
        """
        return self._PreAuthorization

    @PreAuthorization.setter
    def PreAuthorization(self, PreAuthorization):
        self._PreAuthorization = PreAuthorization


    def _deserialize(self, params):
        self._IdcName = params.get("IdcName")
        self._ContactName = params.get("ContactName")
        self._ContactPhone = params.get("ContactPhone")
        self._Instructions = params.get("Instructions")
        self._ServiceLevel = params.get("ServiceLevel")
        self._PreAuthorization = params.get("PreAuthorization")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmCommonServiceWorkOrderRequest(AbstractModel):
    """ConfirmCommonServiceWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 工单ID
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        """工单ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmCommonServiceWorkOrderResponse(AbstractModel):
    """ConfirmCommonServiceWorkOrder返回参数结构体

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


class CreateCommonServiceWorkOrderRequest(AbstractModel):
    """CreateCommonServiceWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DevicePositionSet: 设备及位置信息列表
        :type DevicePositionSet: list of DevicePosition
        :param _ServiceLevel: 服务级别，只支持传入 1、2、3，分别对应 L1、L2、L3
        :type ServiceLevel: int
        :param _PreAuthorization: 操作预授权
        :type PreAuthorization: bool
        :param _ContactName: 业务联系人
        :type ContactName: str
        :param _ContactPhone: 联系人电话
        :type ContactPhone: str
        :param _DeviceType: 设备类型 server 服务器，netDevice 网络设备	
        :type DeviceType: str
        :param _Instructions: 操作说明
        :type Instructions: str
        """
        self._DevicePositionSet = None
        self._ServiceLevel = None
        self._PreAuthorization = None
        self._ContactName = None
        self._ContactPhone = None
        self._DeviceType = None
        self._Instructions = None

    @property
    def DevicePositionSet(self):
        """设备及位置信息列表
        :rtype: list of DevicePosition
        """
        return self._DevicePositionSet

    @DevicePositionSet.setter
    def DevicePositionSet(self, DevicePositionSet):
        self._DevicePositionSet = DevicePositionSet

    @property
    def ServiceLevel(self):
        """服务级别，只支持传入 1、2、3，分别对应 L1、L2、L3
        :rtype: int
        """
        return self._ServiceLevel

    @ServiceLevel.setter
    def ServiceLevel(self, ServiceLevel):
        self._ServiceLevel = ServiceLevel

    @property
    def PreAuthorization(self):
        """操作预授权
        :rtype: bool
        """
        return self._PreAuthorization

    @PreAuthorization.setter
    def PreAuthorization(self, PreAuthorization):
        self._PreAuthorization = PreAuthorization

    @property
    def ContactName(self):
        """业务联系人
        :rtype: str
        """
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def ContactPhone(self):
        """联系人电话
        :rtype: str
        """
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def DeviceType(self):
        """设备类型 server 服务器，netDevice 网络设备	
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Instructions(self):
        """操作说明
        :rtype: str
        """
        return self._Instructions

    @Instructions.setter
    def Instructions(self, Instructions):
        self._Instructions = Instructions


    def _deserialize(self, params):
        if params.get("DevicePositionSet") is not None:
            self._DevicePositionSet = []
            for item in params.get("DevicePositionSet"):
                obj = DevicePosition()
                obj._deserialize(item)
                self._DevicePositionSet.append(obj)
        self._ServiceLevel = params.get("ServiceLevel")
        self._PreAuthorization = params.get("PreAuthorization")
        self._ContactName = params.get("ContactName")
        self._ContactPhone = params.get("ContactPhone")
        self._DeviceType = params.get("DeviceType")
        self._Instructions = params.get("Instructions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommonServiceWorkOrderResponse(AbstractModel):
    """CreateCommonServiceWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateModelEvaluationWorkOrderRequest(AbstractModel):
    """CreateModelEvaluationWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelSet: 设备名称及型号
        :type ModelSet: list of ModelVersion
        :param _CampusId: 园区ID
        :type CampusId: int
        :param _DeviceType: 只支持传入 server 和 netDevice
        :type DeviceType: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._ModelSet = None
        self._CampusId = None
        self._DeviceType = None
        self._Remark = None

    @property
    def ModelSet(self):
        """设备名称及型号
        :rtype: list of ModelVersion
        """
        return self._ModelSet

    @ModelSet.setter
    def ModelSet(self, ModelSet):
        self._ModelSet = ModelSet

    @property
    def CampusId(self):
        """园区ID
        :rtype: int
        """
        return self._CampusId

    @CampusId.setter
    def CampusId(self, CampusId):
        self._CampusId = CampusId

    @property
    def DeviceType(self):
        """只支持传入 server 和 netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        if params.get("ModelSet") is not None:
            self._ModelSet = []
            for item in params.get("ModelSet"):
                obj = ModelVersion()
                obj._deserialize(item)
                self._ModelSet.append(obj)
        self._CampusId = params.get("CampusId")
        self._DeviceType = params.get("DeviceType")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelEvaluationWorkOrderResponse(AbstractModel):
    """CreateModelEvaluationWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateMovingWorkOrderRequest(AbstractModel):
    """CreateMovingWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _DeviceType: 设备类型，server, netDevice
        :type DeviceType: str
        :param _WithPowerOn: 上架后是否开电
        :type WithPowerOn: bool
        :param _DeviceMovingList: 设备搬迁信息列表
        :type DeviceMovingList: list of DeviceRackOn
        :param _Remark: 备注
        :type Remark: str
        """
        self._IdcId = None
        self._DeviceType = None
        self._WithPowerOn = None
        self._DeviceMovingList = None
        self._Remark = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """设备类型，server, netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def WithPowerOn(self):
        """上架后是否开电
        :rtype: bool
        """
        return self._WithPowerOn

    @WithPowerOn.setter
    def WithPowerOn(self, WithPowerOn):
        self._WithPowerOn = WithPowerOn

    @property
    def DeviceMovingList(self):
        """设备搬迁信息列表
        :rtype: list of DeviceRackOn
        """
        return self._DeviceMovingList

    @DeviceMovingList.setter
    def DeviceMovingList(self, DeviceMovingList):
        self._DeviceMovingList = DeviceMovingList

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        self._WithPowerOn = params.get("WithPowerOn")
        if params.get("DeviceMovingList") is not None:
            self._DeviceMovingList = []
            for item in params.get("DeviceMovingList"):
                obj = DeviceRackOn()
                obj._deserialize(item)
                self._DeviceMovingList.append(obj)
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMovingWorkOrderResponse(AbstractModel):
    """CreateMovingWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateNetDeviceModelRequest(AbstractModel):
    """CreateNetDeviceModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelDetail: 网络设备型号
        :type ModelDetail: :class:`tencentcloud.chc.v20230418.models.NetDeviceModel`
        """
        self._ModelDetail = None

    @property
    def ModelDetail(self):
        """网络设备型号
        :rtype: :class:`tencentcloud.chc.v20230418.models.NetDeviceModel`
        """
        return self._ModelDetail

    @ModelDetail.setter
    def ModelDetail(self, ModelDetail):
        self._ModelDetail = ModelDetail


    def _deserialize(self, params):
        if params.get("ModelDetail") is not None:
            self._ModelDetail = NetDeviceModel()
            self._ModelDetail._deserialize(params.get("ModelDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetDeviceModelResponse(AbstractModel):
    """CreateNetDeviceModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DevModel: 型号名称
        :type DevModel: str
        :param _Version: 版本号
        :type Version: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DevModel = None
        self._Version = None
        self._RequestId = None

    @property
    def DevModel(self):
        """型号名称
        :rtype: str
        """
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def Version(self):
        """版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

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
        self._DevModel = params.get("DevModel")
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class CreatePersonnelVisitWorkOrderRequest(AbstractModel):
    """CreatePersonnelVisitWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonnelSet: 到访人员信息
        :type PersonnelSet: list of Personnel
        :param _IdcId: 机房 ID
        :type IdcId: int
        :param _IdcUnitIdSet: 机房管理单元列表
        :type IdcUnitIdSet: list of int non-negative
        :param _EnterStartTime: 到访开始时间
        :type EnterStartTime: str
        :param _EnterEndTime: 到访结束时间
        :type EnterEndTime: str
        :param _VisitReason: 到访原因，映射关系：IT_OPERATION IT运维 OTHER 其他
        :type VisitReason: list of str
        :param _VisitRemark: 到访说明
        :type VisitRemark: str
        """
        self._PersonnelSet = None
        self._IdcId = None
        self._IdcUnitIdSet = None
        self._EnterStartTime = None
        self._EnterEndTime = None
        self._VisitReason = None
        self._VisitRemark = None

    @property
    def PersonnelSet(self):
        """到访人员信息
        :rtype: list of Personnel
        """
        return self._PersonnelSet

    @PersonnelSet.setter
    def PersonnelSet(self, PersonnelSet):
        self._PersonnelSet = PersonnelSet

    @property
    def IdcId(self):
        """机房 ID
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def IdcUnitIdSet(self):
        """机房管理单元列表
        :rtype: list of int non-negative
        """
        return self._IdcUnitIdSet

    @IdcUnitIdSet.setter
    def IdcUnitIdSet(self, IdcUnitIdSet):
        self._IdcUnitIdSet = IdcUnitIdSet

    @property
    def EnterStartTime(self):
        """到访开始时间
        :rtype: str
        """
        return self._EnterStartTime

    @EnterStartTime.setter
    def EnterStartTime(self, EnterStartTime):
        self._EnterStartTime = EnterStartTime

    @property
    def EnterEndTime(self):
        """到访结束时间
        :rtype: str
        """
        return self._EnterEndTime

    @EnterEndTime.setter
    def EnterEndTime(self, EnterEndTime):
        self._EnterEndTime = EnterEndTime

    @property
    def VisitReason(self):
        """到访原因，映射关系：IT_OPERATION IT运维 OTHER 其他
        :rtype: list of str
        """
        return self._VisitReason

    @VisitReason.setter
    def VisitReason(self, VisitReason):
        self._VisitReason = VisitReason

    @property
    def VisitRemark(self):
        """到访说明
        :rtype: str
        """
        return self._VisitRemark

    @VisitRemark.setter
    def VisitRemark(self, VisitRemark):
        self._VisitRemark = VisitRemark


    def _deserialize(self, params):
        if params.get("PersonnelSet") is not None:
            self._PersonnelSet = []
            for item in params.get("PersonnelSet"):
                obj = Personnel()
                obj._deserialize(item)
                self._PersonnelSet.append(obj)
        self._IdcId = params.get("IdcId")
        self._IdcUnitIdSet = params.get("IdcUnitIdSet")
        self._EnterStartTime = params.get("EnterStartTime")
        self._EnterEndTime = params.get("EnterEndTime")
        self._VisitReason = params.get("VisitReason")
        self._VisitRemark = params.get("VisitRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonnelVisitWorkOrderResponse(AbstractModel):
    """CreatePersonnelVisitWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreatePowerOffWorkOrderRequest(AbstractModel):
    """CreatePowerOffWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _DeviceType: 设备类型，server, netDevice
        :type DeviceType: str
        :param _IsPowerOffConfirm: 关电确认，1.授权时关电 2.关电前需要确认
        :type IsPowerOffConfirm: str
        :param _DeviceSnList: 设备sn列表
        :type DeviceSnList: list of str
        :param _PowerOffConfirmInfo: 关电前需要确认时必填
        :type PowerOffConfirmInfo: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        :param _Remark: 备注
        :type Remark: str
        """
        self._IdcId = None
        self._DeviceType = None
        self._IsPowerOffConfirm = None
        self._DeviceSnList = None
        self._PowerOffConfirmInfo = None
        self._Remark = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """设备类型，server, netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def IsPowerOffConfirm(self):
        """关电确认，1.授权时关电 2.关电前需要确认
        :rtype: str
        """
        return self._IsPowerOffConfirm

    @IsPowerOffConfirm.setter
    def IsPowerOffConfirm(self, IsPowerOffConfirm):
        self._IsPowerOffConfirm = IsPowerOffConfirm

    @property
    def DeviceSnList(self):
        """设备sn列表
        :rtype: list of str
        """
        return self._DeviceSnList

    @DeviceSnList.setter
    def DeviceSnList(self, DeviceSnList):
        self._DeviceSnList = DeviceSnList

    @property
    def PowerOffConfirmInfo(self):
        """关电前需要确认时必填
        :rtype: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        """
        return self._PowerOffConfirmInfo

    @PowerOffConfirmInfo.setter
    def PowerOffConfirmInfo(self, PowerOffConfirmInfo):
        self._PowerOffConfirmInfo = PowerOffConfirmInfo

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        self._IsPowerOffConfirm = params.get("IsPowerOffConfirm")
        self._DeviceSnList = params.get("DeviceSnList")
        if params.get("PowerOffConfirmInfo") is not None:
            self._PowerOffConfirmInfo = PowerOffConfirm()
            self._PowerOffConfirmInfo._deserialize(params.get("PowerOffConfirmInfo"))
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePowerOffWorkOrderResponse(AbstractModel):
    """CreatePowerOffWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreatePowerOnWorkOrderRequest(AbstractModel):
    """CreatePowerOnWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _DeviceType: 设备类型，server, netDevice
        :type DeviceType: str
        :param _DeviceSnList: 设备sn列表
        :type DeviceSnList: list of str
        """
        self._IdcId = None
        self._DeviceType = None
        self._DeviceSnList = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """设备类型，server, netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def DeviceSnList(self):
        """设备sn列表
        :rtype: list of str
        """
        return self._DeviceSnList

    @DeviceSnList.setter
    def DeviceSnList(self, DeviceSnList):
        self._DeviceSnList = DeviceSnList


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        self._DeviceSnList = params.get("DeviceSnList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePowerOnWorkOrderResponse(AbstractModel):
    """CreatePowerOnWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateQuitWorkOrderRequest(AbstractModel):
    """CreateQuitWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _DeviceType: 设备类型，server, netDevice, otherDevice
        :type DeviceType: str
        :param _StuffOption: 下架选择 1.自行解决 2.由腾讯IDC负责 3.不涉及下架，如：其他设备退出
        :type StuffOption: str
        :param _IsPowerOffConfirm: 关电确认 1.授权时关电 2.关电前需要确认
        :type IsPowerOffConfirm: str
        :param _DeviceSnList: 设备sn列表
        :type DeviceSnList: list of str
        :param _HandoverMethod: 交接方式 1.物流上门收货 2.客户上门自提
        :type HandoverMethod: str
        :param _SelfOperationInfo: 自行解决必填
        :type SelfOperationInfo: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        :param _PowerOffConfirmInfo: 关电前需要确认时必填
        :type PowerOffConfirmInfo: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        :param _Remark: 备注
        :type Remark: str
        :param _LogisticsReceipt: 物流上门收货必传
        :type LogisticsReceipt: :class:`tencentcloud.chc.v20230418.models.LogisticsReceipt`
        :param _CustomerReceipt: 客户上门自提必传
        :type CustomerReceipt: :class:`tencentcloud.chc.v20230418.models.CustomerReceipt`
        """
        self._IdcId = None
        self._DeviceType = None
        self._StuffOption = None
        self._IsPowerOffConfirm = None
        self._DeviceSnList = None
        self._HandoverMethod = None
        self._SelfOperationInfo = None
        self._PowerOffConfirmInfo = None
        self._Remark = None
        self._LogisticsReceipt = None
        self._CustomerReceipt = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """设备类型，server, netDevice, otherDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def StuffOption(self):
        """下架选择 1.自行解决 2.由腾讯IDC负责 3.不涉及下架，如：其他设备退出
        :rtype: str
        """
        return self._StuffOption

    @StuffOption.setter
    def StuffOption(self, StuffOption):
        self._StuffOption = StuffOption

    @property
    def IsPowerOffConfirm(self):
        """关电确认 1.授权时关电 2.关电前需要确认
        :rtype: str
        """
        return self._IsPowerOffConfirm

    @IsPowerOffConfirm.setter
    def IsPowerOffConfirm(self, IsPowerOffConfirm):
        self._IsPowerOffConfirm = IsPowerOffConfirm

    @property
    def DeviceSnList(self):
        """设备sn列表
        :rtype: list of str
        """
        return self._DeviceSnList

    @DeviceSnList.setter
    def DeviceSnList(self, DeviceSnList):
        self._DeviceSnList = DeviceSnList

    @property
    def HandoverMethod(self):
        """交接方式 1.物流上门收货 2.客户上门自提
        :rtype: str
        """
        return self._HandoverMethod

    @HandoverMethod.setter
    def HandoverMethod(self, HandoverMethod):
        self._HandoverMethod = HandoverMethod

    @property
    def SelfOperationInfo(self):
        """自行解决必填
        :rtype: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        """
        return self._SelfOperationInfo

    @SelfOperationInfo.setter
    def SelfOperationInfo(self, SelfOperationInfo):
        self._SelfOperationInfo = SelfOperationInfo

    @property
    def PowerOffConfirmInfo(self):
        """关电前需要确认时必填
        :rtype: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        """
        return self._PowerOffConfirmInfo

    @PowerOffConfirmInfo.setter
    def PowerOffConfirmInfo(self, PowerOffConfirmInfo):
        self._PowerOffConfirmInfo = PowerOffConfirmInfo

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def LogisticsReceipt(self):
        """物流上门收货必传
        :rtype: :class:`tencentcloud.chc.v20230418.models.LogisticsReceipt`
        """
        return self._LogisticsReceipt

    @LogisticsReceipt.setter
    def LogisticsReceipt(self, LogisticsReceipt):
        self._LogisticsReceipt = LogisticsReceipt

    @property
    def CustomerReceipt(self):
        """客户上门自提必传
        :rtype: :class:`tencentcloud.chc.v20230418.models.CustomerReceipt`
        """
        return self._CustomerReceipt

    @CustomerReceipt.setter
    def CustomerReceipt(self, CustomerReceipt):
        self._CustomerReceipt = CustomerReceipt


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        self._StuffOption = params.get("StuffOption")
        self._IsPowerOffConfirm = params.get("IsPowerOffConfirm")
        self._DeviceSnList = params.get("DeviceSnList")
        self._HandoverMethod = params.get("HandoverMethod")
        if params.get("SelfOperationInfo") is not None:
            self._SelfOperationInfo = SelfOperation()
            self._SelfOperationInfo._deserialize(params.get("SelfOperationInfo"))
        if params.get("PowerOffConfirmInfo") is not None:
            self._PowerOffConfirmInfo = PowerOffConfirm()
            self._PowerOffConfirmInfo._deserialize(params.get("PowerOffConfirmInfo"))
        self._Remark = params.get("Remark")
        if params.get("LogisticsReceipt") is not None:
            self._LogisticsReceipt = LogisticsReceipt()
            self._LogisticsReceipt._deserialize(params.get("LogisticsReceipt"))
        if params.get("CustomerReceipt") is not None:
            self._CustomerReceipt = CustomerReceipt()
            self._CustomerReceipt._deserialize(params.get("CustomerReceipt"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQuitWorkOrderResponse(AbstractModel):
    """CreateQuitWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateRackOffWorkOrderRequest(AbstractModel):
    """CreateRackOffWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _DeviceType: 设备类型，server, netDevice
        :type DeviceType: str
        :param _StuffOption: 下架人员 1.自行解决 2.由腾讯IDC负责
        :type StuffOption: str
        :param _IsPowerOffConfirm: 关电确认 1.授权时关电 2.关电前需要确认
        :type IsPowerOffConfirm: str
        :param _DeviceSnList: 设备sn列表
        :type DeviceSnList: list of str
        :param _SelfOperationInfo: 自行解决必填
        :type SelfOperationInfo: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        :param _PowerOffConfirmInfo: 关电前需要确认时必填
        :type PowerOffConfirmInfo: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        :param _Remark: 备注
        :type Remark: str
        """
        self._IdcId = None
        self._DeviceType = None
        self._StuffOption = None
        self._IsPowerOffConfirm = None
        self._DeviceSnList = None
        self._SelfOperationInfo = None
        self._PowerOffConfirmInfo = None
        self._Remark = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """设备类型，server, netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def StuffOption(self):
        """下架人员 1.自行解决 2.由腾讯IDC负责
        :rtype: str
        """
        return self._StuffOption

    @StuffOption.setter
    def StuffOption(self, StuffOption):
        self._StuffOption = StuffOption

    @property
    def IsPowerOffConfirm(self):
        """关电确认 1.授权时关电 2.关电前需要确认
        :rtype: str
        """
        return self._IsPowerOffConfirm

    @IsPowerOffConfirm.setter
    def IsPowerOffConfirm(self, IsPowerOffConfirm):
        self._IsPowerOffConfirm = IsPowerOffConfirm

    @property
    def DeviceSnList(self):
        """设备sn列表
        :rtype: list of str
        """
        return self._DeviceSnList

    @DeviceSnList.setter
    def DeviceSnList(self, DeviceSnList):
        self._DeviceSnList = DeviceSnList

    @property
    def SelfOperationInfo(self):
        """自行解决必填
        :rtype: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        """
        return self._SelfOperationInfo

    @SelfOperationInfo.setter
    def SelfOperationInfo(self, SelfOperationInfo):
        self._SelfOperationInfo = SelfOperationInfo

    @property
    def PowerOffConfirmInfo(self):
        """关电前需要确认时必填
        :rtype: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        """
        return self._PowerOffConfirmInfo

    @PowerOffConfirmInfo.setter
    def PowerOffConfirmInfo(self, PowerOffConfirmInfo):
        self._PowerOffConfirmInfo = PowerOffConfirmInfo

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        self._StuffOption = params.get("StuffOption")
        self._IsPowerOffConfirm = params.get("IsPowerOffConfirm")
        self._DeviceSnList = params.get("DeviceSnList")
        if params.get("SelfOperationInfo") is not None:
            self._SelfOperationInfo = SelfOperation()
            self._SelfOperationInfo._deserialize(params.get("SelfOperationInfo"))
        if params.get("PowerOffConfirmInfo") is not None:
            self._PowerOffConfirmInfo = PowerOffConfirm()
            self._PowerOffConfirmInfo._deserialize(params.get("PowerOffConfirmInfo"))
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRackOffWorkOrderResponse(AbstractModel):
    """CreateRackOffWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateRackOnWorkOrderRequest(AbstractModel):
    """CreateRackOnWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _DeviceType: 设备类型，server, netDevice
        :type DeviceType: str
        :param _StuffOption: 上架人员 1.自行解决 2.由腾讯IDC负责
        :type StuffOption: str
        :param _WithPowerOn: 上架后是否开电
        :type WithPowerOn: bool
        :param _DeviceRackOnList: 服务器收货列表
        :type DeviceRackOnList: list of DeviceRackOn
        :param _SelfOperationInfo: 自行解决必填
        :type SelfOperationInfo: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        """
        self._IdcId = None
        self._DeviceType = None
        self._StuffOption = None
        self._WithPowerOn = None
        self._DeviceRackOnList = None
        self._SelfOperationInfo = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """设备类型，server, netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def StuffOption(self):
        """上架人员 1.自行解决 2.由腾讯IDC负责
        :rtype: str
        """
        return self._StuffOption

    @StuffOption.setter
    def StuffOption(self, StuffOption):
        self._StuffOption = StuffOption

    @property
    def WithPowerOn(self):
        """上架后是否开电
        :rtype: bool
        """
        return self._WithPowerOn

    @WithPowerOn.setter
    def WithPowerOn(self, WithPowerOn):
        self._WithPowerOn = WithPowerOn

    @property
    def DeviceRackOnList(self):
        """服务器收货列表
        :rtype: list of DeviceRackOn
        """
        return self._DeviceRackOnList

    @DeviceRackOnList.setter
    def DeviceRackOnList(self, DeviceRackOnList):
        self._DeviceRackOnList = DeviceRackOnList

    @property
    def SelfOperationInfo(self):
        """自行解决必填
        :rtype: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        """
        return self._SelfOperationInfo

    @SelfOperationInfo.setter
    def SelfOperationInfo(self, SelfOperationInfo):
        self._SelfOperationInfo = SelfOperationInfo


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        self._StuffOption = params.get("StuffOption")
        self._WithPowerOn = params.get("WithPowerOn")
        if params.get("DeviceRackOnList") is not None:
            self._DeviceRackOnList = []
            for item in params.get("DeviceRackOnList"):
                obj = DeviceRackOn()
                obj._deserialize(item)
                self._DeviceRackOnList.append(obj)
        if params.get("SelfOperationInfo") is not None:
            self._SelfOperationInfo = SelfOperation()
            self._SelfOperationInfo._deserialize(params.get("SelfOperationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRackOnWorkOrderResponse(AbstractModel):
    """CreateRackOnWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateReceivingWorkOrderRequest(AbstractModel):
    """CreateReceivingWorkOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _DeviceType: 设备类型，server, netDevice, wire, otherDevice
        :type DeviceType: str
        :param _EntryTime: 进入时间
        :type EntryTime: str
        :param _ReceivingOperation: 1.收货-仅核对外包装完整和数量，不开箱 2.验收-开箱核对型号SN一致
        :type ReceivingOperation: str
        :param _IsExpressDelivery: 是否快递寄件
        :type IsExpressDelivery: bool
        :param _ExpressInfo: 快递寄件信息,快递寄件必填
        :type ExpressInfo: :class:`tencentcloud.chc.v20230418.models.ExpressDelivery`
        :param _Remark: 备注
        :type Remark: str
        :param _ServerDeviceList: 服务器收货列表
        :type ServerDeviceList: list of ServerReceivingInfo
        :param _NetDeviceList: 网络设备收货列表
        :type NetDeviceList: list of NetReceivingInfo
        :param _WireDeviceList: 线材收货列表
        :type WireDeviceList: list of WireReceivingInfo
        :param _OtherDeviceList: 其他设备收货列表
        :type OtherDeviceList: list of OtherDevReceivingInfo
        """
        self._IdcId = None
        self._DeviceType = None
        self._EntryTime = None
        self._ReceivingOperation = None
        self._IsExpressDelivery = None
        self._ExpressInfo = None
        self._Remark = None
        self._ServerDeviceList = None
        self._NetDeviceList = None
        self._WireDeviceList = None
        self._OtherDeviceList = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """设备类型，server, netDevice, wire, otherDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EntryTime(self):
        """进入时间
        :rtype: str
        """
        return self._EntryTime

    @EntryTime.setter
    def EntryTime(self, EntryTime):
        self._EntryTime = EntryTime

    @property
    def ReceivingOperation(self):
        """1.收货-仅核对外包装完整和数量，不开箱 2.验收-开箱核对型号SN一致
        :rtype: str
        """
        return self._ReceivingOperation

    @ReceivingOperation.setter
    def ReceivingOperation(self, ReceivingOperation):
        self._ReceivingOperation = ReceivingOperation

    @property
    def IsExpressDelivery(self):
        """是否快递寄件
        :rtype: bool
        """
        return self._IsExpressDelivery

    @IsExpressDelivery.setter
    def IsExpressDelivery(self, IsExpressDelivery):
        self._IsExpressDelivery = IsExpressDelivery

    @property
    def ExpressInfo(self):
        """快递寄件信息,快递寄件必填
        :rtype: :class:`tencentcloud.chc.v20230418.models.ExpressDelivery`
        """
        return self._ExpressInfo

    @ExpressInfo.setter
    def ExpressInfo(self, ExpressInfo):
        self._ExpressInfo = ExpressInfo

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ServerDeviceList(self):
        """服务器收货列表
        :rtype: list of ServerReceivingInfo
        """
        return self._ServerDeviceList

    @ServerDeviceList.setter
    def ServerDeviceList(self, ServerDeviceList):
        self._ServerDeviceList = ServerDeviceList

    @property
    def NetDeviceList(self):
        """网络设备收货列表
        :rtype: list of NetReceivingInfo
        """
        return self._NetDeviceList

    @NetDeviceList.setter
    def NetDeviceList(self, NetDeviceList):
        self._NetDeviceList = NetDeviceList

    @property
    def WireDeviceList(self):
        """线材收货列表
        :rtype: list of WireReceivingInfo
        """
        return self._WireDeviceList

    @WireDeviceList.setter
    def WireDeviceList(self, WireDeviceList):
        self._WireDeviceList = WireDeviceList

    @property
    def OtherDeviceList(self):
        """其他设备收货列表
        :rtype: list of OtherDevReceivingInfo
        """
        return self._OtherDeviceList

    @OtherDeviceList.setter
    def OtherDeviceList(self, OtherDeviceList):
        self._OtherDeviceList = OtherDeviceList


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        self._EntryTime = params.get("EntryTime")
        self._ReceivingOperation = params.get("ReceivingOperation")
        self._IsExpressDelivery = params.get("IsExpressDelivery")
        if params.get("ExpressInfo") is not None:
            self._ExpressInfo = ExpressDelivery()
            self._ExpressInfo._deserialize(params.get("ExpressInfo"))
        self._Remark = params.get("Remark")
        if params.get("ServerDeviceList") is not None:
            self._ServerDeviceList = []
            for item in params.get("ServerDeviceList"):
                obj = ServerReceivingInfo()
                obj._deserialize(item)
                self._ServerDeviceList.append(obj)
        if params.get("NetDeviceList") is not None:
            self._NetDeviceList = []
            for item in params.get("NetDeviceList"):
                obj = NetReceivingInfo()
                obj._deserialize(item)
                self._NetDeviceList.append(obj)
        if params.get("WireDeviceList") is not None:
            self._WireDeviceList = []
            for item in params.get("WireDeviceList"):
                obj = WireReceivingInfo()
                obj._deserialize(item)
                self._WireDeviceList.append(obj)
        if params.get("OtherDeviceList") is not None:
            self._OtherDeviceList = []
            for item in params.get("OtherDeviceList"):
                obj = OtherDevReceivingInfo()
                obj._deserialize(item)
                self._OtherDeviceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceivingWorkOrderResponse(AbstractModel):
    """CreateReceivingWorkOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderSet: 创建的工单信息
        :type WorkOrderSet: list of WorkOrderTinyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def WorkOrderSet(self):
        """创建的工单信息
        :rtype: list of WorkOrderTinyInfo
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderTinyInfo()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateServerModelRequest(AbstractModel):
    """CreateServerModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelDetail: 设备型号详情
        :type ModelDetail: :class:`tencentcloud.chc.v20230418.models.ServerModel`
        """
        self._ModelDetail = None

    @property
    def ModelDetail(self):
        """设备型号详情
        :rtype: :class:`tencentcloud.chc.v20230418.models.ServerModel`
        """
        return self._ModelDetail

    @ModelDetail.setter
    def ModelDetail(self, ModelDetail):
        self._ModelDetail = ModelDetail


    def _deserialize(self, params):
        if params.get("ModelDetail") is not None:
            self._ModelDetail = ServerModel()
            self._ModelDetail._deserialize(params.get("ModelDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServerModelResponse(AbstractModel):
    """CreateServerModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DevModel: 型号名称
        :type DevModel: str
        :param _Version: 版本
        :type Version: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DevModel = None
        self._Version = None
        self._RequestId = None

    @property
    def DevModel(self):
        """型号名称
        :rtype: str
        """
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def Version(self):
        """版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

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
        self._DevModel = params.get("DevModel")
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class CustomerInfo(AbstractModel):
    """客户信息

    """

    def __init__(self):
        r"""
        :param _CustomerName: 公司全称
        :type CustomerName: str
        :param _ShortCustomerName: 公司简称
        :type ShortCustomerName: str
        :param _WholeFlag: 是否全托管用户
        :type WholeFlag: bool
        """
        self._CustomerName = None
        self._ShortCustomerName = None
        self._WholeFlag = None

    @property
    def CustomerName(self):
        """公司全称
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def ShortCustomerName(self):
        """公司简称
        :rtype: str
        """
        return self._ShortCustomerName

    @ShortCustomerName.setter
    def ShortCustomerName(self, ShortCustomerName):
        self._ShortCustomerName = ShortCustomerName

    @property
    def WholeFlag(self):
        """是否全托管用户
        :rtype: bool
        """
        return self._WholeFlag

    @WholeFlag.setter
    def WholeFlag(self, WholeFlag):
        self._WholeFlag = WholeFlag


    def _deserialize(self, params):
        self._CustomerName = params.get("CustomerName")
        self._ShortCustomerName = params.get("ShortCustomerName")
        self._WholeFlag = params.get("WholeFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomerReceipt(AbstractModel):
    """客户上门自提信息

    """

    def __init__(self):
        r"""
        :param _PickUpStuff: 自提人员姓名
        :type PickUpStuff: str
        :param _PickUpStuffContact: 自提人电话
        :type PickUpStuffContact: str
        :param _PickUpStuffIDCard: 自提人身份证号
        :type PickUpStuffIDCard: str
        :param _PickUpTime: 自提时间
        :type PickUpTime: str
        """
        self._PickUpStuff = None
        self._PickUpStuffContact = None
        self._PickUpStuffIDCard = None
        self._PickUpTime = None

    @property
    def PickUpStuff(self):
        """自提人员姓名
        :rtype: str
        """
        return self._PickUpStuff

    @PickUpStuff.setter
    def PickUpStuff(self, PickUpStuff):
        self._PickUpStuff = PickUpStuff

    @property
    def PickUpStuffContact(self):
        """自提人电话
        :rtype: str
        """
        return self._PickUpStuffContact

    @PickUpStuffContact.setter
    def PickUpStuffContact(self, PickUpStuffContact):
        self._PickUpStuffContact = PickUpStuffContact

    @property
    def PickUpStuffIDCard(self):
        """自提人身份证号
        :rtype: str
        """
        return self._PickUpStuffIDCard

    @PickUpStuffIDCard.setter
    def PickUpStuffIDCard(self, PickUpStuffIDCard):
        self._PickUpStuffIDCard = PickUpStuffIDCard

    @property
    def PickUpTime(self):
        """自提时间
        :rtype: str
        """
        return self._PickUpTime

    @PickUpTime.setter
    def PickUpTime(self, PickUpTime):
        self._PickUpTime = PickUpTime


    def _deserialize(self, params):
        self._PickUpStuff = params.get("PickUpStuff")
        self._PickUpStuffContact = params.get("PickUpStuffContact")
        self._PickUpStuffIDCard = params.get("PickUpStuffIDCard")
        self._PickUpTime = params.get("PickUpTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableModelListRequest(AbstractModel):
    """DescribeAvailableModelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房ID
        :type IdcId: int
        :param _DeviceType: server 服务器，netDevice 网络设备
        :type DeviceType: str
        """
        self._IdcId = None
        self._DeviceType = None

    @property
    def IdcId(self):
        """机房ID
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def DeviceType(self):
        """server 服务器，netDevice 网络设备
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableModelListResponse(AbstractModel):
    """DescribeAvailableModelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelVersionSet: 机房内可用的设备型号及版本列表
        :type ModelVersionSet: list of AvailableModelVersion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelVersionSet = None
        self._RequestId = None

    @property
    def ModelVersionSet(self):
        """机房内可用的设备型号及版本列表
        :rtype: list of AvailableModelVersion
        """
        return self._ModelVersionSet

    @ModelVersionSet.setter
    def ModelVersionSet(self, ModelVersionSet):
        self._ModelVersionSet = ModelVersionSet

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
        if params.get("ModelVersionSet") is not None:
            self._ModelVersionSet = []
            for item in params.get("ModelVersionSet"):
                obj = AvailableModelVersion()
                obj._deserialize(item)
                self._ModelVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCampusListRequest(AbstractModel):
    """DescribeCampusList请求参数结构体

    """


class DescribeCampusListResponse(AbstractModel):
    """DescribeCampusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CampusSet: 客户可操作的园区列表
        :type CampusSet: list of Campus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CampusSet = None
        self._RequestId = None

    @property
    def CampusSet(self):
        """客户可操作的园区列表
        :rtype: list of Campus
        """
        return self._CampusSet

    @CampusSet.setter
    def CampusSet(self, CampusSet):
        self._CampusSet = CampusSet

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
        if params.get("CampusSet") is not None:
            self._CampusSet = []
            for item in params.get("CampusSet"):
                obj = Campus()
                obj._deserialize(item)
                self._CampusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCommonServiceWorkOrderDetailRequest(AbstractModel):
    """DescribeCommonServiceWorkOrderDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 工单ID
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        """工单ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCommonServiceWorkOrderDetailResponse(AbstractModel):
    """DescribeCommonServiceWorkOrderDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StepSet: 进度
        :type StepSet: list of OrderStep
        :param _BaseInfo: 基本信息
        :type BaseInfo: :class:`tencentcloud.chc.v20230418.models.CommonServiceBaseInfo`
        :param _DeviceSet: 设备信息
        :type DeviceSet: list of DevicePosition
        :param _OrderStatus: 工单状态
        :type OrderStatus: str
        :param _RejectReason: 拒绝原因
        :type RejectReason: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StepSet = None
        self._BaseInfo = None
        self._DeviceSet = None
        self._OrderStatus = None
        self._RejectReason = None
        self._RequestId = None

    @property
    def StepSet(self):
        """进度
        :rtype: list of OrderStep
        """
        return self._StepSet

    @StepSet.setter
    def StepSet(self, StepSet):
        self._StepSet = StepSet

    @property
    def BaseInfo(self):
        """基本信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.CommonServiceBaseInfo`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def DeviceSet(self):
        """设备信息
        :rtype: list of DevicePosition
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def OrderStatus(self):
        """工单状态
        :rtype: str
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def RejectReason(self):
        """拒绝原因
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason

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
        if params.get("StepSet") is not None:
            self._StepSet = []
            for item in params.get("StepSet"):
                obj = OrderStep()
                obj._deserialize(item)
                self._StepSet.append(obj)
        if params.get("BaseInfo") is not None:
            self._BaseInfo = CommonServiceBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = DevicePosition()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._OrderStatus = params.get("OrderStatus")
        self._RejectReason = params.get("RejectReason")
        self._RequestId = params.get("RequestId")


class DescribeCustomerInfoRequest(AbstractModel):
    """DescribeCustomerInfo请求参数结构体

    """


class DescribeCustomerInfoResponse(AbstractModel):
    """DescribeCustomerInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomerInfo: 客户信息
        :type CustomerInfo: :class:`tencentcloud.chc.v20230418.models.CustomerInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CustomerInfo = None
        self._RequestId = None

    @property
    def CustomerInfo(self):
        """客户信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.CustomerInfo`
        """
        return self._CustomerInfo

    @CustomerInfo.setter
    def CustomerInfo(self, CustomerInfo):
        self._CustomerInfo = CustomerInfo

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
        if params.get("CustomerInfo") is not None:
            self._CustomerInfo = CustomerInfo()
            self._CustomerInfo._deserialize(params.get("CustomerInfo"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    """DescribeDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceType: 设备类型 server 服务器，netDevice 网络设备，otherDevice 其他设备
        :type DeviceType: str
        :param _Filters: 
<li><strong>rack-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机架ID</strong>】进行过滤。例如：15082。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"></p> <li><strong> sn</strong></li> <p style="padding-left: 30px;">按照【<strong>设备 SN 码</strong>】进行过滤，设备 SN 例如：TEN948P004。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong> idc-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机房ID</strong>】进行过滤，机房ID例如：159。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>  <li><strong>idc-unit-id </strong></li> <p style="padding-left: 30px;">按照【<strong>机房管理单元ID</strong>】进行过滤，机房管理ID例如：568。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>server-type-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机器子类型</strong>】进行过滤，只包含以下几种：1:服务器, 2:Twins主机, 3:Twins子机,5:虚拟机, 6:2U4S主机, 7:2U4S子机,8 Rack主机,9 Rack子机，例如： 1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>status</strong></li> <p style="padding-left: 30px;">按照【<strong>设备状态</strong>】进行过滤，操作状态只包含：POWER_ON 设备开电，POWER_OFF 设备关电，RACK_OFF 未上架，MOVING 搬迁中 。例如： POWER_OFF。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>svr-is-special</strong></li> <p style="padding-left: 30px;">按照【<strong>是否</strong>】进行过滤，支持 0：自有，1 租用。例如： 1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>

        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为1000
        :type Limit: int
        :param _DstService: 传入目标服务，返回允许进行此服务的设备列表；可以和Filters一起使用。允许的值：('rackOn', 'powerOn', 'powerOff', 'rackOff', 'quit', 'moving'，'netDeviceCommon', 'serverCommon')
        :type DstService: str
        """
        self._DeviceType = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._DstService = None

    @property
    def DeviceType(self):
        """设备类型 server 服务器，netDevice 网络设备，otherDevice 其他设备
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Filters(self):
        """
<li><strong>rack-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机架ID</strong>】进行过滤。例如：15082。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"></p> <li><strong> sn</strong></li> <p style="padding-left: 30px;">按照【<strong>设备 SN 码</strong>】进行过滤，设备 SN 例如：TEN948P004。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong> idc-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机房ID</strong>】进行过滤，机房ID例如：159。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>  <li><strong>idc-unit-id </strong></li> <p style="padding-left: 30px;">按照【<strong>机房管理单元ID</strong>】进行过滤，机房管理ID例如：568。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>server-type-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机器子类型</strong>】进行过滤，只包含以下几种：1:服务器, 2:Twins主机, 3:Twins子机,5:虚拟机, 6:2U4S主机, 7:2U4S子机,8 Rack主机,9 Rack子机，例如： 1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>status</strong></li> <p style="padding-left: 30px;">按照【<strong>设备状态</strong>】进行过滤，操作状态只包含：POWER_ON 设备开电，POWER_OFF 设备关电，RACK_OFF 未上架，MOVING 搬迁中 。例如： POWER_OFF。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>svr-is-special</strong></li> <p style="padding-left: 30px;">按照【<strong>是否</strong>】进行过滤，支持 0：自有，1 租用。例如： 1。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>

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
        """返回数量，默认为20，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def DstService(self):
        """传入目标服务，返回允许进行此服务的设备列表；可以和Filters一起使用。允许的值：('rackOn', 'powerOn', 'powerOff', 'rackOff', 'quit', 'moving'，'netDeviceCommon', 'serverCommon')
        :rtype: str
        """
        return self._DstService

    @DstService.setter
    def DstService(self, DstService):
        self._DstService = DstService


    def _deserialize(self, params):
        self._DeviceType = params.get("DeviceType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DstService = params.get("DstService")
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
        :param _Total: 总数
        :type Total: int
        :param _DeviceSet: 服务器列表
        :type DeviceSet: list of Device
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DeviceSet = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DeviceSet(self):
        """服务器列表
        :rtype: list of Device
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

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
        self._Total = params.get("Total")
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = Device()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceWorkOrderDetailRequest(AbstractModel):
    """DescribeDeviceWorkOrderDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 工单ID
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        """工单ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceWorkOrderDetailResponse(AbstractModel):
    """DescribeDeviceWorkOrderDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 工单ID
        :type OrderId: str
        :param _ServiceType: 服务类型
        :type ServiceType: str
        :param _OrderType: 工单类型
        :type OrderType: str
        :param _OrderStatus: 工单状态
        :type OrderStatus: str
        :param _StepSet: 工单流程状态
        :type StepSet: list of OrderStep
        :param _DeviceSet: 工单设备信息
        :type DeviceSet: list of DeviceHistory
        :param _BaseInfo: 工单的入参信息
        :type BaseInfo: :class:`tencentcloud.chc.v20230418.models.DeviceOrderBaseInfo`
        :param _RejectReason: 工单的拒绝原因，工单状态为reject的时候返回
        :type RejectReason: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._ServiceType = None
        self._OrderType = None
        self._OrderStatus = None
        self._StepSet = None
        self._DeviceSet = None
        self._BaseInfo = None
        self._RejectReason = None
        self._RequestId = None

    @property
    def OrderId(self):
        """工单ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ServiceType(self):
        """服务类型
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def OrderType(self):
        """工单类型
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def OrderStatus(self):
        """工单状态
        :rtype: str
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def StepSet(self):
        """工单流程状态
        :rtype: list of OrderStep
        """
        return self._StepSet

    @StepSet.setter
    def StepSet(self, StepSet):
        self._StepSet = StepSet

    @property
    def DeviceSet(self):
        """工单设备信息
        :rtype: list of DeviceHistory
        """
        return self._DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet):
        self._DeviceSet = DeviceSet

    @property
    def BaseInfo(self):
        """工单的入参信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.DeviceOrderBaseInfo`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def RejectReason(self):
        """工单的拒绝原因，工单状态为reject的时候返回
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason

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
        self._OrderId = params.get("OrderId")
        self._ServiceType = params.get("ServiceType")
        self._OrderType = params.get("OrderType")
        self._OrderStatus = params.get("OrderStatus")
        if params.get("StepSet") is not None:
            self._StepSet = []
            for item in params.get("StepSet"):
                obj = OrderStep()
                obj._deserialize(item)
                self._StepSet.append(obj)
        if params.get("DeviceSet") is not None:
            self._DeviceSet = []
            for item in params.get("DeviceSet"):
                obj = DeviceHistory()
                obj._deserialize(item)
                self._DeviceSet.append(obj)
        if params.get("BaseInfo") is not None:
            self._BaseInfo = DeviceOrderBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        self._RejectReason = params.get("RejectReason")
        self._RequestId = params.get("RequestId")


class DescribeIdcUnitAssetDetailRequest(AbstractModel):
    """DescribeIdcUnitAssetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcUnitId: 机房管理单元ID
        :type IdcUnitId: int
        """
        self._IdcUnitId = None

    @property
    def IdcUnitId(self):
        """机房管理单元ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId


    def _deserialize(self, params):
        self._IdcUnitId = params.get("IdcUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdcUnitAssetDetailResponse(AbstractModel):
    """DescribeIdcUnitAssetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcUnitDetail: 机房管理单元详情
        :type IdcUnitDetail: :class:`tencentcloud.chc.v20230418.models.IdcUnitInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdcUnitDetail = None
        self._RequestId = None

    @property
    def IdcUnitDetail(self):
        """机房管理单元详情
        :rtype: :class:`tencentcloud.chc.v20230418.models.IdcUnitInfo`
        """
        return self._IdcUnitDetail

    @IdcUnitDetail.setter
    def IdcUnitDetail(self, IdcUnitDetail):
        self._IdcUnitDetail = IdcUnitDetail

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
        if params.get("IdcUnitDetail") is not None:
            self._IdcUnitDetail = IdcUnitInfo()
            self._IdcUnitDetail._deserialize(params.get("IdcUnitDetail"))
        self._RequestId = params.get("RequestId")


class DescribeIdcUnitDetailRequest(AbstractModel):
    """DescribeIdcUnitDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcUnitId: 机房管理单元ID
        :type IdcUnitId: int
        """
        self._IdcUnitId = None

    @property
    def IdcUnitId(self):
        """机房管理单元ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId


    def _deserialize(self, params):
        self._IdcUnitId = params.get("IdcUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIdcUnitDetailResponse(AbstractModel):
    """DescribeIdcUnitDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcUnitDetail: 机房管理单元详情
        :type IdcUnitDetail: :class:`tencentcloud.chc.v20230418.models.IdcUnitInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdcUnitDetail = None
        self._RequestId = None

    @property
    def IdcUnitDetail(self):
        """机房管理单元详情
        :rtype: :class:`tencentcloud.chc.v20230418.models.IdcUnitInfo`
        """
        return self._IdcUnitDetail

    @IdcUnitDetail.setter
    def IdcUnitDetail(self, IdcUnitDetail):
        self._IdcUnitDetail = IdcUnitDetail

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
        if params.get("IdcUnitDetail") is not None:
            self._IdcUnitDetail = IdcUnitInfo()
            self._IdcUnitDetail._deserialize(params.get("IdcUnitDetail"))
        self._RequestId = params.get("RequestId")


class DescribeIdcsRequest(AbstractModel):
    """DescribeIdcs请求参数结构体

    """


class DescribeIdcsResponse(AbstractModel):
    """DescribeIdcs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcSet: 机房管理单元列表
        :type IdcSet: list of Idc
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdcSet = None
        self._RequestId = None

    @property
    def IdcSet(self):
        """机房管理单元列表
        :rtype: list of Idc
        """
        return self._IdcSet

    @IdcSet.setter
    def IdcSet(self, IdcSet):
        self._IdcSet = IdcSet

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
        if params.get("IdcSet") is not None:
            self._IdcSet = []
            for item in params.get("IdcSet"):
                obj = Idc()
                obj._deserialize(item)
                self._IdcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModelEvaluationWorkOrderDetailRequest(AbstractModel):
    """DescribeModelEvaluationWorkOrderDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 工单ID
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        """工单ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelEvaluationWorkOrderDetailResponse(AbstractModel):
    """DescribeModelEvaluationWorkOrderDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StepSet: 工单进度
        :type StepSet: list of OrderStep
        :param _BaseInfo: 工单详情
        :type BaseInfo: :class:`tencentcloud.chc.v20230418.models.ModelEvaluationBaseInfo`
        :param _NetDeviceModelSet: 评估中的网络设备型号详情
        :type NetDeviceModelSet: list of ModelVersionDetail
        :param _ServerModelSet: 评估中的服务器型号详情
        :type ServerModelSet: list of ModelVersionDetail
        :param _OrderStatus: 订单状态, process 处理中 ，reject 已拒绝 ，finish 已完成，exception 异常
        :type OrderStatus: str
        :param _RejectReason: 工单拒绝原因
        :type RejectReason: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StepSet = None
        self._BaseInfo = None
        self._NetDeviceModelSet = None
        self._ServerModelSet = None
        self._OrderStatus = None
        self._RejectReason = None
        self._RequestId = None

    @property
    def StepSet(self):
        """工单进度
        :rtype: list of OrderStep
        """
        return self._StepSet

    @StepSet.setter
    def StepSet(self, StepSet):
        self._StepSet = StepSet

    @property
    def BaseInfo(self):
        """工单详情
        :rtype: :class:`tencentcloud.chc.v20230418.models.ModelEvaluationBaseInfo`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def NetDeviceModelSet(self):
        """评估中的网络设备型号详情
        :rtype: list of ModelVersionDetail
        """
        return self._NetDeviceModelSet

    @NetDeviceModelSet.setter
    def NetDeviceModelSet(self, NetDeviceModelSet):
        self._NetDeviceModelSet = NetDeviceModelSet

    @property
    def ServerModelSet(self):
        """评估中的服务器型号详情
        :rtype: list of ModelVersionDetail
        """
        return self._ServerModelSet

    @ServerModelSet.setter
    def ServerModelSet(self, ServerModelSet):
        self._ServerModelSet = ServerModelSet

    @property
    def OrderStatus(self):
        """订单状态, process 处理中 ，reject 已拒绝 ，finish 已完成，exception 异常
        :rtype: str
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def RejectReason(self):
        """工单拒绝原因
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason

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
        if params.get("StepSet") is not None:
            self._StepSet = []
            for item in params.get("StepSet"):
                obj = OrderStep()
                obj._deserialize(item)
                self._StepSet.append(obj)
        if params.get("BaseInfo") is not None:
            self._BaseInfo = ModelEvaluationBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("NetDeviceModelSet") is not None:
            self._NetDeviceModelSet = []
            for item in params.get("NetDeviceModelSet"):
                obj = ModelVersionDetail()
                obj._deserialize(item)
                self._NetDeviceModelSet.append(obj)
        if params.get("ServerModelSet") is not None:
            self._ServerModelSet = []
            for item in params.get("ServerModelSet"):
                obj = ModelVersionDetail()
                obj._deserialize(item)
                self._ServerModelSet.append(obj)
        self._OrderStatus = params.get("OrderStatus")
        self._RejectReason = params.get("RejectReason")
        self._RequestId = params.get("RequestId")


class DescribeModelRequest(AbstractModel):
    """DescribeModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DevModel: 服务器设备型号
        :type DevModel: str
        :param _CampusId: 园区ID
        :type CampusId: int
        :param _DeviceType: 设备类型，服务器传入 server，网络设备传入 netDevice
        :type DeviceType: str
        :param _Checked: 是否只返回已评估的版本
        :type Checked: bool
        """
        self._DevModel = None
        self._CampusId = None
        self._DeviceType = None
        self._Checked = None

    @property
    def DevModel(self):
        """服务器设备型号
        :rtype: str
        """
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def CampusId(self):
        """园区ID
        :rtype: int
        """
        return self._CampusId

    @CampusId.setter
    def CampusId(self, CampusId):
        self._CampusId = CampusId

    @property
    def DeviceType(self):
        """设备类型，服务器传入 server，网络设备传入 netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Checked(self):
        """是否只返回已评估的版本
        :rtype: bool
        """
        return self._Checked

    @Checked.setter
    def Checked(self, Checked):
        self._Checked = Checked


    def _deserialize(self, params):
        self._DevModel = params.get("DevModel")
        self._CampusId = params.get("CampusId")
        self._DeviceType = params.get("DeviceType")
        self._Checked = params.get("Checked")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelResponse(AbstractModel):
    """DescribeModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelSet: 设备型号详情
        :type ModelSet: list of ModelVersionDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelSet = None
        self._RequestId = None

    @property
    def ModelSet(self):
        """设备型号详情
        :rtype: list of ModelVersionDetail
        """
        return self._ModelSet

    @ModelSet.setter
    def ModelSet(self, ModelSet):
        self._ModelSet = ModelSet

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
        if params.get("ModelSet") is not None:
            self._ModelSet = []
            for item in params.get("ModelSet"):
                obj = ModelVersionDetail()
                obj._deserialize(item)
                self._ModelSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModelTemplateRequest(AbstractModel):
    """DescribeModelTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceType: 型号类型，只支持传入 server 和 netDevice
        :type DeviceType: str
        """
        self._DeviceType = None

    @property
    def DeviceType(self):
        """型号类型，只支持传入 server 和 netDevice
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelTemplateResponse(AbstractModel):
    """DescribeModelTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateDetail: 该型号模板的选项列表
        :type TemplateDetail: list of TemplateOption
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateDetail = None
        self._RequestId = None

    @property
    def TemplateDetail(self):
        """该型号模板的选项列表
        :rtype: list of TemplateOption
        """
        return self._TemplateDetail

    @TemplateDetail.setter
    def TemplateDetail(self, TemplateDetail):
        self._TemplateDetail = TemplateDetail

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
        if params.get("TemplateDetail") is not None:
            self._TemplateDetail = []
            for item in params.get("TemplateDetail"):
                obj = TemplateOption()
                obj._deserialize(item)
                self._TemplateDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModelVersionListRequest(AbstractModel):
    """DescribeModelVersionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceType: 型号类型，只支持传入 netDevice 和 server
        :type DeviceType: str
        :param _Filters: model-name  型号名称  类型：String  必选：否
        :type Filters: list of Filter
        :param _Checked: 是否已评估
        :type Checked: bool
        :param _CampusId: 园区ID，当 Checked 参数传 True 时，该参数必须传值
        :type CampusId: int
        """
        self._DeviceType = None
        self._Filters = None
        self._Checked = None
        self._CampusId = None

    @property
    def DeviceType(self):
        """型号类型，只支持传入 netDevice 和 server
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Filters(self):
        """model-name  型号名称  类型：String  必选：否
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Checked(self):
        """是否已评估
        :rtype: bool
        """
        return self._Checked

    @Checked.setter
    def Checked(self, Checked):
        self._Checked = Checked

    @property
    def CampusId(self):
        """园区ID，当 Checked 参数传 True 时，该参数必须传值
        :rtype: int
        """
        return self._CampusId

    @CampusId.setter
    def CampusId(self, CampusId):
        self._CampusId = CampusId


    def _deserialize(self, params):
        self._DeviceType = params.get("DeviceType")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Checked = params.get("Checked")
        self._CampusId = params.get("CampusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelVersionListResponse(AbstractModel):
    """DescribeModelVersionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelVersionSet: 型号和对应的版本数量
        :type ModelVersionSet: list of ModelVersionCount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelVersionSet = None
        self._RequestId = None

    @property
    def ModelVersionSet(self):
        """型号和对应的版本数量
        :rtype: list of ModelVersionCount
        """
        return self._ModelVersionSet

    @ModelVersionSet.setter
    def ModelVersionSet(self, ModelVersionSet):
        self._ModelVersionSet = ModelVersionSet

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
        if params.get("ModelVersionSet") is not None:
            self._ModelVersionSet = []
            for item in params.get("ModelVersionSet"):
                obj = ModelVersionCount()
                obj._deserialize(item)
                self._ModelVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePersonnelVisitWorkOrderDetailRequest(AbstractModel):
    """DescribePersonnelVisitWorkOrderDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 工单ID
        :type OrderId: str
        """
        self._OrderId = None

    @property
    def OrderId(self):
        """工单ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonnelVisitWorkOrderDetailResponse(AbstractModel):
    """DescribePersonnelVisitWorkOrderDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StepSet: 工单进度	
        :type StepSet: list of OrderStep
        :param _BaseInfo: 工单详情
        :type BaseInfo: :class:`tencentcloud.chc.v20230418.models.PersonnelVisitBaseInfo`
        :param _PersonnelSet: 到访人员详情
        :type PersonnelSet: list of Personnel
        :param _OrderStatus: 工单状态 订单状态, processing 处理中 ，reject 已拒绝 ，finish 已完成，exception 异常
        :type OrderStatus: str
        :param _RejectReason: 拒绝原因
        :type RejectReason: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StepSet = None
        self._BaseInfo = None
        self._PersonnelSet = None
        self._OrderStatus = None
        self._RejectReason = None
        self._RequestId = None

    @property
    def StepSet(self):
        """工单进度	
        :rtype: list of OrderStep
        """
        return self._StepSet

    @StepSet.setter
    def StepSet(self, StepSet):
        self._StepSet = StepSet

    @property
    def BaseInfo(self):
        """工单详情
        :rtype: :class:`tencentcloud.chc.v20230418.models.PersonnelVisitBaseInfo`
        """
        return self._BaseInfo

    @BaseInfo.setter
    def BaseInfo(self, BaseInfo):
        self._BaseInfo = BaseInfo

    @property
    def PersonnelSet(self):
        """到访人员详情
        :rtype: list of Personnel
        """
        return self._PersonnelSet

    @PersonnelSet.setter
    def PersonnelSet(self, PersonnelSet):
        self._PersonnelSet = PersonnelSet

    @property
    def OrderStatus(self):
        """工单状态 订单状态, processing 处理中 ，reject 已拒绝 ，finish 已完成，exception 异常
        :rtype: str
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def RejectReason(self):
        """拒绝原因
        :rtype: str
        """
        return self._RejectReason

    @RejectReason.setter
    def RejectReason(self, RejectReason):
        self._RejectReason = RejectReason

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
        if params.get("StepSet") is not None:
            self._StepSet = []
            for item in params.get("StepSet"):
                obj = OrderStep()
                obj._deserialize(item)
                self._StepSet.append(obj)
        if params.get("BaseInfo") is not None:
            self._BaseInfo = PersonnelVisitBaseInfo()
            self._BaseInfo._deserialize(params.get("BaseInfo"))
        if params.get("PersonnelSet") is not None:
            self._PersonnelSet = []
            for item in params.get("PersonnelSet"):
                obj = Personnel()
                obj._deserialize(item)
                self._PersonnelSet.append(obj)
        self._OrderStatus = params.get("OrderStatus")
        self._RejectReason = params.get("RejectReason")
        self._RequestId = params.get("RequestId")


class DescribePositionStatusSummaryRequest(AbstractModel):
    """DescribePositionStatusSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <li><strong>rack-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机架ID</strong>】进行过滤。例如：15082。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"></p> <li><strong> rack-name</strong></li> <p style="padding-left: 30px;">按照【<strong>机架名称</strong>】进行过滤，机架名称例如：M301-E10。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong> idc-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机房ID</strong>】进行过滤，机房ID例如：159。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>  <li><strong>idc-unit-id </strong></li> <p style="padding-left: 30px;">按照【<strong>机房管理单元ID</strong>】进行过滤，机房管理ID例如：568。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>position-status</strong></li> <p style="padding-left: 30px;">按照【<strong>机位状态</strong>】进行过滤，机位状态只包含以下四种：机位状态,0 空闲,1 已用,2 不可用,3 预占用,4 预留，例如： 0。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>op-status</strong></li> <p style="padding-left: 30px;">按照【<strong>操作状态</strong>】进行过滤，操作状态只包含两种：FINISH 操作完成，PENDING 操作中，例如： PENDING。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """<li><strong>rack-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机架ID</strong>】进行过滤。例如：15082。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"></p> <li><strong> rack-name</strong></li> <p style="padding-left: 30px;">按照【<strong>机架名称</strong>】进行过滤，机架名称例如：M301-E10。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong> idc-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机房ID</strong>】进行过滤，机房ID例如：159。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>  <li><strong>idc-unit-id </strong></li> <p style="padding-left: 30px;">按照【<strong>机房管理单元ID</strong>】进行过滤，机房管理ID例如：568。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>position-status</strong></li> <p style="padding-left: 30px;">按照【<strong>机位状态</strong>】进行过滤，机位状态只包含以下四种：机位状态,0 空闲,1 已用,2 不可用,3 预占用,4 预留，例如： 0。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>op-status</strong></li> <p style="padding-left: 30px;">按照【<strong>操作状态</strong>】进行过滤，操作状态只包含两种：FINISH 操作完成，PENDING 操作中，例如： PENDING。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribePositionStatusSummaryResponse(AbstractModel):
    """DescribePositionStatusSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _StatusCountSet: 状态及对应数量
        :type StatusCountSet: list of PositionStatusItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._StatusCountSet = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def StatusCountSet(self):
        """状态及对应数量
        :rtype: list of PositionStatusItem
        """
        return self._StatusCountSet

    @StatusCountSet.setter
    def StatusCountSet(self, StatusCountSet):
        self._StatusCountSet = StatusCountSet

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
        self._Total = params.get("Total")
        if params.get("StatusCountSet") is not None:
            self._StatusCountSet = []
            for item in params.get("StatusCountSet"):
                obj = PositionStatusItem()
                obj._deserialize(item)
                self._StatusCountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePositionsRequest(AbstractModel):
    """DescribePositions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        :param _Filters: <li><strong>rack-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机架ID</strong>】进行过滤。例如：15082。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"></p> <li><strong> rack-name</strong></li> <p style="padding-left: 30px;">按照【<strong>机架名称</strong>】进行过滤，机架名称例如：M301-E10。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong> idc-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机房ID</strong>】进行过滤，机房ID例如：159。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>  <li><strong>idc-unit-id </strong></li> <p style="padding-left: 30px;">按照【<strong>机房管理单元ID</strong>】进行过滤，机房管理ID例如：568。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>position-status</strong></li> <p style="padding-left: 30px;">按照【<strong>机位状态</strong>】进行过滤，机位状态只包含以下四种：机位状态,0 空闲,1 已用,2 不可用,3 预占用,4 预留，例如： 0。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>op-status</strong></li> <p style="padding-left: 30px;">按照【<strong>操作状态</strong>】进行过滤，操作状态只包含两种：FINISH 操作完成，PENDING 操作中，例如： PENDING。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>

        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """<li><strong>rack-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机架ID</strong>】进行过滤。例如：15082。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"></p> <li><strong> rack-name</strong></li> <p style="padding-left: 30px;">按照【<strong>机架名称</strong>】进行过滤，机架名称例如：M301-E10。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong> idc-id</strong></li> <p style="padding-left: 30px;">按照【<strong>机房ID</strong>】进行过滤，机房ID例如：159。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>  <li><strong>idc-unit-id </strong></li> <p style="padding-left: 30px;">按照【<strong>机房管理单元ID</strong>】进行过滤，机房管理ID例如：568。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p> <li><strong>position-status</strong></li> <p style="padding-left: 30px;">按照【<strong>机位状态</strong>】进行过滤，机位状态只包含以下四种：机位状态,0 空闲,1 已用,2 不可用,3 预占用,4 预留，例如： 0。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>
<li><strong>op-status</strong></li> <p style="padding-left: 30px;">按照【<strong>操作状态</strong>】进行过滤，操作状态只包含两种：FINISH 操作完成，PENDING 操作中，例如： PENDING。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p>

        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribePositionsResponse(AbstractModel):
    """DescribePositions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PositionSet: 客户拥有的机位列表
        :type PositionSet: list of Position
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PositionSet = None
        self._Total = None
        self._RequestId = None

    @property
    def PositionSet(self):
        """客户拥有的机位列表
        :rtype: list of Position
        """
        return self._PositionSet

    @PositionSet.setter
    def PositionSet(self, PositionSet):
        self._PositionSet = PositionSet

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("PositionSet") is not None:
            self._PositionSet = []
            for item in params.get("PositionSet"):
                obj = Position()
                obj._deserialize(item)
                self._PositionSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeRacksDistributionRequest(AbstractModel):
    """DescribeRacksDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdcUnitId: 机房管理单元ID
        :type IdcUnitId: int
        """
        self._IdcUnitId = None

    @property
    def IdcUnitId(self):
        """机房管理单元ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId


    def _deserialize(self, params):
        self._IdcUnitId = params.get("IdcUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRacksDistributionResponse(AbstractModel):
    """DescribeRacksDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DistributionSet: 机架的用量分布
        :type DistributionSet: list of Distribution
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DistributionSet = None
        self._RequestId = None

    @property
    def DistributionSet(self):
        """机架的用量分布
        :rtype: list of Distribution
        """
        return self._DistributionSet

    @DistributionSet.setter
    def DistributionSet(self, DistributionSet):
        self._DistributionSet = DistributionSet

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
        if params.get("DistributionSet") is not None:
            self._DistributionSet = []
            for item in params.get("DistributionSet"):
                obj = Distribution()
                obj._deserialize(item)
                self._DistributionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRacksRequest(AbstractModel):
    """DescribeRacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        :param _Filters: 过滤条件

rack-id
按照机架id进行过滤。
类型：String
必选：否

rack-name
按照机架名称进行过滤。
类型：String
必选：否

idc-id
按照机房id进行过滤。
类型：String
必选：否

idc-unit-id
按照机房管理单元id过滤
类型： String
必选： 否

is-power-on
按照是否开电进行过滤，支持传入 0 和 1。1 代表开电，0 代表关电
类型： String
必选： 否

hosting-type
按照托管类型进行过滤。支持传入 CUSTOMER_MIX 代表客户混合，CUSTOMER_ONLY 代表客户独享 ，NOT_INIT 代表未初始化
类型： String
必选： 否


        :type Filters: list of Filter
        :param _DstService: 传入目标服务，返回允许进行此服务的机架列表；可以和Filters一起使用。允许的值：('rackPowerOn', 'rackPowerOff')
        :type DstService: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._DstService = None

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤条件

rack-id
按照机架id进行过滤。
类型：String
必选：否

rack-name
按照机架名称进行过滤。
类型：String
必选：否

idc-id
按照机房id进行过滤。
类型：String
必选：否

idc-unit-id
按照机房管理单元id过滤
类型： String
必选： 否

is-power-on
按照是否开电进行过滤，支持传入 0 和 1。1 代表开电，0 代表关电
类型： String
必选： 否

hosting-type
按照托管类型进行过滤。支持传入 CUSTOMER_MIX 代表客户混合，CUSTOMER_ONLY 代表客户独享 ，NOT_INIT 代表未初始化
类型： String
必选： 否


        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DstService(self):
        """传入目标服务，返回允许进行此服务的机架列表；可以和Filters一起使用。允许的值：('rackPowerOn', 'rackPowerOff')
        :rtype: str
        """
        return self._DstService

    @DstService.setter
    def DstService(self, DstService):
        self._DstService = DstService


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DstService = params.get("DstService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRacksResponse(AbstractModel):
    """DescribeRacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RackSet: 客户拥有的机架列表
        :type RackSet: list of Rack
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RackSet = None
        self._Total = None
        self._RequestId = None

    @property
    def RackSet(self):
        """客户拥有的机架列表
        :rtype: list of Rack
        """
        return self._RackSet

    @RackSet.setter
    def RackSet(self, RackSet):
        self._RackSet = RackSet

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("RackSet") is not None:
            self._RackSet = []
            for item in params.get("RackSet"):
                obj = Rack()
                obj._deserialize(item)
                self._RackSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeResourceUsageRequest(AbstractModel):
    """DescribeResourceUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeResourceUsageResponse(AbstractModel):
    """DescribeResourceUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HostingServerCount: 托管服务器数量
        :type HostingServerCount: int
        :param _RentServerCount: 租用服务器数量
        :type RentServerCount: int
        :param _NetDeviceCount: 网络设备数量
        :type NetDeviceCount: int
        :param _RackTotalCount: 机架总数
        :type RackTotalCount: int
        :param _RackPowerOnCount: 开电机架总数
        :type RackPowerOnCount: int
        :param _PositionUsedCount: 机位使用数量
        :type PositionUsedCount: int
        :param _PositionTotalCount: 机位总数
        :type PositionTotalCount: int
        :param _RackPowerOnRate: 机架开电率，保留一位小数
        :type RackPowerOnRate: str
        :param _PositionUsedRate: 机位使用率，
        :type PositionUsedRate: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HostingServerCount = None
        self._RentServerCount = None
        self._NetDeviceCount = None
        self._RackTotalCount = None
        self._RackPowerOnCount = None
        self._PositionUsedCount = None
        self._PositionTotalCount = None
        self._RackPowerOnRate = None
        self._PositionUsedRate = None
        self._RequestId = None

    @property
    def HostingServerCount(self):
        """托管服务器数量
        :rtype: int
        """
        return self._HostingServerCount

    @HostingServerCount.setter
    def HostingServerCount(self, HostingServerCount):
        self._HostingServerCount = HostingServerCount

    @property
    def RentServerCount(self):
        """租用服务器数量
        :rtype: int
        """
        return self._RentServerCount

    @RentServerCount.setter
    def RentServerCount(self, RentServerCount):
        self._RentServerCount = RentServerCount

    @property
    def NetDeviceCount(self):
        """网络设备数量
        :rtype: int
        """
        return self._NetDeviceCount

    @NetDeviceCount.setter
    def NetDeviceCount(self, NetDeviceCount):
        self._NetDeviceCount = NetDeviceCount

    @property
    def RackTotalCount(self):
        """机架总数
        :rtype: int
        """
        return self._RackTotalCount

    @RackTotalCount.setter
    def RackTotalCount(self, RackTotalCount):
        self._RackTotalCount = RackTotalCount

    @property
    def RackPowerOnCount(self):
        """开电机架总数
        :rtype: int
        """
        return self._RackPowerOnCount

    @RackPowerOnCount.setter
    def RackPowerOnCount(self, RackPowerOnCount):
        self._RackPowerOnCount = RackPowerOnCount

    @property
    def PositionUsedCount(self):
        """机位使用数量
        :rtype: int
        """
        return self._PositionUsedCount

    @PositionUsedCount.setter
    def PositionUsedCount(self, PositionUsedCount):
        self._PositionUsedCount = PositionUsedCount

    @property
    def PositionTotalCount(self):
        """机位总数
        :rtype: int
        """
        return self._PositionTotalCount

    @PositionTotalCount.setter
    def PositionTotalCount(self, PositionTotalCount):
        self._PositionTotalCount = PositionTotalCount

    @property
    def RackPowerOnRate(self):
        """机架开电率，保留一位小数
        :rtype: str
        """
        return self._RackPowerOnRate

    @RackPowerOnRate.setter
    def RackPowerOnRate(self, RackPowerOnRate):
        self._RackPowerOnRate = RackPowerOnRate

    @property
    def PositionUsedRate(self):
        """机位使用率，
        :rtype: str
        """
        return self._PositionUsedRate

    @PositionUsedRate.setter
    def PositionUsedRate(self, PositionUsedRate):
        self._PositionUsedRate = PositionUsedRate

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
        self._HostingServerCount = params.get("HostingServerCount")
        self._RentServerCount = params.get("RentServerCount")
        self._NetDeviceCount = params.get("NetDeviceCount")
        self._RackTotalCount = params.get("RackTotalCount")
        self._RackPowerOnCount = params.get("RackPowerOnCount")
        self._PositionUsedCount = params.get("PositionUsedCount")
        self._PositionTotalCount = params.get("PositionTotalCount")
        self._RackPowerOnRate = params.get("RackPowerOnRate")
        self._PositionUsedRate = params.get("PositionUsedRate")
        self._RequestId = params.get("RequestId")


class DescribeWorkOrderListRequest(AbstractModel):
    """DescribeWorkOrderList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。支持：service-type、order-type、order-status、order-id
        :type Filters: list of Filter
        :param _SnList: 通过sn过滤工单，上限10个
        :type SnList: list of str
        :param _Offset: 起始
        :type Offset: int
        :param _Limit: 长度
        :type Limit: int
        """
        self._Filters = None
        self._SnList = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """过滤条件。支持：service-type、order-type、order-status、order-id
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SnList(self):
        """通过sn过滤工单，上限10个
        :rtype: list of str
        """
        return self._SnList

    @SnList.setter
    def SnList(self, SnList):
        self._SnList = SnList

    @property
    def Offset(self):
        """起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """长度
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SnList = params.get("SnList")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkOrderListResponse(AbstractModel):
    """DescribeWorkOrderList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _WorkOrderSet: 查询结果
        :type WorkOrderSet: list of WorkOrderData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._WorkOrderSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def WorkOrderSet(self):
        """查询结果
        :rtype: list of WorkOrderData
        """
        return self._WorkOrderSet

    @WorkOrderSet.setter
    def WorkOrderSet(self, WorkOrderSet):
        self._WorkOrderSet = WorkOrderSet

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
        if params.get("WorkOrderSet") is not None:
            self._WorkOrderSet = []
            for item in params.get("WorkOrderSet"):
                obj = WorkOrderData()
                obj._deserialize(item)
                self._WorkOrderSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWorkOrderStatisticsRequest(AbstractModel):
    """DescribeWorkOrderStatistics请求参数结构体

    """


class DescribeWorkOrderStatisticsResponse(AbstractModel):
    """DescribeWorkOrderStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 总工单数量
        :type TotalNum: int
        :param _ProcessingNum: 进行中的工单数量
        :type ProcessingNum: int
        :param _ConfirmingNum: 待确认的工单数量
        :type ConfirmingNum: int
        :param _FinishNum: 完成的工单数量
        :type FinishNum: int
        :param _RejectNum: 拒绝的工单数量
        :type RejectNum: int
        :param _ExceptionNum: 异常的工单数量
        :type ExceptionNum: int
        :param _CancelNum: 客户取消的工单数量
        :type CancelNum: int
        :param _CheckingNum: 围笼进出审核的工单数量
        :type CheckingNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._ProcessingNum = None
        self._ConfirmingNum = None
        self._FinishNum = None
        self._RejectNum = None
        self._ExceptionNum = None
        self._CancelNum = None
        self._CheckingNum = None
        self._RequestId = None

    @property
    def TotalNum(self):
        """总工单数量
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def ProcessingNum(self):
        """进行中的工单数量
        :rtype: int
        """
        return self._ProcessingNum

    @ProcessingNum.setter
    def ProcessingNum(self, ProcessingNum):
        self._ProcessingNum = ProcessingNum

    @property
    def ConfirmingNum(self):
        """待确认的工单数量
        :rtype: int
        """
        return self._ConfirmingNum

    @ConfirmingNum.setter
    def ConfirmingNum(self, ConfirmingNum):
        self._ConfirmingNum = ConfirmingNum

    @property
    def FinishNum(self):
        """完成的工单数量
        :rtype: int
        """
        return self._FinishNum

    @FinishNum.setter
    def FinishNum(self, FinishNum):
        self._FinishNum = FinishNum

    @property
    def RejectNum(self):
        """拒绝的工单数量
        :rtype: int
        """
        return self._RejectNum

    @RejectNum.setter
    def RejectNum(self, RejectNum):
        self._RejectNum = RejectNum

    @property
    def ExceptionNum(self):
        """异常的工单数量
        :rtype: int
        """
        return self._ExceptionNum

    @ExceptionNum.setter
    def ExceptionNum(self, ExceptionNum):
        self._ExceptionNum = ExceptionNum

    @property
    def CancelNum(self):
        """客户取消的工单数量
        :rtype: int
        """
        return self._CancelNum

    @CancelNum.setter
    def CancelNum(self, CancelNum):
        self._CancelNum = CancelNum

    @property
    def CheckingNum(self):
        """围笼进出审核的工单数量
        :rtype: int
        """
        return self._CheckingNum

    @CheckingNum.setter
    def CheckingNum(self, CheckingNum):
        self._CheckingNum = CheckingNum

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
        self._TotalNum = params.get("TotalNum")
        self._ProcessingNum = params.get("ProcessingNum")
        self._ConfirmingNum = params.get("ConfirmingNum")
        self._FinishNum = params.get("FinishNum")
        self._RejectNum = params.get("RejectNum")
        self._ExceptionNum = params.get("ExceptionNum")
        self._CancelNum = params.get("CancelNum")
        self._CheckingNum = params.get("CheckingNum")
        self._RequestId = params.get("RequestId")


class DescribeWorkOrderTypesRequest(AbstractModel):
    """DescribeWorkOrderTypes请求参数结构体

    """


class DescribeWorkOrderTypesResponse(AbstractModel):
    """DescribeWorkOrderTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CollectedWorkOderTypeSet: 已收藏的工单类型列表
        :type CollectedWorkOderTypeSet: list of WorkOrderTypeDetail
        :param _WorkOrderFamilySet: 全部工单类型列表
        :type WorkOrderFamilySet: list of WorkOrderFamilyDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CollectedWorkOderTypeSet = None
        self._WorkOrderFamilySet = None
        self._RequestId = None

    @property
    def CollectedWorkOderTypeSet(self):
        """已收藏的工单类型列表
        :rtype: list of WorkOrderTypeDetail
        """
        return self._CollectedWorkOderTypeSet

    @CollectedWorkOderTypeSet.setter
    def CollectedWorkOderTypeSet(self, CollectedWorkOderTypeSet):
        self._CollectedWorkOderTypeSet = CollectedWorkOderTypeSet

    @property
    def WorkOrderFamilySet(self):
        """全部工单类型列表
        :rtype: list of WorkOrderFamilyDetail
        """
        return self._WorkOrderFamilySet

    @WorkOrderFamilySet.setter
    def WorkOrderFamilySet(self, WorkOrderFamilySet):
        self._WorkOrderFamilySet = WorkOrderFamilySet

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
        if params.get("CollectedWorkOderTypeSet") is not None:
            self._CollectedWorkOderTypeSet = []
            for item in params.get("CollectedWorkOderTypeSet"):
                obj = WorkOrderTypeDetail()
                obj._deserialize(item)
                self._CollectedWorkOderTypeSet.append(obj)
        if params.get("WorkOrderFamilySet") is not None:
            self._WorkOrderFamilySet = []
            for item in params.get("WorkOrderFamilySet"):
                obj = WorkOrderFamilyDetail()
                obj._deserialize(item)
                self._WorkOrderFamilySet.append(obj)
        self._RequestId = params.get("RequestId")


class Device(AbstractModel):
    """服务器信息

    """

    def __init__(self):
        r"""
        :param _Sn: 设备 SN 码
        :type Sn: str
        :param _ModelVersion: 设备型号版本
        :type ModelVersion: str
        :param _AssetId: 设备固资号。只有设备类型为服务器时才返回
        :type AssetId: str
        :param _SvrIsSpecial: 0 自有，1 租用。只有设备类型为服务器时才返回
        :type SvrIsSpecial: int
        :param _Ip: IP。
        :type Ip: str
        :param _IdcName: 设备所属的机房名称
        :type IdcName: str
        :param _IdcId: 设备所属的机房ID
        :type IdcId: int
        :param _IdcUnitId: 设备所属的机房管理单元ID
        :type IdcUnitId: int
        :param _IdcUnitName: 设备所属的机房管理单元名称
        :type IdcUnitName: str
        :param _RackId: 已上架设备所在的机架ID，未上架设备不返回
        :type RackId: int
        :param _ServerTypeId: 服务器类型， 1 代表服务器， 7 代表 2U4S。只有设备类型为服务器时才返回
        :type ServerTypeId: int
        :param _RackName: 已上架设备所在的机架名称，未上架设备不返回
        :type RackName: str
        :param _PositionCode: 已上架设备所在的机位编号，未上架设备不返回。只有设备类型为服务器时才返回
        :type PositionCode: int
        :param _Status: 设备状态：POWER_ON 已开电 POWER_OFF 未开电 RACK_OFF 未上架 MOVING 搬迁中
        :type Status: str
        :param _PowerOnTime: 设备最近一次的开电时间，YYYY-MM-DD 格式。
        :type PowerOnTime: str
        :param _OnshelfDate: 设备最近一次的上架时间，YYYY-MM-DD 格式。
        :type OnshelfDate: str
        :param _DeviceType: 设备类型 server 服务器，netDevice 网络设备
        :type DeviceType: str
        :param _Manufacturer: 厂商
        :type Manufacturer: str
        :param _TypeName: 其他设备-设备子类型
        :type TypeName: str
        :param _HardwareMemo: 硬件备注
        :type HardwareMemo: str
        """
        self._Sn = None
        self._ModelVersion = None
        self._AssetId = None
        self._SvrIsSpecial = None
        self._Ip = None
        self._IdcName = None
        self._IdcId = None
        self._IdcUnitId = None
        self._IdcUnitName = None
        self._RackId = None
        self._ServerTypeId = None
        self._RackName = None
        self._PositionCode = None
        self._Status = None
        self._PowerOnTime = None
        self._OnshelfDate = None
        self._DeviceType = None
        self._Manufacturer = None
        self._TypeName = None
        self._HardwareMemo = None

    @property
    def Sn(self):
        """设备 SN 码
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def ModelVersion(self):
        """设备型号版本
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def AssetId(self):
        """设备固资号。只有设备类型为服务器时才返回
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def SvrIsSpecial(self):
        """0 自有，1 租用。只有设备类型为服务器时才返回
        :rtype: int
        """
        return self._SvrIsSpecial

    @SvrIsSpecial.setter
    def SvrIsSpecial(self, SvrIsSpecial):
        self._SvrIsSpecial = SvrIsSpecial

    @property
    def Ip(self):
        """IP。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def IdcName(self):
        """设备所属的机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def IdcId(self):
        """设备所属的机房ID
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def IdcUnitId(self):
        """设备所属的机房管理单元ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId

    @property
    def IdcUnitName(self):
        """设备所属的机房管理单元名称
        :rtype: str
        """
        return self._IdcUnitName

    @IdcUnitName.setter
    def IdcUnitName(self, IdcUnitName):
        self._IdcUnitName = IdcUnitName

    @property
    def RackId(self):
        """已上架设备所在的机架ID，未上架设备不返回
        :rtype: int
        """
        return self._RackId

    @RackId.setter
    def RackId(self, RackId):
        self._RackId = RackId

    @property
    def ServerTypeId(self):
        """服务器类型， 1 代表服务器， 7 代表 2U4S。只有设备类型为服务器时才返回
        :rtype: int
        """
        return self._ServerTypeId

    @ServerTypeId.setter
    def ServerTypeId(self, ServerTypeId):
        self._ServerTypeId = ServerTypeId

    @property
    def RackName(self):
        """已上架设备所在的机架名称，未上架设备不返回
        :rtype: str
        """
        return self._RackName

    @RackName.setter
    def RackName(self, RackName):
        self._RackName = RackName

    @property
    def PositionCode(self):
        """已上架设备所在的机位编号，未上架设备不返回。只有设备类型为服务器时才返回
        :rtype: int
        """
        return self._PositionCode

    @PositionCode.setter
    def PositionCode(self, PositionCode):
        self._PositionCode = PositionCode

    @property
    def Status(self):
        """设备状态：POWER_ON 已开电 POWER_OFF 未开电 RACK_OFF 未上架 MOVING 搬迁中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PowerOnTime(self):
        """设备最近一次的开电时间，YYYY-MM-DD 格式。
        :rtype: str
        """
        return self._PowerOnTime

    @PowerOnTime.setter
    def PowerOnTime(self, PowerOnTime):
        self._PowerOnTime = PowerOnTime

    @property
    def OnshelfDate(self):
        """设备最近一次的上架时间，YYYY-MM-DD 格式。
        :rtype: str
        """
        return self._OnshelfDate

    @OnshelfDate.setter
    def OnshelfDate(self, OnshelfDate):
        self._OnshelfDate = OnshelfDate

    @property
    def DeviceType(self):
        """设备类型 server 服务器，netDevice 网络设备
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Manufacturer(self):
        """厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def TypeName(self):
        """其他设备-设备子类型
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def HardwareMemo(self):
        """硬件备注
        :rtype: str
        """
        return self._HardwareMemo

    @HardwareMemo.setter
    def HardwareMemo(self, HardwareMemo):
        self._HardwareMemo = HardwareMemo


    def _deserialize(self, params):
        self._Sn = params.get("Sn")
        self._ModelVersion = params.get("ModelVersion")
        self._AssetId = params.get("AssetId")
        self._SvrIsSpecial = params.get("SvrIsSpecial")
        self._Ip = params.get("Ip")
        self._IdcName = params.get("IdcName")
        self._IdcId = params.get("IdcId")
        self._IdcUnitId = params.get("IdcUnitId")
        self._IdcUnitName = params.get("IdcUnitName")
        self._RackId = params.get("RackId")
        self._ServerTypeId = params.get("ServerTypeId")
        self._RackName = params.get("RackName")
        self._PositionCode = params.get("PositionCode")
        self._Status = params.get("Status")
        self._PowerOnTime = params.get("PowerOnTime")
        self._OnshelfDate = params.get("OnshelfDate")
        self._DeviceType = params.get("DeviceType")
        self._Manufacturer = params.get("Manufacturer")
        self._TypeName = params.get("TypeName")
        self._HardwareMemo = params.get("HardwareMemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceHistory(AbstractModel):
    """工单的设备信息

    """

    def __init__(self):
        r"""
        :param _Sn: 设备sn
        :type Sn: str
        :param _DeviceType: 设备类型
        :type DeviceType: str
        :param _RackName: 机架名
        :type RackName: str
        :param _PositionCode: 机位号
        :type PositionCode: int
        :param _IdcId: 机房id
        :type IdcId: int
        :param _IdcName: 机房名称
        :type IdcName: str
        :param _IdcUnitId: 机房管理单元id
        :type IdcUnitId: int
        :param _IdcUnitName: 机房管理单元名称
        :type IdcUnitName: str
        :param _AssetId: 固资号
        :type AssetId: str
        :param _ModelVersion: 设备型号-版本，只有收货单详情返回
        :type ModelVersion: str
        :param _DeviceHeight: 设备高度，只有收货单详情返回
        :type DeviceHeight: str
        :param _Need10GbSlot: 需要万兆机位，只有收货单详情返回
        :type Need10GbSlot: str
        :param _NeedDCPower: 需要直流电，只有收货单详情返回
        :type NeedDCPower: str
        :param _NeedExtranet: 需要外网，只有收货单详情返回
        :type NeedExtranet: str
        :param _NeedVirtualization: 需要虚拟化，只有收货单详情返回
        :type NeedVirtualization: str
        :param _Manufacturer: 厂商,只有收货单详情返回
        :type Manufacturer: str
        :param _HardwareMemo: 硬件备注
        :type HardwareMemo: str
        :param _DstRackName: 目标机架
        :type DstRackName: str
        :param _DstPositionCode: 目标机位
        :type DstPositionCode: str
        :param _DstIp: 目标ip
        :type DstIp: str
        :param _TypeName: 设备子类型, 其他设备/线材用
        :type TypeName: str
        :param _Quantity: 线材-数量，只有收货单详情返回
        :type Quantity: int
        :param _Unit: 计量单位，，只有收货单详情返回，'箱', '卷', '套'
        :type Unit: str
        :param _ReceiptNumber: 线材-收货凭证号，只有收货单详情返回
        :type ReceiptNumber: str
        """
        self._Sn = None
        self._DeviceType = None
        self._RackName = None
        self._PositionCode = None
        self._IdcId = None
        self._IdcName = None
        self._IdcUnitId = None
        self._IdcUnitName = None
        self._AssetId = None
        self._ModelVersion = None
        self._DeviceHeight = None
        self._Need10GbSlot = None
        self._NeedDCPower = None
        self._NeedExtranet = None
        self._NeedVirtualization = None
        self._Manufacturer = None
        self._HardwareMemo = None
        self._DstRackName = None
        self._DstPositionCode = None
        self._DstIp = None
        self._TypeName = None
        self._Quantity = None
        self._Unit = None
        self._ReceiptNumber = None

    @property
    def Sn(self):
        """设备sn
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def DeviceType(self):
        """设备类型
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def RackName(self):
        """机架名
        :rtype: str
        """
        return self._RackName

    @RackName.setter
    def RackName(self, RackName):
        self._RackName = RackName

    @property
    def PositionCode(self):
        """机位号
        :rtype: int
        """
        return self._PositionCode

    @PositionCode.setter
    def PositionCode(self, PositionCode):
        self._PositionCode = PositionCode

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def IdcName(self):
        """机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def IdcUnitId(self):
        """机房管理单元id
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId

    @property
    def IdcUnitName(self):
        """机房管理单元名称
        :rtype: str
        """
        return self._IdcUnitName

    @IdcUnitName.setter
    def IdcUnitName(self, IdcUnitName):
        self._IdcUnitName = IdcUnitName

    @property
    def AssetId(self):
        """固资号
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def ModelVersion(self):
        """设备型号-版本，只有收货单详情返回
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def DeviceHeight(self):
        """设备高度，只有收货单详情返回
        :rtype: str
        """
        return self._DeviceHeight

    @DeviceHeight.setter
    def DeviceHeight(self, DeviceHeight):
        self._DeviceHeight = DeviceHeight

    @property
    def Need10GbSlot(self):
        """需要万兆机位，只有收货单详情返回
        :rtype: str
        """
        return self._Need10GbSlot

    @Need10GbSlot.setter
    def Need10GbSlot(self, Need10GbSlot):
        self._Need10GbSlot = Need10GbSlot

    @property
    def NeedDCPower(self):
        """需要直流电，只有收货单详情返回
        :rtype: str
        """
        return self._NeedDCPower

    @NeedDCPower.setter
    def NeedDCPower(self, NeedDCPower):
        self._NeedDCPower = NeedDCPower

    @property
    def NeedExtranet(self):
        """需要外网，只有收货单详情返回
        :rtype: str
        """
        return self._NeedExtranet

    @NeedExtranet.setter
    def NeedExtranet(self, NeedExtranet):
        self._NeedExtranet = NeedExtranet

    @property
    def NeedVirtualization(self):
        """需要虚拟化，只有收货单详情返回
        :rtype: str
        """
        return self._NeedVirtualization

    @NeedVirtualization.setter
    def NeedVirtualization(self, NeedVirtualization):
        self._NeedVirtualization = NeedVirtualization

    @property
    def Manufacturer(self):
        """厂商,只有收货单详情返回
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def HardwareMemo(self):
        """硬件备注
        :rtype: str
        """
        return self._HardwareMemo

    @HardwareMemo.setter
    def HardwareMemo(self, HardwareMemo):
        self._HardwareMemo = HardwareMemo

    @property
    def DstRackName(self):
        """目标机架
        :rtype: str
        """
        return self._DstRackName

    @DstRackName.setter
    def DstRackName(self, DstRackName):
        self._DstRackName = DstRackName

    @property
    def DstPositionCode(self):
        """目标机位
        :rtype: str
        """
        return self._DstPositionCode

    @DstPositionCode.setter
    def DstPositionCode(self, DstPositionCode):
        self._DstPositionCode = DstPositionCode

    @property
    def DstIp(self):
        """目标ip
        :rtype: str
        """
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp

    @property
    def TypeName(self):
        """设备子类型, 其他设备/线材用
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def Quantity(self):
        """线材-数量，只有收货单详情返回
        :rtype: int
        """
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Unit(self):
        """计量单位，，只有收货单详情返回，'箱', '卷', '套'
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def ReceiptNumber(self):
        """线材-收货凭证号，只有收货单详情返回
        :rtype: str
        """
        return self._ReceiptNumber

    @ReceiptNumber.setter
    def ReceiptNumber(self, ReceiptNumber):
        self._ReceiptNumber = ReceiptNumber


    def _deserialize(self, params):
        self._Sn = params.get("Sn")
        self._DeviceType = params.get("DeviceType")
        self._RackName = params.get("RackName")
        self._PositionCode = params.get("PositionCode")
        self._IdcId = params.get("IdcId")
        self._IdcName = params.get("IdcName")
        self._IdcUnitId = params.get("IdcUnitId")
        self._IdcUnitName = params.get("IdcUnitName")
        self._AssetId = params.get("AssetId")
        self._ModelVersion = params.get("ModelVersion")
        self._DeviceHeight = params.get("DeviceHeight")
        self._Need10GbSlot = params.get("Need10GbSlot")
        self._NeedDCPower = params.get("NeedDCPower")
        self._NeedExtranet = params.get("NeedExtranet")
        self._NeedVirtualization = params.get("NeedVirtualization")
        self._Manufacturer = params.get("Manufacturer")
        self._HardwareMemo = params.get("HardwareMemo")
        self._DstRackName = params.get("DstRackName")
        self._DstPositionCode = params.get("DstPositionCode")
        self._DstIp = params.get("DstIp")
        self._TypeName = params.get("TypeName")
        self._Quantity = params.get("Quantity")
        self._Unit = params.get("Unit")
        self._ReceiptNumber = params.get("ReceiptNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceOrderBaseInfo(AbstractModel):
    """设备类工单的基础历史入参信息

    """

    def __init__(self):
        r"""
        :param _IdcId: 机房id
        :type IdcId: int
        :param _IdcName: 机房名称
        :type IdcName: str
        :param _DeviceType: 设备类型
        :type DeviceType: str
        :param _Remark: 备注
        :type Remark: str
        :param _ReceivingOperation: 1.收货-仅核对外包装完整和数量，不开箱 2.验收-开箱核对型号SN一致
        :type ReceivingOperation: str
        :param _EntryTime: 设备收货-进入时间
        :type EntryTime: str
        :param _IsExpressDelivery: 设备收货-是否快递寄件
        :type IsExpressDelivery: bool
        :param _ExpressInfo: 设备收货-快递寄件信息
        :type ExpressInfo: :class:`tencentcloud.chc.v20230418.models.ExpressDelivery`
        :param _StuffOption: 上/下架人员 1.自行解决 2.由腾讯IDC负责
        :type StuffOption: str
        :param _SelfOperationInfo: 上/下架自行解决信息
        :type SelfOperationInfo: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        :param _WithPowerOn: 上架后开电
        :type WithPowerOn: bool
        :param _IsPowerOffConfirm: 关电确认 1.授权时关电 2.关电前需要确认
        :type IsPowerOffConfirm: str
        :param _PowerOffConfirmInfo: 关电前需要确认信息
        :type PowerOffConfirmInfo: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        :param _HandoverMethod: 退出交接方式 1.物流上门收货 2.客户上门自提
        :type HandoverMethod: str
        :param _CustomerReceipt: 客户上门自提信息
        :type CustomerReceipt: :class:`tencentcloud.chc.v20230418.models.CustomerReceipt`
        :param _LogisticsReceipt: 物流上门收货信息
        :type LogisticsReceipt: :class:`tencentcloud.chc.v20230418.models.LogisticsReceipt`
        """
        self._IdcId = None
        self._IdcName = None
        self._DeviceType = None
        self._Remark = None
        self._ReceivingOperation = None
        self._EntryTime = None
        self._IsExpressDelivery = None
        self._ExpressInfo = None
        self._StuffOption = None
        self._SelfOperationInfo = None
        self._WithPowerOn = None
        self._IsPowerOffConfirm = None
        self._PowerOffConfirmInfo = None
        self._HandoverMethod = None
        self._CustomerReceipt = None
        self._LogisticsReceipt = None

    @property
    def IdcId(self):
        """机房id
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def IdcName(self):
        """机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def DeviceType(self):
        """设备类型
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReceivingOperation(self):
        """1.收货-仅核对外包装完整和数量，不开箱 2.验收-开箱核对型号SN一致
        :rtype: str
        """
        return self._ReceivingOperation

    @ReceivingOperation.setter
    def ReceivingOperation(self, ReceivingOperation):
        self._ReceivingOperation = ReceivingOperation

    @property
    def EntryTime(self):
        """设备收货-进入时间
        :rtype: str
        """
        return self._EntryTime

    @EntryTime.setter
    def EntryTime(self, EntryTime):
        self._EntryTime = EntryTime

    @property
    def IsExpressDelivery(self):
        """设备收货-是否快递寄件
        :rtype: bool
        """
        return self._IsExpressDelivery

    @IsExpressDelivery.setter
    def IsExpressDelivery(self, IsExpressDelivery):
        self._IsExpressDelivery = IsExpressDelivery

    @property
    def ExpressInfo(self):
        """设备收货-快递寄件信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.ExpressDelivery`
        """
        return self._ExpressInfo

    @ExpressInfo.setter
    def ExpressInfo(self, ExpressInfo):
        self._ExpressInfo = ExpressInfo

    @property
    def StuffOption(self):
        """上/下架人员 1.自行解决 2.由腾讯IDC负责
        :rtype: str
        """
        return self._StuffOption

    @StuffOption.setter
    def StuffOption(self, StuffOption):
        self._StuffOption = StuffOption

    @property
    def SelfOperationInfo(self):
        """上/下架自行解决信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.SelfOperation`
        """
        return self._SelfOperationInfo

    @SelfOperationInfo.setter
    def SelfOperationInfo(self, SelfOperationInfo):
        self._SelfOperationInfo = SelfOperationInfo

    @property
    def WithPowerOn(self):
        """上架后开电
        :rtype: bool
        """
        return self._WithPowerOn

    @WithPowerOn.setter
    def WithPowerOn(self, WithPowerOn):
        self._WithPowerOn = WithPowerOn

    @property
    def IsPowerOffConfirm(self):
        """关电确认 1.授权时关电 2.关电前需要确认
        :rtype: str
        """
        return self._IsPowerOffConfirm

    @IsPowerOffConfirm.setter
    def IsPowerOffConfirm(self, IsPowerOffConfirm):
        self._IsPowerOffConfirm = IsPowerOffConfirm

    @property
    def PowerOffConfirmInfo(self):
        """关电前需要确认信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.PowerOffConfirm`
        """
        return self._PowerOffConfirmInfo

    @PowerOffConfirmInfo.setter
    def PowerOffConfirmInfo(self, PowerOffConfirmInfo):
        self._PowerOffConfirmInfo = PowerOffConfirmInfo

    @property
    def HandoverMethod(self):
        """退出交接方式 1.物流上门收货 2.客户上门自提
        :rtype: str
        """
        return self._HandoverMethod

    @HandoverMethod.setter
    def HandoverMethod(self, HandoverMethod):
        self._HandoverMethod = HandoverMethod

    @property
    def CustomerReceipt(self):
        """客户上门自提信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.CustomerReceipt`
        """
        return self._CustomerReceipt

    @CustomerReceipt.setter
    def CustomerReceipt(self, CustomerReceipt):
        self._CustomerReceipt = CustomerReceipt

    @property
    def LogisticsReceipt(self):
        """物流上门收货信息
        :rtype: :class:`tencentcloud.chc.v20230418.models.LogisticsReceipt`
        """
        return self._LogisticsReceipt

    @LogisticsReceipt.setter
    def LogisticsReceipt(self, LogisticsReceipt):
        self._LogisticsReceipt = LogisticsReceipt


    def _deserialize(self, params):
        self._IdcId = params.get("IdcId")
        self._IdcName = params.get("IdcName")
        self._DeviceType = params.get("DeviceType")
        self._Remark = params.get("Remark")
        self._ReceivingOperation = params.get("ReceivingOperation")
        self._EntryTime = params.get("EntryTime")
        self._IsExpressDelivery = params.get("IsExpressDelivery")
        if params.get("ExpressInfo") is not None:
            self._ExpressInfo = ExpressDelivery()
            self._ExpressInfo._deserialize(params.get("ExpressInfo"))
        self._StuffOption = params.get("StuffOption")
        if params.get("SelfOperationInfo") is not None:
            self._SelfOperationInfo = SelfOperation()
            self._SelfOperationInfo._deserialize(params.get("SelfOperationInfo"))
        self._WithPowerOn = params.get("WithPowerOn")
        self._IsPowerOffConfirm = params.get("IsPowerOffConfirm")
        if params.get("PowerOffConfirmInfo") is not None:
            self._PowerOffConfirmInfo = PowerOffConfirm()
            self._PowerOffConfirmInfo._deserialize(params.get("PowerOffConfirmInfo"))
        self._HandoverMethod = params.get("HandoverMethod")
        if params.get("CustomerReceipt") is not None:
            self._CustomerReceipt = CustomerReceipt()
            self._CustomerReceipt._deserialize(params.get("CustomerReceipt"))
        if params.get("LogisticsReceipt") is not None:
            self._LogisticsReceipt = LogisticsReceipt()
            self._LogisticsReceipt._deserialize(params.get("LogisticsReceipt"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicePosition(AbstractModel):
    """设备及位置信息

    """

    def __init__(self):
        r"""
        :param _Sn: 设备SN
        :type Sn: str
        :param _RackName: 机架名称
        :type RackName: str
        :param _IdcUnitId: 机房管理单元ID
        :type IdcUnitId: int
        :param _IdcName: 机房名称
        :type IdcName: str
        :param _IdcUnitName: 机房管理单元名称
        :type IdcUnitName: str
        :param _AssetId: 设备固资。只有服务器设备才需要这个值
        :type AssetId: str
        :param _PositionCode: 机位编号，只有服务器设备才需要传这个值
        :type PositionCode: int
        :param _DeviceType: server 代表服务器，netDevice 代表网络设备
        :type DeviceType: str
        """
        self._Sn = None
        self._RackName = None
        self._IdcUnitId = None
        self._IdcName = None
        self._IdcUnitName = None
        self._AssetId = None
        self._PositionCode = None
        self._DeviceType = None

    @property
    def Sn(self):
        """设备SN
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def RackName(self):
        """机架名称
        :rtype: str
        """
        return self._RackName

    @RackName.setter
    def RackName(self, RackName):
        self._RackName = RackName

    @property
    def IdcUnitId(self):
        """机房管理单元ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId

    @property
    def IdcName(self):
        """机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def IdcUnitName(self):
        """机房管理单元名称
        :rtype: str
        """
        return self._IdcUnitName

    @IdcUnitName.setter
    def IdcUnitName(self, IdcUnitName):
        self._IdcUnitName = IdcUnitName

    @property
    def AssetId(self):
        """设备固资。只有服务器设备才需要这个值
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def PositionCode(self):
        """机位编号，只有服务器设备才需要传这个值
        :rtype: int
        """
        return self._PositionCode

    @PositionCode.setter
    def PositionCode(self, PositionCode):
        self._PositionCode = PositionCode

    @property
    def DeviceType(self):
        """server 代表服务器，netDevice 代表网络设备
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._Sn = params.get("Sn")
        self._RackName = params.get("RackName")
        self._IdcUnitId = params.get("IdcUnitId")
        self._IdcName = params.get("IdcName")
        self._IdcUnitName = params.get("IdcUnitName")
        self._AssetId = params.get("AssetId")
        self._PositionCode = params.get("PositionCode")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceRackOn(AbstractModel):
    """设备上架信息

    """

    def __init__(self):
        r"""
        :param _DeviceSn: 设备sn
        :type DeviceSn: str
        :param _DstRackName: 目标机架
        :type DstRackName: str
        :param _DstPositionCode: 目标机位,服务器必传,网络设备不用传
        :type DstPositionCode: str
        :param _DstIp: 设备ip
        :type DstIp: str
        """
        self._DeviceSn = None
        self._DstRackName = None
        self._DstPositionCode = None
        self._DstIp = None

    @property
    def DeviceSn(self):
        """设备sn
        :rtype: str
        """
        return self._DeviceSn

    @DeviceSn.setter
    def DeviceSn(self, DeviceSn):
        self._DeviceSn = DeviceSn

    @property
    def DstRackName(self):
        """目标机架
        :rtype: str
        """
        return self._DstRackName

    @DstRackName.setter
    def DstRackName(self, DstRackName):
        self._DstRackName = DstRackName

    @property
    def DstPositionCode(self):
        """目标机位,服务器必传,网络设备不用传
        :rtype: str
        """
        return self._DstPositionCode

    @DstPositionCode.setter
    def DstPositionCode(self, DstPositionCode):
        self._DstPositionCode = DstPositionCode

    @property
    def DstIp(self):
        """设备ip
        :rtype: str
        """
        return self._DstIp

    @DstIp.setter
    def DstIp(self, DstIp):
        self._DstIp = DstIp


    def _deserialize(self, params):
        self._DeviceSn = params.get("DeviceSn")
        self._DstRackName = params.get("DstRackName")
        self._DstPositionCode = params.get("DstPositionCode")
        self._DstIp = params.get("DstIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Distribution(AbstractModel):
    """机架用量分布

    """

    def __init__(self):
        r"""
        :param _RackNumber: 机架编号
        :type RackNumber: str
        :param _RackUsageSet: 机架的用量分布
        :type RackUsageSet: list of RackUsage
        """
        self._RackNumber = None
        self._RackUsageSet = None

    @property
    def RackNumber(self):
        """机架编号
        :rtype: str
        """
        return self._RackNumber

    @RackNumber.setter
    def RackNumber(self, RackNumber):
        self._RackNumber = RackNumber

    @property
    def RackUsageSet(self):
        """机架的用量分布
        :rtype: list of RackUsage
        """
        return self._RackUsageSet

    @RackUsageSet.setter
    def RackUsageSet(self, RackUsageSet):
        self._RackUsageSet = RackUsageSet


    def _deserialize(self, params):
        self._RackNumber = params.get("RackNumber")
        if params.get("RackUsageSet") is not None:
            self._RackUsageSet = []
            for item in params.get("RackUsageSet"):
                obj = RackUsage()
                obj._deserialize(item)
                self._RackUsageSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpressDelivery(AbstractModel):
    """快递寄件信息,快递寄件必填

    """

    def __init__(self):
        r"""
        :param _LogisticsCompany: 物流公司
        :type LogisticsCompany: str
        :param _ExpressNumber: 快递单号
        :type ExpressNumber: str
        """
        self._LogisticsCompany = None
        self._ExpressNumber = None

    @property
    def LogisticsCompany(self):
        """物流公司
        :rtype: str
        """
        return self._LogisticsCompany

    @LogisticsCompany.setter
    def LogisticsCompany(self, LogisticsCompany):
        self._LogisticsCompany = LogisticsCompany

    @property
    def ExpressNumber(self):
        """快递单号
        :rtype: str
        """
        return self._ExpressNumber

    @ExpressNumber.setter
    def ExpressNumber(self, ExpressNumber):
        self._ExpressNumber = ExpressNumber


    def _deserialize(self, params):
        self._LogisticsCompany = params.get("LogisticsCompany")
        self._ExpressNumber = params.get("ExpressNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

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
        


class Idc(AbstractModel):
    """机房信息

    """

    def __init__(self):
        r"""
        :param _IdcName: 机房名称
        :type IdcName: str
        :param _IdcId: 机房ID
        :type IdcId: int
        :param _IdcUnitSet: 机房管理单元详情列表
        :type IdcUnitSet: list of IdcUnit
        """
        self._IdcName = None
        self._IdcId = None
        self._IdcUnitSet = None

    @property
    def IdcName(self):
        """机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def IdcId(self):
        """机房ID
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def IdcUnitSet(self):
        """机房管理单元详情列表
        :rtype: list of IdcUnit
        """
        return self._IdcUnitSet

    @IdcUnitSet.setter
    def IdcUnitSet(self, IdcUnitSet):
        self._IdcUnitSet = IdcUnitSet


    def _deserialize(self, params):
        self._IdcName = params.get("IdcName")
        self._IdcId = params.get("IdcId")
        if params.get("IdcUnitSet") is not None:
            self._IdcUnitSet = []
            for item in params.get("IdcUnitSet"):
                obj = IdcUnit()
                obj._deserialize(item)
                self._IdcUnitSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdcUnit(AbstractModel):
    """机房管理单元

    """

    def __init__(self):
        r"""
        :param _IdcUnitId: 机房管理单元 ID
        :type IdcUnitId: int
        :param _IdcUnitName: 机房管理单元名称
        :type IdcUnitName: str
        :param _CageSet: 围笼列表
        :type CageSet: list of Cage
        """
        self._IdcUnitId = None
        self._IdcUnitName = None
        self._CageSet = None

    @property
    def IdcUnitId(self):
        """机房管理单元 ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId

    @property
    def IdcUnitName(self):
        """机房管理单元名称
        :rtype: str
        """
        return self._IdcUnitName

    @IdcUnitName.setter
    def IdcUnitName(self, IdcUnitName):
        self._IdcUnitName = IdcUnitName

    @property
    def CageSet(self):
        """围笼列表
        :rtype: list of Cage
        """
        return self._CageSet

    @CageSet.setter
    def CageSet(self, CageSet):
        self._CageSet = CageSet


    def _deserialize(self, params):
        self._IdcUnitId = params.get("IdcUnitId")
        self._IdcUnitName = params.get("IdcUnitName")
        if params.get("CageSet") is not None:
            self._CageSet = []
            for item in params.get("CageSet"):
                obj = Cage()
                obj._deserialize(item)
                self._CageSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdcUnitInfo(AbstractModel):
    """机房管理单元

    """

    def __init__(self):
        r"""
        :param _Address: 机房管理单元地址
        :type Address: str
        :param _Operator: 机房经理
        :type Operator: str
        :param _TelNumber: 联系电话
        :type TelNumber: str
        :param _AssetManager: 资产管理员
        :type AssetManager: str
        :param _AssetManagerTelNumber: 资产管理员电话
        :type AssetManagerTelNumber: str
        """
        self._Address = None
        self._Operator = None
        self._TelNumber = None
        self._AssetManager = None
        self._AssetManagerTelNumber = None

    @property
    def Address(self):
        """机房管理单元地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Operator(self):
        """机房经理
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def TelNumber(self):
        """联系电话
        :rtype: str
        """
        return self._TelNumber

    @TelNumber.setter
    def TelNumber(self, TelNumber):
        self._TelNumber = TelNumber

    @property
    def AssetManager(self):
        """资产管理员
        :rtype: str
        """
        return self._AssetManager

    @AssetManager.setter
    def AssetManager(self, AssetManager):
        self._AssetManager = AssetManager

    @property
    def AssetManagerTelNumber(self):
        """资产管理员电话
        :rtype: str
        """
        return self._AssetManagerTelNumber

    @AssetManagerTelNumber.setter
    def AssetManagerTelNumber(self, AssetManagerTelNumber):
        self._AssetManagerTelNumber = AssetManagerTelNumber


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Operator = params.get("Operator")
        self._TelNumber = params.get("TelNumber")
        self._AssetManager = params.get("AssetManager")
        self._AssetManagerTelNumber = params.get("AssetManagerTelNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogisticsReceipt(AbstractModel):
    """物流上门收货信息

    """

    def __init__(self):
        r"""
        :param _LogisticsArrivalTime: 物流预计上门时间
        :type LogisticsArrivalTime: str
        :param _LogisticsCompany: 物流公司名称
        :type LogisticsCompany: str
        :param _LogisticsStuff: 物流联系人
        :type LogisticsStuff: str
        :param _LogisticsStuffContact: 物流电话
        :type LogisticsStuffContact: str
        :param _ReceiverContact: 收货人电话
        :type ReceiverContact: str
        :param _ReceiverName: 收货人姓名
        :type ReceiverName: str
        :param _ShippingAddress: 收货地址
        :type ShippingAddress: str
        """
        self._LogisticsArrivalTime = None
        self._LogisticsCompany = None
        self._LogisticsStuff = None
        self._LogisticsStuffContact = None
        self._ReceiverContact = None
        self._ReceiverName = None
        self._ShippingAddress = None

    @property
    def LogisticsArrivalTime(self):
        """物流预计上门时间
        :rtype: str
        """
        return self._LogisticsArrivalTime

    @LogisticsArrivalTime.setter
    def LogisticsArrivalTime(self, LogisticsArrivalTime):
        self._LogisticsArrivalTime = LogisticsArrivalTime

    @property
    def LogisticsCompany(self):
        """物流公司名称
        :rtype: str
        """
        return self._LogisticsCompany

    @LogisticsCompany.setter
    def LogisticsCompany(self, LogisticsCompany):
        self._LogisticsCompany = LogisticsCompany

    @property
    def LogisticsStuff(self):
        """物流联系人
        :rtype: str
        """
        return self._LogisticsStuff

    @LogisticsStuff.setter
    def LogisticsStuff(self, LogisticsStuff):
        self._LogisticsStuff = LogisticsStuff

    @property
    def LogisticsStuffContact(self):
        """物流电话
        :rtype: str
        """
        return self._LogisticsStuffContact

    @LogisticsStuffContact.setter
    def LogisticsStuffContact(self, LogisticsStuffContact):
        self._LogisticsStuffContact = LogisticsStuffContact

    @property
    def ReceiverContact(self):
        """收货人电话
        :rtype: str
        """
        return self._ReceiverContact

    @ReceiverContact.setter
    def ReceiverContact(self, ReceiverContact):
        self._ReceiverContact = ReceiverContact

    @property
    def ReceiverName(self):
        """收货人姓名
        :rtype: str
        """
        return self._ReceiverName

    @ReceiverName.setter
    def ReceiverName(self, ReceiverName):
        self._ReceiverName = ReceiverName

    @property
    def ShippingAddress(self):
        """收货地址
        :rtype: str
        """
        return self._ShippingAddress

    @ShippingAddress.setter
    def ShippingAddress(self, ShippingAddress):
        self._ShippingAddress = ShippingAddress


    def _deserialize(self, params):
        self._LogisticsArrivalTime = params.get("LogisticsArrivalTime")
        self._LogisticsCompany = params.get("LogisticsCompany")
        self._LogisticsStuff = params.get("LogisticsStuff")
        self._LogisticsStuffContact = params.get("LogisticsStuffContact")
        self._ReceiverContact = params.get("ReceiverContact")
        self._ReceiverName = params.get("ReceiverName")
        self._ShippingAddress = params.get("ShippingAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelEvaluationBaseInfo(AbstractModel):
    """设备评估工单基本信息

    """

    def __init__(self):
        r"""
        :param _CustomerName: 客户名称
        :type CustomerName: str
        :param _DeviceType: server 服务器  netDevice 网络设备
        :type DeviceType: str
        :param _CampusName: 园区名称
        :type CampusName: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._CustomerName = None
        self._DeviceType = None
        self._CampusName = None
        self._Remark = None

    @property
    def CustomerName(self):
        """客户名称
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def DeviceType(self):
        """server 服务器  netDevice 网络设备
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def CampusName(self):
        """园区名称
        :rtype: str
        """
        return self._CampusName

    @CampusName.setter
    def CampusName(self, CampusName):
        self._CampusName = CampusName

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._CustomerName = params.get("CustomerName")
        self._DeviceType = params.get("DeviceType")
        self._CampusName = params.get("CampusName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelVersion(AbstractModel):
    """型号以及版本号

    """

    def __init__(self):
        r"""
        :param _DevModel: 型号名称
        :type DevModel: str
        :param _Version: 版本
        :type Version: str
        """
        self._DevModel = None
        self._Version = None

    @property
    def DevModel(self):
        """型号名称
        :rtype: str
        """
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def Version(self):
        """版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._DevModel = params.get("DevModel")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelVersionCount(AbstractModel):
    """型号和对应的版本数量

    """

    def __init__(self):
        r"""
        :param _DevModel: 型号名称
        :type DevModel: str
        :param _VersionCount: 版本数量
        :type VersionCount: int
        """
        self._DevModel = None
        self._VersionCount = None

    @property
    def DevModel(self):
        """型号名称
        :rtype: str
        """
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def VersionCount(self):
        """版本数量
        :rtype: int
        """
        return self._VersionCount

    @VersionCount.setter
    def VersionCount(self, VersionCount):
        self._VersionCount = VersionCount


    def _deserialize(self, params):
        self._DevModel = params.get("DevModel")
        self._VersionCount = params.get("VersionCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelVersionDetail(AbstractModel):
    """带有园区评估记录的型号详情

    """

    def __init__(self):
        r"""
        :param _Version: 版本号
        :type Version: str
        :param _CheckResult: 0 代表在当前园区没评估过，1 代表完全满足IDC准入标准 2 代表存在托管风险 3 代表不满足IDC准入标准
        :type CheckResult: int
        :param _OptionSet: 型号各个配置项的详情
        :type OptionSet: list of TemplateOption
        :param _ModelVersion: 设备型号名称及版本
        :type ModelVersion: str
        """
        self._Version = None
        self._CheckResult = None
        self._OptionSet = None
        self._ModelVersion = None

    @property
    def Version(self):
        """版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CheckResult(self):
        """0 代表在当前园区没评估过，1 代表完全满足IDC准入标准 2 代表存在托管风险 3 代表不满足IDC准入标准
        :rtype: int
        """
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def OptionSet(self):
        """型号各个配置项的详情
        :rtype: list of TemplateOption
        """
        return self._OptionSet

    @OptionSet.setter
    def OptionSet(self, OptionSet):
        self._OptionSet = OptionSet

    @property
    def ModelVersion(self):
        """设备型号名称及版本
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._CheckResult = params.get("CheckResult")
        if params.get("OptionSet") is not None:
            self._OptionSet = []
            for item in params.get("OptionSet"):
                obj = TemplateOption()
                obj._deserialize(item)
                self._OptionSet.append(obj)
        self._ModelVersion = params.get("ModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkOrderTypeCollectFlagRequest(AbstractModel):
    """ModifyWorkOrderTypeCollectFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkOrderType: 工单类型的唯一英文标识
        :type WorkOrderType: str
        """
        self._WorkOrderType = None

    @property
    def WorkOrderType(self):
        """工单类型的唯一英文标识
        :rtype: str
        """
        return self._WorkOrderType

    @WorkOrderType.setter
    def WorkOrderType(self, WorkOrderType):
        self._WorkOrderType = WorkOrderType


    def _deserialize(self, params):
        self._WorkOrderType = params.get("WorkOrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkOrderTypeCollectFlagResponse(AbstractModel):
    """ModifyWorkOrderTypeCollectFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CurrentCollectFlag: 工单类型当前的收藏状态
        :type CurrentCollectFlag: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CurrentCollectFlag = None
        self._RequestId = None

    @property
    def CurrentCollectFlag(self):
        """工单类型当前的收藏状态
        :rtype: bool
        """
        return self._CurrentCollectFlag

    @CurrentCollectFlag.setter
    def CurrentCollectFlag(self, CurrentCollectFlag):
        self._CurrentCollectFlag = CurrentCollectFlag

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
        self._CurrentCollectFlag = params.get("CurrentCollectFlag")
        self._RequestId = params.get("RequestId")


class NetDeviceModel(AbstractModel):
    """网络设备型号详情

    """

    def __init__(self):
        r"""
        :param _Version: 版本号
        :type Version: str
        :param _ModelVersion: 型号和版本的组合名称
        :type ModelVersion: str
        :param _DevModel: 型号名
        :type DevModel: str
        :param _DevWidth: 宽度
        :type DevWidth: str
        :param _DevDepth: 深度
        :type DevDepth: str
        :param _DevWeight: 重量
        :type DevWeight: str
        :param _MountEar: 是否携带挂耳
        :type MountEar: str
        :param _AccordCCC: 是否符合CCC认证
        :type AccordCCC: str
        :param _PassNetwork: 是否通过入网许可认证
        :type PassNetwork: str
        :param _PowerportType: 电源接口型号
        :type PowerportType: str
        :param _PowerModule: 电源模块
        :type PowerModule: str
        :param _PowermoduleNum: 电源模块数量
        :type PowermoduleNum: str
        :param _PowermodulePosition: 电源模块位置
        :type PowermodulePosition: str
        :param _HighVoltageAdapt: 高压直流自适应
        :type HighVoltageAdapt: str
        :param _PowerEnergy: 实际工作功耗(W)
        :type PowerEnergy: str
        :param _InwindPosition: 进风口位置
        :type InwindPosition: str
        :param _OutwindPosition: 出风口位置
        :type OutwindPosition: str
        :param _BusinessPortPosition: 业务端口位置
        :type BusinessPortPosition: str
        :param _LineManager: 带有理线器
        :type LineManager: str
        :param _CheckResult: 0 代表在当前园区没评估过，1 代表完全满足IDC准入标准  2 代表存在托管风险  3 代表不满足IDC准入标准
        :type CheckResult: int
        :param _DevHeight: 设备高度
        :type DevHeight: str
        """
        self._Version = None
        self._ModelVersion = None
        self._DevModel = None
        self._DevWidth = None
        self._DevDepth = None
        self._DevWeight = None
        self._MountEar = None
        self._AccordCCC = None
        self._PassNetwork = None
        self._PowerportType = None
        self._PowerModule = None
        self._PowermoduleNum = None
        self._PowermodulePosition = None
        self._HighVoltageAdapt = None
        self._PowerEnergy = None
        self._InwindPosition = None
        self._OutwindPosition = None
        self._BusinessPortPosition = None
        self._LineManager = None
        self._CheckResult = None
        self._DevHeight = None

    @property
    def Version(self):
        """版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ModelVersion(self):
        """型号和版本的组合名称
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def DevModel(self):
        """型号名
        :rtype: str
        """
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def DevWidth(self):
        """宽度
        :rtype: str
        """
        return self._DevWidth

    @DevWidth.setter
    def DevWidth(self, DevWidth):
        self._DevWidth = DevWidth

    @property
    def DevDepth(self):
        """深度
        :rtype: str
        """
        return self._DevDepth

    @DevDepth.setter
    def DevDepth(self, DevDepth):
        self._DevDepth = DevDepth

    @property
    def DevWeight(self):
        """重量
        :rtype: str
        """
        return self._DevWeight

    @DevWeight.setter
    def DevWeight(self, DevWeight):
        self._DevWeight = DevWeight

    @property
    def MountEar(self):
        """是否携带挂耳
        :rtype: str
        """
        return self._MountEar

    @MountEar.setter
    def MountEar(self, MountEar):
        self._MountEar = MountEar

    @property
    def AccordCCC(self):
        """是否符合CCC认证
        :rtype: str
        """
        return self._AccordCCC

    @AccordCCC.setter
    def AccordCCC(self, AccordCCC):
        self._AccordCCC = AccordCCC

    @property
    def PassNetwork(self):
        """是否通过入网许可认证
        :rtype: str
        """
        return self._PassNetwork

    @PassNetwork.setter
    def PassNetwork(self, PassNetwork):
        self._PassNetwork = PassNetwork

    @property
    def PowerportType(self):
        """电源接口型号
        :rtype: str
        """
        return self._PowerportType

    @PowerportType.setter
    def PowerportType(self, PowerportType):
        self._PowerportType = PowerportType

    @property
    def PowerModule(self):
        """电源模块
        :rtype: str
        """
        return self._PowerModule

    @PowerModule.setter
    def PowerModule(self, PowerModule):
        self._PowerModule = PowerModule

    @property
    def PowermoduleNum(self):
        """电源模块数量
        :rtype: str
        """
        return self._PowermoduleNum

    @PowermoduleNum.setter
    def PowermoduleNum(self, PowermoduleNum):
        self._PowermoduleNum = PowermoduleNum

    @property
    def PowermodulePosition(self):
        """电源模块位置
        :rtype: str
        """
        return self._PowermodulePosition

    @PowermodulePosition.setter
    def PowermodulePosition(self, PowermodulePosition):
        self._PowermodulePosition = PowermodulePosition

    @property
    def HighVoltageAdapt(self):
        """高压直流自适应
        :rtype: str
        """
        return self._HighVoltageAdapt

    @HighVoltageAdapt.setter
    def HighVoltageAdapt(self, HighVoltageAdapt):
        self._HighVoltageAdapt = HighVoltageAdapt

    @property
    def PowerEnergy(self):
        """实际工作功耗(W)
        :rtype: str
        """
        return self._PowerEnergy

    @PowerEnergy.setter
    def PowerEnergy(self, PowerEnergy):
        self._PowerEnergy = PowerEnergy

    @property
    def InwindPosition(self):
        """进风口位置
        :rtype: str
        """
        return self._InwindPosition

    @InwindPosition.setter
    def InwindPosition(self, InwindPosition):
        self._InwindPosition = InwindPosition

    @property
    def OutwindPosition(self):
        """出风口位置
        :rtype: str
        """
        return self._OutwindPosition

    @OutwindPosition.setter
    def OutwindPosition(self, OutwindPosition):
        self._OutwindPosition = OutwindPosition

    @property
    def BusinessPortPosition(self):
        """业务端口位置
        :rtype: str
        """
        return self._BusinessPortPosition

    @BusinessPortPosition.setter
    def BusinessPortPosition(self, BusinessPortPosition):
        self._BusinessPortPosition = BusinessPortPosition

    @property
    def LineManager(self):
        """带有理线器
        :rtype: str
        """
        return self._LineManager

    @LineManager.setter
    def LineManager(self, LineManager):
        self._LineManager = LineManager

    @property
    def CheckResult(self):
        """0 代表在当前园区没评估过，1 代表完全满足IDC准入标准  2 代表存在托管风险  3 代表不满足IDC准入标准
        :rtype: int
        """
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def DevHeight(self):
        """设备高度
        :rtype: str
        """
        return self._DevHeight

    @DevHeight.setter
    def DevHeight(self, DevHeight):
        self._DevHeight = DevHeight


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._ModelVersion = params.get("ModelVersion")
        self._DevModel = params.get("DevModel")
        self._DevWidth = params.get("DevWidth")
        self._DevDepth = params.get("DevDepth")
        self._DevWeight = params.get("DevWeight")
        self._MountEar = params.get("MountEar")
        self._AccordCCC = params.get("AccordCCC")
        self._PassNetwork = params.get("PassNetwork")
        self._PowerportType = params.get("PowerportType")
        self._PowerModule = params.get("PowerModule")
        self._PowermoduleNum = params.get("PowermoduleNum")
        self._PowermodulePosition = params.get("PowermodulePosition")
        self._HighVoltageAdapt = params.get("HighVoltageAdapt")
        self._PowerEnergy = params.get("PowerEnergy")
        self._InwindPosition = params.get("InwindPosition")
        self._OutwindPosition = params.get("OutwindPosition")
        self._BusinessPortPosition = params.get("BusinessPortPosition")
        self._LineManager = params.get("LineManager")
        self._CheckResult = params.get("CheckResult")
        self._DevHeight = params.get("DevHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetReceivingInfo(AbstractModel):
    """网络设备收货详情

    """

    def __init__(self):
        r"""
        :param _DeviceSn: 设备sn
        :type DeviceSn: str
        :param _ModelVersion: 设备型号-版本
        :type ModelVersion: str
        :param _HardwareMemo: 硬件备注
        :type HardwareMemo: str
        :param _Manufacturer: 厂商
        :type Manufacturer: str
        """
        self._DeviceSn = None
        self._ModelVersion = None
        self._HardwareMemo = None
        self._Manufacturer = None

    @property
    def DeviceSn(self):
        """设备sn
        :rtype: str
        """
        return self._DeviceSn

    @DeviceSn.setter
    def DeviceSn(self, DeviceSn):
        self._DeviceSn = DeviceSn

    @property
    def ModelVersion(self):
        """设备型号-版本
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def HardwareMemo(self):
        """硬件备注
        :rtype: str
        """
        return self._HardwareMemo

    @HardwareMemo.setter
    def HardwareMemo(self, HardwareMemo):
        self._HardwareMemo = HardwareMemo

    @property
    def Manufacturer(self):
        """厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer


    def _deserialize(self, params):
        self._DeviceSn = params.get("DeviceSn")
        self._ModelVersion = params.get("ModelVersion")
        self._HardwareMemo = params.get("HardwareMemo")
        self._Manufacturer = params.get("Manufacturer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptionValueItem(AbstractModel):
    """型号选项下拉框中的选项值

    """

    def __init__(self):
        r"""
        :param _OptionValue: 选项的值
        :type OptionValue: str
        :param _Selected: 是否默认选中
        :type Selected: bool
        """
        self._OptionValue = None
        self._Selected = None

    @property
    def OptionValue(self):
        """选项的值
        :rtype: str
        """
        return self._OptionValue

    @OptionValue.setter
    def OptionValue(self, OptionValue):
        self._OptionValue = OptionValue

    @property
    def Selected(self):
        """是否默认选中
        :rtype: bool
        """
        return self._Selected

    @Selected.setter
    def Selected(self, Selected):
        self._Selected = Selected


    def _deserialize(self, params):
        self._OptionValue = params.get("OptionValue")
        self._Selected = params.get("Selected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderStep(AbstractModel):
    """工单详情中的工单流程步骤

    """

    def __init__(self):
        r"""
        :param _StepName: 步骤名
        :type StepName: str
        :param _OwnerName: 处理人
        :type OwnerName: str
        :param _FinishTime: 完成时间
        :type FinishTime: str
        :param _StepStatus: 此步骤状态
        :type StepStatus: str
        """
        self._StepName = None
        self._OwnerName = None
        self._FinishTime = None
        self._StepStatus = None

    @property
    def StepName(self):
        """步骤名
        :rtype: str
        """
        return self._StepName

    @StepName.setter
    def StepName(self, StepName):
        self._StepName = StepName

    @property
    def OwnerName(self):
        """处理人
        :rtype: str
        """
        return self._OwnerName

    @OwnerName.setter
    def OwnerName(self, OwnerName):
        self._OwnerName = OwnerName

    @property
    def FinishTime(self):
        """完成时间
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def StepStatus(self):
        """此步骤状态
        :rtype: str
        """
        return self._StepStatus

    @StepStatus.setter
    def StepStatus(self, StepStatus):
        self._StepStatus = StepStatus


    def _deserialize(self, params):
        self._StepName = params.get("StepName")
        self._OwnerName = params.get("OwnerName")
        self._FinishTime = params.get("FinishTime")
        self._StepStatus = params.get("StepStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtherDevReceivingInfo(AbstractModel):
    """其他设备收货信息

    """

    def __init__(self):
        r"""
        :param _DeviceSn: 设备sn
        :type DeviceSn: str
        :param _TypeName: 'USB', '移动硬盘', '网络设备板卡', '网络设备模块', '服务器硬盘', '服务器内存', '其他'
        :type TypeName: str
        :param _Manufacturer: 厂商
        :type Manufacturer: str
        :param _HardwareMemo: 硬件备注
        :type HardwareMemo: str
        """
        self._DeviceSn = None
        self._TypeName = None
        self._Manufacturer = None
        self._HardwareMemo = None

    @property
    def DeviceSn(self):
        """设备sn
        :rtype: str
        """
        return self._DeviceSn

    @DeviceSn.setter
    def DeviceSn(self, DeviceSn):
        self._DeviceSn = DeviceSn

    @property
    def TypeName(self):
        """'USB', '移动硬盘', '网络设备板卡', '网络设备模块', '服务器硬盘', '服务器内存', '其他'
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def Manufacturer(self):
        """厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def HardwareMemo(self):
        """硬件备注
        :rtype: str
        """
        return self._HardwareMemo

    @HardwareMemo.setter
    def HardwareMemo(self, HardwareMemo):
        self._HardwareMemo = HardwareMemo


    def _deserialize(self, params):
        self._DeviceSn = params.get("DeviceSn")
        self._TypeName = params.get("TypeName")
        self._Manufacturer = params.get("Manufacturer")
        self._HardwareMemo = params.get("HardwareMemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Personnel(AbstractModel):
    """到访人员

    """

    def __init__(self):
        r"""
        :param _IDCardNumber: 证件号码
        :type IDCardNumber: str
        :param _IDCardType: 证件类型。对应关系如下：IDENTITY_CARD: 身份证,
HONG_KONG_AND_MACAO_PASS: 港澳通行证',
PASSPORT: 护照,
DRIVING_LICENSE: 驾照,
OTHER: 其他
        :type IDCardType: str
        :param _Company: 公司名称
        :type Company: str
        :param _LanguageType: 语言。对应关系：ENGLISH: 英文, CHINESE: 中文
        :type LanguageType: str
        :param _Name: 姓名
        :type Name: str
        :param _TelNumber: 电话
        :type TelNumber: str
        :param _Position: 职位
        :type Position: str
        :param _Wechat: 微信
        :type Wechat: str
        :param _Email: 邮箱
        :type Email: str
        """
        self._IDCardNumber = None
        self._IDCardType = None
        self._Company = None
        self._LanguageType = None
        self._Name = None
        self._TelNumber = None
        self._Position = None
        self._Wechat = None
        self._Email = None

    @property
    def IDCardNumber(self):
        """证件号码
        :rtype: str
        """
        return self._IDCardNumber

    @IDCardNumber.setter
    def IDCardNumber(self, IDCardNumber):
        self._IDCardNumber = IDCardNumber

    @property
    def IDCardType(self):
        """证件类型。对应关系如下：IDENTITY_CARD: 身份证,
HONG_KONG_AND_MACAO_PASS: 港澳通行证',
PASSPORT: 护照,
DRIVING_LICENSE: 驾照,
OTHER: 其他
        :rtype: str
        """
        return self._IDCardType

    @IDCardType.setter
    def IDCardType(self, IDCardType):
        self._IDCardType = IDCardType

    @property
    def Company(self):
        """公司名称
        :rtype: str
        """
        return self._Company

    @Company.setter
    def Company(self, Company):
        self._Company = Company

    @property
    def LanguageType(self):
        """语言。对应关系：ENGLISH: 英文, CHINESE: 中文
        :rtype: str
        """
        return self._LanguageType

    @LanguageType.setter
    def LanguageType(self, LanguageType):
        self._LanguageType = LanguageType

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TelNumber(self):
        """电话
        :rtype: str
        """
        return self._TelNumber

    @TelNumber.setter
    def TelNumber(self, TelNumber):
        self._TelNumber = TelNumber

    @property
    def Position(self):
        """职位
        :rtype: str
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Wechat(self):
        """微信
        :rtype: str
        """
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat

    @property
    def Email(self):
        """邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._IDCardNumber = params.get("IDCardNumber")
        self._IDCardType = params.get("IDCardType")
        self._Company = params.get("Company")
        self._LanguageType = params.get("LanguageType")
        self._Name = params.get("Name")
        self._TelNumber = params.get("TelNumber")
        self._Position = params.get("Position")
        self._Wechat = params.get("Wechat")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonnelVisitBaseInfo(AbstractModel):
    """人员到访工单基本信息

    """

    def __init__(self):
        r"""
        :param _IdcName: 机房名称
        :type IdcName: str
        :param _VisitReason: 到访原因。到访原因，映射关系：DEVICE_MAINTENANCE 设备维护 DEVICE_MOVE 设备收货上下架 CHECK 盘点 OTHER 其他
        :type VisitReason: list of str
        :param _VisitRemark: 到访原因
        :type VisitRemark: str
        :param _EnterStartTime: 到访结束时间
        :type EnterStartTime: str
        :param _EnterEndTime: 到访开始时间
        :type EnterEndTime: str
        :param _IdcUnitNameList: 机房管理单元列表
        :type IdcUnitNameList: list of str
        """
        self._IdcName = None
        self._VisitReason = None
        self._VisitRemark = None
        self._EnterStartTime = None
        self._EnterEndTime = None
        self._IdcUnitNameList = None

    @property
    def IdcName(self):
        """机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def VisitReason(self):
        """到访原因。到访原因，映射关系：DEVICE_MAINTENANCE 设备维护 DEVICE_MOVE 设备收货上下架 CHECK 盘点 OTHER 其他
        :rtype: list of str
        """
        return self._VisitReason

    @VisitReason.setter
    def VisitReason(self, VisitReason):
        self._VisitReason = VisitReason

    @property
    def VisitRemark(self):
        """到访原因
        :rtype: str
        """
        return self._VisitRemark

    @VisitRemark.setter
    def VisitRemark(self, VisitRemark):
        self._VisitRemark = VisitRemark

    @property
    def EnterStartTime(self):
        """到访结束时间
        :rtype: str
        """
        return self._EnterStartTime

    @EnterStartTime.setter
    def EnterStartTime(self, EnterStartTime):
        self._EnterStartTime = EnterStartTime

    @property
    def EnterEndTime(self):
        """到访开始时间
        :rtype: str
        """
        return self._EnterEndTime

    @EnterEndTime.setter
    def EnterEndTime(self, EnterEndTime):
        self._EnterEndTime = EnterEndTime

    @property
    def IdcUnitNameList(self):
        """机房管理单元列表
        :rtype: list of str
        """
        return self._IdcUnitNameList

    @IdcUnitNameList.setter
    def IdcUnitNameList(self, IdcUnitNameList):
        self._IdcUnitNameList = IdcUnitNameList


    def _deserialize(self, params):
        self._IdcName = params.get("IdcName")
        self._VisitReason = params.get("VisitReason")
        self._VisitRemark = params.get("VisitRemark")
        self._EnterStartTime = params.get("EnterStartTime")
        self._EnterEndTime = params.get("EnterEndTime")
        self._IdcUnitNameList = params.get("IdcUnitNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Position(AbstractModel):
    """机位信息

    """

    def __init__(self):
        r"""
        :param _PositionId: 机位ID
        :type PositionId: int
        :param _Height: 机位高度
        :type Height: int
        :param _PositionCode: 机位编号
        :type PositionCode: str
        :param _PositionStatus: 机位状态,0 空闲,1 已用,2 不可用,3 预占用,4 预留
        :type PositionStatus: int
        :param _PlanDeviceType: 设备规划类型ID
        :type PlanDeviceType: int
        :param _IdcUnitId: 机位所属的机房管理单元ID
        :type IdcUnitId: int
        :param _RackId: 机位所属的机架ID
        :type RackId: int
        :param _RackName: 机位所属的机架名称
        :type RackName: str
        :param _IdcUnitName: 机位所属的机房管理单元名称
        :type IdcUnitName: str
        :param _IdcName: 机位所属的机房名称
        :type IdcName: str
        :param _IdcId: 机位所属的机房ID
        :type IdcId: int
        :param _Sn: 机位上如果有设备，该字段代表设备的 SN 码，如果是空闲机位，不返回该字段。
        :type Sn: str
        :param _AssetId: 机位上如果有设备，该字段代表设备的固资号，如果是空闲机位，不返回该字段。
        :type AssetId: str
        :param _ModelVersion: 机位上如果有设备，该字段代表设备的设备型号加版本号，如果是空闲机位，不返回该字段。
        :type ModelVersion: str
        """
        self._PositionId = None
        self._Height = None
        self._PositionCode = None
        self._PositionStatus = None
        self._PlanDeviceType = None
        self._IdcUnitId = None
        self._RackId = None
        self._RackName = None
        self._IdcUnitName = None
        self._IdcName = None
        self._IdcId = None
        self._Sn = None
        self._AssetId = None
        self._ModelVersion = None

    @property
    def PositionId(self):
        """机位ID
        :rtype: int
        """
        return self._PositionId

    @PositionId.setter
    def PositionId(self, PositionId):
        self._PositionId = PositionId

    @property
    def Height(self):
        """机位高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def PositionCode(self):
        """机位编号
        :rtype: str
        """
        return self._PositionCode

    @PositionCode.setter
    def PositionCode(self, PositionCode):
        self._PositionCode = PositionCode

    @property
    def PositionStatus(self):
        """机位状态,0 空闲,1 已用,2 不可用,3 预占用,4 预留
        :rtype: int
        """
        return self._PositionStatus

    @PositionStatus.setter
    def PositionStatus(self, PositionStatus):
        self._PositionStatus = PositionStatus

    @property
    def PlanDeviceType(self):
        """设备规划类型ID
        :rtype: int
        """
        return self._PlanDeviceType

    @PlanDeviceType.setter
    def PlanDeviceType(self, PlanDeviceType):
        self._PlanDeviceType = PlanDeviceType

    @property
    def IdcUnitId(self):
        """机位所属的机房管理单元ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId

    @property
    def RackId(self):
        """机位所属的机架ID
        :rtype: int
        """
        return self._RackId

    @RackId.setter
    def RackId(self, RackId):
        self._RackId = RackId

    @property
    def RackName(self):
        """机位所属的机架名称
        :rtype: str
        """
        return self._RackName

    @RackName.setter
    def RackName(self, RackName):
        self._RackName = RackName

    @property
    def IdcUnitName(self):
        """机位所属的机房管理单元名称
        :rtype: str
        """
        return self._IdcUnitName

    @IdcUnitName.setter
    def IdcUnitName(self, IdcUnitName):
        self._IdcUnitName = IdcUnitName

    @property
    def IdcName(self):
        """机位所属的机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def IdcId(self):
        """机位所属的机房ID
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def Sn(self):
        """机位上如果有设备，该字段代表设备的 SN 码，如果是空闲机位，不返回该字段。
        :rtype: str
        """
        return self._Sn

    @Sn.setter
    def Sn(self, Sn):
        self._Sn = Sn

    @property
    def AssetId(self):
        """机位上如果有设备，该字段代表设备的固资号，如果是空闲机位，不返回该字段。
        :rtype: str
        """
        return self._AssetId

    @AssetId.setter
    def AssetId(self, AssetId):
        self._AssetId = AssetId

    @property
    def ModelVersion(self):
        """机位上如果有设备，该字段代表设备的设备型号加版本号，如果是空闲机位，不返回该字段。
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion


    def _deserialize(self, params):
        self._PositionId = params.get("PositionId")
        self._Height = params.get("Height")
        self._PositionCode = params.get("PositionCode")
        self._PositionStatus = params.get("PositionStatus")
        self._PlanDeviceType = params.get("PlanDeviceType")
        self._IdcUnitId = params.get("IdcUnitId")
        self._RackId = params.get("RackId")
        self._RackName = params.get("RackName")
        self._IdcUnitName = params.get("IdcUnitName")
        self._IdcName = params.get("IdcName")
        self._IdcId = params.get("IdcId")
        self._Sn = params.get("Sn")
        self._AssetId = params.get("AssetId")
        self._ModelVersion = params.get("ModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PositionStatusItem(AbstractModel):
    """机位状态及对应的数量

    """

    def __init__(self):
        r"""
        :param _PositionStatus: 状态值
        :type PositionStatus: int
        :param _Count: 对应的机位数量
        :type Count: int
        """
        self._PositionStatus = None
        self._Count = None

    @property
    def PositionStatus(self):
        """状态值
        :rtype: int
        """
        return self._PositionStatus

    @PositionStatus.setter
    def PositionStatus(self, PositionStatus):
        self._PositionStatus = PositionStatus

    @property
    def Count(self):
        """对应的机位数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._PositionStatus = params.get("PositionStatus")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PowerOffConfirm(AbstractModel):
    """关电确认信息

    """

    def __init__(self):
        r"""
        :param _ConfirmContact: 联系人
        :type ConfirmContact: str
        :param _ConfirmContactNumber: 联系人电话
        :type ConfirmContactNumber: str
        """
        self._ConfirmContact = None
        self._ConfirmContactNumber = None

    @property
    def ConfirmContact(self):
        """联系人
        :rtype: str
        """
        return self._ConfirmContact

    @ConfirmContact.setter
    def ConfirmContact(self, ConfirmContact):
        self._ConfirmContact = ConfirmContact

    @property
    def ConfirmContactNumber(self):
        """联系人电话
        :rtype: str
        """
        return self._ConfirmContactNumber

    @ConfirmContactNumber.setter
    def ConfirmContactNumber(self, ConfirmContactNumber):
        self._ConfirmContactNumber = ConfirmContactNumber


    def _deserialize(self, params):
        self._ConfirmContact = params.get("ConfirmContact")
        self._ConfirmContactNumber = params.get("ConfirmContactNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rack(AbstractModel):
    """机架的信息

    """

    def __init__(self):
        r"""
        :param _RackName: 机架名称
        :type RackName: str
        :param _IdcUnitId: 机架所属的机房管理单元ID
        :type IdcUnitId: int
        :param _IdcUnitName: 机架所属的机房管理单元名称
        :type IdcUnitName: str
        :param _IdcName: 机架所属的机房名称
        :type IdcName: str
        :param _IdcId: 机架所属的机房ID
        :type IdcId: int
        :param _RackId: 机架ID
        :type RackId: int
        :param _IsPowerOn: 是否开电
        :type IsPowerOn: bool
        :param _RackOpenTime: 机架最近一次开电时间，YYYY-MM-DD 格式
        :type RackOpenTime: str
        :param _HostingType: 托管类型
        :type HostingType: str
        """
        self._RackName = None
        self._IdcUnitId = None
        self._IdcUnitName = None
        self._IdcName = None
        self._IdcId = None
        self._RackId = None
        self._IsPowerOn = None
        self._RackOpenTime = None
        self._HostingType = None

    @property
    def RackName(self):
        """机架名称
        :rtype: str
        """
        return self._RackName

    @RackName.setter
    def RackName(self, RackName):
        self._RackName = RackName

    @property
    def IdcUnitId(self):
        """机架所属的机房管理单元ID
        :rtype: int
        """
        return self._IdcUnitId

    @IdcUnitId.setter
    def IdcUnitId(self, IdcUnitId):
        self._IdcUnitId = IdcUnitId

    @property
    def IdcUnitName(self):
        """机架所属的机房管理单元名称
        :rtype: str
        """
        return self._IdcUnitName

    @IdcUnitName.setter
    def IdcUnitName(self, IdcUnitName):
        self._IdcUnitName = IdcUnitName

    @property
    def IdcName(self):
        """机架所属的机房名称
        :rtype: str
        """
        return self._IdcName

    @IdcName.setter
    def IdcName(self, IdcName):
        self._IdcName = IdcName

    @property
    def IdcId(self):
        """机架所属的机房ID
        :rtype: int
        """
        return self._IdcId

    @IdcId.setter
    def IdcId(self, IdcId):
        self._IdcId = IdcId

    @property
    def RackId(self):
        """机架ID
        :rtype: int
        """
        return self._RackId

    @RackId.setter
    def RackId(self, RackId):
        self._RackId = RackId

    @property
    def IsPowerOn(self):
        """是否开电
        :rtype: bool
        """
        return self._IsPowerOn

    @IsPowerOn.setter
    def IsPowerOn(self, IsPowerOn):
        self._IsPowerOn = IsPowerOn

    @property
    def RackOpenTime(self):
        """机架最近一次开电时间，YYYY-MM-DD 格式
        :rtype: str
        """
        return self._RackOpenTime

    @RackOpenTime.setter
    def RackOpenTime(self, RackOpenTime):
        self._RackOpenTime = RackOpenTime

    @property
    def HostingType(self):
        """托管类型
        :rtype: str
        """
        return self._HostingType

    @HostingType.setter
    def HostingType(self, HostingType):
        self._HostingType = HostingType


    def _deserialize(self, params):
        self._RackName = params.get("RackName")
        self._IdcUnitId = params.get("IdcUnitId")
        self._IdcUnitName = params.get("IdcUnitName")
        self._IdcName = params.get("IdcName")
        self._IdcId = params.get("IdcId")
        self._RackId = params.get("RackId")
        self._IsPowerOn = params.get("IsPowerOn")
        self._RackOpenTime = params.get("RackOpenTime")
        self._HostingType = params.get("HostingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RackUsage(AbstractModel):
    """机架用量

    """

    def __init__(self):
        r"""
        :param _RackId: 机架ID
        :type RackId: int
        :param _UsedNum: 已使用的机位数量
        :type UsedNum: int
        :param _UnusedNum: 空闲机位数量
        :type UnusedNum: int
        :param _RackShortName: 机架简称
        :type RackShortName: str
        :param _TotalNum: 机位总数
        :type TotalNum: int
        :param _UsedRate: 机位使用率
        :type UsedRate: float
        """
        self._RackId = None
        self._UsedNum = None
        self._UnusedNum = None
        self._RackShortName = None
        self._TotalNum = None
        self._UsedRate = None

    @property
    def RackId(self):
        """机架ID
        :rtype: int
        """
        return self._RackId

    @RackId.setter
    def RackId(self, RackId):
        self._RackId = RackId

    @property
    def UsedNum(self):
        """已使用的机位数量
        :rtype: int
        """
        return self._UsedNum

    @UsedNum.setter
    def UsedNum(self, UsedNum):
        self._UsedNum = UsedNum

    @property
    def UnusedNum(self):
        """空闲机位数量
        :rtype: int
        """
        return self._UnusedNum

    @UnusedNum.setter
    def UnusedNum(self, UnusedNum):
        self._UnusedNum = UnusedNum

    @property
    def RackShortName(self):
        """机架简称
        :rtype: str
        """
        return self._RackShortName

    @RackShortName.setter
    def RackShortName(self, RackShortName):
        self._RackShortName = RackShortName

    @property
    def TotalNum(self):
        """机位总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def UsedRate(self):
        """机位使用率
        :rtype: float
        """
        return self._UsedRate

    @UsedRate.setter
    def UsedRate(self, UsedRate):
        self._UsedRate = UsedRate


    def _deserialize(self, params):
        self._RackId = params.get("RackId")
        self._UsedNum = params.get("UsedNum")
        self._UnusedNum = params.get("UnusedNum")
        self._RackShortName = params.get("RackShortName")
        self._TotalNum = params.get("TotalNum")
        self._UsedRate = params.get("UsedRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelfOperation(AbstractModel):
    """客户自行上门信息

    """

    def __init__(self):
        r"""
        :param _StuffContact: 联系人员电话
        :type StuffContact: str
        :param _StuffIDCard: 身份证号
        :type StuffIDCard: str
        :param _StuffName: 人员姓名
        :type StuffName: str
        :param _OperationTime: 上门时间
        :type OperationTime: str
        """
        self._StuffContact = None
        self._StuffIDCard = None
        self._StuffName = None
        self._OperationTime = None

    @property
    def StuffContact(self):
        """联系人员电话
        :rtype: str
        """
        return self._StuffContact

    @StuffContact.setter
    def StuffContact(self, StuffContact):
        self._StuffContact = StuffContact

    @property
    def StuffIDCard(self):
        """身份证号
        :rtype: str
        """
        return self._StuffIDCard

    @StuffIDCard.setter
    def StuffIDCard(self, StuffIDCard):
        self._StuffIDCard = StuffIDCard

    @property
    def StuffName(self):
        """人员姓名
        :rtype: str
        """
        return self._StuffName

    @StuffName.setter
    def StuffName(self, StuffName):
        self._StuffName = StuffName

    @property
    def OperationTime(self):
        """上门时间
        :rtype: str
        """
        return self._OperationTime

    @OperationTime.setter
    def OperationTime(self, OperationTime):
        self._OperationTime = OperationTime


    def _deserialize(self, params):
        self._StuffContact = params.get("StuffContact")
        self._StuffIDCard = params.get("StuffIDCard")
        self._StuffName = params.get("StuffName")
        self._OperationTime = params.get("OperationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerModel(AbstractModel):
    """服务器设备型号

    """

    def __init__(self):
        r"""
        :param _DevModel: 型号名称
        :type DevModel: str
        :param _DevNode: 节点数
        :type DevNode: str
        :param _DevHeight: 设备高度
        :type DevHeight: str
        :param _PowerEnergy: 功耗
        :type PowerEnergy: str
        :param _PowerportType: 电源接口型号
        :type PowerportType: str
        :param _PowermoduleNum: 电源模块数量
        :type PowermoduleNum: str
        :param _InwindPosition: 进风口位置
        :type InwindPosition: str
        :param _OutwindPosition: 出风口位置
        :type OutwindPosition: str
        :param _NetportPosition: 网卡接口位置
        :type NetportPosition: str
        :param _DevWidth: 宽度
        :type DevWidth: str
        :param _DevDepth: 深度
        :type DevDepth: str
        :param _DevWeight: 重量
        :type DevWeight: str
        :param _PowerModule: 电源模块
        :type PowerModule: str
        :param _PowermodulePosition: 电源模块位置
        :type PowermodulePosition: str
        :param _NetportType: 网络接口类型
        :type NetportType: str
        :param _NetSpeed: 网卡速率
        :type NetSpeed: str
        :param _CheckResult: 0 代表在当前园区没评估过，1 代表完全满足IDC准入标准 2 代表存在托管风险 3 代表不满足IDC准入标准
        :type CheckResult: int
        :param _Version: 版本号
        :type Version: str
        :param _ModelVersion: 型号和版本的组合名称
        :type ModelVersion: str
        """
        self._DevModel = None
        self._DevNode = None
        self._DevHeight = None
        self._PowerEnergy = None
        self._PowerportType = None
        self._PowermoduleNum = None
        self._InwindPosition = None
        self._OutwindPosition = None
        self._NetportPosition = None
        self._DevWidth = None
        self._DevDepth = None
        self._DevWeight = None
        self._PowerModule = None
        self._PowermodulePosition = None
        self._NetportType = None
        self._NetSpeed = None
        self._CheckResult = None
        self._Version = None
        self._ModelVersion = None

    @property
    def DevModel(self):
        """型号名称
        :rtype: str
        """
        return self._DevModel

    @DevModel.setter
    def DevModel(self, DevModel):
        self._DevModel = DevModel

    @property
    def DevNode(self):
        """节点数
        :rtype: str
        """
        return self._DevNode

    @DevNode.setter
    def DevNode(self, DevNode):
        self._DevNode = DevNode

    @property
    def DevHeight(self):
        """设备高度
        :rtype: str
        """
        return self._DevHeight

    @DevHeight.setter
    def DevHeight(self, DevHeight):
        self._DevHeight = DevHeight

    @property
    def PowerEnergy(self):
        """功耗
        :rtype: str
        """
        return self._PowerEnergy

    @PowerEnergy.setter
    def PowerEnergy(self, PowerEnergy):
        self._PowerEnergy = PowerEnergy

    @property
    def PowerportType(self):
        """电源接口型号
        :rtype: str
        """
        return self._PowerportType

    @PowerportType.setter
    def PowerportType(self, PowerportType):
        self._PowerportType = PowerportType

    @property
    def PowermoduleNum(self):
        """电源模块数量
        :rtype: str
        """
        return self._PowermoduleNum

    @PowermoduleNum.setter
    def PowermoduleNum(self, PowermoduleNum):
        self._PowermoduleNum = PowermoduleNum

    @property
    def InwindPosition(self):
        """进风口位置
        :rtype: str
        """
        return self._InwindPosition

    @InwindPosition.setter
    def InwindPosition(self, InwindPosition):
        self._InwindPosition = InwindPosition

    @property
    def OutwindPosition(self):
        """出风口位置
        :rtype: str
        """
        return self._OutwindPosition

    @OutwindPosition.setter
    def OutwindPosition(self, OutwindPosition):
        self._OutwindPosition = OutwindPosition

    @property
    def NetportPosition(self):
        """网卡接口位置
        :rtype: str
        """
        return self._NetportPosition

    @NetportPosition.setter
    def NetportPosition(self, NetportPosition):
        self._NetportPosition = NetportPosition

    @property
    def DevWidth(self):
        """宽度
        :rtype: str
        """
        return self._DevWidth

    @DevWidth.setter
    def DevWidth(self, DevWidth):
        self._DevWidth = DevWidth

    @property
    def DevDepth(self):
        """深度
        :rtype: str
        """
        return self._DevDepth

    @DevDepth.setter
    def DevDepth(self, DevDepth):
        self._DevDepth = DevDepth

    @property
    def DevWeight(self):
        """重量
        :rtype: str
        """
        return self._DevWeight

    @DevWeight.setter
    def DevWeight(self, DevWeight):
        self._DevWeight = DevWeight

    @property
    def PowerModule(self):
        """电源模块
        :rtype: str
        """
        return self._PowerModule

    @PowerModule.setter
    def PowerModule(self, PowerModule):
        self._PowerModule = PowerModule

    @property
    def PowermodulePosition(self):
        """电源模块位置
        :rtype: str
        """
        return self._PowermodulePosition

    @PowermodulePosition.setter
    def PowermodulePosition(self, PowermodulePosition):
        self._PowermodulePosition = PowermodulePosition

    @property
    def NetportType(self):
        """网络接口类型
        :rtype: str
        """
        return self._NetportType

    @NetportType.setter
    def NetportType(self, NetportType):
        self._NetportType = NetportType

    @property
    def NetSpeed(self):
        """网卡速率
        :rtype: str
        """
        return self._NetSpeed

    @NetSpeed.setter
    def NetSpeed(self, NetSpeed):
        self._NetSpeed = NetSpeed

    @property
    def CheckResult(self):
        """0 代表在当前园区没评估过，1 代表完全满足IDC准入标准 2 代表存在托管风险 3 代表不满足IDC准入标准
        :rtype: int
        """
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def Version(self):
        """版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ModelVersion(self):
        """型号和版本的组合名称
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion


    def _deserialize(self, params):
        self._DevModel = params.get("DevModel")
        self._DevNode = params.get("DevNode")
        self._DevHeight = params.get("DevHeight")
        self._PowerEnergy = params.get("PowerEnergy")
        self._PowerportType = params.get("PowerportType")
        self._PowermoduleNum = params.get("PowermoduleNum")
        self._InwindPosition = params.get("InwindPosition")
        self._OutwindPosition = params.get("OutwindPosition")
        self._NetportPosition = params.get("NetportPosition")
        self._DevWidth = params.get("DevWidth")
        self._DevDepth = params.get("DevDepth")
        self._DevWeight = params.get("DevWeight")
        self._PowerModule = params.get("PowerModule")
        self._PowermodulePosition = params.get("PowermodulePosition")
        self._NetportType = params.get("NetportType")
        self._NetSpeed = params.get("NetSpeed")
        self._CheckResult = params.get("CheckResult")
        self._Version = params.get("Version")
        self._ModelVersion = params.get("ModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerReceivingInfo(AbstractModel):
    """服务器收货信息

    """

    def __init__(self):
        r"""
        :param _DeviceSn: 设备sn
        :type DeviceSn: str
        :param _ModelVersion: 设备型号-版本
        :type ModelVersion: str
        :param _Need10GbSlot: 需要万兆机位
        :type Need10GbSlot: str
        :param _NeedDCPower: 需要直流电
        :type NeedDCPower: str
        :param _NeedExtranet: 需要外网
        :type NeedExtranet: str
        :param _NeedVirtualization: 需要虚拟化
        :type NeedVirtualization: str
        :param _HardwareMemo: 硬件备注
        :type HardwareMemo: str
        """
        self._DeviceSn = None
        self._ModelVersion = None
        self._Need10GbSlot = None
        self._NeedDCPower = None
        self._NeedExtranet = None
        self._NeedVirtualization = None
        self._HardwareMemo = None

    @property
    def DeviceSn(self):
        """设备sn
        :rtype: str
        """
        return self._DeviceSn

    @DeviceSn.setter
    def DeviceSn(self, DeviceSn):
        self._DeviceSn = DeviceSn

    @property
    def ModelVersion(self):
        """设备型号-版本
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def Need10GbSlot(self):
        """需要万兆机位
        :rtype: str
        """
        return self._Need10GbSlot

    @Need10GbSlot.setter
    def Need10GbSlot(self, Need10GbSlot):
        self._Need10GbSlot = Need10GbSlot

    @property
    def NeedDCPower(self):
        """需要直流电
        :rtype: str
        """
        return self._NeedDCPower

    @NeedDCPower.setter
    def NeedDCPower(self, NeedDCPower):
        self._NeedDCPower = NeedDCPower

    @property
    def NeedExtranet(self):
        """需要外网
        :rtype: str
        """
        return self._NeedExtranet

    @NeedExtranet.setter
    def NeedExtranet(self, NeedExtranet):
        self._NeedExtranet = NeedExtranet

    @property
    def NeedVirtualization(self):
        """需要虚拟化
        :rtype: str
        """
        return self._NeedVirtualization

    @NeedVirtualization.setter
    def NeedVirtualization(self, NeedVirtualization):
        self._NeedVirtualization = NeedVirtualization

    @property
    def HardwareMemo(self):
        """硬件备注
        :rtype: str
        """
        return self._HardwareMemo

    @HardwareMemo.setter
    def HardwareMemo(self, HardwareMemo):
        self._HardwareMemo = HardwareMemo


    def _deserialize(self, params):
        self._DeviceSn = params.get("DeviceSn")
        self._ModelVersion = params.get("ModelVersion")
        self._Need10GbSlot = params.get("Need10GbSlot")
        self._NeedDCPower = params.get("NeedDCPower")
        self._NeedExtranet = params.get("NeedExtranet")
        self._NeedVirtualization = params.get("NeedVirtualization")
        self._HardwareMemo = params.get("HardwareMemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateOption(AbstractModel):
    """型号模板的选项

    """

    def __init__(self):
        r"""
        :param _OptionName: 选项名称
        :type OptionName: str
        :param _Standard: 腾讯的标准
        :type Standard: str
        :param _StandardInfo: 腾讯标准的展示字段
        :type StandardInfo: str
        :param _OptionKey: 选项的唯一标识
        :type OptionKey: str
        :param _InputType: 输入的类型
        :type InputType: str
        :param _ValueType: 输入值的类型
        :type ValueType: str
        :param _CompareType: 是否符合腾讯标准的比较方式，-- 为不做比较
        :type CompareType: str
        :param _OptionValueSet: 下拉列表中填充的选项值
        :type OptionValueSet: list of OptionValueItem
        :param _InputHint: 输入框中的占位的提示符
        :type InputHint: str
        :param _InputInfo: 输入框下方的提示文案
        :type InputInfo: str
        :param _OptionValue: 客户写入的值
        :type OptionValue: str
        """
        self._OptionName = None
        self._Standard = None
        self._StandardInfo = None
        self._OptionKey = None
        self._InputType = None
        self._ValueType = None
        self._CompareType = None
        self._OptionValueSet = None
        self._InputHint = None
        self._InputInfo = None
        self._OptionValue = None

    @property
    def OptionName(self):
        """选项名称
        :rtype: str
        """
        return self._OptionName

    @OptionName.setter
    def OptionName(self, OptionName):
        self._OptionName = OptionName

    @property
    def Standard(self):
        """腾讯的标准
        :rtype: str
        """
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def StandardInfo(self):
        """腾讯标准的展示字段
        :rtype: str
        """
        return self._StandardInfo

    @StandardInfo.setter
    def StandardInfo(self, StandardInfo):
        self._StandardInfo = StandardInfo

    @property
    def OptionKey(self):
        """选项的唯一标识
        :rtype: str
        """
        return self._OptionKey

    @OptionKey.setter
    def OptionKey(self, OptionKey):
        self._OptionKey = OptionKey

    @property
    def InputType(self):
        """输入的类型
        :rtype: str
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def ValueType(self):
        """输入值的类型
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def CompareType(self):
        """是否符合腾讯标准的比较方式，-- 为不做比较
        :rtype: str
        """
        return self._CompareType

    @CompareType.setter
    def CompareType(self, CompareType):
        self._CompareType = CompareType

    @property
    def OptionValueSet(self):
        """下拉列表中填充的选项值
        :rtype: list of OptionValueItem
        """
        return self._OptionValueSet

    @OptionValueSet.setter
    def OptionValueSet(self, OptionValueSet):
        self._OptionValueSet = OptionValueSet

    @property
    def InputHint(self):
        """输入框中的占位的提示符
        :rtype: str
        """
        return self._InputHint

    @InputHint.setter
    def InputHint(self, InputHint):
        self._InputHint = InputHint

    @property
    def InputInfo(self):
        """输入框下方的提示文案
        :rtype: str
        """
        return self._InputInfo

    @InputInfo.setter
    def InputInfo(self, InputInfo):
        self._InputInfo = InputInfo

    @property
    def OptionValue(self):
        """客户写入的值
        :rtype: str
        """
        return self._OptionValue

    @OptionValue.setter
    def OptionValue(self, OptionValue):
        self._OptionValue = OptionValue


    def _deserialize(self, params):
        self._OptionName = params.get("OptionName")
        self._Standard = params.get("Standard")
        self._StandardInfo = params.get("StandardInfo")
        self._OptionKey = params.get("OptionKey")
        self._InputType = params.get("InputType")
        self._ValueType = params.get("ValueType")
        self._CompareType = params.get("CompareType")
        if params.get("OptionValueSet") is not None:
            self._OptionValueSet = []
            for item in params.get("OptionValueSet"):
                obj = OptionValueItem()
                obj._deserialize(item)
                self._OptionValueSet.append(obj)
        self._InputHint = params.get("InputHint")
        self._InputInfo = params.get("InputInfo")
        self._OptionValue = params.get("OptionValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WireReceivingInfo(AbstractModel):
    """线材收货信息

    """

    def __init__(self):
        r"""
        :param _TypeName: '光纤', '网线', '电源线'
        :type TypeName: str
        :param _Quantity: 数量
        :type Quantity: int
        :param _Unit: '箱', '卷', '套'
        :type Unit: str
        :param _ReceiptNumber: 收货凭证号
        :type ReceiptNumber: str
        :param _HardwareMemo: 硬件备注
        :type HardwareMemo: str
        """
        self._TypeName = None
        self._Quantity = None
        self._Unit = None
        self._ReceiptNumber = None
        self._HardwareMemo = None

    @property
    def TypeName(self):
        """'光纤', '网线', '电源线'
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def Quantity(self):
        """数量
        :rtype: int
        """
        return self._Quantity

    @Quantity.setter
    def Quantity(self, Quantity):
        self._Quantity = Quantity

    @property
    def Unit(self):
        """'箱', '卷', '套'
        :rtype: str
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def ReceiptNumber(self):
        """收货凭证号
        :rtype: str
        """
        return self._ReceiptNumber

    @ReceiptNumber.setter
    def ReceiptNumber(self, ReceiptNumber):
        self._ReceiptNumber = ReceiptNumber

    @property
    def HardwareMemo(self):
        """硬件备注
        :rtype: str
        """
        return self._HardwareMemo

    @HardwareMemo.setter
    def HardwareMemo(self, HardwareMemo):
        self._HardwareMemo = HardwareMemo


    def _deserialize(self, params):
        self._TypeName = params.get("TypeName")
        self._Quantity = params.get("Quantity")
        self._Unit = params.get("Unit")
        self._ReceiptNumber = params.get("ReceiptNumber")
        self._HardwareMemo = params.get("HardwareMemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkOrderData(AbstractModel):
    """工单的常用信息返回

    """

    def __init__(self):
        r"""
        :param _WorkOrderId: 工单号
        :type WorkOrderId: str
        :param _ServiceType: 服务类型，一个服务可能会产生多个工单
        :type ServiceType: str
        :param _OrderType: 工单类型
        :type OrderType: str
        :param _OrderStatus: 工单状态
        :type OrderStatus: str
        :param _Creator: 工单创建人
        :type Creator: str
        :param _CreateTime: 工单创建时间
        :type CreateTime: str
        :param _FinishTime: 工单完成时间
        :type FinishTime: str
        """
        self._WorkOrderId = None
        self._ServiceType = None
        self._OrderType = None
        self._OrderStatus = None
        self._Creator = None
        self._CreateTime = None
        self._FinishTime = None

    @property
    def WorkOrderId(self):
        """工单号
        :rtype: str
        """
        return self._WorkOrderId

    @WorkOrderId.setter
    def WorkOrderId(self, WorkOrderId):
        self._WorkOrderId = WorkOrderId

    @property
    def ServiceType(self):
        """服务类型，一个服务可能会产生多个工单
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def OrderType(self):
        """工单类型
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def OrderStatus(self):
        """工单状态
        :rtype: str
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def Creator(self):
        """工单创建人
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreateTime(self):
        """工单创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FinishTime(self):
        """工单完成时间
        :rtype: str
        """
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime


    def _deserialize(self, params):
        self._WorkOrderId = params.get("WorkOrderId")
        self._ServiceType = params.get("ServiceType")
        self._OrderType = params.get("OrderType")
        self._OrderStatus = params.get("OrderStatus")
        self._Creator = params.get("Creator")
        self._CreateTime = params.get("CreateTime")
        self._FinishTime = params.get("FinishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkOrderFamilyDetail(AbstractModel):
    """带有分类的工单类型列表

    """

    def __init__(self):
        r"""
        :param _WorkOrderFamily: 工单类型大类的名称
        :type WorkOrderFamily: str
        :param _WorkOrderTypeSet: 工单类型详情列表
        :type WorkOrderTypeSet: list of WorkOrderTypeDetail
        """
        self._WorkOrderFamily = None
        self._WorkOrderTypeSet = None

    @property
    def WorkOrderFamily(self):
        """工单类型大类的名称
        :rtype: str
        """
        return self._WorkOrderFamily

    @WorkOrderFamily.setter
    def WorkOrderFamily(self, WorkOrderFamily):
        self._WorkOrderFamily = WorkOrderFamily

    @property
    def WorkOrderTypeSet(self):
        """工单类型详情列表
        :rtype: list of WorkOrderTypeDetail
        """
        return self._WorkOrderTypeSet

    @WorkOrderTypeSet.setter
    def WorkOrderTypeSet(self, WorkOrderTypeSet):
        self._WorkOrderTypeSet = WorkOrderTypeSet


    def _deserialize(self, params):
        self._WorkOrderFamily = params.get("WorkOrderFamily")
        if params.get("WorkOrderTypeSet") is not None:
            self._WorkOrderTypeSet = []
            for item in params.get("WorkOrderTypeSet"):
                obj = WorkOrderTypeDetail()
                obj._deserialize(item)
                self._WorkOrderTypeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkOrderTinyInfo(AbstractModel):
    """工单信息的简要，一般用于工单创建的返回

    """

    def __init__(self):
        r"""
        :param _WorkOrderId: 工单id
        :type WorkOrderId: str
        :param _ServiceType: 服务类型，一个服务可能会产生多个工单
        :type ServiceType: str
        :param _OrderType: 工单类型
        :type OrderType: str
        """
        self._WorkOrderId = None
        self._ServiceType = None
        self._OrderType = None

    @property
    def WorkOrderId(self):
        """工单id
        :rtype: str
        """
        return self._WorkOrderId

    @WorkOrderId.setter
    def WorkOrderId(self, WorkOrderId):
        self._WorkOrderId = WorkOrderId

    @property
    def ServiceType(self):
        """服务类型，一个服务可能会产生多个工单
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def OrderType(self):
        """工单类型
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._WorkOrderId = params.get("WorkOrderId")
        self._ServiceType = params.get("ServiceType")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkOrderTypeDetail(AbstractModel):
    """工单类型详情

    """

    def __init__(self):
        r"""
        :param _WorkOrderFamily: 工单类型所属的大类
        :type WorkOrderFamily: str
        :param _WorkOrderName: 工单类型名称
        :type WorkOrderName: str
        :param _WorkOrderType: 工单类型的唯一英文标识
        :type WorkOrderType: str
        :param _WorkOrderDescription: 工单类型简述
        :type WorkOrderDescription: str
        :param _CollectFlag: 是否被收藏
        :type CollectFlag: bool
        :param _SlaMessage: 服务时效
        :type SlaMessage: str
        """
        self._WorkOrderFamily = None
        self._WorkOrderName = None
        self._WorkOrderType = None
        self._WorkOrderDescription = None
        self._CollectFlag = None
        self._SlaMessage = None

    @property
    def WorkOrderFamily(self):
        """工单类型所属的大类
        :rtype: str
        """
        return self._WorkOrderFamily

    @WorkOrderFamily.setter
    def WorkOrderFamily(self, WorkOrderFamily):
        self._WorkOrderFamily = WorkOrderFamily

    @property
    def WorkOrderName(self):
        """工单类型名称
        :rtype: str
        """
        return self._WorkOrderName

    @WorkOrderName.setter
    def WorkOrderName(self, WorkOrderName):
        self._WorkOrderName = WorkOrderName

    @property
    def WorkOrderType(self):
        """工单类型的唯一英文标识
        :rtype: str
        """
        return self._WorkOrderType

    @WorkOrderType.setter
    def WorkOrderType(self, WorkOrderType):
        self._WorkOrderType = WorkOrderType

    @property
    def WorkOrderDescription(self):
        """工单类型简述
        :rtype: str
        """
        return self._WorkOrderDescription

    @WorkOrderDescription.setter
    def WorkOrderDescription(self, WorkOrderDescription):
        self._WorkOrderDescription = WorkOrderDescription

    @property
    def CollectFlag(self):
        """是否被收藏
        :rtype: bool
        """
        return self._CollectFlag

    @CollectFlag.setter
    def CollectFlag(self, CollectFlag):
        self._CollectFlag = CollectFlag

    @property
    def SlaMessage(self):
        """服务时效
        :rtype: str
        """
        return self._SlaMessage

    @SlaMessage.setter
    def SlaMessage(self, SlaMessage):
        self._SlaMessage = SlaMessage


    def _deserialize(self, params):
        self._WorkOrderFamily = params.get("WorkOrderFamily")
        self._WorkOrderName = params.get("WorkOrderName")
        self._WorkOrderType = params.get("WorkOrderType")
        self._WorkOrderDescription = params.get("WorkOrderDescription")
        self._CollectFlag = params.get("CollectFlag")
        self._SlaMessage = params.get("SlaMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        