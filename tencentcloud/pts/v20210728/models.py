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


class AbortCronJobsRequest(AbstractModel):
    """AbortCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        """
        self._ProjectId = None
        self._CronJobIds = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CronJobIds(self):
        return self._CronJobIds

    @CronJobIds.setter
    def CronJobIds(self, CronJobIds):
        self._CronJobIds = CronJobIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CronJobIds = params.get("CronJobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortCronJobsResponse(AbstractModel):
    """AbortCronJobs返回参数结构体

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


class AbortJobRequest(AbstractModel):
    """AbortJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 待停止的压测任务的 ID（所有的压测任务 ID 可以从 DescribeJobs 接口获取）
        :type JobId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _AbortReason: 中断原因
        :type AbortReason: int
        """
        self._JobId = None
        self._ProjectId = None
        self._ScenarioId = None
        self._AbortReason = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def AbortReason(self):
        return self._AbortReason

    @AbortReason.setter
    def AbortReason(self, AbortReason):
        self._AbortReason = AbortReason


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        self._AbortReason = params.get("AbortReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbortJobResponse(AbstractModel):
    """AbortJob返回参数结构体

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


class AdjustJobSpeedRequest(AbstractModel):
    """AdjustJobSpeed请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _TargetRequestsPerSecond: 目标 RPS。其取值应大于起始 RPS，并且小于最大 RPS
        :type TargetRequestsPerSecond: int
        """
        self._JobId = None
        self._TargetRequestsPerSecond = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TargetRequestsPerSecond(self):
        return self._TargetRequestsPerSecond

    @TargetRequestsPerSecond.setter
    def TargetRequestsPerSecond(self, TargetRequestsPerSecond):
        self._TargetRequestsPerSecond = TargetRequestsPerSecond


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TargetRequestsPerSecond = params.get("TargetRequestsPerSecond")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdjustJobSpeedResponse(AbstractModel):
    """AdjustJobSpeed返回参数结构体

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


class AggregationLegend(AbstractModel):
    """聚合函数

    """

    def __init__(self):
        r"""
        :param _Aggregation: 指标支持的聚合函数
        :type Aggregation: str
        :param _Legend: 聚合函数作用于指标后对应的描述
        :type Legend: str
        :param _Unit: 聚合之后的指标单位
        :type Unit: str
        """
        self._Aggregation = None
        self._Legend = None
        self._Unit = None

    @property
    def Aggregation(self):
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

    @property
    def Legend(self):
        return self._Legend

    @Legend.setter
    def Legend(self, Legend):
        self._Legend = Legend

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit


    def _deserialize(self, params):
        self._Aggregation = params.get("Aggregation")
        self._Legend = params.get("Legend")
        self._Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertChannel(AbstractModel):
    """告警通知渠道

    """

    def __init__(self):
        r"""
        :param _NoticeId: 通知模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeId: str
        :param _AMPConsumerId: AMP consumer ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AMPConsumerId: str
        """
        self._NoticeId = None
        self._AMPConsumerId = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def AMPConsumerId(self):
        return self._AMPConsumerId

    @AMPConsumerId.setter
    def AMPConsumerId(self, AMPConsumerId):
        self._AMPConsumerId = AMPConsumerId


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._AMPConsumerId = params.get("AMPConsumerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertChannelRecord(AbstractModel):
    """告警通知接收组

    """

    def __init__(self):
        r"""
        :param _NoticeId: Notice ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeId: str
        :param _AMPConsumerId: Consumer ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AMPConsumerId: str
        :param _ProjectId: 项目 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _AppId: App ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubAccountUin: 子账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        """
        self._NoticeId = None
        self._AMPConsumerId = None
        self._ProjectId = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._AppId = None
        self._Uin = None
        self._SubAccountUin = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def AMPConsumerId(self):
        return self._AMPConsumerId

    @AMPConsumerId.setter
    def AMPConsumerId(self, AMPConsumerId):
        self._AMPConsumerId = AMPConsumerId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._AMPConsumerId = params.get("AMPConsumerId")
        self._ProjectId = params.get("ProjectId")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertRecord(AbstractModel):
    """告警历史记录项

    """

    def __init__(self):
        r"""
        :param _AlertRecordId: 告警历史记录项 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRecordId: str
        :param _ProjectId: 项目 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _ScenarioId: 场景 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioId: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.pts.v20210728.models.AlertRecordStatus`
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _JobId: 任务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _AppId: App ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubAccountUin: 子账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _ScenarioName: 场景名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioName: str
        :param _Target: 告警对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Target: str
        :param _JobSLAId: 告警规则 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobSLAId: str
        :param _JobSLADescription: 告警规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type JobSLADescription: str
        """
        self._AlertRecordId = None
        self._ProjectId = None
        self._ScenarioId = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._JobId = None
        self._AppId = None
        self._Uin = None
        self._SubAccountUin = None
        self._ScenarioName = None
        self._Target = None
        self._JobSLAId = None
        self._JobSLADescription = None

    @property
    def AlertRecordId(self):
        return self._AlertRecordId

    @AlertRecordId.setter
    def AlertRecordId(self, AlertRecordId):
        self._AlertRecordId = AlertRecordId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def ScenarioName(self):
        return self._ScenarioName

    @ScenarioName.setter
    def ScenarioName(self, ScenarioName):
        self._ScenarioName = ScenarioName

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def JobSLAId(self):
        return self._JobSLAId

    @JobSLAId.setter
    def JobSLAId(self, JobSLAId):
        self._JobSLAId = JobSLAId

    @property
    def JobSLADescription(self):
        return self._JobSLADescription

    @JobSLADescription.setter
    def JobSLADescription(self, JobSLADescription):
        self._JobSLADescription = JobSLADescription


    def _deserialize(self, params):
        self._AlertRecordId = params.get("AlertRecordId")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        if params.get("Status") is not None:
            self._Status = AlertRecordStatus()
            self._Status._deserialize(params.get("Status"))
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._JobId = params.get("JobId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._ScenarioName = params.get("ScenarioName")
        self._Target = params.get("Target")
        self._JobSLAId = params.get("JobSLAId")
        self._JobSLADescription = params.get("JobSLADescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AlertRecordStatus(AbstractModel):
    """告警历史项的状态

    """

    def __init__(self):
        r"""
        :param _AbortJob: 停止压测任务成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type AbortJob: int
        :param _SendNotice: 发送告警通知成功与否
注意：此字段可能返回 null，表示取不到有效值。
        :type SendNotice: int
        """
        self._AbortJob = None
        self._SendNotice = None

    @property
    def AbortJob(self):
        return self._AbortJob

    @AbortJob.setter
    def AbortJob(self, AbortJob):
        self._AbortJob = AbortJob

    @property
    def SendNotice(self):
        return self._SendNotice

    @SendNotice.setter
    def SendNotice(self, SendNotice):
        self._SendNotice = SendNotice


    def _deserialize(self, params):
        self._AbortJob = params.get("AbortJob")
        self._SendNotice = params.get("SendNotice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Attributes(AbstractModel):
    """采样日志附带属性

    """

    def __init__(self):
        r"""
        :param _Status: 采用请求返回码
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Result: 采样请求结果码
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _Service: 采样请求API
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _Method: 采样请求调用方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _Duration: 采样请求延时时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        """
        self._Status = None
        self._Result = None
        self._Service = None
        self._Method = None
        self._Duration = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._Service = params.get("Service")
        self._Method = params.get("Method")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckSummary(AbstractModel):
    """检查点汇总结果

    """

    def __init__(self):
        r"""
        :param _Name: 检查点名字
        :type Name: str
        :param _Step: 检查点所在步骤名字
        :type Step: str
        :param _SuccessCount: 检查点成功次数
        :type SuccessCount: int
        :param _FailCount: 检查失败次数
        :type FailCount: int
        :param _ErrorRate: 错误比例
        :type ErrorRate: float
        """
        self._Name = None
        self._Step = None
        self._SuccessCount = None
        self._FailCount = None
        self._ErrorRate = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount

    @property
    def ErrorRate(self):
        return self._ErrorRate

    @ErrorRate.setter
    def ErrorRate(self, ErrorRate):
        self._ErrorRate = ErrorRate


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Step = params.get("Step")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        self._ErrorRate = params.get("ErrorRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Concurrency(AbstractModel):
    """并发模式的施压配置

    """

    def __init__(self):
        r"""
        :param _Stages: 多阶段配置数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Stages: list of Stage
        :param _IterationCount: 运行次数
注意：此字段可能返回 null，表示取不到有效值。
        :type IterationCount: int
        :param _MaxRequestsPerSecond: 最大RPS
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestsPerSecond: int
        :param _GracefulStopSeconds: 优雅终止任务的等待时间
注意：此字段可能返回 null，表示取不到有效值。
        :type GracefulStopSeconds: int
        :param _Resources: 资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: int
        """
        self._Stages = None
        self._IterationCount = None
        self._MaxRequestsPerSecond = None
        self._GracefulStopSeconds = None
        self._Resources = None

    @property
    def Stages(self):
        return self._Stages

    @Stages.setter
    def Stages(self, Stages):
        self._Stages = Stages

    @property
    def IterationCount(self):
        return self._IterationCount

    @IterationCount.setter
    def IterationCount(self, IterationCount):
        self._IterationCount = IterationCount

    @property
    def MaxRequestsPerSecond(self):
        return self._MaxRequestsPerSecond

    @MaxRequestsPerSecond.setter
    def MaxRequestsPerSecond(self, MaxRequestsPerSecond):
        self._MaxRequestsPerSecond = MaxRequestsPerSecond

    @property
    def GracefulStopSeconds(self):
        return self._GracefulStopSeconds

    @GracefulStopSeconds.setter
    def GracefulStopSeconds(self, GracefulStopSeconds):
        self._GracefulStopSeconds = GracefulStopSeconds

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        if params.get("Stages") is not None:
            self._Stages = []
            for item in params.get("Stages"):
                obj = Stage()
                obj._deserialize(item)
                self._Stages.append(obj)
        self._IterationCount = params.get("IterationCount")
        self._MaxRequestsPerSecond = params.get("MaxRequestsPerSecond")
        self._GracefulStopSeconds = params.get("GracefulStopSeconds")
        self._Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyScenarioRequest(AbstractModel):
    """CopyScenario请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _ScenarioId: 场景 ID
        :type ScenarioId: str
        """
        self._ProjectId = None
        self._ScenarioId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyScenarioResponse(AbstractModel):
    """CopyScenario返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioId: 复制出的新场景 ID
        :type ScenarioId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScenarioId = None
        self._RequestId = None

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScenarioId = params.get("ScenarioId")
        self._RequestId = params.get("RequestId")


class CreateAlertChannelRequest(AbstractModel):
    """CreateAlertChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeId: monitor 服务的告警通知模板的 NoticeId，可从 monitor 服务的云 API 的 DescribeAlarmNotices 接口响应里的 Id 字段获取。（CreateAlertChannel 接口的入参里用于标识一个告警通知模板的 AMPConsumerId 与 NoticeId 二选一即可）
        :type NoticeId: str
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _AMPConsumerId: monitor 服务的告警通知模板的 AMPConsumerId，可从 monitor 服务的云 API 的 DescribeAlarmNotices 接口响应里的 AMPConsumerId 字段获取。（CreateAlertChannel 接口的入参里用于标识一个告警通知模板的 AMPConsumerId 与 NoticeId 二选一即可）
        :type AMPConsumerId: str
        """
        self._NoticeId = None
        self._ProjectId = None
        self._AMPConsumerId = None

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AMPConsumerId(self):
        return self._AMPConsumerId

    @AMPConsumerId.setter
    def AMPConsumerId(self, AMPConsumerId):
        self._AMPConsumerId = AMPConsumerId


    def _deserialize(self, params):
        self._NoticeId = params.get("NoticeId")
        self._ProjectId = params.get("ProjectId")
        self._AMPConsumerId = params.get("AMPConsumerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAlertChannelResponse(AbstractModel):
    """CreateAlertChannel返回参数结构体

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


class CreateCronJobRequest(AbstractModel):
    """CreateCronJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 定时任务名字
        :type Name: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _ScenarioName: 场景名称
        :type ScenarioName: str
        :param _FrequencyType: 执行频率类型，1:只执行一次; 2:日粒度; 3:周粒度; 4:高级
        :type FrequencyType: int
        :param _CronExpression: cron表达式
        :type CronExpression: str
        :param _JobOwner: 任务发起人
        :type JobOwner: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _NoticeId: Notice ID
        :type NoticeId: str
        :param _Note: 备注
        :type Note: str
        """
        self._Name = None
        self._ProjectId = None
        self._ScenarioId = None
        self._ScenarioName = None
        self._FrequencyType = None
        self._CronExpression = None
        self._JobOwner = None
        self._EndTime = None
        self._NoticeId = None
        self._Note = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def ScenarioName(self):
        return self._ScenarioName

    @ScenarioName.setter
    def ScenarioName(self, ScenarioName):
        self._ScenarioName = ScenarioName

    @property
    def FrequencyType(self):
        return self._FrequencyType

    @FrequencyType.setter
    def FrequencyType(self, FrequencyType):
        self._FrequencyType = FrequencyType

    @property
    def CronExpression(self):
        return self._CronExpression

    @CronExpression.setter
    def CronExpression(self, CronExpression):
        self._CronExpression = CronExpression

    @property
    def JobOwner(self):
        return self._JobOwner

    @JobOwner.setter
    def JobOwner(self, JobOwner):
        self._JobOwner = JobOwner

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        self._ScenarioName = params.get("ScenarioName")
        self._FrequencyType = params.get("FrequencyType")
        self._CronExpression = params.get("CronExpression")
        self._JobOwner = params.get("JobOwner")
        self._EndTime = params.get("EndTime")
        self._NoticeId = params.get("NoticeId")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCronJobResponse(AbstractModel):
    """CreateCronJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CronJobId: 定时任务ID
        :type CronJobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CronJobId = None
        self._RequestId = None

    @property
    def CronJobId(self):
        return self._CronJobId

    @CronJobId.setter
    def CronJobId(self, CronJobId):
        self._CronJobId = CronJobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CronJobId = params.get("CronJobId")
        self._RequestId = params.get("RequestId")


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment请求参数结构体

    """


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment返回参数结构体

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


class CreateFileRequest(AbstractModel):
    """CreateFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileId: 文件 ID。其值应为前序步骤上传该文件到 cos 桶后，文件在 cos 桶中的相应目录
        :type FileId: str
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _Kind: 文件种类，参数文件-1，协议文件-2，请求文件-3
        :type Kind: int
        :param _Name: 文件名
        :type Name: str
        :param _Size: 文件大小
        :type Size: int
        :param _Type: 文件类型，文件夹-folder
        :type Type: str
        :param _LineCount: 行数
        :type LineCount: int
        :param _HeadLines: 前几行数据
        :type HeadLines: list of str
        :param _TailLines: 后几行数据
        :type TailLines: list of str
        :param _HeaderInFile: 表头是否在文件内
        :type HeaderInFile: bool
        :param _HeaderColumns: 表头
        :type HeaderColumns: list of str
        :param _FileInfos: 文件夹中的文件
        :type FileInfos: list of FileInfo
        """
        self._FileId = None
        self._ProjectId = None
        self._Kind = None
        self._Name = None
        self._Size = None
        self._Type = None
        self._LineCount = None
        self._HeadLines = None
        self._TailLines = None
        self._HeaderInFile = None
        self._HeaderColumns = None
        self._FileInfos = None

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LineCount(self):
        return self._LineCount

    @LineCount.setter
    def LineCount(self, LineCount):
        self._LineCount = LineCount

    @property
    def HeadLines(self):
        return self._HeadLines

    @HeadLines.setter
    def HeadLines(self, HeadLines):
        self._HeadLines = HeadLines

    @property
    def TailLines(self):
        return self._TailLines

    @TailLines.setter
    def TailLines(self, TailLines):
        self._TailLines = TailLines

    @property
    def HeaderInFile(self):
        return self._HeaderInFile

    @HeaderInFile.setter
    def HeaderInFile(self, HeaderInFile):
        self._HeaderInFile = HeaderInFile

    @property
    def HeaderColumns(self):
        return self._HeaderColumns

    @HeaderColumns.setter
    def HeaderColumns(self, HeaderColumns):
        self._HeaderColumns = HeaderColumns

    @property
    def FileInfos(self):
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._ProjectId = params.get("ProjectId")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        self._LineCount = params.get("LineCount")
        self._HeadLines = params.get("HeadLines")
        self._TailLines = params.get("TailLines")
        self._HeaderInFile = params.get("HeaderInFile")
        self._HeaderColumns = params.get("HeaderColumns")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileResponse(AbstractModel):
    """CreateFile返回参数结构体

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
        :param _Name: 项目名
        :type Name: str
        :param _Description: 项目描述
        :type Description: str
        :param _Tags: 标签数组
        :type Tags: list of TagSpec
        """
        self._Name = None
        self._Description = None
        self._Tags = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpec()
                obj._deserialize(item)
                self._Tags.append(obj)
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
        :param _ProjectId: 项目ID
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


class CreateScenarioRequest(AbstractModel):
    """CreateScenario请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 场景名
        :type Name: str
        :param _Type: 压测引擎类型
        :type Type: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Description: 场景描述
        :type Description: str
        :param _Load: 施压配置
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param _Configs: deprecated
        :type Configs: list of str
        :param _Datasets: 测试数据集
        :type Datasets: list of TestData
        :param _Extensions: deprecated
        :type Extensions: list of str
        :param _SLAId: deprecated
        :type SLAId: str
        :param _CronId: cron job ID
        :type CronId: str
        :param _Scripts: deprecated
        :type Scripts: list of str
        :param _TestScripts: 测试脚本文件信息
        :type TestScripts: list of ScriptInfo
        :param _Protocols: 协议文件路径
        :type Protocols: list of ProtocolInfo
        :param _RequestFiles: 请求文件路径
        :type RequestFiles: list of FileInfo
        :param _SLAPolicy: SLA 策略
        :type SLAPolicy: :class:`tencentcloud.pts.v20210728.models.SLAPolicy`
        :param _Plugins: 拓展包文件路径
        :type Plugins: list of FileInfo
        :param _DomainNameConfig: 域名解析配置
        :type DomainNameConfig: :class:`tencentcloud.pts.v20210728.models.DomainNameConfig`
        :param _Owner: 创建人名
        :type Owner: str
        """
        self._Name = None
        self._Type = None
        self._ProjectId = None
        self._Description = None
        self._Load = None
        self._Configs = None
        self._Datasets = None
        self._Extensions = None
        self._SLAId = None
        self._CronId = None
        self._Scripts = None
        self._TestScripts = None
        self._Protocols = None
        self._RequestFiles = None
        self._SLAPolicy = None
        self._Plugins = None
        self._DomainNameConfig = None
        self._Owner = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Load(self):
        return self._Load

    @Load.setter
    def Load(self, Load):
        self._Load = Load

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def Datasets(self):
        return self._Datasets

    @Datasets.setter
    def Datasets(self, Datasets):
        self._Datasets = Datasets

    @property
    def Extensions(self):
        return self._Extensions

    @Extensions.setter
    def Extensions(self, Extensions):
        self._Extensions = Extensions

    @property
    def SLAId(self):
        return self._SLAId

    @SLAId.setter
    def SLAId(self, SLAId):
        self._SLAId = SLAId

    @property
    def CronId(self):
        return self._CronId

    @CronId.setter
    def CronId(self, CronId):
        self._CronId = CronId

    @property
    def Scripts(self):
        return self._Scripts

    @Scripts.setter
    def Scripts(self, Scripts):
        self._Scripts = Scripts

    @property
    def TestScripts(self):
        return self._TestScripts

    @TestScripts.setter
    def TestScripts(self, TestScripts):
        self._TestScripts = TestScripts

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def RequestFiles(self):
        return self._RequestFiles

    @RequestFiles.setter
    def RequestFiles(self, RequestFiles):
        self._RequestFiles = RequestFiles

    @property
    def SLAPolicy(self):
        return self._SLAPolicy

    @SLAPolicy.setter
    def SLAPolicy(self, SLAPolicy):
        self._SLAPolicy = SLAPolicy

    @property
    def Plugins(self):
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def DomainNameConfig(self):
        return self._DomainNameConfig

    @DomainNameConfig.setter
    def DomainNameConfig(self, DomainNameConfig):
        self._DomainNameConfig = DomainNameConfig

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        if params.get("Load") is not None:
            self._Load = Load()
            self._Load._deserialize(params.get("Load"))
        self._Configs = params.get("Configs")
        if params.get("Datasets") is not None:
            self._Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self._Datasets.append(obj)
        self._Extensions = params.get("Extensions")
        self._SLAId = params.get("SLAId")
        self._CronId = params.get("CronId")
        self._Scripts = params.get("Scripts")
        if params.get("TestScripts") is not None:
            self._TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self._TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self._Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self._Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self._RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self._RequestFiles.append(obj)
        if params.get("SLAPolicy") is not None:
            self._SLAPolicy = SLAPolicy()
            self._SLAPolicy._deserialize(params.get("SLAPolicy"))
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self._Plugins.append(obj)
        if params.get("DomainNameConfig") is not None:
            self._DomainNameConfig = DomainNameConfig()
            self._DomainNameConfig._deserialize(params.get("DomainNameConfig"))
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScenarioResponse(AbstractModel):
    """CreateScenario返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScenarioId = None
        self._RequestId = None

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScenarioId = params.get("ScenarioId")
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """COS临时凭证

    """

    def __init__(self):
        r"""
        :param _TmpSecretId: 临时secret ID
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时secret key
        :type TmpSecretKey: str
        :param _Token: 临时token
        :type Token: str
        """
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._Token = None

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronJob(AbstractModel):
    """定时任务

    """

    def __init__(self):
        r"""
        :param _CronJobId: 定时任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJobId: str
        :param _Name: 定时任务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _ScenarioId: 场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioId: str
        :param _ScenarioName: 场景名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioName: str
        :param _CronExpression: cron 表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type CronExpression: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _AbortReason: 中止原因
注意：此字段可能返回 null，表示取不到有效值。
        :type AbortReason: int
        :param _Status: 定时任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _NoticeId: Notice ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NoticeId: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _FrequencyType: 执行频率类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FrequencyType: int
        :param _Note: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param _JobOwner: tom
注意：此字段可能返回 null，表示取不到有效值。
        :type JobOwner: str
        :param _AppId: App ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubAccountUin: 子账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        """
        self._CronJobId = None
        self._Name = None
        self._ProjectId = None
        self._ScenarioId = None
        self._ScenarioName = None
        self._CronExpression = None
        self._EndTime = None
        self._AbortReason = None
        self._Status = None
        self._NoticeId = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._FrequencyType = None
        self._Note = None
        self._JobOwner = None
        self._AppId = None
        self._Uin = None
        self._SubAccountUin = None

    @property
    def CronJobId(self):
        return self._CronJobId

    @CronJobId.setter
    def CronJobId(self, CronJobId):
        self._CronJobId = CronJobId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def ScenarioName(self):
        return self._ScenarioName

    @ScenarioName.setter
    def ScenarioName(self, ScenarioName):
        self._ScenarioName = ScenarioName

    @property
    def CronExpression(self):
        return self._CronExpression

    @CronExpression.setter
    def CronExpression(self, CronExpression):
        self._CronExpression = CronExpression

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AbortReason(self):
        return self._AbortReason

    @AbortReason.setter
    def AbortReason(self, AbortReason):
        self._AbortReason = AbortReason

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def FrequencyType(self):
        return self._FrequencyType

    @FrequencyType.setter
    def FrequencyType(self, FrequencyType):
        self._FrequencyType = FrequencyType

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def JobOwner(self):
        return self._JobOwner

    @JobOwner.setter
    def JobOwner(self, JobOwner):
        self._JobOwner = JobOwner

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin


    def _deserialize(self, params):
        self._CronJobId = params.get("CronJobId")
        self._Name = params.get("Name")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        self._ScenarioName = params.get("ScenarioName")
        self._CronExpression = params.get("CronExpression")
        self._EndTime = params.get("EndTime")
        self._AbortReason = params.get("AbortReason")
        self._Status = params.get("Status")
        self._NoticeId = params.get("NoticeId")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._FrequencyType = params.get("FrequencyType")
        self._Note = params.get("Note")
        self._JobOwner = params.get("JobOwner")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomSample(AbstractModel):
    """sample附带原始查询语句中的metric, aggregation

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名
        :type Metric: str
        :param _Aggregation: 聚合条件
        :type Aggregation: str
        :param _Labels: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param _Value: 查询值
        :type Value: float
        :param _Timestamp: Time is the number of milliseconds since the epoch
// (1970-01-01 00:00 UTC) excluding leap seconds.
        :type Timestamp: int
        :param _Unit: 指标对应的单位，当前单位有：s,bytes,bytes/s,reqs,reqs/s,checks,checks/s,iters,iters/s,VUs, %
        :type Unit: str
        :param _Name: 指标序列名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Metric = None
        self._Aggregation = None
        self._Labels = None
        self._Value = None
        self._Timestamp = None
        self._Unit = None
        self._Name = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Aggregation(self):
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Aggregation = params.get("Aggregation")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Value = params.get("Value")
        self._Timestamp = params.get("Timestamp")
        self._Unit = params.get("Unit")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomSampleMatrix(AbstractModel):
    """指标矩阵，可包含多条指标序列

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名字
        :type Metric: str
        :param _Aggregation: 聚合函数
        :type Aggregation: str
        :param _Unit: 指标单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param _Streams: 指标序列数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Streams: list of SampleStream
        """
        self._Metric = None
        self._Aggregation = None
        self._Unit = None
        self._Streams = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Aggregation(self):
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Streams(self):
        return self._Streams

    @Streams.setter
    def Streams(self, Streams):
        self._Streams = Streams


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Aggregation = params.get("Aggregation")
        self._Unit = params.get("Unit")
        if params.get("Streams") is not None:
            self._Streams = []
            for item in params.get("Streams"):
                obj = SampleStream()
                obj._deserialize(item)
                self._Streams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSConfig(AbstractModel):
    """施压机 DNS 配置

    """

    def __init__(self):
        r"""
        :param _Nameservers: DNS IP 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Nameservers: list of str
        """
        self._Nameservers = None

    @property
    def Nameservers(self):
        return self._Nameservers

    @Nameservers.setter
    def Nameservers(self, Nameservers):
        self._Nameservers = Nameservers


    def _deserialize(self, params):
        self._Nameservers = params.get("Nameservers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlertChannelRequest(AbstractModel):
    """DeleteAlertChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _NoticeId: 待删除的通知渠道的 Notice ID（所有通知渠道的 Notice ID 可以从 DescribeAlertChannels 接口获取）
        :type NoticeId: str
        """
        self._ProjectId = None
        self._NoticeId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAlertChannelResponse(AbstractModel):
    """DeleteAlertChannel返回参数结构体

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


class DeleteCronJobsRequest(AbstractModel):
    """DeleteCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        """
        self._ProjectId = None
        self._CronJobIds = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CronJobIds(self):
        return self._CronJobIds

    @CronJobIds.setter
    def CronJobIds(self, CronJobIds):
        self._CronJobIds = CronJobIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CronJobIds = params.get("CronJobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCronJobsResponse(AbstractModel):
    """DeleteCronJobs返回参数结构体

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


class DeleteEnvironmentsRequest(AbstractModel):
    """DeleteEnvironments请求参数结构体

    """


class DeleteEnvironmentsResponse(AbstractModel):
    """DeleteEnvironments返回参数结构体

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


class DeleteFilesRequest(AbstractModel):
    """DeleteFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _FileIds: 待删除的文件的 ID（所有文件 ID 可从接口 DescribeFiles 获取）
        :type FileIds: list of str
        """
        self._ProjectId = None
        self._FileIds = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._FileIds = params.get("FileIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFilesResponse(AbstractModel):
    """DeleteFiles返回参数结构体

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


class DeleteJobsRequest(AbstractModel):
    """DeleteJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobIds: 待删除的任务的 ID（所有任务的 ID 可以从 DescribeJobs 获取）
        :type JobIds: list of str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        """
        self._JobIds = None
        self._ProjectId = None
        self._ScenarioIds = None

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioIds(self):
        return self._ScenarioIds

    @ScenarioIds.setter
    def ScenarioIds(self, ScenarioIds):
        self._ScenarioIds = ScenarioIds


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioIds = params.get("ScenarioIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobsResponse(AbstractModel):
    """DeleteJobs返回参数结构体

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


class DeleteProjectsRequest(AbstractModel):
    """DeleteProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param _DeleteScenarios: 是否删除项目相关的场景。默认为否。
        :type DeleteScenarios: bool
        :param _DeleteJobs: 是否删除项目相关的任务。默认为否。
        :type DeleteJobs: bool
        """
        self._ProjectIds = None
        self._DeleteScenarios = None
        self._DeleteJobs = None

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def DeleteScenarios(self):
        return self._DeleteScenarios

    @DeleteScenarios.setter
    def DeleteScenarios(self, DeleteScenarios):
        self._DeleteScenarios = DeleteScenarios

    @property
    def DeleteJobs(self):
        return self._DeleteJobs

    @DeleteJobs.setter
    def DeleteJobs(self, DeleteJobs):
        self._DeleteJobs = DeleteJobs


    def _deserialize(self, params):
        self._ProjectIds = params.get("ProjectIds")
        self._DeleteScenarios = params.get("DeleteScenarios")
        self._DeleteJobs = params.get("DeleteJobs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectsResponse(AbstractModel):
    """DeleteProjects返回参数结构体

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


class DeleteScenariosRequest(AbstractModel):
    """DeleteScenarios请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _DeleteJobs: 是否删除场景相关的任务。默认为否。
        :type DeleteJobs: bool
        """
        self._ScenarioIds = None
        self._ProjectId = None
        self._DeleteJobs = None

    @property
    def ScenarioIds(self):
        return self._ScenarioIds

    @ScenarioIds.setter
    def ScenarioIds(self, ScenarioIds):
        self._ScenarioIds = ScenarioIds

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeleteJobs(self):
        return self._DeleteJobs

    @DeleteJobs.setter
    def DeleteJobs(self, DeleteJobs):
        self._DeleteJobs = DeleteJobs


    def _deserialize(self, params):
        self._ScenarioIds = params.get("ScenarioIds")
        self._ProjectId = params.get("ProjectId")
        self._DeleteJobs = params.get("DeleteJobs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScenariosResponse(AbstractModel):
    """DeleteScenarios返回参数结构体

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


class DescribeAlertChannelsRequest(AbstractModel):
    """DescribeAlertChannels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectIds: 项目 ID 列表
        :type ProjectIds: list of str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param _NoticeIds: Notice ID 列表
        :type NoticeIds: list of str
        :param _OrderBy: 排序项
        :type OrderBy: str
        :param _Ascend: 是否正序
        :type Ascend: bool
        """
        self._ProjectIds = None
        self._Offset = None
        self._Limit = None
        self._NoticeIds = None
        self._OrderBy = None
        self._Ascend = None

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

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
    def NoticeIds(self):
        return self._NoticeIds

    @NoticeIds.setter
    def NoticeIds(self, NoticeIds):
        self._NoticeIds = NoticeIds

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend


    def _deserialize(self, params):
        self._ProjectIds = params.get("ProjectIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NoticeIds = params.get("NoticeIds")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertChannelsResponse(AbstractModel):
    """DescribeAlertChannels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlertChannelSet: 告警通知接收组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertChannelSet: list of AlertChannelRecord
        :param _Total: 告警通知接收组数目
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlertChannelSet = None
        self._Total = None
        self._RequestId = None

    @property
    def AlertChannelSet(self):
        return self._AlertChannelSet

    @AlertChannelSet.setter
    def AlertChannelSet(self, AlertChannelSet):
        self._AlertChannelSet = AlertChannelSet

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
        if params.get("AlertChannelSet") is not None:
            self._AlertChannelSet = []
            for item in params.get("AlertChannelSet"):
                obj = AlertChannelRecord()
                obj._deserialize(item)
                self._AlertChannelSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAlertRecordsRequest(AbstractModel):
    """DescribeAlertRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectIds: 项目 ID 列表
        :type ProjectIds: list of str
        :param _ScenarioIds: 场景 ID 列表
        :type ScenarioIds: list of str
        :param _JobIds: 任务 ID 列表
        :type JobIds: list of str
        :param _Ascend: 是否正序
        :type Ascend: bool
        :param _OrderBy: 排序项
        :type OrderBy: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param _ScenarioNames: 按场景名筛选
        :type ScenarioNames: list of str
        """
        self._ProjectIds = None
        self._ScenarioIds = None
        self._JobIds = None
        self._Ascend = None
        self._OrderBy = None
        self._Offset = None
        self._Limit = None
        self._ScenarioNames = None

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ScenarioIds(self):
        return self._ScenarioIds

    @ScenarioIds.setter
    def ScenarioIds(self, ScenarioIds):
        self._ScenarioIds = ScenarioIds

    @property
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

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
    def ScenarioNames(self):
        return self._ScenarioNames

    @ScenarioNames.setter
    def ScenarioNames(self, ScenarioNames):
        self._ScenarioNames = ScenarioNames


    def _deserialize(self, params):
        self._ProjectIds = params.get("ProjectIds")
        self._ScenarioIds = params.get("ScenarioIds")
        self._JobIds = params.get("JobIds")
        self._Ascend = params.get("Ascend")
        self._OrderBy = params.get("OrderBy")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ScenarioNames = params.get("ScenarioNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlertRecordsResponse(AbstractModel):
    """DescribeAlertRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AlertRecordSet: 告警历史
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRecordSet: list of AlertRecord
        :param _Total: 告警历史记录的总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AlertRecordSet = None
        self._Total = None
        self._RequestId = None

    @property
    def AlertRecordSet(self):
        return self._AlertRecordSet

    @AlertRecordSet.setter
    def AlertRecordSet(self, AlertRecordSet):
        self._AlertRecordSet = AlertRecordSet

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
        if params.get("AlertRecordSet") is not None:
            self._AlertRecordSet = []
            for item in params.get("AlertRecordSet"):
                obj = AlertRecord()
                obj._deserialize(item)
                self._AlertRecordSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeAvailableMetricsRequest(AbstractModel):
    """DescribeAvailableMetrics请求参数结构体

    """


class DescribeAvailableMetricsResponse(AbstractModel):
    """DescribeAvailableMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricSet: 系统支持的所有指标
        :type MetricSet: list of MetricInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricSet = None
        self._RequestId = None

    @property
    def MetricSet(self):
        return self._MetricSet

    @MetricSet.setter
    def MetricSet(self, MetricSet):
        self._MetricSet = MetricSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self._MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricInfo()
                obj._deserialize(item)
                self._MetricSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCheckSummaryRequest(AbstractModel):
    """DescribeCheckSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._JobId = None
        self._ScenarioId = None
        self._ProjectId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ScenarioId = params.get("ScenarioId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCheckSummaryResponse(AbstractModel):
    """DescribeCheckSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckSummarySet: 检查点汇总信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckSummarySet: list of CheckSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckSummarySet = None
        self._RequestId = None

    @property
    def CheckSummarySet(self):
        return self._CheckSummarySet

    @CheckSummarySet.setter
    def CheckSummarySet(self, CheckSummarySet):
        self._CheckSummarySet = CheckSummarySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CheckSummarySet") is not None:
            self._CheckSummarySet = []
            for item in params.get("CheckSummarySet"):
                obj = CheckSummary()
                obj._deserialize(item)
                self._CheckSummarySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCronJobsRequest(AbstractModel):
    """DescribeCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        :param _CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        :param _CronJobName: 定时任务名字，模糊查询
        :type CronJobName: str
        :param _CronJobStatus: 定时任务状态数组
        :type CronJobStatus: list of int
        :param _OrderBy: 排序的列
        :type OrderBy: str
        :param _Ascend: 是否正序
        :type Ascend: bool
        """
        self._ProjectIds = None
        self._Offset = None
        self._Limit = None
        self._CronJobIds = None
        self._CronJobName = None
        self._CronJobStatus = None
        self._OrderBy = None
        self._Ascend = None

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

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
    def CronJobIds(self):
        return self._CronJobIds

    @CronJobIds.setter
    def CronJobIds(self, CronJobIds):
        self._CronJobIds = CronJobIds

    @property
    def CronJobName(self):
        return self._CronJobName

    @CronJobName.setter
    def CronJobName(self, CronJobName):
        self._CronJobName = CronJobName

    @property
    def CronJobStatus(self):
        return self._CronJobStatus

    @CronJobStatus.setter
    def CronJobStatus(self, CronJobStatus):
        self._CronJobStatus = CronJobStatus

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend


    def _deserialize(self, params):
        self._ProjectIds = params.get("ProjectIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CronJobIds = params.get("CronJobIds")
        self._CronJobName = params.get("CronJobName")
        self._CronJobStatus = params.get("CronJobStatus")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCronJobsResponse(AbstractModel):
    """DescribeCronJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 定时任务总数
        :type Total: int
        :param _CronJobSet: 定时任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJobSet: list of CronJob
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._CronJobSet = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CronJobSet(self):
        return self._CronJobSet

    @CronJobSet.setter
    def CronJobSet(self, CronJobSet):
        self._CronJobSet = CronJobSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CronJobSet") is not None:
            self._CronJobSet = []
            for item in params.get("CronJobSet"):
                obj = CronJob()
                obj._deserialize(item)
                self._CronJobSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments请求参数结构体

    """


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments返回参数结构体

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


class DescribeErrorSummaryRequest(AbstractModel):
    """DescribeErrorSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._JobId = None
        self._ScenarioId = None
        self._ProjectId = None
        self._Filters = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ScenarioId = params.get("ScenarioId")
        self._ProjectId = params.get("ProjectId")
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
        


class DescribeErrorSummaryResponse(AbstractModel):
    """DescribeErrorSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorSummarySet: 错误汇总信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorSummarySet: list of ErrorSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorSummarySet = None
        self._RequestId = None

    @property
    def ErrorSummarySet(self):
        return self._ErrorSummarySet

    @ErrorSummarySet.setter
    def ErrorSummarySet(self, ErrorSummarySet):
        self._ErrorSummarySet = ErrorSummarySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorSummarySet") is not None:
            self._ErrorSummarySet = []
            for item in params.get("ErrorSummarySet"):
                obj = ErrorSummary()
                obj._deserialize(item)
                self._ErrorSummarySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFilesRequest(AbstractModel):
    """DescribeFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectIds: 项目 ID 数组
        :type ProjectIds: list of str
        :param _FileIds: 文件 ID 数组
        :type FileIds: list of str
        :param _FileName: 文件名
        :type FileName: str
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大为 100
        :type Limit: int
        :param _Kind: 文件种类，参数文件-1，协议文件-2，请求文件-3
        :type Kind: int
        """
        self._ProjectIds = None
        self._FileIds = None
        self._FileName = None
        self._Offset = None
        self._Limit = None
        self._Kind = None

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def FileIds(self):
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

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
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._ProjectIds = params.get("ProjectIds")
        self._FileIds = params.get("FileIds")
        self._FileName = params.get("FileName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFilesResponse(AbstractModel):
    """DescribeFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileSet: 文件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSet: list of File
        :param _Total: 文件总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileSet = None
        self._Total = None
        self._RequestId = None

    @property
    def FileSet(self):
        return self._FileSet

    @FileSet.setter
    def FileSet(self, FileSet):
        self._FileSet = FileSet

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
        if params.get("FileSet") is not None:
            self._FileSet = []
            for item in params.get("FileSet"):
                obj = File()
                obj._deserialize(item)
                self._FileSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param _ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param _Offset: 分页起始位置
        :type Offset: int
        :param _Limit: 每页最大数目
        :type Limit: int
        :param _JobIds: 任务ID数组
        :type JobIds: list of str
        :param _OrderBy: 按字段排序
        :type OrderBy: str
        :param _Ascend: 升序/降序
        :type Ascend: bool
        :param _StartTime: 任务开始时间
        :type StartTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _Debug: 调试任务标记
        :type Debug: bool
        :param _Status: 任务的状态
        :type Status: list of int
        """
        self._ScenarioIds = None
        self._ProjectIds = None
        self._Offset = None
        self._Limit = None
        self._JobIds = None
        self._OrderBy = None
        self._Ascend = None
        self._StartTime = None
        self._EndTime = None
        self._Debug = None
        self._Status = None

    @property
    def ScenarioIds(self):
        return self._ScenarioIds

    @ScenarioIds.setter
    def ScenarioIds(self, ScenarioIds):
        self._ScenarioIds = ScenarioIds

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

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
    def JobIds(self):
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend

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
    def Debug(self):
        return self._Debug

    @Debug.setter
    def Debug(self, Debug):
        self._Debug = Debug

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ScenarioIds = params.get("ScenarioIds")
        self._ProjectIds = params.get("ProjectIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._JobIds = params.get("JobIds")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Debug = params.get("Debug")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobSet: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type JobSet: list of Job
        :param _Total: 任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobSet = None
        self._Total = None
        self._RequestId = None

    @property
    def JobSet(self):
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

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
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = Job()
                obj._deserialize(item)
                self._JobSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeLabelValuesRequest(AbstractModel):
    """DescribeLabelValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _Metric: 指标名。取值范围参见 DescribeMetricLabelWithValues 接口返回的所有指标名
        :type Metric: str
        :param _LabelName: 标签名。取值范围参见 DescribeMetricLabelWithValues 接口返回的指标及其支持的标签名
        :type LabelName: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._JobId = None
        self._ScenarioId = None
        self._Metric = None
        self._LabelName = None
        self._ProjectId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ScenarioId = params.get("ScenarioId")
        self._Metric = params.get("Metric")
        self._LabelName = params.get("LabelName")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLabelValuesResponse(AbstractModel):
    """DescribeLabelValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LabelValueSet: 标签值数组
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValueSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LabelValueSet = None
        self._RequestId = None

    @property
    def LabelValueSet(self):
        return self._LabelValueSet

    @LabelValueSet.setter
    def LabelValueSet(self, LabelValueSet):
        self._LabelValueSet = LabelValueSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LabelValueSet = params.get("LabelValueSet")
        self._RequestId = params.get("RequestId")


class DescribeMetricLabelWithValuesRequest(AbstractModel):
    """DescribeMetricLabelWithValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: job id
        :type JobId: str
        :param _ProjectId: project id
        :type ProjectId: str
        :param _ScenarioId: scenario id
        :type ScenarioId: str
        """
        self._JobId = None
        self._ProjectId = None
        self._ScenarioId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMetricLabelWithValuesResponse(AbstractModel):
    """DescribeMetricLabelWithValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricLabelWithValuesSet: 指标所有的label和values数组
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricLabelWithValuesSet: list of MetricLabelWithValues
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricLabelWithValuesSet = None
        self._RequestId = None

    @property
    def MetricLabelWithValuesSet(self):
        return self._MetricLabelWithValuesSet

    @MetricLabelWithValuesSet.setter
    def MetricLabelWithValuesSet(self, MetricLabelWithValuesSet):
        self._MetricLabelWithValuesSet = MetricLabelWithValuesSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricLabelWithValuesSet") is not None:
            self._MetricLabelWithValuesSet = []
            for item in params.get("MetricLabelWithValuesSet"):
                obj = MetricLabelWithValues()
                obj._deserialize(item)
                self._MetricLabelWithValuesSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNormalLogsRequest(AbstractModel):
    """DescribeNormalLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 压测项目ID
        :type ProjectId: str
        :param _ScenarioId: 测试场景ID
        :type ScenarioId: str
        :param _JobId: 压测任务ID
        :type JobId: str
        :param _Context: 日志上下文，加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
        :type Context: str
        :param _From: 日志开始时间
        :type From: str
        :param _To: 日志结束时间
        :type To: str
        :param _SeverityText: 日志级别，可取debug/info/error
        :type SeverityText: str
        :param _Instance: 施压节点IP
        :type Instance: str
        :param _InstanceRegion: 施压节点所在地域
        :type InstanceRegion: str
        :param _LogType: 日志类型， console代表用户输出，engine代表引擎输出
        :type LogType: str
        :param _Limit: 返回日志条数限制，最大100
        :type Limit: int
        """
        self._ProjectId = None
        self._ScenarioId = None
        self._JobId = None
        self._Context = None
        self._From = None
        self._To = None
        self._SeverityText = None
        self._Instance = None
        self._InstanceRegion = None
        self._LogType = None
        self._Limit = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def SeverityText(self):
        return self._SeverityText

    @SeverityText.setter
    def SeverityText(self, SeverityText):
        self._SeverityText = SeverityText

    @property
    def Instance(self):
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def InstanceRegion(self):
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        self._JobId = params.get("JobId")
        self._Context = params.get("Context")
        self._From = params.get("From")
        self._To = params.get("To")
        self._SeverityText = params.get("SeverityText")
        self._Instance = params.get("Instance")
        self._InstanceRegion = params.get("InstanceRegion")
        self._LogType = params.get("LogType")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNormalLogsResponse(AbstractModel):
    """DescribeNormalLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 日志上下文，加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _NormalLogs: 日志数组
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalLogs: list of NormalLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._NormalLogs = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def NormalLogs(self):
        return self._NormalLogs

    @NormalLogs.setter
    def NormalLogs(self, NormalLogs):
        self._NormalLogs = NormalLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        if params.get("NormalLogs") is not None:
            self._NormalLogs = []
            for item in params.get("NormalLogs"):
                obj = NormalLog()
                obj._deserialize(item)
                self._NormalLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页offset
        :type Offset: int
        :param _Limit: 每页limit
        :type Limit: int
        :param _ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param _ProjectName: 项目名
        :type ProjectName: str
        :param _OrderBy: 按字段排序
        :type OrderBy: str
        :param _Ascend: 升序/降序
        :type Ascend: bool
        :param _TagFilters: 标签数组
        :type TagFilters: list of TagSpec
        """
        self._Offset = None
        self._Limit = None
        self._ProjectIds = None
        self._ProjectName = None
        self._OrderBy = None
        self._Ascend = None
        self._TagFilters = None

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
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectIds = params.get("ProjectIds")
        self._ProjectName = params.get("ProjectName")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagSpec()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectSet: 项目数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectSet: list of Project
        :param _Total: 项目数量
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectSet = None
        self._Total = None
        self._RequestId = None

    @property
    def ProjectSet(self):
        return self._ProjectSet

    @ProjectSet.setter
    def ProjectSet(self, ProjectSet):
        self._ProjectSet = ProjectSet

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
        if params.get("ProjectSet") is not None:
            self._ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = Project()
                obj._deserialize(item)
                self._ProjectSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadType: 通过该参数指定不同压测网络环境，在不同网络环境下，PTS可用的地域不一样
        :type LoadType: int
        """
        self._LoadType = None

    @property
    def LoadType(self):
        return self._LoadType

    @LoadType.setter
    def LoadType(self, LoadType):
        self._LoadType = LoadType


    def _deserialize(self, params):
        self._LoadType = params.get("LoadType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 地域数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionSet: list of RegionDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRequestSummaryRequest(AbstractModel):
    """DescribeRequestSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 压测任务ID
        :type JobId: str
        :param _ScenarioId: 压测场景ID
        :type ScenarioId: str
        :param _ProjectId: 压测项目ID
        :type ProjectId: str
        """
        self._JobId = None
        self._ScenarioId = None
        self._ProjectId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ScenarioId = params.get("ScenarioId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRequestSummaryResponse(AbstractModel):
    """DescribeRequestSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestSummarySet: 请求汇总信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestSummarySet: list of RequestSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestSummarySet = None
        self._RequestId = None

    @property
    def RequestSummarySet(self):
        return self._RequestSummarySet

    @RequestSummarySet.setter
    def RequestSummarySet(self, RequestSummarySet):
        self._RequestSummarySet = RequestSummarySet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RequestSummarySet") is not None:
            self._RequestSummarySet = []
            for item in params.get("RequestSummarySet"):
                obj = RequestSummary()
                obj._deserialize(item)
                self._RequestSummarySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSampleBatchQueryRequest(AbstractModel):
    """DescribeSampleBatchQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 压测任务的 ID
        :type JobId: str
        :param _ScenarioId: 场景的 ID
        :type ScenarioId: str
        :param _Queries: 查询指标数组
        :type Queries: list of InternalMetricQuery
        :param _ProjectId: 项目的 ID
        :type ProjectId: str
        """
        self._JobId = None
        self._ScenarioId = None
        self._Queries = None
        self._ProjectId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Queries(self):
        return self._Queries

    @Queries.setter
    def Queries(self, Queries):
        self._Queries = Queries

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ScenarioId = params.get("ScenarioId")
        if params.get("Queries") is not None:
            self._Queries = []
            for item in params.get("Queries"):
                obj = InternalMetricQuery()
                obj._deserialize(item)
                self._Queries.append(obj)
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleBatchQueryResponse(AbstractModel):
    """DescribeSampleBatchQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricSampleSet: 返回指标内容
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSampleSet: list of CustomSample
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricSampleSet = None
        self._RequestId = None

    @property
    def MetricSampleSet(self):
        return self._MetricSampleSet

    @MetricSampleSet.setter
    def MetricSampleSet(self, MetricSampleSet):
        self._MetricSampleSet = MetricSampleSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricSampleSet") is not None:
            self._MetricSampleSet = []
            for item in params.get("MetricSampleSet"):
                obj = CustomSample()
                obj._deserialize(item)
                self._MetricSampleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSampleLogsRequest(AbstractModel):
    """DescribeSampleLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 测试项目ID
        :type ProjectId: str
        :param _ScenarioId: 测试场景ID
        :type ScenarioId: str
        :param _JobId: 测试任务ID
        :type JobId: str
        :param _Context: 加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
        :type Context: str
        :param _From: 日志开始时间
        :type From: str
        :param _To: 日志结束时间
        :type To: str
        :param _SeverityText: 日志级别debug,info,error
        :type SeverityText: str
        :param _InstanceRegion: ap-shanghai, ap-guangzhou
        :type InstanceRegion: str
        :param _Instance: 施压引擎节点IP
        :type Instance: str
        :param _LogType: request 代表采样日志,可为不填
        :type LogType: str
        :param _Limit: 返回日志条数，最大100
        :type Limit: int
        :param _ReactionTimeRange: 采样日志响应时间范围
        :type ReactionTimeRange: :class:`tencentcloud.pts.v20210728.models.ReactionTimeRange`
        :param _Status: 采样请求状态码
        :type Status: str
        :param _Result: 采样请求结果码
        :type Result: str
        :param _Method: 采样请求方法
        :type Method: str
        :param _Service: 采样服务API
        :type Service: str
        """
        self._ProjectId = None
        self._ScenarioId = None
        self._JobId = None
        self._Context = None
        self._From = None
        self._To = None
        self._SeverityText = None
        self._InstanceRegion = None
        self._Instance = None
        self._LogType = None
        self._Limit = None
        self._ReactionTimeRange = None
        self._Status = None
        self._Result = None
        self._Method = None
        self._Service = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def SeverityText(self):
        return self._SeverityText

    @SeverityText.setter
    def SeverityText(self, SeverityText):
        self._SeverityText = SeverityText

    @property
    def InstanceRegion(self):
        return self._InstanceRegion

    @InstanceRegion.setter
    def InstanceRegion(self, InstanceRegion):
        self._InstanceRegion = InstanceRegion

    @property
    def Instance(self):
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ReactionTimeRange(self):
        return self._ReactionTimeRange

    @ReactionTimeRange.setter
    def ReactionTimeRange(self, ReactionTimeRange):
        self._ReactionTimeRange = ReactionTimeRange

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        self._JobId = params.get("JobId")
        self._Context = params.get("Context")
        self._From = params.get("From")
        self._To = params.get("To")
        self._SeverityText = params.get("SeverityText")
        self._InstanceRegion = params.get("InstanceRegion")
        self._Instance = params.get("Instance")
        self._LogType = params.get("LogType")
        self._Limit = params.get("Limit")
        if params.get("ReactionTimeRange") is not None:
            self._ReactionTimeRange = ReactionTimeRange()
            self._ReactionTimeRange._deserialize(params.get("ReactionTimeRange"))
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._Method = params.get("Method")
        self._Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleLogsResponse(AbstractModel):
    """DescribeSampleLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 日志总数
        :type Total: int
        :param _Context: 日志上下文，加载更多日志时使用，透传上次返回的Context值，获取后续的日志内容。过期时间1小时
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _SampleLogs: 采样日志数组
注意：此字段可能返回 null，表示取不到有效值。
        :type SampleLogs: list of SampleLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Context = None
        self._SampleLogs = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def SampleLogs(self):
        return self._SampleLogs

    @SampleLogs.setter
    def SampleLogs(self, SampleLogs):
        self._SampleLogs = SampleLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Context = params.get("Context")
        if params.get("SampleLogs") is not None:
            self._SampleLogs = []
            for item in params.get("SampleLogs"):
                obj = SampleLog()
                obj._deserialize(item)
                self._SampleLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSampleMatrixBatchQueryRequest(AbstractModel):
    """DescribeSampleMatrixBatchQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _Queries: 查询语句
        :type Queries: list of InternalMetricQuery
        """
        self._JobId = None
        self._ProjectId = None
        self._ScenarioId = None
        self._Queries = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Queries(self):
        return self._Queries

    @Queries.setter
    def Queries(self, Queries):
        self._Queries = Queries


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        if params.get("Queries") is not None:
            self._Queries = []
            for item in params.get("Queries"):
                obj = InternalMetricQuery()
                obj._deserialize(item)
                self._Queries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleMatrixBatchQueryResponse(AbstractModel):
    """DescribeSampleMatrixBatchQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricSampleMatrixSet: 批量指标矩阵
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSampleMatrixSet: list of CustomSampleMatrix
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricSampleMatrixSet = None
        self._RequestId = None

    @property
    def MetricSampleMatrixSet(self):
        return self._MetricSampleMatrixSet

    @MetricSampleMatrixSet.setter
    def MetricSampleMatrixSet(self, MetricSampleMatrixSet):
        self._MetricSampleMatrixSet = MetricSampleMatrixSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricSampleMatrixSet") is not None:
            self._MetricSampleMatrixSet = []
            for item in params.get("MetricSampleMatrixSet"):
                obj = CustomSampleMatrix()
                obj._deserialize(item)
                self._MetricSampleMatrixSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSampleMatrixQueryRequest(AbstractModel):
    """DescribeSampleMatrixQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _Metric: 指标名。取值范围参见 DescribeMetricLabelWithValues 接口返回的所有指标名
        :type Metric: str
        :param _Aggregation: 聚合函数。取值范围：Rate,Count,Avg,P90,P95,P99,Gauge
        :type Aggregation: str
        :param _Filters: 用标签过滤规则来过滤指标，规则中包含标签名 LabelName、标签值 LabelValue、操作符 Operator（0代表相等，1代表不等）
        :type Filters: list of Filter
        :param _GroupBy: 分组
        :type GroupBy: list of str
        """
        self._JobId = None
        self._ProjectId = None
        self._ScenarioId = None
        self._Metric = None
        self._Aggregation = None
        self._Filters = None
        self._GroupBy = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Aggregation(self):
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        self._Metric = params.get("Metric")
        self._Aggregation = params.get("Aggregation")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._GroupBy = params.get("GroupBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleMatrixQueryResponse(AbstractModel):
    """DescribeSampleMatrixQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricSampleMatrix: 指标矩阵
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSampleMatrix: :class:`tencentcloud.pts.v20210728.models.CustomSampleMatrix`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricSampleMatrix = None
        self._RequestId = None

    @property
    def MetricSampleMatrix(self):
        return self._MetricSampleMatrix

    @MetricSampleMatrix.setter
    def MetricSampleMatrix(self, MetricSampleMatrix):
        self._MetricSampleMatrix = MetricSampleMatrix

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricSampleMatrix") is not None:
            self._MetricSampleMatrix = CustomSampleMatrix()
            self._MetricSampleMatrix._deserialize(params.get("MetricSampleMatrix"))
        self._RequestId = params.get("RequestId")


class DescribeSampleQueryRequest(AbstractModel):
    """DescribeSampleQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: job id
        :type JobId: str
        :param _ScenarioId: 场景Id
        :type ScenarioId: str
        :param _Metric: 指标名。取值范围参见 DescribeMetricLabelWithValues 接口返回的所有指标名
        :type Metric: str
        :param _Aggregation: 聚合函数。取值范围：Rate,Count,Avg,P90,P95,P99,Gauge
        :type Aggregation: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Labels: 标签过滤条件。各指标支持的标签参见 DescribeMetricLabelWithValues 接口返回的所有指标及其支持的标签
        :type Labels: list of Label
        """
        self._JobId = None
        self._ScenarioId = None
        self._Metric = None
        self._Aggregation = None
        self._ProjectId = None
        self._Labels = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Aggregation(self):
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ScenarioId = params.get("ScenarioId")
        self._Metric = params.get("Metric")
        self._Aggregation = params.get("Aggregation")
        self._ProjectId = params.get("ProjectId")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleQueryResponse(AbstractModel):
    """DescribeSampleQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricSample: 返回指标内容
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricSample: :class:`tencentcloud.pts.v20210728.models.CustomSample`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricSample = None
        self._RequestId = None

    @property
    def MetricSample(self):
        return self._MetricSample

    @MetricSample.setter
    def MetricSample(self, MetricSample):
        self._MetricSample = MetricSample

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MetricSample") is not None:
            self._MetricSample = CustomSample()
            self._MetricSample._deserialize(params.get("MetricSample"))
        self._RequestId = params.get("RequestId")


class DescribeScenarioWithJobsRequest(AbstractModel):
    """DescribeScenarioWithJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param _ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param _ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param _ScenarioName: 场景名
        :type ScenarioName: str
        :param _ScenarioStatus: 场景状态数组
        :type ScenarioStatus: int
        :param _OrderBy: 排序的列
        :type OrderBy: str
        :param _Ascend: 是否正序
        :type Ascend: bool
        :param _ScenarioRelatedJobsParams: job相关参数
        :type ScenarioRelatedJobsParams: :class:`tencentcloud.pts.v20210728.models.ScenarioRelatedJobsParams`
        :param _IgnoreScript: 是否需要返回场景的脚本内容
        :type IgnoreScript: bool
        :param _IgnoreDataset: 是否需要返回测试数据文件信息
        :type IgnoreDataset: bool
        :param _ScenarioType: 场景类型，如pts-http, pts-js, pts-trpc, pts-jmeter	
        :type ScenarioType: str
        :param _Owner: 创建人员
        :type Owner: str
        """
        self._Offset = None
        self._Limit = None
        self._ProjectIds = None
        self._ScenarioIds = None
        self._ScenarioName = None
        self._ScenarioStatus = None
        self._OrderBy = None
        self._Ascend = None
        self._ScenarioRelatedJobsParams = None
        self._IgnoreScript = None
        self._IgnoreDataset = None
        self._ScenarioType = None
        self._Owner = None

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
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ScenarioIds(self):
        return self._ScenarioIds

    @ScenarioIds.setter
    def ScenarioIds(self, ScenarioIds):
        self._ScenarioIds = ScenarioIds

    @property
    def ScenarioName(self):
        return self._ScenarioName

    @ScenarioName.setter
    def ScenarioName(self, ScenarioName):
        self._ScenarioName = ScenarioName

    @property
    def ScenarioStatus(self):
        return self._ScenarioStatus

    @ScenarioStatus.setter
    def ScenarioStatus(self, ScenarioStatus):
        self._ScenarioStatus = ScenarioStatus

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend

    @property
    def ScenarioRelatedJobsParams(self):
        return self._ScenarioRelatedJobsParams

    @ScenarioRelatedJobsParams.setter
    def ScenarioRelatedJobsParams(self, ScenarioRelatedJobsParams):
        self._ScenarioRelatedJobsParams = ScenarioRelatedJobsParams

    @property
    def IgnoreScript(self):
        return self._IgnoreScript

    @IgnoreScript.setter
    def IgnoreScript(self, IgnoreScript):
        self._IgnoreScript = IgnoreScript

    @property
    def IgnoreDataset(self):
        return self._IgnoreDataset

    @IgnoreDataset.setter
    def IgnoreDataset(self, IgnoreDataset):
        self._IgnoreDataset = IgnoreDataset

    @property
    def ScenarioType(self):
        return self._ScenarioType

    @ScenarioType.setter
    def ScenarioType(self, ScenarioType):
        self._ScenarioType = ScenarioType

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectIds = params.get("ProjectIds")
        self._ScenarioIds = params.get("ScenarioIds")
        self._ScenarioName = params.get("ScenarioName")
        self._ScenarioStatus = params.get("ScenarioStatus")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        if params.get("ScenarioRelatedJobsParams") is not None:
            self._ScenarioRelatedJobsParams = ScenarioRelatedJobsParams()
            self._ScenarioRelatedJobsParams._deserialize(params.get("ScenarioRelatedJobsParams"))
        self._IgnoreScript = params.get("IgnoreScript")
        self._IgnoreDataset = params.get("IgnoreDataset")
        self._ScenarioType = params.get("ScenarioType")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenarioWithJobsResponse(AbstractModel):
    """DescribeScenarioWithJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioWithJobsSet: 场景配置以及附带的job内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioWithJobsSet: list of ScenarioWithJobs
        :param _Total: 场景总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScenarioWithJobsSet = None
        self._Total = None
        self._RequestId = None

    @property
    def ScenarioWithJobsSet(self):
        return self._ScenarioWithJobsSet

    @ScenarioWithJobsSet.setter
    def ScenarioWithJobsSet(self, ScenarioWithJobsSet):
        self._ScenarioWithJobsSet = ScenarioWithJobsSet

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
        if params.get("ScenarioWithJobsSet") is not None:
            self._ScenarioWithJobsSet = []
            for item in params.get("ScenarioWithJobsSet"):
                obj = ScenarioWithJobs()
                obj._deserialize(item)
                self._ScenarioWithJobsSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeScenariosRequest(AbstractModel):
    """DescribeScenarios请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioIds: 场景ID数组
        :type ScenarioIds: list of str
        :param _ScenarioName: 场景名
        :type ScenarioName: str
        :param _ScenarioStatus: 场景状态数组
        :type ScenarioStatus: list of int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大为100
        :type Limit: int
        :param _OrderBy: 排序的列
        :type OrderBy: str
        :param _Ascend: 是否正序
        :type Ascend: bool
        :param _ProjectIds: 项目ID数组
        :type ProjectIds: list of str
        :param _ScenarioType: 场景类型
        :type ScenarioType: str
        """
        self._ScenarioIds = None
        self._ScenarioName = None
        self._ScenarioStatus = None
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._Ascend = None
        self._ProjectIds = None
        self._ScenarioType = None

    @property
    def ScenarioIds(self):
        return self._ScenarioIds

    @ScenarioIds.setter
    def ScenarioIds(self, ScenarioIds):
        self._ScenarioIds = ScenarioIds

    @property
    def ScenarioName(self):
        return self._ScenarioName

    @ScenarioName.setter
    def ScenarioName(self, ScenarioName):
        self._ScenarioName = ScenarioName

    @property
    def ScenarioStatus(self):
        return self._ScenarioStatus

    @ScenarioStatus.setter
    def ScenarioStatus(self, ScenarioStatus):
        self._ScenarioStatus = ScenarioStatus

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

    @property
    def ScenarioType(self):
        return self._ScenarioType

    @ScenarioType.setter
    def ScenarioType(self, ScenarioType):
        self._ScenarioType = ScenarioType


    def _deserialize(self, params):
        self._ScenarioIds = params.get("ScenarioIds")
        self._ScenarioName = params.get("ScenarioName")
        self._ScenarioStatus = params.get("ScenarioStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        self._ProjectIds = params.get("ProjectIds")
        self._ScenarioType = params.get("ScenarioType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenariosResponse(AbstractModel):
    """DescribeScenarios返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioSet: 场景列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioSet: list of Scenario
        :param _Total: 场景总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScenarioSet = None
        self._Total = None
        self._RequestId = None

    @property
    def ScenarioSet(self):
        return self._ScenarioSet

    @ScenarioSet.setter
    def ScenarioSet(self, ScenarioSet):
        self._ScenarioSet = ScenarioSet

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
        if params.get("ScenarioSet") is not None:
            self._ScenarioSet = []
            for item in params.get("ScenarioSet"):
                obj = Scenario()
                obj._deserialize(item)
                self._ScenarioSet.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DomainNameConfig(AbstractModel):
    """施压机的域名解析相关配置

    """

    def __init__(self):
        r"""
        :param _HostAliases: 域名绑定配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HostAliases: list of HostAlias
        :param _DNSConfig: DNS 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DNSConfig: :class:`tencentcloud.pts.v20210728.models.DNSConfig`
        """
        self._HostAliases = None
        self._DNSConfig = None

    @property
    def HostAliases(self):
        return self._HostAliases

    @HostAliases.setter
    def HostAliases(self, HostAliases):
        self._HostAliases = HostAliases

    @property
    def DNSConfig(self):
        return self._DNSConfig

    @DNSConfig.setter
    def DNSConfig(self, DNSConfig):
        self._DNSConfig = DNSConfig


    def _deserialize(self, params):
        if params.get("HostAliases") is not None:
            self._HostAliases = []
            for item in params.get("HostAliases"):
                obj = HostAlias()
                obj._deserialize(item)
                self._HostAliases.append(obj)
        if params.get("DNSConfig") is not None:
            self._DNSConfig = DNSConfig()
            self._DNSConfig._deserialize(params.get("DNSConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorSummary(AbstractModel):
    """错误信息汇总

    """

    def __init__(self):
        r"""
        :param _Status: 状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Result: 结果码
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _Count: 错误出现次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _Rate: 错误率
注意：此字段可能返回 null，表示取不到有效值。
        :type Rate: float
        :param _Message: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Proto: 请求协议类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Proto: str
        """
        self._Status = None
        self._Result = None
        self._Count = None
        self._Rate = None
        self._Message = None
        self._Proto = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Proto(self):
        return self._Proto

    @Proto.setter
    def Proto(self, Proto):
        self._Proto = Proto


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._Count = params.get("Count")
        self._Rate = params.get("Rate")
        self._Message = params.get("Message")
        self._Proto = params.get("Proto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class File(AbstractModel):
    """文件列表

    """

    def __init__(self):
        r"""
        :param _FileId: 文件 ID
        :type FileId: str
        :param _Kind: 文件种类，参数文件-1，协议文件-2，请求文件-3
        :type Kind: int
        :param _Name: 文件名
        :type Name: str
        :param _Size: 文件字节数
        :type Size: int
        :param _Type: 文件类型
        :type Type: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _LineCount: 文件行数
注意：此字段可能返回 null，表示取不到有效值。
        :type LineCount: int
        :param _HeadLines: 头部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadLines: list of str
        :param _TailLines: 尾部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type TailLines: list of str
        :param _HeaderInFile: 首行是否为参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderInFile: bool
        :param _HeaderColumns: 参数名数组
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderColumns: list of str
        :param _FileInfos: 文件夹中的文件
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfos: list of FileInfo
        :param _ScenarioSet: 关联场景
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioSet: list of Scenario
        :param _Status: 文件状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _ProjectId: 项目 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _AppID: 此字段不再使用
注意：此字段可能返回 null，表示取不到有效值。
        :type AppID: int
        :param _Uin: 用户主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubAccountUin: 用户子账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _AppId: 用户账号的 App ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        """
        self._FileId = None
        self._Kind = None
        self._Name = None
        self._Size = None
        self._Type = None
        self._UpdatedAt = None
        self._LineCount = None
        self._HeadLines = None
        self._TailLines = None
        self._HeaderInFile = None
        self._HeaderColumns = None
        self._FileInfos = None
        self._ScenarioSet = None
        self._Status = None
        self._CreatedAt = None
        self._ProjectId = None
        self._AppID = None
        self._Uin = None
        self._SubAccountUin = None
        self._AppId = None

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def Kind(self):
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def LineCount(self):
        return self._LineCount

    @LineCount.setter
    def LineCount(self, LineCount):
        self._LineCount = LineCount

    @property
    def HeadLines(self):
        return self._HeadLines

    @HeadLines.setter
    def HeadLines(self, HeadLines):
        self._HeadLines = HeadLines

    @property
    def TailLines(self):
        return self._TailLines

    @TailLines.setter
    def TailLines(self, TailLines):
        self._TailLines = TailLines

    @property
    def HeaderInFile(self):
        return self._HeaderInFile

    @HeaderInFile.setter
    def HeaderInFile(self, HeaderInFile):
        self._HeaderInFile = HeaderInFile

    @property
    def HeaderColumns(self):
        return self._HeaderColumns

    @HeaderColumns.setter
    def HeaderColumns(self, HeaderColumns):
        self._HeaderColumns = HeaderColumns

    @property
    def FileInfos(self):
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos

    @property
    def ScenarioSet(self):
        return self._ScenarioSet

    @ScenarioSet.setter
    def ScenarioSet(self, ScenarioSet):
        self._ScenarioSet = ScenarioSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AppID(self):
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._Kind = params.get("Kind")
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        self._UpdatedAt = params.get("UpdatedAt")
        self._LineCount = params.get("LineCount")
        self._HeadLines = params.get("HeadLines")
        self._TailLines = params.get("TailLines")
        self._HeaderInFile = params.get("HeaderInFile")
        self._HeaderColumns = params.get("HeaderColumns")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        if params.get("ScenarioSet") is not None:
            self._ScenarioSet = []
            for item in params.get("ScenarioSet"):
                obj = Scenario()
                obj._deserialize(item)
                self._ScenarioSet.append(obj)
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._ProjectId = params.get("ProjectId")
        self._AppID = params.get("AppID")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """文件基本信息

    """

    def __init__(self):
        r"""
        :param _Name: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Size: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _FileId: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        """
        self._Name = None
        self._Size = None
        self._Type = None
        self._UpdatedAt = None
        self._FileId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        self._UpdatedAt = params.get("UpdatedAt")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """指标查询过滤

    """

    def __init__(self):
        r"""
        :param _Operator: 等于：0，不等于：1
        :type Operator: int
        :param _LabelName: 标签名，可选值包括：
1. method，请求方法名；
2. proto：协议名；
3. service：服务名；
4. status：响应状态码；
5. result：响应详情；
6. check：检查名。
        :type LabelName: str
        :param _LabelValue: 标签值：
1. method：请求方法名，以 http 协议为例，method 为 GET、POST、PUT 等；
2. proto：协议名，以 http 协议为例，proto 为 HTTP/1.1、HTTP/2 等；
3. service：服务名，以 http 协议为例，service 为请求 url，如 http://httpbin.org/get 等；
4. status：响应状态码，以 http 协议为例，状态码包括 200、404、500 等；
5. result：响应详情，通过 result 判断请求成功或失败；请求正常，result 标签值为 ok；请求失败，result 标签携带错误码和描述；
6. check：检查名，标签值为用户设置的检查点名称。
        :type LabelValue: str
        """
        self._Operator = None
        self._LabelName = None
        self._LabelValue = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        self._LabelName = params.get("LabelName")
        self._LabelValue = params.get("LabelValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateTmpKeyRequest(AbstractModel):
    """GenerateTmpKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        """
        self._ProjectId = None
        self._ScenarioId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateTmpKeyResponse(AbstractModel):
    """GenerateTmpKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 临时访问凭证获取时刻的时间戳（单位秒）
        :type StartTime: int
        :param _ExpiredTime: 临时访问凭证超时 时刻的时间戳（单位秒）
        :type ExpiredTime: int
        :param _Credentials: 临时访问凭证
        :type Credentials: :class:`tencentcloud.pts.v20210728.models.Credentials`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._ExpiredTime = None
        self._Credentials = None
        self._RequestId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Credentials(self):
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class GeoRegionsLoadItem(AbstractModel):
    """压力分布配置

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _Region: 地域
        :type Region: str
        :param _Percentage: 百分比
        :type Percentage: int
        """
        self._RegionId = None
        self._Region = None
        self._Percentage = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Region = params.get("Region")
        self._Percentage = params.get("Percentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostAlias(AbstractModel):
    """施压机域名绑定配置

    """

    def __init__(self):
        r"""
        :param _HostNames: 需绑定的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type HostNames: list of str
        :param _IP: 需绑定的 IP 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        """
        self._HostNames = None
        self._IP = None

    @property
    def HostNames(self):
        return self._HostNames

    @HostNames.setter
    def HostNames(self, HostNames):
        self._HostNames = HostNames

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP


    def _deserialize(self, params):
        self._HostNames = params.get("HostNames")
        self._IP = params.get("IP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternalMetricQuery(AbstractModel):
    """查询结构封装

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名
        :type Metric: str
        :param _Aggregation: 聚合函数。取值范围：Rate,Count,Avg,P90,P95,P99,Gauge
        :type Aggregation: str
        :param _Labels: deprecated, 请使用Filters
        :type Labels: list of Label
        :param _Filters: 用标签过滤规则来过滤指标，规则中包含标签名 LabelName、标签值 LabelValue、操作符 Operator（0代表相等，1代表不等）
        :type Filters: list of Filter
        :param _GroupBy: 指标分组
        :type GroupBy: list of str
        """
        self._Metric = None
        self._Aggregation = None
        self._Labels = None
        self._Filters = None
        self._GroupBy = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Aggregation(self):
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def GroupBy(self):
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Aggregation = params.get("Aggregation")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._GroupBy = params.get("GroupBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """任务

    """

    def __init__(self):
        r"""
        :param _JobId: 任务的JobID
注意：此字段可能返回 null，表示取不到有效值。
        :type JobId: str
        :param _ScenarioId: 任务的场景ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioId: str
        :param _Load: 任务的施压配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param _Configs: 此字段不再使用
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of str
        :param _Datasets: 任务的数据集文件
注意：此字段可能返回 null，表示取不到有效值。
        :type Datasets: list of TestData
        :param _Extensions: 此字段不再使用
注意：此字段可能返回 null，表示取不到有效值。
        :type Extensions: list of str
        :param _Status: 任务的运行状态, JobUnknown: 0,JobCreated:1,JobPending:2, JobPreparing:3,JobSelectClustering:4,JobCreateTasking:5,JobSyncTasking:6
JobRunning:11,JobFinished:12,JobPrepareException:13,JobFinishException:14,JobAborting:15,JobAborted:16,JobAbortException:17,JobDeleted:18,
JobSelectClusterException:19,JobCreateTaskException:20,JobSyncTaskException:21
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StartTime: 任务的开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务的结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _MaxVirtualUserCount: 任务的最大VU数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxVirtualUserCount: int
        :param _Note: 任务的备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Note: str
        :param _ErrorRate: 错误率百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorRate: float
        :param _JobOwner: 任务发起人
注意：此字段可能返回 null，表示取不到有效值。
        :type JobOwner: str
        :param _LoadSources: 此字段不再使用
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadSources: :class:`tencentcloud.pts.v20210728.models.LoadSource`
        :param _Duration: 任务时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _MaxRequestsPerSecond: 最大每秒请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestsPerSecond: int
        :param _RequestTotal: 总请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestTotal: float
        :param _RequestsPerSecond: 平均每秒请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestsPerSecond: float
        :param _ResponseTimeAverage: 平均响应时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeAverage: float
        :param _ResponseTimeP99: 响应时间第99百分位
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeP99: float
        :param _ResponseTimeP95: 响应时间第95百分位
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeP95: float
        :param _ResponseTimeP90: 响应时间第90百分位
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeP90: float
        :param _Scripts: 此字段不再使用
注意：此字段可能返回 null，表示取不到有效值。
        :type Scripts: list of str
        :param _ResponseTimeMax: 最大响应时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeMax: float
        :param _ResponseTimeMin: 最小响应时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseTimeMin: float
        :param _LoadSourceInfos: 发压host信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadSourceInfos: list of LoadSource
        :param _TestScripts: 测试脚本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TestScripts: list of ScriptInfo
        :param _Protocols: 协议脚本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocols: list of ProtocolInfo
        :param _RequestFiles: 请求文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestFiles: list of FileInfo
        :param _Plugins: 拓展包文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Plugins: list of FileInfo
        :param _CronId: 定时任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CronId: str
        :param _Type: 场景类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _DomainNameConfig: 域名绑定配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainNameConfig: :class:`tencentcloud.pts.v20210728.models.DomainNameConfig`
        :param _Debug: false
注意：此字段可能返回 null，表示取不到有效值。
        :type Debug: bool
        :param _AbortReason: 中断原因
注意：此字段可能返回 null，表示取不到有效值。
        :type AbortReason: int
        :param _CreatedAt: 任务的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _NotificationHooks: 通知事件回调
注意：此字段可能返回 null，表示取不到有效值。
        :type NotificationHooks: list of NotificationHook
        :param _NetworkReceiveRate: 每秒接收字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkReceiveRate: float
        :param _NetworkSendRate: 每秒发送字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkSendRate: float
        :param _Message: 任务状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _ProjectName: test-project
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _ScenarioName: test-scenario
注意：此字段可能返回 null，表示取不到有效值。
        :type ScenarioName: str
        :param _PayMode: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        """
        self._JobId = None
        self._ScenarioId = None
        self._Load = None
        self._Configs = None
        self._Datasets = None
        self._Extensions = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._MaxVirtualUserCount = None
        self._Note = None
        self._ErrorRate = None
        self._JobOwner = None
        self._LoadSources = None
        self._Duration = None
        self._MaxRequestsPerSecond = None
        self._RequestTotal = None
        self._RequestsPerSecond = None
        self._ResponseTimeAverage = None
        self._ResponseTimeP99 = None
        self._ResponseTimeP95 = None
        self._ResponseTimeP90 = None
        self._Scripts = None
        self._ResponseTimeMax = None
        self._ResponseTimeMin = None
        self._LoadSourceInfos = None
        self._TestScripts = None
        self._Protocols = None
        self._RequestFiles = None
        self._Plugins = None
        self._CronId = None
        self._Type = None
        self._DomainNameConfig = None
        self._Debug = None
        self._AbortReason = None
        self._CreatedAt = None
        self._ProjectId = None
        self._NotificationHooks = None
        self._NetworkReceiveRate = None
        self._NetworkSendRate = None
        self._Message = None
        self._ProjectName = None
        self._ScenarioName = None
        self._PayMode = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Load(self):
        return self._Load

    @Load.setter
    def Load(self, Load):
        self._Load = Load

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def Datasets(self):
        return self._Datasets

    @Datasets.setter
    def Datasets(self, Datasets):
        self._Datasets = Datasets

    @property
    def Extensions(self):
        return self._Extensions

    @Extensions.setter
    def Extensions(self, Extensions):
        self._Extensions = Extensions

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def MaxVirtualUserCount(self):
        return self._MaxVirtualUserCount

    @MaxVirtualUserCount.setter
    def MaxVirtualUserCount(self, MaxVirtualUserCount):
        self._MaxVirtualUserCount = MaxVirtualUserCount

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def ErrorRate(self):
        return self._ErrorRate

    @ErrorRate.setter
    def ErrorRate(self, ErrorRate):
        self._ErrorRate = ErrorRate

    @property
    def JobOwner(self):
        return self._JobOwner

    @JobOwner.setter
    def JobOwner(self, JobOwner):
        self._JobOwner = JobOwner

    @property
    def LoadSources(self):
        return self._LoadSources

    @LoadSources.setter
    def LoadSources(self, LoadSources):
        self._LoadSources = LoadSources

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def MaxRequestsPerSecond(self):
        return self._MaxRequestsPerSecond

    @MaxRequestsPerSecond.setter
    def MaxRequestsPerSecond(self, MaxRequestsPerSecond):
        self._MaxRequestsPerSecond = MaxRequestsPerSecond

    @property
    def RequestTotal(self):
        return self._RequestTotal

    @RequestTotal.setter
    def RequestTotal(self, RequestTotal):
        self._RequestTotal = RequestTotal

    @property
    def RequestsPerSecond(self):
        return self._RequestsPerSecond

    @RequestsPerSecond.setter
    def RequestsPerSecond(self, RequestsPerSecond):
        self._RequestsPerSecond = RequestsPerSecond

    @property
    def ResponseTimeAverage(self):
        return self._ResponseTimeAverage

    @ResponseTimeAverage.setter
    def ResponseTimeAverage(self, ResponseTimeAverage):
        self._ResponseTimeAverage = ResponseTimeAverage

    @property
    def ResponseTimeP99(self):
        return self._ResponseTimeP99

    @ResponseTimeP99.setter
    def ResponseTimeP99(self, ResponseTimeP99):
        self._ResponseTimeP99 = ResponseTimeP99

    @property
    def ResponseTimeP95(self):
        return self._ResponseTimeP95

    @ResponseTimeP95.setter
    def ResponseTimeP95(self, ResponseTimeP95):
        self._ResponseTimeP95 = ResponseTimeP95

    @property
    def ResponseTimeP90(self):
        return self._ResponseTimeP90

    @ResponseTimeP90.setter
    def ResponseTimeP90(self, ResponseTimeP90):
        self._ResponseTimeP90 = ResponseTimeP90

    @property
    def Scripts(self):
        return self._Scripts

    @Scripts.setter
    def Scripts(self, Scripts):
        self._Scripts = Scripts

    @property
    def ResponseTimeMax(self):
        return self._ResponseTimeMax

    @ResponseTimeMax.setter
    def ResponseTimeMax(self, ResponseTimeMax):
        self._ResponseTimeMax = ResponseTimeMax

    @property
    def ResponseTimeMin(self):
        return self._ResponseTimeMin

    @ResponseTimeMin.setter
    def ResponseTimeMin(self, ResponseTimeMin):
        self._ResponseTimeMin = ResponseTimeMin

    @property
    def LoadSourceInfos(self):
        return self._LoadSourceInfos

    @LoadSourceInfos.setter
    def LoadSourceInfos(self, LoadSourceInfos):
        self._LoadSourceInfos = LoadSourceInfos

    @property
    def TestScripts(self):
        return self._TestScripts

    @TestScripts.setter
    def TestScripts(self, TestScripts):
        self._TestScripts = TestScripts

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def RequestFiles(self):
        return self._RequestFiles

    @RequestFiles.setter
    def RequestFiles(self, RequestFiles):
        self._RequestFiles = RequestFiles

    @property
    def Plugins(self):
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def CronId(self):
        return self._CronId

    @CronId.setter
    def CronId(self, CronId):
        self._CronId = CronId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DomainNameConfig(self):
        return self._DomainNameConfig

    @DomainNameConfig.setter
    def DomainNameConfig(self, DomainNameConfig):
        self._DomainNameConfig = DomainNameConfig

    @property
    def Debug(self):
        return self._Debug

    @Debug.setter
    def Debug(self, Debug):
        self._Debug = Debug

    @property
    def AbortReason(self):
        return self._AbortReason

    @AbortReason.setter
    def AbortReason(self, AbortReason):
        self._AbortReason = AbortReason

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def NotificationHooks(self):
        return self._NotificationHooks

    @NotificationHooks.setter
    def NotificationHooks(self, NotificationHooks):
        self._NotificationHooks = NotificationHooks

    @property
    def NetworkReceiveRate(self):
        return self._NetworkReceiveRate

    @NetworkReceiveRate.setter
    def NetworkReceiveRate(self, NetworkReceiveRate):
        self._NetworkReceiveRate = NetworkReceiveRate

    @property
    def NetworkSendRate(self):
        return self._NetworkSendRate

    @NetworkSendRate.setter
    def NetworkSendRate(self, NetworkSendRate):
        self._NetworkSendRate = NetworkSendRate

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ScenarioName(self):
        return self._ScenarioName

    @ScenarioName.setter
    def ScenarioName(self, ScenarioName):
        self._ScenarioName = ScenarioName

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ScenarioId = params.get("ScenarioId")
        if params.get("Load") is not None:
            self._Load = Load()
            self._Load._deserialize(params.get("Load"))
        self._Configs = params.get("Configs")
        if params.get("Datasets") is not None:
            self._Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self._Datasets.append(obj)
        self._Extensions = params.get("Extensions")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MaxVirtualUserCount = params.get("MaxVirtualUserCount")
        self._Note = params.get("Note")
        self._ErrorRate = params.get("ErrorRate")
        self._JobOwner = params.get("JobOwner")
        if params.get("LoadSources") is not None:
            self._LoadSources = LoadSource()
            self._LoadSources._deserialize(params.get("LoadSources"))
        self._Duration = params.get("Duration")
        self._MaxRequestsPerSecond = params.get("MaxRequestsPerSecond")
        self._RequestTotal = params.get("RequestTotal")
        self._RequestsPerSecond = params.get("RequestsPerSecond")
        self._ResponseTimeAverage = params.get("ResponseTimeAverage")
        self._ResponseTimeP99 = params.get("ResponseTimeP99")
        self._ResponseTimeP95 = params.get("ResponseTimeP95")
        self._ResponseTimeP90 = params.get("ResponseTimeP90")
        self._Scripts = params.get("Scripts")
        self._ResponseTimeMax = params.get("ResponseTimeMax")
        self._ResponseTimeMin = params.get("ResponseTimeMin")
        if params.get("LoadSourceInfos") is not None:
            self._LoadSourceInfos = []
            for item in params.get("LoadSourceInfos"):
                obj = LoadSource()
                obj._deserialize(item)
                self._LoadSourceInfos.append(obj)
        if params.get("TestScripts") is not None:
            self._TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self._TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self._Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self._Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self._RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self._RequestFiles.append(obj)
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self._Plugins.append(obj)
        self._CronId = params.get("CronId")
        self._Type = params.get("Type")
        if params.get("DomainNameConfig") is not None:
            self._DomainNameConfig = DomainNameConfig()
            self._DomainNameConfig._deserialize(params.get("DomainNameConfig"))
        self._Debug = params.get("Debug")
        self._AbortReason = params.get("AbortReason")
        self._CreatedAt = params.get("CreatedAt")
        self._ProjectId = params.get("ProjectId")
        if params.get("NotificationHooks") is not None:
            self._NotificationHooks = []
            for item in params.get("NotificationHooks"):
                obj = NotificationHook()
                obj._deserialize(item)
                self._NotificationHooks.append(obj)
        self._NetworkReceiveRate = params.get("NetworkReceiveRate")
        self._NetworkSendRate = params.get("NetworkSendRate")
        self._Message = params.get("Message")
        self._ProjectName = params.get("ProjectName")
        self._ScenarioName = params.get("ScenarioName")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """包含labelName 和labelValue

    """

    def __init__(self):
        r"""
        :param _LabelName: 标签名
        :type LabelName: str
        :param _LabelValue: 标签值
        :type LabelValue: str
        """
        self._LabelName = None
        self._LabelValue = None

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue


    def _deserialize(self, params):
        self._LabelName = params.get("LabelName")
        self._LabelValue = params.get("LabelValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LabelWithValues(AbstractModel):
    """标签及对应的值

    """

    def __init__(self):
        r"""
        :param _LabelName: 标签名称
        :type LabelName: str
        :param _LabelValues: 标签值
        :type LabelValues: list of str
        """
        self._LabelName = None
        self._LabelValues = None

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def LabelValues(self):
        return self._LabelValues

    @LabelValues.setter
    def LabelValues(self, LabelValues):
        self._LabelValues = LabelValues


    def _deserialize(self, params):
        self._LabelName = params.get("LabelName")
        self._LabelValues = params.get("LabelValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Load(AbstractModel):
    """施压配置

    """

    def __init__(self):
        r"""
        :param _LoadSpec: 施压配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadSpec: :class:`tencentcloud.pts.v20210728.models.LoadSpec`
        :param _VpcLoadDistribution: 压力来源
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcLoadDistribution: :class:`tencentcloud.pts.v20210728.models.VpcLoadDistribution`
        :param _GeoRegionsLoadDistribution: 多地域压力分布
注意：此字段可能返回 null，表示取不到有效值。
        :type GeoRegionsLoadDistribution: list of GeoRegionsLoadItem
        """
        self._LoadSpec = None
        self._VpcLoadDistribution = None
        self._GeoRegionsLoadDistribution = None

    @property
    def LoadSpec(self):
        return self._LoadSpec

    @LoadSpec.setter
    def LoadSpec(self, LoadSpec):
        self._LoadSpec = LoadSpec

    @property
    def VpcLoadDistribution(self):
        return self._VpcLoadDistribution

    @VpcLoadDistribution.setter
    def VpcLoadDistribution(self, VpcLoadDistribution):
        self._VpcLoadDistribution = VpcLoadDistribution

    @property
    def GeoRegionsLoadDistribution(self):
        return self._GeoRegionsLoadDistribution

    @GeoRegionsLoadDistribution.setter
    def GeoRegionsLoadDistribution(self, GeoRegionsLoadDistribution):
        self._GeoRegionsLoadDistribution = GeoRegionsLoadDistribution


    def _deserialize(self, params):
        if params.get("LoadSpec") is not None:
            self._LoadSpec = LoadSpec()
            self._LoadSpec._deserialize(params.get("LoadSpec"))
        if params.get("VpcLoadDistribution") is not None:
            self._VpcLoadDistribution = VpcLoadDistribution()
            self._VpcLoadDistribution._deserialize(params.get("VpcLoadDistribution"))
        if params.get("GeoRegionsLoadDistribution") is not None:
            self._GeoRegionsLoadDistribution = []
            for item in params.get("GeoRegionsLoadDistribution"):
                obj = GeoRegionsLoadItem()
                obj._deserialize(item)
                self._GeoRegionsLoadDistribution.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadSource(AbstractModel):
    """发压host来源

    """

    def __init__(self):
        r"""
        :param _IP: 发压host的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _PodName: 发压host所在的pod
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param _Region: 所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._IP = None
        self._PodName = None
        self._Region = None

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._PodName = params.get("PodName")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadSpec(AbstractModel):
    """施压配置

    """

    def __init__(self):
        r"""
        :param _Concurrency: 并发施压模式的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Concurrency: :class:`tencentcloud.pts.v20210728.models.Concurrency`
        :param _RequestsPerSecond: RPS施压模式的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestsPerSecond: :class:`tencentcloud.pts.v20210728.models.RequestsPerSecond`
        :param _ScriptOrigin: 脚本内置压力模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptOrigin: :class:`tencentcloud.pts.v20210728.models.ScriptOrigin`
        """
        self._Concurrency = None
        self._RequestsPerSecond = None
        self._ScriptOrigin = None

    @property
    def Concurrency(self):
        return self._Concurrency

    @Concurrency.setter
    def Concurrency(self, Concurrency):
        self._Concurrency = Concurrency

    @property
    def RequestsPerSecond(self):
        return self._RequestsPerSecond

    @RequestsPerSecond.setter
    def RequestsPerSecond(self, RequestsPerSecond):
        self._RequestsPerSecond = RequestsPerSecond

    @property
    def ScriptOrigin(self):
        return self._ScriptOrigin

    @ScriptOrigin.setter
    def ScriptOrigin(self, ScriptOrigin):
        self._ScriptOrigin = ScriptOrigin


    def _deserialize(self, params):
        if params.get("Concurrency") is not None:
            self._Concurrency = Concurrency()
            self._Concurrency._deserialize(params.get("Concurrency"))
        if params.get("RequestsPerSecond") is not None:
            self._RequestsPerSecond = RequestsPerSecond()
            self._RequestsPerSecond._deserialize(params.get("RequestsPerSecond"))
        if params.get("ScriptOrigin") is not None:
            self._ScriptOrigin = ScriptOrigin()
            self._ScriptOrigin._deserialize(params.get("ScriptOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricInfo(AbstractModel):
    """指标结构

    """

    def __init__(self):
        r"""
        :param _Metric: 后台指标
        :type Metric: str
        :param _Alias: 前台展示指标名称
        :type Alias: str
        :param _Description: 指标描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _MetricType: 指标类型
        :type MetricType: str
        :param _Unit: 默认指标单位
        :type Unit: str
        :param _Aggregations: 指标支持的聚合函数
        :type Aggregations: list of AggregationLegend
        :param _InnerMetric: 是否内部指标，内部指标不可在前台提供用户自由选择
        :type InnerMetric: bool
        """
        self._Metric = None
        self._Alias = None
        self._Description = None
        self._MetricType = None
        self._Unit = None
        self._Aggregations = None
        self._InnerMetric = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MetricType(self):
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Aggregations(self):
        return self._Aggregations

    @Aggregations.setter
    def Aggregations(self, Aggregations):
        self._Aggregations = Aggregations

    @property
    def InnerMetric(self):
        return self._InnerMetric

    @InnerMetric.setter
    def InnerMetric(self, InnerMetric):
        self._InnerMetric = InnerMetric


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Alias = params.get("Alias")
        self._Description = params.get("Description")
        self._MetricType = params.get("MetricType")
        self._Unit = params.get("Unit")
        if params.get("Aggregations") is not None:
            self._Aggregations = []
            for item in params.get("Aggregations"):
                obj = AggregationLegend()
                obj._deserialize(item)
                self._Aggregations.append(obj)
        self._InnerMetric = params.get("InnerMetric")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricLabelWithValues(AbstractModel):
    """PTS提供的指标名，指标对应的labels及values

    """

    def __init__(self):
        r"""
        :param _MetricName: metric 名字
        :type MetricName: str
        :param _LabelValuesSet: label及values 数组
        :type LabelValuesSet: list of LabelWithValues
        """
        self._MetricName = None
        self._LabelValuesSet = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def LabelValuesSet(self):
        return self._LabelValuesSet

    @LabelValuesSet.setter
    def LabelValuesSet(self, LabelValuesSet):
        self._LabelValuesSet = LabelValuesSet


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        if params.get("LabelValuesSet") is not None:
            self._LabelValuesSet = []
            for item in params.get("LabelValuesSet"):
                obj = LabelWithValues()
                obj._deserialize(item)
                self._LabelValuesSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NormalLog(AbstractModel):
    """通用日志

    """

    def __init__(self):
        r"""
        :param _Timestamp: 毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _SeverityText: 日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type SeverityText: str
        :param _Body: 日志输出内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        """
        self._Timestamp = None
        self._SeverityText = None
        self._Body = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SeverityText(self):
        return self._SeverityText

    @SeverityText.setter
    def SeverityText(self, SeverityText):
        self._SeverityText = SeverityText

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._SeverityText = params.get("SeverityText")
        self._Body = params.get("Body")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Notification(AbstractModel):
    """测试启动前后的消息通知

    """

    def __init__(self):
        r"""
        :param _Events: 发生事件
        :type Events: list of str
        :param _URL: webhook的网址
        :type URL: str
        """
        self._Events = None
        self._URL = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL


    def _deserialize(self, params):
        self._Events = params.get("Events")
        self._URL = params.get("URL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotificationHook(AbstractModel):
    """事件通知回调

    """

    def __init__(self):
        r"""
        :param _Events: 通知事件
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of str
        :param _URL: 回调 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        """
        self._Events = None
        self._URL = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL


    def _deserialize(self, params):
        self._Events = params.get("Events")
        self._URL = params.get("URL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    """项目

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Name: 项目名
        :type Name: str
        :param _Description: 项目描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Tags: 标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagSpec
        :param _Status: 项目状态
        :type Status: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 修改时间
        :type UpdatedAt: str
        :param _AppId: App ID
        :type AppId: int
        :param _Uin: 用户ID
        :type Uin: str
        :param _SubAccountUin: 子用户ID
        :type SubAccountUin: str
        """
        self._ProjectId = None
        self._Name = None
        self._Description = None
        self._Tags = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._AppId = None
        self._Uin = None
        self._SubAccountUin = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpec()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolInfo(AbstractModel):
    """协议文件详情

    """

    def __init__(self):
        r"""
        :param _Name: 协议详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Size: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _FileId: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        """
        self._Name = None
        self._Size = None
        self._Type = None
        self._UpdatedAt = None
        self._FileId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        self._UpdatedAt = params.get("UpdatedAt")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReactionTimeRange(AbstractModel):
    """采用日志响应时间RT范围

    """

    def __init__(self):
        r"""
        :param _Min: 最小响应时间，单位ms
        :type Min: str
        :param _Max: 最大响应时间，单位ms
        :type Max: str
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionDetail(AbstractModel):
    """地域

    """

    def __init__(self):
        r"""
        :param _Region: 地域代码
        :type Region: str
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _Area: 地域所在的地区
        :type Area: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _RegionState: 地域状态
        :type RegionState: int
        :param _RegionShortName: 地域简称
        :type RegionShortName: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        """
        self._Region = None
        self._RegionId = None
        self._Area = None
        self._RegionName = None
        self._RegionState = None
        self._RegionShortName = None
        self._CreatedAt = None
        self._UpdatedAt = None

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
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def RegionShortName(self):
        return self._RegionShortName

    @RegionShortName.setter
    def RegionShortName(self, RegionShortName):
        self._RegionShortName = RegionShortName

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionId = params.get("RegionId")
        self._Area = params.get("Area")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        self._RegionShortName = params.get("RegionShortName")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestSummary(AbstractModel):
    """压测请求明细

    """

    def __init__(self):
        r"""
        :param _Service: 请求URL
        :type Service: str
        :param _Method: 请求方法
        :type Method: str
        :param _Count: 请求次数
        :type Count: int
        :param _Average: 请求响应平均耗时，单位秒
        :type Average: float
        :param _P90: 请求p90耗时，单位秒
        :type P90: float
        :param _P95: 请求p95耗时，单位秒
        :type P95: float
        :param _Min: 请求最小耗时，单位秒
        :type Min: float
        :param _Max: 请求最大耗时，单位秒
        :type Max: float
        :param _ErrorPercentage: 请求错误率
        :type ErrorPercentage: float
        :param _P99: 请求p99耗时，单位秒
        :type P99: float
        :param _Status: 响应状态码
        :type Status: str
        :param _Result: 响应详情
        :type Result: str
        """
        self._Service = None
        self._Method = None
        self._Count = None
        self._Average = None
        self._P90 = None
        self._P95 = None
        self._Min = None
        self._Max = None
        self._ErrorPercentage = None
        self._P99 = None
        self._Status = None
        self._Result = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Average(self):
        return self._Average

    @Average.setter
    def Average(self, Average):
        self._Average = Average

    @property
    def P90(self):
        return self._P90

    @P90.setter
    def P90(self, P90):
        self._P90 = P90

    @property
    def P95(self):
        return self._P95

    @P95.setter
    def P95(self, P95):
        self._P95 = P95

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max

    @property
    def ErrorPercentage(self):
        return self._ErrorPercentage

    @ErrorPercentage.setter
    def ErrorPercentage(self, ErrorPercentage):
        self._ErrorPercentage = ErrorPercentage

    @property
    def P99(self):
        return self._P99

    @P99.setter
    def P99(self, P99):
        self._P99 = P99

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._Method = params.get("Method")
        self._Count = params.get("Count")
        self._Average = params.get("Average")
        self._P90 = params.get("P90")
        self._P95 = params.get("P95")
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        self._ErrorPercentage = params.get("ErrorPercentage")
        self._P99 = params.get("P99")
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestsPerSecond(AbstractModel):
    """RPS模式的施压配置

    """

    def __init__(self):
        r"""
        :param _MaxRequestsPerSecond: 最大RPS
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestsPerSecond: int
        :param _DurationSeconds: 施压时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationSeconds: int
        :param _TargetVirtualUsers: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetVirtualUsers: int
        :param _Resources: 资源数
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: int
        :param _StartRequestsPerSecond: 起始RPS
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRequestsPerSecond: int
        :param _TargetRequestsPerSecond: 目标RPS，入参无效
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetRequestsPerSecond: int
        :param _GracefulStopSeconds: 优雅关停的等待时间
注意：此字段可能返回 null，表示取不到有效值。
        :type GracefulStopSeconds: int
        """
        self._MaxRequestsPerSecond = None
        self._DurationSeconds = None
        self._TargetVirtualUsers = None
        self._Resources = None
        self._StartRequestsPerSecond = None
        self._TargetRequestsPerSecond = None
        self._GracefulStopSeconds = None

    @property
    def MaxRequestsPerSecond(self):
        return self._MaxRequestsPerSecond

    @MaxRequestsPerSecond.setter
    def MaxRequestsPerSecond(self, MaxRequestsPerSecond):
        self._MaxRequestsPerSecond = MaxRequestsPerSecond

    @property
    def DurationSeconds(self):
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds

    @property
    def TargetVirtualUsers(self):
        return self._TargetVirtualUsers

    @TargetVirtualUsers.setter
    def TargetVirtualUsers(self, TargetVirtualUsers):
        self._TargetVirtualUsers = TargetVirtualUsers

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def StartRequestsPerSecond(self):
        return self._StartRequestsPerSecond

    @StartRequestsPerSecond.setter
    def StartRequestsPerSecond(self, StartRequestsPerSecond):
        self._StartRequestsPerSecond = StartRequestsPerSecond

    @property
    def TargetRequestsPerSecond(self):
        return self._TargetRequestsPerSecond

    @TargetRequestsPerSecond.setter
    def TargetRequestsPerSecond(self, TargetRequestsPerSecond):
        self._TargetRequestsPerSecond = TargetRequestsPerSecond

    @property
    def GracefulStopSeconds(self):
        return self._GracefulStopSeconds

    @GracefulStopSeconds.setter
    def GracefulStopSeconds(self, GracefulStopSeconds):
        self._GracefulStopSeconds = GracefulStopSeconds


    def _deserialize(self, params):
        self._MaxRequestsPerSecond = params.get("MaxRequestsPerSecond")
        self._DurationSeconds = params.get("DurationSeconds")
        self._TargetVirtualUsers = params.get("TargetVirtualUsers")
        self._Resources = params.get("Resources")
        self._StartRequestsPerSecond = params.get("StartRequestsPerSecond")
        self._TargetRequestsPerSecond = params.get("TargetRequestsPerSecond")
        self._GracefulStopSeconds = params.get("GracefulStopSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartCronJobsRequest(AbstractModel):
    """RestartCronJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CronJobIds: 定时任务ID数组
        :type CronJobIds: list of str
        """
        self._ProjectId = None
        self._CronJobIds = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CronJobIds(self):
        return self._CronJobIds

    @CronJobIds.setter
    def CronJobIds(self, CronJobIds):
        self._CronJobIds = CronJobIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CronJobIds = params.get("CronJobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartCronJobsResponse(AbstractModel):
    """RestartCronJobs返回参数结构体

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


class SLALabel(AbstractModel):
    """SLA 标签

    """

    def __init__(self):
        r"""
        :param _LabelName: 标签名
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        :param _LabelValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        """
        self._LabelName = None
        self._LabelValue = None

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue


    def _deserialize(self, params):
        self._LabelName = params.get("LabelName")
        self._LabelValue = params.get("LabelValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SLAPolicy(AbstractModel):
    """SLA 策略

    """

    def __init__(self):
        r"""
        :param _SLARules: SLA 规则
注意：此字段可能返回 null，表示取不到有效值。
        :type SLARules: list of SLARule
        :param _AlertChannel: 告警通知渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertChannel: :class:`tencentcloud.pts.v20210728.models.AlertChannel`
        """
        self._SLARules = None
        self._AlertChannel = None

    @property
    def SLARules(self):
        return self._SLARules

    @SLARules.setter
    def SLARules(self, SLARules):
        self._SLARules = SLARules

    @property
    def AlertChannel(self):
        return self._AlertChannel

    @AlertChannel.setter
    def AlertChannel(self, AlertChannel):
        self._AlertChannel = AlertChannel


    def _deserialize(self, params):
        if params.get("SLARules") is not None:
            self._SLARules = []
            for item in params.get("SLARules"):
                obj = SLARule()
                obj._deserialize(item)
                self._SLARules.append(obj)
        if params.get("AlertChannel") is not None:
            self._AlertChannel = AlertChannel()
            self._AlertChannel._deserialize(params.get("AlertChannel"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SLARule(AbstractModel):
    """SLA 规则

    """

    def __init__(self):
        r"""
        :param _Metric: 压测指标
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param _Aggregation: 压测指标聚合方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Aggregation: str
        :param _Condition: 压测指标条件判断符号
注意：此字段可能返回 null，表示取不到有效值。
        :type Condition: str
        :param _Value: 阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        :param _LabelFilter: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelFilter: list of SLALabel
        :param _AbortFlag: 是否停止压测任务
注意：此字段可能返回 null，表示取不到有效值。
        :type AbortFlag: bool
        :param _For: 持续时长
注意：此字段可能返回 null，表示取不到有效值。
        :type For: str
        """
        self._Metric = None
        self._Aggregation = None
        self._Condition = None
        self._Value = None
        self._LabelFilter = None
        self._AbortFlag = None
        self._For = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Aggregation(self):
        return self._Aggregation

    @Aggregation.setter
    def Aggregation(self, Aggregation):
        self._Aggregation = Aggregation

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def LabelFilter(self):
        return self._LabelFilter

    @LabelFilter.setter
    def LabelFilter(self, LabelFilter):
        self._LabelFilter = LabelFilter

    @property
    def AbortFlag(self):
        return self._AbortFlag

    @AbortFlag.setter
    def AbortFlag(self, AbortFlag):
        self._AbortFlag = AbortFlag

    @property
    def For(self):
        return self._For

    @For.setter
    def For(self, For):
        self._For = For


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        self._Aggregation = params.get("Aggregation")
        self._Condition = params.get("Condition")
        self._Value = params.get("Value")
        if params.get("LabelFilter") is not None:
            self._LabelFilter = []
            for item in params.get("LabelFilter"):
                obj = SLALabel()
                obj._deserialize(item)
                self._LabelFilter.append(obj)
        self._AbortFlag = params.get("AbortFlag")
        self._For = params.get("For")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleLog(AbstractModel):
    """采样日志

    """

    def __init__(self):
        r"""
        :param _Timestamp: 日志毫秒时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Attributes: 采样日志属性
注意：此字段可能返回 null，表示取不到有效值。
        :type Attributes: :class:`tencentcloud.pts.v20210728.models.Attributes`
        :param _Body: har格式的采样请求
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        """
        self._Timestamp = None
        self._Attributes = None
        self._Body = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Attributes(self):
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("Attributes") is not None:
            self._Attributes = Attributes()
            self._Attributes._deserialize(params.get("Attributes"))
        self._Body = params.get("Body")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SamplePair(AbstractModel):
    """sample采样值

    """

    def __init__(self):
        r"""
        :param _Timestamp: is the number of milliseconds since the epoch (1970-01-01 00:00 UTC) excluding leap seconds.
        :type Timestamp: int
        :param _Value: is a representation of a value for a given sample at a given time.
        :type Value: float
        """
        self._Timestamp = None
        self._Value = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleStream(AbstractModel):
    """连续指标采样内容

    """

    def __init__(self):
        r"""
        :param _Labels: labels描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param _Values: 指标采样数组
        :type Values: list of SamplePair
        :param _Name: 指标序列名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._Labels = None
        self._Values = None
        self._Name = None

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = SamplePair()
                obj._deserialize(item)
                self._Values.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Scenario(AbstractModel):
    """场景列表

    """

    def __init__(self):
        r"""
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _Name: 场景名
        :type Name: str
        :param _Description: 场景描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Type: 场景类型，如pts-http, pts-js, pts-trpc, pts-jmeter
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status: 场景状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Load: 施压配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param _EncodedScripts: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type EncodedScripts: str
        :param _Configs: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type Configs: list of str
        :param _Extensions: deprecated
注意：此字段可能返回 null，表示取不到有效值。
        :type Extensions: list of str
        :param _Datasets: 测试数据集
注意：此字段可能返回 null，表示取不到有效值。
        :type Datasets: list of TestData
        :param _SLAId: SLA规则的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SLAId: str
        :param _CronId: Cron Job规则的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CronId: str
        :param _CreatedAt: 场景创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 场景修改时间
        :type UpdatedAt: str
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _AppId: App ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _Uin: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubAccountUin: 子用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountUin: str
        :param _TestScripts: 测试脚本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TestScripts: list of ScriptInfo
        :param _Protocols: 协议文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocols: list of ProtocolInfo
        :param _RequestFiles: 请求文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestFiles: list of FileInfo
        :param _SLAPolicy: SLA 策略
注意：此字段可能返回 null，表示取不到有效值。
        :type SLAPolicy: :class:`tencentcloud.pts.v20210728.models.SLAPolicy`
        :param _Plugins: 扩展包信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Plugins: list of FileInfo
        :param _DomainNameConfig: 域名解析配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainNameConfig: :class:`tencentcloud.pts.v20210728.models.DomainNameConfig`
        :param _NotificationHooks: 通知事件回调
注意：此字段可能返回 null，表示取不到有效值。
        :type NotificationHooks: list of NotificationHook
        :param _Owner: 创建人员
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param _ProjectName: 场景所在的项目的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        """
        self._ScenarioId = None
        self._Name = None
        self._Description = None
        self._Type = None
        self._Status = None
        self._Load = None
        self._EncodedScripts = None
        self._Configs = None
        self._Extensions = None
        self._Datasets = None
        self._SLAId = None
        self._CronId = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._ProjectId = None
        self._AppId = None
        self._Uin = None
        self._SubAccountUin = None
        self._TestScripts = None
        self._Protocols = None
        self._RequestFiles = None
        self._SLAPolicy = None
        self._Plugins = None
        self._DomainNameConfig = None
        self._NotificationHooks = None
        self._Owner = None
        self._ProjectName = None

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Load(self):
        return self._Load

    @Load.setter
    def Load(self, Load):
        self._Load = Load

    @property
    def EncodedScripts(self):
        return self._EncodedScripts

    @EncodedScripts.setter
    def EncodedScripts(self, EncodedScripts):
        self._EncodedScripts = EncodedScripts

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def Extensions(self):
        return self._Extensions

    @Extensions.setter
    def Extensions(self, Extensions):
        self._Extensions = Extensions

    @property
    def Datasets(self):
        return self._Datasets

    @Datasets.setter
    def Datasets(self, Datasets):
        self._Datasets = Datasets

    @property
    def SLAId(self):
        return self._SLAId

    @SLAId.setter
    def SLAId(self, SLAId):
        self._SLAId = SLAId

    @property
    def CronId(self):
        return self._CronId

    @CronId.setter
    def CronId(self, CronId):
        self._CronId = CronId

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def TestScripts(self):
        return self._TestScripts

    @TestScripts.setter
    def TestScripts(self, TestScripts):
        self._TestScripts = TestScripts

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def RequestFiles(self):
        return self._RequestFiles

    @RequestFiles.setter
    def RequestFiles(self, RequestFiles):
        self._RequestFiles = RequestFiles

    @property
    def SLAPolicy(self):
        return self._SLAPolicy

    @SLAPolicy.setter
    def SLAPolicy(self, SLAPolicy):
        self._SLAPolicy = SLAPolicy

    @property
    def Plugins(self):
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def DomainNameConfig(self):
        return self._DomainNameConfig

    @DomainNameConfig.setter
    def DomainNameConfig(self, DomainNameConfig):
        self._DomainNameConfig = DomainNameConfig

    @property
    def NotificationHooks(self):
        return self._NotificationHooks

    @NotificationHooks.setter
    def NotificationHooks(self, NotificationHooks):
        self._NotificationHooks = NotificationHooks

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._ScenarioId = params.get("ScenarioId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        if params.get("Load") is not None:
            self._Load = Load()
            self._Load._deserialize(params.get("Load"))
        self._EncodedScripts = params.get("EncodedScripts")
        self._Configs = params.get("Configs")
        self._Extensions = params.get("Extensions")
        if params.get("Datasets") is not None:
            self._Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self._Datasets.append(obj)
        self._SLAId = params.get("SLAId")
        self._CronId = params.get("CronId")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._ProjectId = params.get("ProjectId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        if params.get("TestScripts") is not None:
            self._TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self._TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self._Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self._Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self._RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self._RequestFiles.append(obj)
        if params.get("SLAPolicy") is not None:
            self._SLAPolicy = SLAPolicy()
            self._SLAPolicy._deserialize(params.get("SLAPolicy"))
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self._Plugins.append(obj)
        if params.get("DomainNameConfig") is not None:
            self._DomainNameConfig = DomainNameConfig()
            self._DomainNameConfig._deserialize(params.get("DomainNameConfig"))
        if params.get("NotificationHooks") is not None:
            self._NotificationHooks = []
            for item in params.get("NotificationHooks"):
                obj = NotificationHook()
                obj._deserialize(item)
                self._NotificationHooks.append(obj)
        self._Owner = params.get("Owner")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScenarioRelatedJobsParams(AbstractModel):
    """查询与特定scenario关联的job的参数

    """

    def __init__(self):
        r"""
        :param _Offset: job偏移量
        :type Offset: int
        :param _Limit: 限制最多查询的job数
        :type Limit: int
        :param _OrderBy: 排序字段
        :type OrderBy: str
        :param _Ascend: 是否升序
        :type Ascend: bool
        """
        self._Offset = None
        self._Limit = None
        self._OrderBy = None
        self._Ascend = None

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
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Ascend(self):
        return self._Ascend

    @Ascend.setter
    def Ascend(self, Ascend):
        self._Ascend = Ascend


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderBy = params.get("OrderBy")
        self._Ascend = params.get("Ascend")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScenarioWithJobs(AbstractModel):
    """带已执行任务的scenario

    """

    def __init__(self):
        r"""
        :param _Scenario: scecario结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Scenario: :class:`tencentcloud.pts.v20210728.models.Scenario`
        :param _Jobs: job结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Jobs: list of Job
        """
        self._Scenario = None
        self._Jobs = None

    @property
    def Scenario(self):
        return self._Scenario

    @Scenario.setter
    def Scenario(self, Scenario):
        self._Scenario = Scenario

    @property
    def Jobs(self):
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs


    def _deserialize(self, params):
        if params.get("Scenario") is not None:
            self._Scenario = Scenario()
            self._Scenario._deserialize(params.get("Scenario"))
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = Job()
                obj._deserialize(item)
                self._Jobs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScriptInfo(AbstractModel):
    """脚本信息

    """

    def __init__(self):
        r"""
        :param _Name: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Size: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _EncodedContent: base64编码后的文件内容
注意：此字段可能返回 null，表示取不到有效值。
        :type EncodedContent: str
        :param _EncodedHttpArchive: base64编码后的har结构体
注意：此字段可能返回 null，表示取不到有效值。
        :type EncodedHttpArchive: str
        :param _LoadWeight: 脚本权重，范围 1-100
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadWeight: int
        :param _FileId: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        """
        self._Name = None
        self._Size = None
        self._Type = None
        self._UpdatedAt = None
        self._EncodedContent = None
        self._EncodedHttpArchive = None
        self._LoadWeight = None
        self._FileId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def EncodedContent(self):
        return self._EncodedContent

    @EncodedContent.setter
    def EncodedContent(self, EncodedContent):
        self._EncodedContent = EncodedContent

    @property
    def EncodedHttpArchive(self):
        return self._EncodedHttpArchive

    @EncodedHttpArchive.setter
    def EncodedHttpArchive(self, EncodedHttpArchive):
        self._EncodedHttpArchive = EncodedHttpArchive

    @property
    def LoadWeight(self):
        return self._LoadWeight

    @LoadWeight.setter
    def LoadWeight(self, LoadWeight):
        self._LoadWeight = LoadWeight

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Size = params.get("Size")
        self._Type = params.get("Type")
        self._UpdatedAt = params.get("UpdatedAt")
        self._EncodedContent = params.get("EncodedContent")
        self._EncodedHttpArchive = params.get("EncodedHttpArchive")
        self._LoadWeight = params.get("LoadWeight")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScriptOrigin(AbstractModel):
    """脚本内置压力模型

    """

    def __init__(self):
        r"""
        :param _MachineNumber: 机器数量
        :type MachineNumber: int
        :param _MachineSpecification: 机器规格
        :type MachineSpecification: str
        :param _DurationSeconds: 压测时长
        :type DurationSeconds: int
        """
        self._MachineNumber = None
        self._MachineSpecification = None
        self._DurationSeconds = None

    @property
    def MachineNumber(self):
        return self._MachineNumber

    @MachineNumber.setter
    def MachineNumber(self, MachineNumber):
        self._MachineNumber = MachineNumber

    @property
    def MachineSpecification(self):
        return self._MachineSpecification

    @MachineSpecification.setter
    def MachineSpecification(self, MachineSpecification):
        self._MachineSpecification = MachineSpecification

    @property
    def DurationSeconds(self):
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._MachineNumber = params.get("MachineNumber")
        self._MachineSpecification = params.get("MachineSpecification")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Stage(AbstractModel):
    """分阶段施压时，对单个阶段的配置

    """

    def __init__(self):
        r"""
        :param _DurationSeconds: 施压时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DurationSeconds: int
        :param _TargetVirtualUsers: 虚拟用户数
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetVirtualUsers: int
        """
        self._DurationSeconds = None
        self._TargetVirtualUsers = None

    @property
    def DurationSeconds(self):
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds

    @property
    def TargetVirtualUsers(self):
        return self._TargetVirtualUsers

    @TargetVirtualUsers.setter
    def TargetVirtualUsers(self, TargetVirtualUsers):
        self._TargetVirtualUsers = TargetVirtualUsers


    def _deserialize(self, params):
        self._DurationSeconds = params.get("DurationSeconds")
        self._TargetVirtualUsers = params.get("TargetVirtualUsers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartJobRequest(AbstractModel):
    """StartJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _JobOwner: 任务发起人
        :type JobOwner: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Debug: 是否调试
        :type Debug: bool
        :param _Note: 备注
        :type Note: str
        """
        self._ScenarioId = None
        self._JobOwner = None
        self._ProjectId = None
        self._Debug = None
        self._Note = None

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def JobOwner(self):
        return self._JobOwner

    @JobOwner.setter
    def JobOwner(self, JobOwner):
        self._JobOwner = JobOwner

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Debug(self):
        return self._Debug

    @Debug.setter
    def Debug(self, Debug):
        self._Debug = Debug

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._ScenarioId = params.get("ScenarioId")
        self._JobOwner = params.get("JobOwner")
        self._ProjectId = params.get("ProjectId")
        self._Debug = params.get("Debug")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartJobResponse(AbstractModel):
    """StartJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class TagSpec(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class TestData(AbstractModel):
    """测试数据集

    """

    def __init__(self):
        r"""
        :param _Name: 测试数据集所在的文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Split: 测试数据集是否分片
注意：此字段可能返回 null，表示取不到有效值。
        :type Split: bool
        :param _HeaderInFile: 首行是否为参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderInFile: bool
        :param _HeaderColumns: 参数名数组
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderColumns: list of str
        :param _LineCount: 文件行数
注意：此字段可能返回 null，表示取不到有效值。
        :type LineCount: int
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _Size: 文件字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type Size: int
        :param _HeadLines: 头部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type HeadLines: list of str
        :param _TailLines: 尾部数据行
注意：此字段可能返回 null，表示取不到有效值。
        :type TailLines: list of str
        :param _Type: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _FileId: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        """
        self._Name = None
        self._Split = None
        self._HeaderInFile = None
        self._HeaderColumns = None
        self._LineCount = None
        self._UpdatedAt = None
        self._Size = None
        self._HeadLines = None
        self._TailLines = None
        self._Type = None
        self._FileId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Split(self):
        return self._Split

    @Split.setter
    def Split(self, Split):
        self._Split = Split

    @property
    def HeaderInFile(self):
        return self._HeaderInFile

    @HeaderInFile.setter
    def HeaderInFile(self, HeaderInFile):
        self._HeaderInFile = HeaderInFile

    @property
    def HeaderColumns(self):
        return self._HeaderColumns

    @HeaderColumns.setter
    def HeaderColumns(self, HeaderColumns):
        self._HeaderColumns = HeaderColumns

    @property
    def LineCount(self):
        return self._LineCount

    @LineCount.setter
    def LineCount(self, LineCount):
        self._LineCount = LineCount

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def HeadLines(self):
        return self._HeadLines

    @HeadLines.setter
    def HeadLines(self, HeadLines):
        self._HeadLines = HeadLines

    @property
    def TailLines(self):
        return self._TailLines

    @TailLines.setter
    def TailLines(self, TailLines):
        self._TailLines = TailLines

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Split = params.get("Split")
        self._HeaderInFile = params.get("HeaderInFile")
        self._HeaderColumns = params.get("HeaderColumns")
        self._LineCount = params.get("LineCount")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Size = params.get("Size")
        self._HeadLines = params.get("HeadLines")
        self._TailLines = params.get("TailLines")
        self._Type = params.get("Type")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCronJobRequest(AbstractModel):
    """UpdateCronJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _CronJobId: 定时任务ID
        :type CronJobId: str
        :param _Note: 备注
        :type Note: str
        :param _CronExpression: cron表达式
        :type CronExpression: str
        :param _FrequencyType: 执行频率类型，1:只执行一次; 2:日粒度; 3:周粒度; 4:高级
        :type FrequencyType: int
        :param _Name: 定时任务名字
        :type Name: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _ScenarioName: 场景名称
        :type ScenarioName: str
        :param _JobOwner: 任务发起人
        :type JobOwner: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _NoticeId: Notice ID
        :type NoticeId: str
        """
        self._ProjectId = None
        self._CronJobId = None
        self._Note = None
        self._CronExpression = None
        self._FrequencyType = None
        self._Name = None
        self._ScenarioId = None
        self._ScenarioName = None
        self._JobOwner = None
        self._EndTime = None
        self._NoticeId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CronJobId(self):
        return self._CronJobId

    @CronJobId.setter
    def CronJobId(self, CronJobId):
        self._CronJobId = CronJobId

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def CronExpression(self):
        return self._CronExpression

    @CronExpression.setter
    def CronExpression(self, CronExpression):
        self._CronExpression = CronExpression

    @property
    def FrequencyType(self):
        return self._FrequencyType

    @FrequencyType.setter
    def FrequencyType(self, FrequencyType):
        self._FrequencyType = FrequencyType

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def ScenarioName(self):
        return self._ScenarioName

    @ScenarioName.setter
    def ScenarioName(self, ScenarioName):
        self._ScenarioName = ScenarioName

    @property
    def JobOwner(self):
        return self._JobOwner

    @JobOwner.setter
    def JobOwner(self, JobOwner):
        self._JobOwner = JobOwner

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NoticeId(self):
        return self._NoticeId

    @NoticeId.setter
    def NoticeId(self, NoticeId):
        self._NoticeId = NoticeId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CronJobId = params.get("CronJobId")
        self._Note = params.get("Note")
        self._CronExpression = params.get("CronExpression")
        self._FrequencyType = params.get("FrequencyType")
        self._Name = params.get("Name")
        self._ScenarioId = params.get("ScenarioId")
        self._ScenarioName = params.get("ScenarioName")
        self._JobOwner = params.get("JobOwner")
        self._EndTime = params.get("EndTime")
        self._NoticeId = params.get("NoticeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCronJobResponse(AbstractModel):
    """UpdateCronJob返回参数结构体

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


class UpdateEnvironmentRequest(AbstractModel):
    """UpdateEnvironment请求参数结构体

    """


class UpdateEnvironmentResponse(AbstractModel):
    """UpdateEnvironment返回参数结构体

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


class UpdateFileScenarioRelationRequest(AbstractModel):
    """UpdateFileScenarioRelation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileId: 文件 ID。其值应为前序步骤上传该文件到 cos 桶后，文件在 cos 桶中的相应目录
        :type FileId: str
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _ScenarioIds: 场景 ID 数组
        :type ScenarioIds: list of str
        """
        self._FileId = None
        self._ProjectId = None
        self._ScenarioIds = None

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioIds(self):
        return self._ScenarioIds

    @ScenarioIds.setter
    def ScenarioIds(self, ScenarioIds):
        self._ScenarioIds = ScenarioIds


    def _deserialize(self, params):
        self._FileId = params.get("FileId")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioIds = params.get("ScenarioIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFileScenarioRelationResponse(AbstractModel):
    """UpdateFileScenarioRelation返回参数结构体

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


class UpdateJobRequest(AbstractModel):
    """UpdateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _Note: 任务备注信息
        :type Note: str
        """
        self._JobId = None
        self._ProjectId = None
        self._ScenarioId = None
        self._Note = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ProjectId = params.get("ProjectId")
        self._ScenarioId = params.get("ScenarioId")
        self._Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateJobResponse(AbstractModel):
    """UpdateJob返回参数结构体

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


class UpdateProjectRequest(AbstractModel):
    """UpdateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Name: 项目名
        :type Name: str
        :param _Description: 项目描述
        :type Description: str
        :param _Status: 项目状态，默认传递1
        :type Status: int
        :param _Tags: 标签数组
        :type Tags: list of TagSpec
        """
        self._ProjectId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Tags = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpec()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProjectResponse(AbstractModel):
    """UpdateProject返回参数结构体

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


class UpdateScenarioRequest(AbstractModel):
    """UpdateScenario请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ScenarioId: 场景ID
        :type ScenarioId: str
        :param _Name: 场景名；调用该接口时，请将 Scenario 中不需要修改的字段保持原样也作为接口的入参，否则场景可能会不可用。
        :type Name: str
        :param _Description: 场景描述
        :type Description: str
        :param _Type: 压测场景的模式类型。取值范围：pts-http 代表简单模式，pts-js 代表脚本模式，pts-jmeter 代表 JMeter 模式。
        :type Type: str
        :param _Load: 施压配置
        :type Load: :class:`tencentcloud.pts.v20210728.models.Load`
        :param _EncodedScripts: deprecated
        :type EncodedScripts: str
        :param _Configs: deprecated
        :type Configs: list of str
        :param _Datasets: 测试数据集
        :type Datasets: list of TestData
        :param _Extensions: deprecated
        :type Extensions: list of str
        :param _SLAId: SLA规则ID
        :type SLAId: str
        :param _CronId: cron job ID
        :type CronId: str
        :param _Status: 场景状态（注：现已无需传递该参数）
        :type Status: int
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _TestScripts: 测试脚本路径
        :type TestScripts: list of ScriptInfo
        :param _Protocols: 协议文件路径
        :type Protocols: list of ProtocolInfo
        :param _RequestFiles: 请求文件路径
        :type RequestFiles: list of FileInfo
        :param _SLAPolicy: SLA 策略
        :type SLAPolicy: :class:`tencentcloud.pts.v20210728.models.SLAPolicy`
        :param _Plugins: 拓展包文件路径
        :type Plugins: list of FileInfo
        :param _DomainNameConfig: 域名解析配置
        :type DomainNameConfig: :class:`tencentcloud.pts.v20210728.models.DomainNameConfig`
        :param _NotificationHooks: WebHook请求配置
        :type NotificationHooks: list of Notification
        :param _Owner: 创建人名
        :type Owner: str
        :param _EnvId: 环境ID
        :type EnvId: str
        """
        self._ScenarioId = None
        self._Name = None
        self._Description = None
        self._Type = None
        self._Load = None
        self._EncodedScripts = None
        self._Configs = None
        self._Datasets = None
        self._Extensions = None
        self._SLAId = None
        self._CronId = None
        self._Status = None
        self._ProjectId = None
        self._TestScripts = None
        self._Protocols = None
        self._RequestFiles = None
        self._SLAPolicy = None
        self._Plugins = None
        self._DomainNameConfig = None
        self._NotificationHooks = None
        self._Owner = None
        self._EnvId = None

    @property
    def ScenarioId(self):
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Load(self):
        return self._Load

    @Load.setter
    def Load(self, Load):
        self._Load = Load

    @property
    def EncodedScripts(self):
        return self._EncodedScripts

    @EncodedScripts.setter
    def EncodedScripts(self, EncodedScripts):
        self._EncodedScripts = EncodedScripts

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def Datasets(self):
        return self._Datasets

    @Datasets.setter
    def Datasets(self, Datasets):
        self._Datasets = Datasets

    @property
    def Extensions(self):
        return self._Extensions

    @Extensions.setter
    def Extensions(self, Extensions):
        self._Extensions = Extensions

    @property
    def SLAId(self):
        return self._SLAId

    @SLAId.setter
    def SLAId(self, SLAId):
        self._SLAId = SLAId

    @property
    def CronId(self):
        return self._CronId

    @CronId.setter
    def CronId(self, CronId):
        self._CronId = CronId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TestScripts(self):
        return self._TestScripts

    @TestScripts.setter
    def TestScripts(self, TestScripts):
        self._TestScripts = TestScripts

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def RequestFiles(self):
        return self._RequestFiles

    @RequestFiles.setter
    def RequestFiles(self, RequestFiles):
        self._RequestFiles = RequestFiles

    @property
    def SLAPolicy(self):
        return self._SLAPolicy

    @SLAPolicy.setter
    def SLAPolicy(self, SLAPolicy):
        self._SLAPolicy = SLAPolicy

    @property
    def Plugins(self):
        return self._Plugins

    @Plugins.setter
    def Plugins(self, Plugins):
        self._Plugins = Plugins

    @property
    def DomainNameConfig(self):
        return self._DomainNameConfig

    @DomainNameConfig.setter
    def DomainNameConfig(self, DomainNameConfig):
        self._DomainNameConfig = DomainNameConfig

    @property
    def NotificationHooks(self):
        return self._NotificationHooks

    @NotificationHooks.setter
    def NotificationHooks(self, NotificationHooks):
        self._NotificationHooks = NotificationHooks

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._ScenarioId = params.get("ScenarioId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        if params.get("Load") is not None:
            self._Load = Load()
            self._Load._deserialize(params.get("Load"))
        self._EncodedScripts = params.get("EncodedScripts")
        self._Configs = params.get("Configs")
        if params.get("Datasets") is not None:
            self._Datasets = []
            for item in params.get("Datasets"):
                obj = TestData()
                obj._deserialize(item)
                self._Datasets.append(obj)
        self._Extensions = params.get("Extensions")
        self._SLAId = params.get("SLAId")
        self._CronId = params.get("CronId")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        if params.get("TestScripts") is not None:
            self._TestScripts = []
            for item in params.get("TestScripts"):
                obj = ScriptInfo()
                obj._deserialize(item)
                self._TestScripts.append(obj)
        if params.get("Protocols") is not None:
            self._Protocols = []
            for item in params.get("Protocols"):
                obj = ProtocolInfo()
                obj._deserialize(item)
                self._Protocols.append(obj)
        if params.get("RequestFiles") is not None:
            self._RequestFiles = []
            for item in params.get("RequestFiles"):
                obj = FileInfo()
                obj._deserialize(item)
                self._RequestFiles.append(obj)
        if params.get("SLAPolicy") is not None:
            self._SLAPolicy = SLAPolicy()
            self._SLAPolicy._deserialize(params.get("SLAPolicy"))
        if params.get("Plugins") is not None:
            self._Plugins = []
            for item in params.get("Plugins"):
                obj = FileInfo()
                obj._deserialize(item)
                self._Plugins.append(obj)
        if params.get("DomainNameConfig") is not None:
            self._DomainNameConfig = DomainNameConfig()
            self._DomainNameConfig._deserialize(params.get("DomainNameConfig"))
        if params.get("NotificationHooks") is not None:
            self._NotificationHooks = []
            for item in params.get("NotificationHooks"):
                obj = Notification()
                obj._deserialize(item)
                self._NotificationHooks.append(obj)
        self._Owner = params.get("Owner")
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScenarioResponse(AbstractModel):
    """UpdateScenario返回参数结构体

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


class VpcLoadDistribution(AbstractModel):
    """压力来源配置

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _Region: 地域
        :type Region: str
        :param _VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetIds: 子网ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        """
        self._RegionId = None
        self._Region = None
        self._VpcId = None
        self._SubnetIds = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        