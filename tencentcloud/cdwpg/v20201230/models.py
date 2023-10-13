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


class CBSSpec(AbstractModel):
    """磁盘规格

    """

    def __init__(self):
        r"""
        :param _DiskType: 盘类型
        :type DiskType: str
        :param _DiskSize: 大小
        :type DiskSize: int
        :param _DiskCount: 个数
        :type DiskCount: int
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskCount = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskCount(self):
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskCount = params.get("DiskCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargeProperties(AbstractModel):
    """计费时间参数

    """

    def __init__(self):
        r"""
        :param _RenewFlag: 1-需要自动续期
        :type RenewFlag: int
        :param _TimeSpan: 订单时间范围
        :type TimeSpan: int
        :param _TimeUnit: 时间单位，一般为h和m
        :type TimeUnit: str
        :param _PayMode: 计费类型0-按量计费，1-包年包月
        :type PayMode: int
        :param _ChargeType: PREPAID、POSTPAID_BY_HOUR
        :type ChargeType: str
        """
        self._RenewFlag = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._PayMode = None
        self._ChargeType = None

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._PayMode = params.get("PayMode")
        self._ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceByApiRequest(AbstractModel):
    """CreateInstanceByApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Zone: 可用区
        :type Zone: str
        :param _UserVPCId: 私有网络
        :type UserVPCId: str
        :param _UserSubnetId: 子网
        :type UserSubnetId: str
        :param _ChargeProperties: 计费方式
        :type ChargeProperties: :class:`tencentcloud.cdwpg.v20201230.models.ChargeProperties`
        :param _AdminPassword: 集群密码
        :type AdminPassword: str
        :param _Resources: 资源信息
        :type Resources: list of ResourceSpecNew
        :param _Tags: 标签列表
        :type Tags: :class:`tencentcloud.cdwpg.v20201230.models.Tag`
        """
        self._InstanceName = None
        self._Zone = None
        self._UserVPCId = None
        self._UserSubnetId = None
        self._ChargeProperties = None
        self._AdminPassword = None
        self._Resources = None
        self._Tags = None

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def UserVPCId(self):
        return self._UserVPCId

    @UserVPCId.setter
    def UserVPCId(self, UserVPCId):
        self._UserVPCId = UserVPCId

    @property
    def UserSubnetId(self):
        return self._UserSubnetId

    @UserSubnetId.setter
    def UserSubnetId(self, UserSubnetId):
        self._UserSubnetId = UserSubnetId

    @property
    def ChargeProperties(self):
        return self._ChargeProperties

    @ChargeProperties.setter
    def ChargeProperties(self, ChargeProperties):
        self._ChargeProperties = ChargeProperties

    @property
    def AdminPassword(self):
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._InstanceName = params.get("InstanceName")
        self._Zone = params.get("Zone")
        self._UserVPCId = params.get("UserVPCId")
        self._UserSubnetId = params.get("UserSubnetId")
        if params.get("ChargeProperties") is not None:
            self._ChargeProperties = ChargeProperties()
            self._ChargeProperties._deserialize(params.get("ChargeProperties"))
        self._AdminPassword = params.get("AdminPassword")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ResourceSpecNew()
                obj._deserialize(item)
                self._Resources.append(obj)
        if params.get("Tags") is not None:
            self._Tags = Tag()
            self._Tags._deserialize(params.get("Tags"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceByApiResponse(AbstractModel):
    """CreateInstanceByApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._InstanceId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InstanceId = params.get("InstanceId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceInfo: 实例描述信息
        :type InstanceInfo: :class:`tencentcloud.cdwpg.v20201230.models.InstanceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceInfo = None
        self._RequestId = None

    @property
    def InstanceInfo(self):
        return self._InstanceInfo

    @InstanceInfo.setter
    def InstanceInfo(self, InstanceInfo):
        self._InstanceInfo = InstanceInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceInfo") is not None:
            self._InstanceInfo = InstanceInfo()
            self._InstanceInfo._deserialize(params.get("InstanceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeInstanceStateRequest(AbstractModel):
    """DescribeInstanceState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群实例名称
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceStateResponse(AbstractModel):
    """DescribeInstanceState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceState: 集群状态，例如：Serving
        :type InstanceState: str
        :param _FlowCreateTime: 集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowCreateTime: str
        :param _FlowName: 集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowName: str
        :param _FlowProgress: 集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowProgress: float
        :param _InstanceStateDesc: 集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateDesc: str
        :param _FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMsg: str
        :param _ProcessName: 当前步骤的名称，例如：”购买资源中“
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param _BackupStatus: 集群备份任务开启状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._BackupStatus = None
        self._RequestId = None

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessName = params.get("ProcessName")
        self._BackupStatus = params.get("BackupStatus")
        self._RequestId = params.get("RequestId")


class DescribeSimpleInstancesRequest(AbstractModel):
    """DescribeSimpleInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchInstanceId: 11
        :type SearchInstanceId: str
        :param _SearchInstanceName: 11
        :type SearchInstanceName: str
        :param _Offset: 11
        :type Offset: int
        :param _Limit: 11
        :type Limit: int
        :param _SearchTags: 11
        :type SearchTags: list of str
        """
        self._SearchInstanceId = None
        self._SearchInstanceName = None
        self._Offset = None
        self._Limit = None
        self._SearchTags = None

    @property
    def SearchInstanceId(self):
        return self._SearchInstanceId

    @SearchInstanceId.setter
    def SearchInstanceId(self, SearchInstanceId):
        self._SearchInstanceId = SearchInstanceId

    @property
    def SearchInstanceName(self):
        return self._SearchInstanceName

    @SearchInstanceName.setter
    def SearchInstanceName(self, SearchInstanceName):
        self._SearchInstanceName = SearchInstanceName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchTags(self):
        return self._SearchTags

    @SearchTags.setter
    def SearchTags(self, SearchTags):
        self._SearchTags = SearchTags


    def _deserialize(self, params):
        self._SearchInstanceId = params.get("SearchInstanceId")
        self._SearchInstanceName = params.get("SearchInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchTags = params.get("SearchTags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSimpleInstancesResponse(AbstractModel):
    """DescribeSimpleInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _InstancesList: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancesList: list of InstanceSimpleInfoNew
        :param _ErrorMsg: -
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstancesList = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstancesList(self):
        return self._InstancesList

    @InstancesList.setter
    def InstancesList(self, InstancesList):
        self._InstancesList = InstancesList

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstancesList") is not None:
            self._InstancesList = []
            for item in params.get("InstancesList"):
                obj = InstanceSimpleInfoNew()
                obj._deserialize(item)
                self._InstancesList.append(obj)
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DestroyInstanceByApiRequest(AbstractModel):
    """DestroyInstanceByApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例名称，例如"cdwpg-xxxx"
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyInstanceByApiResponse(AbstractModel):
    """DestroyInstanceByApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowId: 销毁流程Id
        :type FlowId: str
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def FlowId(self):
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """云原生实例详情

    """

    def __init__(self):
        r"""
        :param _ID: ID值
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _InstanceType: cdwpg-cn或者其他
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _InstanceName: cdwpg-cn或者其他
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Status: Running
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StatusDesc: 运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _InstanceStateInfo: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateInfo: :class:`tencentcloud.cdwpg.v20201230.models.InstanceStateInfo`
        :param _InstanceID: -
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceID: str
        :param _CreateTime: 2022-09-05 20:00:01
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Region: ap-chongqing
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Zone: ap
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _RegionDesc: region
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionDesc: str
        :param _ZoneDesc: zone
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneDesc: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Version: v3
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Charset: 字符集
注意：此字段可能返回 null，表示取不到有效值。
        :type Charset: str
        :param _EngineVersion: 引擎版本
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersion: str
        :param _GTMNodes: GTM节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GTMNodes: list of InstanceNodeGroup
        :param _CNNodes: CN节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CNNodes: list of InstanceNodeGroup
        :param _DNNodes: DN节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DNNodes: list of InstanceNodeGroup
        :param _BackupStorage: 备份存储
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStorage: list of InstanceNodeGroup
        :param _FNNodes: FN节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FNNodes: list of InstanceNodeGroup
        """
        self._ID = None
        self._InstanceType = None
        self._InstanceName = None
        self._Status = None
        self._StatusDesc = None
        self._InstanceStateInfo = None
        self._InstanceID = None
        self._CreateTime = None
        self._Region = None
        self._Zone = None
        self._RegionDesc = None
        self._ZoneDesc = None
        self._Tags = None
        self._Version = None
        self._Charset = None
        self._EngineVersion = None
        self._GTMNodes = None
        self._CNNodes = None
        self._DNNodes = None
        self._BackupStorage = None
        self._FNNodes = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def InstanceStateInfo(self):
        return self._InstanceStateInfo

    @InstanceStateInfo.setter
    def InstanceStateInfo(self, InstanceStateInfo):
        self._InstanceStateInfo = InstanceStateInfo

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RegionDesc(self):
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def ZoneDesc(self):
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def GTMNodes(self):
        return self._GTMNodes

    @GTMNodes.setter
    def GTMNodes(self, GTMNodes):
        self._GTMNodes = GTMNodes

    @property
    def CNNodes(self):
        return self._CNNodes

    @CNNodes.setter
    def CNNodes(self, CNNodes):
        self._CNNodes = CNNodes

    @property
    def DNNodes(self):
        return self._DNNodes

    @DNNodes.setter
    def DNNodes(self, DNNodes):
        self._DNNodes = DNNodes

    @property
    def BackupStorage(self):
        return self._BackupStorage

    @BackupStorage.setter
    def BackupStorage(self, BackupStorage):
        self._BackupStorage = BackupStorage

    @property
    def FNNodes(self):
        return self._FNNodes

    @FNNodes.setter
    def FNNodes(self, FNNodes):
        self._FNNodes = FNNodes


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceType = params.get("InstanceType")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        if params.get("InstanceStateInfo") is not None:
            self._InstanceStateInfo = InstanceStateInfo()
            self._InstanceStateInfo._deserialize(params.get("InstanceStateInfo"))
        self._InstanceID = params.get("InstanceID")
        self._CreateTime = params.get("CreateTime")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._RegionDesc = params.get("RegionDesc")
        self._ZoneDesc = params.get("ZoneDesc")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Version = params.get("Version")
        self._Charset = params.get("Charset")
        self._EngineVersion = params.get("EngineVersion")
        if params.get("GTMNodes") is not None:
            self._GTMNodes = []
            for item in params.get("GTMNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._GTMNodes.append(obj)
        if params.get("CNNodes") is not None:
            self._CNNodes = []
            for item in params.get("CNNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._CNNodes.append(obj)
        if params.get("DNNodes") is not None:
            self._DNNodes = []
            for item in params.get("DNNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._DNNodes.append(obj)
        if params.get("BackupStorage") is not None:
            self._BackupStorage = []
            for item in params.get("BackupStorage"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._BackupStorage.append(obj)
        if params.get("FNNodes") is not None:
            self._FNNodes = []
            for item in params.get("FNNodes"):
                obj = InstanceNodeGroup()
                obj._deserialize(item)
                self._FNNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNodeGroup(AbstractModel):
    """集群节点信息

    """


class InstanceSimpleInfoNew(AbstractModel):
    """精简集群信息

    """

    def __init__(self):
        r"""
        :param _ID: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: int
        :param _InstanceId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _Version: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Region: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _RegionId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param _RegionDesc: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionDesc: str
        :param _Zone: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _ZoneId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param _ZoneDesc: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneDesc: str
        :param _VpcId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _CreateTime: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ExpireTime: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _AccessInfo: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessInfo: str
        :param _PayMode: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _RenewFlag: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: bool
        """
        self._ID = None
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._Region = None
        self._RegionId = None
        self._RegionDesc = None
        self._Zone = None
        self._ZoneId = None
        self._ZoneDesc = None
        self._VpcId = None
        self._SubnetId = None
        self._CreateTime = None
        self._ExpireTime = None
        self._AccessInfo = None
        self._PayMode = None
        self._RenewFlag = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionDesc(self):
        return self._RegionDesc

    @RegionDesc.setter
    def RegionDesc(self, RegionDesc):
        self._RegionDesc = RegionDesc

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneDesc(self):
        return self._ZoneDesc

    @ZoneDesc.setter
    def ZoneDesc(self, ZoneDesc):
        self._ZoneDesc = ZoneDesc

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AccessInfo(self):
        return self._AccessInfo

    @AccessInfo.setter
    def AccessInfo(self, AccessInfo):
        self._AccessInfo = AccessInfo

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._RegionDesc = params.get("RegionDesc")
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ZoneDesc = params.get("ZoneDesc")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AccessInfo = params.get("AccessInfo")
        self._PayMode = params.get("PayMode")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStateInfo(AbstractModel):
    """集群状态抽象后的结构体

    """

    def __init__(self):
        r"""
        :param _InstanceState: 集群状态，例如：Serving
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceState: str
        :param _FlowCreateTime: 集群操作创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowCreateTime: str
        :param _FlowName: 集群操作名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowName: str
        :param _FlowProgress: 集群操作进度
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowProgress: int
        :param _InstanceStateDesc: 集群状态描述，例如：运行中
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStateDesc: str
        :param _FlowMsg: 集群流程错误信息，例如：“创建失败，资源不足”
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMsg: str
        :param _ProcessName: 当前步骤的名称，例如：”购买资源中“
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessName: str
        :param _BackupStatus: 集群是否有备份中任务，有为1,无为0
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupStatus: int
        :param _RequestId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        :param _BackupOpenStatus: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOpenStatus: int
        """
        self._InstanceState = None
        self._FlowCreateTime = None
        self._FlowName = None
        self._FlowProgress = None
        self._InstanceStateDesc = None
        self._FlowMsg = None
        self._ProcessName = None
        self._BackupStatus = None
        self._RequestId = None
        self._BackupOpenStatus = None

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def FlowCreateTime(self):
        return self._FlowCreateTime

    @FlowCreateTime.setter
    def FlowCreateTime(self, FlowCreateTime):
        self._FlowCreateTime = FlowCreateTime

    @property
    def FlowName(self):
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def FlowProgress(self):
        return self._FlowProgress

    @FlowProgress.setter
    def FlowProgress(self, FlowProgress):
        self._FlowProgress = FlowProgress

    @property
    def InstanceStateDesc(self):
        return self._InstanceStateDesc

    @InstanceStateDesc.setter
    def InstanceStateDesc(self, InstanceStateDesc):
        self._InstanceStateDesc = InstanceStateDesc

    @property
    def FlowMsg(self):
        return self._FlowMsg

    @FlowMsg.setter
    def FlowMsg(self, FlowMsg):
        self._FlowMsg = FlowMsg

    @property
    def ProcessName(self):
        return self._ProcessName

    @ProcessName.setter
    def ProcessName(self, ProcessName):
        self._ProcessName = ProcessName

    @property
    def BackupStatus(self):
        return self._BackupStatus

    @BackupStatus.setter
    def BackupStatus(self, BackupStatus):
        self._BackupStatus = BackupStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def BackupOpenStatus(self):
        return self._BackupOpenStatus

    @BackupOpenStatus.setter
    def BackupOpenStatus(self, BackupOpenStatus):
        self._BackupOpenStatus = BackupOpenStatus


    def _deserialize(self, params):
        self._InstanceState = params.get("InstanceState")
        self._FlowCreateTime = params.get("FlowCreateTime")
        self._FlowName = params.get("FlowName")
        self._FlowProgress = params.get("FlowProgress")
        self._InstanceStateDesc = params.get("InstanceStateDesc")
        self._FlowMsg = params.get("FlowMsg")
        self._ProcessName = params.get("ProcessName")
        self._BackupStatus = params.get("BackupStatus")
        self._RequestId = params.get("RequestId")
        self._BackupOpenStatus = params.get("BackupOpenStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _InstanceName: 新修改的实例名称
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ResourceSpecNew(AbstractModel):
    """资源规格

    """

    def __init__(self):
        r"""
        :param _SpecName: 资源名称
        :type SpecName: str
        :param _Count: 资源数
        :type Count: int
        :param _DiskSpec: 磁盘信息
        :type DiskSpec: :class:`tencentcloud.cdwpg.v20201230.models.CBSSpec`
        :param _Type: 资源类型，DATA
        :type Type: str
        """
        self._SpecName = None
        self._Count = None
        self._DiskSpec = None
        self._Type = None

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DiskSpec(self):
        return self._DiskSpec

    @DiskSpec.setter
    def DiskSpec(self, DiskSpec):
        self._DiskSpec = DiskSpec

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._Count = params.get("Count")
        if params.get("DiskSpec") is not None:
            self._DiskSpec = CBSSpec()
            self._DiskSpec._deserialize(params.get("DiskSpec"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签描述

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        