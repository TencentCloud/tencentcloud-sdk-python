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
        :param ResourceGroupId: 预付费专用资源组id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param ResourceGroupName: 预付费专用资源组名称
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
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (for后付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
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
        :param ResourceGroupId: 预付费专用资源组
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
        :param ResourceGroupName: 预付费专用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param FailureReason: 失败原因
        :type FailureReason: str
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (for后付费)
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
        


class CreateBatchTaskRequest(AbstractModel):
    """CreateBatchTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchTaskName: 跑批任务名称，不超过60个字符，仅支持中英文、数字、下划线"_"、短横"-"，只能以中英文、数字开头
        :type BatchTaskName: str
        :param ChargeType: 计费模式，eg：PREPAID预付费，即包年包月；POSTPAID_BY_HOUR按小时后付费
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
        :param ResourceGroupId: 预付费专用资源组
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
        :param ModelFormat: 模型格式 （PYTORCH/TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/PMML）
        :type ModelFormat: str
        :param ReasoningEnvironmentId: 推理镜像ID
        :type ReasoningEnvironmentId: str
        :param AutoClean: 模型自动清理开关(true/false)，当前版本仅支持SAVED_MODEL格式模型
        :type AutoClean: str
        :param MaxReservedModels: 模型数量保留上限(默认值为24个，上限为24，下限为1，步长为1)
        :type MaxReservedModels: int
        :param ModelCleanPeriod: 模型清理周期(默认值为1分钟，上限为1440，下限为1分钟，步长为1)
        :type ModelCleanPeriod: int
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
        :param TrainingMode: 训练模式，通过DescribeTrainingFrameworks接口查询，eg：PS_WORKER、DDP、MPI、HOROVOD
        :type TrainingMode: str
        :param ChargeType: 计费模式，eg：PREPAID预付费，即包年包月；POSTPAID_BY_HOUR按小时后付费
        :type ChargeType: str
        :param ResourceConfigInfos: 资源配置，需填写对应算力规格ID和节点数量，算力规格ID查询接口为DescribeBillingSpecsPrice，eg：[{"Role":"WORKER", "InstanceType": "TI.S.MEDIUM.POST", "InstanceNum": 1}]
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param CodePackagePath: COS代码包路径
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param Output: COS训练输出路径
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param LogEnable: 是否上报日志
        :type LogEnable: bool
        :param FrameworkName: 训练框架名称，通过DescribeTrainingFrameworks接口查询，eg：SPARK、PYSPARK、TENSORFLOW、PYTORCH
        :type FrameworkName: str
        :param FrameworkVersion: 训练框架版本，通过DescribeTrainingFrameworks接口查询，eg：tf1.15-py3.7-cpu、torch1.9-py3.8-cuda11.1-gpu
        :type FrameworkVersion: str
        :param ResourceGroupId: 预付费专用资源组ID，通过DescribeBillingResourceGroups接口查询
        :type ResourceGroupId: str
        :param Tags: 标签配置
        :type Tags: list of Tag
        :param ImageInfo: 自定义镜像信息
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param StartCmdInfo: 启动命令信息，默认为sh start.sh
        :type StartCmdInfo: :class:`tencentcloud.tione.v20211111.models.StartCmdInfo`
        :param DataSource: 数据来源，eg：DATASET、COS、CFS、HDFS
        :type DataSource: str
        :param DataConfigs: 数据配置
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
        """
        self.Name = None
        self.TrainingMode = None
        self.ChargeType = None
        self.ResourceConfigInfos = None
        self.CodePackagePath = None
        self.Output = None
        self.LogEnable = None
        self.FrameworkName = None
        self.FrameworkVersion = None
        self.ResourceGroupId = None
        self.Tags = None
        self.ImageInfo = None
        self.StartCmdInfo = None
        self.DataSource = None
        self.DataConfigs = None
        self.VpcId = None
        self.SubnetId = None
        self.LogConfig = None
        self.TuningParameters = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TrainingMode = params.get("TrainingMode")
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
        if params.get("Output") is not None:
            self.Output = CosPathInfo()
            self.Output._deserialize(params.get("Output"))
        self.LogEnable = params.get("LogEnable")
        self.FrameworkName = params.get("FrameworkName")
        self.FrameworkVersion = params.get("FrameworkVersion")
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
        self.DataSource = params.get("DataSource")
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
        """
        self.MappingPath = None
        self.DataSourceType = None
        self.DataSetSource = None
        self.COSSource = None
        self.CFSSource = None
        self.HDFSSource = None


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
        :param ChargeType: 付费模式：POSTPAID_BY_HOUR后付费、PREPAID预付费
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
        """
        self.DatasetId = None
        self.Offset = None
        self.Limit = None
        self.LabelList = None
        self.AnnotationStatus = None
        self.DatasetIds = None


    def _deserialize(self, params):
        self.DatasetId = params.get("DatasetId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.LabelList = params.get("LabelList")
        self.AnnotationStatus = params.get("AnnotationStatus")
        self.DatasetIds = params.get("DatasetIds")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AnnotatedTotalCount = None
        self.NonAnnotatedTotalCount = None
        self.FilterTotalCount = None
        self.FilterLabelList = None
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
    TrainingModelSource (模型来源)  其值Filter.Values支持： JOB/COS/AUTO_ML
    AlgorithmFramework (算法框架) 其值Filter.Values支持：TENSORFLOW/PYTORCH/DETECTRON2
    ModelFormat（模型格式）其值Filter.Values支持：
TORCH_SCRIPT/PYTORCH/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/PMML
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PodNames = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PodNames = params.get("PodNames")
        self.TotalCount = params.get("TotalCount")
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
        """
        self.Version = None
        self.TrainingModes = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.TrainingModes = params.get("TrainingModes")
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
        """
        self.Role = None
        self.Cpu = None
        self.Memory = None
        self.GpuType = None
        self.Gpu = None
        self.InstanceType = None
        self.InstanceNum = None
        self.InstanceTypeAlias = None


    def _deserialize(self, params):
        self.Role = params.get("Role")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.GpuType = params.get("GpuType")
        self.Gpu = params.get("Gpu")
        self.InstanceType = params.get("InstanceType")
        self.InstanceNum = params.get("InstanceNum")
        self.InstanceTypeAlias = params.get("InstanceTypeAlias")
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
        :param GpuType: Gpu卡型号 T4或者V100
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param RealGpu: 创建或更新时无需填写，仅展示需要关注
后付费非整卡实例对应的实际的Gpu卡资源, 表示gpu资源对应实际的gpu卡个数.
RealGpu=100表示实际使用了一张gpu卡, 对应实际的实例机型, 有可能代表带有1/4卡的实例4个, 或者带有1/2卡的实例2个, 或者带有1卡的实力1个.
注意：此字段可能返回 null，表示取不到有效值。
        :type RealGpu: int
        """
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.GpuType = None
        self.RealGpu = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.GpuType = params.get("GpuType")
        self.RealGpu = params.get("RealGpu")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """
        self.SpecId = None
        self.SpecName = None
        self.SpecAlias = None


    def _deserialize(self, params):
        self.SpecId = params.get("SpecId")
        self.SpecName = params.get("SpecName")
        self.SpecAlias = params.get("SpecAlias")
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
        """
        self.SpecName = None
        self.TotalCost = None
        self.RealTotalCost = None


    def _deserialize(self, params):
        self.SpecName = params.get("SpecName")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
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
        """
        self.TrainingModelId = None
        self.TrainingModelName = None
        self.Tags = None
        self.CreateTime = None


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
        :param FrameworkName: 训练框架名称，eg：SPARK、TENSORFLOW、PYTORCH、LIGHT
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkName: str
        :param FrameworkVersion: 训练框架版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FrameworkVersion: str
        :param TrainingMode: 训练模式，eg：PS_WORKER、DDP、MPI、HOROVOD
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingMode: str
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
        :param ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
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
        :param Status: 任务状态
        :type Status: str
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
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (for后付费)
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingInfo: str
        :param ResourceGroupName: 预付费专用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param Message: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.Id = None
        self.Name = None
        self.Uin = None
        self.SubUin = None
        self.Region = None
        self.FrameworkName = None
        self.FrameworkVersion = None
        self.TrainingMode = None
        self.ChargeType = None
        self.ResourceGroupId = None
        self.ResourceConfigInfos = None
        self.Tags = None
        self.ImageInfo = None
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
        self.Status = None
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


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Uin = params.get("Uin")
        self.SubUin = params.get("SubUin")
        self.Region = params.get("Region")
        self.FrameworkName = params.get("FrameworkName")
        self.FrameworkVersion = params.get("FrameworkVersion")
        self.TrainingMode = params.get("TrainingMode")
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
        if params.get("ImageInfo") is not None:
            self.ImageInfo = ImageInfo()
            self.ImageInfo._deserialize(params.get("ImageInfo"))
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
        self.Status = params.get("Status")
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
        :param TrainingMode: 训练模式eg：PS_WORKER、DDP、MPI、HOROVOD
注意：此字段可能返回 null，表示取不到有效值。
        :type TrainingMode: str
        :param ChargeType: 计费模式
        :type ChargeType: str
        :param ChargeStatus: 计费状态，eg：BILLING计费中，ARREARS_STOP欠费停止，NOT_BILLING不在计费中
        :type ChargeStatus: str
        :param ResourceGroupId: 预付费专用资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param ResourceConfigInfos: 资源配置
        :type ResourceConfigInfos: list of ResourceConfigInfo
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
        :param BillingInfo: 计费金额信息，eg：2.00元/小时 (for后付费)
        :type BillingInfo: str
        :param ResourceGroupName: 预付费专用资源组名称
        :type ResourceGroupName: str
        :param ImageInfo: 自定义镜像信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param Message: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.Id = None
        self.Name = None
        self.FrameworkName = None
        self.FrameworkVersion = None
        self.TrainingMode = None
        self.ChargeType = None
        self.ChargeStatus = None
        self.ResourceGroupId = None
        self.ResourceConfigInfos = None
        self.Tags = None
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


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.FrameworkName = params.get("FrameworkName")
        self.FrameworkVersion = params.get("FrameworkVersion")
        self.TrainingMode = params.get("TrainingMode")
        self.ChargeType = params.get("ChargeType")
        self.ChargeStatus = params.get("ChargeStatus")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        