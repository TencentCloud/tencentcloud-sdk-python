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
注意：此字段可能返回 null，表示取不到有效值。
        :type OldPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`
        :param NewPodList: 新实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NewPodList: :class:`tencentcloud.tem.v20210701.models.DeployServicePodDetail`
        :param BatchStatus: 当前批次状态："WaitForTimeExceed", "WaitForResume", "Deploying", "Finish", "NotStart"
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchStatus: str
        :param PodNum: 该批次预计旧实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PodNum: int
        :param BatchIndex: 批次id
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchIndex: int
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type PodId: str
        :param PodStatus: pod状态
注意：此字段可能返回 null，表示取不到有效值。
        :type PodStatus: list of str
        :param PodVersion: pod版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PodVersion: str
        :param CreateTime: pod创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Zone: pod所在可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
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
        :param TotalBatchCount: 总分批数
        :type TotalBatchCount: int
        :param BetaBatchNum: beta分批实例数
        :type BetaBatchNum: int
        :param DeployStrategyType: 分批策略：0-全自动，1-全手动，2-beta分批，beta批一定是手动的
        :type DeployStrategyType: int
        :param BatchInterval: 每批暂停间隔
        :type BatchInterval: int
        """
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
        :param ApplicationId: 服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        """
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
        :param Result: 分批发布结果详情
        :type Result: :class:`tencentcloud.tem.v20210701.models.TemDeployApplicationDetailInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Offset: 分页下标
        :type Offset: int
        :param Limit: 单页条数
        :type Limit: int
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 请求id
        :type RequestId: str
        :param PodList: 条目
        :type PodList: list of RunVersionPod
        """
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
        :param ApplicationId: 需要开始下一批次的服务id
        :type ApplicationId: str
        :param EnvironmentId: 环境id
        :type EnvironmentId: str
        """
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
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ApplicationId: 需要回滚的服务id
        :type ApplicationId: str
        :param EnvironmentId: 需要回滚的服务所在环境id
        :type EnvironmentId: str
        """
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
        :param Result: 是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Webshell: shell地址
        :type Webshell: str
        :param PodId: pod的id
        :type PodId: str
        :param Status: 状态
        :type Status: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PodIp: 实例的ip
        :type PodIp: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param DeployVersion: 部署版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployVersion: str
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Status: 当前状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param BetaBatchDetail: beta分批详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BetaBatchDetail: :class:`tencentcloud.tem.v20210701.models.DeployServiceBatchDetail`
        :param OtherBatchDetail: 其他分批详情
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherBatchDetail: list of DeployServiceBatchDetail
        :param OldVersionPodList: 老版本pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OldVersionPodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param CurrentBatchIndex: 当前批次id
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentBatchIndex: int
        :param ErrorMessage: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param CurrentBatchStatus: 当前批次状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentBatchStatus: str
        """
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
        