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
        :param Id: 接口id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param ServiceGroupId: 接口所属服务组id
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroupId: str
        :param Description: 接口描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param RelativeUrl: 相对路径
注意：此字段可能返回 null，表示取不到有效值。
        :type RelativeUrl: str
        :param ServiceType: 服务类型 HTTP HTTPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param HttpMethod: GET POST
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpMethod: str
        :param HttpInputExample: 请求示例
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpInputExample: str
        :param HttpOutputExample: 回包示例
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpOutputExample: str
        :param UpdatedBy: 更新成员
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedBy: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param Uin: 主账号uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param SubUin: 子账号subuin
注意：此字段可能返回 null，表示取不到有效值。
        :type SubUin: str
        """
        self.Id = None
        self.ServiceGroupId = None
        self.Description = None
        self.RelativeUrl = None
        self.ServiceType = None
        self.HttpMethod = None
        self.HttpInputExample = None
        self.HttpOutputExample = None
        self.UpdatedBy = None
        self.UpdatedAt = None
        self.Uin = None
        self.SubUin = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ServiceGroupId = params.get("ServiceGroupId")
        self.Description = params.get("Description")
        self.RelativeUrl = params.get("RelativeUrl")
        self.ServiceType = params.get("ServiceType")
        self.HttpMethod = params.get("HttpMethod")
        self.HttpInputExample = params.get("HttpInputExample")
        self.HttpOutputExample = params.get("HttpOutputExample")
        self.UpdatedBy = params.get("UpdatedBy")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Uin = params.get("Uin")
        self.SubUin = params.get("SubUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModelAccTask(AbstractModel):
    """批量模型加速任务

    """

    def __init__(self):
        r"""
        :param ModelId: 模型ID
        :type ModelId: str
        :param ModelVersion: 模型版本
        :type ModelVersion: str
        :param ModelSource: 模型来源(JOB/COS)
        :type ModelSource: str
        :param ModelFormat: 模型格式(TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/MMDETECTION/ONNX/HUGGING_FACE)
        :type ModelFormat: str
        :param TensorInfos: 模型Tensor信息
        :type TensorInfos: list of str
        :param AccEngineVersion: 加速引擎版本
        :type AccEngineVersion: str
        :param ModelInputPath: 模型输入cos路径
        :type ModelInputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param ModelName: 模型名称
        :type ModelName: str
        :param ModelSignature: SavedModel保存时配置的签名
        :type ModelSignature: str
        :param FrameworkVersion: 加速引擎对应的框架版本
        :type FrameworkVersion: str
        """
        self.ModelId = None
        self.ModelVersion = None
        self.ModelSource = None
        self.ModelFormat = None
        self.TensorInfos = None
        self.AccEngineVersion = None
        self.ModelInputPath = None
        self.ModelName = None
        self.ModelSignature = None
        self.FrameworkVersion = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ModelVersion = params.get("ModelVersion")
        self.ModelSource = params.get("ModelSource")
        self.ModelFormat = params.get("ModelFormat")
        self.TensorInfos = params.get("TensorInfos")
        self.AccEngineVersion = params.get("AccEngineVersion")
        if params.get("ModelInputPath") is not None:
            self.ModelInputPath = CosPathInfo()
            self.ModelInputPath._deserialize(params.get("ModelInputPath"))
        self.ModelName = params.get("ModelName")
        self.ModelSignature = params.get("ModelSignature")
        self.FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchTaskDetail(AbstractModel):
    """跑批任务详情

    """

    def __init__(self):
        r"""
        :param BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        :param BatchTaskName: 跑批任务名称
        :type BatchTaskName: str
        :param Uin: 主账号uin
        :type Uin: str
        :param SubUin: 子账号uin
        :type SubUin: str
        :param Region: 地域
        :type Region: str
        :param ChargeType: 计费模式
        :type ChargeType: str
        :param ResourceGroupId: 包年包月资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param ResourceGroupName: 包年包月资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param ResourceConfigInfo: 资源配置
        :type ResourceConfigInfo: :class:`tencentcloud.tione.v20211111.models.ResourceConfigInfo`
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param ModelInfo: 服务对应的模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param CodePackagePath: 代码包
注意：此字段可能返回 null，表示取不到有效值。
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param StartCmd: 启动命令
注意：此字段可能返回 null，表示取不到有效值。
        :type StartCmd: str
        :param DataConfigs: 输入数据配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DataConfigs: list of DataConfig
        :param Outputs: 输出数据配置
        :type Outputs: list of DataConfig
        :param LogEnable: 是否上报日志
        :type LogEnable: bool
        :param LogConfig: 日志配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param VpcId: vpc id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Status: 任务状态
        :type Status: str
        :param RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param StartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param LatestInstanceId: 最近一次实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestInstanceId: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (for 按量计费)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param PodList: 运行中的Pod的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: list of str
        :param ModelInferenceCodeInfo: 模型推理代码信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInferenceCodeInfo: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        self.BatchTaskId = None
        self.BatchTaskName = None
        self.Uin = None
        self.SubUin = None
        self.Region = None
        self.ChargeType = None
        self.ResourceGroupId = None
        self.ResourceGroupName = None
        self.ResourceConfigInfo = None
        self.Tags = None
        self.ModelInfo = None
        self.ImageInfo = None
        self.CodePackagePath = None
        self.StartCmd = None
        self.DataConfigs = None
        self.Outputs = None
        self.LogEnable = None
        self.LogConfig = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.RuntimeInSeconds = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.ChargeStatus = None
        self.LatestInstanceId = None
        self.Remark = None
        self.FailureReason = None
        self.BillingInfo = None
        self.PodList = None
        self.ModelInferenceCodeInfo = None


    def _deserialize(self, params):
        self.BatchTaskId = params.get("BatchTaskId")
        self.BatchTaskName = params.get("BatchTaskName")
        self.Uin = params.get("Uin")
        self.SubUin = params.get("SubUin")
        self.Region = params.get("Region")
        self.ChargeType = params.get("ChargeType")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.ResourceGroupName = params.get("ResourceGroupName")
        if params.get("ResourceConfigInfo") is not None:
            self.ResourceConfigInfo = ResourceConfigInfo()
            self.ResourceConfigInfo._deserialize(params.get("ResourceConfigInfo"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ModelInfo") is not None:
            self.ModelInfo = ModelInfo()
            self.ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodePackagePath") is not None:
            self.CodePackagePath = CosPathInfo()
            self.CodePackagePath._deserialize(params.get("CodePackagePath"))
        self.StartCmd = params.get("StartCmd")
        if params.get("DataConfigs") is not None:
            self.DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self.DataConfigs.append(obj)
        if params.get("Outputs") is not None:
            self.Outputs = []
            for item in params.get("Outputs"):
                obj = DataConfig()
                obj._deserialize(item)
                self.Outputs.append(obj)
        self.LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self.LogConfig = LogConfig()
            self.LogConfig._deserialize(params.get("LogConfig"))
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.RuntimeInSeconds = params.get("RuntimeInSeconds")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ChargeStatus = params.get("ChargeStatus")
        self.LatestInstanceId = params.get("LatestInstanceId")
        self.Remark = params.get("Remark")
        self.FailureReason = params.get("FailureReason")
        self.BillingInfo = params.get("BillingInfo")
        self.PodList = params.get("PodList")
        if params.get("ModelInferenceCodeInfo") is not None:
            self.ModelInferenceCodeInfo = CosPathInfo()
            self.ModelInferenceCodeInfo._deserialize(params.get("ModelInferenceCodeInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchTaskInstance(AbstractModel):
    """批处理任务实例

    """

    def __init__(self):
        r"""
        :param BatchTaskInstanceId: 任务实例id
        :type BatchTaskInstanceId: str
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Status: 任务状态
        :type Status: str
        :param RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        """
        self.BatchTaskInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.RuntimeInSeconds = None


    def _deserialize(self, params):
        self.BatchTaskInstanceId = params.get("BatchTaskInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.RuntimeInSeconds = params.get("RuntimeInSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchTaskSetItem(AbstractModel):
    """出参类型

    """

    def __init__(self):
        r"""
        :param BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        :param BatchTaskName: 跑批任务名称
        :type BatchTaskName: str
        :param ModelInfo: 模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param ImageInfo: 镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param ChargeType: 计费模式
        :type ChargeType: str
        :param ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param ResourceGroupId: 包年包月资源组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param ResourceConfigInfo: 资源配置
        :type ResourceConfigInfo: :class:`tencentcloud.tione.v20211111.models.ResourceConfigInfo`
        :param Tags: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Status: 任务状态
        :type Status: str
        :param RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Outputs: 输出
        :type Outputs: list of DataConfig
        :param ResourceGroupName: 包年包月资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param FailureReason: 失败原因
        :type FailureReason: str
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (for 按量计费)
        :type BillingInfo: str
        """
        self.BatchTaskId = None
        self.BatchTaskName = None
        self.ModelInfo = None
        self.ImageInfo = None
        self.ChargeType = None
        self.ChargeStatus = None
        self.ResourceGroupId = None
        self.ResourceConfigInfo = None
        self.Tags = None
        self.Status = None
        self.RuntimeInSeconds = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.UpdateTime = None
        self.Outputs = None
        self.ResourceGroupName = None
        self.FailureReason = None
        self.BillingInfo = None


    def _deserialize(self, params):
        self.BatchTaskId = params.get("BatchTaskId")
        self.BatchTaskName = params.get("BatchTaskName")
        if params.get("ModelInfo") is not None:
            self.ModelInfo = ModelInfo()
            self.ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.ChargeType = params.get("ChargeType")
        self.ChargeStatus = params.get("ChargeStatus")
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ResourceConfigInfo") is not None:
            self.ResourceConfigInfo = ResourceConfigInfo()
            self.ResourceConfigInfo._deserialize(params.get("ResourceConfigInfo"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Status = params.get("Status")
        self.RuntimeInSeconds = params.get("RuntimeInSeconds")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Outputs") is not None:
            self.Outputs = []
            for item in params.get("Outputs"):
                obj = DataConfig()
                obj._deserialize(item)
                self.Outputs.append(obj)
        self.ResourceGroupName = params.get("ResourceGroupName")
        self.FailureReason = params.get("FailureReason")
        self.BillingInfo = params.get("BillingInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSConfig(AbstractModel):
    """CFS存储的配置

    """

    def __init__(self):
        r"""
        :param Id: cfs的实例的ID
        :type Id: str
        :param Path: 存储的路径
        :type Path: str
        :param MountType: cfs的挂载类型，可选值为：STORAGE、SOURCE 分别表示存储拓展模式和数据源模式，默认为 STORAGE
注意：此字段可能返回 null，表示取不到有效值。
        :type MountType: str
        :param Protocol: 协议 1: NFS, 2: TURBO
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        """
        self.Id = None
        self.Path = None
        self.MountType = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Path = params.get("Path")
        self.MountType = params.get("MountType")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSTurbo(AbstractModel):
    """配置CFSTurbo参数

    """

    def __init__(self):
        r"""
        :param Id: CFSTurbo实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Path: CFSTurbo路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self.Id = None
        self.Path = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Container(AbstractModel):
    """容器信息

    """

    def __init__(self):
        r"""
        :param Name: 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param ContainerId: id
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerId: str
        :param Image: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param Status: 容器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.tione.v20211111.models.ContainerStatus`
        """
        self.Name = None
        self.ContainerId = None
        self.Image = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ContainerId = params.get("ContainerId")
        self.Image = params.get("Image")
        if params.get("Status") is not None:
            self.Status = ContainerStatus()
            self.Status._deserialize(params.get("Status"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerStatus(AbstractModel):
    """容器状态

    """

    def __init__(self):
        r"""
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param State: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param Ready: 是否就绪
注意：此字段可能返回 null，表示取不到有效值。
        :type Ready: bool
        :param Reason: 状态原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param Message: 容器的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.RestartCount = None
        self.State = None
        self.Ready = None
        self.Reason = None
        self.Message = None


    def _deserialize(self, params):
        self.RestartCount = params.get("RestartCount")
        self.State = params.get("State")
        self.Ready = params.get("Ready")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosPathInfo(AbstractModel):
    """cos的路径信息

    """

    def __init__(self):
        r"""
        :param Bucket: 存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Region: 所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Paths: 路径列表，目前只支持单个
注意：此字段可能返回 null，表示取不到有效值。
        :type Paths: list of str
        """
        self.Bucket = None
        self.Region = None
        self.Paths = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Paths = params.get("Paths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchModelAccTasksRequest(AbstractModel):
    """CreateBatchModelAccTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskName: 模型加速任务名称
        :type ModelAccTaskName: str
        :param BatchModelAccTasks: 批量模型加速任务
        :type BatchModelAccTasks: list of BatchModelAccTask
        :param ModelOutputPath: 模型加速保存路径
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param Tags: 标签
        :type Tags: list of Tag
        :param OptimizationLevel: 优化级别(NO_LOSS/FP16/INT8)，默认FP16
        :type OptimizationLevel: str
        :param GPUType: GPU卡类型(T4/V100/A10)，默认T4
        :type GPUType: str
        :param HyperParameter: 专业参数设置
        :type HyperParameter: :class:`tencentcloud.tione.v20211111.models.HyperParameter`
        """
        self.ModelAccTaskName = None
        self.BatchModelAccTasks = None
        self.ModelOutputPath = None
        self.Tags = None
        self.OptimizationLevel = None
        self.GPUType = None
        self.HyperParameter = None


    def _deserialize(self, params):
        self.ModelAccTaskName = params.get("ModelAccTaskName")
        if params.get("BatchModelAccTasks") is not None:
            self.BatchModelAccTasks = []
            for item in params.get("BatchModelAccTasks"):
                obj = BatchModelAccTask()
                obj._deserialize(item)
                self.BatchModelAccTasks.append(obj)
        if params.get("ModelOutputPath") is not None:
            self.ModelOutputPath = CosPathInfo()
            self.ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.OptimizationLevel = params.get("OptimizationLevel")
        self.GPUType = params.get("GPUType")
        if params.get("HyperParameter") is not None:
            self.HyperParameter = HyperParameter()
            self.HyperParameter._deserialize(params.get("HyperParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchModelAccTasksResponse(AbstractModel):
    """CreateBatchModelAccTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskIds: 模型优化任务ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelAccTaskIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelAccTaskIds = params.get("ModelAccTaskIds")
        self.RequestId = params.get("RequestId")


class CreateBatchTaskRequest(AbstractModel):
    """CreateBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskName: 跑批任务名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type BatchTaskName: str
        :param ChargeType: 计费模式，eg：PREPAID 包年包月；POSTPAID_BY_HOUR 按量计费
        :type ChargeType: str
        :param ResourceConfigInfo: 资源配置
        :type ResourceConfigInfo: :class:`tencentcloud.tione.v20211111.models.ResourceConfigInfo`
        :param Outputs: 结果输出
        :type Outputs: list of DataConfig
        :param LogEnable: 是否上报日志
        :type LogEnable: bool
        :param JobType: 工作类型 1:单次 2:周期
        :type JobType: int
        :param CronInfo: 任务周期描述
        :type CronInfo: :class:`tencentcloud.tione.v20211111.models.CronInfo`
        :param ResourceGroupId: 包年包月资源组ID
        :type ResourceGroupId: str
        :param Tags: 标签配置
        :type Tags: list of Tag
        :param ModelInfo: 服务对应的模型信息，有模型文件时需要填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param ImageInfo: 自定义镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param CodePackage: 代码包
        :type CodePackage: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param StartCmd: 启动命令
        :type StartCmd: str
        :param DataConfigs: 数据配置
        :type DataConfigs: list of DataConfig
        :param LogConfig: 日志配置
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param VpcId: VPC Id
        :type VpcId: str
        :param SubnetId: 子网Id
        :type SubnetId: str
        :param Remark: 备注
        :type Remark: str
        :param CallbackUrl: 任务执行结果回调URL，仅支持http和https。回调格式&内容详见: [TI-ONE 接口回调说明](https://cloud.tencent.com/document/product/851/84292)
        :type CallbackUrl: str
        """
        self.BatchTaskName = None
        self.ChargeType = None
        self.ResourceConfigInfo = None
        self.Outputs = None
        self.LogEnable = None
        self.JobType = None
        self.CronInfo = None
        self.ResourceGroupId = None
        self.Tags = None
        self.ModelInfo = None
        self.ImageInfo = None
        self.CodePackage = None
        self.StartCmd = None
        self.DataConfigs = None
        self.LogConfig = None
        self.VpcId = None
        self.SubnetId = None
        self.Remark = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.BatchTaskName = params.get("BatchTaskName")
        self.ChargeType = params.get("ChargeType")
        if params.get("ResourceConfigInfo") is not None:
            self.ResourceConfigInfo = ResourceConfigInfo()
            self.ResourceConfigInfo._deserialize(params.get("ResourceConfigInfo"))
        if params.get("Outputs") is not None:
            self.Outputs = []
            for item in params.get("Outputs"):
                obj = DataConfig()
                obj._deserialize(item)
                self.Outputs.append(obj)
        self.LogEnable = params.get("LogEnable")
        self.JobType = params.get("JobType")
        if params.get("CronInfo") is not None:
            self.CronInfo = CronInfo()
            self.CronInfo._deserialize(params.get("CronInfo"))
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ModelInfo") is not None:
            self.ModelInfo = ModelInfo()
            self.ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodePackage") is not None:
            self.CodePackage = CosPathInfo()
            self.CodePackage._deserialize(params.get("CodePackage"))
        self.StartCmd = params.get("StartCmd")
        if params.get("DataConfigs") is not None:
            self.DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self.DataConfigs.append(obj)
        if params.get("LogConfig") is not None:
            self.LogConfig = LogConfig()
            self.LogConfig._deserialize(params.get("LogConfig"))
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Remark = params.get("Remark")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchTaskResponse(AbstractModel):
    """CreateBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchTaskId = params.get("BatchTaskId")
        self.RequestId = params.get("RequestId")


class CreateDatasetRequest(AbstractModel):
    """CreateDataset请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasetName: 数据集名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type DatasetName: str
        :param DatasetType: 数据集类型:
TYPE_DATASET_TEXT，文本
TYPE_DATASET_IMAGE，图片
TYPE_DATASET_TABLE，表格
TYPE_DATASET_OTHER，其他
        :type DatasetType: str
        :param StorageDataPath: 数据源cos路径
        :type StorageDataPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param StorageLabelPath: 数据集标签cos存储路径
        :type StorageLabelPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param DatasetTags: 数据集标签
        :type DatasetTags: list of Tag
        :param AnnotationStatus: 数据集标注状态:
STATUS_NON_ANNOTATED，未标注
STATUS_ANNOTATED，已标注
        :type AnnotationStatus: str
        :param AnnotationType: 标注类型:
ANNOTATION_TYPE_CLASSIFICATION，图片分类
ANNOTATION_TYPE_DETECTION，目标检测
ANNOTATION_TYPE_SEGMENTATION，图片分割
ANNOTATION_TYPE_TRACKING，目标跟踪
        :type AnnotationType: str
        :param AnnotationFormat: 标注格式:
ANNOTATION_FORMAT_TI，TI平台格式
ANNOTATION_FORMAT_PASCAL，Pascal Voc
ANNOTATION_FORMAT_COCO，COCO
ANNOTATION_FORMAT_FILE，文件目录结构
        :type AnnotationFormat: str
        :param SchemaInfos: 表头信息
        :type SchemaInfos: list of SchemaInfo
        :param IsSchemaExisted: 数据是否存在表头
        :type IsSchemaExisted: bool
        :param ContentType: 导入文件粒度，按行或者按文件
        :type ContentType: str
        """
        self.DatasetName = None
        self.DatasetType = None
        self.StorageDataPath = None
        self.StorageLabelPath = None
        self.DatasetTags = None
        self.AnnotationStatus = None
        self.AnnotationType = None
        self.AnnotationFormat = None
        self.SchemaInfos = None
        self.IsSchemaExisted = None
        self.ContentType = None


    def _deserialize(self, params):
        self.DatasetName = params.get("DatasetName")
        self.DatasetType = params.get("DatasetType")
        if params.get("StorageDataPath") is not None:
            self.StorageDataPath = CosPathInfo()
            self.StorageDataPath._deserialize(params.get("StorageDataPath"))
        if params.get("StorageLabelPath") is not None:
            self.StorageLabelPath = CosPathInfo()
            self.StorageLabelPath._deserialize(params.get("StorageLabelPath"))
        if params.get("DatasetTags") is not None:
            self.DatasetTags = []
            for item in params.get("DatasetTags"):
                obj = Tag()
                obj._deserialize(item)
                self.DatasetTags.append(obj)
        self.AnnotationStatus = params.get("AnnotationStatus")
        self.AnnotationType = params.get("AnnotationType")
        self.AnnotationFormat = params.get("AnnotationFormat")
        if params.get("SchemaInfos") is not None:
            self.SchemaInfos = []
            for item in params.get("SchemaInfos"):
                obj = SchemaInfo()
                obj._deserialize(item)
                self.SchemaInfos.append(obj)
        self.IsSchemaExisted = params.get("IsSchemaExisted")
        self.ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatasetResponse(AbstractModel):
    """CreateDataset返回参数结构体

    """

    def __init__(self):
        r"""
        :param DatasetId: 数据集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DatasetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.RequestId = params.get("RequestId")


class CreateModelServiceRequest(AbstractModel):
    """CreateModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 新增版本时需要填写
        :type ServiceGroupId: str
        :param ServiceGroupName: 不超过60个字，仅支持英文、数字、下划线"_"、短横"-"，只能以英文、数字开头
        :type ServiceGroupName: str
        :param ServiceDescription: 模型服务的描述
        :type ServiceDescription: str
        :param ChargeType: 付费模式,有 PREPAID （包年包月）和 POSTPAID_BY_HOUR（按量付费）
        :type ChargeType: str
        :param ResourceGroupId: 预付费模式下所属的资源组id，同服务组下唯一
        :type ResourceGroupId: str
        :param ModelInfo: 模型信息，需要挂载模型时填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param ImageInfo: 镜像信息，配置服务运行所需的镜像地址等信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param Env: 环境变量，可选参数，用于配置容器中的环境变量
        :type Env: list of EnvVar
        :param Resources: 资源描述，指定包年包月模式下的cpu,mem,gpu等信息，后付费无需填写
        :type Resources: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param InstanceType: 使用DescribeBillingSpecs接口返回的规格列表中的值，或者参考实例列表:
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
        :param ScaleMode: 扩缩容类型 支持：自动 - "AUTO", 手动 - "MANUAL",默认为MANUAL
        :type ScaleMode: str
        :param Replicas: 实例数量, 不同计费模式和调节模式下对应关系如下
PREPAID 和 POSTPAID_BY_HOUR:
手动调节模式下对应 实例数量
自动调节模式下对应 基于时间的默认策略的实例数量
HYBRID_PAID:
后付费实例手动调节模式下对应 实例数量
后付费实例自动调节模式下对应 时间策略的默认策略的实例数量
        :type Replicas: int
        :param HorizontalPodAutoscaler: 自动伸缩信息
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        :param LogEnable: 是否开启日志投递，开启后需填写配置投递到指定cls
        :type LogEnable: bool
        :param LogConfig: 日志配置，需要投递服务日志到指定cls时填写
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param AuthorizationEnable: 是否开启接口鉴权，开启后自动生成token信息，访问需要token鉴权
        :type AuthorizationEnable: bool
        :param Tags: 腾讯云标签
        :type Tags: list of Tag
        :param NewVersion: 是否新增版本
        :type NewVersion: bool
        :param CronScaleJobs: 定时任务配置，使用定时策略时填写
        :type CronScaleJobs: list of CronScaleJob
        :param ScaleStrategy: 自动伸缩策略配置 HPA : 通过HPA进行弹性伸缩 CRON 通过定时任务进行伸缩
        :type ScaleStrategy: str
        :param HybridBillingPrepaidReplicas: 计费模式[HYBRID_PAID]时生效, 用于标识混合计费模式下的预付费实例数
        :type HybridBillingPrepaidReplicas: int
        :param CreateSource: [AUTO_ML 自动学习，自动学习正式发布 AUTO_ML_FORMAL, DEFAULT 默认]
        :type CreateSource: str
        :param ModelHotUpdateEnable: 是否开启模型的热更新。默认不开启
        :type ModelHotUpdateEnable: bool
        :param ScheduledAction: 定时停止配置
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param VolumeMount: 挂载配置，目前只支持CFS
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        :param ServiceLimit: 服务限速限流相关配置
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param CallbackUrl: 回调地址，用于回调创建服务状态信息，回调格式&内容详情见：[TI-ONE 接口回调说明](https://cloud.tencent.com/document/product/851/84292)
        :type CallbackUrl: str
        """
        self.ServiceGroupId = None
        self.ServiceGroupName = None
        self.ServiceDescription = None
        self.ChargeType = None
        self.ResourceGroupId = None
        self.ModelInfo = None
        self.ImageInfo = None
        self.Env = None
        self.Resources = None
        self.InstanceType = None
        self.ScaleMode = None
        self.Replicas = None
        self.HorizontalPodAutoscaler = None
        self.LogEnable = None
        self.LogConfig = None
        self.AuthorizationEnable = None
        self.Tags = None
        self.NewVersion = None
        self.CronScaleJobs = None
        self.ScaleStrategy = None
        self.HybridBillingPrepaidReplicas = None
        self.CreateSource = None
        self.ModelHotUpdateEnable = None
        self.ScheduledAction = None
        self.VolumeMount = None
        self.ServiceLimit = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        self.ServiceGroupName = params.get("ServiceGroupName")
        self.ServiceDescription = params.get("ServiceDescription")
        self.ChargeType = params.get("ChargeType")
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ModelInfo") is not None:
            self.ModelInfo = ModelInfo()
            self.ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("Env") is not None:
            self.Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self.Env.append(obj)
        if params.get("Resources") is not None:
            self.Resources = ResourceInfo()
            self.Resources._deserialize(params.get("Resources"))
        self.InstanceType = params.get("InstanceType")
        self.ScaleMode = params.get("ScaleMode")
        self.Replicas = params.get("Replicas")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self.LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self.LogConfig = LogConfig()
            self.LogConfig._deserialize(params.get("LogConfig"))
        self.AuthorizationEnable = params.get("AuthorizationEnable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.NewVersion = params.get("NewVersion")
        if params.get("CronScaleJobs") is not None:
            self.CronScaleJobs = []
            for item in params.get("CronScaleJobs"):
                obj = CronScaleJob()
                obj._deserialize(item)
                self.CronScaleJobs.append(obj)
        self.ScaleStrategy = params.get("ScaleStrategy")
        self.HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
        self.CreateSource = params.get("CreateSource")
        self.ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
        if params.get("ScheduledAction") is not None:
            self.ScheduledAction = ScheduledAction()
            self.ScheduledAction._deserialize(params.get("ScheduledAction"))
        if params.get("VolumeMount") is not None:
            self.VolumeMount = VolumeMount()
            self.VolumeMount._deserialize(params.get("VolumeMount"))
        if params.get("ServiceLimit") is not None:
            self.ServiceLimit = ServiceLimit()
            self.ServiceLimit._deserialize(params.get("ServiceLimit"))
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelServiceResponse(AbstractModel):
    """CreateModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Service: 生成的模型服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")


class CreateOptimizedModelRequest(AbstractModel):
    """CreateOptimizedModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        :param Tags: 标签
        :type Tags: list of Tag
        """
        self.ModelAccTaskId = None
        self.Tags = None


    def _deserialize(self, params):
        self.ModelAccTaskId = params.get("ModelAccTaskId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOptimizedModelResponse(AbstractModel):
    """CreateOptimizedModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelId: 模型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param ModelVersionId: 模型版本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelVersionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelId = None
        self.ModelVersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ModelVersionId = params.get("ModelVersionId")
        self.RequestId = params.get("RequestId")


class CreateTrainingModelRequest(AbstractModel):
    """CreateTrainingModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImportMethod: 导入方式
MODEL：导入新模型
VERSION：导入新版本
EXIST：导入现有版本
        :type ImportMethod: str
        :param TrainingModelCosPath: 模型来源cos目录，以/结尾
        :type TrainingModelCosPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param ReasoningEnvironmentSource: 推理环境来源（SYSTEM/CUSTOM）
        :type ReasoningEnvironmentSource: str
        :param TrainingModelName: 模型名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type TrainingModelName: str
        :param Tags: 标签配置
        :type Tags: list of Tag
        :param TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param AlgorithmFramework: 算法框架 （PYTORCH/TENSORFLOW/DETECTRON2/PMML/MMDETECTION)
        :type AlgorithmFramework: str
        :param ReasoningEnvironment: 推理环境
        :type ReasoningEnvironment: str
        :param TrainingModelIndex: 训练指标，最多支持1000字符
        :type TrainingModelIndex: str
        :param TrainingModelVersion: 模型版本
        :type TrainingModelVersion: str
        :param ReasoningImageInfo: 自定义推理环境
        :type ReasoningImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param ModelMoveMode: 模型移动方式（CUT/COPY）
        :type ModelMoveMode: str
        :param TrainingJobId: 训练任务ID
        :type TrainingJobId: str
        :param TrainingModelId: 模型ID（导入新模型不需要，导入新版本需要）
        :type TrainingModelId: str
        :param ModelOutputPath: 模型存储cos目录
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param TrainingModelSource: 模型来源 （JOB/COS）
        :type TrainingModelSource: str
        :param TrainingPreference: 模型偏好
        :type TrainingPreference: str
        :param AutoMLTaskId: 自动学习任务ID（已废弃）
        :type AutoMLTaskId: str
        :param TrainingJobVersion: 任务版本
        :type TrainingJobVersion: str
        :param ModelVersionType: 模型版本类型；
枚举值：NORMAL(通用)  ACCELERATE(加速)
注意:  默认为NORMAL
        :type ModelVersionType: str
        :param ModelFormat: 模型格式 （PYTORCH/TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/PMML/MMDETECTION/ONNX/HUGGING_FACE）
        :type ModelFormat: str
        :param ReasoningEnvironmentId: 推理镜像ID
        :type ReasoningEnvironmentId: str
        :param AutoClean: 模型自动清理开关(true/false)，当前版本仅支持SAVED_MODEL格式模型
        :type AutoClean: str
        :param MaxReservedModels: 模型数量保留上限(默认值为24个，上限为24，下限为1，步长为1)
        :type MaxReservedModels: int
        :param ModelCleanPeriod: 模型清理周期(默认值为1分钟，上限为1440，下限为1分钟，步长为1)
        :type ModelCleanPeriod: int
        :param IsQAT: 是否QAT模型
        :type IsQAT: bool
        """
        self.ImportMethod = None
        self.TrainingModelCosPath = None
        self.ReasoningEnvironmentSource = None
        self.TrainingModelName = None
        self.Tags = None
        self.TrainingJobName = None
        self.AlgorithmFramework = None
        self.ReasoningEnvironment = None
        self.TrainingModelIndex = None
        self.TrainingModelVersion = None
        self.ReasoningImageInfo = None
        self.ModelMoveMode = None
        self.TrainingJobId = None
        self.TrainingModelId = None
        self.ModelOutputPath = None
        self.TrainingModelSource = None
        self.TrainingPreference = None
        self.AutoMLTaskId = None
        self.TrainingJobVersion = None
        self.ModelVersionType = None
        self.ModelFormat = None
        self.ReasoningEnvironmentId = None
        self.AutoClean = None
        self.MaxReservedModels = None
        self.ModelCleanPeriod = None
        self.IsQAT = None


    def _deserialize(self, params):
        self.ImportMethod = params.get("ImportMethod")
        if params.get("TrainingModelCosPath") is not None:
            self.TrainingModelCosPath = CosPathInfo()
            self.TrainingModelCosPath._deserialize(params.get("TrainingModelCosPath"))
        self.ReasoningEnvironmentSource = params.get("ReasoningEnvironmentSource")
        self.TrainingModelName = params.get("TrainingModelName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.TrainingJobName = params.get("TrainingJobName")
        self.AlgorithmFramework = params.get("AlgorithmFramework")
        self.ReasoningEnvironment = params.get("ReasoningEnvironment")
        self.TrainingModelIndex = params.get("TrainingModelIndex")
        self.TrainingModelVersion = params.get("TrainingModelVersion")
        if params.get("ReasoningImageInfo") is not None:
            self.ReasoningImageInfo = ImageInfo()
            self.ReasoningImageInfo._deserialize(params.get("ReasoningImageInfo"))
        self.ModelMoveMode = params.get("ModelMoveMode")
        self.TrainingJobId = params.get("TrainingJobId")
        self.TrainingModelId = params.get("TrainingModelId")
        if params.get("ModelOutputPath") is not None:
            self.ModelOutputPath = CosPathInfo()
            self.ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        self.TrainingModelSource = params.get("TrainingModelSource")
        self.TrainingPreference = params.get("TrainingPreference")
        self.AutoMLTaskId = params.get("AutoMLTaskId")
        self.TrainingJobVersion = params.get("TrainingJobVersion")
        self.ModelVersionType = params.get("ModelVersionType")
        self.ModelFormat = params.get("ModelFormat")
        self.ReasoningEnvironmentId = params.get("ReasoningEnvironmentId")
        self.AutoClean = params.get("AutoClean")
        self.MaxReservedModels = params.get("MaxReservedModels")
        self.ModelCleanPeriod = params.get("ModelCleanPeriod")
        self.IsQAT = params.get("IsQAT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingModelResponse(AbstractModel):
    """CreateTrainingModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 模型ID，TrainingModel ID
        :type Id: str
        :param TrainingModelVersionId: 模型版本ID
        :type TrainingModelVersionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.TrainingModelVersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TrainingModelVersionId = params.get("TrainingModelVersionId")
        self.RequestId = params.get("RequestId")


class CreateTrainingTaskRequest(AbstractModel):
    """CreateTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 训练任务名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type Name: str
        :param ChargeType: 计费模式，eg：PREPAID 包年包月（资源组）;
POSTPAID_BY_HOUR 按量计费
        :type ChargeType: str
        :param ResourceConfigInfos: 资源配置，需填写对应算力规格ID和节点数量，算力规格ID查询接口为DescribeBillingSpecsPrice，eg：[{"Role":"WORKER", "InstanceType": "TI.S.MEDIUM.POST", "InstanceNum": 1}]
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param CodePackagePath: COS代码包路径
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param TrainingMode: 训练模式，通过DescribeTrainingFrameworks接口查询，eg：PS_WORKER、DDP、MPI、HOROVOD
        :type TrainingMode: str
        :param Output: COS训练输出路径
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param LogEnable: 是否上报日志
        :type LogEnable: bool
        :param FrameworkName: 训练框架名称，通过DescribeTrainingFrameworks接口查询，eg：SPARK、PYSPARK、TENSORFLOW、PYTORCH
        :type FrameworkName: str
        :param FrameworkVersion: 训练框架版本，通过DescribeTrainingFrameworks接口查询，eg：1.15、1.9
        :type FrameworkVersion: str
        :param FrameworkEnvironment: 训练框架环境，通过DescribeTrainingFrameworks接口查询，eg：tf1.15-py3.7-cpu、torch1.9-py3.8-cuda11.1-gpu
        :type FrameworkEnvironment: str
        :param ResourceGroupId: 预付费专用资源组ID，通过DescribeBillingResourceGroups接口查询
        :type ResourceGroupId: str
        :param Tags: 标签配置
        :type Tags: list of Tag
        :param ImageInfo: 自定义镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param StartCmdInfo: 启动命令信息，默认为sh start.sh
        :type StartCmdInfo: :class:`tencentcloud.tione.v20211111.models.StartCmdInfo`
        :param DataConfigs: 数据配置，依赖DataSource字段
        :type DataConfigs: list of DataConfig
        :param VpcId: VPC Id
        :type VpcId: str
        :param SubnetId: 子网Id
        :type SubnetId: str
        :param LogConfig: CLS日志配置
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param TuningParameters: 调优参数
        :type TuningParameters: str
        :param Remark: 备注，最多500个字
        :type Remark: str
        :param DataSource: 数据来源，eg：DATASET、COS、CFS、HDFS
        :type DataSource: str
        :param CallbackUrl: 回调地址，用于创建/启动/停止训练任务的异步回调。回调格式&内容详见：[[TI-ONE接口回调说明]](https://cloud.tencent.com/document/product/851/84292)
        :type CallbackUrl: str
        """
        self.Name = None
        self.ChargeType = None
        self.ResourceConfigInfos = None
        self.CodePackagePath = None
        self.TrainingMode = None
        self.Output = None
        self.LogEnable = None
        self.FrameworkName = None
        self.FrameworkVersion = None
        self.FrameworkEnvironment = None
        self.ResourceGroupId = None
        self.Tags = None
        self.ImageInfo = None
        self.StartCmdInfo = None
        self.DataConfigs = None
        self.VpcId = None
        self.SubnetId = None
        self.LogConfig = None
        self.TuningParameters = None
        self.Remark = None
        self.DataSource = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ChargeType = params.get("ChargeType")
        if params.get("ResourceConfigInfos") is not None:
            self.ResourceConfigInfos = []
            for item in params.get("ResourceConfigInfos"):
                obj = ResourceConfigInfo()
                obj._deserialize(item)
                self.ResourceConfigInfos.append(obj)
        if params.get("CodePackagePath") is not None:
            self.CodePackagePath = CosPathInfo()
            self.CodePackagePath._deserialize(params.get("CodePackagePath"))
        self.TrainingMode = params.get("TrainingMode")
        if params.get("Output") is not None:
            self.Output = CosPathInfo()
            self.Output._deserialize(params.get("Output"))
        self.LogEnable = params.get("LogEnable")
        self.FrameworkName = params.get("FrameworkName")
        self.FrameworkVersion = params.get("FrameworkVersion")
        self.FrameworkEnvironment = params.get("FrameworkEnvironment")
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("StartCmdInfo") is not None:
            self.StartCmdInfo = StartCmdInfo()
            self.StartCmdInfo._deserialize(params.get("StartCmdInfo"))
        if params.get("DataConfigs") is not None:
            self.DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self.DataConfigs.append(obj)
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("LogConfig") is not None:
            self.LogConfig = LogConfig()
            self.LogConfig._deserialize(params.get("LogConfig"))
        self.TuningParameters = params.get("TuningParameters")
        self.Remark = params.get("Remark")
        self.DataSource = params.get("DataSource")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingTaskResponse(AbstractModel):
    """CreateTrainingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CronInfo(AbstractModel):
    """跑批任务周期描述

    """

    def __init__(self):
        r"""
        :param CronConfig: cron配置
        :type CronConfig: str
        :param StartTime: 周期开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 周期结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.CronConfig = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.CronConfig = params.get("CronConfig")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronScaleJob(AbstractModel):
    """定时扩缩任务

    """

    def __init__(self):
        r"""
        :param Schedule: Cron表达式，标识任务的执行时间，精确到分钟级
        :type Schedule: str
        :param Name: 定时任务名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param TargetReplicas: 目标实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetReplicas: int
        :param MinReplicas: 目标min
注意：此字段可能返回 null，表示取不到有效值。
        :type MinReplicas: int
        :param MaxReplicas: 目标max
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param ExcludeDates: 例外时间，Cron表达式，在对应时间内不执行任务。最多支持3条。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeDates: list of str
        """
        self.Schedule = None
        self.Name = None
        self.TargetReplicas = None
        self.MinReplicas = None
        self.MaxReplicas = None
        self.ExcludeDates = None


    def _deserialize(self, params):
        self.Schedule = params.get("Schedule")
        self.Name = params.get("Name")
        self.TargetReplicas = params.get("TargetReplicas")
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        self.ExcludeDates = params.get("ExcludeDates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomTrainingData(AbstractModel):
    """自定义指标

    """

    def __init__(self):
        r"""
        :param MetricName: 指标名
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param Metrics: 指标
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of CustomTrainingMetric
        """
        self.MetricName = None
        self.Metrics = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = CustomTrainingMetric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomTrainingMetric(AbstractModel):
    """自定义指标

    """

    def __init__(self):
        r"""
        :param XType: X轴数据类型: TIMESTAMP; EPOCH; STEP
        :type XType: str
        :param Points: 数据点
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of CustomTrainingPoint
        """
        self.XType = None
        self.Points = None


    def _deserialize(self, params):
        self.XType = params.get("XType")
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = CustomTrainingPoint()
                obj._deserialize(item)
                self.Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomTrainingPoint(AbstractModel):
    """自定义训练指标数据点

    """

    def __init__(self):
        r"""
        :param XValue: X值
        :type XValue: float
        :param YValue: Y值
        :type YValue: float
        """
        self.XValue = None
        self.YValue = None


    def _deserialize(self, params):
        self.XValue = params.get("XValue")
        self.YValue = params.get("YValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataConfig(AbstractModel):
    """数据配置

    """

    def __init__(self):
        r"""
        :param MappingPath: 映射路径
        :type MappingPath: str
        :param DataSourceType: DATASET、COS、CFS、HDFS、WEDATA_HDFS
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceType: str
        :param DataSetSource: 来自数据集的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSetSource: :class:`tencentcloud.tione.v20211111.models.DataSetConfig`
        :param COSSource: 来自cos的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type COSSource: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param CFSSource: 来自CFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSSource: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param HDFSSource: 来自HDFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type HDFSSource: :class:`tencentcloud.tione.v20211111.models.HDFSConfig`
        :param GooseFSSource: 配置GooseFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type GooseFSSource: :class:`tencentcloud.tione.v20211111.models.GooseFS`
        :param CFSTurboSource: 配置TurboFS的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type CFSTurboSource: :class:`tencentcloud.tione.v20211111.models.CFSTurbo`
        """
        self.MappingPath = None
        self.DataSourceType = None
        self.DataSetSource = None
        self.COSSource = None
        self.CFSSource = None
        self.HDFSSource = None
        self.GooseFSSource = None
        self.CFSTurboSource = None


    def _deserialize(self, params):
        self.MappingPath = params.get("MappingPath")
        self.DataSourceType = params.get("DataSourceType")
        if params.get("DataSetSource") is not None:
            self.DataSetSource = DataSetConfig()
            self.DataSetSource._deserialize(params.get("DataSetSource"))
        if params.get("COSSource") is not None:
            self.COSSource = CosPathInfo()
            self.COSSource._deserialize(params.get("COSSource"))
        if params.get("CFSSource") is not None:
            self.CFSSource = CFSConfig()
            self.CFSSource._deserialize(params.get("CFSSource"))
        if params.get("HDFSSource") is not None:
            self.HDFSSource = HDFSConfig()
            self.HDFSSource._deserialize(params.get("HDFSSource"))
        if params.get("GooseFSSource") is not None:
            self.GooseFSSource = GooseFS()
            self.GooseFSSource._deserialize(params.get("GooseFSSource"))
        if params.get("CFSTurboSource") is not None:
            self.CFSTurboSource = CFSTurbo()
            self.CFSTurboSource._deserialize(params.get("CFSTurboSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataPoint(AbstractModel):
    """数据点

    """

    def __init__(self):
        r"""
        :param Name: 指标名字
        :type Name: str
        :param Value: 值
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSetConfig(AbstractModel):
    """数据集结构体

    """

    def __init__(self):
        r"""
        :param Id: 数据集ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasetGroup(AbstractModel):
    """数据集组

    """

    def __init__(self):
        r"""
        :param DatasetId: 数据集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetId: str
        :param DatasetName: 数据集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetName: str
        :param Creator: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param DatasetVersion: 数据集版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetVersion: str
        :param DatasetType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetType: str
        :param DatasetTags: 数据集标签
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetTags: list of Tag
        :param DatasetAnnotationTaskName: 数据集标注任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskName: str
        :param DatasetAnnotationTaskId: 数据集标注任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskId: str
        :param Process: 处理进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: int
        :param DatasetStatus: 数据集状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetStatus: str
        :param ErrorMsg: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ExternalTaskType: 外部关联TASKType
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalTaskType: str
        :param DatasetSize: 数据集大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetSize: str
        :param FileNum: 数据集数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type FileNum: int
        :param StorageDataPath: 数据集源COS路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageDataPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param StorageLabelPath: 数据集标签存储路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLabelPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param DatasetVersions: 数据集版本聚合详情
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetVersions: list of DatasetInfo
        :param AnnotationStatus: 数据集标注状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationStatus: str
        :param AnnotationType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationType: str
        :param AnnotationFormat: 数据集标注格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationFormat: str
        :param DatasetScope: 数据集范围
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetScope: str
        :param OcrScene: 数据集OCR子场景
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrScene: str
        :param AnnotationKeyStatus: 数据集字典修改状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationKeyStatus: str
        :param ContentType: 文本数据集导入方式
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        """
        self.DatasetId = None
        self.DatasetName = None
        self.Creator = None
        self.DatasetVersion = None
        self.DatasetType = None
        self.DatasetTags = None
        self.DatasetAnnotationTaskName = None
        self.DatasetAnnotationTaskId = None
        self.Process = None
        self.DatasetStatus = None
        self.ErrorMsg = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExternalTaskType = None
        self.DatasetSize = None
        self.FileNum = None
        self.StorageDataPath = None
        self.StorageLabelPath = None
        self.DatasetVersions = None
        self.AnnotationStatus = None
        self.AnnotationType = None
        self.AnnotationFormat = None
        self.DatasetScope = None
        self.OcrScene = None
        self.AnnotationKeyStatus = None
        self.ContentType = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.DatasetName = params.get("DatasetName")
        self.Creator = params.get("Creator")
        self.DatasetVersion = params.get("DatasetVersion")
        self.DatasetType = params.get("DatasetType")
        if params.get("DatasetTags") is not None:
            self.DatasetTags = []
            for item in params.get("DatasetTags"):
                obj = Tag()
                obj._deserialize(item)
                self.DatasetTags.append(obj)
        self.DatasetAnnotationTaskName = params.get("DatasetAnnotationTaskName")
        self.DatasetAnnotationTaskId = params.get("DatasetAnnotationTaskId")
        self.Process = params.get("Process")
        self.DatasetStatus = params.get("DatasetStatus")
        self.ErrorMsg = params.get("ErrorMsg")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExternalTaskType = params.get("ExternalTaskType")
        self.DatasetSize = params.get("DatasetSize")
        self.FileNum = params.get("FileNum")
        if params.get("StorageDataPath") is not None:
            self.StorageDataPath = CosPathInfo()
            self.StorageDataPath._deserialize(params.get("StorageDataPath"))
        if params.get("StorageLabelPath") is not None:
            self.StorageLabelPath = CosPathInfo()
            self.StorageLabelPath._deserialize(params.get("StorageLabelPath"))
        if params.get("DatasetVersions") is not None:
            self.DatasetVersions = []
            for item in params.get("DatasetVersions"):
                obj = DatasetInfo()
                obj._deserialize(item)
                self.DatasetVersions.append(obj)
        self.AnnotationStatus = params.get("AnnotationStatus")
        self.AnnotationType = params.get("AnnotationType")
        self.AnnotationFormat = params.get("AnnotationFormat")
        self.DatasetScope = params.get("DatasetScope")
        self.OcrScene = params.get("OcrScene")
        self.AnnotationKeyStatus = params.get("AnnotationKeyStatus")
        self.ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasetInfo(AbstractModel):
    """数据集详情

    """

    def __init__(self):
        r"""
        :param DatasetId: 数据集id
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetId: str
        :param DatasetName: 数据集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetName: str
        :param Creator: 数据集创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type Creator: str
        :param DatasetVersion: 数据集版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetVersion: str
        :param DatasetType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetType: str
        :param DatasetTags: 数据集标签
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetTags: list of Tag
        :param DatasetAnnotationTaskName: 数据集对应标注任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskName: str
        :param DatasetAnnotationTaskId: 数据集对应标注任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetAnnotationTaskId: str
        :param Process: 处理进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Process: int
        :param DatasetStatus: 数据集状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetStatus: str
        :param ErrorMsg: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param CreateTime: 数据集创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 数据集更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ExternalTaskType: 外部任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalTaskType: str
        :param DatasetSize: 数据集存储大小
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetSize: str
        :param FileNum: 数据集数据数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FileNum: int
        :param StorageDataPath: 数据集源cos 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageDataPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param StorageLabelPath: 数据集输出cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLabelPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param AnnotationStatus: 数据集标注状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationStatus: str
        :param AnnotationType: 数据集类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationType: str
        :param AnnotationFormat: 数据集标注格式
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationFormat: str
        :param DatasetScope: 数据集范围
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetScope: str
        :param OcrScene: 数据集OCR子场景
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrScene: str
        :param AnnotationKeyStatus: 数据集字典修改状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotationKeyStatus: str
        """
        self.DatasetId = None
        self.DatasetName = None
        self.Creator = None
        self.DatasetVersion = None
        self.DatasetType = None
        self.DatasetTags = None
        self.DatasetAnnotationTaskName = None
        self.DatasetAnnotationTaskId = None
        self.Process = None
        self.DatasetStatus = None
        self.ErrorMsg = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExternalTaskType = None
        self.DatasetSize = None
        self.FileNum = None
        self.StorageDataPath = None
        self.StorageLabelPath = None
        self.AnnotationStatus = None
        self.AnnotationType = None
        self.AnnotationFormat = None
        self.DatasetScope = None
        self.OcrScene = None
        self.AnnotationKeyStatus = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.DatasetName = params.get("DatasetName")
        self.Creator = params.get("Creator")
        self.DatasetVersion = params.get("DatasetVersion")
        self.DatasetType = params.get("DatasetType")
        if params.get("DatasetTags") is not None:
            self.DatasetTags = []
            for item in params.get("DatasetTags"):
                obj = Tag()
                obj._deserialize(item)
                self.DatasetTags.append(obj)
        self.DatasetAnnotationTaskName = params.get("DatasetAnnotationTaskName")
        self.DatasetAnnotationTaskId = params.get("DatasetAnnotationTaskId")
        self.Process = params.get("Process")
        self.DatasetStatus = params.get("DatasetStatus")
        self.ErrorMsg = params.get("ErrorMsg")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExternalTaskType = params.get("ExternalTaskType")
        self.DatasetSize = params.get("DatasetSize")
        self.FileNum = params.get("FileNum")
        if params.get("StorageDataPath") is not None:
            self.StorageDataPath = CosPathInfo()
            self.StorageDataPath._deserialize(params.get("StorageDataPath"))
        if params.get("StorageLabelPath") is not None:
            self.StorageLabelPath = CosPathInfo()
            self.StorageLabelPath._deserialize(params.get("StorageLabelPath"))
        self.AnnotationStatus = params.get("AnnotationStatus")
        self.AnnotationType = params.get("AnnotationType")
        self.AnnotationFormat = params.get("AnnotationFormat")
        self.DatasetScope = params.get("DatasetScope")
        self.OcrScene = params.get("OcrScene")
        self.AnnotationKeyStatus = params.get("AnnotationKeyStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultNginxGatewayCallInfo(AbstractModel):
    """默认Nginx网关结构

    """

    def __init__(self):
        r"""
        :param Host: host
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        """
        self.Host = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBatchTaskRequest(AbstractModel):
    """DeleteBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        """
        self.BatchTaskId = None


    def _deserialize(self, params):
        self.BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBatchTaskResponse(AbstractModel):
    """DeleteBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDatasetRequest(AbstractModel):
    """DeleteDataset请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasetId: 数据集id
        :type DatasetId: str
        :param DeleteLabelEnable: 是否删除cos标签文件
        :type DeleteLabelEnable: bool
        """
        self.DatasetId = None
        self.DeleteLabelEnable = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.DeleteLabelEnable = params.get("DeleteLabelEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDatasetResponse(AbstractModel):
    """DeleteDataset返回参数结构体

    """

    def __init__(self):
        r"""
        :param DatasetId: 删除的datasetId
        :type DatasetId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DatasetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.RequestId = params.get("RequestId")


class DeleteModelAccelerateTaskRequest(AbstractModel):
    """DeleteModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        """
        self.ModelAccTaskId = None


    def _deserialize(self, params):
        self.ModelAccTaskId = params.get("ModelAccTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelAccelerateTaskResponse(AbstractModel):
    """DeleteModelAccelerateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteModelServiceGroupRequest(AbstractModel):
    """DeleteModelServiceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 服务id
        :type ServiceGroupId: str
        """
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelServiceGroupResponse(AbstractModel):
    """DeleteModelServiceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteModelServiceRequest(AbstractModel):
    """DeleteModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务id
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelServiceResponse(AbstractModel):
    """DeleteModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTrainingModelRequest(AbstractModel):
    """DeleteTrainingModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingModelId: 模型ID
        :type TrainingModelId: str
        :param EnableDeleteCos: 是否同步清理cos
        :type EnableDeleteCos: bool
        :param ModelVersionType: 删除模型类型，枚举值：NORMAL 普通，ACCELERATE 加速，不传则删除所有
        :type ModelVersionType: str
        """
        self.TrainingModelId = None
        self.EnableDeleteCos = None
        self.ModelVersionType = None


    def _deserialize(self, params):
        self.TrainingModelId = params.get("TrainingModelId")
        self.EnableDeleteCos = params.get("EnableDeleteCos")
        self.ModelVersionType = params.get("ModelVersionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrainingModelResponse(AbstractModel):
    """DeleteTrainingModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTrainingModelVersionRequest(AbstractModel):
    """DeleteTrainingModelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingModelVersionId: 模型版本ID
        :type TrainingModelVersionId: str
        :param EnableDeleteCos: 是否同步清理cos
        :type EnableDeleteCos: bool
        """
        self.TrainingModelVersionId = None
        self.EnableDeleteCos = None


    def _deserialize(self, params):
        self.TrainingModelVersionId = params.get("TrainingModelVersionId")
        self.EnableDeleteCos = params.get("EnableDeleteCos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrainingModelVersionResponse(AbstractModel):
    """DeleteTrainingModelVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTrainingTaskRequest(AbstractModel):
    """DeleteTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTrainingTaskResponse(AbstractModel):
    """DeleteTrainingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAPIConfigsRequest(AbstractModel):
    """DescribeAPIConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        :param Filters: 分页参数，支持的分页过滤Name包括：
["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId"]
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIConfigsResponse(AbstractModel):
    """DescribeAPIConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 接口数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Details: 接口详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of APIConfigDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = APIConfigDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBatchTaskInstancesRequest(AbstractModel):
    """DescribeBatchTaskInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskId: 跑批任务id
        :type BatchTaskId: str
        """
        self.BatchTaskId = None


    def _deserialize(self, params):
        self.BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskInstancesResponse(AbstractModel):
    """DescribeBatchTaskInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchInstances: 实例集
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchInstances: list of BatchTaskInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchInstances = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BatchInstances") is not None:
            self.BatchInstances = []
            for item in params.get("BatchInstances"):
                obj = BatchTaskInstance()
                obj._deserialize(item)
                self.BatchInstances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBatchTaskRequest(AbstractModel):
    """DescribeBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        """
        self.BatchTaskId = None


    def _deserialize(self, params):
        self.BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTaskResponse(AbstractModel):
    """DescribeBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskDetail: 跑批任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchTaskDetail: :class:`tencentcloud.tione.v20211111.models.BatchTaskDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchTaskDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BatchTaskDetail") is not None:
            self.BatchTaskDetail = BatchTaskDetail()
            self.BatchTaskDetail._deserialize(params.get("BatchTaskDetail"))
        self.RequestId = params.get("RequestId")


class DescribeBatchTasksRequest(AbstractModel):
    """DescribeBatchTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤器，eg：[{ "Name": "Id", "Values": ["train-23091792777383936"] }]

取值范围：
Name（名称）：task1
Id（task ID）：train-23091792777383936
Status（状态）：STARTING / RUNNING / STOPPING / STOPPED / FAILED / SUCCEED / SUBMIT_FAILED
ChargeType（计费类型）：PREPAID 包年包月 / POSTPAID_BY_HOUR 按量计费
CHARGE_STATUS（计费状态）：NOT_BILLING（未开始计费）/ BILLING（计费中）/ ARREARS_STOP（欠费停止）
        :type Filters: list of Filter
        :param TagFilters: 标签过滤器，eg：[{ "TagKey": "TagKeyA", "TagValue": ["TagValueA"] }]
        :type TagFilters: list of TagFilter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大为50
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC（升序排列）/ DESC（降序排列），默认为DESC
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        """
        self.Filters = None
        self.TagFilters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchTasksResponse(AbstractModel):
    """DescribeBatchTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 数量
        :type TotalCount: int
        :param BatchTaskSet: 任务集
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchTaskSet: list of BatchTaskSetItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BatchTaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BatchTaskSet") is not None:
            self.BatchTaskSet = []
            for item in params.get("BatchTaskSet"):
                obj = BatchTaskSetItem()
                obj._deserialize(item)
                self.BatchTaskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillingResourceGroupsRequest(AbstractModel):
    """DescribeBillingResourceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 资源组类型; 枚举值 TRAIN:训练 INFERENCE:推理
        :type Type: str
        :param Filters: Filter.Name: 枚举值: ResourceGroupId (资源组id列表)
                    ResourceGroupName (资源组名称列表)
Filter.Values: 长度为1且Filter.Fuzzy=true时，支持模糊查询; 不为1时，精确查询
每次请求的Filters的上限为5，Filter.Values的上限为100
        :type Filters: list of Filter
        :param TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        :param Offset: 偏移量，默认为0；分页查询起始位置，如：Limit为100，第一页Offset为0，第二页OffSet为100....即每页左边为闭区间
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为30;
注意：小于0则默认为20；大于30则默认为30
        :type Limit: int
        :param SearchWord: 支持模糊查找资源组id和资源组名
        :type SearchWord: str
        :param DontShowInstanceSet: 是否不展示节点列表; 
true: 不展示，false 展示；
默认为false
        :type DontShowInstanceSet: bool
        """
        self.Type = None
        self.Filters = None
        self.TagFilters = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None
        self.DontShowInstanceSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")
        self.DontShowInstanceSet = params.get("DontShowInstanceSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingResourceGroupsResponse(AbstractModel):
    """DescribeBillingResourceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 资源组总数； 注意接口是分页拉取的，total是指资源组总数，不是本次返回中ResourceGroupSet数组的大小
        :type TotalCount: int
        :param ResourceGroupSet: 资源组详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupSet: list of ResourceGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ResourceGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceGroupSet") is not None:
            self.ResourceGroupSet = []
            for item in params.get("ResourceGroupSet"):
                obj = ResourceGroup()
                obj._deserialize(item)
                self.ResourceGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillingSpecsPriceRequest(AbstractModel):
    """DescribeBillingSpecsPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpecsParam: 询价参数，支持批量询价
        :type SpecsParam: list of SpecUnit
        """
        self.SpecsParam = None


    def _deserialize(self, params):
        if params.get("SpecsParam") is not None:
            self.SpecsParam = []
            for item in params.get("SpecsParam"):
                obj = SpecUnit()
                obj._deserialize(item)
                self.SpecsParam.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingSpecsPriceResponse(AbstractModel):
    """DescribeBillingSpecsPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param SpecsPrice: 计费项价格，支持批量返回
        :type SpecsPrice: list of SpecPrice
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SpecsPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecsPrice") is not None:
            self.SpecsPrice = []
            for item in params.get("SpecsPrice"):
                obj = SpecPrice()
                obj._deserialize(item)
                self.SpecsPrice.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillingSpecsRequest(AbstractModel):
    """DescribeBillingSpecs请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 枚举值：TRAIN、NOTEBOOK、INFERENCE
        :type TaskType: str
        :param ChargeType: 付费模式：POSTPAID_BY_HOUR按量计费、PREPAID包年包月
        :type ChargeType: str
        :param ResourceType: 资源类型：CALC 计算资源、CPU CPU资源、GPU GPU资源、CBS云硬盘
        :type ResourceType: str
        """
        self.TaskType = None
        self.ChargeType = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ChargeType = params.get("ChargeType")
        self.ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingSpecsResponse(AbstractModel):
    """DescribeBillingSpecs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Specs: 计费项列表
        :type Specs: list of Spec
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Specs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Specs") is not None:
            self.Specs = []
            for item in params.get("Specs"):
                obj = Spec()
                obj._deserialize(item)
                self.Specs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatasetDetailStructuredRequest(AbstractModel):
    """DescribeDatasetDetailStructured请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasetId: 数据集ID
        :type DatasetId: str
        :param Offset: 偏移值
        :type Offset: int
        :param Limit: 返回数据条数，默认20，目前最大支持2000条数据
        :type Limit: int
        """
        self.DatasetId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasetDetailStructuredResponse(AbstractModel):
    """DescribeDatasetDetailStructured返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 数据总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ColumnNames: 表格头信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnNames: list of str
        :param RowItems: 表格内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RowItems: list of RowItem
        :param RowTexts: 文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RowTexts: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ColumnNames = None
        self.RowItems = None
        self.RowTexts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.ColumnNames = params.get("ColumnNames")
        if params.get("RowItems") is not None:
            self.RowItems = []
            for item in params.get("RowItems"):
                obj = RowItem()
                obj._deserialize(item)
                self.RowItems.append(obj)
        self.RowTexts = params.get("RowTexts")
        self.RequestId = params.get("RequestId")


class DescribeDatasetDetailUnstructuredRequest(AbstractModel):
    """DescribeDatasetDetailUnstructured请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasetId: 数据集ID
        :type DatasetId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回个数，默认20，目前最大支持2000条数据
        :type Limit: int
        :param LabelList: 标签过滤参数，对应标签值
        :type LabelList: list of str
        :param AnnotationStatus: 标注状态过滤参数:
STATUS_ANNOTATED，已标注
STATUS_NON_ANNOTATED，未标注
STATUS_ALL，全部
默认为STATUS_ALL
        :type AnnotationStatus: str
        :param DatasetIds: 数据集ID列表
        :type DatasetIds: list of str
        :param TextClassificationLabels: 要筛选的文本分类场景标签信息
        :type TextClassificationLabels: list of TextLabelDistributionInfo
        """
        self.DatasetId = None
        self.Offset = None
        self.Limit = None
        self.LabelList = None
        self.AnnotationStatus = None
        self.DatasetIds = None
        self.TextClassificationLabels = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.LabelList = params.get("LabelList")
        self.AnnotationStatus = params.get("AnnotationStatus")
        self.DatasetIds = params.get("DatasetIds")
        if params.get("TextClassificationLabels") is not None:
            self.TextClassificationLabels = []
            for item in params.get("TextClassificationLabels"):
                obj = TextLabelDistributionInfo()
                obj._deserialize(item)
                self.TextClassificationLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasetDetailUnstructuredResponse(AbstractModel):
    """DescribeDatasetDetailUnstructured返回参数结构体

    """

    def __init__(self):
        r"""
        :param AnnotatedTotalCount: 已标注数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type AnnotatedTotalCount: int
        :param NonAnnotatedTotalCount: 没有标注数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type NonAnnotatedTotalCount: int
        :param FilterTotalCount: 过滤数据总量
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterTotalCount: int
        :param FilterLabelList: 过滤数据详情
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterLabelList: list of FilterLabelInfo
        :param RowTexts: 数据文本行，默认返回前1000行
注意：此字段可能返回 null，表示取不到有效值。
        :type RowTexts: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AnnotatedTotalCount = None
        self.NonAnnotatedTotalCount = None
        self.FilterTotalCount = None
        self.FilterLabelList = None
        self.RowTexts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AnnotatedTotalCount = params.get("AnnotatedTotalCount")
        self.NonAnnotatedTotalCount = params.get("NonAnnotatedTotalCount")
        self.FilterTotalCount = params.get("FilterTotalCount")
        if params.get("FilterLabelList") is not None:
            self.FilterLabelList = []
            for item in params.get("FilterLabelList"):
                obj = FilterLabelInfo()
                obj._deserialize(item)
                self.FilterLabelList.append(obj)
        self.RowTexts = params.get("RowTexts")
        self.RequestId = params.get("RequestId")


class DescribeDatasetsRequest(AbstractModel):
    """DescribeDatasets请求参数结构体

    """

    def __init__(self):
        r"""
        :param DatasetIds: 数据集id列表
        :type DatasetIds: list of str
        :param Filters: 数据集查询过滤条件，多个Filter之间的关系为逻辑与（AND）关系，过滤字段Filter.Name，类型为String
DatasetName，数据集名称
DatasetScope，数据集范围，SCOPE_DATASET_PRIVATE或SCOPE_DATASET_PUBLIC
        :type Filters: list of Filter
        :param TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        :param Order: 排序值，支持Asc或Desc，默认Desc
        :type Order: str
        :param OrderField: 排序字段，支持CreateTime或UpdateTime，默认CreateTime
        :type OrderField: str
        :param Offset: 偏移值
        :type Offset: int
        :param Limit: 返回数据个数，默认20，最大支持200
        :type Limit: int
        """
        self.DatasetIds = None
        self.Filters = None
        self.TagFilters = None
        self.Order = None
        self.OrderField = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DatasetIds = params.get("DatasetIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasetsResponse(AbstractModel):
    """DescribeDatasets返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 数据集总量（名称维度）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param DatasetGroups: 数据集按照数据集名称聚合的分组
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetGroups: list of DatasetGroup
        :param DatasetIdNums: 数据集ID总量
注意：此字段可能返回 null，表示取不到有效值。
        :type DatasetIdNums: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DatasetGroups = None
        self.DatasetIdNums = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DatasetGroups") is not None:
            self.DatasetGroups = []
            for item in params.get("DatasetGroups"):
                obj = DatasetGroup()
                obj._deserialize(item)
                self.DatasetGroups.append(obj)
        self.DatasetIdNums = params.get("DatasetIdNums")
        self.RequestId = params.get("RequestId")


class DescribeInferTemplatesRequest(AbstractModel):
    """DescribeInferTemplates请求参数结构体

    """


class DescribeInferTemplatesResponse(AbstractModel):
    """DescribeInferTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param FrameworkTemplates: 模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkTemplates: list of InferTemplateGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrameworkTemplates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FrameworkTemplates") is not None:
            self.FrameworkTemplates = []
            for item in params.get("FrameworkTemplates"):
                obj = InferTemplateGroup()
                obj._deserialize(item)
                self.FrameworkTemplates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLatestTrainingMetricsRequest(AbstractModel):
    """DescribeLatestTrainingMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLatestTrainingMetricsResponse(AbstractModel):
    """DescribeLatestTrainingMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param Metrics: 最近一次上报的训练指标.每个Metric中只有一个点的数据, 即len(Values) = len(Timestamps) = 1
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of TrainingMetric
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Metrics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = TrainingMetric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogsRequest(AbstractModel):
    """DescribeLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Service: 查询哪个服务的事件（可选值为TRAIN, NOTEBOOK, INFER）
        :type Service: str
        :param PodName: 查询哪个Pod的日志（支持结尾通配符*)
        :type PodName: str
        :param StartTime: 日志查询开始时间（RFC3339格式的时间字符串），默认值为当前时间的前一个小时
        :type StartTime: str
        :param EndTime: 日志查询结束时间（RFC3339格式的时间字符串），默认值为当前时间
        :type EndTime: str
        :param Limit: 日志查询条数，默认值100，最大值100
        :type Limit: int
        :param Order: 排序方向（可选值为ASC, DESC ），默认为DESC
        :type Order: str
        :param OrderField: 按哪个字段排序（可选值为Timestamp），默认值为Timestamp
        :type OrderField: str
        :param Context: 日志查询上下文，查询下一页的时候需要回传这个字段，该字段来自本接口的返回
        :type Context: str
        :param Filters: 过滤条件
注意: 
1. Filter.Name：目前只支持Key（也就是按关键字过滤日志）
2. Filter.Values：表示过滤日志的关键字；Values为多个的时候表示同时满足
3. Filter. Negative和Filter. Fuzzy没有使用
        :type Filters: list of Filter
        """
        self.Service = None
        self.PodName = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.Context = None
        self.Filters = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.PodName = params.get("PodName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.Context = params.get("Context")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogsResponse(AbstractModel):
    """DescribeLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Context: 分页的游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Content: 日志数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: list of LogIdentity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = LogIdentity()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModelAccEngineVersionsRequest(AbstractModel):
    """DescribeModelAccEngineVersions请求参数结构体

    """


class DescribeModelAccEngineVersionsResponse(AbstractModel):
    """DescribeModelAccEngineVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccEngineVersions: 模型加速版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccEngineVersions: list of ModelAccEngineVersion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelAccEngineVersions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModelAccEngineVersions") is not None:
            self.ModelAccEngineVersions = []
            for item in params.get("ModelAccEngineVersions"):
                obj = ModelAccEngineVersion()
                obj._deserialize(item)
                self.ModelAccEngineVersions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModelAccelerateTaskRequest(AbstractModel):
    """DescribeModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        """
        self.ModelAccTaskId = None


    def _deserialize(self, params):
        self.ModelAccTaskId = params.get("ModelAccTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelAccelerateTaskResponse(AbstractModel):
    """DescribeModelAccelerateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccelerateTask: 模型加速任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccelerateTask: :class:`tencentcloud.tione.v20211111.models.ModelAccelerateTask`
        :param ModelAccRuntimeInSecond: 模型加速时长，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccRuntimeInSecond: int
        :param ModelAccStartTime: 模型加速任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccStartTime: str
        :param ModelAccEndTime: 模型加速任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccEndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelAccelerateTask = None
        self.ModelAccRuntimeInSecond = None
        self.ModelAccStartTime = None
        self.ModelAccEndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModelAccelerateTask") is not None:
            self.ModelAccelerateTask = ModelAccelerateTask()
            self.ModelAccelerateTask._deserialize(params.get("ModelAccelerateTask"))
        self.ModelAccRuntimeInSecond = params.get("ModelAccRuntimeInSecond")
        self.ModelAccStartTime = params.get("ModelAccStartTime")
        self.ModelAccEndTime = params.get("ModelAccEndTime")
        self.RequestId = params.get("RequestId")


class DescribeModelAccelerateTasksRequest(AbstractModel):
    """DescribeModelAccelerateTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤器
ModelAccTaskName 任务名称
ModelSource 模型来源
        :type Filters: list of Filter
        :param OrderField: 排序字段，默认CreateTime
        :type OrderField: str
        :param Order: 排序方式：ASC/DESC，默认DESC
        :type Order: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回记录条数，默认10
        :type Limit: int
        :param TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        """
        self.Filters = None
        self.OrderField = None
        self.Order = None
        self.Offset = None
        self.Limit = None
        self.TagFilters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelAccelerateTasksResponse(AbstractModel):
    """DescribeModelAccelerateTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccelerateTasks: 模型加速任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccelerateTasks: list of ModelAccelerateTask
        :param TotalCount: 任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelAccelerateTasks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModelAccelerateTasks") is not None:
            self.ModelAccelerateTasks = []
            for item in params.get("ModelAccelerateTasks"):
                obj = ModelAccelerateTask()
                obj._deserialize(item)
                self.ModelAccelerateTasks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeModelServiceCallInfoRequest(AbstractModel):
    """DescribeModelServiceCallInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        """
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceCallInfoResponse(AbstractModel):
    """DescribeModelServiceCallInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceCallInfo: 服务调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCallInfo: :class:`tencentcloud.tione.v20211111.models.ServiceCallInfo`
        :param InferGatewayCallInfo: 升级网关调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InferGatewayCallInfo: :class:`tencentcloud.tione.v20211111.models.InferGatewayCallInfo`
        :param DefaultNginxGatewayCallInfo: 默认nginx网关的调用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultNginxGatewayCallInfo: :class:`tencentcloud.tione.v20211111.models.DefaultNginxGatewayCallInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceCallInfo = None
        self.InferGatewayCallInfo = None
        self.DefaultNginxGatewayCallInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceCallInfo") is not None:
            self.ServiceCallInfo = ServiceCallInfo()
            self.ServiceCallInfo._deserialize(params.get("ServiceCallInfo"))
        if params.get("InferGatewayCallInfo") is not None:
            self.InferGatewayCallInfo = InferGatewayCallInfo()
            self.InferGatewayCallInfo._deserialize(params.get("InferGatewayCallInfo"))
        if params.get("DefaultNginxGatewayCallInfo") is not None:
            self.DefaultNginxGatewayCallInfo = DefaultNginxGatewayCallInfo()
            self.DefaultNginxGatewayCallInfo._deserialize(params.get("DefaultNginxGatewayCallInfo"))
        self.RequestId = params.get("RequestId")


class DescribeModelServiceGroupRequest(AbstractModel):
    """DescribeModelServiceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 服务组ID
        :type ServiceGroupId: str
        """
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceGroupResponse(AbstractModel):
    """DescribeModelServiceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceGroup: 服务组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroup: :class:`tencentcloud.tione.v20211111.models.ServiceGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceGroup") is not None:
            self.ServiceGroup = ServiceGroup()
            self.ServiceGroup._deserialize(params.get("ServiceGroup"))
        self.RequestId = params.get("RequestId")


class DescribeModelServiceGroupsRequest(AbstractModel):
    """DescribeModelServiceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        :param Filters: 分页参数，支持的分页过滤Name包括：
["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId","Status","CreatedBy","ModelVersionId"]
        :type Filters: list of Filter
        :param TagFilters: 标签过滤参数
        :type TagFilters: list of TagFilter
        """
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.Filters = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceGroupsResponse(AbstractModel):
    """DescribeModelServiceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 推理服务组数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ServiceGroups: 服务组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroups: list of ServiceGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceGroups") is not None:
            self.ServiceGroups = []
            for item in params.get("ServiceGroups"):
                obj = ServiceGroup()
                obj._deserialize(item)
                self.ServiceGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModelServiceHistoryRequest(AbstractModel):
    """DescribeModelServiceHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务Id
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceHistoryResponse(AbstractModel):
    """DescribeModelServiceHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 历史版本总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ServiceHistory: 服务版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceHistory: list of ServiceHistory
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceHistory") is not None:
            self.ServiceHistory = []
            for item in params.get("ServiceHistory"):
                obj = ServiceHistory()
                obj._deserialize(item)
                self.ServiceHistory.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModelServiceHotUpdatedRequest(AbstractModel):
    """DescribeModelServiceHotUpdated请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageInfo: 镜像信息，配置服务运行所需的镜像地址等信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param ModelInfo: 模型信息，需要挂载模型时填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param VolumeMount: 挂载信息
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        """
        self.ImageInfo = None
        self.ModelInfo = None
        self.VolumeMount = None


    def _deserialize(self, params):
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("ModelInfo") is not None:
            self.ModelInfo = ModelInfo()
            self.ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("VolumeMount") is not None:
            self.VolumeMount = VolumeMount()
            self.VolumeMount._deserialize(params.get("VolumeMount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceHotUpdatedResponse(AbstractModel):
    """DescribeModelServiceHotUpdated返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeModelServiceRequest(AbstractModel):
    """DescribeModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务id
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceResponse(AbstractModel):
    """DescribeModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Service: 服务信息
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")


class DescribeModelServicesRequest(AbstractModel):
    """DescribeModelServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为20
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        :param Filters: 分页参数，支持的分页过滤Name包括：
["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId","Status","CreatedBy","ModelId"]
        :type Filters: list of Filter
        :param TagFilters: 标签过滤参数
        :type TagFilters: list of TagFilter
        """
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.Filters = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServicesResponse(AbstractModel):
    """DescribeModelServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Services: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of Service
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Services = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Services") is not None:
            self.Services = []
            for item in params.get("Services"):
                obj = Service()
                obj._deserialize(item)
                self.Services.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrainingFrameworksRequest(AbstractModel):
    """DescribeTrainingFrameworks请求参数结构体

    """


class DescribeTrainingFrameworksResponse(AbstractModel):
    """DescribeTrainingFrameworks返回参数结构体

    """

    def __init__(self):
        r"""
        :param FrameworkInfos: 框架信息列表
        :type FrameworkInfos: list of FrameworkInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrameworkInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FrameworkInfos") is not None:
            self.FrameworkInfos = []
            for item in params.get("FrameworkInfos"):
                obj = FrameworkInfo()
                obj._deserialize(item)
                self.FrameworkInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrainingMetricsRequest(AbstractModel):
    """DescribeTrainingMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingMetricsResponse(AbstractModel):
    """DescribeTrainingMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param Data: 训练指标数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CustomTrainingData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CustomTrainingData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrainingModelVersionRequest(AbstractModel):
    """DescribeTrainingModelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingModelVersionId: 模型版本ID
        :type TrainingModelVersionId: str
        """
        self.TrainingModelVersionId = None


    def _deserialize(self, params):
        self.TrainingModelVersionId = params.get("TrainingModelVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingModelVersionResponse(AbstractModel):
    """DescribeTrainingModelVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingModelVersion: 模型版本
        :type TrainingModelVersion: :class:`tencentcloud.tione.v20211111.models.TrainingModelVersionDTO`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrainingModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrainingModelVersion") is not None:
            self.TrainingModelVersion = TrainingModelVersionDTO()
            self.TrainingModelVersion._deserialize(params.get("TrainingModelVersion"))
        self.RequestId = params.get("RequestId")


class DescribeTrainingModelVersionsRequest(AbstractModel):
    """DescribeTrainingModelVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingModelId: 模型ID
        :type TrainingModelId: str
        :param Filters: 过滤条件
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
        self.TrainingModelId = None
        self.Filters = None


    def _deserialize(self, params):
        self.TrainingModelId = params.get("TrainingModelId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingModelVersionsResponse(AbstractModel):
    """DescribeTrainingModelVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingModelVersions: 模型版本列表
        :type TrainingModelVersions: list of TrainingModelVersionDTO
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrainingModelVersions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrainingModelVersions") is not None:
            self.TrainingModelVersions = []
            for item in params.get("TrainingModelVersions"):
                obj = TrainingModelVersionDTO()
                obj._deserialize(item)
                self.TrainingModelVersions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrainingModelsRequest(AbstractModel):
    """DescribeTrainingModels请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤器
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
        :param OrderField: 排序字段，默认CreateTime
        :type OrderField: str
        :param Order: 排序方式，ASC/DESC，默认DESC
        :type Order: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回结果数量
        :type Limit: int
        :param TagFilters: 标签过滤
        :type TagFilters: list of TagFilter
        :param WithModelVersions: 是否同时返回模型版本列表
        :type WithModelVersions: bool
        """
        self.Filters = None
        self.OrderField = None
        self.Order = None
        self.Offset = None
        self.Limit = None
        self.TagFilters = None
        self.WithModelVersions = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.WithModelVersions = params.get("WithModelVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingModelsResponse(AbstractModel):
    """DescribeTrainingModels返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingModels: 模型列表
        :type TrainingModels: list of TrainingModelDTO
        :param TotalCount: 模型总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrainingModels = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrainingModels") is not None:
            self.TrainingModels = []
            for item in params.get("TrainingModels"):
                obj = TrainingModelDTO()
                obj._deserialize(item)
                self.TrainingModels.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrainingTaskPodsRequest(AbstractModel):
    """DescribeTrainingTaskPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingTaskPodsResponse(AbstractModel):
    """DescribeTrainingTaskPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param PodNames: pod名称列表
        :type PodNames: list of str
        :param TotalCount: 数量
        :type TotalCount: int
        :param PodInfoList: pod详细信息
        :type PodInfoList: :class:`tencentcloud.tione.v20211111.models.PodInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PodNames = None
        self.TotalCount = None
        self.PodInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PodNames = params.get("PodNames")
        self.TotalCount = params.get("TotalCount")
        if params.get("PodInfoList") is not None:
            self.PodInfoList = PodInfo()
            self.PodInfoList._deserialize(params.get("PodInfoList"))
        self.RequestId = params.get("RequestId")


class DescribeTrainingTaskRequest(AbstractModel):
    """DescribeTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingTaskResponse(AbstractModel):
    """DescribeTrainingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingTaskDetail: 训练任务详情
        :type TrainingTaskDetail: :class:`tencentcloud.tione.v20211111.models.TrainingTaskDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrainingTaskDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrainingTaskDetail") is not None:
            self.TrainingTaskDetail = TrainingTaskDetail()
            self.TrainingTaskDetail._deserialize(params.get("TrainingTaskDetail"))
        self.RequestId = params.get("RequestId")


class DescribeTrainingTasksRequest(AbstractModel):
    """DescribeTrainingTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤器，eg：[{ "Name": "Id", "Values": ["train-23091792777383936"] }]

取值范围：
Name（名称）：task1
Id（task ID）：train-23091792777383936
Status（状态）：STARTING / RUNNING / STOPPING / STOPPED / FAILED / SUCCEED / SUBMIT_FAILED
ChargeType（计费类型）：PREPAID（预付费）/ POSTPAID_BY_HOUR（后付费）
CHARGE_STATUS（计费状态）：NOT_BILLING（未开始计费）/ BILLING（计费中）/ ARREARS_STOP（欠费停止）
        :type Filters: list of Filter
        :param TagFilters: 标签过滤器，eg：[{ "TagKey": "TagKeyA", "TagValue": ["TagValueA"] }]
        :type TagFilters: list of TagFilter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大为50
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC（升序排列）/ DESC（降序排列），默认为DESC
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CreateTime" "UpdateTime"
        :type OrderField: str
        """
        self.Filters = None
        self.TagFilters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrainingTasksResponse(AbstractModel):
    """DescribeTrainingTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param TrainingTaskSet: 训练任务集
        :type TrainingTaskSet: list of TrainingTaskSetItem
        :param TotalCount: 数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TrainingTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TrainingTaskSet") is not None:
            self.TrainingTaskSet = []
            for item in params.get("TrainingTaskSet"):
                obj = TrainingTaskSetItem()
                obj._deserialize(item)
                self.TrainingTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetectionLabelInfo(AbstractModel):
    """图像检测参数信息

    """

    def __init__(self):
        r"""
        :param Points: 点坐标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of PointInfo
        :param Labels: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param FrameType: 类别
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameType: str
        """
        self.Points = None
        self.Labels = None
        self.FrameType = None


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = PointInfo()
                obj._deserialize(item)
                self.Points.append(obj)
        self.Labels = params.get("Labels")
        self.FrameType = params.get("FrameType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EngineVersion(AbstractModel):
    """引擎版本

    """

    def __init__(self):
        r"""
        :param Version: 引擎版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param Image: 运行镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param IsSupportIntEightQuantization: 是否支持int8量化
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSupportIntEightQuantization: bool
        :param FrameworkVersion: 框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        """
        self.Version = None
        self.Image = None
        self.IsSupportIntEightQuantization = None
        self.FrameworkVersion = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Image = params.get("Image")
        self.IsSupportIntEightQuantization = params.get("IsSupportIntEightQuantization")
        self.FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param Name: 环境变量key
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 环境变量value
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param Name: 过滤字段名称
        :type Name: str
        :param Values: 过滤字段取值
        :type Values: list of str
        :param Negative: 是否开启反向查询
        :type Negative: bool
        :param Fuzzy: 是否开启模糊匹配
        :type Fuzzy: bool
        """
        self.Name = None
        self.Values = None
        self.Negative = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.Negative = params.get("Negative")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterLabelInfo(AbstractModel):
    """图片列表查询结果详情

    """

    def __init__(self):
        r"""
        :param DatasetId: 数据集id
        :type DatasetId: str
        :param FileId: 文件ID
        :type FileId: str
        :param FileName: 文件路径
        :type FileName: str
        :param ClassificationLabels: 分类标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationLabels: list of str
        :param DetectionLabels: 检测标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionLabels: list of DetectionLabelInfo
        :param SegmentationLabels: 分割标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SegmentationLabels: list of SegmentationInfo
        :param RGBPath: RGB 图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :type RGBPath: str
        :param LabelTemplateType: 标签模板类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelTemplateType: str
        :param DownloadUrl: 下载url链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param DownloadThumbnailUrl: 缩略图下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadThumbnailUrl: str
        :param DownloadRGBUrl: 分割结果图片下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadRGBUrl: str
        :param OcrScene: OCR场景
IDENTITY：识别
STRUCTURE：智能结构化
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrScene: str
        :param OcrLabels: OCR场景标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrLabels: list of OcrLabelInfo
        :param OcrLabelInfo: OCR场景标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrLabelInfo: str
        :param TextClassificationLabelList: 文本分类场景标签结果，内容是json结构
注意：此字段可能返回 null，表示取不到有效值。
        :type TextClassificationLabelList: str
        :param RowText: 文本内容，返回50字符
注意：此字段可能返回 null，表示取不到有效值。
        :type RowText: str
        :param ContentOmit: 文本内容是否完全返回
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentOmit: bool
        """
        self.DatasetId = None
        self.FileId = None
        self.FileName = None
        self.ClassificationLabels = None
        self.DetectionLabels = None
        self.SegmentationLabels = None
        self.RGBPath = None
        self.LabelTemplateType = None
        self.DownloadUrl = None
        self.DownloadThumbnailUrl = None
        self.DownloadRGBUrl = None
        self.OcrScene = None
        self.OcrLabels = None
        self.OcrLabelInfo = None
        self.TextClassificationLabelList = None
        self.RowText = None
        self.ContentOmit = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.ClassificationLabels = params.get("ClassificationLabels")
        if params.get("DetectionLabels") is not None:
            self.DetectionLabels = []
            for item in params.get("DetectionLabels"):
                obj = DetectionLabelInfo()
                obj._deserialize(item)
                self.DetectionLabels.append(obj)
        if params.get("SegmentationLabels") is not None:
            self.SegmentationLabels = []
            for item in params.get("SegmentationLabels"):
                obj = SegmentationInfo()
                obj._deserialize(item)
                self.SegmentationLabels.append(obj)
        self.RGBPath = params.get("RGBPath")
        self.LabelTemplateType = params.get("LabelTemplateType")
        self.DownloadUrl = params.get("DownloadUrl")
        self.DownloadThumbnailUrl = params.get("DownloadThumbnailUrl")
        self.DownloadRGBUrl = params.get("DownloadRGBUrl")
        self.OcrScene = params.get("OcrScene")
        if params.get("OcrLabels") is not None:
            self.OcrLabels = []
            for item in params.get("OcrLabels"):
                obj = OcrLabelInfo()
                obj._deserialize(item)
                self.OcrLabels.append(obj)
        self.OcrLabelInfo = params.get("OcrLabelInfo")
        self.TextClassificationLabelList = params.get("TextClassificationLabelList")
        self.RowText = params.get("RowText")
        self.ContentOmit = params.get("ContentOmit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameworkInfo(AbstractModel):
    """框架信息列表

    """

    def __init__(self):
        r"""
        :param Name: 框架名称
        :type Name: str
        :param VersionInfos: 框架版本以及对应的训练模式
        :type VersionInfos: list of FrameworkVersion
        """
        self.Name = None
        self.VersionInfos = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("VersionInfos") is not None:
            self.VersionInfos = []
            for item in params.get("VersionInfos"):
                obj = FrameworkVersion()
                obj._deserialize(item)
                self.VersionInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameworkVersion(AbstractModel):
    """框架版本以及对应的训练模式

    """

    def __init__(self):
        r"""
        :param Version: 框架版本
        :type Version: str
        :param TrainingModes: 训练模式
        :type TrainingModes: list of str
        :param Environment: 框架运行环境
        :type Environment: str
        """
        self.Version = None
        self.TrainingModes = None
        self.Environment = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.TrainingModes = params.get("TrainingModes")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFS(AbstractModel):
    """配置GooseFS参数

    """

    def __init__(self):
        r"""
        :param Id: goosefs实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GpuDetail(AbstractModel):
    """gpu 详情

    """

    def __init__(self):
        r"""
        :param Name: GPU 显卡类型；枚举值: V100 A100 T4
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: GPU 显卡数；单位为1/100卡，比如100代表1卡
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupResource(AbstractModel):
    """资源信息

    """

    def __init__(self):
        r"""
        :param Cpu: CPU核数; 单位为1/1000核，比如100表示0.1核
        :type Cpu: int
        :param Memory: 内存；单位为MB
        :type Memory: int
        :param Gpu: 总卡数；GPUDetail 显卡数之和；单位为1/100卡，比如100代表1卡
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param GpuDetailSet: Gpu详情
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuDetailSet: list of GpuDetail
        """
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.GpuDetailSet = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        if params.get("GpuDetailSet") is not None:
            self.GpuDetailSet = []
            for item in params.get("GpuDetailSet"):
                obj = GpuDetail()
                obj._deserialize(item)
                self.GpuDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HDFSConfig(AbstractModel):
    """HDFS的参数配置

    """

    def __init__(self):
        r"""
        :param Id: 集群实例ID,实例ID形如: emr-xxxxxxxx
        :type Id: str
        :param Path: 路径
        :type Path: str
        """
        self.Id = None
        self.Path = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalPodAutoscaler(AbstractModel):
    """hpa的描述

    """

    def __init__(self):
        r"""
        :param MinReplicas: 最小实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinReplicas: int
        :param MaxReplicas: 最大实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param HpaMetrics: 扩缩容指标
注意：此字段可能返回 null，表示取不到有效值。
        :type HpaMetrics: list of Option
        """
        self.MinReplicas = None
        self.MaxReplicas = None
        self.HpaMetrics = None


    def _deserialize(self, params):
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        if params.get("HpaMetrics") is not None:
            self.HpaMetrics = []
            for item in params.get("HpaMetrics"):
                obj = Option()
                obj._deserialize(item)
                self.HpaMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HyperParameter(AbstractModel):
    """模型专业参数

    """

    def __init__(self):
        r"""
        :param MaxNNZ: 最大nnz数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNNZ: str
        :param SlotNum: slot数
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotNum: str
        :param CpuCachePercentage: gpu cache 使用率
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuCachePercentage: str
        :param GpuCachePercentage: cpu cache 使用率
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuCachePercentage: str
        :param EnableDistributed: 是否开启分布式模式(true/false)
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDistributed: str
        :param MinBlockSizePt: TORCH_SCRIPT、MMDETECTION、DETECTRON2、HUGGINGFACE格式在进行优化时切分子图的最小算子数目，一般无需进行改动，默认为3
注意：此字段可能返回 null，表示取不到有效值。
        :type MinBlockSizePt: str
        :param MinBlockSizeTf: FROZEN_GRAPH、SAVED_MODEL格式在进行优化时切分子图的最小算子数目，一般无需进行改动，默认为10
注意：此字段可能返回 null，表示取不到有效值。
        :type MinBlockSizeTf: str
        :param PipelineArgs: Stable Diffusion 模型优化参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PipelineArgs: str
        """
        self.MaxNNZ = None
        self.SlotNum = None
        self.CpuCachePercentage = None
        self.GpuCachePercentage = None
        self.EnableDistributed = None
        self.MinBlockSizePt = None
        self.MinBlockSizeTf = None
        self.PipelineArgs = None


    def _deserialize(self, params):
        self.MaxNNZ = params.get("MaxNNZ")
        self.SlotNum = params.get("SlotNum")
        self.CpuCachePercentage = params.get("CpuCachePercentage")
        self.GpuCachePercentage = params.get("GpuCachePercentage")
        self.EnableDistributed = params.get("EnableDistributed")
        self.MinBlockSizePt = params.get("MinBlockSizePt")
        self.MinBlockSizeTf = params.get("MinBlockSizeTf")
        self.PipelineArgs = params.get("PipelineArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    """镜像描述信息

    """

    def __init__(self):
        r"""
        :param ImageType: 镜像类型：TCR为腾讯云TCR镜像; CCR为腾讯云TCR个人版镜像，PreSet为平台预置镜像
        :type ImageType: str
        :param ImageUrl: 镜像地址
        :type ImageUrl: str
        :param RegistryRegion: TCR镜像对应的地域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryRegion: str
        :param RegistryId: TCR镜像对应的实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        """
        self.ImageType = None
        self.ImageUrl = None
        self.RegistryRegion = None
        self.RegistryId = None


    def _deserialize(self, params):
        self.ImageType = params.get("ImageType")
        self.ImageUrl = params.get("ImageUrl")
        self.RegistryRegion = params.get("RegistryRegion")
        self.RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferGatewayCallInfo(AbstractModel):
    """服务的调用信息，服务组下唯一

    """

    def __init__(self):
        r"""
        :param VpcHttpAddr: 内网http调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcHttpAddr: str
        :param VpcHttpsAddr: 内网https调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcHttpsAddr: str
        :param VpcGrpcTlsAddr: 内网grpc调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcGrpcTlsAddr: str
        :param VpcId: 可访问的vpcid
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 后端ip对应的子网
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self.VpcHttpAddr = None
        self.VpcHttpsAddr = None
        self.VpcGrpcTlsAddr = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcHttpAddr = params.get("VpcHttpAddr")
        self.VpcHttpsAddr = params.get("VpcHttpsAddr")
        self.VpcGrpcTlsAddr = params.get("VpcGrpcTlsAddr")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferTemplate(AbstractModel):
    """推理镜像详情

    """

    def __init__(self):
        r"""
        :param InferTemplateId: 模板ID
        :type InferTemplateId: str
        :param InferTemplateImage: 模板镜像
        :type InferTemplateImage: str
        """
        self.InferTemplateId = None
        self.InferTemplateImage = None


    def _deserialize(self, params):
        self.InferTemplateId = params.get("InferTemplateId")
        self.InferTemplateImage = params.get("InferTemplateImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferTemplateGroup(AbstractModel):
    """推理镜像组

    """

    def __init__(self):
        r"""
        :param Framework: 算法框架
注意：此字段可能返回 null，表示取不到有效值。
        :type Framework: str
        :param FrameworkVersion: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        :param Groups: 支持的训练框架集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Groups: list of str
        :param InferTemplates: 镜像模板参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InferTemplates: list of InferTemplate
        """
        self.Framework = None
        self.FrameworkVersion = None
        self.Groups = None
        self.InferTemplates = None


    def _deserialize(self, params):
        self.Framework = params.get("Framework")
        self.FrameworkVersion = params.get("FrameworkVersion")
        self.Groups = params.get("Groups")
        if params.get("InferTemplates") is not None:
            self.InferTemplates = []
            for item in params.get("InferTemplates"):
                obj = InferTemplate()
                obj._deserialize(item)
                self.InferTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """资源组节点信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源组节点id
        :type InstanceId: str
        :param UsedResource: 节点已用资源
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedResource: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param TotalResource: 节点总资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalResource: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param InstanceStatus: 节点状态 
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
        :param SubUin: 创建人
        :type SubUin: str
        :param CreateTime: 创建时间: 
注意：北京时间，比如: 2021-12-01 12:00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ExpireTime: 到期时间
注意：北京时间，比如：2021-12-11 12:00:00
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param AutoRenewFlag: 自动续费标识
注意：此字段为枚举值
说明：
NOTIFY_AND_MANUAL_RENEW：手动续费(取消自动续费)且到期通知
NOTIFY_AND_AUTO_RENEW：自动续费且到期通知
DISABLE_NOTIFY_AND_MANUAL_RENEW：手动续费(取消自动续费)且到期不通知
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: str
        :param SpecId: 计费项ID
        :type SpecId: str
        :param SpecAlias: 计费项别名
        :type SpecAlias: str
        """
        self.InstanceId = None
        self.UsedResource = None
        self.TotalResource = None
        self.InstanceStatus = None
        self.SubUin = None
        self.CreateTime = None
        self.ExpireTime = None
        self.AutoRenewFlag = None
        self.SpecId = None
        self.SpecAlias = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("UsedResource") is not None:
            self.UsedResource = ResourceInfo()
            self.UsedResource._deserialize(params.get("UsedResource"))
        if params.get("TotalResource") is not None:
            self.TotalResource = ResourceInfo()
            self.TotalResource._deserialize(params.get("TotalResource"))
        self.InstanceStatus = params.get("InstanceStatus")
        self.SubUin = params.get("SubUin")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SpecId = params.get("SpecId")
        self.SpecAlias = params.get("SpecAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfig(AbstractModel):
    """日志配置

    """

    def __init__(self):
        r"""
        :param LogsetId: 日志需要投递到cls的日志集
注意：此字段可能返回 null，表示取不到有效值。
        :type LogsetId: str
        :param TopicId: 日志需要投递到cls的主题
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        """
        self.LogsetId = None
        self.TopicId = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogIdentity(AbstractModel):
    """单条日志数据结构

    """

    def __init__(self):
        r"""
        :param Id: 单条日志的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Message: 单条日志的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param PodName: 这条日志对应的Pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PodName: str
        :param Timestamp: 日志的时间戳（RFC3339格式的时间字符串）
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        """
        self.Id = None
        self.Message = None
        self.PodName = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Message = params.get("Message")
        self.PodName = params.get("PodName")
        self.Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """指标数据

    """

    def __init__(self):
        r"""
        :param TaskId: 训练任务id
        :type TaskId: str
        :param Timestamp: 时间戳.unix timestamp,单位为秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param Epoch: 本次上报数据所处的训练周期数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Epoch: int
        :param Step: 本次上报数据所处的训练迭代次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Step: int
        :param TotalSteps: 训练停止所需的迭代总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSteps: int
        :param Points: 数据点。数组元素为不同指标的数据。数组长度不超过10。
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of DataPoint
        """
        self.TaskId = None
        self.Timestamp = None
        self.Uin = None
        self.Epoch = None
        self.Step = None
        self.TotalSteps = None
        self.Points = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Timestamp = params.get("Timestamp")
        self.Uin = params.get("Uin")
        self.Epoch = params.get("Epoch")
        self.Step = params.get("Step")
        self.TotalSteps = params.get("TotalSteps")
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = DataPoint()
                obj._deserialize(item)
                self.Points.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelAccEngineVersion(AbstractModel):
    """模型加速引擎版本

    """

    def __init__(self):
        r"""
        :param ModelFormat: 模型格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelFormat: str
        :param EngineVersions: 引擎版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineVersions: list of EngineVersion
        """
        self.ModelFormat = None
        self.EngineVersions = None


    def _deserialize(self, params):
        self.ModelFormat = params.get("ModelFormat")
        if params.get("EngineVersions") is not None:
            self.EngineVersions = []
            for item in params.get("EngineVersions"):
                obj = EngineVersion()
                obj._deserialize(item)
                self.EngineVersions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelAccelerateTask(AbstractModel):
    """模型加速任务

    """

    def __init__(self):
        r"""
        :param ModelAccTaskId: 模型加速任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskId: str
        :param ModelAccTaskName: 模型加速任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskName: str
        :param ModelId: 模型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelId: str
        :param ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param ModelVersion: 模型版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelVersion: str
        :param ModelSource: 模型来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelSource: str
        :param OptimizationLevel: 优化级别
注意：此字段可能返回 null，表示取不到有效值。
        :type OptimizationLevel: str
        :param TaskStatus: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param ModelInputNum: input节点个数
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputNum: int
        :param ModelInputInfos: input节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputInfos: list of ModelInputInfo
        :param GPUType: GPU型号
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUType: str
        :param ChargeType: 计费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param Speedup: 加速比
注意：此字段可能返回 null，表示取不到有效值。
        :type Speedup: str
        :param ModelInputPath: 模型输入cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param ModelOutputPath: 模型输出cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param ErrorMsg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param AlgorithmFramework: 算法框架
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgorithmFramework: str
        :param WaitNumber: 排队个数
注意：此字段可能返回 null，表示取不到有效值。
        :type WaitNumber: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param TaskProgress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskProgress: int
        :param ModelFormat: 模型格式
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelFormat: str
        :param TensorInfos: 模型Tensor信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TensorInfos: list of str
        :param HyperParameter: 模型专业参数
注意：此字段可能返回 null，表示取不到有效值。
        :type HyperParameter: :class:`tencentcloud.tione.v20211111.models.HyperParameter`
        :param AccEngineVersion: 加速引擎版本
注意：此字段可能返回 null，表示取不到有效值。
        :type AccEngineVersion: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param IsSaved: 优化模型是否已保存到模型仓库
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSaved: bool
        :param ModelSignature: SAVED_MODEL保存时配置的签名
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelSignature: str
        :param QATModel: 是否是QAT模型
注意：此字段可能返回 null，表示取不到有效值。
        :type QATModel: bool
        :param FrameworkVersion: 加速引擎对应的框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        """
        self.ModelAccTaskId = None
        self.ModelAccTaskName = None
        self.ModelId = None
        self.ModelName = None
        self.ModelVersion = None
        self.ModelSource = None
        self.OptimizationLevel = None
        self.TaskStatus = None
        self.ModelInputNum = None
        self.ModelInputInfos = None
        self.GPUType = None
        self.ChargeType = None
        self.Speedup = None
        self.ModelInputPath = None
        self.ModelOutputPath = None
        self.ErrorMsg = None
        self.AlgorithmFramework = None
        self.WaitNumber = None
        self.CreateTime = None
        self.TaskProgress = None
        self.ModelFormat = None
        self.TensorInfos = None
        self.HyperParameter = None
        self.AccEngineVersion = None
        self.Tags = None
        self.IsSaved = None
        self.ModelSignature = None
        self.QATModel = None
        self.FrameworkVersion = None


    def _deserialize(self, params):
        self.ModelAccTaskId = params.get("ModelAccTaskId")
        self.ModelAccTaskName = params.get("ModelAccTaskName")
        self.ModelId = params.get("ModelId")
        self.ModelName = params.get("ModelName")
        self.ModelVersion = params.get("ModelVersion")
        self.ModelSource = params.get("ModelSource")
        self.OptimizationLevel = params.get("OptimizationLevel")
        self.TaskStatus = params.get("TaskStatus")
        self.ModelInputNum = params.get("ModelInputNum")
        if params.get("ModelInputInfos") is not None:
            self.ModelInputInfos = []
            for item in params.get("ModelInputInfos"):
                obj = ModelInputInfo()
                obj._deserialize(item)
                self.ModelInputInfos.append(obj)
        self.GPUType = params.get("GPUType")
        self.ChargeType = params.get("ChargeType")
        self.Speedup = params.get("Speedup")
        if params.get("ModelInputPath") is not None:
            self.ModelInputPath = CosPathInfo()
            self.ModelInputPath._deserialize(params.get("ModelInputPath"))
        if params.get("ModelOutputPath") is not None:
            self.ModelOutputPath = CosPathInfo()
            self.ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        self.ErrorMsg = params.get("ErrorMsg")
        self.AlgorithmFramework = params.get("AlgorithmFramework")
        self.WaitNumber = params.get("WaitNumber")
        self.CreateTime = params.get("CreateTime")
        self.TaskProgress = params.get("TaskProgress")
        self.ModelFormat = params.get("ModelFormat")
        self.TensorInfos = params.get("TensorInfos")
        if params.get("HyperParameter") is not None:
            self.HyperParameter = HyperParameter()
            self.HyperParameter._deserialize(params.get("HyperParameter"))
        self.AccEngineVersion = params.get("AccEngineVersion")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.IsSaved = params.get("IsSaved")
        self.ModelSignature = params.get("ModelSignature")
        self.QATModel = params.get("QATModel")
        self.FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInfo(AbstractModel):
    """模型描述信息

    """

    def __init__(self):
        r"""
        :param ModelVersionId: 模型版本id, DescribeTrainingModelVersion查询模型接口时的id
自动学习类型的模型填写自动学习的任务id
        :type ModelVersionId: str
        :param ModelId: 模型id
        :type ModelId: str
        :param ModelName: 模型名
        :type ModelName: str
        :param ModelVersion: 模型版本
        :type ModelVersion: str
        :param ModelSource: 模型来源
        :type ModelSource: str
        :param CosPathInfo: cos路径信息
        :type CosPathInfo: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param AlgorithmFramework: 模型对应的算法框架，预留
注意：此字段可能返回 null，表示取不到有效值。
        :type AlgorithmFramework: str
        :param ModelType: 默认为 NORMAL, 已加速模型: ACCELERATE, 自动学习模型 AUTO_ML
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelType: str
        """
        self.ModelVersionId = None
        self.ModelId = None
        self.ModelName = None
        self.ModelVersion = None
        self.ModelSource = None
        self.CosPathInfo = None
        self.AlgorithmFramework = None
        self.ModelType = None


    def _deserialize(self, params):
        self.ModelVersionId = params.get("ModelVersionId")
        self.ModelId = params.get("ModelId")
        self.ModelName = params.get("ModelName")
        self.ModelVersion = params.get("ModelVersion")
        self.ModelSource = params.get("ModelSource")
        if params.get("CosPathInfo") is not None:
            self.CosPathInfo = CosPathInfo()
            self.CosPathInfo._deserialize(params.get("CosPathInfo"))
        self.AlgorithmFramework = params.get("AlgorithmFramework")
        self.ModelType = params.get("ModelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInputInfo(AbstractModel):
    """模型输入信息

    """

    def __init__(self):
        r"""
        :param ModelInputType: input数据类型
FIXED：固定
RANGE：浮动
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputType: str
        :param ModelInputDimension: input数据尺寸
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInputDimension: list of str
        """
        self.ModelInputType = None
        self.ModelInputDimension = None


    def _deserialize(self, params):
        self.ModelInputType = params.get("ModelInputType")
        self.ModelInputDimension = params.get("ModelInputDimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelServicePartialConfigRequest(AbstractModel):
    """ModifyModelServicePartialConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 在线推理服务Id，需已存在
        :type ServiceId: str
        :param ScheduledAction: 更新后服务不重启，定时停止的配置
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param ServiceLimit: 更新后服务不重启，服务对应限流限频配置
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        """
        self.ServiceId = None
        self.ScheduledAction = None
        self.ServiceLimit = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        if params.get("ScheduledAction") is not None:
            self.ScheduledAction = ScheduledAction()
            self.ScheduledAction._deserialize(params.get("ScheduledAction"))
        if params.get("ServiceLimit") is not None:
            self.ServiceLimit = ServiceLimit()
            self.ServiceLimit._deserialize(params.get("ServiceLimit"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelServicePartialConfigResponse(AbstractModel):
    """ModifyModelServicePartialConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Service: 被修改后的服务配置
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")


class ModifyModelServiceRequest(AbstractModel):
    """ModifyModelService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务id
        :type ServiceId: str
        :param ModelInfo: 模型信息，需要挂载模型时填写
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param ImageInfo: 镜像信息，配置服务运行所需的镜像地址等信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param Env: 环境变量，可选参数，用于配置容器中的环境变量
        :type Env: list of EnvVar
        :param Resources: 资源描述，指定预付费模式下的cpu,mem,gpu等信息，后付费无需填写
        :type Resources: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param InstanceType: 使用DescribeBillingSpecs接口返回的规格列表中的值，或者参考实例列表:
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
        :param ScaleMode: 扩缩容类型 支持：自动 - "AUTO", 手动 - "MANUAL"
        :type ScaleMode: str
        :param Replicas: 实例数量, 不同计费模式和调节模式下对应关系如下
PREPAID 和 POSTPAID_BY_HOUR:
手动调节模式下对应 实例数量
自动调节模式下对应 基于时间的默认策略的实例数量
HYBRID_PAID:
后付费实例手动调节模式下对应 实例数量
后付费实例自动调节模式下对应 时间策略的默认策略的实例数量
        :type Replicas: int
        :param HorizontalPodAutoscaler: 自动伸缩信息
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        :param LogEnable: 是否开启日志投递，开启后需填写配置投递到指定cls
        :type LogEnable: bool
        :param LogConfig: 日志配置，需要投递服务日志到指定cls时填写
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param ServiceAction: 特殊更新行为： "STOP": 停止, "RESUME": 重启, "SCALE": 扩缩容, 存在这些特殊更新行为时，会忽略其他更新字段
        :type ServiceAction: str
        :param ServiceDescription: 服务的描述
        :type ServiceDescription: str
        :param ScaleStrategy: 自动伸缩策略
        :type ScaleStrategy: str
        :param CronScaleJobs: 自动伸缩策略配置 HPA : 通过HPA进行弹性伸缩 CRON 通过定时任务进行伸缩
        :type CronScaleJobs: list of CronScaleJob
        :param HybridBillingPrepaidReplicas: 计费模式[HYBRID_PAID]时生效, 用于标识混合计费模式下的预付费实例数, 若不填则默认为1
        :type HybridBillingPrepaidReplicas: int
        :param ModelHotUpdateEnable: 是否开启模型的热更新。默认不开启
        :type ModelHotUpdateEnable: bool
        :param ScheduledAction: 定时停止配置
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param ServiceLimit: 服务限速限流相关配置
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param VolumeMount: 挂载配置，目前只支持CFS
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        """
        self.ServiceId = None
        self.ModelInfo = None
        self.ImageInfo = None
        self.Env = None
        self.Resources = None
        self.InstanceType = None
        self.ScaleMode = None
        self.Replicas = None
        self.HorizontalPodAutoscaler = None
        self.LogEnable = None
        self.LogConfig = None
        self.ServiceAction = None
        self.ServiceDescription = None
        self.ScaleStrategy = None
        self.CronScaleJobs = None
        self.HybridBillingPrepaidReplicas = None
        self.ModelHotUpdateEnable = None
        self.ScheduledAction = None
        self.ServiceLimit = None
        self.VolumeMount = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        if params.get("ModelInfo") is not None:
            self.ModelInfo = ModelInfo()
            self.ModelInfo._deserialize(params.get("ModelInfo"))
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("Env") is not None:
            self.Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self.Env.append(obj)
        if params.get("Resources") is not None:
            self.Resources = ResourceInfo()
            self.Resources._deserialize(params.get("Resources"))
        self.InstanceType = params.get("InstanceType")
        self.ScaleMode = params.get("ScaleMode")
        self.Replicas = params.get("Replicas")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self.LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self.LogConfig = LogConfig()
            self.LogConfig._deserialize(params.get("LogConfig"))
        self.ServiceAction = params.get("ServiceAction")
        self.ServiceDescription = params.get("ServiceDescription")
        self.ScaleStrategy = params.get("ScaleStrategy")
        if params.get("CronScaleJobs") is not None:
            self.CronScaleJobs = []
            for item in params.get("CronScaleJobs"):
                obj = CronScaleJob()
                obj._deserialize(item)
                self.CronScaleJobs.append(obj)
        self.HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
        self.ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
        if params.get("ScheduledAction") is not None:
            self.ScheduledAction = ScheduledAction()
            self.ScheduledAction._deserialize(params.get("ScheduledAction"))
        if params.get("ServiceLimit") is not None:
            self.ServiceLimit = ServiceLimit()
            self.ServiceLimit._deserialize(params.get("ServiceLimit"))
        if params.get("VolumeMount") is not None:
            self.VolumeMount = VolumeMount()
            self.VolumeMount._deserialize(params.get("VolumeMount"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelServiceResponse(AbstractModel):
    """ModifyModelService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Service: 生成的模型服务
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.tione.v20211111.models.Service`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")


class ModifyServiceGroupWeightsRequest(AbstractModel):
    """ModifyServiceGroupWeights请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        :param Weights: 权重设置
        :type Weights: list of WeightEntry
        """
        self.ServiceGroupId = None
        self.Weights = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        if params.get("Weights") is not None:
            self.Weights = []
            for item in params.get("Weights"):
                obj = WeightEntry()
                obj._deserialize(item)
                self.Weights.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceGroupWeightsResponse(AbstractModel):
    """ModifyServiceGroupWeights返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceGroup: 更新权重后的服务组信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroup: :class:`tencentcloud.tione.v20211111.models.ServiceGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceGroup") is not None:
            self.ServiceGroup = ServiceGroup()
            self.ServiceGroup._deserialize(params.get("ServiceGroup"))
        self.RequestId = params.get("RequestId")


class OcrLabelInfo(AbstractModel):
    """OCR场景标签列表

    """

    def __init__(self):
        r"""
        :param Points: 坐标点围起来的框
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of PointInfo
        :param FrameType: 框的形状：
FRAME_TYPE_RECTANGLE
FRAME_TYPE_POLYGON
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameType: str
        :param Key: 智能结构化：key区域对应的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param KeyId: 智能结构化：上述key的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param Value: 识别：框区域的内容
智能结构化：value区域对应的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param KeyIdsForValue: 智能结构化：value区域所关联的key 区域的keyID的集合
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyIdsForValue: list of str
        :param Direction: key或者value区域内容的方向：
DIRECTION_VERTICAL
DIRECTION_HORIZONTAL
注意：此字段可能返回 null，表示取不到有效值。
        :type Direction: str
        """
        self.Points = None
        self.FrameType = None
        self.Key = None
        self.KeyId = None
        self.Value = None
        self.KeyIdsForValue = None
        self.Direction = None


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = PointInfo()
                obj._deserialize(item)
                self.Points.append(obj)
        self.FrameType = params.get("FrameType")
        self.Key = params.get("Key")
        self.KeyId = params.get("KeyId")
        self.Value = params.get("Value")
        self.KeyIdsForValue = params.get("KeyIdsForValue")
        self.Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Option(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param Name: 指标名
        :type Name: str
        :param Value: 指标值
        :type Value: int
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pod(AbstractModel):
    """Pod信息展示

    """

    def __init__(self):
        r"""
        :param Name: pod名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Uid: pod的唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type Uid: str
        :param ChargeType: 服务付费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param Phase: pod的状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Phase: str
        :param IP: pod的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param CreateTime: pod的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Containers: 容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Containers: :class:`tencentcloud.tione.v20211111.models.Container`
        :param ContainerInfos: 容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerInfos: list of Container
        """
        self.Name = None
        self.Uid = None
        self.ChargeType = None
        self.Phase = None
        self.IP = None
        self.CreateTime = None
        self.Containers = None
        self.ContainerInfos = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.ChargeType = params.get("ChargeType")
        self.Phase = params.get("Phase")
        self.IP = params.get("IP")
        self.CreateTime = params.get("CreateTime")
        if params.get("Containers") is not None:
            self.Containers = Container()
            self.Containers._deserialize(params.get("Containers"))
        if params.get("ContainerInfos") is not None:
            self.ContainerInfos = []
            for item in params.get("ContainerInfos"):
                obj = Container()
                obj._deserialize(item)
                self.ContainerInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodInfo(AbstractModel):
    """任务建模Pod信息

    """

    def __init__(self):
        r"""
        :param Name: pod名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param IP: pod的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        """
        self.Name = None
        self.IP = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IP = params.get("IP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PointInfo(AbstractModel):
    """点信息描述

    """

    def __init__(self):
        r"""
        :param X: X坐标值
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param Y: Y坐标值
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushTrainingMetricsRequest(AbstractModel):
    """PushTrainingMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 指标数据
        :type Data: list of MetricData
        """
        self.Data = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushTrainingMetricsResponse(AbstractModel):
    """PushTrainingMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RDMAConfig(AbstractModel):
    """RDMA配置

    """

    def __init__(self):
        r"""
        :param Enable: 是否开启RDMA
注意：此字段可能返回 null，表示取不到有效值。
        :type Enable: bool
        """
        self.Enable = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConfigInfo(AbstractModel):
    """资源配置

    """

    def __init__(self):
        r"""
        :param Role: 角色，eg：PS、WORKER、DRIVER、EXECUTOR
        :type Role: str
        :param Cpu: cpu核数，1000=1核
        :type Cpu: int
        :param Memory: 内存，单位为MB
        :type Memory: int
        :param GpuType: gpu卡类型
        :type GpuType: str
        :param Gpu: gpu数
        :type Gpu: int
        :param InstanceType: 算力规格ID
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
        :param InstanceNum: 计算节点数
        :type InstanceNum: int
        :param InstanceTypeAlias: 算力规格名称
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
        :param RDMAConfig: RDMA配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RDMAConfig: :class:`tencentcloud.tione.v20211111.models.RDMAConfig`
        """
        self.Role = None
        self.Cpu = None
        self.Memory = None
        self.GpuType = None
        self.Gpu = None
        self.InstanceType = None
        self.InstanceNum = None
        self.InstanceTypeAlias = None
        self.RDMAConfig = None


    def _deserialize(self, params):
        self.Role = params.get("Role")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.GpuType = params.get("GpuType")
        self.Gpu = params.get("Gpu")
        self.InstanceType = params.get("InstanceType")
        self.InstanceNum = params.get("InstanceNum")
        self.InstanceTypeAlias = params.get("InstanceTypeAlias")
        if params.get("RDMAConfig") is not None:
            self.RDMAConfig = RDMAConfig()
            self.RDMAConfig._deserialize(params.get("RDMAConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceGroup(AbstractModel):
    """资源组

    """

    def __init__(self):
        r"""
        :param ResourceGroupId: 资源组id
        :type ResourceGroupId: str
        :param ResourceGroupName: 资源组名称
        :type ResourceGroupName: str
        :param FreeInstance: 可用节点个数(运行中的节点)
        :type FreeInstance: int
        :param TotalInstance: 总节点个数(所有节点)
        :type TotalInstance: int
        :param UsedResource: 资资源组已用的资源
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedResource: :class:`tencentcloud.tione.v20211111.models.GroupResource`
        :param TotalResource: 资源组总资源
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalResource: :class:`tencentcloud.tione.v20211111.models.GroupResource`
        :param InstanceSet: 节点信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of Instance
        :param TagSet: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        """
        self.ResourceGroupId = None
        self.ResourceGroupName = None
        self.FreeInstance = None
        self.TotalInstance = None
        self.UsedResource = None
        self.TotalResource = None
        self.InstanceSet = None
        self.TagSet = None


    def _deserialize(self, params):
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.ResourceGroupName = params.get("ResourceGroupName")
        self.FreeInstance = params.get("FreeInstance")
        self.TotalInstance = params.get("TotalInstance")
        if params.get("UsedResource") is not None:
            self.UsedResource = GroupResource()
            self.UsedResource._deserialize(params.get("UsedResource"))
        if params.get("TotalResource") is not None:
            self.TotalResource = GroupResource()
            self.TotalResource._deserialize(params.get("TotalResource"))
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInfo(AbstractModel):
    """描述资源信息

    """

    def __init__(self):
        r"""
        :param Cpu: 处理器资源, 单位为1/1000核
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Memory: 内存资源, 单位为1M
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param Gpu: Gpu卡个数资源, 单位为0.01单位的GpuType.
Gpu=100表示使用了“一张”gpu卡, 但此处的“一张”卡有可能是虚拟化后的1/4卡, 也有可能是整张卡. 取决于实例的机型
例1 实例的机型带有1张虚拟gpu卡, 每张虚拟gpu卡对应1/4张实际T4卡, 则此时 GpuType=T4, Gpu=100, RealGpu=25.
例2 实例的机型带有4张gpu整卡, 每张卡对应1张实际T4卡, 则 此时 GpuType=T4, Gpu=400, RealGpu=400.
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param GpuType: Gpu卡型号 T4或者V100。仅展示当前 GPU 卡型号，若存在多类型同时使用，则参考 RealGpuDetailSet 的值。
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param RealGpu: 创建或更新时无需填写，仅展示需要关注
后付费非整卡实例对应的实际的Gpu卡资源, 表示gpu资源对应实际的gpu卡个数.
RealGpu=100表示实际使用了一张gpu卡, 对应实际的实例机型, 有可能代表带有1/4卡的实例4个, 或者带有1/2卡的实例2个, 或者带有1卡的实力1个.
        :type RealGpu: int
        :param RealGpuDetailSet: 创建或更新时无需填写，仅展示需要关注。详细的GPU使用信息。
        :type RealGpuDetailSet: list of GpuDetail
        """
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.GpuType = None
        self.RealGpu = None
        self.RealGpuDetailSet = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.GpuType = params.get("GpuType")
        self.RealGpu = params.get("RealGpu")
        if params.get("RealGpuDetailSet") is not None:
            self.RealGpuDetailSet = []
            for item in params.get("RealGpuDetailSet"):
                obj = GpuDetail()
                obj._deserialize(item)
                self.RealGpuDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartModelAccelerateTaskRequest(AbstractModel):
    """RestartModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        :param ModelAccTaskName: 模型加速任务名称
        :type ModelAccTaskName: str
        :param ModelSource: 模型来源（JOB/COS）
        :type ModelSource: str
        :param AlgorithmFramework: 算法框架（废弃）
        :type AlgorithmFramework: str
        :param ModelId: 模型ID
        :type ModelId: str
        :param ModelName: 模型名称
        :type ModelName: str
        :param ModelVersion: 模型版本
        :type ModelVersion: str
        :param ModelInputPath: 模型输入cos路径
        :type ModelInputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param OptimizationLevel: 优化级别（NO_LOSS/FP16/INT8），默认FP16
        :type OptimizationLevel: str
        :param ModelInputNum: input节点个数（废弃）
        :type ModelInputNum: int
        :param ModelInputInfos: input节点信息（废弃）
        :type ModelInputInfos: list of ModelInputInfo
        :param ModelOutputPath: 模型输出cos路径
        :type ModelOutputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param ModelFormat: 模型格式（TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/MMDETECTION/ONNX/HUGGING_FACE）
        :type ModelFormat: str
        :param TensorInfos: 模型Tensor信息
        :type TensorInfos: list of str
        :param GPUType: GPU类型（T4/V100/A10），默认T4
        :type GPUType: str
        :param HyperParameter: 模型专业参数
        :type HyperParameter: :class:`tencentcloud.tione.v20211111.models.HyperParameter`
        :param AccEngineVersion: 加速引擎版本
        :type AccEngineVersion: str
        :param Tags: 标签
        :type Tags: list of Tag
        :param ModelSignature: SavedModel保存时配置的签名
        :type ModelSignature: str
        :param FrameworkVersion: 加速引擎对应的框架版本
        :type FrameworkVersion: str
        """
        self.ModelAccTaskId = None
        self.ModelAccTaskName = None
        self.ModelSource = None
        self.AlgorithmFramework = None
        self.ModelId = None
        self.ModelName = None
        self.ModelVersion = None
        self.ModelInputPath = None
        self.OptimizationLevel = None
        self.ModelInputNum = None
        self.ModelInputInfos = None
        self.ModelOutputPath = None
        self.ModelFormat = None
        self.TensorInfos = None
        self.GPUType = None
        self.HyperParameter = None
        self.AccEngineVersion = None
        self.Tags = None
        self.ModelSignature = None
        self.FrameworkVersion = None


    def _deserialize(self, params):
        self.ModelAccTaskId = params.get("ModelAccTaskId")
        self.ModelAccTaskName = params.get("ModelAccTaskName")
        self.ModelSource = params.get("ModelSource")
        self.AlgorithmFramework = params.get("AlgorithmFramework")
        self.ModelId = params.get("ModelId")
        self.ModelName = params.get("ModelName")
        self.ModelVersion = params.get("ModelVersion")
        if params.get("ModelInputPath") is not None:
            self.ModelInputPath = CosPathInfo()
            self.ModelInputPath._deserialize(params.get("ModelInputPath"))
        self.OptimizationLevel = params.get("OptimizationLevel")
        self.ModelInputNum = params.get("ModelInputNum")
        if params.get("ModelInputInfos") is not None:
            self.ModelInputInfos = []
            for item in params.get("ModelInputInfos"):
                obj = ModelInputInfo()
                obj._deserialize(item)
                self.ModelInputInfos.append(obj)
        if params.get("ModelOutputPath") is not None:
            self.ModelOutputPath = CosPathInfo()
            self.ModelOutputPath._deserialize(params.get("ModelOutputPath"))
        self.ModelFormat = params.get("ModelFormat")
        self.TensorInfos = params.get("TensorInfos")
        self.GPUType = params.get("GPUType")
        if params.get("HyperParameter") is not None:
            self.HyperParameter = HyperParameter()
            self.HyperParameter._deserialize(params.get("HyperParameter"))
        self.AccEngineVersion = params.get("AccEngineVersion")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ModelSignature = params.get("ModelSignature")
        self.FrameworkVersion = params.get("FrameworkVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartModelAccelerateTaskResponse(AbstractModel):
    """RestartModelAccelerateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RowItem(AbstractModel):
    """文本行信息

    """

    def __init__(self):
        r"""
        :param Values: rowValue 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of RowValue
        """
        self.Values = None


    def _deserialize(self, params):
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = RowValue()
                obj._deserialize(item)
                self.Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowValue(AbstractModel):
    """文件行信息

    """

    def __init__(self):
        r"""
        :param Name: 列名
        :type Name: str
        :param Value: 列值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledAction(AbstractModel):
    """定时的事务和行为

    """

    def __init__(self):
        r"""
        :param ScheduleStop: 是否要定时停止服务，true or false。true 则 ScheduleStopTime 必填， false 则 ScheduleStopTime 不生效
        :type ScheduleStop: bool
        :param ScheduleStopTime: 要执行定时停止的时间，格式：“2022-01-26T19:46:22+08:00”
        :type ScheduleStopTime: str
        """
        self.ScheduleStop = None
        self.ScheduleStopTime = None


    def _deserialize(self, params):
        self.ScheduleStop = params.get("ScheduleStop")
        self.ScheduleStopTime = params.get("ScheduleStopTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemaInfo(AbstractModel):
    """表格数据集表头信息

    """

    def __init__(self):
        r"""
        :param Name: 长度30字符内
        :type Name: str
        :param Type: 数据类型
        :type Type: str
        """
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentationInfo(AbstractModel):
    """图片分割参数信息

    """

    def __init__(self):
        r"""
        :param Points: 点坐标数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Points: list of PointInfo
        :param Label: 分割标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Gray: 灰度值
注意：此字段可能返回 null，表示取不到有效值。
        :type Gray: int
        :param Color: 颜色
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: str
        """
        self.Points = None
        self.Label = None
        self.Gray = None
        self.Color = None


    def _deserialize(self, params):
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = PointInfo()
                obj._deserialize(item)
                self.Points.append(obj)
        self.Label = params.get("Label")
        self.Gray = params.get("Gray")
        self.Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """描述在线服务

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        :param ServiceId: 服务id
        :type ServiceId: str
        :param ServiceGroupName: 服务组名
        :type ServiceGroupName: str
        :param ServiceDescription: 服务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDescription: str
        :param ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param ChargeType: 付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param ResourceGroupId: 包年包月服务的资源组id，按量计费的服务为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param CreatedBy: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedBy: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Uin: 主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param SubUin: 子账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubUin: str
        :param AppId: app_id
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param Version: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param LatestVersion: 服务组下服务的最高版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersion: str
        :param ServiceInfo: 服务的详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceInfo: :class:`tencentcloud.tione.v20211111.models.ServiceInfo`
        :param BusinessStatus: 服务的业务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessStatus: str
        :param CreateSource: 服务的创建来源
AUTO_ML: 来自自动学习的一键发布
DEFAULT: 其他来源
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateSource: str
        :param BillingInfo: 费用信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param Status: 服务状态
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
        :param Weight: 模型权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param IngressName: 服务所在的 ingress 的 name
注意：此字段可能返回 null，表示取不到有效值。
        :type IngressName: str
        :param ServiceLimit: 服务限速限流相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param ScheduledAction: 定时停止的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param CreateFailedReason: 服务创建失败的原因，创建成功后该字段为默认值 CREATE_SUCCEED
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateFailedReason: str
        :param ResourceGroupName: 包年包月服务对应的资源组名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param Tags: 服务的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.ServiceGroupId = None
        self.ServiceId = None
        self.ServiceGroupName = None
        self.ServiceDescription = None
        self.ClusterId = None
        self.Region = None
        self.Namespace = None
        self.ChargeType = None
        self.ResourceGroupId = None
        self.CreatedBy = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Uin = None
        self.SubUin = None
        self.AppId = None
        self.Version = None
        self.LatestVersion = None
        self.ServiceInfo = None
        self.BusinessStatus = None
        self.CreateSource = None
        self.BillingInfo = None
        self.Status = None
        self.Weight = None
        self.IngressName = None
        self.ServiceLimit = None
        self.ScheduledAction = None
        self.CreateFailedReason = None
        self.ResourceGroupName = None
        self.Tags = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        self.ServiceId = params.get("ServiceId")
        self.ServiceGroupName = params.get("ServiceGroupName")
        self.ServiceDescription = params.get("ServiceDescription")
        self.ClusterId = params.get("ClusterId")
        self.Region = params.get("Region")
        self.Namespace = params.get("Namespace")
        self.ChargeType = params.get("ChargeType")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.CreatedBy = params.get("CreatedBy")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Uin = params.get("Uin")
        self.SubUin = params.get("SubUin")
        self.AppId = params.get("AppId")
        self.Version = params.get("Version")
        self.LatestVersion = params.get("LatestVersion")
        if params.get("ServiceInfo") is not None:
            self.ServiceInfo = ServiceInfo()
            self.ServiceInfo._deserialize(params.get("ServiceInfo"))
        self.BusinessStatus = params.get("BusinessStatus")
        self.CreateSource = params.get("CreateSource")
        self.BillingInfo = params.get("BillingInfo")
        self.Status = params.get("Status")
        self.Weight = params.get("Weight")
        self.IngressName = params.get("IngressName")
        if params.get("ServiceLimit") is not None:
            self.ServiceLimit = ServiceLimit()
            self.ServiceLimit._deserialize(params.get("ServiceLimit"))
        if params.get("ScheduledAction") is not None:
            self.ScheduledAction = ScheduledAction()
            self.ScheduledAction._deserialize(params.get("ScheduledAction"))
        self.CreateFailedReason = params.get("CreateFailedReason")
        self.ResourceGroupName = params.get("ResourceGroupName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceCallInfo(AbstractModel):
    """服务的调用信息，服务组下唯一

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 服务组id
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGroupId: str
        :param InnerHttpAddr: 内网http调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpAddr: str
        :param InnerHttpsAddr: 内网https调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpsAddr: str
        :param OuterHttpAddr: 内网http调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type OuterHttpAddr: str
        :param OuterHttpsAddr: 内网https调用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type OuterHttpsAddr: str
        :param AppKey: 调用key
注意：此字段可能返回 null，表示取不到有效值。
        :type AppKey: str
        :param AppSecret: 调用secret
注意：此字段可能返回 null，表示取不到有效值。
        :type AppSecret: str
        """
        self.ServiceGroupId = None
        self.InnerHttpAddr = None
        self.InnerHttpsAddr = None
        self.OuterHttpAddr = None
        self.OuterHttpsAddr = None
        self.AppKey = None
        self.AppSecret = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        self.InnerHttpAddr = params.get("InnerHttpAddr")
        self.InnerHttpsAddr = params.get("InnerHttpsAddr")
        self.OuterHttpAddr = params.get("OuterHttpAddr")
        self.OuterHttpsAddr = params.get("OuterHttpsAddr")
        self.AppKey = params.get("AppKey")
        self.AppSecret = params.get("AppSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGroup(AbstractModel):
    """在线服务一个服务组的信息

    """

    def __init__(self):
        r"""
        :param ServiceGroupId: 服务组id
        :type ServiceGroupId: str
        :param ServiceGroupName: 服务组名
        :type ServiceGroupName: str
        :param CreatedBy: 创建者
        :type CreatedBy: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Uin: 主账号
        :type Uin: str
        :param ServiceCount: 服务组下服务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param RunningServiceCount: 服务组下在运行的服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningServiceCount: int
        :param Services: 服务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Services: list of Service
        :param Status: 服务组状态，与服务一致
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
        :param Tags: 服务组标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param LatestVersion: 服务组下最高版本
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersion: str
        :param BusinessStatus: 服务的业务状态
CREATING 创建中
     CREATE_FAILED 创建失败
     ARREARS_STOP 因欠费被强制停止
     BILLING 计费中
     WHITELIST_USING 白名单试用中
     WHITELIST_STOP 白名单额度不足
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessStatus: str
        :param BillingInfo: 服务的计费信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param CreateSource: 服务的创建来源
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateSource: str
        :param WeightUpdateStatus: 服务组的权重更新状态 
UPDATING 更新中
     UPDATED 更新成功
     UPDATE_FAILED 更新失败
注意：此字段可能返回 null，表示取不到有效值。
        :type WeightUpdateStatus: str
        """
        self.ServiceGroupId = None
        self.ServiceGroupName = None
        self.CreatedBy = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Uin = None
        self.ServiceCount = None
        self.RunningServiceCount = None
        self.Services = None
        self.Status = None
        self.Tags = None
        self.LatestVersion = None
        self.BusinessStatus = None
        self.BillingInfo = None
        self.CreateSource = None
        self.WeightUpdateStatus = None


    def _deserialize(self, params):
        self.ServiceGroupId = params.get("ServiceGroupId")
        self.ServiceGroupName = params.get("ServiceGroupName")
        self.CreatedBy = params.get("CreatedBy")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Uin = params.get("Uin")
        self.ServiceCount = params.get("ServiceCount")
        self.RunningServiceCount = params.get("RunningServiceCount")
        if params.get("Services") is not None:
            self.Services = []
            for item in params.get("Services"):
                obj = Service()
                obj._deserialize(item)
                self.Services.append(obj)
        self.Status = params.get("Status")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.LatestVersion = params.get("LatestVersion")
        self.BusinessStatus = params.get("BusinessStatus")
        self.BillingInfo = params.get("BillingInfo")
        self.CreateSource = params.get("CreateSource")
        self.WeightUpdateStatus = params.get("WeightUpdateStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceHistory(AbstractModel):
    """服务历史版本

    """

    def __init__(self):
        r"""
        :param Revision: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Revision: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Image: 镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param ModelFile: 模型文件
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelFile: str
        :param RawData: 原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :type RawData: str
        """
        self.Revision = None
        self.UpdateTime = None
        self.Image = None
        self.ModelFile = None
        self.RawData = None


    def _deserialize(self, params):
        self.Revision = params.get("Revision")
        self.UpdateTime = params.get("UpdateTime")
        self.Image = params.get("Image")
        self.ModelFile = params.get("ModelFile")
        self.RawData = params.get("RawData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    """推理服务在集群中的信息

    """

    def __init__(self):
        r"""
        :param Replicas: 期望运行的Pod数量，停止状态是0
不同计费模式和调节模式下对应关系如下
PREPAID 和 POSTPAID_BY_HOUR:
手动调节模式下对应 实例数量
自动调节模式下对应 基于时间的默认策略的实例数量
HYBRID_PAID:
后付费实例手动调节模式下对应 实例数量
后付费实例自动调节模式下对应 时间策略的默认策略的实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param ImageInfo: 镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param Env: 环境变量
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: list of EnvVar
        :param Resources: 资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param InstanceType: 后付费实例对应的机型规格
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param ModelInfo: 模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param LogEnable: 是否启用日志
注意：此字段可能返回 null，表示取不到有效值。
        :type LogEnable: bool
        :param LogConfig: 日志配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param AuthorizationEnable: 是否开启鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationEnable: bool
        :param HorizontalPodAutoscaler: hpa配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        :param Status: 服务的状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.tione.v20211111.models.WorkloadStatus`
        :param Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param PodList: 实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodList: list of str
        :param ResourceTotal: 资源总量
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTotal: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param OldReplicas: 历史实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type OldReplicas: int
        :param HybridBillingPrepaidReplicas: 计费模式[HYBRID_PAID]时生效, 用于标识混合计费模式下的预付费实例数, 若不填则默认为1
注意：此字段可能返回 null，表示取不到有效值。
        :type HybridBillingPrepaidReplicas: int
        :param OldHybridBillingPrepaidReplicas: 历史 HYBRID_PAID 时的实例数，用户恢复服务
注意：此字段可能返回 null，表示取不到有效值。
        :type OldHybridBillingPrepaidReplicas: int
        :param ModelHotUpdateEnable: 是否开启模型的热更新。默认不开启
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelHotUpdateEnable: bool
        :param Pods: Pod列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Pods: :class:`tencentcloud.tione.v20211111.models.Pod`
        :param PodInfos: Pod列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodInfos: list of Pod
        :param ScaleStrategy: 定时伸缩策略
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleStrategy: str
        :param CronScaleJobs: 定时伸缩任务
注意：此字段可能返回 null，表示取不到有效值。
        :type CronScaleJobs: list of CronScaleJob
        :param ScaleMode: 实例数量调节方式,默认为手动
支持：自动 - "AUTO", 手动 - "MANUAL"
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleMode: str
        :param ServiceLimit: 服务限速限流相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param ScheduledAction: 定时停止的配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScheduledAction: str
        """
        self.Replicas = None
        self.ImageInfo = None
        self.Env = None
        self.Resources = None
        self.InstanceType = None
        self.ModelInfo = None
        self.LogEnable = None
        self.LogConfig = None
        self.AuthorizationEnable = None
        self.HorizontalPodAutoscaler = None
        self.Status = None
        self.Weight = None
        self.PodList = None
        self.ResourceTotal = None
        self.OldReplicas = None
        self.HybridBillingPrepaidReplicas = None
        self.OldHybridBillingPrepaidReplicas = None
        self.ModelHotUpdateEnable = None
        self.Pods = None
        self.PodInfos = None
        self.ScaleStrategy = None
        self.CronScaleJobs = None
        self.ScaleMode = None
        self.ServiceLimit = None
        self.ScheduledAction = None


    def _deserialize(self, params):
        self.Replicas = params.get("Replicas")
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("Env") is not None:
            self.Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self.Env.append(obj)
        if params.get("Resources") is not None:
            self.Resources = ResourceInfo()
            self.Resources._deserialize(params.get("Resources"))
        self.InstanceType = params.get("InstanceType")
        if params.get("ModelInfo") is not None:
            self.ModelInfo = ModelInfo()
            self.ModelInfo._deserialize(params.get("ModelInfo"))
        self.LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self.LogConfig = LogConfig()
            self.LogConfig._deserialize(params.get("LogConfig"))
        self.AuthorizationEnable = params.get("AuthorizationEnable")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("Status") is not None:
            self.Status = WorkloadStatus()
            self.Status._deserialize(params.get("Status"))
        self.Weight = params.get("Weight")
        self.PodList = params.get("PodList")
        if params.get("ResourceTotal") is not None:
            self.ResourceTotal = ResourceInfo()
            self.ResourceTotal._deserialize(params.get("ResourceTotal"))
        self.OldReplicas = params.get("OldReplicas")
        self.HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
        self.OldHybridBillingPrepaidReplicas = params.get("OldHybridBillingPrepaidReplicas")
        self.ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
        if params.get("Pods") is not None:
            self.Pods = Pod()
            self.Pods._deserialize(params.get("Pods"))
        if params.get("PodInfos") is not None:
            self.PodInfos = []
            for item in params.get("PodInfos"):
                obj = Pod()
                obj._deserialize(item)
                self.PodInfos.append(obj)
        self.ScaleStrategy = params.get("ScaleStrategy")
        if params.get("CronScaleJobs") is not None:
            self.CronScaleJobs = []
            for item in params.get("CronScaleJobs"):
                obj = CronScaleJob()
                obj._deserialize(item)
                self.CronScaleJobs.append(obj)
        self.ScaleMode = params.get("ScaleMode")
        if params.get("ServiceLimit") is not None:
            self.ServiceLimit = ServiceLimit()
            self.ServiceLimit._deserialize(params.get("ServiceLimit"))
        self.ScheduledAction = params.get("ScheduledAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceLimit(AbstractModel):
    """服务的限流限速等配置

    """

    def __init__(self):
        r"""
        :param EnableInstanceRpsLimit: 是否开启实例层面限流限速，true or false。true 则 InstanceRpsLimit 必填， false 则 InstanceRpsLimit 不生效
        :type EnableInstanceRpsLimit: bool
        :param InstanceRpsLimit: 每个服务实例的 request per second 限速, 0 为不限流
        :type InstanceRpsLimit: int
        """
        self.EnableInstanceRpsLimit = None
        self.InstanceRpsLimit = None


    def _deserialize(self, params):
        self.EnableInstanceRpsLimit = params.get("EnableInstanceRpsLimit")
        self.InstanceRpsLimit = params.get("InstanceRpsLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Spec(AbstractModel):
    """计费项内容

    """

    def __init__(self):
        r"""
        :param SpecId: 计费项标签
        :type SpecId: str
        :param SpecName: 计费项名称
        :type SpecName: str
        :param SpecAlias: 计费项显示名称
        :type SpecAlias: str
        :param Available: 是否售罄
        :type Available: bool
        :param AvailableRegion: 当前资源售罄时，可用的区域有哪些
        :type AvailableRegion: list of str
        """
        self.SpecId = None
        self.SpecName = None
        self.SpecAlias = None
        self.Available = None
        self.AvailableRegion = None


    def _deserialize(self, params):
        self.SpecId = params.get("SpecId")
        self.SpecName = params.get("SpecName")
        self.SpecAlias = params.get("SpecAlias")
        self.Available = params.get("Available")
        self.AvailableRegion = params.get("AvailableRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecPrice(AbstractModel):
    """计费项询价结果

    """

    def __init__(self):
        r"""
        :param SpecName: 计费项名称
        :type SpecName: str
        :param TotalCost: 原价，单位：分。最大值42亿，超过则返回0
        :type TotalCost: int
        :param RealTotalCost: 优惠后的价格，单位：分
        :type RealTotalCost: int
        :param SpecCount: 计费项数量
        :type SpecCount: int
        """
        self.SpecName = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.SpecCount = None


    def _deserialize(self, params):
        self.SpecName = params.get("SpecName")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.SpecCount = params.get("SpecCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecUnit(AbstractModel):
    """计费项询价单元

    """

    def __init__(self):
        r"""
        :param SpecName: 计费项名称
        :type SpecName: str
        :param SpecCount: 计费项数量,建议不超过100万
        :type SpecCount: int
        """
        self.SpecName = None
        self.SpecCount = None


    def _deserialize(self, params):
        self.SpecName = params.get("SpecName")
        self.SpecCount = params.get("SpecCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCmdInfo(AbstractModel):
    """启动命令信息

    """

    def __init__(self):
        r"""
        :param StartCmd: 启动命令
        :type StartCmd: str
        :param PsStartCmd: ps启动命令
        :type PsStartCmd: str
        :param WorkerStartCmd: worker启动命令
        :type WorkerStartCmd: str
        """
        self.StartCmd = None
        self.PsStartCmd = None
        self.WorkerStartCmd = None


    def _deserialize(self, params):
        self.StartCmd = params.get("StartCmd")
        self.PsStartCmd = params.get("PsStartCmd")
        self.WorkerStartCmd = params.get("WorkerStartCmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartTrainingTaskRequest(AbstractModel):
    """StartTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartTrainingTaskResponse(AbstractModel):
    """StartTrainingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StatefulSetCondition(AbstractModel):
    """实例状况

    """

    def __init__(self):
        r"""
        :param Message: 信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param Status: Status of the condition, one of True, False, Unknown.
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param LastTransitionTime: 上次更新的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTransitionTime: str
        """
        self.Message = None
        self.Reason = None
        self.Status = None
        self.Type = None
        self.LastTransitionTime = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Reason = params.get("Reason")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.LastTransitionTime = params.get("LastTransitionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopBatchTaskRequest(AbstractModel):
    """StopBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskId: 跑批任务ID
        :type BatchTaskId: str
        """
        self.BatchTaskId = None


    def _deserialize(self, params):
        self.BatchTaskId = params.get("BatchTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopBatchTaskResponse(AbstractModel):
    """StopBatchTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopModelAccelerateTaskRequest(AbstractModel):
    """StopModelAccelerateTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskId: 模型加速任务ID
        :type ModelAccTaskId: str
        """
        self.ModelAccTaskId = None


    def _deserialize(self, params):
        self.ModelAccTaskId = params.get("ModelAccTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopModelAccelerateTaskResponse(AbstractModel):
    """StopModelAccelerateTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param ModelAccTaskId: 模型加速任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAccTaskId: str
        :param AsyncTaskId: 异步任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ModelAccTaskId = None
        self.AsyncTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelAccTaskId = params.get("ModelAccTaskId")
        self.AsyncTaskId = params.get("AsyncTaskId")
        self.RequestId = params.get("RequestId")


class StopTrainingTaskRequest(AbstractModel):
    """StopTrainingTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopTrainingTaskResponse(AbstractModel):
    """StopTrainingTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """描述腾讯云标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """Tag过滤参数

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValues: 多个标签值
        :type TagValues: list of str
        """
        self.TagKey = None
        self.TagValues = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoFifthClass(AbstractModel):
    """五级标签

    """

    def __init__(self):
        r"""
        :param LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        """
        self.LabelValue = None
        self.LabelCount = None
        self.LabelPercentage = None


    def _deserialize(self, params):
        self.LabelValue = params.get("LabelValue")
        self.LabelCount = params.get("LabelCount")
        self.LabelPercentage = params.get("LabelPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoFirstClass(AbstractModel):
    """一级标签

    """

    def __init__(self):
        r"""
        :param LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoSecondClass
        """
        self.LabelValue = None
        self.LabelCount = None
        self.LabelPercentage = None
        self.ChildLabelList = None


    def _deserialize(self, params):
        self.LabelValue = params.get("LabelValue")
        self.LabelCount = params.get("LabelCount")
        self.LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self.ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoSecondClass()
                obj._deserialize(item)
                self.ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoFourthClass(AbstractModel):
    """四级标签

    """

    def __init__(self):
        r"""
        :param LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoFifthClass
        """
        self.LabelValue = None
        self.LabelCount = None
        self.LabelPercentage = None
        self.ChildLabelList = None


    def _deserialize(self, params):
        self.LabelValue = params.get("LabelValue")
        self.LabelCount = params.get("LabelCount")
        self.LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self.ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoFifthClass()
                obj._deserialize(item)
                self.ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoSecondClass(AbstractModel):
    """二级标签

    """

    def __init__(self):
        r"""
        :param LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoThirdClass
        """
        self.LabelValue = None
        self.LabelCount = None
        self.LabelPercentage = None
        self.ChildLabelList = None


    def _deserialize(self, params):
        self.LabelValue = params.get("LabelValue")
        self.LabelCount = params.get("LabelCount")
        self.LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self.ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoThirdClass()
                obj._deserialize(item)
                self.ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionDetailInfoThirdClass(AbstractModel):
    """三级标签

    """

    def __init__(self):
        r"""
        :param LabelValue: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelValue: str
        :param LabelCount: 标签个数
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelCount: int
        :param LabelPercentage: 标签占比
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelPercentage: float
        :param ChildLabelList: 子标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildLabelList: list of TextLabelDistributionDetailInfoFourthClass
        """
        self.LabelValue = None
        self.LabelCount = None
        self.LabelPercentage = None
        self.ChildLabelList = None


    def _deserialize(self, params):
        self.LabelValue = params.get("LabelValue")
        self.LabelCount = params.get("LabelCount")
        self.LabelPercentage = params.get("LabelPercentage")
        if params.get("ChildLabelList") is not None:
            self.ChildLabelList = []
            for item in params.get("ChildLabelList"):
                obj = TextLabelDistributionDetailInfoFourthClass()
                obj._deserialize(item)
                self.ChildLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextLabelDistributionInfo(AbstractModel):
    """文本标签

    """

    def __init__(self):
        r"""
        :param Theme: 文本分类题目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Theme: str
        :param ClassLabelList: 一级标签分布
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassLabelList: list of TextLabelDistributionDetailInfoFirstClass
        """
        self.Theme = None
        self.ClassLabelList = None


    def _deserialize(self, params):
        self.Theme = params.get("Theme")
        if params.get("ClassLabelList") is not None:
            self.ClassLabelList = []
            for item in params.get("ClassLabelList"):
                obj = TextLabelDistributionDetailInfoFirstClass()
                obj._deserialize(item)
                self.ClassLabelList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param MetricName: 指标名
        :type MetricName: str
        :param Values: 数据值
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of TrainingDataPoint
        :param Epochs: 上报的Epoch. 可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Epochs: list of TrainingDataPoint
        :param Steps: 上报的Step. 可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Steps: list of TrainingDataPoint
        :param TotalSteps: 上报的TotalSteps. 可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalSteps: list of TrainingDataPoint
        """
        self.MetricName = None
        self.Values = None
        self.Epochs = None
        self.Steps = None
        self.TotalSteps = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self.Values.append(obj)
        if params.get("Epochs") is not None:
            self.Epochs = []
            for item in params.get("Epochs"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self.Epochs.append(obj)
        if params.get("Steps") is not None:
            self.Steps = []
            for item in params.get("Steps"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self.Steps.append(obj)
        if params.get("TotalSteps") is not None:
            self.TotalSteps = []
            for item in params.get("TotalSteps"):
                obj = TrainingDataPoint()
                obj._deserialize(item)
                self.TotalSteps.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingModelDTO(AbstractModel):
    """模型列表

    """

    def __init__(self):
        r"""
        :param TrainingModelId: 模型id
        :type TrainingModelId: str
        :param TrainingModelName: 模型名称
        :type TrainingModelName: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param CreateTime: 模型创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param TrainingModelVersions: 模型版本列表。默认不返回，仅在指定请求参数开启时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelVersions: list of TrainingModelVersionDTO
        """
        self.TrainingModelId = None
        self.TrainingModelName = None
        self.Tags = None
        self.CreateTime = None
        self.TrainingModelVersions = None


    def _deserialize(self, params):
        self.TrainingModelId = params.get("TrainingModelId")
        self.TrainingModelName = params.get("TrainingModelName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CreateTime = params.get("CreateTime")
        if params.get("TrainingModelVersions") is not None:
            self.TrainingModelVersions = []
            for item in params.get("TrainingModelVersions"):
                obj = TrainingModelVersionDTO()
                obj._deserialize(item)
                self.TrainingModelVersions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingModelVersionDTO(AbstractModel):
    """模型版本列表

    """

    def __init__(self):
        r"""
        :param TrainingModelId: 模型id
        :type TrainingModelId: str
        :param TrainingModelVersionId: 模型版本id
        :type TrainingModelVersionId: str
        :param TrainingModelVersion: 模型版本
        :type TrainingModelVersion: str
        :param TrainingModelSource: 模型来源
        :type TrainingModelSource: str
        :param TrainingModelCreateTime: 创建时间
        :type TrainingModelCreateTime: str
        :param TrainingModelCreator: 创建人uin
        :type TrainingModelCreator: str
        :param AlgorithmFramework: 算法框架
        :type AlgorithmFramework: str
        :param ReasoningEnvironment: 推理环境
        :type ReasoningEnvironment: str
        :param ReasoningEnvironmentSource: 推理环境来源
        :type ReasoningEnvironmentSource: str
        :param TrainingModelIndex: 模型指标
        :type TrainingModelIndex: str
        :param TrainingJobName: 训练任务名称
        :type TrainingJobName: str
        :param TrainingModelCosPath: 模型cos路径
        :type TrainingModelCosPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param TrainingModelName: 模型名称
        :type TrainingModelName: str
        :param TrainingJobId: 训练任务id
        :type TrainingJobId: str
        :param ReasoningImageInfo: 自定义推理环境
        :type ReasoningImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param CreateTime: 模型版本创建时间
        :type CreateTime: str
        :param TrainingModelStatus: 模型处理状态
STATUS_SUCCESS：导入成功，STATUS_FAILED：导入失败 ，STATUS_RUNNING：导入中
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelStatus: str
        :param TrainingModelProgress: 模型处理进度
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelProgress: int
        :param TrainingModelErrorMsg: 模型错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelErrorMsg: str
        :param TrainingModelFormat: 模型格式
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingModelFormat: str
        :param VersionType: 模型版本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionType: str
        :param GPUType: GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GPUType: str
        :param AutoClean: 模型自动清理开关
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoClean: str
        :param ModelCleanPeriod: 模型清理周期
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelCleanPeriod: int
        :param MaxReservedModels: 模型数量保留上限
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReservedModels: int
        :param ModelHotUpdatePath: 模型热更新目录
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelHotUpdatePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param ReasoningEnvironmentId: 推理环境id
注意：此字段可能返回 null，表示取不到有效值。
        :type ReasoningEnvironmentId: str
        :param TrainingJobVersion: 训练任务版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingJobVersion: str
        :param TrainingPreference: 训练偏好
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingPreference: str
        :param AutoMLTaskId: 自动学习任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoMLTaskId: str
        :param IsQAT: 是否QAT模型
注意：此字段可能返回 null，表示取不到有效值。
        :type IsQAT: bool
        """
        self.TrainingModelId = None
        self.TrainingModelVersionId = None
        self.TrainingModelVersion = None
        self.TrainingModelSource = None
        self.TrainingModelCreateTime = None
        self.TrainingModelCreator = None
        self.AlgorithmFramework = None
        self.ReasoningEnvironment = None
        self.ReasoningEnvironmentSource = None
        self.TrainingModelIndex = None
        self.TrainingJobName = None
        self.TrainingModelCosPath = None
        self.TrainingModelName = None
        self.TrainingJobId = None
        self.ReasoningImageInfo = None
        self.CreateTime = None
        self.TrainingModelStatus = None
        self.TrainingModelProgress = None
        self.TrainingModelErrorMsg = None
        self.TrainingModelFormat = None
        self.VersionType = None
        self.GPUType = None
        self.AutoClean = None
        self.ModelCleanPeriod = None
        self.MaxReservedModels = None
        self.ModelHotUpdatePath = None
        self.ReasoningEnvironmentId = None
        self.TrainingJobVersion = None
        self.TrainingPreference = None
        self.AutoMLTaskId = None
        self.IsQAT = None


    def _deserialize(self, params):
        self.TrainingModelId = params.get("TrainingModelId")
        self.TrainingModelVersionId = params.get("TrainingModelVersionId")
        self.TrainingModelVersion = params.get("TrainingModelVersion")
        self.TrainingModelSource = params.get("TrainingModelSource")
        self.TrainingModelCreateTime = params.get("TrainingModelCreateTime")
        self.TrainingModelCreator = params.get("TrainingModelCreator")
        self.AlgorithmFramework = params.get("AlgorithmFramework")
        self.ReasoningEnvironment = params.get("ReasoningEnvironment")
        self.ReasoningEnvironmentSource = params.get("ReasoningEnvironmentSource")
        self.TrainingModelIndex = params.get("TrainingModelIndex")
        self.TrainingJobName = params.get("TrainingJobName")
        if params.get("TrainingModelCosPath") is not None:
            self.TrainingModelCosPath = CosPathInfo()
            self.TrainingModelCosPath._deserialize(params.get("TrainingModelCosPath"))
        self.TrainingModelName = params.get("TrainingModelName")
        self.TrainingJobId = params.get("TrainingJobId")
        if params.get("ReasoningImageInfo") is not None:
            self.ReasoningImageInfo = ImageInfo()
            self.ReasoningImageInfo._deserialize(params.get("ReasoningImageInfo"))
        self.CreateTime = params.get("CreateTime")
        self.TrainingModelStatus = params.get("TrainingModelStatus")
        self.TrainingModelProgress = params.get("TrainingModelProgress")
        self.TrainingModelErrorMsg = params.get("TrainingModelErrorMsg")
        self.TrainingModelFormat = params.get("TrainingModelFormat")
        self.VersionType = params.get("VersionType")
        self.GPUType = params.get("GPUType")
        self.AutoClean = params.get("AutoClean")
        self.ModelCleanPeriod = params.get("ModelCleanPeriod")
        self.MaxReservedModels = params.get("MaxReservedModels")
        if params.get("ModelHotUpdatePath") is not None:
            self.ModelHotUpdatePath = CosPathInfo()
            self.ModelHotUpdatePath._deserialize(params.get("ModelHotUpdatePath"))
        self.ReasoningEnvironmentId = params.get("ReasoningEnvironmentId")
        self.TrainingJobVersion = params.get("TrainingJobVersion")
        self.TrainingPreference = params.get("TrainingPreference")
        self.AutoMLTaskId = params.get("AutoMLTaskId")
        self.IsQAT = params.get("IsQAT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingTaskDetail(AbstractModel):
    """训练任务详情

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        :param Name: 训练任务名称
        :type Name: str
        :param Uin: 主账号uin
        :type Uin: str
        :param SubUin: 子账号uin
        :type SubUin: str
        :param Region: 地域
        :type Region: str
        :param FrameworkName: 训练框架名称，eg：SPARK、PYSARK、TENSORFLOW、PYTORCH
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkName: str
        :param FrameworkVersion: 训练框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        :param FrameworkEnvironment: 框架运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkEnvironment: str
        :param ChargeType: 计费模式
        :type ChargeType: str
        :param ResourceGroupId: 预付费专用资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param ResourceConfigInfos: 资源配置
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param TrainingMode: 训练模式，eg：PS_WORKER、DDP、MPI、HOROVOD
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingMode: str
        :param CodePackagePath: 代码包
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param StartCmdInfo: 启动命令信息
        :type StartCmdInfo: :class:`tencentcloud.tione.v20211111.models.StartCmdInfo`
        :param DataSource: 数据来源，eg：DATASET、COS
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSource: str
        :param DataConfigs: 数据配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DataConfigs: list of DataConfig
        :param TuningParameters: 调优参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TuningParameters: str
        :param Output: 训练输出
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param LogEnable: 是否上报日志
        :type LogEnable: bool
        :param LogConfig: 日志配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param StartTime: 训练开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param LatestInstanceId: 最近一次实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestInstanceId: str
        :param TensorBoardId: TensorBoard ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TensorBoardId: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param EndTime: 训练结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (按量计费)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param ResourceGroupName: 预付费专用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param Message: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Status: 任务状态，eg：STARTING启动中、RUNNING运行中、STOPPING停止中、STOPPED已停止、FAILED异常、SUCCEED已完成
        :type Status: str
        :param CallbackUrl: 回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        """
        self.Id = None
        self.Name = None
        self.Uin = None
        self.SubUin = None
        self.Region = None
        self.FrameworkName = None
        self.FrameworkVersion = None
        self.FrameworkEnvironment = None
        self.ChargeType = None
        self.ResourceGroupId = None
        self.ResourceConfigInfos = None
        self.Tags = None
        self.TrainingMode = None
        self.CodePackagePath = None
        self.StartCmdInfo = None
        self.DataSource = None
        self.DataConfigs = None
        self.TuningParameters = None
        self.Output = None
        self.LogEnable = None
        self.LogConfig = None
        self.VpcId = None
        self.SubnetId = None
        self.ImageInfo = None
        self.RuntimeInSeconds = None
        self.CreateTime = None
        self.StartTime = None
        self.ChargeStatus = None
        self.LatestInstanceId = None
        self.TensorBoardId = None
        self.Remark = None
        self.FailureReason = None
        self.UpdateTime = None
        self.EndTime = None
        self.BillingInfo = None
        self.ResourceGroupName = None
        self.Message = None
        self.Status = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Uin = params.get("Uin")
        self.SubUin = params.get("SubUin")
        self.Region = params.get("Region")
        self.FrameworkName = params.get("FrameworkName")
        self.FrameworkVersion = params.get("FrameworkVersion")
        self.FrameworkEnvironment = params.get("FrameworkEnvironment")
        self.ChargeType = params.get("ChargeType")
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ResourceConfigInfos") is not None:
            self.ResourceConfigInfos = []
            for item in params.get("ResourceConfigInfos"):
                obj = ResourceConfigInfo()
                obj._deserialize(item)
                self.ResourceConfigInfos.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.TrainingMode = params.get("TrainingMode")
        if params.get("CodePackagePath") is not None:
            self.CodePackagePath = CosPathInfo()
            self.CodePackagePath._deserialize(params.get("CodePackagePath"))
        if params.get("StartCmdInfo") is not None:
            self.StartCmdInfo = StartCmdInfo()
            self.StartCmdInfo._deserialize(params.get("StartCmdInfo"))
        self.DataSource = params.get("DataSource")
        if params.get("DataConfigs") is not None:
            self.DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self.DataConfigs.append(obj)
        self.TuningParameters = params.get("TuningParameters")
        if params.get("Output") is not None:
            self.Output = CosPathInfo()
            self.Output._deserialize(params.get("Output"))
        self.LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self.LogConfig = LogConfig()
            self.LogConfig._deserialize(params.get("LogConfig"))
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.RuntimeInSeconds = params.get("RuntimeInSeconds")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.ChargeStatus = params.get("ChargeStatus")
        self.LatestInstanceId = params.get("LatestInstanceId")
        self.TensorBoardId = params.get("TensorBoardId")
        self.Remark = params.get("Remark")
        self.FailureReason = params.get("FailureReason")
        self.UpdateTime = params.get("UpdateTime")
        self.EndTime = params.get("EndTime")
        self.BillingInfo = params.get("BillingInfo")
        self.ResourceGroupName = params.get("ResourceGroupName")
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainingTaskSetItem(AbstractModel):
    """出参类型

    """

    def __init__(self):
        r"""
        :param Id: 训练任务ID
        :type Id: str
        :param Name: 训练任务名称
        :type Name: str
        :param FrameworkName: 框架名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkName: str
        :param FrameworkVersion: 训练框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        :param FrameworkEnvironment: 框架运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkEnvironment: str
        :param ChargeType: 计费模式
        :type ChargeType: str
        :param ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param ResourceGroupId: 预付费专用资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param ResourceConfigInfos: 资源配置
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param TrainingMode: 训练模式eg：PS_WORKER、DDP、MPI、HOROVOD
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingMode: str
        :param Status: 任务状态，eg：STARTING启动中、RUNNING运行中、STOPPING停止中、STOPPED已停止、FAILED异常、SUCCEED已完成
        :type Status: str
        :param RuntimeInSeconds: 运行时长
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeInSeconds: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param StartTime: 训练开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 训练结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Output: 训练输出
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param FailureReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (按量计费)
        :type BillingInfo: str
        :param ResourceGroupName: 预付费专用资源组名称
        :type ResourceGroupName: str
        :param ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param Message: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Tags: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param CallbackUrl: 回调地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        """
        self.Id = None
        self.Name = None
        self.FrameworkName = None
        self.FrameworkVersion = None
        self.FrameworkEnvironment = None
        self.ChargeType = None
        self.ChargeStatus = None
        self.ResourceGroupId = None
        self.ResourceConfigInfos = None
        self.TrainingMode = None
        self.Status = None
        self.RuntimeInSeconds = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Output = None
        self.FailureReason = None
        self.UpdateTime = None
        self.BillingInfo = None
        self.ResourceGroupName = None
        self.ImageInfo = None
        self.Message = None
        self.Tags = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.FrameworkName = params.get("FrameworkName")
        self.FrameworkVersion = params.get("FrameworkVersion")
        self.FrameworkEnvironment = params.get("FrameworkEnvironment")
        self.ChargeType = params.get("ChargeType")
        self.ChargeStatus = params.get("ChargeStatus")
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("ResourceConfigInfos") is not None:
            self.ResourceConfigInfos = []
            for item in params.get("ResourceConfigInfos"):
                obj = ResourceConfigInfo()
                obj._deserialize(item)
                self.ResourceConfigInfos.append(obj)
        self.TrainingMode = params.get("TrainingMode")
        self.Status = params.get("Status")
        self.RuntimeInSeconds = params.get("RuntimeInSeconds")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Output") is not None:
            self.Output = CosPathInfo()
            self.Output._deserialize(params.get("Output"))
        self.FailureReason = params.get("FailureReason")
        self.UpdateTime = params.get("UpdateTime")
        self.BillingInfo = params.get("BillingInfo")
        self.ResourceGroupName = params.get("ResourceGroupName")
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
        self.Message = params.get("Message")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeMount(AbstractModel):
    """外部挂载信息

    """

    def __init__(self):
        r"""
        :param CFSConfig: cfs的配置信息
        :type CFSConfig: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param VolumeSourceType: 挂载源类型
        :type VolumeSourceType: str
        """
        self.CFSConfig = None
        self.VolumeSourceType = None


    def _deserialize(self, params):
        if params.get("CFSConfig") is not None:
            self.CFSConfig = CFSConfig()
            self.CFSConfig._deserialize(params.get("CFSConfig"))
        self.VolumeSourceType = params.get("VolumeSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeightEntry(AbstractModel):
    """服务的权重

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务id
        :type ServiceId: str
        :param Weight: 流量权重值，同 ServiceGroup 下 总和应为 100
        :type Weight: int
        """
        self.ServiceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadStatus(AbstractModel):
    """工作负载的状态

    """

    def __init__(self):
        r"""
        :param Replicas: 当前实例数
        :type Replicas: int
        :param UpdatedReplicas: 更新的实例数
        :type UpdatedReplicas: int
        :param ReadyReplicas: 就绪的实例数
        :type ReadyReplicas: int
        :param AvailableReplicas: 可用的实例数
        :type AvailableReplicas: int
        :param UnavailableReplicas: 不可用的实例数
        :type UnavailableReplicas: int
        :param Status: Normal	正常运行中
Abnormal	服务异常，例如容器启动失败等
Waiting	服务等待中，例如容器下载镜像过程等
Stopped   已停止 
Pending 启动中
Stopping 停止中
        :type Status: str
        :param StatefulSetCondition: 工作负载的状况信息
        :type StatefulSetCondition: list of StatefulSetCondition
        :param Conditions: 工作负载历史的状况信息
        :type Conditions: list of StatefulSetCondition
        """
        self.Replicas = None
        self.UpdatedReplicas = None
        self.ReadyReplicas = None
        self.AvailableReplicas = None
        self.UnavailableReplicas = None
        self.Status = None
        self.StatefulSetCondition = None
        self.Conditions = None


    def _deserialize(self, params):
        self.Replicas = params.get("Replicas")
        self.UpdatedReplicas = params.get("UpdatedReplicas")
        self.ReadyReplicas = params.get("ReadyReplicas")
        self.AvailableReplicas = params.get("AvailableReplicas")
        self.UnavailableReplicas = params.get("UnavailableReplicas")
        self.Status = params.get("Status")
        if params.get("StatefulSetCondition") is not None:
            self.StatefulSetCondition = []
            for item in params.get("StatefulSetCondition"):
                obj = StatefulSetCondition()
                obj._deserialize(item)
                self.StatefulSetCondition.append(obj)
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = StatefulSetCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        