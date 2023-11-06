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


class APIConfigDetail(AbstractModel):
    """接口描述信息

    """

    def __init__(self):
        r"""
        :param _Id: 接口id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _ServiceGroupId: 接口所属服务组id
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroupId: str
        :param _Description: 接口描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RelativeUrl: 相对路径
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeUrl: str
        :param _ServiceType: 服务类型 HTTP HTTPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _HttpMethod: GET POST
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpMethod: str
        :param _HttpInputExample: 请求示例
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpInputExample: str
        :param _HttpOutputExample: 回包示例
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpOutputExample: str
        :param _UpdatedBy: 更新成员
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedBy: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _Uin: 主账号uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubUin: 子账号subuin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubUin: str
        """
        self._Id = None
        self._ServiceGroupId = None
        self._Description = None
        self._RelativeUrl = None
        self._ServiceType = None
        self._HttpMethod = None
        self._HttpInputExample = None
        self._HttpOutputExample = None
        self._UpdatedBy = None
        self._UpdatedAt = None
        self._Uin = None
        self._SubUin = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RelativeUrl(self):
        return self._RelativeUrl

    @RelativeUrl.setter
    def RelativeUrl(self, RelativeUrl):
        self._RelativeUrl = RelativeUrl

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def HttpMethod(self):
        return self._HttpMethod

    @HttpMethod.setter
    def HttpMethod(self, HttpMethod):
        self._HttpMethod = HttpMethod

    @property
    def HttpInputExample(self):
        return self._HttpInputExample

    @HttpInputExample.setter
    def HttpInputExample(self, HttpInputExample):
        self._HttpInputExample = HttpInputExample

    @property
    def HttpOutputExample(self):
        return self._HttpOutputExample

    @HttpOutputExample.setter
    def HttpOutputExample(self, HttpOutputExample):
        self._HttpOutputExample = HttpOutputExample

    @property
    def UpdatedBy(self):
        return self._UpdatedBy

    @UpdatedBy.setter
    def UpdatedBy(self, UpdatedBy):
        self._UpdatedBy = UpdatedBy

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._Description = params.get("Description")
        self._RelativeUrl = params.get("RelativeUrl")
        self._ServiceType = params.get("ServiceType")
        self._HttpMethod = params.get("HttpMethod")
        self._HttpInputExample = params.get("HttpInputExample")
        self._HttpOutputExample = params.get("HttpOutputExample")
        self._UpdatedBy = params.get("UpdatedBy")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModelAccTask(AbstractModel):
    """批量模型加速任务

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ModelVersion: 模型版本
        :type ModelVersion: str
        :param _ModelSource: 模型来源(JOB/COS)
        :type ModelSource: str
        :param _ModelFormat: 模型格式(TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/MMDETECTION/ONNX/HUGGING_FACE)
        :type ModelFormat: str
        :param _TensorInfos: 模型Tensor信息
        :type TensorInfos: list of str
        :param _AccEngineVersion: 加速引擎版本
        :type AccEngineVersion: str
        :param _ModelInputPath: 模型输入cos路径
        :type ModelInputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _ModelSignature: SavedModel保存时配置的签名
        :type ModelSignature: str
        :param _FrameworkVersion: 加速引擎对应的框架版本
        :type FrameworkVersion: str
        """
        self._ModelId = None
        self._ModelVersion = None
        self._ModelSource = None
        self._ModelFormat = None
        self._TensorInfos = None
        self._AccEngineVersion = None
        self._ModelInputPath = None
        self._ModelName = None
        self._ModelSignature = None
        self._FrameworkVersion = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelVersion(self):
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def ModelSource(self):
        return self._ModelSource

    @ModelSource.setter
    def ModelSource(self, ModelSource):
        self._ModelSource = ModelSource

    @property
    def ModelFormat(self):
        return self._ModelFormat

    @ModelFormat.setter
    def ModelFormat(self, ModelFormat):
        self._ModelFormat = ModelFormat

    @property
    def TensorInfos(self):
        return self._TensorInfos

    @TensorInfos.setter
    def TensorInfos(self, TensorInfos):
        self._TensorInfos = TensorInfos

    @property
    def AccEngineVersion(self):
        return self._AccEngineVersion

    @AccEngineVersion.setter
    def AccEngineVersion(self, AccEngineVersion):
        self._AccEngineVersion = AccEngineVersion

    @property
    def ModelInputPath(self):
        return self._ModelInputPath

    @ModelInputPath.setter
    def ModelInputPath(self, ModelInputPath):
        self._ModelInputPath = ModelInputPath

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelSignature(self):
        return self._ModelSignature

    @ModelSignature.setter
    def ModelSignature(self, ModelSignature):
        self._ModelSignature = ModelSignature

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ModelVersion = params.get("ModelVersion")
        self._ModelSource = params.get("ModelSource")
        self._ModelFormat = params.get("ModelFormat")
        self._TensorInfos = params.get("TensorInfos")
        self._AccEngineVersion = params.get("AccEngineVersion")
        if params.get("ModelInputPath") is not None:
            self._ModelInputPath = CosPathInfo()
            self._ModelInputPath._deserialize(params.get("ModelInputPath"))
        self._ModelName = params.get("ModelName")
        self._ModelSignature = params.get("ModelSignature")
        self._FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchTaskDetail(AbstractModel):
    """跑批任务详情

    """

    def __init__(self):
        r"""
        :param _BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        :param _BatchTaskName: 跑批任务名称
        :type BatchTaskName: str
        :param _Uin: 主账号uin
        :type Uin: str
        :param _SubUin: 子账号uin
        :type SubUin: str
        :param _Region: 地域
        :type Region: str
        :param _ChargeType: 计费模式
        :type ChargeType: str
        :param _ResourceGroupId: 包年包月资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ResourceGroupName: 包年包月资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _ResourceConfigInfo: 资源配置
        :type ResourceConfigInfo: :class:`tencentcloud.tione.v20211111.models.ResourceConfigInfo`
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ModelInfo: 服务对应的模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _CodePackagePath: 代码包
注意：此字段可能返回 null，表示取不到有效值。
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StartCmd: 启动命令
注意：此字段可能返回 null，表示取不到有效值。
        :type StartCmd: str
        :param _DataConfigs: 输入数据配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DataConfigs: list of DataConfig
        :param _Outputs: 输出数据配置
        :type Outputs: list of DataConfig
        :param _LogEnable: 是否上报日志
        :type LogEnable: bool
        :param _LogConfig: 日志配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Status: 任务状态
        :type Status: str
        :param _RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _StartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param _LatestInstanceId: 最近一次实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestInstanceId: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _BillingInfo: 计费金额信息，eg：2.00元/小时 (for 按量计费)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param _PodList: 运行中的Pod的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: list of str
        :param _ModelInferenceCodeInfo: 模型推理代码信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInferenceCodeInfo: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        self._BatchTaskId = None
        self._BatchTaskName = None
        self._Uin = None
        self._SubUin = None
        self._Region = None
        self._ChargeType = None
        self._ResourceGroupId = None
        self._ResourceGroupName = None
        self._ResourceConfigInfo = None
        self._Tags = None
        self._ModelInfo = None
        self._ImageInfo = None
        self._CodePackagePath = None
        self._StartCmd = None
        self._DataConfigs = None
        self._Outputs = None
        self._LogEnable = None
        self._LogConfig = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._RuntimeInSeconds = None
        self._CreateTime = None
        self._UpdateTime = None
        self._StartTime = None
        self._EndTime = None
        self._ChargeStatus = None
        self._LatestInstanceId = None
        self._Remark = None
        self._FailureReason = None
        self._BillingInfo = None
        self._PodList = None
        self._ModelInferenceCodeInfo = None

    @property
    def BatchTaskId(self):
        return self._BatchTaskId

    @BatchTaskId.setter
    def BatchTaskId(self, BatchTaskId):
        self._BatchTaskId = BatchTaskId

    @property
    def BatchTaskName(self):
        return self._BatchTaskName

    @BatchTaskName.setter
    def BatchTaskName(self, BatchTaskName):
        self._BatchTaskName = BatchTaskName

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def ResourceConfigInfo(self):
        return self._ResourceConfigInfo

    @ResourceConfigInfo.setter
    def ResourceConfigInfo(self, ResourceConfigInfo):
        self._ResourceConfigInfo = ResourceConfigInfo

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ModelInfo(self):
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def CodePackagePath(self):
        return self._CodePackagePath

    @CodePackagePath.setter
    def CodePackagePath(self, CodePackagePath):
        self._CodePackagePath = CodePackagePath

    @property
    def StartCmd(self):
        return self._StartCmd

    @StartCmd.setter
    def StartCmd(self, StartCmd):
        self._StartCmd = StartCmd

    @property
    def DataConfigs(self):
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

    @property
    def Outputs(self):
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def LatestInstanceId(self):
        return self._LatestInstanceId

    @LatestInstanceId.setter
    def LatestInstanceId(self, LatestInstanceId):
        self._LatestInstanceId = LatestInstanceId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def BillingInfo(self):
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo

    @property
    def PodList(self):
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList

    @property
    def ModelInferenceCodeInfo(self):
        return self._ModelInferenceCodeInfo

    @ModelInferenceCodeInfo.setter
    def ModelInferenceCodeInfo(self, ModelInferenceCodeInfo):
        self._ModelInferenceCodeInfo = ModelInferenceCodeInfo


    def _deserialize(self, params):
        self._BatchTaskId = params.get("BatchTaskId")
        self._BatchTaskName = params.get("BatchTaskName")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._Region = params.get("Region")
        self._ChargeType = params.get("ChargeType")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        if params.get("ResourceConfigInfo") is not None:
            self._ResourceConfigInfo = ResourceConfigInfo()
            self._ResourceConfigInfo._deserialize(params.get("ResourceConfigInfo"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodePackagePath") is not None:
            self._CodePackagePath = CosPathInfo()
            self._CodePackagePath._deserialize(params.get("CodePackagePath"))
        self._StartCmd = params.get("StartCmd")
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._Outputs.append(obj)
        self._LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ChargeStatus = params.get("ChargeStatus")
        self._LatestInstanceId = params.get("LatestInstanceId")
        self._Remark = params.get("Remark")
        self._FailureReason = params.get("FailureReason")
        self._BillingInfo = params.get("BillingInfo")
        self._PodList = params.get("PodList")
        if params.get("ModelInferenceCodeInfo") is not None:
            self._ModelInferenceCodeInfo = CosPathInfo()
            self._ModelInferenceCodeInfo._deserialize(params.get("ModelInferenceCodeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchTaskInstance(AbstractModel):
    """批处理任务实例

    """

    def __init__(self):
        r"""
        :param _BatchTaskInstanceId: 任务实例id
        :type BatchTaskInstanceId: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Status: 任务状态
        :type Status: str
        :param _RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        """
        self._BatchTaskInstanceId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._RuntimeInSeconds = None

    @property
    def BatchTaskInstanceId(self):
        return self._BatchTaskInstanceId

    @BatchTaskInstanceId.setter
    def BatchTaskInstanceId(self, BatchTaskInstanceId):
        self._BatchTaskInstanceId = BatchTaskInstanceId

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds


    def _deserialize(self, params):
        self._BatchTaskInstanceId = params.get("BatchTaskInstanceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchTaskSetItem(AbstractModel):
    """出参类型

    """

    def __init__(self):
        r"""
        :param _BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        :param _BatchTaskName: 跑批任务名称
        :type BatchTaskName: str
        :param _ModelInfo: 模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _ChargeType: 计费模式
        :type ChargeType: str
        :param _ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param _ResourceGroupId: 包年包月资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ResourceConfigInfo: 资源配置
        :type ResourceConfigInfo: :class:`tencentcloud.tione.v20211111.models.ResourceConfigInfo`
        :param _Tags: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Status: 任务状态
        :type Status: str
        :param _RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Outputs: 输出
        :type Outputs: list of DataConfig
        :param _ResourceGroupName: 包年包月资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _FailureReason: 失败原因
        :type FailureReason: str
        :param _BillingInfo: 计费金额信息，eg：2.00元/小时 (for 按量计费)
        :type BillingInfo: str
        """
        self._BatchTaskId = None
        self._BatchTaskName = None
        self._ModelInfo = None
        self._ImageInfo = None
        self._ChargeType = None
        self._ChargeStatus = None
        self._ResourceGroupId = None
        self._ResourceConfigInfo = None
        self._Tags = None
        self._Status = None
        self._RuntimeInSeconds = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._UpdateTime = None
        self._Outputs = None
        self._ResourceGroupName = None
        self._FailureReason = None
        self._BillingInfo = None

    @property
    def BatchTaskId(self):
        return self._BatchTaskId

    @BatchTaskId.setter
    def BatchTaskId(self, BatchTaskId):
        self._BatchTaskId = BatchTaskId

    @property
    def BatchTaskName(self):
        return self._BatchTaskName

    @BatchTaskName.setter
    def BatchTaskName(self, BatchTaskName):
        self._BatchTaskName = BatchTaskName

    @property
    def ModelInfo(self):
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceConfigInfo(self):
        return self._ResourceConfigInfo

    @ResourceConfigInfo.setter
    def ResourceConfigInfo(self, ResourceConfigInfo):
        self._ResourceConfigInfo = ResourceConfigInfo

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
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Outputs(self):
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def BillingInfo(self):
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo


    def _deserialize(self, params):
        self._BatchTaskId = params.get("BatchTaskId")
        self._BatchTaskName = params.get("BatchTaskName")
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._ChargeType = params.get("ChargeType")
        self._ChargeStatus = params.get("ChargeStatus")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ResourceConfigInfo") is not None:
            self._ResourceConfigInfo = ResourceConfigInfo()
            self._ResourceConfigInfo._deserialize(params.get("ResourceConfigInfo"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Status = params.get("Status")
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._Outputs.append(obj)
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._FailureReason = params.get("FailureReason")
        self._BillingInfo = params.get("BillingInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSConfig(AbstractModel):
    """CFS存储的配置

    """

    def __init__(self):
        r"""
        :param _Id: cfs的实例的ID
        :type Id: str
        :param _Path: 存储的路径
        :type Path: str
        :param _MountType: cfs的挂载类型，可选值为：STORAGE、SOURCE 分别表示存储拓展模式和数据源模式，默认为 STORAGE
注意：此字段可能返回 null，表示取不到有效值。
        :type MountType: str
        :param _Protocol: 协议 1: NFS, 2: TURBO
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        """
        self._Id = None
        self._Path = None
        self._MountType = None
        self._Protocol = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def MountType(self):
        return self._MountType

    @MountType.setter
    def MountType(self, MountType):
        self._MountType = MountType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Path = params.get("Path")
        self._MountType = params.get("MountType")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSTurbo(AbstractModel):
    """配置CFSTurbo参数

    """

    def __init__(self):
        r"""
        :param _Id: CFSTurbo实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Path: CFSTurbo路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self._Id = None
        self._Path = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionRequest(AbstractModel):
    """ChatCompletion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 对话的目标模型ID。
自行部署的开源大模型聊天：部署的模型服务组ID，形如ms-xxyyzz。
        :type Model: str
        :param _Messages: 输入对话历史。旧的对话在前，数组中最后一项应该为这次的问题。
        :type Messages: list of Message
        :param _Temperature: 仅当模型为自行部署的开源大模型时生效。采样随机值，默认值为1.0，取值范围[0,2]。较高的值(如0.8)将使输出更加随机，而较低的值(如0.2)将使输出更加确定。建议仅修改此参数或TopP，但不建议两者都修改。
        :type Temperature: float
        :param _TopP: 仅当模型为自行部署的开源大模型时生效。核采样，默认值为1，取值范围[0,1]。指的是预先设置一个概率界限 p，然后将所有可能生成的token，根据概率大小从高到低排列，依次选取。当这些选取的token的累积概率大于或等于 p 值时停止，然后从已经选取的token中进行采样，生成下一个token。例如top_p为0.1时意味着模型只考虑累积概率为10%的token。建议仅修改此参数或Temperature，不建议两者都修改。
        :type TopP: float
        :param _MaxTokens: 仅当模型为自行部署的开源大模型时生效。最大生成的token数目。默认为无限大。
        :type MaxTokens: int
        """
        self._Model = None
        self._Messages = None
        self._Temperature = None
        self._TopP = None
        self._MaxTokens = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Temperature(self):
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def MaxTokens(self):
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._MaxTokens = params.get("MaxTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionResponse(AbstractModel):
    """ChatCompletion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 部署好的服务Id
        :type Model: str
        :param _Choices: 本次问答的答案。
        :type Choices: list of Choice
        :param _Id: 会话Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Usage: token统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Usage: :class:`tencentcloud.tione.v20211111.models.Usage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Model = None
        self._Choices = None
        self._Id = None
        self._Usage = None
        self._RequestId = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Choices(self):
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        self._Id = params.get("Id")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class Choice(AbstractModel):
    """对话结果

    """

    def __init__(self):
        r"""
        :param _Message: 对话结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: :class:`tencentcloud.tione.v20211111.models.Message`
        :param _FinishReason: 结束理由: stop, length, content_filter, null
        :type FinishReason: str
        :param _Index: 序号
        :type Index: int
        """
        self._Message = None
        self._FinishReason = None
        self._Index = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        if params.get("Message") is not None:
            self._Message = Message()
            self._Message._deserialize(params.get("Message"))
        self._FinishReason = params.get("FinishReason")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Container(AbstractModel):
    """容器信息

    """

    def __init__(self):
        r"""
        :param _Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ContainerId: id
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerId: str
        :param _Image: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param _Status: 容器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.tione.v20211111.models.ContainerStatus`
        """
        self._Name = None
        self._ContainerId = None
        self._Image = None
        self._Status = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContainerId(self):
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContainerId = params.get("ContainerId")
        self._Image = params.get("Image")
        if params.get("Status") is not None:
            self._Status = ContainerStatus()
            self._Status._deserialize(params.get("Status"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerStatus(AbstractModel):
    """容器状态

    """

    def __init__(self):
        r"""
        :param _RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param _State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param _Ready: 是否就绪
注意：此字段可能返回 null，表示取不到有效值。
        :type Ready: bool
        :param _Reason: 状态原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _Message: 容器的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._RestartCount = None
        self._State = None
        self._Ready = None
        self._Reason = None
        self._Message = None

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._RestartCount = params.get("RestartCount")
        self._State = params.get("State")
        self._Ready = params.get("Ready")
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosPathInfo(AbstractModel):
    """cos的路径信息

    """

    def __init__(self):
        r"""
        :param _Bucket: 存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _Region: 所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Paths: 路径列表，目前只支持单个
注意：此字段可能返回 null，表示取不到有效值。
        :type Paths: list of str
        """
        self._Bucket = None
        self._Region = None
        self._Paths = None

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Paths = params.get("Paths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchModelAccTasksRequest(AbstractModel):
    """CreateBatchModelAccTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskName: 模型加速任务名称
        :type ModelAccTaskName: str
        :param _BatchModelAccTasks: 批量模型加速任务
        :type BatchModelAccTasks: list of BatchModelAccTask
        :param _ModelOutputPath: 模型加速保存路径
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _OptimizationLevel: 优化级别(NO_LOSS/FP16/INT8)，默认FP16
        :type OptimizationLevel: str
        :param _GPUType: GPU卡类型(T4/V100/A10)，默认T4
        :type GPUType: str
        :param _HyperParameter: 专业参数设置
        :type HyperParameter: :class:`tencentcloud.tione.v20211111.models.HyperParameter`
        """
        self._ModelAccTaskName = None
        self._BatchModelAccTasks = None
        self._ModelOutputPath = None
        self._Tags = None
        self._OptimizationLevel = None
        self._GPUType = None
        self._HyperParameter = None

    @property
    def ModelAccTaskName(self):
        return self._ModelAccTaskName

    @ModelAccTaskName.setter
    def ModelAccTaskName(self, ModelAccTaskName):
        self._ModelAccTaskName = ModelAccTaskName

    @property
    def BatchModelAccTasks(self):
        return self._BatchModelAccTasks

    @BatchModelAccTasks.setter
    def BatchModelAccTasks(self, BatchModelAccTasks):
        self._BatchModelAccTasks = BatchModelAccTasks

    @property
    def ModelOutputPath(self):
        return self._ModelOutputPath

    @ModelOutputPath.setter
    def ModelOutputPath(self, ModelOutputPath):
        self._ModelOutputPath = ModelOutputPath

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def OptimizationLevel(self):
        return self._OptimizationLevel

    @OptimizationLevel.setter
    def OptimizationLevel(self, OptimizationLevel):
        self._OptimizationLevel = OptimizationLevel

    @property
    def GPUType(self):
        return self._GPUType

    @GPUType.setter
    def GPUType(self, GPUType):
        self._GPUType = GPUType

    @property
    def HyperParameter(self):
        return self._HyperParameter

    @HyperParameter.setter
    def HyperParameter(self, HyperParameter):
        self._HyperParameter = HyperParameter


    def _deserialize(self, params):
        self._ModelAccTaskName = params.get("ModelAccTaskName")
        if params.get("BatchModelAccTasks") is not None:
            self._BatchModelAccTasks = []
            for item in params.get("BatchModelAccTasks"):
                obj = BatchModelAccTask()
                obj._deserialize(item)
                self._BatchModelAccTasks.append(obj)
        if params.get("ModelOutputPath") is not None:
            self._ModelOutputPath = CosPathInfo()
            self._ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._OptimizationLevel = params.get("OptimizationLevel")
        self._GPUType = params.get("GPUType")
        if params.get("HyperParameter") is not None:
            self._HyperParameter = HyperParameter()
            self._HyperParameter._deserialize(params.get("HyperParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchModelAccTasksResponse(AbstractModel):
    """CreateBatchModelAccTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskIds: 模型优化任务ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelAccTaskIds = None
        self._RequestId = None

    @property
    def ModelAccTaskIds(self):
        return self._ModelAccTaskIds

    @ModelAccTaskIds.setter
    def ModelAccTaskIds(self, ModelAccTaskIds):
        self._ModelAccTaskIds = ModelAccTaskIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelAccTaskIds = params.get("ModelAccTaskIds")
        self._RequestId = params.get("RequestId")


class CreateBatchTaskRequest(AbstractModel):
    """CreateBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTaskName: 跑批任务名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type BatchTaskName: str
        :param _ChargeType: 计费模式，eg：PREPAID 包年包月；POSTPAID_BY_HOUR 按量计费
        :type ChargeType: str
        :param _ResourceConfigInfo: 资源配置
        :type ResourceConfigInfo: :class:`tencentcloud.tione.v20211111.models.ResourceConfigInfo`
        :param _Outputs: 结果输出
        :type Outputs: list of DataConfig
        :param _LogEnable: 是否上报日志
        :type LogEnable: bool
        :param _JobType: 工作类型 1:单次 2:周期
        :type JobType: int
        :param _CronInfo: 任务周期描述
        :type CronInfo: :class:`tencentcloud.tione.v20211111.models.CronInfo`
        :param _ResourceGroupId: 包年包月资源组ID
        :type ResourceGroupId: str
        :param _Tags: 标签配置
        :type Tags: list of Tag
        :param _ModelInfo: 服务对应的模型信息，有模型文件时需要填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _ImageInfo: 自定义镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _CodePackage: 代码包
        :type CodePackage: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StartCmd: 启动命令
        :type StartCmd: str
        :param _DataConfigs: 数据配置
        :type DataConfigs: list of DataConfig
        :param _LogConfig: 日志配置
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _VpcId: VPC Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _Remark: 备注
        :type Remark: str
        :param _CallbackUrl: 任务执行结果回调URL，仅支持http和https。回调格式&内容详见: [TI-ONE 接口回调说明](https://cloud.tencent.com/document/product/851/84292)
        :type CallbackUrl: str
        """
        self._BatchTaskName = None
        self._ChargeType = None
        self._ResourceConfigInfo = None
        self._Outputs = None
        self._LogEnable = None
        self._JobType = None
        self._CronInfo = None
        self._ResourceGroupId = None
        self._Tags = None
        self._ModelInfo = None
        self._ImageInfo = None
        self._CodePackage = None
        self._StartCmd = None
        self._DataConfigs = None
        self._LogConfig = None
        self._VpcId = None
        self._SubnetId = None
        self._Remark = None
        self._CallbackUrl = None

    @property
    def BatchTaskName(self):
        return self._BatchTaskName

    @BatchTaskName.setter
    def BatchTaskName(self, BatchTaskName):
        self._BatchTaskName = BatchTaskName

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceConfigInfo(self):
        return self._ResourceConfigInfo

    @ResourceConfigInfo.setter
    def ResourceConfigInfo(self, ResourceConfigInfo):
        self._ResourceConfigInfo = ResourceConfigInfo

    @property
    def Outputs(self):
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def JobType(self):
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def CronInfo(self):
        return self._CronInfo

    @CronInfo.setter
    def CronInfo(self, CronInfo):
        self._CronInfo = CronInfo

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ModelInfo(self):
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def CodePackage(self):
        return self._CodePackage

    @CodePackage.setter
    def CodePackage(self, CodePackage):
        self._CodePackage = CodePackage

    @property
    def StartCmd(self):
        return self._StartCmd

    @StartCmd.setter
    def StartCmd(self, StartCmd):
        self._StartCmd = StartCmd

    @property
    def DataConfigs(self):
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

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
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._BatchTaskName = params.get("BatchTaskName")
        self._ChargeType = params.get("ChargeType")
        if params.get("ResourceConfigInfo") is not None:
            self._ResourceConfigInfo = ResourceConfigInfo()
            self._ResourceConfigInfo._deserialize(params.get("ResourceConfigInfo"))
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._Outputs.append(obj)
        self._LogEnable = params.get("LogEnable")
        self._JobType = params.get("JobType")
        if params.get("CronInfo") is not None:
            self._CronInfo = CronInfo()
            self._CronInfo._deserialize(params.get("CronInfo"))
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodePackage") is not None:
            self._CodePackage = CosPathInfo()
            self._CodePackage._deserialize(params.get("CodePackage"))
        self._StartCmd = params.get("StartCmd")
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Remark = params.get("Remark")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchTaskResponse(AbstractModel):
    """CreateBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchTaskId = None
        self._RequestId = None

    @property
    def BatchTaskId(self):
        return self._BatchTaskId

    @BatchTaskId.setter
    def BatchTaskId(self, BatchTaskId):
        self._BatchTaskId = BatchTaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchTaskId = params.get("BatchTaskId")
        self._RequestId = params.get("RequestId")


class CreateDatasetRequest(AbstractModel):
    """CreateDataset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasetName: 数据集名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type DatasetName: str
        :param _DatasetType: 数据集类型:
TYPE_DATASET_TEXT，文本
TYPE_DATASET_IMAGE，图片
TYPE_DATASET_TABLE，表格
TYPE_DATASET_OTHER，其他
        :type DatasetType: str
        :param _StorageDataPath: 数据源cos路径
        :type StorageDataPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StorageLabelPath: 数据集标签cos存储路径
        :type StorageLabelPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _DatasetTags: 数据集标签
        :type DatasetTags: list of Tag
        :param _AnnotationStatus: 数据集标注状态:
STATUS_NON_ANNOTATED，未标注
STATUS_ANNOTATED，已标注
        :type AnnotationStatus: str
        :param _AnnotationType: 标注类型:
ANNOTATION_TYPE_CLASSIFICATION，图片分类
ANNOTATION_TYPE_DETECTION，目标检测
ANNOTATION_TYPE_SEGMENTATION，图片分割
ANNOTATION_TYPE_TRACKING，目标跟踪
        :type AnnotationType: str
        :param _AnnotationFormat: 标注格式:
ANNOTATION_FORMAT_TI，TI平台格式
ANNOTATION_FORMAT_PASCAL，Pascal Voc
ANNOTATION_FORMAT_COCO，COCO
ANNOTATION_FORMAT_FILE，文件目录结构
        :type AnnotationFormat: str
        :param _SchemaInfos: 表头信息
        :type SchemaInfos: list of SchemaInfo
        :param _IsSchemaExisted: 数据是否存在表头
        :type IsSchemaExisted: bool
        :param _ContentType: 导入文件粒度，按行或者按文件
        :type ContentType: str
        """
        self._DatasetName = None
        self._DatasetType = None
        self._StorageDataPath = None
        self._StorageLabelPath = None
        self._DatasetTags = None
        self._AnnotationStatus = None
        self._AnnotationType = None
        self._AnnotationFormat = None
        self._SchemaInfos = None
        self._IsSchemaExisted = None
        self._ContentType = None

    @property
    def DatasetName(self):
        return self._DatasetName

    @DatasetName.setter
    def DatasetName(self, DatasetName):
        self._DatasetName = DatasetName

    @property
    def DatasetType(self):
        return self._DatasetType

    @DatasetType.setter
    def DatasetType(self, DatasetType):
        self._DatasetType = DatasetType

    @property
    def StorageDataPath(self):
        return self._StorageDataPath

    @StorageDataPath.setter
    def StorageDataPath(self, StorageDataPath):
        self._StorageDataPath = StorageDataPath

    @property
    def StorageLabelPath(self):
        return self._StorageLabelPath

    @StorageLabelPath.setter
    def StorageLabelPath(self, StorageLabelPath):
        self._StorageLabelPath = StorageLabelPath

    @property
    def DatasetTags(self):
        return self._DatasetTags

    @DatasetTags.setter
    def DatasetTags(self, DatasetTags):
        self._DatasetTags = DatasetTags

    @property
    def AnnotationStatus(self):
        return self._AnnotationStatus

    @AnnotationStatus.setter
    def AnnotationStatus(self, AnnotationStatus):
        self._AnnotationStatus = AnnotationStatus

    @property
    def AnnotationType(self):
        return self._AnnotationType

    @AnnotationType.setter
    def AnnotationType(self, AnnotationType):
        self._AnnotationType = AnnotationType

    @property
    def AnnotationFormat(self):
        return self._AnnotationFormat

    @AnnotationFormat.setter
    def AnnotationFormat(self, AnnotationFormat):
        self._AnnotationFormat = AnnotationFormat

    @property
    def SchemaInfos(self):
        return self._SchemaInfos

    @SchemaInfos.setter
    def SchemaInfos(self, SchemaInfos):
        self._SchemaInfos = SchemaInfos

    @property
    def IsSchemaExisted(self):
        return self._IsSchemaExisted

    @IsSchemaExisted.setter
    def IsSchemaExisted(self, IsSchemaExisted):
        self._IsSchemaExisted = IsSchemaExisted

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._DatasetName = params.get("DatasetName")
        self._DatasetType = params.get("DatasetType")
        if params.get("StorageDataPath") is not None:
            self._StorageDataPath = CosPathInfo()
            self._StorageDataPath._deserialize(params.get("StorageDataPath"))
        if params.get("StorageLabelPath") is not None:
            self._StorageLabelPath = CosPathInfo()
            self._StorageLabelPath._deserialize(params.get("StorageLabelPath"))
        if params.get("DatasetTags") is not None:
            self._DatasetTags = []
            for item in params.get("DatasetTags"):
                obj = Tag()
                obj._deserialize(item)
                self._DatasetTags.append(obj)
        self._AnnotationStatus = params.get("AnnotationStatus")
        self._AnnotationType = params.get("AnnotationType")
        self._AnnotationFormat = params.get("AnnotationFormat")
        if params.get("SchemaInfos") is not None:
            self._SchemaInfos = []
            for item in params.get("SchemaInfos"):
                obj = SchemaInfo()
                obj._deserialize(item)
                self._SchemaInfos.append(obj)
        self._IsSchemaExisted = params.get("IsSchemaExisted")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatasetResponse(AbstractModel):
    """CreateDataset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasetId: 数据集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DatasetId = None
        self._RequestId = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._RequestId = params.get("RequestId")


class CreateModelServiceRequest(AbstractModel):
    """CreateModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 新增版本时需要填写
        :type ServiceGroupId: str
        :param _ServiceGroupName: 不超过60个字，仅支持英文、数字、下划线"_"、短横"-"，只能以英文、数字开头
        :type ServiceGroupName: str
        :param _ServiceDescription: 模型服务的描述
        :type ServiceDescription: str
        :param _ChargeType: 付费模式,有 PREPAID （包年包月）和 POSTPAID_BY_HOUR（按量付费）
        :type ChargeType: str
        :param _ResourceGroupId: 预付费模式下所属的资源组id，同服务组下唯一
        :type ResourceGroupId: str
        :param _ModelInfo: 模型信息，需要挂载模型时填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _ImageInfo: 镜像信息，配置服务运行所需的镜像地址等信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _Env: 环境变量，可选参数，用于配置容器中的环境变量
        :type Env: list of EnvVar
        :param _Resources: 资源描述，指定包年包月模式下的cpu,mem,gpu等信息，后付费无需填写
        :type Resources: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _InstanceType: 使用DescribeBillingSpecs接口返回的规格列表中的值，或者参考实例列表:
TI.S.MEDIUM.POST	2C4G
TI.S.LARGE.POST	4C8G
TI.S.2XLARGE16.POST	8C16G
TI.S.2XLARGE32.POST	8C32G
TI.S.4XLARGE32.POST	16C32G
TI.S.4XLARGE64.POST	16C64G
TI.S.6XLARGE48.POST	24C48G
TI.S.6XLARGE96.POST	24C96G
TI.S.8XLARGE64.POST	32C64G
TI.S.8XLARGE128.POST 32C128G
TI.GN7.LARGE20.POST	4C20G T4*1/4
TI.GN7.2XLARGE40.POST	10C40G T4*1/2
TI.GN7.2XLARGE32.POST	8C32G T4*1
TI.GN7.5XLARGE80.POST	20C80G T4*1
TI.GN7.8XLARGE128.POST	32C128G T4*1
TI.GN7.10XLARGE160.POST	40C160G T4*2
TI.GN7.20XLARGE320.POST	80C320G T4*4
        :type InstanceType: str
        :param _ScaleMode: 扩缩容类型 支持：自动 - "AUTO", 手动 - "MANUAL",默认为MANUAL
        :type ScaleMode: str
        :param _Replicas: 实例数量, 不同计费模式和调节模式下对应关系如下
PREPAID 和 POSTPAID_BY_HOUR:
手动调节模式下对应 实例数量
自动调节模式下对应 基于时间的默认策略的实例数量
HYBRID_PAID:
后付费实例手动调节模式下对应 实例数量
后付费实例自动调节模式下对应 时间策略的默认策略的实例数量
        :type Replicas: int
        :param _HorizontalPodAutoscaler: 自动伸缩信息
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        :param _LogEnable: 是否开启日志投递，开启后需填写配置投递到指定cls
        :type LogEnable: bool
        :param _LogConfig: 日志配置，需要投递服务日志到指定cls时填写
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _AuthorizationEnable: 是否开启接口鉴权，开启后自动生成token信息，访问需要token鉴权
        :type AuthorizationEnable: bool
        :param _Tags: 腾讯云标签
        :type Tags: list of Tag
        :param _NewVersion: 是否新增版本
        :type NewVersion: bool
        :param _CronScaleJobs: 定时任务配置，使用定时策略时填写
        :type CronScaleJobs: list of CronScaleJob
        :param _ScaleStrategy: 自动伸缩策略配置 HPA : 通过HPA进行弹性伸缩 CRON 通过定时任务进行伸缩
        :type ScaleStrategy: str
        :param _HybridBillingPrepaidReplicas: 计费模式[HYBRID_PAID]时生效, 用于标识混合计费模式下的预付费实例数
        :type HybridBillingPrepaidReplicas: int
        :param _CreateSource: [AUTO_ML 自动学习，自动学习正式发布 AUTO_ML_FORMAL, DEFAULT 默认]
        :type CreateSource: str
        :param _ModelHotUpdateEnable: 是否开启模型的热更新。默认不开启
        :type ModelHotUpdateEnable: bool
        :param _ScheduledAction: 定时停止配置
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param _VolumeMount: 挂载配置，目前只支持CFS
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        :param _ServiceLimit: 服务限速限流相关配置
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param _CallbackUrl: 回调地址，用于回调创建服务状态信息，回调格式&内容详情见：[TI-ONE 接口回调说明](https://cloud.tencent.com/document/product/851/84292)
        :type CallbackUrl: str
        :param _ModelTurboEnable: 是否开启模型的加速, 仅对StableDiffusion(动态加速)格式的模型有效。
        :type ModelTurboEnable: bool
        :param _ServiceCategory: 服务分类
        :type ServiceCategory: str
        :param _Command: 服务的启动命令
        :type Command: str
        :param _ServiceEIP: 是否开启TIONE内网访问外部
        :type ServiceEIP: :class:`tencentcloud.tione.v20211111.models.ServiceEIP`
        """
        self._ServiceGroupId = None
        self._ServiceGroupName = None
        self._ServiceDescription = None
        self._ChargeType = None
        self._ResourceGroupId = None
        self._ModelInfo = None
        self._ImageInfo = None
        self._Env = None
        self._Resources = None
        self._InstanceType = None
        self._ScaleMode = None
        self._Replicas = None
        self._HorizontalPodAutoscaler = None
        self._LogEnable = None
        self._LogConfig = None
        self._AuthorizationEnable = None
        self._Tags = None
        self._NewVersion = None
        self._CronScaleJobs = None
        self._ScaleStrategy = None
        self._HybridBillingPrepaidReplicas = None
        self._CreateSource = None
        self._ModelHotUpdateEnable = None
        self._ScheduledAction = None
        self._VolumeMount = None
        self._ServiceLimit = None
        self._CallbackUrl = None
        self._ModelTurboEnable = None
        self._ServiceCategory = None
        self._Command = None
        self._ServiceEIP = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def ServiceGroupName(self):
        return self._ServiceGroupName

    @ServiceGroupName.setter
    def ServiceGroupName(self, ServiceGroupName):
        self._ServiceGroupName = ServiceGroupName

    @property
    def ServiceDescription(self):
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ModelInfo(self):
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ScaleMode(self):
        return self._ScaleMode

    @ScaleMode.setter
    def ScaleMode(self, ScaleMode):
        self._ScaleMode = ScaleMode

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def AuthorizationEnable(self):
        return self._AuthorizationEnable

    @AuthorizationEnable.setter
    def AuthorizationEnable(self, AuthorizationEnable):
        self._AuthorizationEnable = AuthorizationEnable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NewVersion(self):
        return self._NewVersion

    @NewVersion.setter
    def NewVersion(self, NewVersion):
        self._NewVersion = NewVersion

    @property
    def CronScaleJobs(self):
        return self._CronScaleJobs

    @CronScaleJobs.setter
    def CronScaleJobs(self, CronScaleJobs):
        self._CronScaleJobs = CronScaleJobs

    @property
    def ScaleStrategy(self):
        return self._ScaleStrategy

    @ScaleStrategy.setter
    def ScaleStrategy(self, ScaleStrategy):
        self._ScaleStrategy = ScaleStrategy

    @property
    def HybridBillingPrepaidReplicas(self):
        return self._HybridBillingPrepaidReplicas

    @HybridBillingPrepaidReplicas.setter
    def HybridBillingPrepaidReplicas(self, HybridBillingPrepaidReplicas):
        self._HybridBillingPrepaidReplicas = HybridBillingPrepaidReplicas

    @property
    def CreateSource(self):
        return self._CreateSource

    @CreateSource.setter
    def CreateSource(self, CreateSource):
        self._CreateSource = CreateSource

    @property
    def ModelHotUpdateEnable(self):
        return self._ModelHotUpdateEnable

    @ModelHotUpdateEnable.setter
    def ModelHotUpdateEnable(self, ModelHotUpdateEnable):
        self._ModelHotUpdateEnable = ModelHotUpdateEnable

    @property
    def ScheduledAction(self):
        return self._ScheduledAction

    @ScheduledAction.setter
    def ScheduledAction(self, ScheduledAction):
        self._ScheduledAction = ScheduledAction

    @property
    def VolumeMount(self):
        return self._VolumeMount

    @VolumeMount.setter
    def VolumeMount(self, VolumeMount):
        self._VolumeMount = VolumeMount

    @property
    def ServiceLimit(self):
        return self._ServiceLimit

    @ServiceLimit.setter
    def ServiceLimit(self, ServiceLimit):
        self._ServiceLimit = ServiceLimit

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def ModelTurboEnable(self):
        return self._ModelTurboEnable

    @ModelTurboEnable.setter
    def ModelTurboEnable(self, ModelTurboEnable):
        self._ModelTurboEnable = ModelTurboEnable

    @property
    def ServiceCategory(self):
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
        self._ServiceCategory = ServiceCategory

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ServiceEIP(self):
        return self._ServiceEIP

    @ServiceEIP.setter
    def ServiceEIP(self, ServiceEIP):
        self._ServiceEIP = ServiceEIP


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._ServiceGroupName = params.get("ServiceGroupName")
        self._ServiceDescription = params.get("ServiceDescription")
        self._ChargeType = params.get("ChargeType")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("Env") is not None:
            self._Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self._Env.append(obj)
        if params.get("Resources") is not None:
            self._Resources = ResourceInfo()
            self._Resources._deserialize(params.get("Resources"))
        self._InstanceType = params.get("InstanceType")
        self._ScaleMode = params.get("ScaleMode")
        self._Replicas = params.get("Replicas")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self._LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._AuthorizationEnable = params.get("AuthorizationEnable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NewVersion = params.get("NewVersion")
        if params.get("CronScaleJobs") is not None:
            self._CronScaleJobs = []
            for item in params.get("CronScaleJobs"):
                obj = CronScaleJob()
                obj._deserialize(item)
                self._CronScaleJobs.append(obj)
        self._ScaleStrategy = params.get("ScaleStrategy")
        self._HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
        self._CreateSource = params.get("CreateSource")
        self._ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
        if params.get("ScheduledAction") is not None:
            self._ScheduledAction = ScheduledAction()
            self._ScheduledAction._deserialize(params.get("ScheduledAction"))
        if params.get("VolumeMount") is not None:
            self._VolumeMount = VolumeMount()
            self._VolumeMount._deserialize(params.get("VolumeMount"))
        if params.get("ServiceLimit") is not None:
            self._ServiceLimit = ServiceLimit()
            self._ServiceLimit._deserialize(params.get("ServiceLimit"))
        self._CallbackUrl = params.get("CallbackUrl")
        self._ModelTurboEnable = params.get("ModelTurboEnable")
        self._ServiceCategory = params.get("ServiceCategory")
        self._Command = params.get("Command")
        if params.get("ServiceEIP") is not None:
            self._ServiceEIP = ServiceEIP()
            self._ServiceEIP._deserialize(params.get("ServiceEIP"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelServiceResponse(AbstractModel):
    """CreateModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 生成的模型服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Service = None
        self._RequestId = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        self._RequestId = params.get("RequestId")


class CreateNotebookImageRequest(AbstractModel):
    """CreateNotebookImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _NotebookId: notebook id
        :type NotebookId: str
        :param _Kernels: 要保存的kernel数组
        :type Kernels: list of str
        """
        self._ImageInfo = None
        self._NotebookId = None
        self._Kernels = None

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def NotebookId(self):
        return self._NotebookId

    @NotebookId.setter
    def NotebookId(self, NotebookId):
        self._NotebookId = NotebookId

    @property
    def Kernels(self):
        return self._Kernels

    @Kernels.setter
    def Kernels(self, Kernels):
        self._Kernels = Kernels


    def _deserialize(self, params):
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._NotebookId = params.get("NotebookId")
        self._Kernels = params.get("Kernels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookImageResponse(AbstractModel):
    """CreateNotebookImage返回参数结构体

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


class CreateNotebookRequest(AbstractModel):
    """CreateNotebook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称。不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type Name: str
        :param _ChargeType: 计算资源付费模式 ，可选值为：
PREPAID：预付费，即包年包月
POSTPAID_BY_HOUR：按小时后付费
        :type ChargeType: str
        :param _ResourceConf: 计算资源配置
        :type ResourceConf: :class:`tencentcloud.tione.v20211111.models.ResourceConf`
        :param _LogEnable: 是否上报日志
        :type LogEnable: bool
        :param _RootAccess: 是否ROOT权限
        :type RootAccess: bool
        :param _AutoStopping: 是否自动停止
        :type AutoStopping: bool
        :param _DirectInternetAccess: 是否访问公网
        :type DirectInternetAccess: bool
        :param _ResourceGroupId: 资源组ID(for预付费)
        :type ResourceGroupId: str
        :param _VpcId: Vpc-Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _VolumeSourceType: 存储的类型。取值包含： 
    FREE:    预付费的免费存储
    CLOUD_PREMIUM： 高性能云硬盘
    CLOUD_SSD： SSD云硬盘
    CFS:     CFS存储，包含NFS和turbo
        :type VolumeSourceType: str
        :param _VolumeSizeInGB: 存储卷大小，单位GB
        :type VolumeSizeInGB: int
        :param _VolumeSourceCFS: CFS存储的配置
        :type VolumeSourceCFS: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _LogConfig: 日志配置
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _LifecycleScriptId: 生命周期脚本的ID
        :type LifecycleScriptId: str
        :param _DefaultCodeRepoId: 默认GIT存储库的ID
        :type DefaultCodeRepoId: str
        :param _AdditionalCodeRepoIds: 其他GIT存储库的ID，最多3个
        :type AdditionalCodeRepoIds: list of str
        :param _AutomaticStopTime: 自动停止时间，单位小时
        :type AutomaticStopTime: int
        :param _Tags: 标签配置
        :type Tags: list of Tag
        :param _DataConfigs: 数据配置
        :type DataConfigs: list of DataConfig
        :param _ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _ImageType: 镜像类型
        :type ImageType: str
        :param _SSHConfig: SSH配置信息
        :type SSHConfig: :class:`tencentcloud.tione.v20211111.models.SSHConfig`
        """
        self._Name = None
        self._ChargeType = None
        self._ResourceConf = None
        self._LogEnable = None
        self._RootAccess = None
        self._AutoStopping = None
        self._DirectInternetAccess = None
        self._ResourceGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._VolumeSourceType = None
        self._VolumeSizeInGB = None
        self._VolumeSourceCFS = None
        self._LogConfig = None
        self._LifecycleScriptId = None
        self._DefaultCodeRepoId = None
        self._AdditionalCodeRepoIds = None
        self._AutomaticStopTime = None
        self._Tags = None
        self._DataConfigs = None
        self._ImageInfo = None
        self._ImageType = None
        self._SSHConfig = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceConf(self):
        return self._ResourceConf

    @ResourceConf.setter
    def ResourceConf(self, ResourceConf):
        self._ResourceConf = ResourceConf

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def RootAccess(self):
        return self._RootAccess

    @RootAccess.setter
    def RootAccess(self, RootAccess):
        self._RootAccess = RootAccess

    @property
    def AutoStopping(self):
        return self._AutoStopping

    @AutoStopping.setter
    def AutoStopping(self, AutoStopping):
        self._AutoStopping = AutoStopping

    @property
    def DirectInternetAccess(self):
        return self._DirectInternetAccess

    @DirectInternetAccess.setter
    def DirectInternetAccess(self, DirectInternetAccess):
        self._DirectInternetAccess = DirectInternetAccess

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

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
    def VolumeSourceType(self):
        return self._VolumeSourceType

    @VolumeSourceType.setter
    def VolumeSourceType(self, VolumeSourceType):
        self._VolumeSourceType = VolumeSourceType

    @property
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB

    @property
    def VolumeSourceCFS(self):
        return self._VolumeSourceCFS

    @VolumeSourceCFS.setter
    def VolumeSourceCFS(self, VolumeSourceCFS):
        self._VolumeSourceCFS = VolumeSourceCFS

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def LifecycleScriptId(self):
        return self._LifecycleScriptId

    @LifecycleScriptId.setter
    def LifecycleScriptId(self, LifecycleScriptId):
        self._LifecycleScriptId = LifecycleScriptId

    @property
    def DefaultCodeRepoId(self):
        return self._DefaultCodeRepoId

    @DefaultCodeRepoId.setter
    def DefaultCodeRepoId(self, DefaultCodeRepoId):
        self._DefaultCodeRepoId = DefaultCodeRepoId

    @property
    def AdditionalCodeRepoIds(self):
        return self._AdditionalCodeRepoIds

    @AdditionalCodeRepoIds.setter
    def AdditionalCodeRepoIds(self, AdditionalCodeRepoIds):
        self._AdditionalCodeRepoIds = AdditionalCodeRepoIds

    @property
    def AutomaticStopTime(self):
        return self._AutomaticStopTime

    @AutomaticStopTime.setter
    def AutomaticStopTime(self, AutomaticStopTime):
        self._AutomaticStopTime = AutomaticStopTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DataConfigs(self):
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def SSHConfig(self):
        return self._SSHConfig

    @SSHConfig.setter
    def SSHConfig(self, SSHConfig):
        self._SSHConfig = SSHConfig


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ChargeType = params.get("ChargeType")
        if params.get("ResourceConf") is not None:
            self._ResourceConf = ResourceConf()
            self._ResourceConf._deserialize(params.get("ResourceConf"))
        self._LogEnable = params.get("LogEnable")
        self._RootAccess = params.get("RootAccess")
        self._AutoStopping = params.get("AutoStopping")
        self._DirectInternetAccess = params.get("DirectInternetAccess")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VolumeSourceType = params.get("VolumeSourceType")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        if params.get("VolumeSourceCFS") is not None:
            self._VolumeSourceCFS = CFSConfig()
            self._VolumeSourceCFS._deserialize(params.get("VolumeSourceCFS"))
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._LifecycleScriptId = params.get("LifecycleScriptId")
        self._DefaultCodeRepoId = params.get("DefaultCodeRepoId")
        self._AdditionalCodeRepoIds = params.get("AdditionalCodeRepoIds")
        self._AutomaticStopTime = params.get("AutomaticStopTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._ImageType = params.get("ImageType")
        if params.get("SSHConfig") is not None:
            self._SSHConfig = SSHConfig()
            self._SSHConfig._deserialize(params.get("SSHConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNotebookResponse(AbstractModel):
    """CreateNotebook返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: notebook标志
        :type Id: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateOptimizedModelRequest(AbstractModel):
    """CreateOptimizedModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._ModelAccTaskId = None
        self._Tags = None

    @property
    def ModelAccTaskId(self):
        return self._ModelAccTaskId

    @ModelAccTaskId.setter
    def ModelAccTaskId(self, ModelAccTaskId):
        self._ModelAccTaskId = ModelAccTaskId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ModelAccTaskId = params.get("ModelAccTaskId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOptimizedModelResponse(AbstractModel):
    """CreateOptimizedModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _ModelVersionId: 模型版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelVersionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelId = None
        self._ModelVersionId = None
        self._RequestId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelVersionId(self):
        return self._ModelVersionId

    @ModelVersionId.setter
    def ModelVersionId(self, ModelVersionId):
        self._ModelVersionId = ModelVersionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ModelVersionId = params.get("ModelVersionId")
        self._RequestId = params.get("RequestId")


class CreateTrainingModelRequest(AbstractModel):
    """CreateTrainingModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImportMethod: 导入方式
MODEL：导入新模型
VERSION：导入新版本
EXIST：导入现有版本
        :type ImportMethod: str
        :param _ReasoningEnvironmentSource: 推理环境来源（SYSTEM/CUSTOM）
        :type ReasoningEnvironmentSource: str
        :param _TrainingModelName: 模型名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type TrainingModelName: str
        :param _Tags: 标签配置
        :type Tags: list of Tag
        :param _TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param _TrainingModelCosPath: 模型来源cos目录，以/结尾
        :type TrainingModelCosPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _AlgorithmFramework: 算法框架 （PYTORCH/TENSORFLOW/DETECTRON2/PMML/MMDETECTION)
        :type AlgorithmFramework: str
        :param _ReasoningEnvironment: 推理环境
        :type ReasoningEnvironment: str
        :param _TrainingModelIndex: 训练指标，最多支持1000字符
        :type TrainingModelIndex: str
        :param _TrainingModelVersion: 模型版本
        :type TrainingModelVersion: str
        :param _ReasoningImageInfo: 自定义推理环境
        :type ReasoningImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _ModelMoveMode: 模型移动方式（CUT/COPY）
        :type ModelMoveMode: str
        :param _TrainingJobId: 训练任务ID
        :type TrainingJobId: str
        :param _TrainingModelId: 模型ID（导入新模型不需要，导入新版本需要）
        :type TrainingModelId: str
        :param _ModelOutputPath: 模型存储cos目录
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _TrainingModelSource: 模型来源 （JOB/COS）
        :type TrainingModelSource: str
        :param _TrainingPreference: 模型偏好
        :type TrainingPreference: str
        :param _AutoMLTaskId: 自动学习任务ID（已废弃）
        :type AutoMLTaskId: str
        :param _TrainingJobVersion: 任务版本
        :type TrainingJobVersion: str
        :param _ModelVersionType: 模型版本类型；
枚举值：NORMAL(通用)  ACCELERATE(加速)
注意:  默认为NORMAL
        :type ModelVersionType: str
        :param _ModelFormat: 模型格式 （PYTORCH/TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/PMML/MMDETECTION/ONNX/HUGGING_FACE）
        :type ModelFormat: str
        :param _ReasoningEnvironmentId: 推理镜像ID
        :type ReasoningEnvironmentId: str
        :param _AutoClean: 模型自动清理开关(true/false)，当前版本仅支持SAVED_MODEL格式模型
        :type AutoClean: str
        :param _MaxReservedModels: 模型数量保留上限(默认值为24个，上限为24，下限为1，步长为1)
        :type MaxReservedModels: int
        :param _ModelCleanPeriod: 模型清理周期(默认值为1分钟，上限为1440，下限为1分钟，步长为1)
        :type ModelCleanPeriod: int
        :param _IsQAT: 是否QAT模型
        :type IsQAT: bool
        """
        self._ImportMethod = None
        self._ReasoningEnvironmentSource = None
        self._TrainingModelName = None
        self._Tags = None
        self._TrainingJobName = None
        self._TrainingModelCosPath = None
        self._AlgorithmFramework = None
        self._ReasoningEnvironment = None
        self._TrainingModelIndex = None
        self._TrainingModelVersion = None
        self._ReasoningImageInfo = None
        self._ModelMoveMode = None
        self._TrainingJobId = None
        self._TrainingModelId = None
        self._ModelOutputPath = None
        self._TrainingModelSource = None
        self._TrainingPreference = None
        self._AutoMLTaskId = None
        self._TrainingJobVersion = None
        self._ModelVersionType = None
        self._ModelFormat = None
        self._ReasoningEnvironmentId = None
        self._AutoClean = None
        self._MaxReservedModels = None
        self._ModelCleanPeriod = None
        self._IsQAT = None

    @property
    def ImportMethod(self):
        return self._ImportMethod

    @ImportMethod.setter
    def ImportMethod(self, ImportMethod):
        self._ImportMethod = ImportMethod

    @property
    def ReasoningEnvironmentSource(self):
        return self._ReasoningEnvironmentSource

    @ReasoningEnvironmentSource.setter
    def ReasoningEnvironmentSource(self, ReasoningEnvironmentSource):
        self._ReasoningEnvironmentSource = ReasoningEnvironmentSource

    @property
    def TrainingModelName(self):
        return self._TrainingModelName

    @TrainingModelName.setter
    def TrainingModelName(self, TrainingModelName):
        self._TrainingModelName = TrainingModelName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName

    @property
    def TrainingModelCosPath(self):
        return self._TrainingModelCosPath

    @TrainingModelCosPath.setter
    def TrainingModelCosPath(self, TrainingModelCosPath):
        self._TrainingModelCosPath = TrainingModelCosPath

    @property
    def AlgorithmFramework(self):
        return self._AlgorithmFramework

    @AlgorithmFramework.setter
    def AlgorithmFramework(self, AlgorithmFramework):
        self._AlgorithmFramework = AlgorithmFramework

    @property
    def ReasoningEnvironment(self):
        return self._ReasoningEnvironment

    @ReasoningEnvironment.setter
    def ReasoningEnvironment(self, ReasoningEnvironment):
        self._ReasoningEnvironment = ReasoningEnvironment

    @property
    def TrainingModelIndex(self):
        return self._TrainingModelIndex

    @TrainingModelIndex.setter
    def TrainingModelIndex(self, TrainingModelIndex):
        self._TrainingModelIndex = TrainingModelIndex

    @property
    def TrainingModelVersion(self):
        return self._TrainingModelVersion

    @TrainingModelVersion.setter
    def TrainingModelVersion(self, TrainingModelVersion):
        self._TrainingModelVersion = TrainingModelVersion

    @property
    def ReasoningImageInfo(self):
        return self._ReasoningImageInfo

    @ReasoningImageInfo.setter
    def ReasoningImageInfo(self, ReasoningImageInfo):
        self._ReasoningImageInfo = ReasoningImageInfo

    @property
    def ModelMoveMode(self):
        return self._ModelMoveMode

    @ModelMoveMode.setter
    def ModelMoveMode(self, ModelMoveMode):
        self._ModelMoveMode = ModelMoveMode

    @property
    def TrainingJobId(self):
        return self._TrainingJobId

    @TrainingJobId.setter
    def TrainingJobId(self, TrainingJobId):
        self._TrainingJobId = TrainingJobId

    @property
    def TrainingModelId(self):
        return self._TrainingModelId

    @TrainingModelId.setter
    def TrainingModelId(self, TrainingModelId):
        self._TrainingModelId = TrainingModelId

    @property
    def ModelOutputPath(self):
        return self._ModelOutputPath

    @ModelOutputPath.setter
    def ModelOutputPath(self, ModelOutputPath):
        self._ModelOutputPath = ModelOutputPath

    @property
    def TrainingModelSource(self):
        return self._TrainingModelSource

    @TrainingModelSource.setter
    def TrainingModelSource(self, TrainingModelSource):
        self._TrainingModelSource = TrainingModelSource

    @property
    def TrainingPreference(self):
        return self._TrainingPreference

    @TrainingPreference.setter
    def TrainingPreference(self, TrainingPreference):
        self._TrainingPreference = TrainingPreference

    @property
    def AutoMLTaskId(self):
        return self._AutoMLTaskId

    @AutoMLTaskId.setter
    def AutoMLTaskId(self, AutoMLTaskId):
        self._AutoMLTaskId = AutoMLTaskId

    @property
    def TrainingJobVersion(self):
        return self._TrainingJobVersion

    @TrainingJobVersion.setter
    def TrainingJobVersion(self, TrainingJobVersion):
        self._TrainingJobVersion = TrainingJobVersion

    @property
    def ModelVersionType(self):
        return self._ModelVersionType

    @ModelVersionType.setter
    def ModelVersionType(self, ModelVersionType):
        self._ModelVersionType = ModelVersionType

    @property
    def ModelFormat(self):
        return self._ModelFormat

    @ModelFormat.setter
    def ModelFormat(self, ModelFormat):
        self._ModelFormat = ModelFormat

    @property
    def ReasoningEnvironmentId(self):
        return self._ReasoningEnvironmentId

    @ReasoningEnvironmentId.setter
    def ReasoningEnvironmentId(self, ReasoningEnvironmentId):
        self._ReasoningEnvironmentId = ReasoningEnvironmentId

    @property
    def AutoClean(self):
        return self._AutoClean

    @AutoClean.setter
    def AutoClean(self, AutoClean):
        self._AutoClean = AutoClean

    @property
    def MaxReservedModels(self):
        return self._MaxReservedModels

    @MaxReservedModels.setter
    def MaxReservedModels(self, MaxReservedModels):
        self._MaxReservedModels = MaxReservedModels

    @property
    def ModelCleanPeriod(self):
        return self._ModelCleanPeriod

    @ModelCleanPeriod.setter
    def ModelCleanPeriod(self, ModelCleanPeriod):
        self._ModelCleanPeriod = ModelCleanPeriod

    @property
    def IsQAT(self):
        return self._IsQAT

    @IsQAT.setter
    def IsQAT(self, IsQAT):
        self._IsQAT = IsQAT


    def _deserialize(self, params):
        self._ImportMethod = params.get("ImportMethod")
        self._ReasoningEnvironmentSource = params.get("ReasoningEnvironmentSource")
        self._TrainingModelName = params.get("TrainingModelName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TrainingJobName = params.get("TrainingJobName")
        if params.get("TrainingModelCosPath") is not None:
            self._TrainingModelCosPath = CosPathInfo()
            self._TrainingModelCosPath._deserialize(params.get("TrainingModelCosPath"))
        self._AlgorithmFramework = params.get("AlgorithmFramework")
        self._ReasoningEnvironment = params.get("ReasoningEnvironment")
        self._TrainingModelIndex = params.get("TrainingModelIndex")
        self._TrainingModelVersion = params.get("TrainingModelVersion")
        if params.get("ReasoningImageInfo") is not None:
            self._ReasoningImageInfo = ImageInfo()
            self._ReasoningImageInfo._deserialize(params.get("ReasoningImageInfo"))
        self._ModelMoveMode = params.get("ModelMoveMode")
        self._TrainingJobId = params.get("TrainingJobId")
        self._TrainingModelId = params.get("TrainingModelId")
        if params.get("ModelOutputPath") is not None:
            self._ModelOutputPath = CosPathInfo()
            self._ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        self._TrainingModelSource = params.get("TrainingModelSource")
        self._TrainingPreference = params.get("TrainingPreference")
        self._AutoMLTaskId = params.get("AutoMLTaskId")
        self._TrainingJobVersion = params.get("TrainingJobVersion")
        self._ModelVersionType = params.get("ModelVersionType")
        self._ModelFormat = params.get("ModelFormat")
        self._ReasoningEnvironmentId = params.get("ReasoningEnvironmentId")
        self._AutoClean = params.get("AutoClean")
        self._MaxReservedModels = params.get("MaxReservedModels")
        self._ModelCleanPeriod = params.get("ModelCleanPeriod")
        self._IsQAT = params.get("IsQAT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingModelResponse(AbstractModel):
    """CreateTrainingModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 模型ID，TrainingModel ID
        :type Id: str
        :param _TrainingModelVersionId: 模型版本ID
        :type TrainingModelVersionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._TrainingModelVersionId = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TrainingModelVersionId(self):
        return self._TrainingModelVersionId

    @TrainingModelVersionId.setter
    def TrainingModelVersionId(self, TrainingModelVersionId):
        self._TrainingModelVersionId = TrainingModelVersionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TrainingModelVersionId = params.get("TrainingModelVersionId")
        self._RequestId = params.get("RequestId")


class CreateTrainingTaskRequest(AbstractModel):
    """CreateTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 训练任务名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type Name: str
        :param _ChargeType: 计费模式，eg：PREPAID 包年包月（资源组）;
POSTPAID_BY_HOUR 按量计费
        :type ChargeType: str
        :param _ResourceConfigInfos: 资源配置，需填写对应算力规格ID和节点数量，算力规格ID查询接口为DescribeBillingSpecsPrice，eg：[{"Role":"WORKER", "InstanceType": "TI.S.MEDIUM.POST", "InstanceNum": 1}]
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param _FrameworkName: 训练框架名称，通过DescribeTrainingFrameworks接口查询，eg：SPARK、PYSPARK、TENSORFLOW、PYTORCH
        :type FrameworkName: str
        :param _FrameworkVersion: 训练框架版本，通过DescribeTrainingFrameworks接口查询，eg：1.15、1.9
        :type FrameworkVersion: str
        :param _FrameworkEnvironment: 训练框架环境，通过DescribeTrainingFrameworks接口查询，eg：tf1.15-py3.7-cpu、torch1.9-py3.8-cuda11.1-gpu
        :type FrameworkEnvironment: str
        :param _ResourceGroupId: 预付费专用资源组ID，通过DescribeBillingResourceGroups接口查询
        :type ResourceGroupId: str
        :param _Tags: 标签配置
        :type Tags: list of Tag
        :param _ImageInfo: 自定义镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _CodePackagePath: COS代码包路径
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StartCmdInfo: 启动命令信息，默认为sh start.sh
        :type StartCmdInfo: :class:`tencentcloud.tione.v20211111.models.StartCmdInfo`
        :param _TrainingMode: 训练模式，通过DescribeTrainingFrameworks接口查询，eg：PS_WORKER、DDP、MPI、HOROVOD
        :type TrainingMode: str
        :param _DataConfigs: 数据配置，依赖DataSource字段
        :type DataConfigs: list of DataConfig
        :param _VpcId: VPC Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _Output: COS训练输出路径
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _LogConfig: CLS日志配置
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _TuningParameters: 调优参数
        :type TuningParameters: str
        :param _LogEnable: 是否上报日志
        :type LogEnable: bool
        :param _Remark: 备注，最多500个字
        :type Remark: str
        :param _DataSource: 数据来源，eg：DATASET、COS、CFS、HDFS
        :type DataSource: str
        :param _CallbackUrl: 回调地址，用于创建/启动/停止训练任务的异步回调。回调格式&内容详见：[[TI-ONE接口回调说明]](https://cloud.tencent.com/document/product/851/84292)
        :type CallbackUrl: str
        """
        self._Name = None
        self._ChargeType = None
        self._ResourceConfigInfos = None
        self._FrameworkName = None
        self._FrameworkVersion = None
        self._FrameworkEnvironment = None
        self._ResourceGroupId = None
        self._Tags = None
        self._ImageInfo = None
        self._CodePackagePath = None
        self._StartCmdInfo = None
        self._TrainingMode = None
        self._DataConfigs = None
        self._VpcId = None
        self._SubnetId = None
        self._Output = None
        self._LogConfig = None
        self._TuningParameters = None
        self._LogEnable = None
        self._Remark = None
        self._DataSource = None
        self._CallbackUrl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceConfigInfos(self):
        return self._ResourceConfigInfos

    @ResourceConfigInfos.setter
    def ResourceConfigInfos(self, ResourceConfigInfos):
        self._ResourceConfigInfos = ResourceConfigInfos

    @property
    def FrameworkName(self):
        return self._FrameworkName

    @FrameworkName.setter
    def FrameworkName(self, FrameworkName):
        self._FrameworkName = FrameworkName

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion

    @property
    def FrameworkEnvironment(self):
        return self._FrameworkEnvironment

    @FrameworkEnvironment.setter
    def FrameworkEnvironment(self, FrameworkEnvironment):
        self._FrameworkEnvironment = FrameworkEnvironment

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def CodePackagePath(self):
        return self._CodePackagePath

    @CodePackagePath.setter
    def CodePackagePath(self, CodePackagePath):
        self._CodePackagePath = CodePackagePath

    @property
    def StartCmdInfo(self):
        return self._StartCmdInfo

    @StartCmdInfo.setter
    def StartCmdInfo(self, StartCmdInfo):
        self._StartCmdInfo = StartCmdInfo

    @property
    def TrainingMode(self):
        return self._TrainingMode

    @TrainingMode.setter
    def TrainingMode(self, TrainingMode):
        self._TrainingMode = TrainingMode

    @property
    def DataConfigs(self):
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

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
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def TuningParameters(self):
        return self._TuningParameters

    @TuningParameters.setter
    def TuningParameters(self, TuningParameters):
        self._TuningParameters = TuningParameters

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ChargeType = params.get("ChargeType")
        if params.get("ResourceConfigInfos") is not None:
            self._ResourceConfigInfos = []
            for item in params.get("ResourceConfigInfos"):
                obj = ResourceConfigInfo()
                obj._deserialize(item)
                self._ResourceConfigInfos.append(obj)
        self._FrameworkName = params.get("FrameworkName")
        self._FrameworkVersion = params.get("FrameworkVersion")
        self._FrameworkEnvironment = params.get("FrameworkEnvironment")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodePackagePath") is not None:
            self._CodePackagePath = CosPathInfo()
            self._CodePackagePath._deserialize(params.get("CodePackagePath"))
        if params.get("StartCmdInfo") is not None:
            self._StartCmdInfo = StartCmdInfo()
            self._StartCmdInfo._deserialize(params.get("StartCmdInfo"))
        self._TrainingMode = params.get("TrainingMode")
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("Output") is not None:
            self._Output = CosPathInfo()
            self._Output._deserialize(params.get("Output"))
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._TuningParameters = params.get("TuningParameters")
        self._LogEnable = params.get("LogEnable")
        self._Remark = params.get("Remark")
        self._DataSource = params.get("DataSource")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingTaskResponse(AbstractModel):
    """CreateTrainingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CronInfo(AbstractModel):
    """跑批任务周期描述

    """

    def __init__(self):
        r"""
        :param _CronConfig: cron配置
        :type CronConfig: str
        :param _StartTime: 周期开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 周期结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._CronConfig = None
        self._StartTime = None
        self._EndTime = None

    @property
    def CronConfig(self):
        return self._CronConfig

    @CronConfig.setter
    def CronConfig(self, CronConfig):
        self._CronConfig = CronConfig

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
        self._CronConfig = params.get("CronConfig")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronScaleJob(AbstractModel):
    """定时扩缩任务

    """

    def __init__(self):
        r"""
        :param _Schedule: Cron表达式，标识任务的执行时间，精确到分钟级
        :type Schedule: str
        :param _Name: 定时任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _TargetReplicas: 目标实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetReplicas: int
        :param _MinReplicas: 目标min
注意：此字段可能返回 null，表示取不到有效值。
        :type MinReplicas: int
        :param _MaxReplicas: 目标max
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param _ExcludeDates: 例外时间，Cron表达式，在对应时间内不执行任务。最多支持3条。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeDates: list of str
        """
        self._Schedule = None
        self._Name = None
        self._TargetReplicas = None
        self._MinReplicas = None
        self._MaxReplicas = None
        self._ExcludeDates = None

    @property
    def Schedule(self):
        return self._Schedule

    @Schedule.setter
    def Schedule(self, Schedule):
        self._Schedule = Schedule

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TargetReplicas(self):
        return self._TargetReplicas

    @TargetReplicas.setter
    def TargetReplicas(self, TargetReplicas):
        self._TargetReplicas = TargetReplicas

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def ExcludeDates(self):
        return self._ExcludeDates

    @ExcludeDates.setter
    def ExcludeDates(self, ExcludeDates):
        self._ExcludeDates = ExcludeDates


    def _deserialize(self, params):
        self._Schedule = params.get("Schedule")
        self._Name = params.get("Name")
        self._TargetReplicas = params.get("TargetReplicas")
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._ExcludeDates = params.get("ExcludeDates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CrossTenantENIInfo(AbstractModel):
    """跨租户弹性网卡下Pod调用信息

    """

    def __init__(self):
        r"""
        :param _PrimaryIP: Pod IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrimaryIP: str
        :param _Port: Pod Port
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        """
        self._PrimaryIP = None
        self._Port = None

    @property
    def PrimaryIP(self):
        return self._PrimaryIP

    @PrimaryIP.setter
    def PrimaryIP(self, PrimaryIP):
        self._PrimaryIP = PrimaryIP

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._PrimaryIP = params.get("PrimaryIP")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomTrainingData(AbstractModel):
    """自定义指标

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param _Metrics: 指标
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of CustomTrainingMetric
        """
        self._MetricName = None
        self._Metrics = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = CustomTrainingMetric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomTrainingMetric(AbstractModel):
    """自定义指标

    """

    def __init__(self):
        r"""
        :param _XType: X轴数据类型: TIMESTAMP; EPOCH; STEP
        :type XType: str
        :param _Points: 数据点
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of CustomTrainingPoint
        """
        self._XType = None
        self._Points = None

    @property
    def XType(self):
        return self._XType

    @XType.setter
    def XType(self, XType):
        self._XType = XType

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points


    def _deserialize(self, params):
        self._XType = params.get("XType")
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = CustomTrainingPoint()
                obj._deserialize(item)
                self._Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomTrainingPoint(AbstractModel):
    """自定义训练指标数据点

    """

    def __init__(self):
        r"""
        :param _XValue: X值
        :type XValue: float
        :param _YValue: Y值
        :type YValue: float
        """
        self._XValue = None
        self._YValue = None

    @property
    def XValue(self):
        return self._XValue

    @XValue.setter
    def XValue(self, XValue):
        self._XValue = XValue

    @property
    def YValue(self):
        return self._YValue

    @YValue.setter
    def YValue(self, YValue):
        self._YValue = YValue


    def _deserialize(self, params):
        self._XValue = params.get("XValue")
        self._YValue = params.get("YValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataConfig(AbstractModel):
    """数据配置

    """

    def __init__(self):
        r"""
        :param _MappingPath: 映射路径
        :type MappingPath: str
        :param _DataSourceType: DATASET、COS、CFS、HDFS、WEDATA_HDFS
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceType: str
        :param _DataSetSource: 来自数据集的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSetSource: :class:`tencentcloud.tione.v20211111.models.DataSetConfig`
        :param _COSSource: 来自cos的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type COSSource: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _CFSSource: 来自CFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSSource: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _HDFSSource: 来自HDFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type HDFSSource: :class:`tencentcloud.tione.v20211111.models.HDFSConfig`
        :param _GooseFSSource: 配置GooseFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type GooseFSSource: :class:`tencentcloud.tione.v20211111.models.GooseFS`
        :param _CFSTurboSource: 配置TurboFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSTurboSource: :class:`tencentcloud.tione.v20211111.models.CFSTurbo`
        """
        self._MappingPath = None
        self._DataSourceType = None
        self._DataSetSource = None
        self._COSSource = None
        self._CFSSource = None
        self._HDFSSource = None
        self._GooseFSSource = None
        self._CFSTurboSource = None

    @property
    def MappingPath(self):
        return self._MappingPath

    @MappingPath.setter
    def MappingPath(self, MappingPath):
        self._MappingPath = MappingPath

    @property
    def DataSourceType(self):
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def DataSetSource(self):
        return self._DataSetSource

    @DataSetSource.setter
    def DataSetSource(self, DataSetSource):
        self._DataSetSource = DataSetSource

    @property
    def COSSource(self):
        return self._COSSource

    @COSSource.setter
    def COSSource(self, COSSource):
        self._COSSource = COSSource

    @property
    def CFSSource(self):
        return self._CFSSource

    @CFSSource.setter
    def CFSSource(self, CFSSource):
        self._CFSSource = CFSSource

    @property
    def HDFSSource(self):
        return self._HDFSSource

    @HDFSSource.setter
    def HDFSSource(self, HDFSSource):
        self._HDFSSource = HDFSSource

    @property
    def GooseFSSource(self):
        return self._GooseFSSource

    @GooseFSSource.setter
    def GooseFSSource(self, GooseFSSource):
        self._GooseFSSource = GooseFSSource

    @property
    def CFSTurboSource(self):
        return self._CFSTurboSource

    @CFSTurboSource.setter
    def CFSTurboSource(self, CFSTurboSource):
        self._CFSTurboSource = CFSTurboSource


    def _deserialize(self, params):
        self._MappingPath = params.get("MappingPath")
        self._DataSourceType = params.get("DataSourceType")
        if params.get("DataSetSource") is not None:
            self._DataSetSource = DataSetConfig()
            self._DataSetSource._deserialize(params.get("DataSetSource"))
        if params.get("COSSource") is not None:
            self._COSSource = CosPathInfo()
            self._COSSource._deserialize(params.get("COSSource"))
        if params.get("CFSSource") is not None:
            self._CFSSource = CFSConfig()
            self._CFSSource._deserialize(params.get("CFSSource"))
        if params.get("HDFSSource") is not None:
            self._HDFSSource = HDFSConfig()
            self._HDFSSource._deserialize(params.get("HDFSSource"))
        if params.get("GooseFSSource") is not None:
            self._GooseFSSource = GooseFS()
            self._GooseFSSource._deserialize(params.get("GooseFSSource"))
        if params.get("CFSTurboSource") is not None:
            self._CFSTurboSource = CFSTurbo()
            self._CFSTurboSource._deserialize(params.get("CFSTurboSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataPoint(AbstractModel):
    """数据点

    """

    def __init__(self):
        r"""
        :param _Name: 指标名字
        :type Name: str
        :param _Value: 值
        :type Value: float
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSetConfig(AbstractModel):
    """数据集结构体

    """

    def __init__(self):
        r"""
        :param _Id: 数据集ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasetGroup(AbstractModel):
    """数据集组

    """

    def __init__(self):
        r"""
        :param _DatasetId: 数据集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetId: str
        :param _DatasetName: 数据集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetName: str
        :param _Creator: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _DatasetVersion: 数据集版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetVersion: str
        :param _DatasetType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetType: str
        :param _DatasetTags: 数据集标签
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetTags: list of Tag
        :param _DatasetAnnotationTaskName: 数据集标注任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskName: str
        :param _DatasetAnnotationTaskId: 数据集标注任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskId: str
        :param _Process: 处理进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: int
        :param _DatasetStatus: 数据集状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetStatus: str
        :param _ErrorMsg: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _ExternalTaskType: 外部关联TASKType
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalTaskType: str
        :param _DatasetSize: 数据集大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetSize: str
        :param _FileNum: 数据集数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type FileNum: int
        :param _StorageDataPath: 数据集源COS路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageDataPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StorageLabelPath: 数据集标签存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLabelPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _DatasetVersions: 数据集版本聚合详情
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetVersions: list of DatasetInfo
        :param _AnnotationStatus: 数据集标注状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationStatus: str
        :param _AnnotationType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationType: str
        :param _AnnotationFormat: 数据集标注格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationFormat: str
        :param _DatasetScope: 数据集范围
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetScope: str
        :param _OcrScene: 数据集OCR子场景
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrScene: str
        :param _AnnotationKeyStatus: 数据集字典修改状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationKeyStatus: str
        :param _ContentType: 文本数据集导入方式
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        """
        self._DatasetId = None
        self._DatasetName = None
        self._Creator = None
        self._DatasetVersion = None
        self._DatasetType = None
        self._DatasetTags = None
        self._DatasetAnnotationTaskName = None
        self._DatasetAnnotationTaskId = None
        self._Process = None
        self._DatasetStatus = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ExternalTaskType = None
        self._DatasetSize = None
        self._FileNum = None
        self._StorageDataPath = None
        self._StorageLabelPath = None
        self._DatasetVersions = None
        self._AnnotationStatus = None
        self._AnnotationType = None
        self._AnnotationFormat = None
        self._DatasetScope = None
        self._OcrScene = None
        self._AnnotationKeyStatus = None
        self._ContentType = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

    @property
    def DatasetName(self):
        return self._DatasetName

    @DatasetName.setter
    def DatasetName(self, DatasetName):
        self._DatasetName = DatasetName

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def DatasetVersion(self):
        return self._DatasetVersion

    @DatasetVersion.setter
    def DatasetVersion(self, DatasetVersion):
        self._DatasetVersion = DatasetVersion

    @property
    def DatasetType(self):
        return self._DatasetType

    @DatasetType.setter
    def DatasetType(self, DatasetType):
        self._DatasetType = DatasetType

    @property
    def DatasetTags(self):
        return self._DatasetTags

    @DatasetTags.setter
    def DatasetTags(self, DatasetTags):
        self._DatasetTags = DatasetTags

    @property
    def DatasetAnnotationTaskName(self):
        return self._DatasetAnnotationTaskName

    @DatasetAnnotationTaskName.setter
    def DatasetAnnotationTaskName(self, DatasetAnnotationTaskName):
        self._DatasetAnnotationTaskName = DatasetAnnotationTaskName

    @property
    def DatasetAnnotationTaskId(self):
        return self._DatasetAnnotationTaskId

    @DatasetAnnotationTaskId.setter
    def DatasetAnnotationTaskId(self, DatasetAnnotationTaskId):
        self._DatasetAnnotationTaskId = DatasetAnnotationTaskId

    @property
    def Process(self):
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def DatasetStatus(self):
        return self._DatasetStatus

    @DatasetStatus.setter
    def DatasetStatus(self, DatasetStatus):
        self._DatasetStatus = DatasetStatus

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExternalTaskType(self):
        return self._ExternalTaskType

    @ExternalTaskType.setter
    def ExternalTaskType(self, ExternalTaskType):
        self._ExternalTaskType = ExternalTaskType

    @property
    def DatasetSize(self):
        return self._DatasetSize

    @DatasetSize.setter
    def DatasetSize(self, DatasetSize):
        self._DatasetSize = DatasetSize

    @property
    def FileNum(self):
        return self._FileNum

    @FileNum.setter
    def FileNum(self, FileNum):
        self._FileNum = FileNum

    @property
    def StorageDataPath(self):
        return self._StorageDataPath

    @StorageDataPath.setter
    def StorageDataPath(self, StorageDataPath):
        self._StorageDataPath = StorageDataPath

    @property
    def StorageLabelPath(self):
        return self._StorageLabelPath

    @StorageLabelPath.setter
    def StorageLabelPath(self, StorageLabelPath):
        self._StorageLabelPath = StorageLabelPath

    @property
    def DatasetVersions(self):
        return self._DatasetVersions

    @DatasetVersions.setter
    def DatasetVersions(self, DatasetVersions):
        self._DatasetVersions = DatasetVersions

    @property
    def AnnotationStatus(self):
        return self._AnnotationStatus

    @AnnotationStatus.setter
    def AnnotationStatus(self, AnnotationStatus):
        self._AnnotationStatus = AnnotationStatus

    @property
    def AnnotationType(self):
        return self._AnnotationType

    @AnnotationType.setter
    def AnnotationType(self, AnnotationType):
        self._AnnotationType = AnnotationType

    @property
    def AnnotationFormat(self):
        return self._AnnotationFormat

    @AnnotationFormat.setter
    def AnnotationFormat(self, AnnotationFormat):
        self._AnnotationFormat = AnnotationFormat

    @property
    def DatasetScope(self):
        return self._DatasetScope

    @DatasetScope.setter
    def DatasetScope(self, DatasetScope):
        self._DatasetScope = DatasetScope

    @property
    def OcrScene(self):
        return self._OcrScene

    @OcrScene.setter
    def OcrScene(self, OcrScene):
        self._OcrScene = OcrScene

    @property
    def AnnotationKeyStatus(self):
        return self._AnnotationKeyStatus

    @AnnotationKeyStatus.setter
    def AnnotationKeyStatus(self, AnnotationKeyStatus):
        self._AnnotationKeyStatus = AnnotationKeyStatus

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._DatasetName = params.get("DatasetName")
        self._Creator = params.get("Creator")
        self._DatasetVersion = params.get("DatasetVersion")
        self._DatasetType = params.get("DatasetType")
        if params.get("DatasetTags") is not None:
            self._DatasetTags = []
            for item in params.get("DatasetTags"):
                obj = Tag()
                obj._deserialize(item)
                self._DatasetTags.append(obj)
        self._DatasetAnnotationTaskName = params.get("DatasetAnnotationTaskName")
        self._DatasetAnnotationTaskId = params.get("DatasetAnnotationTaskId")
        self._Process = params.get("Process")
        self._DatasetStatus = params.get("DatasetStatus")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ExternalTaskType = params.get("ExternalTaskType")
        self._DatasetSize = params.get("DatasetSize")
        self._FileNum = params.get("FileNum")
        if params.get("StorageDataPath") is not None:
            self._StorageDataPath = CosPathInfo()
            self._StorageDataPath._deserialize(params.get("StorageDataPath"))
        if params.get("StorageLabelPath") is not None:
            self._StorageLabelPath = CosPathInfo()
            self._StorageLabelPath._deserialize(params.get("StorageLabelPath"))
        if params.get("DatasetVersions") is not None:
            self._DatasetVersions = []
            for item in params.get("DatasetVersions"):
                obj = DatasetInfo()
                obj._deserialize(item)
                self._DatasetVersions.append(obj)
        self._AnnotationStatus = params.get("AnnotationStatus")
        self._AnnotationType = params.get("AnnotationType")
        self._AnnotationFormat = params.get("AnnotationFormat")
        self._DatasetScope = params.get("DatasetScope")
        self._OcrScene = params.get("OcrScene")
        self._AnnotationKeyStatus = params.get("AnnotationKeyStatus")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasetInfo(AbstractModel):
    """数据集详情

    """

    def __init__(self):
        r"""
        :param _DatasetId: 数据集id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetId: str
        :param _DatasetName: 数据集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetName: str
        :param _Creator: 数据集创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param _DatasetVersion: 数据集版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetVersion: str
        :param _DatasetType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetType: str
        :param _DatasetTags: 数据集标签
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetTags: list of Tag
        :param _DatasetAnnotationTaskName: 数据集对应标注任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskName: str
        :param _DatasetAnnotationTaskId: 数据集对应标注任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskId: str
        :param _Process: 处理进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: int
        :param _DatasetStatus: 数据集状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetStatus: str
        :param _ErrorMsg: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _CreateTime: 数据集创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 数据集更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _ExternalTaskType: 外部任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalTaskType: str
        :param _DatasetSize: 数据集存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetSize: str
        :param _FileNum: 数据集数据数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FileNum: int
        :param _StorageDataPath: 数据集源cos 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageDataPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StorageLabelPath: 数据集输出cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLabelPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _AnnotationStatus: 数据集标注状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationStatus: str
        :param _AnnotationType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationType: str
        :param _AnnotationFormat: 数据集标注格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationFormat: str
        :param _DatasetScope: 数据集范围
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetScope: str
        :param _OcrScene: 数据集OCR子场景
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrScene: str
        :param _AnnotationKeyStatus: 数据集字典修改状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationKeyStatus: str
        """
        self._DatasetId = None
        self._DatasetName = None
        self._Creator = None
        self._DatasetVersion = None
        self._DatasetType = None
        self._DatasetTags = None
        self._DatasetAnnotationTaskName = None
        self._DatasetAnnotationTaskId = None
        self._Process = None
        self._DatasetStatus = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ExternalTaskType = None
        self._DatasetSize = None
        self._FileNum = None
        self._StorageDataPath = None
        self._StorageLabelPath = None
        self._AnnotationStatus = None
        self._AnnotationType = None
        self._AnnotationFormat = None
        self._DatasetScope = None
        self._OcrScene = None
        self._AnnotationKeyStatus = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

    @property
    def DatasetName(self):
        return self._DatasetName

    @DatasetName.setter
    def DatasetName(self, DatasetName):
        self._DatasetName = DatasetName

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def DatasetVersion(self):
        return self._DatasetVersion

    @DatasetVersion.setter
    def DatasetVersion(self, DatasetVersion):
        self._DatasetVersion = DatasetVersion

    @property
    def DatasetType(self):
        return self._DatasetType

    @DatasetType.setter
    def DatasetType(self, DatasetType):
        self._DatasetType = DatasetType

    @property
    def DatasetTags(self):
        return self._DatasetTags

    @DatasetTags.setter
    def DatasetTags(self, DatasetTags):
        self._DatasetTags = DatasetTags

    @property
    def DatasetAnnotationTaskName(self):
        return self._DatasetAnnotationTaskName

    @DatasetAnnotationTaskName.setter
    def DatasetAnnotationTaskName(self, DatasetAnnotationTaskName):
        self._DatasetAnnotationTaskName = DatasetAnnotationTaskName

    @property
    def DatasetAnnotationTaskId(self):
        return self._DatasetAnnotationTaskId

    @DatasetAnnotationTaskId.setter
    def DatasetAnnotationTaskId(self, DatasetAnnotationTaskId):
        self._DatasetAnnotationTaskId = DatasetAnnotationTaskId

    @property
    def Process(self):
        return self._Process

    @Process.setter
    def Process(self, Process):
        self._Process = Process

    @property
    def DatasetStatus(self):
        return self._DatasetStatus

    @DatasetStatus.setter
    def DatasetStatus(self, DatasetStatus):
        self._DatasetStatus = DatasetStatus

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ExternalTaskType(self):
        return self._ExternalTaskType

    @ExternalTaskType.setter
    def ExternalTaskType(self, ExternalTaskType):
        self._ExternalTaskType = ExternalTaskType

    @property
    def DatasetSize(self):
        return self._DatasetSize

    @DatasetSize.setter
    def DatasetSize(self, DatasetSize):
        self._DatasetSize = DatasetSize

    @property
    def FileNum(self):
        return self._FileNum

    @FileNum.setter
    def FileNum(self, FileNum):
        self._FileNum = FileNum

    @property
    def StorageDataPath(self):
        return self._StorageDataPath

    @StorageDataPath.setter
    def StorageDataPath(self, StorageDataPath):
        self._StorageDataPath = StorageDataPath

    @property
    def StorageLabelPath(self):
        return self._StorageLabelPath

    @StorageLabelPath.setter
    def StorageLabelPath(self, StorageLabelPath):
        self._StorageLabelPath = StorageLabelPath

    @property
    def AnnotationStatus(self):
        return self._AnnotationStatus

    @AnnotationStatus.setter
    def AnnotationStatus(self, AnnotationStatus):
        self._AnnotationStatus = AnnotationStatus

    @property
    def AnnotationType(self):
        return self._AnnotationType

    @AnnotationType.setter
    def AnnotationType(self, AnnotationType):
        self._AnnotationType = AnnotationType

    @property
    def AnnotationFormat(self):
        return self._AnnotationFormat

    @AnnotationFormat.setter
    def AnnotationFormat(self, AnnotationFormat):
        self._AnnotationFormat = AnnotationFormat

    @property
    def DatasetScope(self):
        return self._DatasetScope

    @DatasetScope.setter
    def DatasetScope(self, DatasetScope):
        self._DatasetScope = DatasetScope

    @property
    def OcrScene(self):
        return self._OcrScene

    @OcrScene.setter
    def OcrScene(self, OcrScene):
        self._OcrScene = OcrScene

    @property
    def AnnotationKeyStatus(self):
        return self._AnnotationKeyStatus

    @AnnotationKeyStatus.setter
    def AnnotationKeyStatus(self, AnnotationKeyStatus):
        self._AnnotationKeyStatus = AnnotationKeyStatus


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._DatasetName = params.get("DatasetName")
        self._Creator = params.get("Creator")
        self._DatasetVersion = params.get("DatasetVersion")
        self._DatasetType = params.get("DatasetType")
        if params.get("DatasetTags") is not None:
            self._DatasetTags = []
            for item in params.get("DatasetTags"):
                obj = Tag()
                obj._deserialize(item)
                self._DatasetTags.append(obj)
        self._DatasetAnnotationTaskName = params.get("DatasetAnnotationTaskName")
        self._DatasetAnnotationTaskId = params.get("DatasetAnnotationTaskId")
        self._Process = params.get("Process")
        self._DatasetStatus = params.get("DatasetStatus")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ExternalTaskType = params.get("ExternalTaskType")
        self._DatasetSize = params.get("DatasetSize")
        self._FileNum = params.get("FileNum")
        if params.get("StorageDataPath") is not None:
            self._StorageDataPath = CosPathInfo()
            self._StorageDataPath._deserialize(params.get("StorageDataPath"))
        if params.get("StorageLabelPath") is not None:
            self._StorageLabelPath = CosPathInfo()
            self._StorageLabelPath._deserialize(params.get("StorageLabelPath"))
        self._AnnotationStatus = params.get("AnnotationStatus")
        self._AnnotationType = params.get("AnnotationType")
        self._AnnotationFormat = params.get("AnnotationFormat")
        self._DatasetScope = params.get("DatasetScope")
        self._OcrScene = params.get("OcrScene")
        self._AnnotationKeyStatus = params.get("AnnotationKeyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultNginxGatewayCallInfo(AbstractModel):
    """默认Nginx网关结构

    """

    def __init__(self):
        r"""
        :param _Host: host
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        """
        self._Host = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBatchTaskRequest(AbstractModel):
    """DeleteBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        """
        self._BatchTaskId = None

    @property
    def BatchTaskId(self):
        return self._BatchTaskId

    @BatchTaskId.setter
    def BatchTaskId(self, BatchTaskId):
        self._BatchTaskId = BatchTaskId


    def _deserialize(self, params):
        self._BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBatchTaskResponse(AbstractModel):
    """DeleteBatchTask返回参数结构体

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


class DeleteDatasetRequest(AbstractModel):
    """DeleteDataset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasetId: 数据集id
        :type DatasetId: str
        :param _DeleteLabelEnable: 是否删除cos标签文件
        :type DeleteLabelEnable: bool
        """
        self._DatasetId = None
        self._DeleteLabelEnable = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

    @property
    def DeleteLabelEnable(self):
        return self._DeleteLabelEnable

    @DeleteLabelEnable.setter
    def DeleteLabelEnable(self, DeleteLabelEnable):
        self._DeleteLabelEnable = DeleteLabelEnable


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._DeleteLabelEnable = params.get("DeleteLabelEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDatasetResponse(AbstractModel):
    """DeleteDataset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasetId: 删除的datasetId
        :type DatasetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DatasetId = None
        self._RequestId = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._RequestId = params.get("RequestId")


class DeleteModelAccelerateTaskRequest(AbstractModel):
    """DeleteModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        """
        self._ModelAccTaskId = None

    @property
    def ModelAccTaskId(self):
        return self._ModelAccTaskId

    @ModelAccTaskId.setter
    def ModelAccTaskId(self, ModelAccTaskId):
        self._ModelAccTaskId = ModelAccTaskId


    def _deserialize(self, params):
        self._ModelAccTaskId = params.get("ModelAccTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelAccelerateTaskResponse(AbstractModel):
    """DeleteModelAccelerateTask返回参数结构体

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


class DeleteModelServiceGroupRequest(AbstractModel):
    """DeleteModelServiceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 服务id
        :type ServiceGroupId: str
        """
        self._ServiceGroupId = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelServiceGroupResponse(AbstractModel):
    """DeleteModelServiceGroup返回参数结构体

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


class DeleteModelServiceRequest(AbstractModel):
    """DeleteModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务id
        :type ServiceId: str
        :param _ServiceCategory: 服务分类
        :type ServiceCategory: str
        """
        self._ServiceId = None
        self._ServiceCategory = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceCategory(self):
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
        self._ServiceCategory = ServiceCategory


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceCategory = params.get("ServiceCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelServiceResponse(AbstractModel):
    """DeleteModelService返回参数结构体

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


class DeleteNotebookImageRecordRequest(AbstractModel):
    """DeleteNotebookImageRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录id
        :type RecordId: str
        """
        self._RecordId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookImageRecordResponse(AbstractModel):
    """DeleteNotebookImageRecord返回参数结构体

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


class DeleteNotebookRequest(AbstractModel):
    """DeleteNotebook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: notebook id
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNotebookResponse(AbstractModel):
    """DeleteNotebook返回参数结构体

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


class DeleteTrainingModelRequest(AbstractModel):
    """DeleteTrainingModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingModelId: 模型ID
        :type TrainingModelId: str
        :param _EnableDeleteCos: 是否同步清理cos
        :type EnableDeleteCos: bool
        :param _ModelVersionType: 删除模型类型，枚举值：NORMAL 普通，ACCELERATE 加速，不传则删除所有
        :type ModelVersionType: str
        """
        self._TrainingModelId = None
        self._EnableDeleteCos = None
        self._ModelVersionType = None

    @property
    def TrainingModelId(self):
        return self._TrainingModelId

    @TrainingModelId.setter
    def TrainingModelId(self, TrainingModelId):
        self._TrainingModelId = TrainingModelId

    @property
    def EnableDeleteCos(self):
        return self._EnableDeleteCos

    @EnableDeleteCos.setter
    def EnableDeleteCos(self, EnableDeleteCos):
        self._EnableDeleteCos = EnableDeleteCos

    @property
    def ModelVersionType(self):
        return self._ModelVersionType

    @ModelVersionType.setter
    def ModelVersionType(self, ModelVersionType):
        self._ModelVersionType = ModelVersionType


    def _deserialize(self, params):
        self._TrainingModelId = params.get("TrainingModelId")
        self._EnableDeleteCos = params.get("EnableDeleteCos")
        self._ModelVersionType = params.get("ModelVersionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrainingModelResponse(AbstractModel):
    """DeleteTrainingModel返回参数结构体

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


class DeleteTrainingModelVersionRequest(AbstractModel):
    """DeleteTrainingModelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingModelVersionId: 模型版本ID
        :type TrainingModelVersionId: str
        :param _EnableDeleteCos: 是否同步清理cos
        :type EnableDeleteCos: bool
        """
        self._TrainingModelVersionId = None
        self._EnableDeleteCos = None

    @property
    def TrainingModelVersionId(self):
        return self._TrainingModelVersionId

    @TrainingModelVersionId.setter
    def TrainingModelVersionId(self, TrainingModelVersionId):
        self._TrainingModelVersionId = TrainingModelVersionId

    @property
    def EnableDeleteCos(self):
        return self._EnableDeleteCos

    @EnableDeleteCos.setter
    def EnableDeleteCos(self, EnableDeleteCos):
        self._EnableDeleteCos = EnableDeleteCos


    def _deserialize(self, params):
        self._TrainingModelVersionId = params.get("TrainingModelVersionId")
        self._EnableDeleteCos = params.get("EnableDeleteCos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrainingModelVersionResponse(AbstractModel):
    """DeleteTrainingModelVersion返回参数结构体

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


class DeleteTrainingTaskRequest(AbstractModel):
    """DeleteTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrainingTaskResponse(AbstractModel):
    """DeleteTrainingTask返回参数结构体

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


class DescribeAPIConfigsRequest(AbstractModel):
    """DescribeAPIConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        :param _Filters: 分页参数，支持的分页过滤Name包括：
["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId"]
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._Filters = None

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
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
        


class DescribeAPIConfigsResponse(AbstractModel):
    """DescribeAPIConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 接口数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Details: 接口详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of APIConfigDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Details = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = APIConfigDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBatchTaskInstancesRequest(AbstractModel):
    """DescribeBatchTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTaskId: 跑批任务id
        :type BatchTaskId: str
        """
        self._BatchTaskId = None

    @property
    def BatchTaskId(self):
        return self._BatchTaskId

    @BatchTaskId.setter
    def BatchTaskId(self, BatchTaskId):
        self._BatchTaskId = BatchTaskId


    def _deserialize(self, params):
        self._BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskInstancesResponse(AbstractModel):
    """DescribeBatchTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchInstances: 实例集
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchInstances: list of BatchTaskInstance
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchInstances = None
        self._RequestId = None

    @property
    def BatchInstances(self):
        return self._BatchInstances

    @BatchInstances.setter
    def BatchInstances(self, BatchInstances):
        self._BatchInstances = BatchInstances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BatchInstances") is not None:
            self._BatchInstances = []
            for item in params.get("BatchInstances"):
                obj = BatchTaskInstance()
                obj._deserialize(item)
                self._BatchInstances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBatchTaskRequest(AbstractModel):
    """DescribeBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        """
        self._BatchTaskId = None

    @property
    def BatchTaskId(self):
        return self._BatchTaskId

    @BatchTaskId.setter
    def BatchTaskId(self, BatchTaskId):
        self._BatchTaskId = BatchTaskId


    def _deserialize(self, params):
        self._BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskResponse(AbstractModel):
    """DescribeBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTaskDetail: 跑批任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchTaskDetail: :class:`tencentcloud.tione.v20211111.models.BatchTaskDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchTaskDetail = None
        self._RequestId = None

    @property
    def BatchTaskDetail(self):
        return self._BatchTaskDetail

    @BatchTaskDetail.setter
    def BatchTaskDetail(self, BatchTaskDetail):
        self._BatchTaskDetail = BatchTaskDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BatchTaskDetail") is not None:
            self._BatchTaskDetail = BatchTaskDetail()
            self._BatchTaskDetail._deserialize(params.get("BatchTaskDetail"))
        self._RequestId = params.get("RequestId")


class DescribeBatchTasksRequest(AbstractModel):
    """DescribeBatchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤器，eg：[{ "Name": "Id", "Values": ["train-23091792777383936"] }]

取值范围：
Name（名称）：task1
Id（task ID）：train-23091792777383936
Status（状态）：STARTING / RUNNING / STOPPING / STOPPED / FAILED / SUCCEED / SUBMIT_FAILED
ChargeType（计费类型）：PREPAID 包年包月 / POSTPAID_BY_HOUR 按量计费
CHARGE_STATUS（计费状态）：NOT_BILLING（未开始计费）/ BILLING（计费中）/ ARREARS_STOP（欠费停止）
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤器，eg：[{ "TagKey": "TagKeyA", "TagValue": ["TagValueA"] }]
        :type TagFilters: list of TagFilter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为10，最大为50
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC（升序排列）/ DESC（降序排列），默认为DESC
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        """
        self._Filters = None
        self._TagFilters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTasksResponse(AbstractModel):
    """DescribeBatchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _BatchTaskSet: 任务集
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchTaskSet: list of BatchTaskSetItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BatchTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BatchTaskSet(self):
        return self._BatchTaskSet

    @BatchTaskSet.setter
    def BatchTaskSet(self, BatchTaskSet):
        self._BatchTaskSet = BatchTaskSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BatchTaskSet") is not None:
            self._BatchTaskSet = []
            for item in params.get("BatchTaskSet"):
                obj = BatchTaskSetItem()
                obj._deserialize(item)
                self._BatchTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillingResourceGroupsRequest(AbstractModel):
    """DescribeBillingResourceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 资源组类型; 枚举值 TRAIN:训练 INFERENCE:推理
        :type Type: str
        :param _Filters: Filter.Name: 枚举值: ResourceGroupId (资源组id列表)
                    ResourceGroupName (资源组名称列表)
Filter.Values: 长度为1且Filter.Fuzzy=true时，支持模糊查询; 不为1时，精确查询
每次请求的Filters的上限为5，Filter.Values的上限为100
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        :param _Offset: 偏移量，默认为0；分页查询起始位置，如：Limit为100，第一页Offset为0，第二页OffSet为100....即每页左边为闭区间
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为30;
注意：小于0则默认为20；大于30则默认为30
        :type Limit: int
        :param _SearchWord: 支持模糊查找资源组id和资源组名
        :type SearchWord: str
        :param _DontShowInstanceSet: 是否不展示节点列表; 
true: 不展示，false 展示；
默认为false
        :type DontShowInstanceSet: bool
        """
        self._Type = None
        self._Filters = None
        self._TagFilters = None
        self._Offset = None
        self._Limit = None
        self._SearchWord = None
        self._DontShowInstanceSet = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

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
    def SearchWord(self):
        return self._SearchWord

    @SearchWord.setter
    def SearchWord(self, SearchWord):
        self._SearchWord = SearchWord

    @property
    def DontShowInstanceSet(self):
        return self._DontShowInstanceSet

    @DontShowInstanceSet.setter
    def DontShowInstanceSet(self, DontShowInstanceSet):
        self._DontShowInstanceSet = DontShowInstanceSet


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchWord = params.get("SearchWord")
        self._DontShowInstanceSet = params.get("DontShowInstanceSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingResourceGroupsResponse(AbstractModel):
    """DescribeBillingResourceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资源组总数； 注意接口是分页拉取的，total是指资源组总数，不是本次返回中ResourceGroupSet数组的大小
        :type TotalCount: int
        :param _ResourceGroupSet: 资源组详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupSet: list of ResourceGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResourceGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResourceGroupSet(self):
        return self._ResourceGroupSet

    @ResourceGroupSet.setter
    def ResourceGroupSet(self, ResourceGroupSet):
        self._ResourceGroupSet = ResourceGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ResourceGroupSet") is not None:
            self._ResourceGroupSet = []
            for item in params.get("ResourceGroupSet"):
                obj = ResourceGroup()
                obj._deserialize(item)
                self._ResourceGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillingResourceInstanceRunningJobsRequest(AbstractModel):
    """DescribeBillingResourceInstanceRunningJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceGroupId: 资源组id
        :type ResourceGroupId: str
        :param _ResourceInstanceId: 资源组节点id
        :type ResourceInstanceId: str
        """
        self._ResourceGroupId = None
        self._ResourceInstanceId = None

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceInstanceId(self):
        return self._ResourceInstanceId

    @ResourceInstanceId.setter
    def ResourceInstanceId(self, ResourceInstanceId):
        self._ResourceInstanceId = ResourceInstanceId


    def _deserialize(self, params):
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceInstanceId = params.get("ResourceInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingResourceInstanceRunningJobsResponse(AbstractModel):
    """DescribeBillingResourceInstanceRunningJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceInstanceRunningJobInfos: 资源组节点运行中的任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceInstanceRunningJobInfos: list of ResourceInstanceRunningJobInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceInstanceRunningJobInfos = None
        self._RequestId = None

    @property
    def ResourceInstanceRunningJobInfos(self):
        return self._ResourceInstanceRunningJobInfos

    @ResourceInstanceRunningJobInfos.setter
    def ResourceInstanceRunningJobInfos(self, ResourceInstanceRunningJobInfos):
        self._ResourceInstanceRunningJobInfos = ResourceInstanceRunningJobInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResourceInstanceRunningJobInfos") is not None:
            self._ResourceInstanceRunningJobInfos = []
            for item in params.get("ResourceInstanceRunningJobInfos"):
                obj = ResourceInstanceRunningJobInfo()
                obj._deserialize(item)
                self._ResourceInstanceRunningJobInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillingSpecsPriceRequest(AbstractModel):
    """DescribeBillingSpecsPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpecsParam: 询价参数，支持批量询价
        :type SpecsParam: list of SpecUnit
        """
        self._SpecsParam = None

    @property
    def SpecsParam(self):
        return self._SpecsParam

    @SpecsParam.setter
    def SpecsParam(self, SpecsParam):
        self._SpecsParam = SpecsParam


    def _deserialize(self, params):
        if params.get("SpecsParam") is not None:
            self._SpecsParam = []
            for item in params.get("SpecsParam"):
                obj = SpecUnit()
                obj._deserialize(item)
                self._SpecsParam.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingSpecsPriceResponse(AbstractModel):
    """DescribeBillingSpecsPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpecsPrice: 计费项价格，支持批量返回
        :type SpecsPrice: list of SpecPrice
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpecsPrice = None
        self._RequestId = None

    @property
    def SpecsPrice(self):
        return self._SpecsPrice

    @SpecsPrice.setter
    def SpecsPrice(self, SpecsPrice):
        self._SpecsPrice = SpecsPrice

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SpecsPrice") is not None:
            self._SpecsPrice = []
            for item in params.get("SpecsPrice"):
                obj = SpecPrice()
                obj._deserialize(item)
                self._SpecsPrice.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBillingSpecsRequest(AbstractModel):
    """DescribeBillingSpecs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskType: 枚举值：TRAIN、NOTEBOOK、INFERENCE
        :type TaskType: str
        :param _ChargeType: 付费模式：POSTPAID_BY_HOUR按量计费、PREPAID包年包月
        :type ChargeType: str
        :param _ResourceType: 资源类型：CALC 计算资源、CPU CPU资源、GPU GPU资源、CBS云硬盘
        :type ResourceType: str
        """
        self._TaskType = None
        self._ChargeType = None
        self._ResourceType = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._ChargeType = params.get("ChargeType")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingSpecsResponse(AbstractModel):
    """DescribeBillingSpecs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Specs: 计费项列表
        :type Specs: list of Spec
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Specs = None
        self._RequestId = None

    @property
    def Specs(self):
        return self._Specs

    @Specs.setter
    def Specs(self, Specs):
        self._Specs = Specs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Specs") is not None:
            self._Specs = []
            for item in params.get("Specs"):
                obj = Spec()
                obj._deserialize(item)
                self._Specs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatasetDetailStructuredRequest(AbstractModel):
    """DescribeDatasetDetailStructured请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasetId: 数据集ID
        :type DatasetId: str
        :param _Offset: 偏移值
        :type Offset: int
        :param _Limit: 返回数据条数，默认20，目前最大支持2000条数据
        :type Limit: int
        """
        self._DatasetId = None
        self._Offset = None
        self._Limit = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

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


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasetDetailStructuredResponse(AbstractModel):
    """DescribeDatasetDetailStructured返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ColumnNames: 表格头信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnNames: list of str
        :param _RowItems: 表格内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RowItems: list of RowItem
        :param _RowTexts: 文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RowTexts: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ColumnNames = None
        self._RowItems = None
        self._RowTexts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ColumnNames(self):
        return self._ColumnNames

    @ColumnNames.setter
    def ColumnNames(self, ColumnNames):
        self._ColumnNames = ColumnNames

    @property
    def RowItems(self):
        return self._RowItems

    @RowItems.setter
    def RowItems(self, RowItems):
        self._RowItems = RowItems

    @property
    def RowTexts(self):
        return self._RowTexts

    @RowTexts.setter
    def RowTexts(self, RowTexts):
        self._RowTexts = RowTexts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._ColumnNames = params.get("ColumnNames")
        if params.get("RowItems") is not None:
            self._RowItems = []
            for item in params.get("RowItems"):
                obj = RowItem()
                obj._deserialize(item)
                self._RowItems.append(obj)
        self._RowTexts = params.get("RowTexts")
        self._RequestId = params.get("RequestId")


class DescribeDatasetDetailUnstructuredRequest(AbstractModel):
    """DescribeDatasetDetailUnstructured请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasetId: 数据集ID
        :type DatasetId: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回个数，默认20，目前最大支持2000条数据
        :type Limit: int
        :param _LabelList: 标签过滤参数，对应标签值
        :type LabelList: list of str
        :param _AnnotationStatus: 标注状态过滤参数:
STATUS_ANNOTATED，已标注
STATUS_NON_ANNOTATED，未标注
STATUS_ALL，全部
默认为STATUS_ALL
        :type AnnotationStatus: str
        :param _DatasetIds: 数据集ID列表
        :type DatasetIds: list of str
        :param _TextClassificationLabels: 要筛选的文本分类场景标签信息
        :type TextClassificationLabels: list of TextLabelDistributionInfo
        """
        self._DatasetId = None
        self._Offset = None
        self._Limit = None
        self._LabelList = None
        self._AnnotationStatus = None
        self._DatasetIds = None
        self._TextClassificationLabels = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

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
    def LabelList(self):
        return self._LabelList

    @LabelList.setter
    def LabelList(self, LabelList):
        self._LabelList = LabelList

    @property
    def AnnotationStatus(self):
        return self._AnnotationStatus

    @AnnotationStatus.setter
    def AnnotationStatus(self, AnnotationStatus):
        self._AnnotationStatus = AnnotationStatus

    @property
    def DatasetIds(self):
        return self._DatasetIds

    @DatasetIds.setter
    def DatasetIds(self, DatasetIds):
        self._DatasetIds = DatasetIds

    @property
    def TextClassificationLabels(self):
        return self._TextClassificationLabels

    @TextClassificationLabels.setter
    def TextClassificationLabels(self, TextClassificationLabels):
        self._TextClassificationLabels = TextClassificationLabels


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._LabelList = params.get("LabelList")
        self._AnnotationStatus = params.get("AnnotationStatus")
        self._DatasetIds = params.get("DatasetIds")
        if params.get("TextClassificationLabels") is not None:
            self._TextClassificationLabels = []
            for item in params.get("TextClassificationLabels"):
                obj = TextLabelDistributionInfo()
                obj._deserialize(item)
                self._TextClassificationLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasetDetailUnstructuredResponse(AbstractModel):
    """DescribeDatasetDetailUnstructured返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AnnotatedTotalCount: 已标注数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotatedTotalCount: int
        :param _NonAnnotatedTotalCount: 没有标注数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type NonAnnotatedTotalCount: int
        :param _FilterTotalCount: 过滤数据总量
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterTotalCount: int
        :param _FilterLabelList: 过滤数据详情
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterLabelList: list of FilterLabelInfo
        :param _RowTexts: 数据文本行，默认返回前1000行
注意：此字段可能返回 null，表示取不到有效值。
        :type RowTexts: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AnnotatedTotalCount = None
        self._NonAnnotatedTotalCount = None
        self._FilterTotalCount = None
        self._FilterLabelList = None
        self._RowTexts = None
        self._RequestId = None

    @property
    def AnnotatedTotalCount(self):
        return self._AnnotatedTotalCount

    @AnnotatedTotalCount.setter
    def AnnotatedTotalCount(self, AnnotatedTotalCount):
        self._AnnotatedTotalCount = AnnotatedTotalCount

    @property
    def NonAnnotatedTotalCount(self):
        return self._NonAnnotatedTotalCount

    @NonAnnotatedTotalCount.setter
    def NonAnnotatedTotalCount(self, NonAnnotatedTotalCount):
        self._NonAnnotatedTotalCount = NonAnnotatedTotalCount

    @property
    def FilterTotalCount(self):
        return self._FilterTotalCount

    @FilterTotalCount.setter
    def FilterTotalCount(self, FilterTotalCount):
        self._FilterTotalCount = FilterTotalCount

    @property
    def FilterLabelList(self):
        return self._FilterLabelList

    @FilterLabelList.setter
    def FilterLabelList(self, FilterLabelList):
        self._FilterLabelList = FilterLabelList

    @property
    def RowTexts(self):
        return self._RowTexts

    @RowTexts.setter
    def RowTexts(self, RowTexts):
        self._RowTexts = RowTexts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AnnotatedTotalCount = params.get("AnnotatedTotalCount")
        self._NonAnnotatedTotalCount = params.get("NonAnnotatedTotalCount")
        self._FilterTotalCount = params.get("FilterTotalCount")
        if params.get("FilterLabelList") is not None:
            self._FilterLabelList = []
            for item in params.get("FilterLabelList"):
                obj = FilterLabelInfo()
                obj._deserialize(item)
                self._FilterLabelList.append(obj)
        self._RowTexts = params.get("RowTexts")
        self._RequestId = params.get("RequestId")


class DescribeDatasetsRequest(AbstractModel):
    """DescribeDatasets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DatasetIds: 数据集id列表
        :type DatasetIds: list of str
        :param _Filters: 数据集查询过滤条件，多个Filter之间的关系为逻辑与（AND）关系，过滤字段Filter.Name，类型为String
DatasetName，数据集名称
DatasetScope，数据集范围，SCOPE_DATASET_PRIVATE或SCOPE_DATASET_PUBLIC
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        :param _Order: 排序值，支持Asc或Desc，默认Desc
        :type Order: str
        :param _OrderField: 排序字段，支持CreateTime或UpdateTime，默认CreateTime
        :type OrderField: str
        :param _Offset: 偏移值
        :type Offset: int
        :param _Limit: 返回数据个数，默认20，最大支持200
        :type Limit: int
        """
        self._DatasetIds = None
        self._Filters = None
        self._TagFilters = None
        self._Order = None
        self._OrderField = None
        self._Offset = None
        self._Limit = None

    @property
    def DatasetIds(self):
        return self._DatasetIds

    @DatasetIds.setter
    def DatasetIds(self, DatasetIds):
        self._DatasetIds = DatasetIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

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


    def _deserialize(self, params):
        self._DatasetIds = params.get("DatasetIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasetsResponse(AbstractModel):
    """DescribeDatasets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据集总量（名称维度）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _DatasetGroups: 数据集按照数据集名称聚合的分组
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetGroups: list of DatasetGroup
        :param _DatasetIdNums: 数据集ID总量
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetIdNums: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DatasetGroups = None
        self._DatasetIdNums = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DatasetGroups(self):
        return self._DatasetGroups

    @DatasetGroups.setter
    def DatasetGroups(self, DatasetGroups):
        self._DatasetGroups = DatasetGroups

    @property
    def DatasetIdNums(self):
        return self._DatasetIdNums

    @DatasetIdNums.setter
    def DatasetIdNums(self, DatasetIdNums):
        self._DatasetIdNums = DatasetIdNums

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DatasetGroups") is not None:
            self._DatasetGroups = []
            for item in params.get("DatasetGroups"):
                obj = DatasetGroup()
                obj._deserialize(item)
                self._DatasetGroups.append(obj)
        self._DatasetIdNums = params.get("DatasetIdNums")
        self._RequestId = params.get("RequestId")


class DescribeInferTemplatesRequest(AbstractModel):
    """DescribeInferTemplates请求参数结构体

    """


class DescribeInferTemplatesResponse(AbstractModel):
    """DescribeInferTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FrameworkTemplates: 模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkTemplates: list of InferTemplateGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FrameworkTemplates = None
        self._RequestId = None

    @property
    def FrameworkTemplates(self):
        return self._FrameworkTemplates

    @FrameworkTemplates.setter
    def FrameworkTemplates(self, FrameworkTemplates):
        self._FrameworkTemplates = FrameworkTemplates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FrameworkTemplates") is not None:
            self._FrameworkTemplates = []
            for item in params.get("FrameworkTemplates"):
                obj = InferTemplateGroup()
                obj._deserialize(item)
                self._FrameworkTemplates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLatestTrainingMetricsRequest(AbstractModel):
    """DescribeLatestTrainingMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLatestTrainingMetricsResponse(AbstractModel):
    """DescribeLatestTrainingMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Metrics: 最近一次上报的训练指标.每个Metric中只有一个点的数据, 即len(Values) = len(Timestamps) = 1
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of TrainingMetric
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Metrics = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = TrainingMetric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogsRequest(AbstractModel):
    """DescribeLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 查询哪个服务的事件（可选值为TRAIN, NOTEBOOK, INFER）
        :type Service: str
        :param _StartTime: 日志查询开始时间（RFC3339格式的时间字符串），默认值为当前时间的前一个小时
        :type StartTime: str
        :param _EndTime: 日志查询结束时间（RFC3339格式的时间字符串），默认值为当前时间
        :type EndTime: str
        :param _Limit: 日志查询条数，默认值100，最大值100
        :type Limit: int
        :param _PodName: 查询哪个Pod的日志（支持结尾通配符*)
        :type PodName: str
        :param _Order: 排序方向（可选值为ASC, DESC ），默认为DESC
        :type Order: str
        :param _OrderField: 按哪个字段排序（可选值为Timestamp），默认值为Timestamp
        :type OrderField: str
        :param _Context: 日志查询上下文，查询下一页的时候需要回传这个字段，该字段来自本接口的返回
        :type Context: str
        :param _Filters: 过滤条件
注意: 
1. Filter.Name：目前只支持Key（也就是按关键字过滤日志）
2. Filter.Values：表示过滤日志的关键字；Values为多个的时候表示同时满足
3. Filter. Negative和Filter. Fuzzy没有使用
        :type Filters: list of Filter
        """
        self._Service = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._PodName = None
        self._Order = None
        self._OrderField = None
        self._Context = None
        self._Filters = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._PodName = params.get("PodName")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        self._Context = params.get("Context")
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
        


class DescribeLogsResponse(AbstractModel):
    """DescribeLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 分页的游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _Content: 日志数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of LogIdentity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Content = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = LogIdentity()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModelAccEngineVersionsRequest(AbstractModel):
    """DescribeModelAccEngineVersions请求参数结构体

    """


class DescribeModelAccEngineVersionsResponse(AbstractModel):
    """DescribeModelAccEngineVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccEngineVersions: 模型加速版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccEngineVersions: list of ModelAccEngineVersion
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelAccEngineVersions = None
        self._RequestId = None

    @property
    def ModelAccEngineVersions(self):
        return self._ModelAccEngineVersions

    @ModelAccEngineVersions.setter
    def ModelAccEngineVersions(self, ModelAccEngineVersions):
        self._ModelAccEngineVersions = ModelAccEngineVersions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ModelAccEngineVersions") is not None:
            self._ModelAccEngineVersions = []
            for item in params.get("ModelAccEngineVersions"):
                obj = ModelAccEngineVersion()
                obj._deserialize(item)
                self._ModelAccEngineVersions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModelAccelerateTaskRequest(AbstractModel):
    """DescribeModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        """
        self._ModelAccTaskId = None

    @property
    def ModelAccTaskId(self):
        return self._ModelAccTaskId

    @ModelAccTaskId.setter
    def ModelAccTaskId(self, ModelAccTaskId):
        self._ModelAccTaskId = ModelAccTaskId


    def _deserialize(self, params):
        self._ModelAccTaskId = params.get("ModelAccTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelAccelerateTaskResponse(AbstractModel):
    """DescribeModelAccelerateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccelerateTask: 模型加速任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccelerateTask: :class:`tencentcloud.tione.v20211111.models.ModelAccelerateTask`
        :param _ModelAccRuntimeInSecond: 模型加速时长，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccRuntimeInSecond: int
        :param _ModelAccStartTime: 模型加速任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccStartTime: str
        :param _ModelAccEndTime: 模型加速任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccEndTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelAccelerateTask = None
        self._ModelAccRuntimeInSecond = None
        self._ModelAccStartTime = None
        self._ModelAccEndTime = None
        self._RequestId = None

    @property
    def ModelAccelerateTask(self):
        return self._ModelAccelerateTask

    @ModelAccelerateTask.setter
    def ModelAccelerateTask(self, ModelAccelerateTask):
        self._ModelAccelerateTask = ModelAccelerateTask

    @property
    def ModelAccRuntimeInSecond(self):
        return self._ModelAccRuntimeInSecond

    @ModelAccRuntimeInSecond.setter
    def ModelAccRuntimeInSecond(self, ModelAccRuntimeInSecond):
        self._ModelAccRuntimeInSecond = ModelAccRuntimeInSecond

    @property
    def ModelAccStartTime(self):
        return self._ModelAccStartTime

    @ModelAccStartTime.setter
    def ModelAccStartTime(self, ModelAccStartTime):
        self._ModelAccStartTime = ModelAccStartTime

    @property
    def ModelAccEndTime(self):
        return self._ModelAccEndTime

    @ModelAccEndTime.setter
    def ModelAccEndTime(self, ModelAccEndTime):
        self._ModelAccEndTime = ModelAccEndTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ModelAccelerateTask") is not None:
            self._ModelAccelerateTask = ModelAccelerateTask()
            self._ModelAccelerateTask._deserialize(params.get("ModelAccelerateTask"))
        self._ModelAccRuntimeInSecond = params.get("ModelAccRuntimeInSecond")
        self._ModelAccStartTime = params.get("ModelAccStartTime")
        self._ModelAccEndTime = params.get("ModelAccEndTime")
        self._RequestId = params.get("RequestId")


class DescribeModelAccelerateTasksRequest(AbstractModel):
    """DescribeModelAccelerateTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤器
ModelAccTaskName 任务名称
ModelSource 模型来源
        :type Filters: list of Filter
        :param _OrderField: 排序字段，默认CreateTime
        :type OrderField: str
        :param _Order: 排序方式：ASC/DESC，默认DESC
        :type Order: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回记录条数，默认10
        :type Limit: int
        :param _TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        """
        self._Filters = None
        self._OrderField = None
        self._Order = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

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
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelAccelerateTasksResponse(AbstractModel):
    """DescribeModelAccelerateTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccelerateTasks: 模型加速任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccelerateTasks: list of ModelAccelerateTask
        :param _TotalCount: 任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelAccelerateTasks = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ModelAccelerateTasks(self):
        return self._ModelAccelerateTasks

    @ModelAccelerateTasks.setter
    def ModelAccelerateTasks(self, ModelAccelerateTasks):
        self._ModelAccelerateTasks = ModelAccelerateTasks

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
        if params.get("ModelAccelerateTasks") is not None:
            self._ModelAccelerateTasks = []
            for item in params.get("ModelAccelerateTasks"):
                obj = ModelAccelerateTask()
                obj._deserialize(item)
                self._ModelAccelerateTasks.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeModelServiceCallInfoRequest(AbstractModel):
    """DescribeModelServiceCallInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        :param _ServiceCategory: 服务分类
        :type ServiceCategory: str
        """
        self._ServiceGroupId = None
        self._ServiceCategory = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def ServiceCategory(self):
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
        self._ServiceCategory = ServiceCategory


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._ServiceCategory = params.get("ServiceCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceCallInfoResponse(AbstractModel):
    """DescribeModelServiceCallInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceCallInfo: 服务调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCallInfo: :class:`tencentcloud.tione.v20211111.models.ServiceCallInfo`
        :param _InferGatewayCallInfo: 升级网关调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InferGatewayCallInfo: :class:`tencentcloud.tione.v20211111.models.InferGatewayCallInfo`
        :param _DefaultNginxGatewayCallInfo: 默认nginx网关的调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultNginxGatewayCallInfo: :class:`tencentcloud.tione.v20211111.models.DefaultNginxGatewayCallInfo`
        :param _TJCallInfo: 太极服务的调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TJCallInfo: :class:`tencentcloud.tione.v20211111.models.TJCallInfo`
        :param _IntranetCallInfo: 内网调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetCallInfo: :class:`tencentcloud.tione.v20211111.models.IntranetCallInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceCallInfo = None
        self._InferGatewayCallInfo = None
        self._DefaultNginxGatewayCallInfo = None
        self._TJCallInfo = None
        self._IntranetCallInfo = None
        self._RequestId = None

    @property
    def ServiceCallInfo(self):
        return self._ServiceCallInfo

    @ServiceCallInfo.setter
    def ServiceCallInfo(self, ServiceCallInfo):
        self._ServiceCallInfo = ServiceCallInfo

    @property
    def InferGatewayCallInfo(self):
        return self._InferGatewayCallInfo

    @InferGatewayCallInfo.setter
    def InferGatewayCallInfo(self, InferGatewayCallInfo):
        self._InferGatewayCallInfo = InferGatewayCallInfo

    @property
    def DefaultNginxGatewayCallInfo(self):
        return self._DefaultNginxGatewayCallInfo

    @DefaultNginxGatewayCallInfo.setter
    def DefaultNginxGatewayCallInfo(self, DefaultNginxGatewayCallInfo):
        self._DefaultNginxGatewayCallInfo = DefaultNginxGatewayCallInfo

    @property
    def TJCallInfo(self):
        return self._TJCallInfo

    @TJCallInfo.setter
    def TJCallInfo(self, TJCallInfo):
        self._TJCallInfo = TJCallInfo

    @property
    def IntranetCallInfo(self):
        return self._IntranetCallInfo

    @IntranetCallInfo.setter
    def IntranetCallInfo(self, IntranetCallInfo):
        self._IntranetCallInfo = IntranetCallInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceCallInfo") is not None:
            self._ServiceCallInfo = ServiceCallInfo()
            self._ServiceCallInfo._deserialize(params.get("ServiceCallInfo"))
        if params.get("InferGatewayCallInfo") is not None:
            self._InferGatewayCallInfo = InferGatewayCallInfo()
            self._InferGatewayCallInfo._deserialize(params.get("InferGatewayCallInfo"))
        if params.get("DefaultNginxGatewayCallInfo") is not None:
            self._DefaultNginxGatewayCallInfo = DefaultNginxGatewayCallInfo()
            self._DefaultNginxGatewayCallInfo._deserialize(params.get("DefaultNginxGatewayCallInfo"))
        if params.get("TJCallInfo") is not None:
            self._TJCallInfo = TJCallInfo()
            self._TJCallInfo._deserialize(params.get("TJCallInfo"))
        if params.get("IntranetCallInfo") is not None:
            self._IntranetCallInfo = IntranetCallInfo()
            self._IntranetCallInfo._deserialize(params.get("IntranetCallInfo"))
        self._RequestId = params.get("RequestId")


class DescribeModelServiceGroupRequest(AbstractModel):
    """DescribeModelServiceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 服务组ID
        :type ServiceGroupId: str
        :param _ServiceCategory: 服务分类
        :type ServiceCategory: str
        """
        self._ServiceGroupId = None
        self._ServiceCategory = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def ServiceCategory(self):
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
        self._ServiceCategory = ServiceCategory


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._ServiceCategory = params.get("ServiceCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceGroupResponse(AbstractModel):
    """DescribeModelServiceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceGroup: 服务组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroup: :class:`tencentcloud.tione.v20211111.models.ServiceGroup`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceGroup = None
        self._RequestId = None

    @property
    def ServiceGroup(self):
        return self._ServiceGroup

    @ServiceGroup.setter
    def ServiceGroup(self, ServiceGroup):
        self._ServiceGroup = ServiceGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceGroup") is not None:
            self._ServiceGroup = ServiceGroup()
            self._ServiceGroup._deserialize(params.get("ServiceGroup"))
        self._RequestId = params.get("RequestId")


class DescribeModelServiceGroupsRequest(AbstractModel):
    """DescribeModelServiceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        :param _Filters: 分页参数，支持的分页过滤Name包括：
["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId","Status","CreatedBy","ModelVersionId"]
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤参数
        :type TagFilters: list of TagFilter
        :param _ServiceCategory: 服务分类
        :type ServiceCategory: str
        """
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._Filters = None
        self._TagFilters = None
        self._ServiceCategory = None

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def ServiceCategory(self):
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
        self._ServiceCategory = ServiceCategory


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._ServiceCategory = params.get("ServiceCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceGroupsResponse(AbstractModel):
    """DescribeModelServiceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 推理服务组数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ServiceGroups: 服务组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroups: list of ServiceGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ServiceGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceGroups(self):
        return self._ServiceGroups

    @ServiceGroups.setter
    def ServiceGroups(self, ServiceGroups):
        self._ServiceGroups = ServiceGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ServiceGroups") is not None:
            self._ServiceGroups = []
            for item in params.get("ServiceGroups"):
                obj = ServiceGroup()
                obj._deserialize(item)
                self._ServiceGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModelServiceHistoryRequest(AbstractModel):
    """DescribeModelServiceHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务Id
        :type ServiceId: str
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceHistoryResponse(AbstractModel):
    """DescribeModelServiceHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 历史版本总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ServiceHistory: 服务版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceHistory: list of ServiceHistory
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ServiceHistory = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceHistory(self):
        return self._ServiceHistory

    @ServiceHistory.setter
    def ServiceHistory(self, ServiceHistory):
        self._ServiceHistory = ServiceHistory

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ServiceHistory") is not None:
            self._ServiceHistory = []
            for item in params.get("ServiceHistory"):
                obj = ServiceHistory()
                obj._deserialize(item)
                self._ServiceHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModelServiceHotUpdatedRequest(AbstractModel):
    """DescribeModelServiceHotUpdated请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageInfo: 镜像信息，配置服务运行所需的镜像地址等信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _ModelInfo: 模型信息，需要挂载模型时填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _VolumeMount: 挂载信息
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        """
        self._ImageInfo = None
        self._ModelInfo = None
        self._VolumeMount = None

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def ModelInfo(self):
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def VolumeMount(self):
        return self._VolumeMount

    @VolumeMount.setter
    def VolumeMount(self, VolumeMount):
        self._VolumeMount = VolumeMount


    def _deserialize(self, params):
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("VolumeMount") is not None:
            self._VolumeMount = VolumeMount()
            self._VolumeMount._deserialize(params.get("VolumeMount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceHotUpdatedResponse(AbstractModel):
    """DescribeModelServiceHotUpdated返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelTurboFlag: 模型加速标志位.Allowed 允许模型加速. Forbidden 禁止模型加速
        :type ModelTurboFlag: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelTurboFlag = None
        self._RequestId = None

    @property
    def ModelTurboFlag(self):
        return self._ModelTurboFlag

    @ModelTurboFlag.setter
    def ModelTurboFlag(self, ModelTurboFlag):
        self._ModelTurboFlag = ModelTurboFlag

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelTurboFlag = params.get("ModelTurboFlag")
        self._RequestId = params.get("RequestId")


class DescribeModelServiceRequest(AbstractModel):
    """DescribeModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务id
        :type ServiceId: str
        :param _ServiceCategory: 服务分类
        :type ServiceCategory: str
        """
        self._ServiceId = None
        self._ServiceCategory = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceCategory(self):
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
        self._ServiceCategory = ServiceCategory


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceCategory = params.get("ServiceCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceResponse(AbstractModel):
    """DescribeModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 服务信息
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Service = None
        self._RequestId = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        self._RequestId = params.get("RequestId")


class DescribeModelServicesRequest(AbstractModel):
    """DescribeModelServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为20
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        :param _Filters: 分页参数，支持的分页过滤Name包括：
["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId","Status","CreatedBy","ModelId"]
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤参数
        :type TagFilters: list of TagFilter
        """
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._Filters = None
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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServicesResponse(AbstractModel):
    """DescribeModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Services: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of Service
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Services = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Services") is not None:
            self._Services = []
            for item in params.get("Services"):
                obj = Service()
                obj._deserialize(item)
                self._Services.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNotebookImageKernelsRequest(AbstractModel):
    """DescribeNotebookImageKernels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookId: notebook id
        :type NotebookId: str
        """
        self._NotebookId = None

    @property
    def NotebookId(self):
        return self._NotebookId

    @NotebookId.setter
    def NotebookId(self, NotebookId):
        self._NotebookId = NotebookId


    def _deserialize(self, params):
        self._NotebookId = params.get("NotebookId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookImageKernelsResponse(AbstractModel):
    """DescribeNotebookImageKernels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Kernels: 镜像kernel数组
        :type Kernels: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Kernels = None
        self._RequestId = None

    @property
    def Kernels(self):
        return self._Kernels

    @Kernels.setter
    def Kernels(self, Kernels):
        self._Kernels = Kernels

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Kernels = params.get("Kernels")
        self._RequestId = params.get("RequestId")


class DescribeNotebookImageRecordsRequest(AbstractModel):
    """DescribeNotebookImageRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookId: notebook id
        :type NotebookId: str
        :param _Offset: 位移值
        :type Offset: int
        :param _Limit: 日志限制
        :type Limit: int
        :param _Filters: 状态筛选
        :type Filters: list of Filter
        """
        self._NotebookId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def NotebookId(self):
        return self._NotebookId

    @NotebookId.setter
    def NotebookId(self, NotebookId):
        self._NotebookId = NotebookId

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._NotebookId = params.get("NotebookId")
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
        


class DescribeNotebookImageRecordsResponse(AbstractModel):
    """DescribeNotebookImageRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _NotebookImageRecords: 镜像保存记录
        :type NotebookImageRecords: list of NotebookImageRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NotebookImageRecords = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NotebookImageRecords(self):
        return self._NotebookImageRecords

    @NotebookImageRecords.setter
    def NotebookImageRecords(self, NotebookImageRecords):
        self._NotebookImageRecords = NotebookImageRecords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NotebookImageRecords") is not None:
            self._NotebookImageRecords = []
            for item in params.get("NotebookImageRecords"):
                obj = NotebookImageRecord()
                obj._deserialize(item)
                self._NotebookImageRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNotebookRequest(AbstractModel):
    """DescribeNotebook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: notebook id
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebookResponse(AbstractModel):
    """DescribeNotebook返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookDetail: 详情
        :type NotebookDetail: :class:`tencentcloud.tione.v20211111.models.NotebookDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookDetail = None
        self._RequestId = None

    @property
    def NotebookDetail(self):
        return self._NotebookDetail

    @NotebookDetail.setter
    def NotebookDetail(self, NotebookDetail):
        self._NotebookDetail = NotebookDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NotebookDetail") is not None:
            self._NotebookDetail = NotebookDetail()
            self._NotebookDetail._deserialize(params.get("NotebookDetail"))
        self._RequestId = params.get("RequestId")


class DescribeNotebooksRequest(AbstractModel):
    """DescribeNotebooks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 每页返回的实例数，默认为10
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列。默认为DESC
        :type Order: str
        :param _OrderField: 根据哪个字段排序，如：CreateTime、UpdateTime，默认为UpdateTime
        :type OrderField: str
        :param _Filters: 过滤器，eg：[{ "Name": "Id", "Values": ["nb-123456789"] }]

取值范围
Name（名称）：notebook1
Id（notebook ID）：nb-123456789
Status（状态）：Starting / Running / Stopped / Stopping / Failed / SubmitFailed
ChargeType（计费类型）：PREPAID（预付费）/ POSTPAID_BY_HOUR（后付费）
ChargeStatus（计费状态）：NOT_BILLING（未开始计费）/ BILLING（计费中）/ BILLING_STORAGE（存储计费中）/ARREARS_STOP（欠费停止）
DefaultCodeRepoId（默认代码仓库ID）：cr-123456789
AdditionalCodeRepoId（关联代码仓库ID）：cr-123456789
LifecycleScriptId（生命周期ID）：ls-12312312311312
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤器，eg：[{ "TagKey": "TagKeyA", "TagValue": ["TagValueA"] }]
        :type TagFilters: list of TagFilter
        """
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._Filters = None
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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNotebooksResponse(AbstractModel):
    """DescribeNotebooks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NotebookSet: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type NotebookSet: list of NotebookSetItem
        :param _TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NotebookSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NotebookSet(self):
        return self._NotebookSet

    @NotebookSet.setter
    def NotebookSet(self, NotebookSet):
        self._NotebookSet = NotebookSet

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
        if params.get("NotebookSet") is not None:
            self._NotebookSet = []
            for item in params.get("NotebookSet"):
                obj = NotebookSetItem()
                obj._deserialize(item)
                self._NotebookSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTrainingFrameworksRequest(AbstractModel):
    """DescribeTrainingFrameworks请求参数结构体

    """


class DescribeTrainingFrameworksResponse(AbstractModel):
    """DescribeTrainingFrameworks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FrameworkInfos: 框架信息列表
        :type FrameworkInfos: list of FrameworkInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FrameworkInfos = None
        self._RequestId = None

    @property
    def FrameworkInfos(self):
        return self._FrameworkInfos

    @FrameworkInfos.setter
    def FrameworkInfos(self, FrameworkInfos):
        self._FrameworkInfos = FrameworkInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FrameworkInfos") is not None:
            self._FrameworkInfos = []
            for item in params.get("FrameworkInfos"):
                obj = FrameworkInfo()
                obj._deserialize(item)
                self._FrameworkInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrainingMetricsRequest(AbstractModel):
    """DescribeTrainingMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingMetricsResponse(AbstractModel):
    """DescribeTrainingMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _Data: 训练指标数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CustomTrainingData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Data = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CustomTrainingData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrainingModelVersionRequest(AbstractModel):
    """DescribeTrainingModelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingModelVersionId: 模型版本ID
        :type TrainingModelVersionId: str
        """
        self._TrainingModelVersionId = None

    @property
    def TrainingModelVersionId(self):
        return self._TrainingModelVersionId

    @TrainingModelVersionId.setter
    def TrainingModelVersionId(self, TrainingModelVersionId):
        self._TrainingModelVersionId = TrainingModelVersionId


    def _deserialize(self, params):
        self._TrainingModelVersionId = params.get("TrainingModelVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingModelVersionResponse(AbstractModel):
    """DescribeTrainingModelVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingModelVersion: 模型版本
        :type TrainingModelVersion: :class:`tencentcloud.tione.v20211111.models.TrainingModelVersionDTO`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrainingModelVersion = None
        self._RequestId = None

    @property
    def TrainingModelVersion(self):
        return self._TrainingModelVersion

    @TrainingModelVersion.setter
    def TrainingModelVersion(self, TrainingModelVersion):
        self._TrainingModelVersion = TrainingModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TrainingModelVersion") is not None:
            self._TrainingModelVersion = TrainingModelVersionDTO()
            self._TrainingModelVersion._deserialize(params.get("TrainingModelVersion"))
        self._RequestId = params.get("RequestId")


class DescribeTrainingModelVersionsRequest(AbstractModel):
    """DescribeTrainingModelVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingModelId: 模型ID
        :type TrainingModelId: str
        :param _Filters: 过滤条件
Filter.Name: 枚举值:
    TrainingModelVersionId (模型版本ID)
    ModelVersionType (模型版本类型) 其值支持: NORMAL(通用) ACCELERATE (加速)
    ModelFormat（模型格式）其值Filter.Values支持：
TORCH_SCRIPT/PYTORCH/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/PMML
    AlgorithmFramework (算法框架) 其值Filter.Values支持：TENSORFLOW/PYTORCH/DETECTRON2
Filter.Values: 当长度为1时，支持模糊查询; 不为1时，精确查询
每次请求的Filters的上限为10，Filter.Values的上限为100
        :type Filters: list of Filter
        """
        self._TrainingModelId = None
        self._Filters = None

    @property
    def TrainingModelId(self):
        return self._TrainingModelId

    @TrainingModelId.setter
    def TrainingModelId(self, TrainingModelId):
        self._TrainingModelId = TrainingModelId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TrainingModelId = params.get("TrainingModelId")
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
        


class DescribeTrainingModelVersionsResponse(AbstractModel):
    """DescribeTrainingModelVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingModelVersions: 模型版本列表
        :type TrainingModelVersions: list of TrainingModelVersionDTO
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrainingModelVersions = None
        self._RequestId = None

    @property
    def TrainingModelVersions(self):
        return self._TrainingModelVersions

    @TrainingModelVersions.setter
    def TrainingModelVersions(self, TrainingModelVersions):
        self._TrainingModelVersions = TrainingModelVersions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TrainingModelVersions") is not None:
            self._TrainingModelVersions = []
            for item in params.get("TrainingModelVersions"):
                obj = TrainingModelVersionDTO()
                obj._deserialize(item)
                self._TrainingModelVersions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrainingModelsRequest(AbstractModel):
    """DescribeTrainingModels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤器
Filter.Name: 枚举值:
keyword (模型名称)
TrainingModelId (模型ID)
ModelVersionType (模型版本类型) 其值Filter.Values支持: NORMAL(通用) ACCELERATE (加速)
TrainingModelSource (模型来源) 其值Filter.Values支持： JOB/COS
ModelFormat（模型格式）其值Filter.Values支持：
PYTORCH/TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/PMML/MMDETECTION/ONNX/HUGGING_FACE
Filter.Values: 当长度为1时，支持模糊查询; 不为1时，精确查询
每次请求的Filters的上限为10，Filter.Values的上限为100
Filter.Fuzzy取值：true/false，是否支持模糊匹配
        :type Filters: list of Filter
        :param _OrderField: 排序字段，默认CreateTime
        :type OrderField: str
        :param _Order: 排序方式，ASC/DESC，默认DESC
        :type Order: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回结果数量
        :type Limit: int
        :param _TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        :param _WithModelVersions: 是否同时返回模型版本列表
        :type WithModelVersions: bool
        """
        self._Filters = None
        self._OrderField = None
        self._Order = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None
        self._WithModelVersions = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

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
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def WithModelVersions(self):
        return self._WithModelVersions

    @WithModelVersions.setter
    def WithModelVersions(self, WithModelVersions):
        self._WithModelVersions = WithModelVersions


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._WithModelVersions = params.get("WithModelVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingModelsResponse(AbstractModel):
    """DescribeTrainingModels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingModels: 模型列表
        :type TrainingModels: list of TrainingModelDTO
        :param _TotalCount: 模型总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrainingModels = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TrainingModels(self):
        return self._TrainingModels

    @TrainingModels.setter
    def TrainingModels(self, TrainingModels):
        self._TrainingModels = TrainingModels

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
        if params.get("TrainingModels") is not None:
            self._TrainingModels = []
            for item in params.get("TrainingModels"):
                obj = TrainingModelDTO()
                obj._deserialize(item)
                self._TrainingModels.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTrainingTaskPodsRequest(AbstractModel):
    """DescribeTrainingTaskPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingTaskPodsResponse(AbstractModel):
    """DescribeTrainingTaskPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PodNames: pod名称列表
        :type PodNames: list of str
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _PodInfoList: pod详细信息
        :type PodInfoList: list of PodInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PodNames = None
        self._TotalCount = None
        self._PodInfoList = None
        self._RequestId = None

    @property
    def PodNames(self):
        return self._PodNames

    @PodNames.setter
    def PodNames(self, PodNames):
        self._PodNames = PodNames

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PodInfoList(self):
        return self._PodInfoList

    @PodInfoList.setter
    def PodInfoList(self, PodInfoList):
        self._PodInfoList = PodInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PodNames = params.get("PodNames")
        self._TotalCount = params.get("TotalCount")
        if params.get("PodInfoList") is not None:
            self._PodInfoList = []
            for item in params.get("PodInfoList"):
                obj = PodInfo()
                obj._deserialize(item)
                self._PodInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrainingTaskRequest(AbstractModel):
    """DescribeTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingTaskResponse(AbstractModel):
    """DescribeTrainingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingTaskDetail: 训练任务详情
        :type TrainingTaskDetail: :class:`tencentcloud.tione.v20211111.models.TrainingTaskDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrainingTaskDetail = None
        self._RequestId = None

    @property
    def TrainingTaskDetail(self):
        return self._TrainingTaskDetail

    @TrainingTaskDetail.setter
    def TrainingTaskDetail(self, TrainingTaskDetail):
        self._TrainingTaskDetail = TrainingTaskDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TrainingTaskDetail") is not None:
            self._TrainingTaskDetail = TrainingTaskDetail()
            self._TrainingTaskDetail._deserialize(params.get("TrainingTaskDetail"))
        self._RequestId = params.get("RequestId")


class DescribeTrainingTasksRequest(AbstractModel):
    """DescribeTrainingTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤器，eg：[{ "Name": "Id", "Values": ["train-23091792777383936"] }]

取值范围：
Name（名称）：task1
Id（task ID）：train-23091792777383936
Status（状态）：STARTING / RUNNING / STOPPING / STOPPED / FAILED / SUCCEED / SUBMIT_FAILED
ChargeType（计费类型）：PREPAID（预付费）/ POSTPAID_BY_HOUR（后付费）
CHARGE_STATUS（计费状态）：NOT_BILLING（未开始计费）/ BILLING（计费中）/ ARREARS_STOP（欠费停止）
        :type Filters: list of Filter
        :param _TagFilters: 标签过滤器，eg：[{ "TagKey": "TagKeyA", "TagValue": ["TagValueA"] }]
        :type TagFilters: list of TagFilter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为10，最大为50
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC（升序排列）/ DESC（降序排列），默认为DESC
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        """
        self._Filters = None
        self._TagFilters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

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
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingTasksResponse(AbstractModel):
    """DescribeTrainingTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TrainingTaskSet: 训练任务集
        :type TrainingTaskSet: list of TrainingTaskSetItem
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TrainingTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TrainingTaskSet(self):
        return self._TrainingTaskSet

    @TrainingTaskSet.setter
    def TrainingTaskSet(self, TrainingTaskSet):
        self._TrainingTaskSet = TrainingTaskSet

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
        if params.get("TrainingTaskSet") is not None:
            self._TrainingTaskSet = []
            for item in params.get("TrainingTaskSet"):
                obj = TrainingTaskSetItem()
                obj._deserialize(item)
                self._TrainingTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetectionLabelInfo(AbstractModel):
    """图像检测参数信息

    """

    def __init__(self):
        r"""
        :param _Points: 点坐标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of PointInfo
        :param _Labels: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param _FrameType: 类别
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameType: str
        """
        self._Points = None
        self._Labels = None
        self._FrameType = None

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def FrameType(self):
        return self._FrameType

    @FrameType.setter
    def FrameType(self, FrameType):
        self._FrameType = FrameType


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = PointInfo()
                obj._deserialize(item)
                self._Points.append(obj)
        self._Labels = params.get("Labels")
        self._FrameType = params.get("FrameType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EngineVersion(AbstractModel):
    """引擎版本

    """

    def __init__(self):
        r"""
        :param _Version: 引擎版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Image: 运行镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param _IsSupportIntEightQuantization: 是否支持int8量化
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportIntEightQuantization: bool
        :param _FrameworkVersion: 框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        """
        self._Version = None
        self._Image = None
        self._IsSupportIntEightQuantization = None
        self._FrameworkVersion = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def IsSupportIntEightQuantization(self):
        return self._IsSupportIntEightQuantization

    @IsSupportIntEightQuantization.setter
    def IsSupportIntEightQuantization(self, IsSupportIntEightQuantization):
        self._IsSupportIntEightQuantization = IsSupportIntEightQuantization

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Image = params.get("Image")
        self._IsSupportIntEightQuantization = params.get("IsSupportIntEightQuantization")
        self._FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param _Name: 环境变量key
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 环境变量value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名称
        :type Name: str
        :param _Values: 过滤字段取值
        :type Values: list of str
        :param _Negative: 是否开启反向查询
        :type Negative: bool
        :param _Fuzzy: 是否开启模糊匹配
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Negative = None
        self._Fuzzy = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Negative(self):
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative

    @property
    def Fuzzy(self):
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Negative = params.get("Negative")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterLabelInfo(AbstractModel):
    """图片列表查询结果详情

    """

    def __init__(self):
        r"""
        :param _DatasetId: 数据集id
        :type DatasetId: str
        :param _FileId: 文件ID
        :type FileId: str
        :param _FileName: 文件路径
        :type FileName: str
        :param _ClassificationLabels: 分类标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationLabels: list of str
        :param _DetectionLabels: 检测标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionLabels: list of DetectionLabelInfo
        :param _SegmentationLabels: 分割标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentationLabels: list of SegmentationInfo
        :param _RGBPath: RGB 图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :type RGBPath: str
        :param _LabelTemplateType: 标签模板类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelTemplateType: str
        :param _DownloadUrl: 下载url链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _DownloadThumbnailUrl: 缩略图下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadThumbnailUrl: str
        :param _DownloadRGBUrl: 分割结果图片下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadRGBUrl: str
        :param _OcrScene: OCR场景
IDENTITY：识别
STRUCTURE：智能结构化
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrScene: str
        :param _OcrLabels: OCR场景标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrLabels: list of OcrLabelInfo
        :param _OcrLabelInfo: OCR场景标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrLabelInfo: str
        :param _TextClassificationLabelList: 文本分类场景标签结果，内容是json结构
注意：此字段可能返回 null，表示取不到有效值。
        :type TextClassificationLabelList: str
        :param _RowText: 文本内容，返回50字符
注意：此字段可能返回 null，表示取不到有效值。
        :type RowText: str
        :param _ContentOmit: 文本内容是否完全返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentOmit: bool
        """
        self._DatasetId = None
        self._FileId = None
        self._FileName = None
        self._ClassificationLabels = None
        self._DetectionLabels = None
        self._SegmentationLabels = None
        self._RGBPath = None
        self._LabelTemplateType = None
        self._DownloadUrl = None
        self._DownloadThumbnailUrl = None
        self._DownloadRGBUrl = None
        self._OcrScene = None
        self._OcrLabels = None
        self._OcrLabelInfo = None
        self._TextClassificationLabelList = None
        self._RowText = None
        self._ContentOmit = None

    @property
    def DatasetId(self):
        return self._DatasetId

    @DatasetId.setter
    def DatasetId(self, DatasetId):
        self._DatasetId = DatasetId

    @property
    def FileId(self):
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ClassificationLabels(self):
        return self._ClassificationLabels

    @ClassificationLabels.setter
    def ClassificationLabels(self, ClassificationLabels):
        self._ClassificationLabels = ClassificationLabels

    @property
    def DetectionLabels(self):
        return self._DetectionLabels

    @DetectionLabels.setter
    def DetectionLabels(self, DetectionLabels):
        self._DetectionLabels = DetectionLabels

    @property
    def SegmentationLabels(self):
        return self._SegmentationLabels

    @SegmentationLabels.setter
    def SegmentationLabels(self, SegmentationLabels):
        self._SegmentationLabels = SegmentationLabels

    @property
    def RGBPath(self):
        return self._RGBPath

    @RGBPath.setter
    def RGBPath(self, RGBPath):
        self._RGBPath = RGBPath

    @property
    def LabelTemplateType(self):
        return self._LabelTemplateType

    @LabelTemplateType.setter
    def LabelTemplateType(self, LabelTemplateType):
        self._LabelTemplateType = LabelTemplateType

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def DownloadThumbnailUrl(self):
        return self._DownloadThumbnailUrl

    @DownloadThumbnailUrl.setter
    def DownloadThumbnailUrl(self, DownloadThumbnailUrl):
        self._DownloadThumbnailUrl = DownloadThumbnailUrl

    @property
    def DownloadRGBUrl(self):
        return self._DownloadRGBUrl

    @DownloadRGBUrl.setter
    def DownloadRGBUrl(self, DownloadRGBUrl):
        self._DownloadRGBUrl = DownloadRGBUrl

    @property
    def OcrScene(self):
        return self._OcrScene

    @OcrScene.setter
    def OcrScene(self, OcrScene):
        self._OcrScene = OcrScene

    @property
    def OcrLabels(self):
        return self._OcrLabels

    @OcrLabels.setter
    def OcrLabels(self, OcrLabels):
        self._OcrLabels = OcrLabels

    @property
    def OcrLabelInfo(self):
        return self._OcrLabelInfo

    @OcrLabelInfo.setter
    def OcrLabelInfo(self, OcrLabelInfo):
        self._OcrLabelInfo = OcrLabelInfo

    @property
    def TextClassificationLabelList(self):
        return self._TextClassificationLabelList

    @TextClassificationLabelList.setter
    def TextClassificationLabelList(self, TextClassificationLabelList):
        self._TextClassificationLabelList = TextClassificationLabelList

    @property
    def RowText(self):
        return self._RowText

    @RowText.setter
    def RowText(self, RowText):
        self._RowText = RowText

    @property
    def ContentOmit(self):
        return self._ContentOmit

    @ContentOmit.setter
    def ContentOmit(self, ContentOmit):
        self._ContentOmit = ContentOmit


    def _deserialize(self, params):
        self._DatasetId = params.get("DatasetId")
        self._FileId = params.get("FileId")
        self._FileName = params.get("FileName")
        self._ClassificationLabels = params.get("ClassificationLabels")
        if params.get("DetectionLabels") is not None:
            self._DetectionLabels = []
            for item in params.get("DetectionLabels"):
                obj = DetectionLabelInfo()
                obj._deserialize(item)
                self._DetectionLabels.append(obj)
        if params.get("SegmentationLabels") is not None:
            self._SegmentationLabels = []
            for item in params.get("SegmentationLabels"):
                obj = SegmentationInfo()
                obj._deserialize(item)
                self._SegmentationLabels.append(obj)
        self._RGBPath = params.get("RGBPath")
        self._LabelTemplateType = params.get("LabelTemplateType")
        self._DownloadUrl = params.get("DownloadUrl")
        self._DownloadThumbnailUrl = params.get("DownloadThumbnailUrl")
        self._DownloadRGBUrl = params.get("DownloadRGBUrl")
        self._OcrScene = params.get("OcrScene")
        if params.get("OcrLabels") is not None:
            self._OcrLabels = []
            for item in params.get("OcrLabels"):
                obj = OcrLabelInfo()
                obj._deserialize(item)
                self._OcrLabels.append(obj)
        self._OcrLabelInfo = params.get("OcrLabelInfo")
        self._TextClassificationLabelList = params.get("TextClassificationLabelList")
        self._RowText = params.get("RowText")
        self._ContentOmit = params.get("ContentOmit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameworkInfo(AbstractModel):
    """框架信息列表

    """

    def __init__(self):
        r"""
        :param _Name: 框架名称
        :type Name: str
        :param _VersionInfos: 框架版本以及对应的训练模式
        :type VersionInfos: list of FrameworkVersion
        """
        self._Name = None
        self._VersionInfos = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VersionInfos(self):
        return self._VersionInfos

    @VersionInfos.setter
    def VersionInfos(self, VersionInfos):
        self._VersionInfos = VersionInfos


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("VersionInfos") is not None:
            self._VersionInfos = []
            for item in params.get("VersionInfos"):
                obj = FrameworkVersion()
                obj._deserialize(item)
                self._VersionInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameworkVersion(AbstractModel):
    """框架版本以及对应的训练模式

    """

    def __init__(self):
        r"""
        :param _Version: 框架版本
        :type Version: str
        :param _TrainingModes: 训练模式
        :type TrainingModes: list of str
        :param _Environment: 框架运行环境
        :type Environment: str
        """
        self._Version = None
        self._TrainingModes = None
        self._Environment = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def TrainingModes(self):
        return self._TrainingModes

    @TrainingModes.setter
    def TrainingModes(self, TrainingModes):
        self._TrainingModes = TrainingModes

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._TrainingModes = params.get("TrainingModes")
        self._Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFS(AbstractModel):
    """配置GooseFS参数

    """

    def __init__(self):
        r"""
        :param _Id: goosefs实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GpuDetail(AbstractModel):
    """gpu 详情

    """

    def __init__(self):
        r"""
        :param _Name: GPU 显卡类型；枚举值: V100 A100 T4
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: GPU 显卡数；单位为1/100卡，比如100代表1卡
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupResource(AbstractModel):
    """资源信息

    """

    def __init__(self):
        r"""
        :param _Cpu: CPU核数; 单位为1/1000核，比如100表示0.1核
        :type Cpu: int
        :param _Memory: 内存；单位为MB
        :type Memory: int
        :param _Gpu: 总卡数；GPUDetail 显卡数之和；单位为1/100卡，比如100代表1卡
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param _GpuDetailSet: Gpu详情
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuDetailSet: list of GpuDetail
        """
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._GpuDetailSet = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuDetailSet(self):
        return self._GpuDetailSet

    @GpuDetailSet.setter
    def GpuDetailSet(self, GpuDetailSet):
        self._GpuDetailSet = GpuDetailSet


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        if params.get("GpuDetailSet") is not None:
            self._GpuDetailSet = []
            for item in params.get("GpuDetailSet"):
                obj = GpuDetail()
                obj._deserialize(item)
                self._GpuDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HDFSConfig(AbstractModel):
    """HDFS的参数配置

    """

    def __init__(self):
        r"""
        :param _Id: 集群实例ID,实例ID形如: emr-xxxxxxxx
        :type Id: str
        :param _Path: 路径
        :type Path: str
        """
        self._Id = None
        self._Path = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalPodAutoscaler(AbstractModel):
    """hpa的描述

    """

    def __init__(self):
        r"""
        :param _MinReplicas: 最小实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinReplicas: int
        :param _MaxReplicas: 最大实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param _HpaMetrics: 扩缩容指标
注意：此字段可能返回 null，表示取不到有效值。
        :type HpaMetrics: list of Option
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._HpaMetrics = None

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def HpaMetrics(self):
        return self._HpaMetrics

    @HpaMetrics.setter
    def HpaMetrics(self, HpaMetrics):
        self._HpaMetrics = HpaMetrics


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("HpaMetrics") is not None:
            self._HpaMetrics = []
            for item in params.get("HpaMetrics"):
                obj = Option()
                obj._deserialize(item)
                self._HpaMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HyperParameter(AbstractModel):
    """模型专业参数

    """

    def __init__(self):
        r"""
        :param _MaxNNZ: 最大nnz数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNNZ: str
        :param _SlotNum: slot数
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotNum: str
        :param _CpuCachePercentage: gpu cache 使用率
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuCachePercentage: str
        :param _GpuCachePercentage: cpu cache 使用率
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuCachePercentage: str
        :param _EnableDistributed: 是否开启分布式模式(true/false)
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDistributed: str
        :param _MinBlockSizePt: TORCH_SCRIPT、MMDETECTION、DETECTRON2、HUGGINGFACE格式在进行优化时切分子图的最小算子数目，一般无需进行改动，默认为3
注意：此字段可能返回 null，表示取不到有效值。
        :type MinBlockSizePt: str
        :param _MinBlockSizeTf: FROZEN_GRAPH、SAVED_MODEL格式在进行优化时切分子图的最小算子数目，一般无需进行改动，默认为10
注意：此字段可能返回 null，表示取不到有效值。
        :type MinBlockSizeTf: str
        :param _PipelineArgs: Stable Diffusion 模型优化参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PipelineArgs: str
        :param _LoraScale: Stable Diffusion 模型优化参数，控制Lora模型的影响效果
注意：此字段可能返回 null，表示取不到有效值。
        :type LoraScale: str
        """
        self._MaxNNZ = None
        self._SlotNum = None
        self._CpuCachePercentage = None
        self._GpuCachePercentage = None
        self._EnableDistributed = None
        self._MinBlockSizePt = None
        self._MinBlockSizeTf = None
        self._PipelineArgs = None
        self._LoraScale = None

    @property
    def MaxNNZ(self):
        return self._MaxNNZ

    @MaxNNZ.setter
    def MaxNNZ(self, MaxNNZ):
        self._MaxNNZ = MaxNNZ

    @property
    def SlotNum(self):
        return self._SlotNum

    @SlotNum.setter
    def SlotNum(self, SlotNum):
        self._SlotNum = SlotNum

    @property
    def CpuCachePercentage(self):
        return self._CpuCachePercentage

    @CpuCachePercentage.setter
    def CpuCachePercentage(self, CpuCachePercentage):
        self._CpuCachePercentage = CpuCachePercentage

    @property
    def GpuCachePercentage(self):
        return self._GpuCachePercentage

    @GpuCachePercentage.setter
    def GpuCachePercentage(self, GpuCachePercentage):
        self._GpuCachePercentage = GpuCachePercentage

    @property
    def EnableDistributed(self):
        return self._EnableDistributed

    @EnableDistributed.setter
    def EnableDistributed(self, EnableDistributed):
        self._EnableDistributed = EnableDistributed

    @property
    def MinBlockSizePt(self):
        return self._MinBlockSizePt

    @MinBlockSizePt.setter
    def MinBlockSizePt(self, MinBlockSizePt):
        self._MinBlockSizePt = MinBlockSizePt

    @property
    def MinBlockSizeTf(self):
        return self._MinBlockSizeTf

    @MinBlockSizeTf.setter
    def MinBlockSizeTf(self, MinBlockSizeTf):
        self._MinBlockSizeTf = MinBlockSizeTf

    @property
    def PipelineArgs(self):
        return self._PipelineArgs

    @PipelineArgs.setter
    def PipelineArgs(self, PipelineArgs):
        self._PipelineArgs = PipelineArgs

    @property
    def LoraScale(self):
        return self._LoraScale

    @LoraScale.setter
    def LoraScale(self, LoraScale):
        self._LoraScale = LoraScale


    def _deserialize(self, params):
        self._MaxNNZ = params.get("MaxNNZ")
        self._SlotNum = params.get("SlotNum")
        self._CpuCachePercentage = params.get("CpuCachePercentage")
        self._GpuCachePercentage = params.get("GpuCachePercentage")
        self._EnableDistributed = params.get("EnableDistributed")
        self._MinBlockSizePt = params.get("MinBlockSizePt")
        self._MinBlockSizeTf = params.get("MinBlockSizeTf")
        self._PipelineArgs = params.get("PipelineArgs")
        self._LoraScale = params.get("LoraScale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """镜像描述信息

    """

    def __init__(self):
        r"""
        :param _ImageType: 镜像类型：TCR为腾讯云TCR镜像; CCR为腾讯云TCR个人版镜像，PreSet为平台预置镜像
        :type ImageType: str
        :param _ImageUrl: 镜像地址
        :type ImageUrl: str
        :param _RegistryRegion: TCR镜像对应的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryRegion: str
        :param _RegistryId: TCR镜像对应的实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        :param _AllowSaveAllContent: 是否允许导出全部内容
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowSaveAllContent: bool
        :param _ImageName: 镜像名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageName: str
        """
        self._ImageType = None
        self._ImageUrl = None
        self._RegistryRegion = None
        self._RegistryId = None
        self._AllowSaveAllContent = None
        self._ImageName = None

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RegistryRegion(self):
        return self._RegistryRegion

    @RegistryRegion.setter
    def RegistryRegion(self, RegistryRegion):
        self._RegistryRegion = RegistryRegion

    @property
    def RegistryId(self):
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def AllowSaveAllContent(self):
        return self._AllowSaveAllContent

    @AllowSaveAllContent.setter
    def AllowSaveAllContent(self, AllowSaveAllContent):
        self._AllowSaveAllContent = AllowSaveAllContent

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName


    def _deserialize(self, params):
        self._ImageType = params.get("ImageType")
        self._ImageUrl = params.get("ImageUrl")
        self._RegistryRegion = params.get("RegistryRegion")
        self._RegistryId = params.get("RegistryId")
        self._AllowSaveAllContent = params.get("AllowSaveAllContent")
        self._ImageName = params.get("ImageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferCodeInfo(AbstractModel):
    """推理代码的信息

    """

    def __init__(self):
        r"""
        :param _CosPathInfo: 推理代码所在的cos详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPathInfo: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        self._CosPathInfo = None

    @property
    def CosPathInfo(self):
        return self._CosPathInfo

    @CosPathInfo.setter
    def CosPathInfo(self, CosPathInfo):
        self._CosPathInfo = CosPathInfo


    def _deserialize(self, params):
        if params.get("CosPathInfo") is not None:
            self._CosPathInfo = CosPathInfo()
            self._CosPathInfo._deserialize(params.get("CosPathInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferGatewayCallInfo(AbstractModel):
    """服务的调用信息，服务组下唯一

    """

    def __init__(self):
        r"""
        :param _VpcHttpAddr: 内网http调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcHttpAddr: str
        :param _VpcHttpsAddr: 内网https调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcHttpsAddr: str
        :param _VpcGrpcTlsAddr: 内网grpc调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcGrpcTlsAddr: str
        :param _VpcId: 可访问的vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 后端ip对应的子网
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self._VpcHttpAddr = None
        self._VpcHttpsAddr = None
        self._VpcGrpcTlsAddr = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcHttpAddr(self):
        return self._VpcHttpAddr

    @VpcHttpAddr.setter
    def VpcHttpAddr(self, VpcHttpAddr):
        self._VpcHttpAddr = VpcHttpAddr

    @property
    def VpcHttpsAddr(self):
        return self._VpcHttpsAddr

    @VpcHttpsAddr.setter
    def VpcHttpsAddr(self, VpcHttpsAddr):
        self._VpcHttpsAddr = VpcHttpsAddr

    @property
    def VpcGrpcTlsAddr(self):
        return self._VpcGrpcTlsAddr

    @VpcGrpcTlsAddr.setter
    def VpcGrpcTlsAddr(self, VpcGrpcTlsAddr):
        self._VpcGrpcTlsAddr = VpcGrpcTlsAddr

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


    def _deserialize(self, params):
        self._VpcHttpAddr = params.get("VpcHttpAddr")
        self._VpcHttpsAddr = params.get("VpcHttpsAddr")
        self._VpcGrpcTlsAddr = params.get("VpcGrpcTlsAddr")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferTemplate(AbstractModel):
    """推理镜像详情

    """

    def __init__(self):
        r"""
        :param _InferTemplateId: 模板ID
        :type InferTemplateId: str
        :param _InferTemplateImage: 模板镜像
        :type InferTemplateImage: str
        """
        self._InferTemplateId = None
        self._InferTemplateImage = None

    @property
    def InferTemplateId(self):
        return self._InferTemplateId

    @InferTemplateId.setter
    def InferTemplateId(self, InferTemplateId):
        self._InferTemplateId = InferTemplateId

    @property
    def InferTemplateImage(self):
        return self._InferTemplateImage

    @InferTemplateImage.setter
    def InferTemplateImage(self, InferTemplateImage):
        self._InferTemplateImage = InferTemplateImage


    def _deserialize(self, params):
        self._InferTemplateId = params.get("InferTemplateId")
        self._InferTemplateImage = params.get("InferTemplateImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferTemplateGroup(AbstractModel):
    """推理镜像组

    """

    def __init__(self):
        r"""
        :param _Framework: 算法框架
注意：此字段可能返回 null，表示取不到有效值。
        :type Framework: str
        :param _FrameworkVersion: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        :param _Groups: 支持的训练框架集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of str
        :param _InferTemplates: 镜像模板参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InferTemplates: list of InferTemplate
        """
        self._Framework = None
        self._FrameworkVersion = None
        self._Groups = None
        self._InferTemplates = None

    @property
    def Framework(self):
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def InferTemplates(self):
        return self._InferTemplates

    @InferTemplates.setter
    def InferTemplates(self, InferTemplates):
        self._InferTemplates = InferTemplates


    def _deserialize(self, params):
        self._Framework = params.get("Framework")
        self._FrameworkVersion = params.get("FrameworkVersion")
        self._Groups = params.get("Groups")
        if params.get("InferTemplates") is not None:
            self._InferTemplates = []
            for item in params.get("InferTemplates"):
                obj = InferTemplate()
                obj._deserialize(item)
                self._InferTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressPrivateLinkInfo(AbstractModel):
    """私有连接通道信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 用户VpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 用户子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _InnerHttpAddr: 内网http调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpAddr: list of str
        :param _InnerHttpsAddr: 内网https调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpsAddr: list of str
        """
        self._VpcId = None
        self._SubnetId = None
        self._InnerHttpAddr = None
        self._InnerHttpsAddr = None

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
    def InnerHttpAddr(self):
        return self._InnerHttpAddr

    @InnerHttpAddr.setter
    def InnerHttpAddr(self, InnerHttpAddr):
        self._InnerHttpAddr = InnerHttpAddr

    @property
    def InnerHttpsAddr(self):
        return self._InnerHttpsAddr

    @InnerHttpsAddr.setter
    def InnerHttpsAddr(self, InnerHttpsAddr):
        self._InnerHttpsAddr = InnerHttpsAddr


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._InnerHttpAddr = params.get("InnerHttpAddr")
        self._InnerHttpsAddr = params.get("InnerHttpsAddr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """资源组节点信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源组节点id
        :type InstanceId: str
        :param _UsedResource: 节点已用资源
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedResource: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _TotalResource: 节点总资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalResource: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _InstanceStatus: 节点状态 
注意：此字段为枚举值
说明: 
DEPLOYING: 部署中
RUNNING: 运行中 
DEPLOY_FAILED: 部署失败
 RELEASING 释放中 
RELEASED：已释放 
EXCEPTION：异常
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        :param _SubUin: 创建人
        :type SubUin: str
        :param _CreateTime: 创建时间: 
注意：北京时间，比如: 2021-12-01 12:00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ExpireTime: 到期时间
注意：北京时间，比如：2021-12-11 12:00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _AutoRenewFlag: 自动续费标识
注意：此字段为枚举值
说明：
NOTIFY_AND_MANUAL_RENEW：手动续费(取消自动续费)且到期通知
NOTIFY_AND_AUTO_RENEW：自动续费且到期通知
DISABLE_NOTIFY_AND_MANUAL_RENEW：手动续费(取消自动续费)且到期不通知
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: str
        :param _SpecId: 计费项ID
        :type SpecId: str
        :param _SpecAlias: 计费项别名
        :type SpecAlias: str
        :param _SpecFeatures: 计费项特性列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecFeatures: list of str
        """
        self._InstanceId = None
        self._UsedResource = None
        self._TotalResource = None
        self._InstanceStatus = None
        self._SubUin = None
        self._CreateTime = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._SpecId = None
        self._SpecAlias = None
        self._SpecFeatures = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UsedResource(self):
        return self._UsedResource

    @UsedResource.setter
    def UsedResource(self, UsedResource):
        self._UsedResource = UsedResource

    @property
    def TotalResource(self):
        return self._TotalResource

    @TotalResource.setter
    def TotalResource(self, TotalResource):
        self._TotalResource = TotalResource

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SubUin(self):
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

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
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def SpecAlias(self):
        return self._SpecAlias

    @SpecAlias.setter
    def SpecAlias(self, SpecAlias):
        self._SpecAlias = SpecAlias

    @property
    def SpecFeatures(self):
        return self._SpecFeatures

    @SpecFeatures.setter
    def SpecFeatures(self, SpecFeatures):
        self._SpecFeatures = SpecFeatures


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("UsedResource") is not None:
            self._UsedResource = ResourceInfo()
            self._UsedResource._deserialize(params.get("UsedResource"))
        if params.get("TotalResource") is not None:
            self._TotalResource = ResourceInfo()
            self._TotalResource._deserialize(params.get("TotalResource"))
        self._InstanceStatus = params.get("InstanceStatus")
        self._SubUin = params.get("SubUin")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SpecId = params.get("SpecId")
        self._SpecAlias = params.get("SpecAlias")
        self._SpecFeatures = params.get("SpecFeatures")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntranetCallInfo(AbstractModel):
    """内网调用信息

    """

    def __init__(self):
        r"""
        :param _IngressPrivateLinkInfo: 私有连接通道信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IngressPrivateLinkInfo: :class:`tencentcloud.tione.v20211111.models.IngressPrivateLinkInfo`
        :param _ServiceEIPInfo: 共享弹性网卡信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceEIPInfo: list of ServiceEIPInfo
        """
        self._IngressPrivateLinkInfo = None
        self._ServiceEIPInfo = None

    @property
    def IngressPrivateLinkInfo(self):
        return self._IngressPrivateLinkInfo

    @IngressPrivateLinkInfo.setter
    def IngressPrivateLinkInfo(self, IngressPrivateLinkInfo):
        self._IngressPrivateLinkInfo = IngressPrivateLinkInfo

    @property
    def ServiceEIPInfo(self):
        return self._ServiceEIPInfo

    @ServiceEIPInfo.setter
    def ServiceEIPInfo(self, ServiceEIPInfo):
        self._ServiceEIPInfo = ServiceEIPInfo


    def _deserialize(self, params):
        if params.get("IngressPrivateLinkInfo") is not None:
            self._IngressPrivateLinkInfo = IngressPrivateLinkInfo()
            self._IngressPrivateLinkInfo._deserialize(params.get("IngressPrivateLinkInfo"))
        if params.get("ServiceEIPInfo") is not None:
            self._ServiceEIPInfo = []
            for item in params.get("ServiceEIPInfo"):
                obj = ServiceEIPInfo()
                obj._deserialize(item)
                self._ServiceEIPInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfig(AbstractModel):
    """日志配置

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志需要投递到cls的日志集
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param _TopicId: 日志需要投递到cls的主题
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        """
        self._LogsetId = None
        self._TopicId = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogIdentity(AbstractModel):
    """单条日志数据结构

    """

    def __init__(self):
        r"""
        :param _Id: 单条日志的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Message: 单条日志的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _PodName: 这条日志对应的Pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param _Timestamp: 日志的时间戳（RFC3339格式的时间字符串）
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        """
        self._Id = None
        self._Message = None
        self._PodName = None
        self._Timestamp = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Message = params.get("Message")
        self._PodName = params.get("PodName")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Message(AbstractModel):
    """对话输入内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色名。支持三个角色：system、user、assistant，其中system仅开头可出现一次，也可忽略。
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _Content: 对话输入内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """指标数据

    """

    def __init__(self):
        r"""
        :param _TaskId: 训练任务id
        :type TaskId: str
        :param _Timestamp: 时间戳.unix timestamp,单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param _Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _Epoch: 本次上报数据所处的训练周期数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Epoch: int
        :param _Step: 本次上报数据所处的训练迭代次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Step: int
        :param _TotalSteps: 训练停止所需的迭代总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSteps: int
        :param _Points: 数据点。数组元素为不同指标的数据。数组长度不超过10。
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of DataPoint
        """
        self._TaskId = None
        self._Timestamp = None
        self._Uin = None
        self._Epoch = None
        self._Step = None
        self._TotalSteps = None
        self._Points = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Epoch(self):
        return self._Epoch

    @Epoch.setter
    def Epoch(self, Epoch):
        self._Epoch = Epoch

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def TotalSteps(self):
        return self._TotalSteps

    @TotalSteps.setter
    def TotalSteps(self, TotalSteps):
        self._TotalSteps = TotalSteps

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Timestamp = params.get("Timestamp")
        self._Uin = params.get("Uin")
        self._Epoch = params.get("Epoch")
        self._Step = params.get("Step")
        self._TotalSteps = params.get("TotalSteps")
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = DataPoint()
                obj._deserialize(item)
                self._Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelAccEngineVersion(AbstractModel):
    """模型加速引擎版本

    """

    def __init__(self):
        r"""
        :param _ModelFormat: 模型格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelFormat: str
        :param _EngineVersions: 引擎版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersions: list of EngineVersion
        """
        self._ModelFormat = None
        self._EngineVersions = None

    @property
    def ModelFormat(self):
        return self._ModelFormat

    @ModelFormat.setter
    def ModelFormat(self, ModelFormat):
        self._ModelFormat = ModelFormat

    @property
    def EngineVersions(self):
        return self._EngineVersions

    @EngineVersions.setter
    def EngineVersions(self, EngineVersions):
        self._EngineVersions = EngineVersions


    def _deserialize(self, params):
        self._ModelFormat = params.get("ModelFormat")
        if params.get("EngineVersions") is not None:
            self._EngineVersions = []
            for item in params.get("EngineVersions"):
                obj = EngineVersion()
                obj._deserialize(item)
                self._EngineVersions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelAccelerateTask(AbstractModel):
    """模型加速任务

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskId: 模型加速任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskId: str
        :param _ModelAccTaskName: 模型加速任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskName: str
        :param _ModelId: 模型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param _ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param _ModelVersion: 模型版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelVersion: str
        :param _ModelSource: 模型来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelSource: str
        :param _OptimizationLevel: 优化级别
注意：此字段可能返回 null，表示取不到有效值。
        :type OptimizationLevel: str
        :param _TaskStatus: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param _ModelInputNum: input节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputNum: int
        :param _ModelInputInfos: input节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputInfos: list of ModelInputInfo
        :param _GPUType: GPU型号
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUType: str
        :param _ChargeType: 计费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _Speedup: 加速比
注意：此字段可能返回 null，表示取不到有效值。
        :type Speedup: str
        :param _ModelInputPath: 模型输入cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _ModelOutputPath: 模型输出cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _AlgorithmFramework: 算法框架
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgorithmFramework: str
        :param _WaitNumber: 排队个数
注意：此字段可能返回 null，表示取不到有效值。
        :type WaitNumber: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _TaskProgress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProgress: int
        :param _ModelFormat: 模型格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelFormat: str
        :param _TensorInfos: 模型Tensor信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TensorInfos: list of str
        :param _HyperParameter: 模型专业参数
注意：此字段可能返回 null，表示取不到有效值。
        :type HyperParameter: :class:`tencentcloud.tione.v20211111.models.HyperParameter`
        :param _AccEngineVersion: 加速引擎版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AccEngineVersion: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _IsSaved: 优化模型是否已保存到模型仓库
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSaved: bool
        :param _ModelSignature: SAVED_MODEL保存时配置的签名
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelSignature: str
        :param _QATModel: 是否是QAT模型
注意：此字段可能返回 null，表示取不到有效值。
        :type QATModel: bool
        :param _FrameworkVersion: 加速引擎对应的框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        """
        self._ModelAccTaskId = None
        self._ModelAccTaskName = None
        self._ModelId = None
        self._ModelName = None
        self._ModelVersion = None
        self._ModelSource = None
        self._OptimizationLevel = None
        self._TaskStatus = None
        self._ModelInputNum = None
        self._ModelInputInfos = None
        self._GPUType = None
        self._ChargeType = None
        self._Speedup = None
        self._ModelInputPath = None
        self._ModelOutputPath = None
        self._ErrorMsg = None
        self._AlgorithmFramework = None
        self._WaitNumber = None
        self._CreateTime = None
        self._TaskProgress = None
        self._ModelFormat = None
        self._TensorInfos = None
        self._HyperParameter = None
        self._AccEngineVersion = None
        self._Tags = None
        self._IsSaved = None
        self._ModelSignature = None
        self._QATModel = None
        self._FrameworkVersion = None

    @property
    def ModelAccTaskId(self):
        return self._ModelAccTaskId

    @ModelAccTaskId.setter
    def ModelAccTaskId(self, ModelAccTaskId):
        self._ModelAccTaskId = ModelAccTaskId

    @property
    def ModelAccTaskName(self):
        return self._ModelAccTaskName

    @ModelAccTaskName.setter
    def ModelAccTaskName(self, ModelAccTaskName):
        self._ModelAccTaskName = ModelAccTaskName

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelVersion(self):
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def ModelSource(self):
        return self._ModelSource

    @ModelSource.setter
    def ModelSource(self, ModelSource):
        self._ModelSource = ModelSource

    @property
    def OptimizationLevel(self):
        return self._OptimizationLevel

    @OptimizationLevel.setter
    def OptimizationLevel(self, OptimizationLevel):
        self._OptimizationLevel = OptimizationLevel

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ModelInputNum(self):
        return self._ModelInputNum

    @ModelInputNum.setter
    def ModelInputNum(self, ModelInputNum):
        self._ModelInputNum = ModelInputNum

    @property
    def ModelInputInfos(self):
        return self._ModelInputInfos

    @ModelInputInfos.setter
    def ModelInputInfos(self, ModelInputInfos):
        self._ModelInputInfos = ModelInputInfos

    @property
    def GPUType(self):
        return self._GPUType

    @GPUType.setter
    def GPUType(self, GPUType):
        self._GPUType = GPUType

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def Speedup(self):
        return self._Speedup

    @Speedup.setter
    def Speedup(self, Speedup):
        self._Speedup = Speedup

    @property
    def ModelInputPath(self):
        return self._ModelInputPath

    @ModelInputPath.setter
    def ModelInputPath(self, ModelInputPath):
        self._ModelInputPath = ModelInputPath

    @property
    def ModelOutputPath(self):
        return self._ModelOutputPath

    @ModelOutputPath.setter
    def ModelOutputPath(self, ModelOutputPath):
        self._ModelOutputPath = ModelOutputPath

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def AlgorithmFramework(self):
        return self._AlgorithmFramework

    @AlgorithmFramework.setter
    def AlgorithmFramework(self, AlgorithmFramework):
        self._AlgorithmFramework = AlgorithmFramework

    @property
    def WaitNumber(self):
        return self._WaitNumber

    @WaitNumber.setter
    def WaitNumber(self, WaitNumber):
        self._WaitNumber = WaitNumber

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TaskProgress(self):
        return self._TaskProgress

    @TaskProgress.setter
    def TaskProgress(self, TaskProgress):
        self._TaskProgress = TaskProgress

    @property
    def ModelFormat(self):
        return self._ModelFormat

    @ModelFormat.setter
    def ModelFormat(self, ModelFormat):
        self._ModelFormat = ModelFormat

    @property
    def TensorInfos(self):
        return self._TensorInfos

    @TensorInfos.setter
    def TensorInfos(self, TensorInfos):
        self._TensorInfos = TensorInfos

    @property
    def HyperParameter(self):
        return self._HyperParameter

    @HyperParameter.setter
    def HyperParameter(self, HyperParameter):
        self._HyperParameter = HyperParameter

    @property
    def AccEngineVersion(self):
        return self._AccEngineVersion

    @AccEngineVersion.setter
    def AccEngineVersion(self, AccEngineVersion):
        self._AccEngineVersion = AccEngineVersion

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsSaved(self):
        return self._IsSaved

    @IsSaved.setter
    def IsSaved(self, IsSaved):
        self._IsSaved = IsSaved

    @property
    def ModelSignature(self):
        return self._ModelSignature

    @ModelSignature.setter
    def ModelSignature(self, ModelSignature):
        self._ModelSignature = ModelSignature

    @property
    def QATModel(self):
        return self._QATModel

    @QATModel.setter
    def QATModel(self, QATModel):
        self._QATModel = QATModel

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion


    def _deserialize(self, params):
        self._ModelAccTaskId = params.get("ModelAccTaskId")
        self._ModelAccTaskName = params.get("ModelAccTaskName")
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._ModelVersion = params.get("ModelVersion")
        self._ModelSource = params.get("ModelSource")
        self._OptimizationLevel = params.get("OptimizationLevel")
        self._TaskStatus = params.get("TaskStatus")
        self._ModelInputNum = params.get("ModelInputNum")
        if params.get("ModelInputInfos") is not None:
            self._ModelInputInfos = []
            for item in params.get("ModelInputInfos"):
                obj = ModelInputInfo()
                obj._deserialize(item)
                self._ModelInputInfos.append(obj)
        self._GPUType = params.get("GPUType")
        self._ChargeType = params.get("ChargeType")
        self._Speedup = params.get("Speedup")
        if params.get("ModelInputPath") is not None:
            self._ModelInputPath = CosPathInfo()
            self._ModelInputPath._deserialize(params.get("ModelInputPath"))
        if params.get("ModelOutputPath") is not None:
            self._ModelOutputPath = CosPathInfo()
            self._ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        self._ErrorMsg = params.get("ErrorMsg")
        self._AlgorithmFramework = params.get("AlgorithmFramework")
        self._WaitNumber = params.get("WaitNumber")
        self._CreateTime = params.get("CreateTime")
        self._TaskProgress = params.get("TaskProgress")
        self._ModelFormat = params.get("ModelFormat")
        self._TensorInfos = params.get("TensorInfos")
        if params.get("HyperParameter") is not None:
            self._HyperParameter = HyperParameter()
            self._HyperParameter._deserialize(params.get("HyperParameter"))
        self._AccEngineVersion = params.get("AccEngineVersion")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsSaved = params.get("IsSaved")
        self._ModelSignature = params.get("ModelSignature")
        self._QATModel = params.get("QATModel")
        self._FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInfo(AbstractModel):
    """模型描述信息

    """

    def __init__(self):
        r"""
        :param _ModelVersionId: 模型版本id, DescribeTrainingModelVersion查询模型接口时的id
自动学习类型的模型填写自动学习的任务id
        :type ModelVersionId: str
        :param _ModelId: 模型id
        :type ModelId: str
        :param _ModelName: 模型名
        :type ModelName: str
        :param _ModelVersion: 模型版本
        :type ModelVersion: str
        :param _ModelSource: 模型来源
        :type ModelSource: str
        :param _CosPathInfo: cos路径信息
        :type CosPathInfo: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _AlgorithmFramework: 模型对应的算法框架，预留
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgorithmFramework: str
        :param _ModelType: 默认为 NORMAL, 已加速模型: ACCELERATE, 自动学习模型 AUTO_ML
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelType: str
        :param _ModelFormat: 模型格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelFormat: str
        """
        self._ModelVersionId = None
        self._ModelId = None
        self._ModelName = None
        self._ModelVersion = None
        self._ModelSource = None
        self._CosPathInfo = None
        self._AlgorithmFramework = None
        self._ModelType = None
        self._ModelFormat = None

    @property
    def ModelVersionId(self):
        return self._ModelVersionId

    @ModelVersionId.setter
    def ModelVersionId(self, ModelVersionId):
        self._ModelVersionId = ModelVersionId

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelVersion(self):
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def ModelSource(self):
        return self._ModelSource

    @ModelSource.setter
    def ModelSource(self, ModelSource):
        self._ModelSource = ModelSource

    @property
    def CosPathInfo(self):
        return self._CosPathInfo

    @CosPathInfo.setter
    def CosPathInfo(self, CosPathInfo):
        self._CosPathInfo = CosPathInfo

    @property
    def AlgorithmFramework(self):
        return self._AlgorithmFramework

    @AlgorithmFramework.setter
    def AlgorithmFramework(self, AlgorithmFramework):
        self._AlgorithmFramework = AlgorithmFramework

    @property
    def ModelType(self):
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def ModelFormat(self):
        return self._ModelFormat

    @ModelFormat.setter
    def ModelFormat(self, ModelFormat):
        self._ModelFormat = ModelFormat


    def _deserialize(self, params):
        self._ModelVersionId = params.get("ModelVersionId")
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._ModelVersion = params.get("ModelVersion")
        self._ModelSource = params.get("ModelSource")
        if params.get("CosPathInfo") is not None:
            self._CosPathInfo = CosPathInfo()
            self._CosPathInfo._deserialize(params.get("CosPathInfo"))
        self._AlgorithmFramework = params.get("AlgorithmFramework")
        self._ModelType = params.get("ModelType")
        self._ModelFormat = params.get("ModelFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInputInfo(AbstractModel):
    """模型输入信息

    """

    def __init__(self):
        r"""
        :param _ModelInputType: input数据类型
FIXED：固定
RANGE：浮动
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputType: str
        :param _ModelInputDimension: input数据尺寸
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputDimension: list of str
        """
        self._ModelInputType = None
        self._ModelInputDimension = None

    @property
    def ModelInputType(self):
        return self._ModelInputType

    @ModelInputType.setter
    def ModelInputType(self, ModelInputType):
        self._ModelInputType = ModelInputType

    @property
    def ModelInputDimension(self):
        return self._ModelInputDimension

    @ModelInputDimension.setter
    def ModelInputDimension(self, ModelInputDimension):
        self._ModelInputDimension = ModelInputDimension


    def _deserialize(self, params):
        self._ModelInputType = params.get("ModelInputType")
        self._ModelInputDimension = params.get("ModelInputDimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelServicePartialConfigRequest(AbstractModel):
    """ModifyModelServicePartialConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 在线推理服务Id，需已存在
        :type ServiceId: str
        :param _ScheduledAction: 更新后服务不重启，定时停止的配置
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param _ServiceLimit: 更新后服务不重启，服务对应限流限频配置
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        """
        self._ServiceId = None
        self._ScheduledAction = None
        self._ServiceLimit = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ScheduledAction(self):
        return self._ScheduledAction

    @ScheduledAction.setter
    def ScheduledAction(self, ScheduledAction):
        self._ScheduledAction = ScheduledAction

    @property
    def ServiceLimit(self):
        return self._ServiceLimit

    @ServiceLimit.setter
    def ServiceLimit(self, ServiceLimit):
        self._ServiceLimit = ServiceLimit


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        if params.get("ScheduledAction") is not None:
            self._ScheduledAction = ScheduledAction()
            self._ScheduledAction._deserialize(params.get("ScheduledAction"))
        if params.get("ServiceLimit") is not None:
            self._ServiceLimit = ServiceLimit()
            self._ServiceLimit._deserialize(params.get("ServiceLimit"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelServicePartialConfigResponse(AbstractModel):
    """ModifyModelServicePartialConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 被修改后的服务配置
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Service = None
        self._RequestId = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        self._RequestId = params.get("RequestId")


class ModifyModelServiceRequest(AbstractModel):
    """ModifyModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务id
        :type ServiceId: str
        :param _ModelInfo: 模型信息，需要挂载模型时填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _ImageInfo: 镜像信息，配置服务运行所需的镜像地址等信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _Env: 环境变量，可选参数，用于配置容器中的环境变量
        :type Env: list of EnvVar
        :param _Resources: 资源描述，指定预付费模式下的cpu,mem,gpu等信息，后付费无需填写
        :type Resources: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _InstanceType: 使用DescribeBillingSpecs接口返回的规格列表中的值，或者参考实例列表:
TI.S.MEDIUM.POST	2C4G
TI.S.LARGE.POST	4C8G
TI.S.2XLARGE16.POST	8C16G
TI.S.2XLARGE32.POST	8C32G
TI.S.4XLARGE32.POST	16C32G
TI.S.4XLARGE64.POST	16C64G
TI.S.6XLARGE48.POST	24C48G
TI.S.6XLARGE96.POST	24C96G
TI.S.8XLARGE64.POST	32C64G
TI.S.8XLARGE128.POST 32C128G
TI.GN7.LARGE20.POST	4C20G T4*1/4
TI.GN7.2XLARGE40.POST	10C40G T4*1/2
TI.GN7.2XLARGE32.POST	8C32G T4*1
TI.GN7.5XLARGE80.POST	20C80G T4*1
TI.GN7.8XLARGE128.POST	32C128G T4*1
TI.GN7.10XLARGE160.POST	40C160G T4*2
TI.GN7.20XLARGE320.POST	80C320G T4*4
        :type InstanceType: str
        :param _ScaleMode: 扩缩容类型 支持：自动 - "AUTO", 手动 - "MANUAL"
        :type ScaleMode: str
        :param _Replicas: 实例数量, 不同计费模式和调节模式下对应关系如下
PREPAID 和 POSTPAID_BY_HOUR:
手动调节模式下对应 实例数量
自动调节模式下对应 基于时间的默认策略的实例数量
HYBRID_PAID:
后付费实例手动调节模式下对应 实例数量
后付费实例自动调节模式下对应 时间策略的默认策略的实例数量
        :type Replicas: int
        :param _HorizontalPodAutoscaler: 自动伸缩信息
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        :param _LogEnable: 是否开启日志投递，开启后需填写配置投递到指定cls
        :type LogEnable: bool
        :param _LogConfig: 日志配置，需要投递服务日志到指定cls时填写
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _ServiceAction: 特殊更新行为： "STOP": 停止, "RESUME": 重启, "SCALE": 扩缩容, 存在这些特殊更新行为时，会忽略其他更新字段
        :type ServiceAction: str
        :param _ServiceDescription: 服务的描述
        :type ServiceDescription: str
        :param _ScaleStrategy: 自动伸缩策略
        :type ScaleStrategy: str
        :param _CronScaleJobs: 自动伸缩策略配置 HPA : 通过HPA进行弹性伸缩 CRON 通过定时任务进行伸缩
        :type CronScaleJobs: list of CronScaleJob
        :param _HybridBillingPrepaidReplicas: 计费模式[HYBRID_PAID]时生效, 用于标识混合计费模式下的预付费实例数, 若不填则默认为1
        :type HybridBillingPrepaidReplicas: int
        :param _ModelHotUpdateEnable: 是否开启模型的热更新。默认不开启
        :type ModelHotUpdateEnable: bool
        :param _ScheduledAction: 定时停止配置
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param _ServiceLimit: 服务限速限流相关配置
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param _VolumeMount: 挂载配置，目前只支持CFS
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        :param _ModelTurboEnable: 是否开启模型的加速, 仅对StableDiffusion(动态加速)格式的模型有效。默认不开启
        :type ModelTurboEnable: bool
        :param _Command: 服务的启动命令
        :type Command: str
        :param _ServiceEIP: 是否开启TIONE内网访问外部
        :type ServiceEIP: :class:`tencentcloud.tione.v20211111.models.ServiceEIP`
        """
        self._ServiceId = None
        self._ModelInfo = None
        self._ImageInfo = None
        self._Env = None
        self._Resources = None
        self._InstanceType = None
        self._ScaleMode = None
        self._Replicas = None
        self._HorizontalPodAutoscaler = None
        self._LogEnable = None
        self._LogConfig = None
        self._ServiceAction = None
        self._ServiceDescription = None
        self._ScaleStrategy = None
        self._CronScaleJobs = None
        self._HybridBillingPrepaidReplicas = None
        self._ModelHotUpdateEnable = None
        self._ScheduledAction = None
        self._ServiceLimit = None
        self._VolumeMount = None
        self._ModelTurboEnable = None
        self._Command = None
        self._ServiceEIP = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ModelInfo(self):
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ScaleMode(self):
        return self._ScaleMode

    @ScaleMode.setter
    def ScaleMode(self, ScaleMode):
        self._ScaleMode = ScaleMode

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def ServiceAction(self):
        return self._ServiceAction

    @ServiceAction.setter
    def ServiceAction(self, ServiceAction):
        self._ServiceAction = ServiceAction

    @property
    def ServiceDescription(self):
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def ScaleStrategy(self):
        return self._ScaleStrategy

    @ScaleStrategy.setter
    def ScaleStrategy(self, ScaleStrategy):
        self._ScaleStrategy = ScaleStrategy

    @property
    def CronScaleJobs(self):
        return self._CronScaleJobs

    @CronScaleJobs.setter
    def CronScaleJobs(self, CronScaleJobs):
        self._CronScaleJobs = CronScaleJobs

    @property
    def HybridBillingPrepaidReplicas(self):
        return self._HybridBillingPrepaidReplicas

    @HybridBillingPrepaidReplicas.setter
    def HybridBillingPrepaidReplicas(self, HybridBillingPrepaidReplicas):
        self._HybridBillingPrepaidReplicas = HybridBillingPrepaidReplicas

    @property
    def ModelHotUpdateEnable(self):
        return self._ModelHotUpdateEnable

    @ModelHotUpdateEnable.setter
    def ModelHotUpdateEnable(self, ModelHotUpdateEnable):
        self._ModelHotUpdateEnable = ModelHotUpdateEnable

    @property
    def ScheduledAction(self):
        return self._ScheduledAction

    @ScheduledAction.setter
    def ScheduledAction(self, ScheduledAction):
        self._ScheduledAction = ScheduledAction

    @property
    def ServiceLimit(self):
        return self._ServiceLimit

    @ServiceLimit.setter
    def ServiceLimit(self, ServiceLimit):
        self._ServiceLimit = ServiceLimit

    @property
    def VolumeMount(self):
        return self._VolumeMount

    @VolumeMount.setter
    def VolumeMount(self, VolumeMount):
        self._VolumeMount = VolumeMount

    @property
    def ModelTurboEnable(self):
        return self._ModelTurboEnable

    @ModelTurboEnable.setter
    def ModelTurboEnable(self, ModelTurboEnable):
        self._ModelTurboEnable = ModelTurboEnable

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ServiceEIP(self):
        return self._ServiceEIP

    @ServiceEIP.setter
    def ServiceEIP(self, ServiceEIP):
        self._ServiceEIP = ServiceEIP


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("Env") is not None:
            self._Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self._Env.append(obj)
        if params.get("Resources") is not None:
            self._Resources = ResourceInfo()
            self._Resources._deserialize(params.get("Resources"))
        self._InstanceType = params.get("InstanceType")
        self._ScaleMode = params.get("ScaleMode")
        self._Replicas = params.get("Replicas")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self._LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._ServiceAction = params.get("ServiceAction")
        self._ServiceDescription = params.get("ServiceDescription")
        self._ScaleStrategy = params.get("ScaleStrategy")
        if params.get("CronScaleJobs") is not None:
            self._CronScaleJobs = []
            for item in params.get("CronScaleJobs"):
                obj = CronScaleJob()
                obj._deserialize(item)
                self._CronScaleJobs.append(obj)
        self._HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
        self._ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
        if params.get("ScheduledAction") is not None:
            self._ScheduledAction = ScheduledAction()
            self._ScheduledAction._deserialize(params.get("ScheduledAction"))
        if params.get("ServiceLimit") is not None:
            self._ServiceLimit = ServiceLimit()
            self._ServiceLimit._deserialize(params.get("ServiceLimit"))
        if params.get("VolumeMount") is not None:
            self._VolumeMount = VolumeMount()
            self._VolumeMount._deserialize(params.get("VolumeMount"))
        self._ModelTurboEnable = params.get("ModelTurboEnable")
        self._Command = params.get("Command")
        if params.get("ServiceEIP") is not None:
            self._ServiceEIP = ServiceEIP()
            self._ServiceEIP._deserialize(params.get("ServiceEIP"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelServiceResponse(AbstractModel):
    """ModifyModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 生成的模型服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Service = None
        self._RequestId = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self._Service = Service()
            self._Service._deserialize(params.get("Service"))
        self._RequestId = params.get("RequestId")


class ModifyNotebookRequest(AbstractModel):
    """ModifyNotebook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: notebook id
        :type Id: str
        :param _Name: 名称
        :type Name: str
        :param _ChargeType: 计算资源付费模式 ，可选值为：
PREPAID：预付费，即包年包月
POSTPAID_BY_HOUR：按小时后付费
        :type ChargeType: str
        :param _ResourceConf: 计算资源配置
        :type ResourceConf: :class:`tencentcloud.tione.v20211111.models.ResourceConf`
        :param _LogEnable: 是否上报日志
        :type LogEnable: bool
        :param _AutoStopping: 是否自动停止
        :type AutoStopping: bool
        :param _DirectInternetAccess: 是否访问公网
        :type DirectInternetAccess: bool
        :param _RootAccess: 是否ROOT权限
        :type RootAccess: bool
        :param _ResourceGroupId: 资源组ID(for预付费)
        :type ResourceGroupId: str
        :param _VpcId: Vpc-Id
        :type VpcId: str
        :param _SubnetId: 子网Id
        :type SubnetId: str
        :param _VolumeSizeInGB: 存储卷大小，单位GB
        :type VolumeSizeInGB: int
        :param _VolumeSourceType: 存储的类型。取值包含： 
    FREE:    预付费的免费存储
    CLOUD_PREMIUM： 高性能云硬盘
    CLOUD_SSD： SSD云硬盘
    CFS:     CFS存储，包含NFS和turbo
        :type VolumeSourceType: str
        :param _VolumeSourceCFS: CFS存储的配置
        :type VolumeSourceCFS: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _LogConfig: 日志配置
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _LifecycleScriptId: 生命周期脚本的ID
        :type LifecycleScriptId: str
        :param _DefaultCodeRepoId: 默认GIT存储库的ID
        :type DefaultCodeRepoId: str
        :param _AdditionalCodeRepoIds: 其他GIT存储库的ID，最多3个
        :type AdditionalCodeRepoIds: list of str
        :param _AutomaticStopTime: 自动停止时间，单位小时
        :type AutomaticStopTime: int
        :param _Tags: 标签配置
        :type Tags: list of Tag
        :param _DataConfigs: 数据配置
        :type DataConfigs: list of DataConfig
        :param _ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _ImageType: 镜像类型
        :type ImageType: str
        :param _SSHConfig: SSH配置
        :type SSHConfig: :class:`tencentcloud.tione.v20211111.models.SSHConfig`
        """
        self._Id = None
        self._Name = None
        self._ChargeType = None
        self._ResourceConf = None
        self._LogEnable = None
        self._AutoStopping = None
        self._DirectInternetAccess = None
        self._RootAccess = None
        self._ResourceGroupId = None
        self._VpcId = None
        self._SubnetId = None
        self._VolumeSizeInGB = None
        self._VolumeSourceType = None
        self._VolumeSourceCFS = None
        self._LogConfig = None
        self._LifecycleScriptId = None
        self._DefaultCodeRepoId = None
        self._AdditionalCodeRepoIds = None
        self._AutomaticStopTime = None
        self._Tags = None
        self._DataConfigs = None
        self._ImageInfo = None
        self._ImageType = None
        self._SSHConfig = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceConf(self):
        return self._ResourceConf

    @ResourceConf.setter
    def ResourceConf(self, ResourceConf):
        self._ResourceConf = ResourceConf

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def AutoStopping(self):
        return self._AutoStopping

    @AutoStopping.setter
    def AutoStopping(self, AutoStopping):
        self._AutoStopping = AutoStopping

    @property
    def DirectInternetAccess(self):
        return self._DirectInternetAccess

    @DirectInternetAccess.setter
    def DirectInternetAccess(self, DirectInternetAccess):
        self._DirectInternetAccess = DirectInternetAccess

    @property
    def RootAccess(self):
        return self._RootAccess

    @RootAccess.setter
    def RootAccess(self, RootAccess):
        self._RootAccess = RootAccess

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

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
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB

    @property
    def VolumeSourceType(self):
        return self._VolumeSourceType

    @VolumeSourceType.setter
    def VolumeSourceType(self, VolumeSourceType):
        self._VolumeSourceType = VolumeSourceType

    @property
    def VolumeSourceCFS(self):
        return self._VolumeSourceCFS

    @VolumeSourceCFS.setter
    def VolumeSourceCFS(self, VolumeSourceCFS):
        self._VolumeSourceCFS = VolumeSourceCFS

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def LifecycleScriptId(self):
        return self._LifecycleScriptId

    @LifecycleScriptId.setter
    def LifecycleScriptId(self, LifecycleScriptId):
        self._LifecycleScriptId = LifecycleScriptId

    @property
    def DefaultCodeRepoId(self):
        return self._DefaultCodeRepoId

    @DefaultCodeRepoId.setter
    def DefaultCodeRepoId(self, DefaultCodeRepoId):
        self._DefaultCodeRepoId = DefaultCodeRepoId

    @property
    def AdditionalCodeRepoIds(self):
        return self._AdditionalCodeRepoIds

    @AdditionalCodeRepoIds.setter
    def AdditionalCodeRepoIds(self, AdditionalCodeRepoIds):
        self._AdditionalCodeRepoIds = AdditionalCodeRepoIds

    @property
    def AutomaticStopTime(self):
        return self._AutomaticStopTime

    @AutomaticStopTime.setter
    def AutomaticStopTime(self, AutomaticStopTime):
        self._AutomaticStopTime = AutomaticStopTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DataConfigs(self):
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def SSHConfig(self):
        return self._SSHConfig

    @SSHConfig.setter
    def SSHConfig(self, SSHConfig):
        self._SSHConfig = SSHConfig


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ChargeType = params.get("ChargeType")
        if params.get("ResourceConf") is not None:
            self._ResourceConf = ResourceConf()
            self._ResourceConf._deserialize(params.get("ResourceConf"))
        self._LogEnable = params.get("LogEnable")
        self._AutoStopping = params.get("AutoStopping")
        self._DirectInternetAccess = params.get("DirectInternetAccess")
        self._RootAccess = params.get("RootAccess")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        self._VolumeSourceType = params.get("VolumeSourceType")
        if params.get("VolumeSourceCFS") is not None:
            self._VolumeSourceCFS = CFSConfig()
            self._VolumeSourceCFS._deserialize(params.get("VolumeSourceCFS"))
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._LifecycleScriptId = params.get("LifecycleScriptId")
        self._DefaultCodeRepoId = params.get("DefaultCodeRepoId")
        self._AdditionalCodeRepoIds = params.get("AdditionalCodeRepoIds")
        self._AutomaticStopTime = params.get("AutomaticStopTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._ImageType = params.get("ImageType")
        if params.get("SSHConfig") is not None:
            self._SSHConfig = SSHConfig()
            self._SSHConfig._deserialize(params.get("SSHConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNotebookResponse(AbstractModel):
    """ModifyNotebook返回参数结构体

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


class ModifyNotebookTagsRequest(AbstractModel):
    """ModifyNotebookTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Notebook Id
        :type Id: str
        :param _Tags: Notebook修改标签集合
        :type Tags: list of Tag
        """
        self._Id = None
        self._Tags = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNotebookTagsResponse(AbstractModel):
    """ModifyNotebookTags返回参数结构体

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


class ModifyServiceGroupWeightsRequest(AbstractModel):
    """ModifyServiceGroupWeights请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        :param _Weights: 权重设置
        :type Weights: list of WeightEntry
        """
        self._ServiceGroupId = None
        self._Weights = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def Weights(self):
        return self._Weights

    @Weights.setter
    def Weights(self, Weights):
        self._Weights = Weights


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        if params.get("Weights") is not None:
            self._Weights = []
            for item in params.get("Weights"):
                obj = WeightEntry()
                obj._deserialize(item)
                self._Weights.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceGroupWeightsResponse(AbstractModel):
    """ModifyServiceGroupWeights返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceGroup: 更新权重后的服务组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroup: :class:`tencentcloud.tione.v20211111.models.ServiceGroup`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceGroup = None
        self._RequestId = None

    @property
    def ServiceGroup(self):
        return self._ServiceGroup

    @ServiceGroup.setter
    def ServiceGroup(self, ServiceGroup):
        self._ServiceGroup = ServiceGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceGroup") is not None:
            self._ServiceGroup = ServiceGroup()
            self._ServiceGroup._deserialize(params.get("ServiceGroup"))
        self._RequestId = params.get("RequestId")


class NotebookDetail(AbstractModel):
    """类型NotebookDetail

    """

    def __init__(self):
        r"""
        :param _Id: notebook  ID
        :type Id: str
        :param _Name: notebook 名称
        :type Name: str
        :param _LifecycleScriptId: 生命周期脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecycleScriptId: str
        :param _PodName: Pod-Name
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param _UpdateTime: Update-Time
        :type UpdateTime: str
        :param _DirectInternetAccess: 是否访问公网
        :type DirectInternetAccess: bool
        :param _ResourceGroupId: 预付费专用资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _Tags: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _AutoStopping: 是否自动停止
        :type AutoStopping: bool
        :param _AdditionalCodeRepoIds: 其他GIT存储库，最多3个，单个
长度不超过512字符
注意：此字段可能返回 null，表示取不到有效值。
        :type AdditionalCodeRepoIds: list of str
        :param _AutomaticStopTime: 自动停止时间，单位小时
注意：此字段可能返回 null，表示取不到有效值。
        :type AutomaticStopTime: int
        :param _ResourceConf: 资源配置
        :type ResourceConf: :class:`tencentcloud.tione.v20211111.models.ResourceConf`
        :param _DefaultCodeRepoId: 默认GIT存储库，长度不超过512字符
        :type DefaultCodeRepoId: str
        :param _EndTime: 训练输出
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _LogEnable: 是否上报日志
        :type LogEnable: bool
        :param _LogConfig: 日志配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Status: 任务状态
        :type Status: str
        :param _RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _StartTime: 训练开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeStatus: str
        :param _RootAccess: 是否ROOT权限
        :type RootAccess: bool
        :param _BillingInfos: 计贺金额信息，eg:2.00元/小时
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfos: list of str
        :param _VolumeSizeInGB: 存储卷大小 （单位时GB，最小10GB，必须是10G的倍数）
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        :param _FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _ChargeType: 计算资源付费模式 (- PREPAID：预付费，即包年包月 - POSTPAID_BY_HOUR：按小时后付费)
        :type ChargeType: str
        :param _InstanceTypeAlias: 后付费资源规格说明
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypeAlias: str
        :param _ResourceGroupName: 预付费资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _VolumeSourceType: 存储的类型。取值包含： 
    FREE:        预付费的免费存储
    CLOUD_PREMIUM： 高性能云硬盘
    CLOUD_SSD： SSD云硬盘
    CFS:     CFS存储，包含NFS和turbo
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSourceType: str
        :param _VolumeSourceCFS: CFS存储的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSourceCFS: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _DataConfigs: 数据配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DataConfigs: list of DataConfig
        :param _Message: notebook 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _DataSource: 数据源来源，eg：WeData_HDFS
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param _ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _ImageType: 镜像类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageType: str
        """
        self._Id = None
        self._Name = None
        self._LifecycleScriptId = None
        self._PodName = None
        self._UpdateTime = None
        self._DirectInternetAccess = None
        self._ResourceGroupId = None
        self._Tags = None
        self._AutoStopping = None
        self._AdditionalCodeRepoIds = None
        self._AutomaticStopTime = None
        self._ResourceConf = None
        self._DefaultCodeRepoId = None
        self._EndTime = None
        self._LogEnable = None
        self._LogConfig = None
        self._VpcId = None
        self._SubnetId = None
        self._Status = None
        self._RuntimeInSeconds = None
        self._CreateTime = None
        self._StartTime = None
        self._ChargeStatus = None
        self._RootAccess = None
        self._BillingInfos = None
        self._VolumeSizeInGB = None
        self._FailureReason = None
        self._ChargeType = None
        self._InstanceTypeAlias = None
        self._ResourceGroupName = None
        self._VolumeSourceType = None
        self._VolumeSourceCFS = None
        self._DataConfigs = None
        self._Message = None
        self._DataSource = None
        self._ImageInfo = None
        self._ImageType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LifecycleScriptId(self):
        return self._LifecycleScriptId

    @LifecycleScriptId.setter
    def LifecycleScriptId(self, LifecycleScriptId):
        self._LifecycleScriptId = LifecycleScriptId

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DirectInternetAccess(self):
        return self._DirectInternetAccess

    @DirectInternetAccess.setter
    def DirectInternetAccess(self, DirectInternetAccess):
        self._DirectInternetAccess = DirectInternetAccess

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AutoStopping(self):
        return self._AutoStopping

    @AutoStopping.setter
    def AutoStopping(self, AutoStopping):
        self._AutoStopping = AutoStopping

    @property
    def AdditionalCodeRepoIds(self):
        return self._AdditionalCodeRepoIds

    @AdditionalCodeRepoIds.setter
    def AdditionalCodeRepoIds(self, AdditionalCodeRepoIds):
        self._AdditionalCodeRepoIds = AdditionalCodeRepoIds

    @property
    def AutomaticStopTime(self):
        return self._AutomaticStopTime

    @AutomaticStopTime.setter
    def AutomaticStopTime(self, AutomaticStopTime):
        self._AutomaticStopTime = AutomaticStopTime

    @property
    def ResourceConf(self):
        return self._ResourceConf

    @ResourceConf.setter
    def ResourceConf(self, ResourceConf):
        self._ResourceConf = ResourceConf

    @property
    def DefaultCodeRepoId(self):
        return self._DefaultCodeRepoId

    @DefaultCodeRepoId.setter
    def DefaultCodeRepoId(self, DefaultCodeRepoId):
        self._DefaultCodeRepoId = DefaultCodeRepoId

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def RootAccess(self):
        return self._RootAccess

    @RootAccess.setter
    def RootAccess(self, RootAccess):
        self._RootAccess = RootAccess

    @property
    def BillingInfos(self):
        return self._BillingInfos

    @BillingInfos.setter
    def BillingInfos(self, BillingInfos):
        self._BillingInfos = BillingInfos

    @property
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def InstanceTypeAlias(self):
        return self._InstanceTypeAlias

    @InstanceTypeAlias.setter
    def InstanceTypeAlias(self, InstanceTypeAlias):
        self._InstanceTypeAlias = InstanceTypeAlias

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def VolumeSourceType(self):
        return self._VolumeSourceType

    @VolumeSourceType.setter
    def VolumeSourceType(self, VolumeSourceType):
        self._VolumeSourceType = VolumeSourceType

    @property
    def VolumeSourceCFS(self):
        return self._VolumeSourceCFS

    @VolumeSourceCFS.setter
    def VolumeSourceCFS(self, VolumeSourceCFS):
        self._VolumeSourceCFS = VolumeSourceCFS

    @property
    def DataConfigs(self):
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._LifecycleScriptId = params.get("LifecycleScriptId")
        self._PodName = params.get("PodName")
        self._UpdateTime = params.get("UpdateTime")
        self._DirectInternetAccess = params.get("DirectInternetAccess")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoStopping = params.get("AutoStopping")
        self._AdditionalCodeRepoIds = params.get("AdditionalCodeRepoIds")
        self._AutomaticStopTime = params.get("AutomaticStopTime")
        if params.get("ResourceConf") is not None:
            self._ResourceConf = ResourceConf()
            self._ResourceConf._deserialize(params.get("ResourceConf"))
        self._DefaultCodeRepoId = params.get("DefaultCodeRepoId")
        self._EndTime = params.get("EndTime")
        self._LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Status = params.get("Status")
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._ChargeStatus = params.get("ChargeStatus")
        self._RootAccess = params.get("RootAccess")
        self._BillingInfos = params.get("BillingInfos")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        self._FailureReason = params.get("FailureReason")
        self._ChargeType = params.get("ChargeType")
        self._InstanceTypeAlias = params.get("InstanceTypeAlias")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._VolumeSourceType = params.get("VolumeSourceType")
        if params.get("VolumeSourceCFS") is not None:
            self._VolumeSourceCFS = CFSConfig()
            self._VolumeSourceCFS._deserialize(params.get("VolumeSourceCFS"))
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        self._Message = params.get("Message")
        self._DataSource = params.get("DataSource")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._ImageType = params.get("ImageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookImageRecord(AbstractModel):
    """镜像保存记录

    """

    def __init__(self):
        r"""
        :param _RecordId: 保存记录ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _ImageUrl: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Message: 状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Kernels: kernel数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Kernels: list of str
        """
        self._RecordId = None
        self._ImageUrl = None
        self._Status = None
        self._CreateTime = None
        self._Message = None
        self._InstanceId = None
        self._Kernels = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Kernels(self):
        return self._Kernels

    @Kernels.setter
    def Kernels(self, Kernels):
        self._Kernels = Kernels


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._ImageUrl = params.get("ImageUrl")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Message = params.get("Message")
        self._InstanceId = params.get("InstanceId")
        self._Kernels = params.get("Kernels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotebookSetItem(AbstractModel):
    """Notebook列表元素

    """

    def __init__(self):
        r"""
        :param _Id: notebook ID
        :type Id: str
        :param _Name: notebook 名称
        :type Name: str
        :param _ChargeType: 计费模式
        :type ChargeType: str
        :param _ResourceConf: 资源配置
        :type ResourceConf: :class:`tencentcloud.tione.v20211111.models.ResourceConf`
        :param _ResourceGroupId: 预付费资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _VolumeSizeInGB: 存储卷大小
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        :param _BillingInfos: 计费金额信息，eg：2.00元/小时 (for后付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfos: list of str
        :param _Tags: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RuntimeInSeconds: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param _ChargeStatus: 计费状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeStatus: str
        :param _Status: 状态
        :type Status: str
        :param _FailureReason: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _PodName: Pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param _InstanceTypeAlias: 后付费资源规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypeAlias: str
        :param _ResourceGroupName: 预付费资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _AutoStopping: 是否自动终止
        :type AutoStopping: bool
        :param _AutomaticStopTime: 自动停止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AutomaticStopTime: int
        :param _VolumeSourceType: 存储的类型。取值包含： 
    FREE:        预付费的免费存储
    CLOUD_PREMIUM： 高性能云硬盘
    CLOUD_SSD： SSD云硬盘
    CFS:     CFS存储，包含NFS和turbo
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSourceType: str
        :param _VolumeSourceCFS: CFS存储的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeSourceCFS: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _Message: notebook 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _UserTypes: notebook用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserTypes: list of str
        :param _SSHConfig: SSH配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SSHConfig: :class:`tencentcloud.tione.v20211111.models.SSHConfig`
        """
        self._Id = None
        self._Name = None
        self._ChargeType = None
        self._ResourceConf = None
        self._ResourceGroupId = None
        self._VolumeSizeInGB = None
        self._BillingInfos = None
        self._Tags = None
        self._CreateTime = None
        self._StartTime = None
        self._UpdateTime = None
        self._RuntimeInSeconds = None
        self._ChargeStatus = None
        self._Status = None
        self._FailureReason = None
        self._EndTime = None
        self._PodName = None
        self._InstanceTypeAlias = None
        self._ResourceGroupName = None
        self._AutoStopping = None
        self._AutomaticStopTime = None
        self._VolumeSourceType = None
        self._VolumeSourceCFS = None
        self._Message = None
        self._UserTypes = None
        self._SSHConfig = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceConf(self):
        return self._ResourceConf

    @ResourceConf.setter
    def ResourceConf(self, ResourceConf):
        self._ResourceConf = ResourceConf

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def VolumeSizeInGB(self):
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB

    @property
    def BillingInfos(self):
        return self._BillingInfos

    @BillingInfos.setter
    def BillingInfos(self, BillingInfos):
        self._BillingInfos = BillingInfos

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def InstanceTypeAlias(self):
        return self._InstanceTypeAlias

    @InstanceTypeAlias.setter
    def InstanceTypeAlias(self, InstanceTypeAlias):
        self._InstanceTypeAlias = InstanceTypeAlias

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def AutoStopping(self):
        return self._AutoStopping

    @AutoStopping.setter
    def AutoStopping(self, AutoStopping):
        self._AutoStopping = AutoStopping

    @property
    def AutomaticStopTime(self):
        return self._AutomaticStopTime

    @AutomaticStopTime.setter
    def AutomaticStopTime(self, AutomaticStopTime):
        self._AutomaticStopTime = AutomaticStopTime

    @property
    def VolumeSourceType(self):
        return self._VolumeSourceType

    @VolumeSourceType.setter
    def VolumeSourceType(self, VolumeSourceType):
        self._VolumeSourceType = VolumeSourceType

    @property
    def VolumeSourceCFS(self):
        return self._VolumeSourceCFS

    @VolumeSourceCFS.setter
    def VolumeSourceCFS(self, VolumeSourceCFS):
        self._VolumeSourceCFS = VolumeSourceCFS

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def UserTypes(self):
        return self._UserTypes

    @UserTypes.setter
    def UserTypes(self, UserTypes):
        self._UserTypes = UserTypes

    @property
    def SSHConfig(self):
        return self._SSHConfig

    @SSHConfig.setter
    def SSHConfig(self, SSHConfig):
        self._SSHConfig = SSHConfig


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ChargeType = params.get("ChargeType")
        if params.get("ResourceConf") is not None:
            self._ResourceConf = ResourceConf()
            self._ResourceConf._deserialize(params.get("ResourceConf"))
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        self._BillingInfos = params.get("BillingInfos")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        self._ChargeStatus = params.get("ChargeStatus")
        self._Status = params.get("Status")
        self._FailureReason = params.get("FailureReason")
        self._EndTime = params.get("EndTime")
        self._PodName = params.get("PodName")
        self._InstanceTypeAlias = params.get("InstanceTypeAlias")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._AutoStopping = params.get("AutoStopping")
        self._AutomaticStopTime = params.get("AutomaticStopTime")
        self._VolumeSourceType = params.get("VolumeSourceType")
        if params.get("VolumeSourceCFS") is not None:
            self._VolumeSourceCFS = CFSConfig()
            self._VolumeSourceCFS._deserialize(params.get("VolumeSourceCFS"))
        self._Message = params.get("Message")
        self._UserTypes = params.get("UserTypes")
        if params.get("SSHConfig") is not None:
            self._SSHConfig = SSHConfig()
            self._SSHConfig._deserialize(params.get("SSHConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrLabelInfo(AbstractModel):
    """OCR场景标签列表

    """

    def __init__(self):
        r"""
        :param _Points: 坐标点围起来的框
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of PointInfo
        :param _FrameType: 框的形状：
FRAME_TYPE_RECTANGLE
FRAME_TYPE_POLYGON
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameType: str
        :param _Key: 智能结构化：key区域对应的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _KeyId: 智能结构化：上述key的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param _Value: 识别：框区域的内容
智能结构化：value区域对应的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _KeyIdsForValue: 智能结构化：value区域所关联的key 区域的keyID的集合
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyIdsForValue: list of str
        :param _Direction: key或者value区域内容的方向：
DIRECTION_VERTICAL
DIRECTION_HORIZONTAL
注意：此字段可能返回 null，表示取不到有效值。
        :type Direction: str
        """
        self._Points = None
        self._FrameType = None
        self._Key = None
        self._KeyId = None
        self._Value = None
        self._KeyIdsForValue = None
        self._Direction = None

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points

    @property
    def FrameType(self):
        return self._FrameType

    @FrameType.setter
    def FrameType(self, FrameType):
        self._FrameType = FrameType

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def KeyIdsForValue(self):
        return self._KeyIdsForValue

    @KeyIdsForValue.setter
    def KeyIdsForValue(self, KeyIdsForValue):
        self._KeyIdsForValue = KeyIdsForValue

    @property
    def Direction(self):
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = PointInfo()
                obj._deserialize(item)
                self._Points.append(obj)
        self._FrameType = params.get("FrameType")
        self._Key = params.get("Key")
        self._KeyId = params.get("KeyId")
        self._Value = params.get("Value")
        self._KeyIdsForValue = params.get("KeyIdsForValue")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Option(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Name: 指标名
        :type Name: str
        :param _Value: 指标值
        :type Value: int
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pod(AbstractModel):
    """Pod信息展示

    """

    def __init__(self):
        r"""
        :param _Name: pod名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Uid: pod的唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type Uid: str
        :param _ChargeType: 服务付费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _Phase: pod的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Phase: str
        :param _IP: pod的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _CreateTime: pod的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Containers: 容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Containers: :class:`tencentcloud.tione.v20211111.models.Container`
        :param _ContainerInfos: 容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerInfos: list of Container
        :param _CrossTenantENIInfo: 容器调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CrossTenantENIInfo: :class:`tencentcloud.tione.v20211111.models.CrossTenantENIInfo`
        """
        self._Name = None
        self._Uid = None
        self._ChargeType = None
        self._Phase = None
        self._IP = None
        self._CreateTime = None
        self._Containers = None
        self._ContainerInfos = None
        self._CrossTenantENIInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def Phase(self):
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Containers(self):
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        self._Containers = Containers

    @property
    def ContainerInfos(self):
        return self._ContainerInfos

    @ContainerInfos.setter
    def ContainerInfos(self, ContainerInfos):
        self._ContainerInfos = ContainerInfos

    @property
    def CrossTenantENIInfo(self):
        return self._CrossTenantENIInfo

    @CrossTenantENIInfo.setter
    def CrossTenantENIInfo(self, CrossTenantENIInfo):
        self._CrossTenantENIInfo = CrossTenantENIInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._ChargeType = params.get("ChargeType")
        self._Phase = params.get("Phase")
        self._IP = params.get("IP")
        self._CreateTime = params.get("CreateTime")
        if params.get("Containers") is not None:
            self._Containers = Container()
            self._Containers._deserialize(params.get("Containers"))
        if params.get("ContainerInfos") is not None:
            self._ContainerInfos = []
            for item in params.get("ContainerInfos"):
                obj = Container()
                obj._deserialize(item)
                self._ContainerInfos.append(obj)
        if params.get("CrossTenantENIInfo") is not None:
            self._CrossTenantENIInfo = CrossTenantENIInfo()
            self._CrossTenantENIInfo._deserialize(params.get("CrossTenantENIInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodInfo(AbstractModel):
    """任务建模Pod信息

    """

    def __init__(self):
        r"""
        :param _Name: pod名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _IP: pod的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _Status: pod状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _StartTime: pod启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: pod结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _ResourceConfigInfo: pod资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceConfigInfo: :class:`tencentcloud.tione.v20211111.models.ResourceConfigInfo`
        """
        self._Name = None
        self._IP = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._ResourceConfigInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

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
    def ResourceConfigInfo(self):
        return self._ResourceConfigInfo

    @ResourceConfigInfo.setter
    def ResourceConfigInfo(self, ResourceConfigInfo):
        self._ResourceConfigInfo = ResourceConfigInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IP = params.get("IP")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("ResourceConfigInfo") is not None:
            self._ResourceConfigInfo = ResourceConfigInfo()
            self._ResourceConfigInfo._deserialize(params.get("ResourceConfigInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PointInfo(AbstractModel):
    """点信息描述

    """

    def __init__(self):
        r"""
        :param _X: X坐标值
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param _Y: Y坐标值
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushTrainingMetricsRequest(AbstractModel):
    """PushTrainingMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 指标数据
        :type Data: list of MetricData
        """
        self._Data = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushTrainingMetricsResponse(AbstractModel):
    """PushTrainingMetrics返回参数结构体

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


class RDMAConfig(AbstractModel):
    """RDMA配置

    """

    def __init__(self):
        r"""
        :param _Enable: 是否开启RDMA
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        """
        self._Enable = None

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConf(AbstractModel):
    """Notebook资源参数

    """

    def __init__(self):
        r"""
        :param _Cpu: cpu 处理器资源, 单位为1/1000核 (for预付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Memory: memory 内存资源, 单位为1M (for预付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _Gpu: gpu Gpu卡资源，单位为1单位的GpuType，例如GpuType=T4时，1 Gpu = 1/100 T4卡，GpuType=vcuda时，1 Gpu = 1/100 vcuda-core (for预付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param _GpuType: GpuType 卡类型 vcuda, T4,P4,V100等 (for预付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param _InstanceType: 计算规格 (for后付费)，可选值如下：
TI.S.LARGE.POST: 4C8G 
TI.S.2XLARGE16.POST:  8C16G 
TI.S.2XLARGE32.POST:  8C32G 
TI.S.4XLARGE32.POST:  16C32G
TI.S.4XLARGE64.POST:  16C64G
TI.S.6XLARGE48.POST:  24C48G
TI.S.6XLARGE96.POST:  24C96G
TI.S.8XLARGE64.POST:  32C64G
TI.S.8XLARGE128.POST : 32C128G
TI.GN10.2XLARGE40.POST: 8C40G V100*1 
TI.GN10.5XLARGE80.POST:  18C80G V100*2 
TI.GN10.10XLARGE160.POST :  32C160G V100*4
TI.GN10.20XLARGE320.POST :  72C320G V100*8
TI.GN7.8XLARGE128.POST: 32C128G T4*1 
TI.GN7.10XLARGE160.POST: 40C160G T4*2 
TI.GN7.20XLARGE320.POST: 80C320G T4*4
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._GpuType = None
        self._InstanceType = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuType(self):
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._GpuType = params.get("GpuType")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConfigInfo(AbstractModel):
    """资源配置

    """

    def __init__(self):
        r"""
        :param _Role: 角色，eg：PS、WORKER、DRIVER、EXECUTOR
        :type Role: str
        :param _Cpu: cpu核数，1000=1核
        :type Cpu: int
        :param _Memory: 内存，单位为MB
        :type Memory: int
        :param _GpuType: gpu卡类型
        :type GpuType: str
        :param _Gpu: gpu数
        :type Gpu: int
        :param _InstanceType: 算力规格ID
计算规格 (for后付费)，可选值如下：
TI.S.LARGE.POST: 4C8G 
TI.S.2XLARGE16.POST:  8C16G 
TI.S.2XLARGE32.POST:  8C32G 
TI.S.4XLARGE32.POST:  16C32G
TI.S.4XLARGE64.POST:  16C64G
TI.S.6XLARGE48.POST:  24C48G
TI.S.6XLARGE96.POST:  24C96G
TI.S.8XLARGE64.POST:  32C64G
TI.S.8XLARGE128.POST : 32C128G
TI.GN10.2XLARGE40.POST: 8C40G V100*1 
TI.GN10.5XLARGE80.POST:  18C80G V100*2 
TI.GN10.10XLARGE160.POST :  32C160G V100*4
TI.GN10.20XLARGE320.POST :  72C320G V100*8
TI.GN7.8XLARGE128.POST: 32C128G T4*1 
TI.GN7.10XLARGE160.POST: 40C160G T4*2 
TI.GN7.20XLARGE320.POST: 80C32
        :type InstanceType: str
        :param _InstanceNum: 计算节点数
        :type InstanceNum: int
        :param _InstanceTypeAlias: 算力规格名称
计算规格 (for后付费)，可选值如下：
4C8G 
8C16G 
8C32G 
16C32G
6C64G
24C48G
24C96G
32C64G
32C128G
8C40G V100*1 
8C80G V100*2 
32C160G V100*4
72C320G V100*8
32C128G T4*1 
40C160G T4*2 
80C32
        :type InstanceTypeAlias: str
        :param _RDMAConfig: RDMA配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RDMAConfig: :class:`tencentcloud.tione.v20211111.models.RDMAConfig`
        """
        self._Role = None
        self._Cpu = None
        self._Memory = None
        self._GpuType = None
        self._Gpu = None
        self._InstanceType = None
        self._InstanceNum = None
        self._InstanceTypeAlias = None
        self._RDMAConfig = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def GpuType(self):
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceNum(self):
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def InstanceTypeAlias(self):
        return self._InstanceTypeAlias

    @InstanceTypeAlias.setter
    def InstanceTypeAlias(self, InstanceTypeAlias):
        self._InstanceTypeAlias = InstanceTypeAlias

    @property
    def RDMAConfig(self):
        return self._RDMAConfig

    @RDMAConfig.setter
    def RDMAConfig(self, RDMAConfig):
        self._RDMAConfig = RDMAConfig


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._GpuType = params.get("GpuType")
        self._Gpu = params.get("Gpu")
        self._InstanceType = params.get("InstanceType")
        self._InstanceNum = params.get("InstanceNum")
        self._InstanceTypeAlias = params.get("InstanceTypeAlias")
        if params.get("RDMAConfig") is not None:
            self._RDMAConfig = RDMAConfig()
            self._RDMAConfig._deserialize(params.get("RDMAConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceGroup(AbstractModel):
    """资源组

    """

    def __init__(self):
        r"""
        :param _ResourceGroupId: 资源组id
        :type ResourceGroupId: str
        :param _ResourceGroupName: 资源组名称
        :type ResourceGroupName: str
        :param _FreeInstance: 可用节点个数(运行中的节点)
        :type FreeInstance: int
        :param _TotalInstance: 总节点个数(所有节点)
        :type TotalInstance: int
        :param _UsedResource: 资资源组已用的资源
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedResource: :class:`tencentcloud.tione.v20211111.models.GroupResource`
        :param _TotalResource: 资源组总资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalResource: :class:`tencentcloud.tione.v20211111.models.GroupResource`
        :param _InstanceSet: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of Instance
        :param _TagSet: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        """
        self._ResourceGroupId = None
        self._ResourceGroupName = None
        self._FreeInstance = None
        self._TotalInstance = None
        self._UsedResource = None
        self._TotalResource = None
        self._InstanceSet = None
        self._TagSet = None

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def FreeInstance(self):
        return self._FreeInstance

    @FreeInstance.setter
    def FreeInstance(self, FreeInstance):
        self._FreeInstance = FreeInstance

    @property
    def TotalInstance(self):
        return self._TotalInstance

    @TotalInstance.setter
    def TotalInstance(self, TotalInstance):
        self._TotalInstance = TotalInstance

    @property
    def UsedResource(self):
        return self._UsedResource

    @UsedResource.setter
    def UsedResource(self, UsedResource):
        self._UsedResource = UsedResource

    @property
    def TotalResource(self):
        return self._TotalResource

    @TotalResource.setter
    def TotalResource(self, TotalResource):
        self._TotalResource = TotalResource

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._FreeInstance = params.get("FreeInstance")
        self._TotalInstance = params.get("TotalInstance")
        if params.get("UsedResource") is not None:
            self._UsedResource = GroupResource()
            self._UsedResource._deserialize(params.get("UsedResource"))
        if params.get("TotalResource") is not None:
            self._TotalResource = GroupResource()
            self._TotalResource._deserialize(params.get("TotalResource"))
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInfo(AbstractModel):
    """描述资源信息

    """

    def __init__(self):
        r"""
        :param _Cpu: 处理器资源, 单位为1/1000核
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Memory: 内存资源, 单位为1M
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _Gpu: Gpu卡个数资源, 单位为0.01单位的GpuType.
Gpu=100表示使用了“一张”gpu卡, 但此处的“一张”卡有可能是虚拟化后的1/4卡, 也有可能是整张卡. 取决于实例的机型
例1 实例的机型带有1张虚拟gpu卡, 每张虚拟gpu卡对应1/4张实际T4卡, 则此时 GpuType=T4, Gpu=100, RealGpu=25.
例2 实例的机型带有4张gpu整卡, 每张卡对应1张实际T4卡, 则 此时 GpuType=T4, Gpu=400, RealGpu=400.
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param _GpuType: Gpu卡型号 T4或者V100。仅展示当前 GPU 卡型号，若存在多类型同时使用，则参考 RealGpuDetailSet 的值。
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param _RealGpu: 创建或更新时无需填写，仅展示需要关注
后付费非整卡实例对应的实际的Gpu卡资源, 表示gpu资源对应实际的gpu卡个数.
RealGpu=100表示实际使用了一张gpu卡, 对应实际的实例机型, 有可能代表带有1/4卡的实例4个, 或者带有1/2卡的实例2个, 或者带有1卡的实力1个.
        :type RealGpu: int
        :param _RealGpuDetailSet: 创建或更新时无需填写，仅展示需要关注。详细的GPU使用信息。
        :type RealGpuDetailSet: list of GpuDetail
        """
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._GpuType = None
        self._RealGpu = None
        self._RealGpuDetailSet = None

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuType(self):
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def RealGpu(self):
        return self._RealGpu

    @RealGpu.setter
    def RealGpu(self, RealGpu):
        self._RealGpu = RealGpu

    @property
    def RealGpuDetailSet(self):
        return self._RealGpuDetailSet

    @RealGpuDetailSet.setter
    def RealGpuDetailSet(self, RealGpuDetailSet):
        self._RealGpuDetailSet = RealGpuDetailSet


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._GpuType = params.get("GpuType")
        self._RealGpu = params.get("RealGpu")
        if params.get("RealGpuDetailSet") is not None:
            self._RealGpuDetailSet = []
            for item in params.get("RealGpuDetailSet"):
                obj = GpuDetail()
                obj._deserialize(item)
                self._RealGpuDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInstanceRunningJobInfo(AbstractModel):
    """资源组节点运行任务信息

    """

    def __init__(self):
        r"""
        :param _PodName: pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param _TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param _TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _TaskName: 任务自定义名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskName: str
        """
        self._PodName = None
        self._TaskType = None
        self._TaskId = None
        self._TaskName = None

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName


    def _deserialize(self, params):
        self._PodName = params.get("PodName")
        self._TaskType = params.get("TaskType")
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartModelAccelerateTaskRequest(AbstractModel):
    """RestartModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        :param _ModelAccTaskName: 模型加速任务名称
        :type ModelAccTaskName: str
        :param _ModelSource: 模型来源（JOB/COS）
        :type ModelSource: str
        :param _AlgorithmFramework: 算法框架（废弃）
        :type AlgorithmFramework: str
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _ModelVersion: 模型版本
        :type ModelVersion: str
        :param _ModelInputPath: 模型输入cos路径
        :type ModelInputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _OptimizationLevel: 优化级别（NO_LOSS/FP16/INT8），默认FP16
        :type OptimizationLevel: str
        :param _ModelInputNum: input节点个数（废弃）
        :type ModelInputNum: int
        :param _ModelInputInfos: input节点信息（废弃）
        :type ModelInputInfos: list of ModelInputInfo
        :param _ModelOutputPath: 模型输出cos路径
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _ModelFormat: 模型格式（TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/MMDETECTION/ONNX/HUGGING_FACE）
        :type ModelFormat: str
        :param _TensorInfos: 模型Tensor信息
        :type TensorInfos: list of str
        :param _GPUType: GPU类型（T4/V100/A10），默认T4
        :type GPUType: str
        :param _HyperParameter: 模型专业参数
        :type HyperParameter: :class:`tencentcloud.tione.v20211111.models.HyperParameter`
        :param _AccEngineVersion: 加速引擎版本
        :type AccEngineVersion: str
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _ModelSignature: SavedModel保存时配置的签名
        :type ModelSignature: str
        :param _FrameworkVersion: 加速引擎对应的框架版本
        :type FrameworkVersion: str
        """
        self._ModelAccTaskId = None
        self._ModelAccTaskName = None
        self._ModelSource = None
        self._AlgorithmFramework = None
        self._ModelId = None
        self._ModelName = None
        self._ModelVersion = None
        self._ModelInputPath = None
        self._OptimizationLevel = None
        self._ModelInputNum = None
        self._ModelInputInfos = None
        self._ModelOutputPath = None
        self._ModelFormat = None
        self._TensorInfos = None
        self._GPUType = None
        self._HyperParameter = None
        self._AccEngineVersion = None
        self._Tags = None
        self._ModelSignature = None
        self._FrameworkVersion = None

    @property
    def ModelAccTaskId(self):
        return self._ModelAccTaskId

    @ModelAccTaskId.setter
    def ModelAccTaskId(self, ModelAccTaskId):
        self._ModelAccTaskId = ModelAccTaskId

    @property
    def ModelAccTaskName(self):
        return self._ModelAccTaskName

    @ModelAccTaskName.setter
    def ModelAccTaskName(self, ModelAccTaskName):
        self._ModelAccTaskName = ModelAccTaskName

    @property
    def ModelSource(self):
        return self._ModelSource

    @ModelSource.setter
    def ModelSource(self, ModelSource):
        self._ModelSource = ModelSource

    @property
    def AlgorithmFramework(self):
        return self._AlgorithmFramework

    @AlgorithmFramework.setter
    def AlgorithmFramework(self, AlgorithmFramework):
        self._AlgorithmFramework = AlgorithmFramework

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelVersion(self):
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def ModelInputPath(self):
        return self._ModelInputPath

    @ModelInputPath.setter
    def ModelInputPath(self, ModelInputPath):
        self._ModelInputPath = ModelInputPath

    @property
    def OptimizationLevel(self):
        return self._OptimizationLevel

    @OptimizationLevel.setter
    def OptimizationLevel(self, OptimizationLevel):
        self._OptimizationLevel = OptimizationLevel

    @property
    def ModelInputNum(self):
        return self._ModelInputNum

    @ModelInputNum.setter
    def ModelInputNum(self, ModelInputNum):
        self._ModelInputNum = ModelInputNum

    @property
    def ModelInputInfos(self):
        return self._ModelInputInfos

    @ModelInputInfos.setter
    def ModelInputInfos(self, ModelInputInfos):
        self._ModelInputInfos = ModelInputInfos

    @property
    def ModelOutputPath(self):
        return self._ModelOutputPath

    @ModelOutputPath.setter
    def ModelOutputPath(self, ModelOutputPath):
        self._ModelOutputPath = ModelOutputPath

    @property
    def ModelFormat(self):
        return self._ModelFormat

    @ModelFormat.setter
    def ModelFormat(self, ModelFormat):
        self._ModelFormat = ModelFormat

    @property
    def TensorInfos(self):
        return self._TensorInfos

    @TensorInfos.setter
    def TensorInfos(self, TensorInfos):
        self._TensorInfos = TensorInfos

    @property
    def GPUType(self):
        return self._GPUType

    @GPUType.setter
    def GPUType(self, GPUType):
        self._GPUType = GPUType

    @property
    def HyperParameter(self):
        return self._HyperParameter

    @HyperParameter.setter
    def HyperParameter(self, HyperParameter):
        self._HyperParameter = HyperParameter

    @property
    def AccEngineVersion(self):
        return self._AccEngineVersion

    @AccEngineVersion.setter
    def AccEngineVersion(self, AccEngineVersion):
        self._AccEngineVersion = AccEngineVersion

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ModelSignature(self):
        return self._ModelSignature

    @ModelSignature.setter
    def ModelSignature(self, ModelSignature):
        self._ModelSignature = ModelSignature

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion


    def _deserialize(self, params):
        self._ModelAccTaskId = params.get("ModelAccTaskId")
        self._ModelAccTaskName = params.get("ModelAccTaskName")
        self._ModelSource = params.get("ModelSource")
        self._AlgorithmFramework = params.get("AlgorithmFramework")
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._ModelVersion = params.get("ModelVersion")
        if params.get("ModelInputPath") is not None:
            self._ModelInputPath = CosPathInfo()
            self._ModelInputPath._deserialize(params.get("ModelInputPath"))
        self._OptimizationLevel = params.get("OptimizationLevel")
        self._ModelInputNum = params.get("ModelInputNum")
        if params.get("ModelInputInfos") is not None:
            self._ModelInputInfos = []
            for item in params.get("ModelInputInfos"):
                obj = ModelInputInfo()
                obj._deserialize(item)
                self._ModelInputInfos.append(obj)
        if params.get("ModelOutputPath") is not None:
            self._ModelOutputPath = CosPathInfo()
            self._ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        self._ModelFormat = params.get("ModelFormat")
        self._TensorInfos = params.get("TensorInfos")
        self._GPUType = params.get("GPUType")
        if params.get("HyperParameter") is not None:
            self._HyperParameter = HyperParameter()
            self._HyperParameter._deserialize(params.get("HyperParameter"))
        self._AccEngineVersion = params.get("AccEngineVersion")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ModelSignature = params.get("ModelSignature")
        self._FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartModelAccelerateTaskResponse(AbstractModel):
    """RestartModelAccelerateTask返回参数结构体

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


class RowItem(AbstractModel):
    """文本行信息

    """

    def __init__(self):
        r"""
        :param _Values: rowValue 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of RowValue
        """
        self._Values = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = RowValue()
                obj._deserialize(item)
                self._Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowValue(AbstractModel):
    """文件行信息

    """

    def __init__(self):
        r"""
        :param _Name: 列名
        :type Name: str
        :param _Value: 列值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SSHConfig(AbstractModel):
    """notebook ssh端口配置

    """

    def __init__(self):
        r"""
        :param _Enable: 是否开启ssh
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        :param _PublicKey: 公钥信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKey: str
        :param _Port: 端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _LoginCommand: 登录命令
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginCommand: str
        """
        self._Enable = None
        self._PublicKey = None
        self._Port = None
        self._LoginCommand = None

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def LoginCommand(self):
        return self._LoginCommand

    @LoginCommand.setter
    def LoginCommand(self, LoginCommand):
        self._LoginCommand = LoginCommand


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._PublicKey = params.get("PublicKey")
        self._Port = params.get("Port")
        self._LoginCommand = params.get("LoginCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledAction(AbstractModel):
    """定时的事务和行为

    """

    def __init__(self):
        r"""
        :param _ScheduleStop: 是否要定时停止服务，true or false。true 则 ScheduleStopTime 必填， false 则 ScheduleStopTime 不生效
        :type ScheduleStop: bool
        :param _ScheduleStopTime: 要执行定时停止的时间，格式：“2022-01-26T19:46:22+08:00”
        :type ScheduleStopTime: str
        """
        self._ScheduleStop = None
        self._ScheduleStopTime = None

    @property
    def ScheduleStop(self):
        return self._ScheduleStop

    @ScheduleStop.setter
    def ScheduleStop(self, ScheduleStop):
        self._ScheduleStop = ScheduleStop

    @property
    def ScheduleStopTime(self):
        return self._ScheduleStopTime

    @ScheduleStopTime.setter
    def ScheduleStopTime(self, ScheduleStopTime):
        self._ScheduleStopTime = ScheduleStopTime


    def _deserialize(self, params):
        self._ScheduleStop = params.get("ScheduleStop")
        self._ScheduleStopTime = params.get("ScheduleStopTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaInfo(AbstractModel):
    """表格数据集表头信息

    """

    def __init__(self):
        r"""
        :param _Name: 长度30字符内
        :type Name: str
        :param _Type: 数据类型
        :type Type: str
        """
        self._Name = None
        self._Type = None

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


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentationInfo(AbstractModel):
    """图片分割参数信息

    """

    def __init__(self):
        r"""
        :param _Points: 点坐标数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of PointInfo
        :param _Label: 分割标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Gray: 灰度值
注意：此字段可能返回 null，表示取不到有效值。
        :type Gray: int
        :param _Color: 颜色
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: str
        """
        self._Points = None
        self._Label = None
        self._Gray = None
        self._Color = None

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Gray(self):
        return self._Gray

    @Gray.setter
    def Gray(self, Gray):
        self._Gray = Gray

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self._Points = []
            for item in params.get("Points"):
                obj = PointInfo()
                obj._deserialize(item)
                self._Points.append(obj)
        self._Label = params.get("Label")
        self._Gray = params.get("Gray")
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendChatMessageRequest(AbstractModel):
    """SendChatMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话id，标识一组对话的唯一id，id变更则重置会话
        :type SessionId: str
        :param _Question: 问题描述
        :type Question: str
        :param _ModelVersion: 会话模型版本。
多行业客服大模型：填写demo_big_model_version_id。
默认为demo_big_model_version_id，即多行业客服大模型。
        :type ModelVersion: str
        :param _Mode: 使用模式(仅多场景客服大模型支持)。
通用问答：填写General。
搜索增强问答：填写WithSearchPlugin。
默认为General，即通用问答。
        :type Mode: str
        :param _SearchSource: 搜索来源。仅当Mode为WithSearchPlugin时生效。
预置文稿库：填写Preset。自定义：填写Custom。
        :type SearchSource: str
        """
        self._SessionId = None
        self._Question = None
        self._ModelVersion = None
        self._Mode = None
        self._SearchSource = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def ModelVersion(self):
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SearchSource(self):
        return self._SearchSource

    @SearchSource.setter
    def SearchSource(self, SearchSource):
        self._SearchSource = SearchSource


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Question = params.get("Question")
        self._ModelVersion = params.get("ModelVersion")
        self._Mode = params.get("Mode")
        self._SearchSource = params.get("SearchSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendChatMessageResponse(AbstractModel):
    """SendChatMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Answer: 答案
        :type Answer: str
        :param _SessionId: 会话id,返回请求的会话id
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Answer = None
        self._SessionId = None
        self._RequestId = None

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Answer = params.get("Answer")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class Service(AbstractModel):
    """描述在线服务

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        :param _ServiceId: 服务id
        :type ServiceId: str
        :param _ServiceGroupName: 服务组名
        :type ServiceGroupName: str
        :param _ServiceDescription: 服务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDescription: str
        :param _ServiceInfo: 服务的详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInfo: :class:`tencentcloud.tione.v20211111.models.ServiceInfo`
        :param _ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _ChargeType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _ResourceGroupId: 包年包月服务的资源组id，按量计费的服务为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ResourceGroupName: 包年包月服务对应的资源组名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _Tags: 服务的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _IngressName: 服务所在的 ingress 的 name
注意：此字段可能返回 null，表示取不到有效值。
        :type IngressName: str
        :param _CreatedBy: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedBy: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Uin: 主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _SubUin: 子账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubUin: str
        :param _AppId: app_id
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _BusinessStatus: 服务的业务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessStatus: str
        :param _ServiceLimit: 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param _ScheduledAction: 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param _CreateFailedReason: 服务创建失败的原因，创建成功后该字段为默认值 CREATE_SUCCEED
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateFailedReason: str
        :param _Status: 服务状态
CREATING 创建中
CREATE_FAILED 创建失败
Normal	正常运行中
Stopped  已停止
Stopping 停止中
Abnormal 异常
Pending 启动中
Waiting 就绪中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _BillingInfo: 费用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param _Weight: 模型权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _CreateSource: 服务的创建来源
AUTO_ML: 来自自动学习的一键发布
DEFAULT: 其他来源
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateSource: str
        :param _Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _LatestVersion: 服务组下服务的最高版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersion: str
        """
        self._ServiceGroupId = None
        self._ServiceId = None
        self._ServiceGroupName = None
        self._ServiceDescription = None
        self._ServiceInfo = None
        self._ClusterId = None
        self._Region = None
        self._Namespace = None
        self._ChargeType = None
        self._ResourceGroupId = None
        self._ResourceGroupName = None
        self._Tags = None
        self._IngressName = None
        self._CreatedBy = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Uin = None
        self._SubUin = None
        self._AppId = None
        self._BusinessStatus = None
        self._ServiceLimit = None
        self._ScheduledAction = None
        self._CreateFailedReason = None
        self._Status = None
        self._BillingInfo = None
        self._Weight = None
        self._CreateSource = None
        self._Version = None
        self._LatestVersion = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceGroupName(self):
        return self._ServiceGroupName

    @ServiceGroupName.setter
    def ServiceGroupName(self, ServiceGroupName):
        self._ServiceGroupName = ServiceGroupName

    @property
    def ServiceDescription(self):
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def ServiceInfo(self):
        return self._ServiceInfo

    @ServiceInfo.setter
    def ServiceInfo(self, ServiceInfo):
        self._ServiceInfo = ServiceInfo

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def CreatedBy(self):
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def BusinessStatus(self):
        return self._BusinessStatus

    @BusinessStatus.setter
    def BusinessStatus(self, BusinessStatus):
        self._BusinessStatus = BusinessStatus

    @property
    def ServiceLimit(self):
        return self._ServiceLimit

    @ServiceLimit.setter
    def ServiceLimit(self, ServiceLimit):
        self._ServiceLimit = ServiceLimit

    @property
    def ScheduledAction(self):
        return self._ScheduledAction

    @ScheduledAction.setter
    def ScheduledAction(self, ScheduledAction):
        self._ScheduledAction = ScheduledAction

    @property
    def CreateFailedReason(self):
        return self._CreateFailedReason

    @CreateFailedReason.setter
    def CreateFailedReason(self, CreateFailedReason):
        self._CreateFailedReason = CreateFailedReason

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BillingInfo(self):
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreateSource(self):
        return self._CreateSource

    @CreateSource.setter
    def CreateSource(self, CreateSource):
        self._CreateSource = CreateSource

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LatestVersion(self):
        return self._LatestVersion

    @LatestVersion.setter
    def LatestVersion(self, LatestVersion):
        self._LatestVersion = LatestVersion


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._ServiceId = params.get("ServiceId")
        self._ServiceGroupName = params.get("ServiceGroupName")
        self._ServiceDescription = params.get("ServiceDescription")
        if params.get("ServiceInfo") is not None:
            self._ServiceInfo = ServiceInfo()
            self._ServiceInfo._deserialize(params.get("ServiceInfo"))
        self._ClusterId = params.get("ClusterId")
        self._Region = params.get("Region")
        self._Namespace = params.get("Namespace")
        self._ChargeType = params.get("ChargeType")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IngressName = params.get("IngressName")
        self._CreatedBy = params.get("CreatedBy")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._AppId = params.get("AppId")
        self._BusinessStatus = params.get("BusinessStatus")
        if params.get("ServiceLimit") is not None:
            self._ServiceLimit = ServiceLimit()
            self._ServiceLimit._deserialize(params.get("ServiceLimit"))
        if params.get("ScheduledAction") is not None:
            self._ScheduledAction = ScheduledAction()
            self._ScheduledAction._deserialize(params.get("ScheduledAction"))
        self._CreateFailedReason = params.get("CreateFailedReason")
        self._Status = params.get("Status")
        self._BillingInfo = params.get("BillingInfo")
        self._Weight = params.get("Weight")
        self._CreateSource = params.get("CreateSource")
        self._Version = params.get("Version")
        self._LatestVersion = params.get("LatestVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceCallInfo(AbstractModel):
    """服务的调用信息，服务组下唯一

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 服务组id
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroupId: str
        :param _InnerHttpAddr: 内网http调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpAddr: str
        :param _InnerHttpsAddr: 内网https调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpsAddr: str
        :param _OuterHttpAddr: 内网http调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type OuterHttpAddr: str
        :param _OuterHttpsAddr: 内网https调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type OuterHttpsAddr: str
        :param _AppKey: 调用key
注意：此字段可能返回 null，表示取不到有效值。
        :type AppKey: str
        :param _AppSecret: 调用secret
注意：此字段可能返回 null，表示取不到有效值。
        :type AppSecret: str
        """
        self._ServiceGroupId = None
        self._InnerHttpAddr = None
        self._InnerHttpsAddr = None
        self._OuterHttpAddr = None
        self._OuterHttpsAddr = None
        self._AppKey = None
        self._AppSecret = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def InnerHttpAddr(self):
        return self._InnerHttpAddr

    @InnerHttpAddr.setter
    def InnerHttpAddr(self, InnerHttpAddr):
        self._InnerHttpAddr = InnerHttpAddr

    @property
    def InnerHttpsAddr(self):
        return self._InnerHttpsAddr

    @InnerHttpsAddr.setter
    def InnerHttpsAddr(self, InnerHttpsAddr):
        self._InnerHttpsAddr = InnerHttpsAddr

    @property
    def OuterHttpAddr(self):
        return self._OuterHttpAddr

    @OuterHttpAddr.setter
    def OuterHttpAddr(self, OuterHttpAddr):
        self._OuterHttpAddr = OuterHttpAddr

    @property
    def OuterHttpsAddr(self):
        return self._OuterHttpsAddr

    @OuterHttpsAddr.setter
    def OuterHttpsAddr(self, OuterHttpsAddr):
        self._OuterHttpsAddr = OuterHttpsAddr

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppSecret(self):
        return self._AppSecret

    @AppSecret.setter
    def AppSecret(self, AppSecret):
        self._AppSecret = AppSecret


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._InnerHttpAddr = params.get("InnerHttpAddr")
        self._InnerHttpsAddr = params.get("InnerHttpsAddr")
        self._OuterHttpAddr = params.get("OuterHttpAddr")
        self._OuterHttpsAddr = params.get("OuterHttpsAddr")
        self._AppKey = params.get("AppKey")
        self._AppSecret = params.get("AppSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEIP(AbstractModel):
    """服务共享弹性网卡设置

    """

    def __init__(self):
        r"""
        :param _EnableEIP: 是否开启TIONE内网到外部的访问
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableEIP: bool
        :param _VpcId: 用户VpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 用户subnetId
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self._EnableEIP = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def EnableEIP(self):
        return self._EnableEIP

    @EnableEIP.setter
    def EnableEIP(self, EnableEIP):
        self._EnableEIP = EnableEIP

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


    def _deserialize(self, params):
        self._EnableEIP = params.get("EnableEIP")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEIPInfo(AbstractModel):
    """共享弹性网卡信息

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _VpcId: 用户VpcId
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 用户子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self._ServiceId = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

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


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGroup(AbstractModel):
    """在线服务一个服务组的信息

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        :param _ServiceGroupName: 服务组名
        :type ServiceGroupName: str
        :param _CreatedBy: 创建者
        :type CreatedBy: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Uin: 主账号
        :type Uin: str
        :param _ServiceCount: 服务组下服务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param _RunningServiceCount: 服务组下在运行的服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningServiceCount: int
        :param _Services: 服务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of Service
        :param _Status: 服务组状态，与服务一致
 CREATING 创建中
     CREATE_FAILED 创建失败
     Normal	正常运行中
     Stopped  已停止
     Stopping 停止中
     Abnormal 异常
     Pending 启动中
     Waiting 就绪中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Tags: 服务组标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _LatestVersion: 服务组下最高版本
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersion: str
        :param _BusinessStatus: 服务的业务状态
CREATING 创建中
     CREATE_FAILED 创建失败
     ARREARS_STOP 因欠费被强制停止
     BILLING 计费中
     WHITELIST_USING 白名单试用中
     WHITELIST_STOP 白名单额度不足
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessStatus: str
        :param _BillingInfo: 服务的计费信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param _CreateSource: 服务的创建来源
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateSource: str
        :param _WeightUpdateStatus: 服务组的权重更新状态 
UPDATING 更新中
     UPDATED 更新成功
     UPDATE_FAILED 更新失败
注意：此字段可能返回 null，表示取不到有效值。
        :type WeightUpdateStatus: str
        """
        self._ServiceGroupId = None
        self._ServiceGroupName = None
        self._CreatedBy = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Uin = None
        self._ServiceCount = None
        self._RunningServiceCount = None
        self._Services = None
        self._Status = None
        self._Tags = None
        self._LatestVersion = None
        self._BusinessStatus = None
        self._BillingInfo = None
        self._CreateSource = None
        self._WeightUpdateStatus = None

    @property
    def ServiceGroupId(self):
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def ServiceGroupName(self):
        return self._ServiceGroupName

    @ServiceGroupName.setter
    def ServiceGroupName(self, ServiceGroupName):
        self._ServiceGroupName = ServiceGroupName

    @property
    def CreatedBy(self):
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ServiceCount(self):
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def RunningServiceCount(self):
        return self._RunningServiceCount

    @RunningServiceCount.setter
    def RunningServiceCount(self, RunningServiceCount):
        self._RunningServiceCount = RunningServiceCount

    @property
    def Services(self):
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

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

    @property
    def LatestVersion(self):
        return self._LatestVersion

    @LatestVersion.setter
    def LatestVersion(self, LatestVersion):
        self._LatestVersion = LatestVersion

    @property
    def BusinessStatus(self):
        return self._BusinessStatus

    @BusinessStatus.setter
    def BusinessStatus(self, BusinessStatus):
        self._BusinessStatus = BusinessStatus

    @property
    def BillingInfo(self):
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo

    @property
    def CreateSource(self):
        return self._CreateSource

    @CreateSource.setter
    def CreateSource(self, CreateSource):
        self._CreateSource = CreateSource

    @property
    def WeightUpdateStatus(self):
        return self._WeightUpdateStatus

    @WeightUpdateStatus.setter
    def WeightUpdateStatus(self, WeightUpdateStatus):
        self._WeightUpdateStatus = WeightUpdateStatus


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._ServiceGroupName = params.get("ServiceGroupName")
        self._CreatedBy = params.get("CreatedBy")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Uin = params.get("Uin")
        self._ServiceCount = params.get("ServiceCount")
        self._RunningServiceCount = params.get("RunningServiceCount")
        if params.get("Services") is not None:
            self._Services = []
            for item in params.get("Services"):
                obj = Service()
                obj._deserialize(item)
                self._Services.append(obj)
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._LatestVersion = params.get("LatestVersion")
        self._BusinessStatus = params.get("BusinessStatus")
        self._BillingInfo = params.get("BillingInfo")
        self._CreateSource = params.get("CreateSource")
        self._WeightUpdateStatus = params.get("WeightUpdateStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceHistory(AbstractModel):
    """服务历史版本

    """

    def __init__(self):
        r"""
        :param _Revision: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Revision: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Image: 镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param _ModelFile: 模型文件
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelFile: str
        :param _RawData: 原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :type RawData: str
        """
        self._Revision = None
        self._UpdateTime = None
        self._Image = None
        self._ModelFile = None
        self._RawData = None

    @property
    def Revision(self):
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ModelFile(self):
        return self._ModelFile

    @ModelFile.setter
    def ModelFile(self, ModelFile):
        self._ModelFile = ModelFile

    @property
    def RawData(self):
        return self._RawData

    @RawData.setter
    def RawData(self, RawData):
        self._RawData = RawData


    def _deserialize(self, params):
        self._Revision = params.get("Revision")
        self._UpdateTime = params.get("UpdateTime")
        self._Image = params.get("Image")
        self._ModelFile = params.get("ModelFile")
        self._RawData = params.get("RawData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    """推理服务在集群中的信息

    """

    def __init__(self):
        r"""
        :param _Replicas: 期望运行的Pod数量，停止状态是0
不同计费模式和调节模式下对应关系如下
PREPAID 和 POSTPAID_BY_HOUR:
手动调节模式下对应 实例数量
自动调节模式下对应 基于时间的默认策略的实例数量
HYBRID_PAID:
后付费实例手动调节模式下对应 实例数量
后付费实例自动调节模式下对应 时间策略的默认策略的实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _ImageInfo: 镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _Env: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: list of EnvVar
        :param _Resources: 资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _InstanceType: 后付费实例对应的机型规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _ModelInfo: 模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _LogEnable: 是否启用日志
注意：此字段可能返回 null，表示取不到有效值。
        :type LogEnable: bool
        :param _LogConfig: 日志配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _AuthorizationEnable: 是否开启鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationEnable: bool
        :param _HorizontalPodAutoscaler: hpa配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        :param _Status: 服务的状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.tione.v20211111.models.WorkloadStatus`
        :param _Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _PodList: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: list of str
        :param _ResourceTotal: 资源总量
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTotal: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _OldReplicas: 历史实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type OldReplicas: int
        :param _HybridBillingPrepaidReplicas: 计费模式[HYBRID_PAID]时生效, 用于标识混合计费模式下的预付费实例数, 若不填则默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type HybridBillingPrepaidReplicas: int
        :param _OldHybridBillingPrepaidReplicas: 历史 HYBRID_PAID 时的实例数，用户恢复服务
注意：此字段可能返回 null，表示取不到有效值。
        :type OldHybridBillingPrepaidReplicas: int
        :param _ModelHotUpdateEnable: 是否开启模型的热更新。默认不开启
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelHotUpdateEnable: bool
        :param _ScaleMode: 实例数量调节方式,默认为手动
支持：自动 - "AUTO", 手动 - "MANUAL"
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleMode: str
        :param _CronScaleJobs: 定时伸缩任务
注意：此字段可能返回 null，表示取不到有效值。
        :type CronScaleJobs: list of CronScaleJob
        :param _ScaleStrategy: 定时伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleStrategy: str
        :param _ScheduledAction: 定时停止的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledAction: str
        :param _Pods: Pod列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Pods: :class:`tencentcloud.tione.v20211111.models.Pod`
        :param _PodInfos: Pod列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodInfos: list of Pod
        :param _ServiceLimit: 服务限速限流相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param _ModelTurboEnable: 是否开启模型的加速, 仅对StableDiffusion(动态加速)格式的模型有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelTurboEnable: bool
        :param _VolumeMount: 挂载
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        :param _InferCodeInfo: 推理代码信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InferCodeInfo: :class:`tencentcloud.tione.v20211111.models.InferCodeInfo`
        :param _Command: 服务的启动命令
注意：此字段可能返回 null，表示取不到有效值。
        :type Command: str
        :param _ServiceEIP: 开启TIONE内网访问外部设置
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceEIP: :class:`tencentcloud.tione.v20211111.models.ServiceEIP`
        """
        self._Replicas = None
        self._ImageInfo = None
        self._Env = None
        self._Resources = None
        self._InstanceType = None
        self._ModelInfo = None
        self._LogEnable = None
        self._LogConfig = None
        self._AuthorizationEnable = None
        self._HorizontalPodAutoscaler = None
        self._Status = None
        self._Weight = None
        self._PodList = None
        self._ResourceTotal = None
        self._OldReplicas = None
        self._HybridBillingPrepaidReplicas = None
        self._OldHybridBillingPrepaidReplicas = None
        self._ModelHotUpdateEnable = None
        self._ScaleMode = None
        self._CronScaleJobs = None
        self._ScaleStrategy = None
        self._ScheduledAction = None
        self._Pods = None
        self._PodInfos = None
        self._ServiceLimit = None
        self._ModelTurboEnable = None
        self._VolumeMount = None
        self._InferCodeInfo = None
        self._Command = None
        self._ServiceEIP = None

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def Env(self):
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ModelInfo(self):
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def AuthorizationEnable(self):
        return self._AuthorizationEnable

    @AuthorizationEnable.setter
    def AuthorizationEnable(self, AuthorizationEnable):
        self._AuthorizationEnable = AuthorizationEnable

    @property
    def HorizontalPodAutoscaler(self):
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PodList(self):
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList

    @property
    def ResourceTotal(self):
        return self._ResourceTotal

    @ResourceTotal.setter
    def ResourceTotal(self, ResourceTotal):
        self._ResourceTotal = ResourceTotal

    @property
    def OldReplicas(self):
        return self._OldReplicas

    @OldReplicas.setter
    def OldReplicas(self, OldReplicas):
        self._OldReplicas = OldReplicas

    @property
    def HybridBillingPrepaidReplicas(self):
        return self._HybridBillingPrepaidReplicas

    @HybridBillingPrepaidReplicas.setter
    def HybridBillingPrepaidReplicas(self, HybridBillingPrepaidReplicas):
        self._HybridBillingPrepaidReplicas = HybridBillingPrepaidReplicas

    @property
    def OldHybridBillingPrepaidReplicas(self):
        return self._OldHybridBillingPrepaidReplicas

    @OldHybridBillingPrepaidReplicas.setter
    def OldHybridBillingPrepaidReplicas(self, OldHybridBillingPrepaidReplicas):
        self._OldHybridBillingPrepaidReplicas = OldHybridBillingPrepaidReplicas

    @property
    def ModelHotUpdateEnable(self):
        return self._ModelHotUpdateEnable

    @ModelHotUpdateEnable.setter
    def ModelHotUpdateEnable(self, ModelHotUpdateEnable):
        self._ModelHotUpdateEnable = ModelHotUpdateEnable

    @property
    def ScaleMode(self):
        return self._ScaleMode

    @ScaleMode.setter
    def ScaleMode(self, ScaleMode):
        self._ScaleMode = ScaleMode

    @property
    def CronScaleJobs(self):
        return self._CronScaleJobs

    @CronScaleJobs.setter
    def CronScaleJobs(self, CronScaleJobs):
        self._CronScaleJobs = CronScaleJobs

    @property
    def ScaleStrategy(self):
        return self._ScaleStrategy

    @ScaleStrategy.setter
    def ScaleStrategy(self, ScaleStrategy):
        self._ScaleStrategy = ScaleStrategy

    @property
    def ScheduledAction(self):
        return self._ScheduledAction

    @ScheduledAction.setter
    def ScheduledAction(self, ScheduledAction):
        self._ScheduledAction = ScheduledAction

    @property
    def Pods(self):
        return self._Pods

    @Pods.setter
    def Pods(self, Pods):
        self._Pods = Pods

    @property
    def PodInfos(self):
        return self._PodInfos

    @PodInfos.setter
    def PodInfos(self, PodInfos):
        self._PodInfos = PodInfos

    @property
    def ServiceLimit(self):
        return self._ServiceLimit

    @ServiceLimit.setter
    def ServiceLimit(self, ServiceLimit):
        self._ServiceLimit = ServiceLimit

    @property
    def ModelTurboEnable(self):
        return self._ModelTurboEnable

    @ModelTurboEnable.setter
    def ModelTurboEnable(self, ModelTurboEnable):
        self._ModelTurboEnable = ModelTurboEnable

    @property
    def VolumeMount(self):
        return self._VolumeMount

    @VolumeMount.setter
    def VolumeMount(self, VolumeMount):
        self._VolumeMount = VolumeMount

    @property
    def InferCodeInfo(self):
        return self._InferCodeInfo

    @InferCodeInfo.setter
    def InferCodeInfo(self, InferCodeInfo):
        self._InferCodeInfo = InferCodeInfo

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ServiceEIP(self):
        return self._ServiceEIP

    @ServiceEIP.setter
    def ServiceEIP(self, ServiceEIP):
        self._ServiceEIP = ServiceEIP


    def _deserialize(self, params):
        self._Replicas = params.get("Replicas")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("Env") is not None:
            self._Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self._Env.append(obj)
        if params.get("Resources") is not None:
            self._Resources = ResourceInfo()
            self._Resources._deserialize(params.get("Resources"))
        self._InstanceType = params.get("InstanceType")
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        self._LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._AuthorizationEnable = params.get("AuthorizationEnable")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("Status") is not None:
            self._Status = WorkloadStatus()
            self._Status._deserialize(params.get("Status"))
        self._Weight = params.get("Weight")
        self._PodList = params.get("PodList")
        if params.get("ResourceTotal") is not None:
            self._ResourceTotal = ResourceInfo()
            self._ResourceTotal._deserialize(params.get("ResourceTotal"))
        self._OldReplicas = params.get("OldReplicas")
        self._HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
        self._OldHybridBillingPrepaidReplicas = params.get("OldHybridBillingPrepaidReplicas")
        self._ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
        self._ScaleMode = params.get("ScaleMode")
        if params.get("CronScaleJobs") is not None:
            self._CronScaleJobs = []
            for item in params.get("CronScaleJobs"):
                obj = CronScaleJob()
                obj._deserialize(item)
                self._CronScaleJobs.append(obj)
        self._ScaleStrategy = params.get("ScaleStrategy")
        self._ScheduledAction = params.get("ScheduledAction")
        if params.get("Pods") is not None:
            self._Pods = Pod()
            self._Pods._deserialize(params.get("Pods"))
        if params.get("PodInfos") is not None:
            self._PodInfos = []
            for item in params.get("PodInfos"):
                obj = Pod()
                obj._deserialize(item)
                self._PodInfos.append(obj)
        if params.get("ServiceLimit") is not None:
            self._ServiceLimit = ServiceLimit()
            self._ServiceLimit._deserialize(params.get("ServiceLimit"))
        self._ModelTurboEnable = params.get("ModelTurboEnable")
        if params.get("VolumeMount") is not None:
            self._VolumeMount = VolumeMount()
            self._VolumeMount._deserialize(params.get("VolumeMount"))
        if params.get("InferCodeInfo") is not None:
            self._InferCodeInfo = InferCodeInfo()
            self._InferCodeInfo._deserialize(params.get("InferCodeInfo"))
        self._Command = params.get("Command")
        if params.get("ServiceEIP") is not None:
            self._ServiceEIP = ServiceEIP()
            self._ServiceEIP._deserialize(params.get("ServiceEIP"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceLimit(AbstractModel):
    """服务的限流限速等配置

    """

    def __init__(self):
        r"""
        :param _EnableInstanceRpsLimit: 是否开启实例层面限流限速，true or false。true 则 InstanceRpsLimit 必填， false 则 InstanceRpsLimit 不生效
        :type EnableInstanceRpsLimit: bool
        :param _InstanceRpsLimit: 每个服务实例的 request per second 限速, 0 为不限流
        :type InstanceRpsLimit: int
        """
        self._EnableInstanceRpsLimit = None
        self._InstanceRpsLimit = None

    @property
    def EnableInstanceRpsLimit(self):
        return self._EnableInstanceRpsLimit

    @EnableInstanceRpsLimit.setter
    def EnableInstanceRpsLimit(self, EnableInstanceRpsLimit):
        self._EnableInstanceRpsLimit = EnableInstanceRpsLimit

    @property
    def InstanceRpsLimit(self):
        return self._InstanceRpsLimit

    @InstanceRpsLimit.setter
    def InstanceRpsLimit(self, InstanceRpsLimit):
        self._InstanceRpsLimit = InstanceRpsLimit


    def _deserialize(self, params):
        self._EnableInstanceRpsLimit = params.get("EnableInstanceRpsLimit")
        self._InstanceRpsLimit = params.get("InstanceRpsLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Spec(AbstractModel):
    """计费项内容

    """

    def __init__(self):
        r"""
        :param _SpecId: 计费项标签
        :type SpecId: str
        :param _SpecName: 计费项名称
        :type SpecName: str
        :param _SpecAlias: 计费项显示名称
        :type SpecAlias: str
        :param _Available: 是否售罄
        :type Available: bool
        :param _AvailableRegion: 当前资源售罄时，可用的区域有哪些
        :type AvailableRegion: list of str
        :param _SpecFeatures: 当前计费项支持的特性
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecFeatures: list of str
        :param _SpecType: 计费项类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecType: str
        :param _GpuType: GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param _CategoryId: 计费项CategoryId
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryId: str
        """
        self._SpecId = None
        self._SpecName = None
        self._SpecAlias = None
        self._Available = None
        self._AvailableRegion = None
        self._SpecFeatures = None
        self._SpecType = None
        self._GpuType = None
        self._CategoryId = None

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def SpecAlias(self):
        return self._SpecAlias

    @SpecAlias.setter
    def SpecAlias(self, SpecAlias):
        self._SpecAlias = SpecAlias

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def AvailableRegion(self):
        return self._AvailableRegion

    @AvailableRegion.setter
    def AvailableRegion(self, AvailableRegion):
        self._AvailableRegion = AvailableRegion

    @property
    def SpecFeatures(self):
        return self._SpecFeatures

    @SpecFeatures.setter
    def SpecFeatures(self, SpecFeatures):
        self._SpecFeatures = SpecFeatures

    @property
    def SpecType(self):
        return self._SpecType

    @SpecType.setter
    def SpecType(self, SpecType):
        self._SpecType = SpecType

    @property
    def GpuType(self):
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def CategoryId(self):
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId


    def _deserialize(self, params):
        self._SpecId = params.get("SpecId")
        self._SpecName = params.get("SpecName")
        self._SpecAlias = params.get("SpecAlias")
        self._Available = params.get("Available")
        self._AvailableRegion = params.get("AvailableRegion")
        self._SpecFeatures = params.get("SpecFeatures")
        self._SpecType = params.get("SpecType")
        self._GpuType = params.get("GpuType")
        self._CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecPrice(AbstractModel):
    """计费项询价结果

    """

    def __init__(self):
        r"""
        :param _SpecName: 计费项名称
        :type SpecName: str
        :param _TotalCost: 原价，单位：分。最大值42亿，超过则返回0
        :type TotalCost: int
        :param _RealTotalCost: 优惠后的价格，单位：分
        :type RealTotalCost: int
        :param _SpecCount: 计费项数量
        :type SpecCount: int
        """
        self._SpecName = None
        self._TotalCost = None
        self._RealTotalCost = None
        self._SpecCount = None

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RealTotalCost(self):
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

    @property
    def SpecCount(self):
        return self._SpecCount

    @SpecCount.setter
    def SpecCount(self, SpecCount):
        self._SpecCount = SpecCount


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._TotalCost = params.get("TotalCost")
        self._RealTotalCost = params.get("RealTotalCost")
        self._SpecCount = params.get("SpecCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecUnit(AbstractModel):
    """计费项询价单元

    """

    def __init__(self):
        r"""
        :param _SpecName: 计费项名称
        :type SpecName: str
        :param _SpecCount: 计费项数量,建议不超过100万
        :type SpecCount: int
        """
        self._SpecName = None
        self._SpecCount = None

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def SpecCount(self):
        return self._SpecCount

    @SpecCount.setter
    def SpecCount(self, SpecCount):
        self._SpecCount = SpecCount


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._SpecCount = params.get("SpecCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCmdInfo(AbstractModel):
    """启动命令信息

    """

    def __init__(self):
        r"""
        :param _StartCmd: 启动命令
        :type StartCmd: str
        :param _PsStartCmd: ps启动命令
        :type PsStartCmd: str
        :param _WorkerStartCmd: worker启动命令
        :type WorkerStartCmd: str
        """
        self._StartCmd = None
        self._PsStartCmd = None
        self._WorkerStartCmd = None

    @property
    def StartCmd(self):
        return self._StartCmd

    @StartCmd.setter
    def StartCmd(self, StartCmd):
        self._StartCmd = StartCmd

    @property
    def PsStartCmd(self):
        return self._PsStartCmd

    @PsStartCmd.setter
    def PsStartCmd(self, PsStartCmd):
        self._PsStartCmd = PsStartCmd

    @property
    def WorkerStartCmd(self):
        return self._WorkerStartCmd

    @WorkerStartCmd.setter
    def WorkerStartCmd(self, WorkerStartCmd):
        self._WorkerStartCmd = WorkerStartCmd


    def _deserialize(self, params):
        self._StartCmd = params.get("StartCmd")
        self._PsStartCmd = params.get("PsStartCmd")
        self._WorkerStartCmd = params.get("WorkerStartCmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartNotebookRequest(AbstractModel):
    """StartNotebook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: notebook id
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartNotebookResponse(AbstractModel):
    """StartNotebook返回参数结构体

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


class StartTrainingTaskRequest(AbstractModel):
    """StartTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartTrainingTaskResponse(AbstractModel):
    """StartTrainingTask返回参数结构体

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


class StatefulSetCondition(AbstractModel):
    """实例状况

    """

    def __init__(self):
        r"""
        :param _Message: 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _Status: Status of the condition, one of True, False, Unknown.
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _LastTransitionTime: 上次更新的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTransitionTime: str
        :param _LastUpdateTime: 上次更新的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        """
        self._Message = None
        self._Reason = None
        self._Status = None
        self._Type = None
        self._LastTransitionTime = None
        self._LastUpdateTime = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LastTransitionTime(self):
        return self._LastTransitionTime

    @LastTransitionTime.setter
    def LastTransitionTime(self, LastTransitionTime):
        self._LastTransitionTime = LastTransitionTime

    @property
    def LastUpdateTime(self):
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Reason = params.get("Reason")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._LastTransitionTime = params.get("LastTransitionTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopBatchTaskRequest(AbstractModel):
    """StopBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        """
        self._BatchTaskId = None

    @property
    def BatchTaskId(self):
        return self._BatchTaskId

    @BatchTaskId.setter
    def BatchTaskId(self, BatchTaskId):
        self._BatchTaskId = BatchTaskId


    def _deserialize(self, params):
        self._BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopBatchTaskResponse(AbstractModel):
    """StopBatchTask返回参数结构体

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


class StopCreatingImageRequest(AbstractModel):
    """StopCreatingImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 镜像保存记录ID
        :type RecordId: str
        """
        self._RecordId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCreatingImageResponse(AbstractModel):
    """StopCreatingImage返回参数结构体

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


class StopModelAccelerateTaskRequest(AbstractModel):
    """StopModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        """
        self._ModelAccTaskId = None

    @property
    def ModelAccTaskId(self):
        return self._ModelAccTaskId

    @ModelAccTaskId.setter
    def ModelAccTaskId(self, ModelAccTaskId):
        self._ModelAccTaskId = ModelAccTaskId


    def _deserialize(self, params):
        self._ModelAccTaskId = params.get("ModelAccTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopModelAccelerateTaskResponse(AbstractModel):
    """StopModelAccelerateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelAccTaskId: 模型加速任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskId: str
        :param _AsyncTaskId: 异步任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelAccTaskId = None
        self._AsyncTaskId = None
        self._RequestId = None

    @property
    def ModelAccTaskId(self):
        return self._ModelAccTaskId

    @ModelAccTaskId.setter
    def ModelAccTaskId(self, ModelAccTaskId):
        self._ModelAccTaskId = ModelAccTaskId

    @property
    def AsyncTaskId(self):
        return self._AsyncTaskId

    @AsyncTaskId.setter
    def AsyncTaskId(self, AsyncTaskId):
        self._AsyncTaskId = AsyncTaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModelAccTaskId = params.get("ModelAccTaskId")
        self._AsyncTaskId = params.get("AsyncTaskId")
        self._RequestId = params.get("RequestId")


class StopNotebookRequest(AbstractModel):
    """StopNotebook请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: notebook id
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopNotebookResponse(AbstractModel):
    """StopNotebook返回参数结构体

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


class StopTrainingTaskRequest(AbstractModel):
    """StopTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopTrainingTaskResponse(AbstractModel):
    """StopTrainingTask返回参数结构体

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


class TJCallInfo(AbstractModel):
    """太极服务的调用信息

    """

    def __init__(self):
        r"""
        :param _HttpAddr: 调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpAddr: str
        :param _Token: token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _CallExample: 调用示例
注意：此字段可能返回 null，表示取不到有效值。
        :type CallExample: str
        """
        self._HttpAddr = None
        self._Token = None
        self._CallExample = None

    @property
    def HttpAddr(self):
        return self._HttpAddr

    @HttpAddr.setter
    def HttpAddr(self, HttpAddr):
        self._HttpAddr = HttpAddr

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def CallExample(self):
        return self._CallExample

    @CallExample.setter
    def CallExample(self, CallExample):
        self._CallExample = CallExample


    def _deserialize(self, params):
        self._HttpAddr = params.get("HttpAddr")
        self._Token = params.get("Token")
        self._CallExample = params.get("CallExample")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """描述腾讯云标签

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
        


class TagFilter(AbstractModel):
    """Tag过滤参数

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValues: 多个标签值
        :type TagValues: list of str
        """
        self._TagKey = None
        self._TagValues = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoFifthClass(AbstractModel):
    """五级标签

    """

    def __init__(self):
        r"""
        :param _LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param _LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        """
        self._LabelValue = None
        self._LabelCount = None
        self._LabelPercentage = None

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def LabelCount(self):
        return self._LabelCount

    @LabelCount.setter
    def LabelCount(self, LabelCount):
        self._LabelCount = LabelCount

    @property
    def LabelPercentage(self):
        return self._LabelPercentage

    @LabelPercentage.setter
    def LabelPercentage(self, LabelPercentage):
        self._LabelPercentage = LabelPercentage


    def _deserialize(self, params):
        self._LabelValue = params.get("LabelValue")
        self._LabelCount = params.get("LabelCount")
        self._LabelPercentage = params.get("LabelPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoFirstClass(AbstractModel):
    """一级标签

    """

    def __init__(self):
        r"""
        :param _LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param _LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param _ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoSecondClass
        """
        self._LabelValue = None
        self._LabelCount = None
        self._LabelPercentage = None
        self._ChildLabelList = None

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def LabelCount(self):
        return self._LabelCount

    @LabelCount.setter
    def LabelCount(self, LabelCount):
        self._LabelCount = LabelCount

    @property
    def LabelPercentage(self):
        return self._LabelPercentage

    @LabelPercentage.setter
    def LabelPercentage(self, LabelPercentage):
        self._LabelPercentage = LabelPercentage

    @property
    def ChildLabelList(self):
        return self._ChildLabelList

    @ChildLabelList.setter
    def ChildLabelList(self, ChildLabelList):
        self._ChildLabelList = ChildLabelList


    def _deserialize(self, params):
        self._LabelValue = params.get("LabelValue")
        self._LabelCount = params.get("LabelCount")
        self._LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self._ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoSecondClass()
                obj._deserialize(item)
                self._ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoFourthClass(AbstractModel):
    """四级标签

    """

    def __init__(self):
        r"""
        :param _LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param _LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param _ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoFifthClass
        """
        self._LabelValue = None
        self._LabelCount = None
        self._LabelPercentage = None
        self._ChildLabelList = None

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def LabelCount(self):
        return self._LabelCount

    @LabelCount.setter
    def LabelCount(self, LabelCount):
        self._LabelCount = LabelCount

    @property
    def LabelPercentage(self):
        return self._LabelPercentage

    @LabelPercentage.setter
    def LabelPercentage(self, LabelPercentage):
        self._LabelPercentage = LabelPercentage

    @property
    def ChildLabelList(self):
        return self._ChildLabelList

    @ChildLabelList.setter
    def ChildLabelList(self, ChildLabelList):
        self._ChildLabelList = ChildLabelList


    def _deserialize(self, params):
        self._LabelValue = params.get("LabelValue")
        self._LabelCount = params.get("LabelCount")
        self._LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self._ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoFifthClass()
                obj._deserialize(item)
                self._ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoSecondClass(AbstractModel):
    """二级标签

    """

    def __init__(self):
        r"""
        :param _LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param _LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param _ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoThirdClass
        """
        self._LabelValue = None
        self._LabelCount = None
        self._LabelPercentage = None
        self._ChildLabelList = None

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def LabelCount(self):
        return self._LabelCount

    @LabelCount.setter
    def LabelCount(self, LabelCount):
        self._LabelCount = LabelCount

    @property
    def LabelPercentage(self):
        return self._LabelPercentage

    @LabelPercentage.setter
    def LabelPercentage(self, LabelPercentage):
        self._LabelPercentage = LabelPercentage

    @property
    def ChildLabelList(self):
        return self._ChildLabelList

    @ChildLabelList.setter
    def ChildLabelList(self, ChildLabelList):
        self._ChildLabelList = ChildLabelList


    def _deserialize(self, params):
        self._LabelValue = params.get("LabelValue")
        self._LabelCount = params.get("LabelCount")
        self._LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self._ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoThirdClass()
                obj._deserialize(item)
                self._ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoThirdClass(AbstractModel):
    """三级标签

    """

    def __init__(self):
        r"""
        :param _LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param _LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param _LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param _ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoFourthClass
        """
        self._LabelValue = None
        self._LabelCount = None
        self._LabelPercentage = None
        self._ChildLabelList = None

    @property
    def LabelValue(self):
        return self._LabelValue

    @LabelValue.setter
    def LabelValue(self, LabelValue):
        self._LabelValue = LabelValue

    @property
    def LabelCount(self):
        return self._LabelCount

    @LabelCount.setter
    def LabelCount(self, LabelCount):
        self._LabelCount = LabelCount

    @property
    def LabelPercentage(self):
        return self._LabelPercentage

    @LabelPercentage.setter
    def LabelPercentage(self, LabelPercentage):
        self._LabelPercentage = LabelPercentage

    @property
    def ChildLabelList(self):
        return self._ChildLabelList

    @ChildLabelList.setter
    def ChildLabelList(self, ChildLabelList):
        self._ChildLabelList = ChildLabelList


    def _deserialize(self, params):
        self._LabelValue = params.get("LabelValue")
        self._LabelCount = params.get("LabelCount")
        self._LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self._ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoFourthClass()
                obj._deserialize(item)
                self._ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionInfo(AbstractModel):
    """文本标签

    """

    def __init__(self):
        r"""
        :param _Theme: 文本分类题目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Theme: str
        :param _ClassLabelList: 一级标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassLabelList: list of TextLabelDistributionDetailInfoFirstClass
        """
        self._Theme = None
        self._ClassLabelList = None

    @property
    def Theme(self):
        return self._Theme

    @Theme.setter
    def Theme(self, Theme):
        self._Theme = Theme

    @property
    def ClassLabelList(self):
        return self._ClassLabelList

    @ClassLabelList.setter
    def ClassLabelList(self, ClassLabelList):
        self._ClassLabelList = ClassLabelList


    def _deserialize(self, params):
        self._Theme = params.get("Theme")
        if params.get("ClassLabelList") is not None:
            self._ClassLabelList = []
            for item in params.get("ClassLabelList"):
                obj = TextLabelDistributionDetailInfoFirstClass()
                obj._deserialize(item)
                self._ClassLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingDataPoint(AbstractModel):
    """训练数据

    """


class TrainingMetric(AbstractModel):
    """训练指标

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名
        :type MetricName: str
        :param _Values: 数据值
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of TrainingDataPoint
        :param _Epochs: 上报的Epoch. 可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Epochs: list of TrainingDataPoint
        :param _Steps: 上报的Step. 可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Steps: list of TrainingDataPoint
        :param _TotalSteps: 上报的TotalSteps. 可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSteps: list of TrainingDataPoint
        """
        self._MetricName = None
        self._Values = None
        self._Epochs = None
        self._Steps = None
        self._TotalSteps = None

    @property
    def MetricName(self):
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Epochs(self):
        return self._Epochs

    @Epochs.setter
    def Epochs(self, Epochs):
        self._Epochs = Epochs

    @property
    def Steps(self):
        return self._Steps

    @Steps.setter
    def Steps(self, Steps):
        self._Steps = Steps

    @property
    def TotalSteps(self):
        return self._TotalSteps

    @TotalSteps.setter
    def TotalSteps(self, TotalSteps):
        self._TotalSteps = TotalSteps


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self._Values.append(obj)
        if params.get("Epochs") is not None:
            self._Epochs = []
            for item in params.get("Epochs"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self._Epochs.append(obj)
        if params.get("Steps") is not None:
            self._Steps = []
            for item in params.get("Steps"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self._Steps.append(obj)
        if params.get("TotalSteps") is not None:
            self._TotalSteps = []
            for item in params.get("TotalSteps"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self._TotalSteps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingModelDTO(AbstractModel):
    """模型列表

    """

    def __init__(self):
        r"""
        :param _TrainingModelId: 模型id
        :type TrainingModelId: str
        :param _TrainingModelName: 模型名称
        :type TrainingModelName: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _CreateTime: 模型创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _TrainingModelVersions: 模型版本列表。默认不返回，仅在指定请求参数开启时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelVersions: list of TrainingModelVersionDTO
        """
        self._TrainingModelId = None
        self._TrainingModelName = None
        self._Tags = None
        self._CreateTime = None
        self._TrainingModelVersions = None

    @property
    def TrainingModelId(self):
        return self._TrainingModelId

    @TrainingModelId.setter
    def TrainingModelId(self, TrainingModelId):
        self._TrainingModelId = TrainingModelId

    @property
    def TrainingModelName(self):
        return self._TrainingModelName

    @TrainingModelName.setter
    def TrainingModelName(self, TrainingModelName):
        self._TrainingModelName = TrainingModelName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TrainingModelVersions(self):
        return self._TrainingModelVersions

    @TrainingModelVersions.setter
    def TrainingModelVersions(self, TrainingModelVersions):
        self._TrainingModelVersions = TrainingModelVersions


    def _deserialize(self, params):
        self._TrainingModelId = params.get("TrainingModelId")
        self._TrainingModelName = params.get("TrainingModelName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateTime = params.get("CreateTime")
        if params.get("TrainingModelVersions") is not None:
            self._TrainingModelVersions = []
            for item in params.get("TrainingModelVersions"):
                obj = TrainingModelVersionDTO()
                obj._deserialize(item)
                self._TrainingModelVersions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingModelVersionDTO(AbstractModel):
    """模型版本列表

    """

    def __init__(self):
        r"""
        :param _TrainingModelId: 模型id
        :type TrainingModelId: str
        :param _TrainingModelVersionId: 模型版本id
        :type TrainingModelVersionId: str
        :param _TrainingModelVersion: 模型版本
        :type TrainingModelVersion: str
        :param _TrainingModelSource: 模型来源
        :type TrainingModelSource: str
        :param _TrainingModelCreateTime: 创建时间
        :type TrainingModelCreateTime: str
        :param _TrainingModelCreator: 创建人uin
        :type TrainingModelCreator: str
        :param _AlgorithmFramework: 算法框架
        :type AlgorithmFramework: str
        :param _ReasoningEnvironment: 推理环境
        :type ReasoningEnvironment: str
        :param _ReasoningEnvironmentSource: 推理环境来源
        :type ReasoningEnvironmentSource: str
        :param _TrainingModelIndex: 模型指标
        :type TrainingModelIndex: str
        :param _TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param _TrainingModelCosPath: 模型cos路径
        :type TrainingModelCosPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _TrainingModelName: 模型名称
        :type TrainingModelName: str
        :param _TrainingJobId: 训练任务id
        :type TrainingJobId: str
        :param _ReasoningImageInfo: 自定义推理环境
        :type ReasoningImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _CreateTime: 模型版本创建时间
        :type CreateTime: str
        :param _TrainingModelStatus: 模型处理状态
STATUS_SUCCESS：导入成功，STATUS_FAILED：导入失败 ，STATUS_RUNNING：导入中
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelStatus: str
        :param _TrainingModelProgress: 模型处理进度
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelProgress: int
        :param _TrainingModelErrorMsg: 模型错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelErrorMsg: str
        :param _TrainingModelFormat: 模型格式
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelFormat: str
        :param _VersionType: 模型版本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionType: str
        :param _GPUType: GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUType: str
        :param _AutoClean: 模型自动清理开关
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoClean: str
        :param _ModelCleanPeriod: 模型清理周期
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelCleanPeriod: int
        :param _MaxReservedModels: 模型数量保留上限
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReservedModels: int
        :param _ModelHotUpdatePath: 模型热更新目录
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelHotUpdatePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _ReasoningEnvironmentId: 推理环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type ReasoningEnvironmentId: str
        :param _TrainingJobVersion: 训练任务版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobVersion: str
        :param _TrainingPreference: 训练偏好
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingPreference: str
        :param _AutoMLTaskId: 自动学习任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoMLTaskId: str
        :param _IsQAT: 是否QAT模型
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQAT: bool
        """
        self._TrainingModelId = None
        self._TrainingModelVersionId = None
        self._TrainingModelVersion = None
        self._TrainingModelSource = None
        self._TrainingModelCreateTime = None
        self._TrainingModelCreator = None
        self._AlgorithmFramework = None
        self._ReasoningEnvironment = None
        self._ReasoningEnvironmentSource = None
        self._TrainingModelIndex = None
        self._TrainingJobName = None
        self._TrainingModelCosPath = None
        self._TrainingModelName = None
        self._TrainingJobId = None
        self._ReasoningImageInfo = None
        self._CreateTime = None
        self._TrainingModelStatus = None
        self._TrainingModelProgress = None
        self._TrainingModelErrorMsg = None
        self._TrainingModelFormat = None
        self._VersionType = None
        self._GPUType = None
        self._AutoClean = None
        self._ModelCleanPeriod = None
        self._MaxReservedModels = None
        self._ModelHotUpdatePath = None
        self._ReasoningEnvironmentId = None
        self._TrainingJobVersion = None
        self._TrainingPreference = None
        self._AutoMLTaskId = None
        self._IsQAT = None

    @property
    def TrainingModelId(self):
        return self._TrainingModelId

    @TrainingModelId.setter
    def TrainingModelId(self, TrainingModelId):
        self._TrainingModelId = TrainingModelId

    @property
    def TrainingModelVersionId(self):
        return self._TrainingModelVersionId

    @TrainingModelVersionId.setter
    def TrainingModelVersionId(self, TrainingModelVersionId):
        self._TrainingModelVersionId = TrainingModelVersionId

    @property
    def TrainingModelVersion(self):
        return self._TrainingModelVersion

    @TrainingModelVersion.setter
    def TrainingModelVersion(self, TrainingModelVersion):
        self._TrainingModelVersion = TrainingModelVersion

    @property
    def TrainingModelSource(self):
        return self._TrainingModelSource

    @TrainingModelSource.setter
    def TrainingModelSource(self, TrainingModelSource):
        self._TrainingModelSource = TrainingModelSource

    @property
    def TrainingModelCreateTime(self):
        return self._TrainingModelCreateTime

    @TrainingModelCreateTime.setter
    def TrainingModelCreateTime(self, TrainingModelCreateTime):
        self._TrainingModelCreateTime = TrainingModelCreateTime

    @property
    def TrainingModelCreator(self):
        return self._TrainingModelCreator

    @TrainingModelCreator.setter
    def TrainingModelCreator(self, TrainingModelCreator):
        self._TrainingModelCreator = TrainingModelCreator

    @property
    def AlgorithmFramework(self):
        return self._AlgorithmFramework

    @AlgorithmFramework.setter
    def AlgorithmFramework(self, AlgorithmFramework):
        self._AlgorithmFramework = AlgorithmFramework

    @property
    def ReasoningEnvironment(self):
        return self._ReasoningEnvironment

    @ReasoningEnvironment.setter
    def ReasoningEnvironment(self, ReasoningEnvironment):
        self._ReasoningEnvironment = ReasoningEnvironment

    @property
    def ReasoningEnvironmentSource(self):
        return self._ReasoningEnvironmentSource

    @ReasoningEnvironmentSource.setter
    def ReasoningEnvironmentSource(self, ReasoningEnvironmentSource):
        self._ReasoningEnvironmentSource = ReasoningEnvironmentSource

    @property
    def TrainingModelIndex(self):
        return self._TrainingModelIndex

    @TrainingModelIndex.setter
    def TrainingModelIndex(self, TrainingModelIndex):
        self._TrainingModelIndex = TrainingModelIndex

    @property
    def TrainingJobName(self):
        return self._TrainingJobName

    @TrainingJobName.setter
    def TrainingJobName(self, TrainingJobName):
        self._TrainingJobName = TrainingJobName

    @property
    def TrainingModelCosPath(self):
        return self._TrainingModelCosPath

    @TrainingModelCosPath.setter
    def TrainingModelCosPath(self, TrainingModelCosPath):
        self._TrainingModelCosPath = TrainingModelCosPath

    @property
    def TrainingModelName(self):
        return self._TrainingModelName

    @TrainingModelName.setter
    def TrainingModelName(self, TrainingModelName):
        self._TrainingModelName = TrainingModelName

    @property
    def TrainingJobId(self):
        return self._TrainingJobId

    @TrainingJobId.setter
    def TrainingJobId(self, TrainingJobId):
        self._TrainingJobId = TrainingJobId

    @property
    def ReasoningImageInfo(self):
        return self._ReasoningImageInfo

    @ReasoningImageInfo.setter
    def ReasoningImageInfo(self, ReasoningImageInfo):
        self._ReasoningImageInfo = ReasoningImageInfo

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TrainingModelStatus(self):
        return self._TrainingModelStatus

    @TrainingModelStatus.setter
    def TrainingModelStatus(self, TrainingModelStatus):
        self._TrainingModelStatus = TrainingModelStatus

    @property
    def TrainingModelProgress(self):
        return self._TrainingModelProgress

    @TrainingModelProgress.setter
    def TrainingModelProgress(self, TrainingModelProgress):
        self._TrainingModelProgress = TrainingModelProgress

    @property
    def TrainingModelErrorMsg(self):
        return self._TrainingModelErrorMsg

    @TrainingModelErrorMsg.setter
    def TrainingModelErrorMsg(self, TrainingModelErrorMsg):
        self._TrainingModelErrorMsg = TrainingModelErrorMsg

    @property
    def TrainingModelFormat(self):
        return self._TrainingModelFormat

    @TrainingModelFormat.setter
    def TrainingModelFormat(self, TrainingModelFormat):
        self._TrainingModelFormat = TrainingModelFormat

    @property
    def VersionType(self):
        return self._VersionType

    @VersionType.setter
    def VersionType(self, VersionType):
        self._VersionType = VersionType

    @property
    def GPUType(self):
        return self._GPUType

    @GPUType.setter
    def GPUType(self, GPUType):
        self._GPUType = GPUType

    @property
    def AutoClean(self):
        return self._AutoClean

    @AutoClean.setter
    def AutoClean(self, AutoClean):
        self._AutoClean = AutoClean

    @property
    def ModelCleanPeriod(self):
        return self._ModelCleanPeriod

    @ModelCleanPeriod.setter
    def ModelCleanPeriod(self, ModelCleanPeriod):
        self._ModelCleanPeriod = ModelCleanPeriod

    @property
    def MaxReservedModels(self):
        return self._MaxReservedModels

    @MaxReservedModels.setter
    def MaxReservedModels(self, MaxReservedModels):
        self._MaxReservedModels = MaxReservedModels

    @property
    def ModelHotUpdatePath(self):
        return self._ModelHotUpdatePath

    @ModelHotUpdatePath.setter
    def ModelHotUpdatePath(self, ModelHotUpdatePath):
        self._ModelHotUpdatePath = ModelHotUpdatePath

    @property
    def ReasoningEnvironmentId(self):
        return self._ReasoningEnvironmentId

    @ReasoningEnvironmentId.setter
    def ReasoningEnvironmentId(self, ReasoningEnvironmentId):
        self._ReasoningEnvironmentId = ReasoningEnvironmentId

    @property
    def TrainingJobVersion(self):
        return self._TrainingJobVersion

    @TrainingJobVersion.setter
    def TrainingJobVersion(self, TrainingJobVersion):
        self._TrainingJobVersion = TrainingJobVersion

    @property
    def TrainingPreference(self):
        return self._TrainingPreference

    @TrainingPreference.setter
    def TrainingPreference(self, TrainingPreference):
        self._TrainingPreference = TrainingPreference

    @property
    def AutoMLTaskId(self):
        return self._AutoMLTaskId

    @AutoMLTaskId.setter
    def AutoMLTaskId(self, AutoMLTaskId):
        self._AutoMLTaskId = AutoMLTaskId

    @property
    def IsQAT(self):
        return self._IsQAT

    @IsQAT.setter
    def IsQAT(self, IsQAT):
        self._IsQAT = IsQAT


    def _deserialize(self, params):
        self._TrainingModelId = params.get("TrainingModelId")
        self._TrainingModelVersionId = params.get("TrainingModelVersionId")
        self._TrainingModelVersion = params.get("TrainingModelVersion")
        self._TrainingModelSource = params.get("TrainingModelSource")
        self._TrainingModelCreateTime = params.get("TrainingModelCreateTime")
        self._TrainingModelCreator = params.get("TrainingModelCreator")
        self._AlgorithmFramework = params.get("AlgorithmFramework")
        self._ReasoningEnvironment = params.get("ReasoningEnvironment")
        self._ReasoningEnvironmentSource = params.get("ReasoningEnvironmentSource")
        self._TrainingModelIndex = params.get("TrainingModelIndex")
        self._TrainingJobName = params.get("TrainingJobName")
        if params.get("TrainingModelCosPath") is not None:
            self._TrainingModelCosPath = CosPathInfo()
            self._TrainingModelCosPath._deserialize(params.get("TrainingModelCosPath"))
        self._TrainingModelName = params.get("TrainingModelName")
        self._TrainingJobId = params.get("TrainingJobId")
        if params.get("ReasoningImageInfo") is not None:
            self._ReasoningImageInfo = ImageInfo()
            self._ReasoningImageInfo._deserialize(params.get("ReasoningImageInfo"))
        self._CreateTime = params.get("CreateTime")
        self._TrainingModelStatus = params.get("TrainingModelStatus")
        self._TrainingModelProgress = params.get("TrainingModelProgress")
        self._TrainingModelErrorMsg = params.get("TrainingModelErrorMsg")
        self._TrainingModelFormat = params.get("TrainingModelFormat")
        self._VersionType = params.get("VersionType")
        self._GPUType = params.get("GPUType")
        self._AutoClean = params.get("AutoClean")
        self._ModelCleanPeriod = params.get("ModelCleanPeriod")
        self._MaxReservedModels = params.get("MaxReservedModels")
        if params.get("ModelHotUpdatePath") is not None:
            self._ModelHotUpdatePath = CosPathInfo()
            self._ModelHotUpdatePath._deserialize(params.get("ModelHotUpdatePath"))
        self._ReasoningEnvironmentId = params.get("ReasoningEnvironmentId")
        self._TrainingJobVersion = params.get("TrainingJobVersion")
        self._TrainingPreference = params.get("TrainingPreference")
        self._AutoMLTaskId = params.get("AutoMLTaskId")
        self._IsQAT = params.get("IsQAT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingTaskDetail(AbstractModel):
    """训练任务详情

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        :param _Name: 训练任务名称
        :type Name: str
        :param _Uin: 主账号uin
        :type Uin: str
        :param _SubUin: 子账号uin
        :type SubUin: str
        :param _Region: 地域
        :type Region: str
        :param _FrameworkName: 训练框架名称，eg：SPARK、PYSARK、TENSORFLOW、PYTORCH
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkName: str
        :param _FrameworkVersion: 训练框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        :param _FrameworkEnvironment: 框架运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkEnvironment: str
        :param _ChargeType: 计费模式
        :type ChargeType: str
        :param _ResourceGroupId: 预付费专用资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ResourceConfigInfos: 资源配置
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _TrainingMode: 训练模式，eg：PS_WORKER、DDP、MPI、HOROVOD
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingMode: str
        :param _CodePackagePath: 代码包
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StartCmdInfo: 启动命令信息
        :type StartCmdInfo: :class:`tencentcloud.tione.v20211111.models.StartCmdInfo`
        :param _DataSource: 数据来源，eg：DATASET、COS
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param _DataConfigs: 数据配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DataConfigs: list of DataConfig
        :param _TuningParameters: 调优参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TuningParameters: str
        :param _Output: 训练输出
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _LogEnable: 是否上报日志
        :type LogEnable: bool
        :param _LogConfig: 日志配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _StartTime: 训练开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param _LatestInstanceId: 最近一次实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestInstanceId: str
        :param _TensorBoardId: TensorBoard ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TensorBoardId: str
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _EndTime: 训练结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _BillingInfo: 计费金额信息，eg：2.00元/小时 (按量计费)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param _ResourceGroupName: 预付费专用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _Message: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Status: 任务状态，eg：STARTING启动中、RUNNING运行中、STOPPING停止中、STOPPED已停止、FAILED异常、SUCCEED已完成
        :type Status: str
        :param _CallbackUrl: 回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        """
        self._Id = None
        self._Name = None
        self._Uin = None
        self._SubUin = None
        self._Region = None
        self._FrameworkName = None
        self._FrameworkVersion = None
        self._FrameworkEnvironment = None
        self._ChargeType = None
        self._ResourceGroupId = None
        self._ResourceConfigInfos = None
        self._Tags = None
        self._TrainingMode = None
        self._CodePackagePath = None
        self._StartCmdInfo = None
        self._DataSource = None
        self._DataConfigs = None
        self._TuningParameters = None
        self._Output = None
        self._LogEnable = None
        self._LogConfig = None
        self._VpcId = None
        self._SubnetId = None
        self._ImageInfo = None
        self._RuntimeInSeconds = None
        self._CreateTime = None
        self._StartTime = None
        self._ChargeStatus = None
        self._LatestInstanceId = None
        self._TensorBoardId = None
        self._Remark = None
        self._FailureReason = None
        self._UpdateTime = None
        self._EndTime = None
        self._BillingInfo = None
        self._ResourceGroupName = None
        self._Message = None
        self._Status = None
        self._CallbackUrl = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FrameworkName(self):
        return self._FrameworkName

    @FrameworkName.setter
    def FrameworkName(self, FrameworkName):
        self._FrameworkName = FrameworkName

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion

    @property
    def FrameworkEnvironment(self):
        return self._FrameworkEnvironment

    @FrameworkEnvironment.setter
    def FrameworkEnvironment(self, FrameworkEnvironment):
        self._FrameworkEnvironment = FrameworkEnvironment

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceConfigInfos(self):
        return self._ResourceConfigInfos

    @ResourceConfigInfos.setter
    def ResourceConfigInfos(self, ResourceConfigInfos):
        self._ResourceConfigInfos = ResourceConfigInfos

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TrainingMode(self):
        return self._TrainingMode

    @TrainingMode.setter
    def TrainingMode(self, TrainingMode):
        self._TrainingMode = TrainingMode

    @property
    def CodePackagePath(self):
        return self._CodePackagePath

    @CodePackagePath.setter
    def CodePackagePath(self, CodePackagePath):
        self._CodePackagePath = CodePackagePath

    @property
    def StartCmdInfo(self):
        return self._StartCmdInfo

    @StartCmdInfo.setter
    def StartCmdInfo(self, StartCmdInfo):
        self._StartCmdInfo = StartCmdInfo

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def DataConfigs(self):
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

    @property
    def TuningParameters(self):
        return self._TuningParameters

    @TuningParameters.setter
    def TuningParameters(self, TuningParameters):
        self._TuningParameters = TuningParameters

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

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
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def LatestInstanceId(self):
        return self._LatestInstanceId

    @LatestInstanceId.setter
    def LatestInstanceId(self, LatestInstanceId):
        self._LatestInstanceId = LatestInstanceId

    @property
    def TensorBoardId(self):
        return self._TensorBoardId

    @TensorBoardId.setter
    def TensorBoardId(self, TensorBoardId):
        self._TensorBoardId = TensorBoardId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def BillingInfo(self):
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._Region = params.get("Region")
        self._FrameworkName = params.get("FrameworkName")
        self._FrameworkVersion = params.get("FrameworkVersion")
        self._FrameworkEnvironment = params.get("FrameworkEnvironment")
        self._ChargeType = params.get("ChargeType")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ResourceConfigInfos") is not None:
            self._ResourceConfigInfos = []
            for item in params.get("ResourceConfigInfos"):
                obj = ResourceConfigInfo()
                obj._deserialize(item)
                self._ResourceConfigInfos.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TrainingMode = params.get("TrainingMode")
        if params.get("CodePackagePath") is not None:
            self._CodePackagePath = CosPathInfo()
            self._CodePackagePath._deserialize(params.get("CodePackagePath"))
        if params.get("StartCmdInfo") is not None:
            self._StartCmdInfo = StartCmdInfo()
            self._StartCmdInfo._deserialize(params.get("StartCmdInfo"))
        self._DataSource = params.get("DataSource")
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        self._TuningParameters = params.get("TuningParameters")
        if params.get("Output") is not None:
            self._Output = CosPathInfo()
            self._Output._deserialize(params.get("Output"))
        self._LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._ChargeStatus = params.get("ChargeStatus")
        self._LatestInstanceId = params.get("LatestInstanceId")
        self._TensorBoardId = params.get("TensorBoardId")
        self._Remark = params.get("Remark")
        self._FailureReason = params.get("FailureReason")
        self._UpdateTime = params.get("UpdateTime")
        self._EndTime = params.get("EndTime")
        self._BillingInfo = params.get("BillingInfo")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingTaskSetItem(AbstractModel):
    """出参类型

    """

    def __init__(self):
        r"""
        :param _Id: 训练任务ID
        :type Id: str
        :param _Name: 训练任务名称
        :type Name: str
        :param _FrameworkName: 框架名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkName: str
        :param _FrameworkVersion: 训练框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        :param _FrameworkEnvironment: 框架运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkEnvironment: str
        :param _ChargeType: 计费模式
        :type ChargeType: str
        :param _ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param _ResourceGroupId: 预付费专用资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _ResourceConfigInfos: 资源配置
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param _TrainingMode: 训练模式eg：PS_WORKER、DDP、MPI、HOROVOD
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingMode: str
        :param _Status: 任务状态，eg：STARTING启动中、RUNNING运行中、STOPPING停止中、STOPPED已停止、FAILED异常、SUCCEED已完成
        :type Status: str
        :param _RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _StartTime: 训练开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 训练结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _Output: 训练输出
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _BillingInfo: 计费金额信息，eg：2.00元/小时 (按量计费)
        :type BillingInfo: str
        :param _ResourceGroupName: 预付费专用资源组名称
        :type ResourceGroupName: str
        :param _ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _Message: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Tags: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _CallbackUrl: 回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        """
        self._Id = None
        self._Name = None
        self._FrameworkName = None
        self._FrameworkVersion = None
        self._FrameworkEnvironment = None
        self._ChargeType = None
        self._ChargeStatus = None
        self._ResourceGroupId = None
        self._ResourceConfigInfos = None
        self._TrainingMode = None
        self._Status = None
        self._RuntimeInSeconds = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Output = None
        self._FailureReason = None
        self._UpdateTime = None
        self._BillingInfo = None
        self._ResourceGroupName = None
        self._ImageInfo = None
        self._Message = None
        self._Tags = None
        self._CallbackUrl = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FrameworkName(self):
        return self._FrameworkName

    @FrameworkName.setter
    def FrameworkName(self, FrameworkName):
        self._FrameworkName = FrameworkName

    @property
    def FrameworkVersion(self):
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion

    @property
    def FrameworkEnvironment(self):
        return self._FrameworkEnvironment

    @FrameworkEnvironment.setter
    def FrameworkEnvironment(self, FrameworkEnvironment):
        self._FrameworkEnvironment = FrameworkEnvironment

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ChargeStatus(self):
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def ResourceGroupId(self):
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceConfigInfos(self):
        return self._ResourceConfigInfos

    @ResourceConfigInfos.setter
    def ResourceConfigInfos(self, ResourceConfigInfos):
        self._ResourceConfigInfos = ResourceConfigInfos

    @property
    def TrainingMode(self):
        return self._TrainingMode

    @TrainingMode.setter
    def TrainingMode(self, TrainingMode):
        self._TrainingMode = TrainingMode

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuntimeInSeconds(self):
        return self._RuntimeInSeconds

    @RuntimeInSeconds.setter
    def RuntimeInSeconds(self, RuntimeInSeconds):
        self._RuntimeInSeconds = RuntimeInSeconds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def FailureReason(self):
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def BillingInfo(self):
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo

    @property
    def ResourceGroupName(self):
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def ImageInfo(self):
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._FrameworkName = params.get("FrameworkName")
        self._FrameworkVersion = params.get("FrameworkVersion")
        self._FrameworkEnvironment = params.get("FrameworkEnvironment")
        self._ChargeType = params.get("ChargeType")
        self._ChargeStatus = params.get("ChargeStatus")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ResourceConfigInfos") is not None:
            self._ResourceConfigInfos = []
            for item in params.get("ResourceConfigInfos"):
                obj = ResourceConfigInfo()
                obj._deserialize(item)
                self._ResourceConfigInfos.append(obj)
        self._TrainingMode = params.get("TrainingMode")
        self._Status = params.get("Status")
        self._RuntimeInSeconds = params.get("RuntimeInSeconds")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Output") is not None:
            self._Output = CosPathInfo()
            self._Output._deserialize(params.get("Output"))
        self._FailureReason = params.get("FailureReason")
        self._UpdateTime = params.get("UpdateTime")
        self._BillingInfo = params.get("BillingInfo")
        self._ResourceGroupName = params.get("ResourceGroupName")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        self._Message = params.get("Message")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    """大模型生成Token统计

    """

    def __init__(self):
        r"""
        :param _CompletionTokens: 生成的token数目
注意：此字段可能返回 null，表示取不到有效值。
        :type CompletionTokens: int
        :param _PromptTokens: 输入的token数目
注意：此字段可能返回 null，表示取不到有效值。
        :type PromptTokens: int
        :param _TotalTokens: 总共token数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalTokens: int
        """
        self._CompletionTokens = None
        self._PromptTokens = None
        self._TotalTokens = None

    @property
    def CompletionTokens(self):
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def PromptTokens(self):
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def TotalTokens(self):
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._CompletionTokens = params.get("CompletionTokens")
        self._PromptTokens = params.get("PromptTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeMount(AbstractModel):
    """外部挂载信息

    """

    def __init__(self):
        r"""
        :param _CFSConfig: cfs的配置信息
        :type CFSConfig: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _VolumeSourceType: 挂载源类型，CFS、COS，默认为CFS
        :type VolumeSourceType: str
        """
        self._CFSConfig = None
        self._VolumeSourceType = None

    @property
    def CFSConfig(self):
        return self._CFSConfig

    @CFSConfig.setter
    def CFSConfig(self, CFSConfig):
        self._CFSConfig = CFSConfig

    @property
    def VolumeSourceType(self):
        return self._VolumeSourceType

    @VolumeSourceType.setter
    def VolumeSourceType(self, VolumeSourceType):
        self._VolumeSourceType = VolumeSourceType


    def _deserialize(self, params):
        if params.get("CFSConfig") is not None:
            self._CFSConfig = CFSConfig()
            self._CFSConfig._deserialize(params.get("CFSConfig"))
        self._VolumeSourceType = params.get("VolumeSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeightEntry(AbstractModel):
    """服务的权重

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务id
        :type ServiceId: str
        :param _Weight: 流量权重值，同 ServiceGroup 下 总和应为 100
        :type Weight: int
        """
        self._ServiceId = None
        self._Weight = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadStatus(AbstractModel):
    """工作负载的状态

    """

    def __init__(self):
        r"""
        :param _Replicas: 当前实例数
        :type Replicas: int
        :param _UpdatedReplicas: 更新的实例数
        :type UpdatedReplicas: int
        :param _ReadyReplicas: 就绪的实例数
        :type ReadyReplicas: int
        :param _AvailableReplicas: 可用的实例数
        :type AvailableReplicas: int
        :param _UnavailableReplicas: 不可用的实例数
        :type UnavailableReplicas: int
        :param _Status: Normal	正常运行中
Abnormal	服务异常，例如容器启动失败等
Waiting	服务等待中，例如容器下载镜像过程等
Stopped   已停止 
Pending 启动中
Stopping 停止中
        :type Status: str
        :param _StatefulSetCondition: 工作负载的状况信息
        :type StatefulSetCondition: list of StatefulSetCondition
        :param _Conditions: 工作负载历史的状况信息
        :type Conditions: list of StatefulSetCondition
        :param _Reason: 状态异常时，展示原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self._Replicas = None
        self._UpdatedReplicas = None
        self._ReadyReplicas = None
        self._AvailableReplicas = None
        self._UnavailableReplicas = None
        self._Status = None
        self._StatefulSetCondition = None
        self._Conditions = None
        self._Reason = None

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def UpdatedReplicas(self):
        return self._UpdatedReplicas

    @UpdatedReplicas.setter
    def UpdatedReplicas(self, UpdatedReplicas):
        self._UpdatedReplicas = UpdatedReplicas

    @property
    def ReadyReplicas(self):
        return self._ReadyReplicas

    @ReadyReplicas.setter
    def ReadyReplicas(self, ReadyReplicas):
        self._ReadyReplicas = ReadyReplicas

    @property
    def AvailableReplicas(self):
        return self._AvailableReplicas

    @AvailableReplicas.setter
    def AvailableReplicas(self, AvailableReplicas):
        self._AvailableReplicas = AvailableReplicas

    @property
    def UnavailableReplicas(self):
        return self._UnavailableReplicas

    @UnavailableReplicas.setter
    def UnavailableReplicas(self, UnavailableReplicas):
        self._UnavailableReplicas = UnavailableReplicas

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatefulSetCondition(self):
        warnings.warn("parameter `StatefulSetCondition` is deprecated", DeprecationWarning) 

        return self._StatefulSetCondition

    @StatefulSetCondition.setter
    def StatefulSetCondition(self, StatefulSetCondition):
        warnings.warn("parameter `StatefulSetCondition` is deprecated", DeprecationWarning) 

        self._StatefulSetCondition = StatefulSetCondition

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Replicas = params.get("Replicas")
        self._UpdatedReplicas = params.get("UpdatedReplicas")
        self._ReadyReplicas = params.get("ReadyReplicas")
        self._AvailableReplicas = params.get("AvailableReplicas")
        self._UnavailableReplicas = params.get("UnavailableReplicas")
        self._Status = params.get("Status")
        if params.get("StatefulSetCondition") is not None:
            self._StatefulSetCondition = []
            for item in params.get("StatefulSetCondition"):
                obj = StatefulSetCondition()
                obj._deserialize(item)
                self._StatefulSetCondition.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = StatefulSetCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        