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


class DeployServiceBatchDetail(AbstractModel):
    """分批发布单批次详情

    """

    def __init__(self):
        """
        :param OldPodList: 旧实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type OldPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`\n        :param NewPodList: 新实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type NewPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`\n        :param BatchStatus: 当前批次状态："WaitForTimeExceed", "WaitForResume", "Deploying", "Finish", "NotStart"
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchStatus: str\n        :param PodNum: 该批次预计旧实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodNum: int\n        :param BatchIndex: 批次id
注意：此字段可能返回 null，表示取不到有效值。\n        :type BatchIndex: int\n        """
        self.OldPodList = None
        self.NewPodList = None
        self.BatchStatus = None
        self.PodNum = None
        self.BatchIndex = None


    def _deserialize(self, params):
        if params.get("OldPodList") is not None:
            self.OldPodList = DeployServicePodDetail()
            self.OldPodList._deserialize(params.get("OldPodList"))
        if params.get("NewPodList") is not None:
            self.NewPodList = DeployServicePodDetail()
            self.NewPodList._deserialize(params.get("NewPodList"))
        self.BatchStatus = params.get("BatchStatus")
        self.PodNum = params.get("PodNum")
        self.BatchIndex = params.get("BatchIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServicePodDetail(AbstractModel):
    """分批发布单批次详情

    """

    def __init__(self):
        """
        :param PodId: pod Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodId: str\n        :param PodStatus: pod状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodStatus: list of str\n        :param PodVersion: pod版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodVersion: str\n        :param CreateTime: pod创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Zone: pod所在可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Zone: str\n        """
        self.PodId = None
        self.PodStatus = None
        self.PodVersion = None
        self.CreateTime = None
        self.Zone = None


    def _deserialize(self, params):
        self.PodId = params.get("PodId")
        self.PodStatus = params.get("PodStatus")
        self.PodVersion = params.get("PodVersion")
        self.CreateTime = params.get("CreateTime")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployStrategyConf(AbstractModel):
    """分批发布策略配置

    """

    def __init__(self):
        """
        :param TotalBatchCount: 总分批数\n        :type TotalBatchCount: int\n        :param BetaBatchNum: beta分批实例数\n        :type BetaBatchNum: int\n        :param DeployStrategyType: 分批策略：0-全自动，1-全手动，2-beta分批，beta批一定是手动的\n        :type DeployStrategyType: int\n        :param BatchInterval: 每批暂停间隔\n        :type BatchInterval: int\n        """
        self.TotalBatchCount = None
        self.BetaBatchNum = None
        self.DeployStrategyType = None
        self.BatchInterval = None


    def _deserialize(self, params):
        self.TotalBatchCount = params.get("TotalBatchCount")
        self.BetaBatchNum = params.get("BetaBatchNum")
        self.DeployStrategyType = params.get("DeployStrategyType")
        self.BatchInterval = params.get("BatchInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployApplicationDetailRequest(AbstractModel):
    """DescribeDeployApplicationDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 服务id\n        :type ApplicationId: str\n        :param EnvironmentId: 环境id\n        :type EnvironmentId: str\n        """
        self.ApplicationId = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployApplicationDetailResponse(AbstractModel):
    """DescribeDeployApplicationDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 分批发布结果详情\n        :type Result: :class:`tencentcloud.tem.v20210701.models.TemDeployApplicationDetailInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TemDeployApplicationDetailInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRunPodPage(AbstractModel):
    """版本pod列表

    """

    def __init__(self):
        """
        :param Offset: 分页下标\n        :type Offset: int\n        :param Limit: 单页条数\n        :type Limit: int\n        :param TotalCount: 总数\n        :type TotalCount: int\n        :param RequestId: 请求id\n        :type RequestId: str\n        :param PodList: 条目\n        :type PodList: list of RunVersionPod\n        """
        self.Offset = None
        self.Limit = None
        self.TotalCount = None
        self.RequestId = None
        self.PodList = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        if params.get("PodList") is not None:
            self.PodList = []
            for item in params.get("PodList"):
                obj = RunVersionPod()
                obj._deserialize(item)
                self.PodList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeDeployApplicationRequest(AbstractModel):
    """ResumeDeployApplication请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 需要开始下一批次的服务id\n        :type ApplicationId: str\n        :param EnvironmentId: 环境id\n        :type EnvironmentId: str\n        """
        self.ApplicationId = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeDeployApplicationResponse(AbstractModel):
    """ResumeDeployApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RevertDeployApplicationRequest(AbstractModel):
    """RevertDeployApplication请求参数结构体

    """

    def __init__(self):
        """
        :param ApplicationId: 需要回滚的服务id\n        :type ApplicationId: str\n        :param EnvironmentId: 需要回滚的服务所在环境id\n        :type EnvironmentId: str\n        """
        self.ApplicationId = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevertDeployApplicationResponse(AbstractModel):
    """RevertDeployApplication返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """版本pod

    """

    def __init__(self):
        """
        :param Webshell: shell地址\n        :type Webshell: str\n        :param PodId: pod的id\n        :type PodId: str\n        :param Status: 状态\n        :type Status: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param PodIp: 实例的ip\n        :type PodIp: str\n        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Zone: str\n        :param DeployVersion: 部署版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployVersion: str\n        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。\n        :type RestartCount: int\n        """
        self.Webshell = None
        self.PodId = None
        self.Status = None
        self.CreateTime = None
        self.PodIp = None
        self.Zone = None
        self.DeployVersion = None
        self.RestartCount = None


    def _deserialize(self, params):
        self.Webshell = params.get("Webshell")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.PodIp = params.get("PodIp")
        self.Zone = params.get("Zone")
        self.DeployVersion = params.get("DeployVersion")
        self.RestartCount = params.get("RestartCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemDeployApplicationDetailInfo(AbstractModel):
    """分批发布详情

    """

    def __init__(self):
        """
        :param DeployStrategyConf: 分批发布策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`\n        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTime: str\n        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        :param Status: 当前状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param BetaBatchDetail: beta分批详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type BetaBatchDetail: :class:`tencentcloud.tem.v20210701.models.DeployServiceBatchDetail`\n        :param OtherBatchDetail: 其他分批详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type OtherBatchDetail: list of DeployServiceBatchDetail\n        :param OldVersionPodList: 老版本pod列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type OldVersionPodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`\n        :param CurrentBatchIndex: 当前批次id
注意：此字段可能返回 null，表示取不到有效值。\n        :type CurrentBatchIndex: int\n        :param ErrorMessage: 错误原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMessage: str\n        :param CurrentBatchStatus: 当前批次状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type CurrentBatchStatus: str\n        """
        self.DeployStrategyConf = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.BetaBatchDetail = None
        self.OtherBatchDetail = None
        self.OldVersionPodList = None
        self.CurrentBatchIndex = None
        self.ErrorMessage = None
        self.CurrentBatchStatus = None


    def _deserialize(self, params):
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("BetaBatchDetail") is not None:
            self.BetaBatchDetail = DeployServiceBatchDetail()
            self.BetaBatchDetail._deserialize(params.get("BetaBatchDetail"))
        if params.get("OtherBatchDetail") is not None:
            self.OtherBatchDetail = []
            for item in params.get("OtherBatchDetail"):
                obj = DeployServiceBatchDetail()
                obj._deserialize(item)
                self.OtherBatchDetail.append(obj)
        if params.get("OldVersionPodList") is not None:
            self.OldVersionPodList = DescribeRunPodPage()
            self.OldVersionPodList._deserialize(params.get("OldVersionPodList"))
        self.CurrentBatchIndex = params.get("CurrentBatchIndex")
        self.ErrorMessage = params.get("ErrorMessage")
        self.CurrentBatchStatus = params.get("CurrentBatchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        