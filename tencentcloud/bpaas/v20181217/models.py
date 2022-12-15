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
        :param Key: 审批流中表单唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 表单value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: list of str
        :param Name: 表单参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Key = None
        self.Value = None
        self.Name = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproveOpinion(AbstractModel):
    """审批意见

    """

    def __init__(self):
        r"""
        :param Type: 方式 1:输入文字反馈  2:预设选项
        :type Type: int
        :param Content: 审批意见
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of str
        """
        self.Type = None
        self.Content = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproveUser(AbstractModel):
    """审批人

    """

    def __init__(self):
        r"""
        :param Uin: 用户uin
        :type Uin: int
        :param Type: 用户类型 (1:用户  2:用户组)
        :type Type: int
        :param Desc: 用户描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Nick: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nick: str
        :param Scf: 动态获取Scf
注意：此字段可能返回 null，表示取不到有效值。
        :type Scf: :class:`tencentcloud.bpaas.v20181217.models.Scf`
        """
        self.Uin = None
        self.Type = None
        self.Desc = None
        self.Nick = None
        self.Scf = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Type = params.get("Type")
        self.Desc = params.get("Desc")
        self.Nick = params.get("Nick")
        if params.get("Scf") is not None:
            self.Scf = Scf()
            self.Scf._deserialize(params.get("Scf"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBpaasApproveDetailRequest(AbstractModel):
    """GetBpaasApproveDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApproveId: 审批id
        :type ApproveId: int
        """
        self.ApproveId = None


    def _deserialize(self, params):
        self.ApproveId = params.get("ApproveId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBpaasApproveDetailResponse(AbstractModel):
    """GetBpaasApproveDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplyUin: 申请人uin
        :type ApplyUin: int
        :param ApplyOwnUin: 申请人主账号
        :type ApplyOwnUin: int
        :param ApplyUinNick: 申请人昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyUinNick: str
        :param BpaasId: 审批流id
        :type BpaasId: int
        :param BpaasName: 审批流名称
        :type BpaasName: str
        :param ApplicationParams: 申请参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationParams: list of ApplyParam
        :param Reason: 申请原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param CreateTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Status: 申请单状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Nodes: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Nodes: list of StatusNode
        :param ApprovingNodeId: 正在审批的节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApprovingNodeId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplyUin = None
        self.ApplyOwnUin = None
        self.ApplyUinNick = None
        self.BpaasId = None
        self.BpaasName = None
        self.ApplicationParams = None
        self.Reason = None
        self.CreateTime = None
        self.Status = None
        self.Nodes = None
        self.ApprovingNodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplyUin = params.get("ApplyUin")
        self.ApplyOwnUin = params.get("ApplyOwnUin")
        self.ApplyUinNick = params.get("ApplyUinNick")
        self.BpaasId = params.get("BpaasId")
        self.BpaasName = params.get("BpaasName")
        if params.get("ApplicationParams") is not None:
            self.ApplicationParams = []
            for item in params.get("ApplicationParams"):
                obj = ApplyParam()
                obj._deserialize(item)
                self.ApplicationParams.append(obj)
        self.Reason = params.get("Reason")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = StatusNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.ApprovingNodeId = params.get("ApprovingNodeId")
        self.RequestId = params.get("RequestId")


class OutApproveBpaasApplicationRequest(AbstractModel):
    """OutApproveBpaasApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 状态  1:通过  2:拒绝
        :type Status: int
        :param ApproveId: 审批单id
        :type ApproveId: int
        :param Msg: 审批意见
        :type Msg: str
        """
        self.Status = None
        self.ApproveId = None
        self.Msg = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ApproveId = params.get("ApproveId")
        self.Msg = params.get("Msg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutApproveBpaasApplicationResponse(AbstractModel):
    """OutApproveBpaasApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Scf(AbstractModel):
    """云函数SCF

    """

    def __init__(self):
        r"""
        :param ScfRegion: Scf函数地域id
        :type ScfRegion: str
        :param ScfRegionName: Scf函数地域
        :type ScfRegionName: str
        :param ScfName: Scf函数名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfName: str
        :param Params: Scf函数入参
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of ScfParam
        """
        self.ScfRegion = None
        self.ScfRegionName = None
        self.ScfName = None
        self.Params = None


    def _deserialize(self, params):
        self.ScfRegion = params.get("ScfRegion")
        self.ScfRegionName = params.get("ScfRegionName")
        self.ScfName = params.get("ScfName")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = ScfParam()
                obj._deserialize(item)
                self.Params.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScfParam(AbstractModel):
    """Scf函数入参

    """

    def __init__(self):
        r"""
        :param Key: 参数Key
        :type Key: str
        :param Type: 参数类型 1用户输入 2预设参数 3表单参数
        :type Type: int
        :param Values: 参数值
        :type Values: list of str
        :param Name: 参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Key = None
        self.Type = None
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusNode(AbstractModel):
    """状态节点

    """

    def __init__(self):
        r"""
        :param NodeId: 节点id
        :type NodeId: str
        :param NodeName: 节点名称
        :type NodeName: str
        :param NodeType: 节点类型 1:审批节点 2:执行节点 3:条件节点
        :type NodeType: int
        :param NextNode: 下一个节点
        :type NextNode: str
        :param Opinion: 审批意见模型
注意：此字段可能返回 null，表示取不到有效值。
        :type Opinion: :class:`tencentcloud.bpaas.v20181217.models.ApproveOpinion`
        :param ScfName: scf函数名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfName: str
        :param SubStatus: 状态（0：待审批，1：审批通过，2：拒绝，3：scf执行失败，4：scf执行成功）18: 外部审批中
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatus: int
        :param ApprovedUin: 审批节点审批人
注意：此字段可能返回 null，表示取不到有效值。
        :type ApprovedUin: list of int non-negative
        :param CreateTime: 审批时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Msg: 审批意见信息 审批节点:审批人意见  执行节点:scf函数执行日志
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Users: 有权限审批该节点的uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: :class:`tencentcloud.bpaas.v20181217.models.ApproveUser`
        :param IsApprove: 是否有权限审批该节点
注意：此字段可能返回 null，表示取不到有效值。
        :type IsApprove: bool
        :param ApproveId: 审批id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveId: str
        :param ApproveMethod: 审批方式 0或签 1会签
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMethod: int
        :param ApproveType: 审批节点审批类型，1人工审批 2自动通过 3自动决绝 4外部审批scf
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveType: int
        :param CallMethod: 外部审批类型 scf:0或null ; CKafka:1
注意：此字段可能返回 null，表示取不到有效值。
        :type CallMethod: int
        :param DataHubId: CKafka - 接入资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DataHubId: str
        :param TaskName: CKafka - 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        :param CKafkaRegion: CKafka - 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type CKafkaRegion: str
        :param ExternalUrl: 外部审批Url
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalUrl: str
        """
        self.NodeId = None
        self.NodeName = None
        self.NodeType = None
        self.NextNode = None
        self.Opinion = None
        self.ScfName = None
        self.SubStatus = None
        self.ApprovedUin = None
        self.CreateTime = None
        self.Msg = None
        self.Users = None
        self.IsApprove = None
        self.ApproveId = None
        self.ApproveMethod = None
        self.ApproveType = None
        self.CallMethod = None
        self.DataHubId = None
        self.TaskName = None
        self.CKafkaRegion = None
        self.ExternalUrl = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        self.NodeType = params.get("NodeType")
        self.NextNode = params.get("NextNode")
        if params.get("Opinion") is not None:
            self.Opinion = ApproveOpinion()
            self.Opinion._deserialize(params.get("Opinion"))
        self.ScfName = params.get("ScfName")
        self.SubStatus = params.get("SubStatus")
        self.ApprovedUin = params.get("ApprovedUin")
        self.CreateTime = params.get("CreateTime")
        self.Msg = params.get("Msg")
        if params.get("Users") is not None:
            self.Users = ApproveUser()
            self.Users._deserialize(params.get("Users"))
        self.IsApprove = params.get("IsApprove")
        self.ApproveId = params.get("ApproveId")
        self.ApproveMethod = params.get("ApproveMethod")
        self.ApproveType = params.get("ApproveType")
        self.CallMethod = params.get("CallMethod")
        self.DataHubId = params.get("DataHubId")
        self.TaskName = params.get("TaskName")
        self.CKafkaRegion = params.get("CKafkaRegion")
        self.ExternalUrl = params.get("ExternalUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        