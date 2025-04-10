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


class ApplyParam(AbstractModel):
    """bpaas申请入参

    """

    def __init__(self):
        r"""
        :param _Key: 审批流中表单唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 表单value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        :param _Name: 表单参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Key = None
        self._Value = None
        self._Name = None

    @property
    def Key(self):
        """审批流中表单唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """表单value
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        """表单参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproveOpinion(AbstractModel):
    """审批意见

    """

    def __init__(self):
        r"""
        :param _Type: 方式 1:输入文字反馈  2:预设选项
        :type Type: int
        :param _Content: 审批意见
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of str
        """
        self._Type = None
        self._Content = None

    @property
    def Type(self):
        """方式 1:输入文字反馈  2:预设选项
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Content(self):
        """审批意见
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproveUser(AbstractModel):
    """审批人

    """

    def __init__(self):
        r"""
        :param _Uin: 用户uin
        :type Uin: int
        :param _Type: 用户类型 (1:用户  2:用户组)
        :type Type: int
        :param _Desc: 用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param _Scf: 动态获取Scf
注意：此字段可能返回 null，表示取不到有效值。
        :type Scf: :class:`tencentcloud.bpaas.v20181217.models.Scf`
        :param _ApproveStatus: 审批状态 （取值范围 0:待审批  1:审批通过  2:拒绝  6:其他人已审批）
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveStatus: int
        :param _ApproveMsg: 审批意见
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMsg: str
        :param _ApproveTime: 审批时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveTime: str
        :param _ApproveGroup: 审批组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveGroup: str
        """
        self._Uin = None
        self._Type = None
        self._Desc = None
        self._Nick = None
        self._Scf = None
        self._ApproveStatus = None
        self._ApproveMsg = None
        self._ApproveTime = None
        self._ApproveGroup = None

    @property
    def Uin(self):
        """用户uin
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Type(self):
        """用户类型 (1:用户  2:用户组)
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Desc(self):
        """用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Nick(self):
        """用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def Scf(self):
        """动态获取Scf
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bpaas.v20181217.models.Scf`
        """
        return self._Scf

    @Scf.setter
    def Scf(self, Scf):
        self._Scf = Scf

    @property
    def ApproveStatus(self):
        """审批状态 （取值范围 0:待审批  1:审批通过  2:拒绝  6:其他人已审批）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ApproveStatus

    @ApproveStatus.setter
    def ApproveStatus(self, ApproveStatus):
        self._ApproveStatus = ApproveStatus

    @property
    def ApproveMsg(self):
        """审批意见
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveMsg

    @ApproveMsg.setter
    def ApproveMsg(self, ApproveMsg):
        self._ApproveMsg = ApproveMsg

    @property
    def ApproveTime(self):
        """审批时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveTime

    @ApproveTime.setter
    def ApproveTime(self, ApproveTime):
        self._ApproveTime = ApproveTime

    @property
    def ApproveGroup(self):
        """审批组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApproveGroup

    @ApproveGroup.setter
    def ApproveGroup(self, ApproveGroup):
        self._ApproveGroup = ApproveGroup


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Type = params.get("Type")
        self._Desc = params.get("Desc")
        self._Nick = params.get("Nick")
        if params.get("Scf") is not None:
            self._Scf = Scf()
            self._Scf._deserialize(params.get("Scf"))
        self._ApproveStatus = params.get("ApproveStatus")
        self._ApproveMsg = params.get("ApproveMsg")
        self._ApproveTime = params.get("ApproveTime")
        self._ApproveGroup = params.get("ApproveGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBpaasApproveDetailRequest(AbstractModel):
    """GetBpaasApproveDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApproveId: 审批id
        :type ApproveId: int
        """
        self._ApproveId = None

    @property
    def ApproveId(self):
        """审批id
        :rtype: int
        """
        return self._ApproveId

    @ApproveId.setter
    def ApproveId(self, ApproveId):
        self._ApproveId = ApproveId


    def _deserialize(self, params):
        self._ApproveId = params.get("ApproveId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBpaasApproveDetailResponse(AbstractModel):
    """GetBpaasApproveDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyUin: 申请人uin
        :type ApplyUin: int
        :param _ApplyOwnUin: 申请人主账号
        :type ApplyOwnUin: int
        :param _ApplyUinNick: 申请人昵称
        :type ApplyUinNick: str
        :param _BpaasId: 审批流id
        :type BpaasId: int
        :param _BpaasName: 审批流名称
        :type BpaasName: str
        :param _ApplicationParams: 申请参数
        :type ApplicationParams: list of ApplyParam
        :param _Reason: 申请原因
        :type Reason: str
        :param _CreateTime: 申请时间
        :type CreateTime: str
        :param _Status: 申请单状态
        :type Status: int
        :param _Nodes: 节点信息
        :type Nodes: list of StatusNode
        :param _ApprovingNodeId: 正在审批的节点id
        :type ApprovingNodeId: str
        :param _ModifyTime: 更新时间，时间格式：2021-12-12 10:12:10	
        :type ModifyTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplyUin = None
        self._ApplyOwnUin = None
        self._ApplyUinNick = None
        self._BpaasId = None
        self._BpaasName = None
        self._ApplicationParams = None
        self._Reason = None
        self._CreateTime = None
        self._Status = None
        self._Nodes = None
        self._ApprovingNodeId = None
        self._ModifyTime = None
        self._RequestId = None

    @property
    def ApplyUin(self):
        """申请人uin
        :rtype: int
        """
        return self._ApplyUin

    @ApplyUin.setter
    def ApplyUin(self, ApplyUin):
        self._ApplyUin = ApplyUin

    @property
    def ApplyOwnUin(self):
        """申请人主账号
        :rtype: int
        """
        return self._ApplyOwnUin

    @ApplyOwnUin.setter
    def ApplyOwnUin(self, ApplyOwnUin):
        self._ApplyOwnUin = ApplyOwnUin

    @property
    def ApplyUinNick(self):
        """申请人昵称
        :rtype: str
        """
        return self._ApplyUinNick

    @ApplyUinNick.setter
    def ApplyUinNick(self, ApplyUinNick):
        self._ApplyUinNick = ApplyUinNick

    @property
    def BpaasId(self):
        """审批流id
        :rtype: int
        """
        return self._BpaasId

    @BpaasId.setter
    def BpaasId(self, BpaasId):
        self._BpaasId = BpaasId

    @property
    def BpaasName(self):
        """审批流名称
        :rtype: str
        """
        return self._BpaasName

    @BpaasName.setter
    def BpaasName(self, BpaasName):
        self._BpaasName = BpaasName

    @property
    def ApplicationParams(self):
        """申请参数
        :rtype: list of ApplyParam
        """
        return self._ApplicationParams

    @ApplicationParams.setter
    def ApplicationParams(self, ApplicationParams):
        self._ApplicationParams = ApplicationParams

    @property
    def Reason(self):
        """申请原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def CreateTime(self):
        """申请时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        """申请单状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Nodes(self):
        """节点信息
        :rtype: list of StatusNode
        """
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def ApprovingNodeId(self):
        """正在审批的节点id
        :rtype: str
        """
        return self._ApprovingNodeId

    @ApprovingNodeId.setter
    def ApprovingNodeId(self, ApprovingNodeId):
        self._ApprovingNodeId = ApprovingNodeId

    @property
    def ModifyTime(self):
        """更新时间，时间格式：2021-12-12 10:12:10	
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
        self._ApplyUin = params.get("ApplyUin")
        self._ApplyOwnUin = params.get("ApplyOwnUin")
        self._ApplyUinNick = params.get("ApplyUinNick")
        self._BpaasId = params.get("BpaasId")
        self._BpaasName = params.get("BpaasName")
        if params.get("ApplicationParams") is not None:
            self._ApplicationParams = []
            for item in params.get("ApplicationParams"):
                obj = ApplyParam()
                obj._deserialize(item)
                self._ApplicationParams.append(obj)
        self._Reason = params.get("Reason")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = StatusNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._ApprovingNodeId = params.get("ApprovingNodeId")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestId = params.get("RequestId")


class OutApproveBpaasApplicationRequest(AbstractModel):
    """OutApproveBpaasApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态  1:通过  2:拒绝
        :type Status: int
        :param _ApproveId: 审批单id
        :type ApproveId: int
        :param _Msg: 审批意见
        :type Msg: str
        """
        self._Status = None
        self._ApproveId = None
        self._Msg = None

    @property
    def Status(self):
        """状态  1:通过  2:拒绝
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApproveId(self):
        """审批单id
        :rtype: int
        """
        return self._ApproveId

    @ApproveId.setter
    def ApproveId(self, ApproveId):
        self._ApproveId = ApproveId

    @property
    def Msg(self):
        """审批意见
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ApproveId = params.get("ApproveId")
        self._Msg = params.get("Msg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutApproveBpaasApplicationResponse(AbstractModel):
    """OutApproveBpaasApplication返回参数结构体

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


class Scf(AbstractModel):
    """云函数SCF

    """

    def __init__(self):
        r"""
        :param _ScfRegion: Scf函数地域id
        :type ScfRegion: str
        :param _ScfRegionName: Scf函数地域
        :type ScfRegionName: str
        :param _ScfName: Scf函数名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfName: str
        :param _Params: Scf函数入参
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of ScfParam
        """
        self._ScfRegion = None
        self._ScfRegionName = None
        self._ScfName = None
        self._Params = None

    @property
    def ScfRegion(self):
        """Scf函数地域id
        :rtype: str
        """
        return self._ScfRegion

    @ScfRegion.setter
    def ScfRegion(self, ScfRegion):
        self._ScfRegion = ScfRegion

    @property
    def ScfRegionName(self):
        """Scf函数地域
        :rtype: str
        """
        return self._ScfRegionName

    @ScfRegionName.setter
    def ScfRegionName(self, ScfRegionName):
        self._ScfRegionName = ScfRegionName

    @property
    def ScfName(self):
        """Scf函数名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScfName

    @ScfName.setter
    def ScfName(self, ScfName):
        self._ScfName = ScfName

    @property
    def Params(self):
        """Scf函数入参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScfParam
        """
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._ScfRegion = params.get("ScfRegion")
        self._ScfRegionName = params.get("ScfRegionName")
        self._ScfName = params.get("ScfName")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = ScfParam()
                obj._deserialize(item)
                self._Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScfParam(AbstractModel):
    """Scf函数入参

    """

    def __init__(self):
        r"""
        :param _Key: 参数Key
        :type Key: str
        :param _Type: 参数类型 1用户输入 2预设参数 3表单参数
        :type Type: int
        :param _Values: 参数值
        :type Values: list of str
        :param _Name: 参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Key = None
        self._Type = None
        self._Values = None
        self._Name = None

    @property
    def Key(self):
        """参数Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        """参数类型 1用户输入 2预设参数 3表单参数
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
        """参数值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        """参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusNode(AbstractModel):
    """状态节点

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点id
        :type NodeId: str
        :param _NodeName: 节点名称
        :type NodeName: str
        :param _NodeType: 节点类型 1:审批节点 2:执行节点 3:条件节点
        :type NodeType: int
        :param _NextNode: 下一个节点
        :type NextNode: str
        :param _Opinion: 审批意见模型
        :type Opinion: :class:`tencentcloud.bpaas.v20181217.models.ApproveOpinion`
        :param _ScfName: scf函数名称
        :type ScfName: str
        :param _SubStatus: 状态（0：待审批，1：审批通过，2：拒绝，3：scf执行失败，4：scf执行成功）18: 外部审批中
        :type SubStatus: int
        :param _ApprovedUin: 审批节点审批人
        :type ApprovedUin: list of int non-negative
        :param _CreateTime: 审批时间
        :type CreateTime: str
        :param _Msg: 审批意见信息 审批节点:审批人意见  执行节点:scf函数执行日志
        :type Msg: str
        :param _Users: 有权限审批该节点的uin
        :type Users: :class:`tencentcloud.bpaas.v20181217.models.ApproveUser`
        :param _IsApprove: 是否有权限审批该节点
        :type IsApprove: bool
        :param _ApproveId: 审批id
        :type ApproveId: str
        :param _ApproveMethod: 审批方式 0或签 1会签
        :type ApproveMethod: int
        :param _ApproveType: 审批节点审批类型，1人工审批 2自动通过 3自动决绝 4外部审批scf
        :type ApproveType: int
        :param _CallMethod: 外部审批类型 scf:0或null ; CKafka:1
        :type CallMethod: int
        :param _DataHubId: CKafka - 接入资源ID
        :type DataHubId: str
        :param _TaskName: CKafka - 任务名称
        :type TaskName: str
        :param _CKafkaRegion: CKafka - 地域
        :type CKafkaRegion: str
        :param _ExternalUrl: 外部审批Url
        :type ExternalUrl: str
        :param _ParallelNodes: 并行节点 3-4
        :type ParallelNodes: str
        :param _RejectedCloudFunctionMsg: scf拒绝时返回信息
        :type RejectedCloudFunctionMsg: str
        :param _PrevNode: 上一个节点
        :type PrevNode: str
        """
        self._NodeId = None
        self._NodeName = None
        self._NodeType = None
        self._NextNode = None
        self._Opinion = None
        self._ScfName = None
        self._SubStatus = None
        self._ApprovedUin = None
        self._CreateTime = None
        self._Msg = None
        self._Users = None
        self._IsApprove = None
        self._ApproveId = None
        self._ApproveMethod = None
        self._ApproveType = None
        self._CallMethod = None
        self._DataHubId = None
        self._TaskName = None
        self._CKafkaRegion = None
        self._ExternalUrl = None
        self._ParallelNodes = None
        self._RejectedCloudFunctionMsg = None
        self._PrevNode = None

    @property
    def NodeId(self):
        """节点id
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        """节点名称
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def NodeType(self):
        """节点类型 1:审批节点 2:执行节点 3:条件节点
        :rtype: int
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def NextNode(self):
        """下一个节点
        :rtype: str
        """
        return self._NextNode

    @NextNode.setter
    def NextNode(self, NextNode):
        self._NextNode = NextNode

    @property
    def Opinion(self):
        """审批意见模型
        :rtype: :class:`tencentcloud.bpaas.v20181217.models.ApproveOpinion`
        """
        return self._Opinion

    @Opinion.setter
    def Opinion(self, Opinion):
        self._Opinion = Opinion

    @property
    def ScfName(self):
        """scf函数名称
        :rtype: str
        """
        return self._ScfName

    @ScfName.setter
    def ScfName(self, ScfName):
        self._ScfName = ScfName

    @property
    def SubStatus(self):
        """状态（0：待审批，1：审批通过，2：拒绝，3：scf执行失败，4：scf执行成功）18: 外部审批中
        :rtype: int
        """
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def ApprovedUin(self):
        """审批节点审批人
        :rtype: list of int non-negative
        """
        return self._ApprovedUin

    @ApprovedUin.setter
    def ApprovedUin(self, ApprovedUin):
        self._ApprovedUin = ApprovedUin

    @property
    def CreateTime(self):
        """审批时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Msg(self):
        """审批意见信息 审批节点:审批人意见  执行节点:scf函数执行日志
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Users(self):
        """有权限审批该节点的uin
        :rtype: :class:`tencentcloud.bpaas.v20181217.models.ApproveUser`
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def IsApprove(self):
        """是否有权限审批该节点
        :rtype: bool
        """
        return self._IsApprove

    @IsApprove.setter
    def IsApprove(self, IsApprove):
        self._IsApprove = IsApprove

    @property
    def ApproveId(self):
        """审批id
        :rtype: str
        """
        return self._ApproveId

    @ApproveId.setter
    def ApproveId(self, ApproveId):
        self._ApproveId = ApproveId

    @property
    def ApproveMethod(self):
        """审批方式 0或签 1会签
        :rtype: int
        """
        return self._ApproveMethod

    @ApproveMethod.setter
    def ApproveMethod(self, ApproveMethod):
        self._ApproveMethod = ApproveMethod

    @property
    def ApproveType(self):
        """审批节点审批类型，1人工审批 2自动通过 3自动决绝 4外部审批scf
        :rtype: int
        """
        return self._ApproveType

    @ApproveType.setter
    def ApproveType(self, ApproveType):
        self._ApproveType = ApproveType

    @property
    def CallMethod(self):
        """外部审批类型 scf:0或null ; CKafka:1
        :rtype: int
        """
        return self._CallMethod

    @CallMethod.setter
    def CallMethod(self, CallMethod):
        self._CallMethod = CallMethod

    @property
    def DataHubId(self):
        """CKafka - 接入资源ID
        :rtype: str
        """
        return self._DataHubId

    @DataHubId.setter
    def DataHubId(self, DataHubId):
        self._DataHubId = DataHubId

    @property
    def TaskName(self):
        """CKafka - 任务名称
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def CKafkaRegion(self):
        """CKafka - 地域
        :rtype: str
        """
        return self._CKafkaRegion

    @CKafkaRegion.setter
    def CKafkaRegion(self, CKafkaRegion):
        self._CKafkaRegion = CKafkaRegion

    @property
    def ExternalUrl(self):
        """外部审批Url
        :rtype: str
        """
        return self._ExternalUrl

    @ExternalUrl.setter
    def ExternalUrl(self, ExternalUrl):
        self._ExternalUrl = ExternalUrl

    @property
    def ParallelNodes(self):
        """并行节点 3-4
        :rtype: str
        """
        return self._ParallelNodes

    @ParallelNodes.setter
    def ParallelNodes(self, ParallelNodes):
        self._ParallelNodes = ParallelNodes

    @property
    def RejectedCloudFunctionMsg(self):
        """scf拒绝时返回信息
        :rtype: str
        """
        return self._RejectedCloudFunctionMsg

    @RejectedCloudFunctionMsg.setter
    def RejectedCloudFunctionMsg(self, RejectedCloudFunctionMsg):
        self._RejectedCloudFunctionMsg = RejectedCloudFunctionMsg

    @property
    def PrevNode(self):
        """上一个节点
        :rtype: str
        """
        return self._PrevNode

    @PrevNode.setter
    def PrevNode(self, PrevNode):
        self._PrevNode = PrevNode


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        self._NodeType = params.get("NodeType")
        self._NextNode = params.get("NextNode")
        if params.get("Opinion") is not None:
            self._Opinion = ApproveOpinion()
            self._Opinion._deserialize(params.get("Opinion"))
        self._ScfName = params.get("ScfName")
        self._SubStatus = params.get("SubStatus")
        self._ApprovedUin = params.get("ApprovedUin")
        self._CreateTime = params.get("CreateTime")
        self._Msg = params.get("Msg")
        if params.get("Users") is not None:
            self._Users = ApproveUser()
            self._Users._deserialize(params.get("Users"))
        self._IsApprove = params.get("IsApprove")
        self._ApproveId = params.get("ApproveId")
        self._ApproveMethod = params.get("ApproveMethod")
        self._ApproveType = params.get("ApproveType")
        self._CallMethod = params.get("CallMethod")
        self._DataHubId = params.get("DataHubId")
        self._TaskName = params.get("TaskName")
        self._CKafkaRegion = params.get("CKafkaRegion")
        self._ExternalUrl = params.get("ExternalUrl")
        self._ParallelNodes = params.get("ParallelNodes")
        self._RejectedCloudFunctionMsg = params.get("RejectedCloudFunctionMsg")
        self._PrevNode = params.get("PrevNode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        