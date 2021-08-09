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


class AIModelApplication(AbstractModel):
    """AI模型申请信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param Status: 申请状态：1-已申请；2-已取消；3-已拒绝；4-已通过\n        :type Status: int\n        """
        self.ProductId = None
        self.ProductName = None
        self.Status = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIModelInfo(AbstractModel):
    """AI模型信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param Status: 申请状态：1-已申请；2-已取消；3-已拒绝；4-已通过\n        :type Status: int\n        :param Total: 可调用数量\n        :type Total: int\n        :param Used: 已调用数量\n        :type Used: int\n        :param ApplyTime: 申请时间\n        :type ApplyTime: int\n        :param ApprovalTime: 审批通过时间\n        :type ApprovalTime: int\n        """
        self.ProductId = None
        self.ProductName = None
        self.Status = None
        self.Total = None
        self.Used = None
        self.ApplyTime = None
        self.ApprovalTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.Status = params.get("Status")
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.ApplyTime = params.get("ApplyTime")
        self.ApprovalTime = params.get("ApprovalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIModelUsageInfo(AbstractModel):
    """AI模型资源使用信息

    """

    def __init__(self):
        """
        :param CreateTime: 开通时间\n        :type CreateTime: int\n        :param Total: 资源总量\n        :type Total: int\n        :param Used: 已使用资源数量\n        :type Used: int\n        """
        self.CreateTime = None
        self.Total = None
        self.Used = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionHistory(AbstractModel):
    """查询设备历史

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param ActionId: 动作Id\n        :type ActionId: str\n        :param ActionName: 动作名称\n        :type ActionName: str\n        :param ReqTime: 请求时间\n        :type ReqTime: int\n        :param RspTime: 响应时间\n        :type RspTime: int\n        :param InputParams: 输入参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type InputParams: str\n        :param OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputParams: str\n        :param Calling: 调用方式\n        :type Calling: str\n        :param ClientToken: 调用Id\n        :type ClientToken: str\n        :param Status: 调用状态\n        :type Status: str\n        """
        self.DeviceName = None
        self.ActionId = None
        self.ActionName = None
        self.ReqTime = None
        self.RspTime = None
        self.InputParams = None
        self.OutputParams = None
        self.Calling = None
        self.ClientToken = None
        self.Status = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.ActionName = params.get("ActionName")
        self.ReqTime = params.get("ReqTime")
        self.RspTime = params.get("RspTime")
        self.InputParams = params.get("InputParams")
        self.OutputParams = params.get("OutputParams")
        self.Calling = params.get("Calling")
        self.ClientToken = params.get("ClientToken")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyAIModelRequest(AbstractModel):
    """ApplyAIModel请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: AI模型ID\n        :type ModelId: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.ModelId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyAIModelResponse(AbstractModel):
    """ApplyAIModel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BalanceTransaction(AbstractModel):
    """账户流水

    """

    def __init__(self):
        """
        :param AccountType: 账户类型：1-设备接入 2-云存。\n        :type AccountType: int\n        :param Operation: 账户变更类型：Rechareg-充值；CreateOrder-新购。\n        :type Operation: str\n        :param DealId: 流水ID。\n        :type DealId: str\n        :param Amount: 变更金额，单位：分（人民币）。\n        :type Amount: int\n        :param Balance: 变更后账户余额，单位：分（人民币）。\n        :type Balance: int\n        :param OperationTime: 变更时间。\n        :type OperationTime: int\n        """
        self.AccountType = None
        self.Operation = None
        self.DealId = None
        self.Amount = None
        self.Balance = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Operation = params.get("Operation")
        self.DealId = params.get("DealId")
        self.Amount = params.get("Amount")
        self.Balance = params.get("Balance")
        self.OperationTime = params.get("OperationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareRequest(AbstractModel):
    """BatchUpdateFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件新版本号\n        :type FirmwareVersion: str\n        :param FirmwareOriVersion: 固件原版本号，根据文件列表升级固件不需要填写此参数\n        :type FirmwareOriVersion: str\n        :param UpgradeMethod: 升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式\n        :type UpgradeMethod: int\n        :param FileName: 设备列表文件名称，根据文件列表升级固件需要填写此参数\n        :type FileName: str\n        :param FileMd5: 设备列表的文件md5值\n        :type FileMd5: str\n        :param FileSize: 设备列表的文件大小值\n        :type FileSize: int\n        :param DeviceNames: 需要升级的设备名称列表\n        :type DeviceNames: list of str\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.FirmwareOriVersion = None
        self.UpgradeMethod = None
        self.FileName = None
        self.FileMd5 = None
        self.FileSize = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.FirmwareOriVersion = params.get("FirmwareOriVersion")
        self.UpgradeMethod = params.get("UpgradeMethod")
        self.FileName = params.get("FileName")
        self.FileMd5 = params.get("FileMd5")
        self.FileSize = params.get("FileSize")
        self.DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareResponse(AbstractModel):
    """BatchUpdateFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindCloudStorageUserRequest(AbstractModel):
    """BindCloudStorageUser请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param UserId: 用户ID\n        :type UserId: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.UserId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudStorageUserResponse(AbstractModel):
    """BindCloudStorageUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelAIModelApplicationRequest(AbstractModel):
    """CancelAIModelApplication请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: AI模型ID\n        :type ModelId: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.ModelId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAIModelApplicationResponse(AbstractModel):
    """CancelAIModelApplication返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelDeviceFirmwareTaskRequest(AbstractModel):
    """CancelDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件升级任务ID\n        :type TaskId: int\n        """
        self.ProductID = None
        self.DeviceName = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDeviceFirmwareTaskResponse(AbstractModel):
    """CancelDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CheckForwardAuthRequest(AbstractModel):
    """CheckForwardAuth请求参数结构体

    """

    def __init__(self):
        """
        :param Skey: 控制台Skey\n        :type Skey: str\n        :param QueueType: 队列类型 0.CMQ  1.Ckafka\n        :type QueueType: int\n        """
        self.Skey = None
        self.QueueType = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckForwardAuthResponse(AbstractModel):
    """CheckForwardAuth返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号\n        :type Endpoint: str\n        :param Result: 结果\n        :type Result: int\n        :param Productid: 产品ID\n        :type Productid: str\n        :param ErrMsg: 错误消息\n        :type ErrMsg: str\n        :param QueueType: 队列类型 0.CMQ  1.Ckafka\n        :type QueueType: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Endpoint = None
        self.Result = None
        self.Productid = None
        self.ErrMsg = None
        self.QueueType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.Result = params.get("Result")
        self.Productid = params.get("Productid")
        self.ErrMsg = params.get("ErrMsg")
        self.QueueType = params.get("QueueType")
        self.RequestId = params.get("RequestId")


class CloudStorageEvent(AbstractModel):
    """云存事件

    """

    def __init__(self):
        """
        :param StartTime: 事件起始时间（Unix 时间戳，秒级\n        :type StartTime: int\n        :param EndTime: 事件结束时间（Unix 时间戳，秒级\n        :type EndTime: int\n        :param Thumbnail: 事件缩略图\n        :type Thumbnail: str\n        :param EventId: 事件ID\n        :type EventId: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.Thumbnail = None
        self.EventId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Thumbnail = params.get("Thumbnail")
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageTimeData(AbstractModel):
    """云存时间轴接口返回数据

    """

    def __init__(self):
        """
        :param TimeList: 云存时间轴信息列表\n        :type TimeList: list of CloudStorageTimeInfo\n        :param VideoURL: 播放地址\n        :type VideoURL: str\n        """
        self.TimeList = None
        self.VideoURL = None


    def _deserialize(self, params):
        if params.get("TimeList") is not None:
            self.TimeList = []
            for item in params.get("TimeList"):
                obj = CloudStorageTimeInfo()
                obj._deserialize(item)
                self.TimeList.append(obj)
        self.VideoURL = params.get("VideoURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageTimeInfo(AbstractModel):
    """云存时间轴信息

    """

    def __init__(self):
        """
        :param StartTime: 开始时间\n        :type StartTime: int\n        :param EndTime: 结束时间\n        :type EndTime: int\n        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageUserInfo(AbstractModel):
    """云存用户信息

    """

    def __init__(self):
        """
        :param UserId: 用户ID\n        :type UserId: str\n        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceDataRequest(AbstractModel):
    """ControlDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Data: 属性数据, JSON格式字符串, 注意字段需要在物模型属性里定义\n        :type Data: str\n        :param Method: 请求类型 , 不填该参数或者 desired 表示下发属性给设备,  reported 表示模拟设备上报属性\n        :type Method: str\n        :param DataTimestamp: 上报数据UNIX时间戳(毫秒), 仅对Method:reported有效\n        :type DataTimestamp: int\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Data = None
        self.Method = None
        self.DataTimestamp = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")
        self.Method = params.get("Method")
        self.DataTimestamp = params.get("DataTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回信息\n        :type Data: str\n        :param Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateAIDetectionRequest(AbstractModel):
    """CreateAIDetection请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param ModelId: AI模型ID\n        :type ModelId: str\n        :param StartTime: 图片上传的开始时间\n        :type StartTime: int\n        :param EndTime: 图片上传的结束时间\n        :type EndTime: int\n        """
        self.ProductId = None
        self.DeviceName = None
        self.ModelId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ModelId = params.get("ModelId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIDetectionResponse(AbstractModel):
    """CreateAIDetection返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBatchRequest(AbstractModel):
    """CreateBatch请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DevNum: 批次创建的设备数量\n        :type DevNum: int\n        :param DevPre: 批次创建的设备前缀。不超过24个字符\n        :type DevPre: str\n        """
        self.ProductId = None
        self.DevNum = None
        self.DevPre = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DevNum = params.get("DevNum")
        self.DevPre = params.get("DevPre")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchResponse(AbstractModel):
    """CreateBatch返回参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID\n        :type BatchId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")


class CreateCOSCredentialsRequest(AbstractModel):
    """CreateCOSCredentials请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCOSCredentialsResponse(AbstractModel):
    """CreateCOSCredentials返回参数结构体

    """

    def __init__(self):
        """
        :param StorageBucket: COS存储桶名称\n        :type StorageBucket: str\n        :param StorageRegion: COS存储桶区域\n        :type StorageRegion: str\n        :param StoragePath: COS存储桶路径\n        :type StoragePath: str\n        :param SecretID: COS上传用的SecretID\n        :type SecretID: str\n        :param SecretKey: COS上传用的SecretKey\n        :type SecretKey: str\n        :param Token: COS上传用的Token\n        :type Token: str\n        :param ExpiredTime: 密钥信息过期时间\n        :type ExpiredTime: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StorageBucket = None
        self.StorageRegion = None
        self.StoragePath = None
        self.SecretID = None
        self.SecretKey = None
        self.Token = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StorageBucket = params.get("StorageBucket")
        self.StorageRegion = params.get("StorageRegion")
        self.StoragePath = params.get("StoragePath")
        self.SecretID = params.get("SecretID")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")


class CreateCloudStorageRequest(AbstractModel):
    """CreateCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param PackageId: 云存套餐ID：
yc1m3d ： 全时3天存储月套餐。
yc1m7d ： 全时7天存储月套餐。
yc1m30d ：全时30天存储月套餐。
yc1y3d ：全时3天存储年套餐。
yc1y7d ：全时7天存储年套餐。
yc1y30d ：全时30天存储年套餐。
ye1m3d ：事件3天存储月套餐。
ye1m7d ：事件7天存储月套餐。
ye1m30d ：事件30天存储月套餐 。
ye1y3d ：事件3天存储年套餐。
ye1y7d ：事件7天存储年套餐。
ye1y30d ：事件30天存储年套餐。
yc1w7d : 全时7天存储周套餐。
ye1w7d : 事件7天存储周套餐。\n        :type PackageId: str\n        :param Override: 如果当前设备已开启云存套餐，Override=1会使用新套餐覆盖原有套餐。不传此参数则默认为0。\n        :type Override: int\n        """
        self.ProductId = None
        self.DeviceName = None
        self.PackageId = None
        self.Override = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.PackageId = params.get("PackageId")
        self.Override = params.get("Override")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudStorageResponse(AbstractModel):
    """CreateCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDataForwardRequest(AbstractModel):
    """CreateDataForward请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。\n        :type ProductId: str\n        :param ForwardAddr: 转发地址。\n        :type ForwardAddr: str\n        :param DataChose: 1-数据信息转发 2-设备上下线状态转发 3-数据信息转发&设备上下线状态转发\n        :type DataChose: int\n        """
        self.ProductId = None
        self.ForwardAddr = None
        self.DataChose = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ForwardAddr = params.get("ForwardAddr")
        self.DataChose = params.get("DataChose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataForwardResponse(AbstractModel):
    """CreateDataForward返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateForwardRuleRequest(AbstractModel):
    """CreateForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param MsgType: 消息类型\n        :type MsgType: int\n        :param Skey: 控制台Skey\n        :type Skey: str\n        :param QueueRegion: 队列区域\n        :type QueueRegion: str\n        :param QueueType: 队列类型 0.CMQ  1.Ckafka\n        :type QueueType: int\n        :param Consecretid: 临时密钥\n        :type Consecretid: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param QueueID: 队列或主题ID\n        :type QueueID: str\n        :param QueueName: 队列或主题名称\n        :type QueueName: str\n        """
        self.ProductID = None
        self.MsgType = None
        self.Skey = None
        self.QueueRegion = None
        self.QueueType = None
        self.Consecretid = None
        self.InstanceId = None
        self.InstanceName = None
        self.QueueID = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Skey = params.get("Skey")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.Consecretid = params.get("Consecretid")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.QueueID = params.get("QueueID")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardRuleResponse(AbstractModel):
    """CreateForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号\n        :type Endpoint: str\n        :param QueueName: 队列名\n        :type QueueName: str\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param MsgType: 消息类型\n        :type MsgType: int\n        :param Result: 结果\n        :type Result: int\n        :param RoleName: 角色名称\n        :type RoleName: str\n        :param RoleID: 角色ID\n        :type RoleID: int\n        :param QueueRegion: 队列区\n        :type QueueRegion: str\n        :param QueueType: 消息队列的类型。 0：CMQ，1：CKafaka\n        :type QueueType: int\n        :param InstanceId: 实例id， 目前只有Ckafaka会用到\n        :type InstanceId: str\n        :param InstanceName: 实例名称，目前只有Ckafaka会用到\n        :type InstanceName: str\n        :param ErrMsg: 错误消息\n        :type ErrMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Endpoint = None
        self.QueueName = None
        self.ProductID = None
        self.MsgType = None
        self.Result = None
        self.RoleName = None
        self.RoleID = None
        self.QueueRegion = None
        self.QueueType = None
        self.InstanceId = None
        self.InstanceName = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.QueueName = params.get("QueueName")
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Result = params.get("Result")
        self.RoleName = params.get("RoleName")
        self.RoleID = params.get("RoleID")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称\n        :type ProductName: str\n        :param DeviceType: 产品设备类型 1.普通设备 2.NVR设备\n        :type DeviceType: int\n        :param ProductVaildYears: 产品有效期\n        :type ProductVaildYears: int\n        :param Features: 设备功能码 ypsxth音频双向通话 spdxth视频单向通话\n        :type Features: list of str\n        :param ChipOs: 设备操作系统 Linux\n        :type ChipOs: str\n        :param ChipManufactureId: 芯片厂商id\n        :type ChipManufactureId: str\n        :param ChipId: 芯片id\n        :type ChipId: str\n        :param ProductDescription: 产品描述信息\n        :type ProductDescription: str\n        :param EncryptionType: 认证方式 只支持取值为2 psk认证\n        :type EncryptionType: int\n        """
        self.ProductName = None
        self.DeviceType = None
        self.ProductVaildYears = None
        self.Features = None
        self.ChipOs = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductDescription = None
        self.EncryptionType = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.DeviceType = params.get("DeviceType")
        self.ProductVaildYears = params.get("ProductVaildYears")
        self.Features = params.get("Features")
        self.ChipOs = params.get("ChipOs")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详情\n        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoProduct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateTaskFileUrlRequest(AbstractModel):
    """CreateTaskFileUrl请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFileUrlResponse(AbstractModel):
    """CreateTaskFileUrl返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 任务文件上传链接\n        :type Url: str\n        :param FileName: 任务文件名\n        :type FileName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Url = None
        self.FileName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileName = params.get("FileName")
        self.RequestId = params.get("RequestId")


class DataForward(AbstractModel):
    """数据转发描述

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。\n        :type ProductId: str\n        :param ForwardAddr: 转发地址。\n        :type ForwardAddr: str\n        :param Status: 转发状态。\n        :type Status: int\n        :param CreateTime: 创建时间。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间。\n        :type UpdateTime: int\n        :param DataChose: 1-数据信息转发 2-设备上下线状态转发 3-数据信息转发&设备上下线状态转发
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataChose: int\n        """
        self.ProductId = None
        self.ForwardAddr = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DataChose = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ForwardAddr = params.get("ForwardAddr")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.DataChose = params.get("DataChose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。\n        :type ProductId: str\n        :param DeviceName: 设备名称。\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFirmwareRequest(AbstractModel):
    """DeleteFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本\n        :type FirmwareVersion: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFirmwareResponse(AbstractModel):
    """DeleteFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteForwardRuleRequest(AbstractModel):
    """DeleteForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Skey: 控制台Skey\n        :type Skey: str\n        :param QueueType: 队列类型\n        :type QueueType: int\n        :param QueueName: 队列名称\n        :type QueueName: str\n        """
        self.ProductID = None
        self.Skey = None
        self.QueueType = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardRuleResponse(AbstractModel):
    """DeleteForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号\n        :type Endpoint: str\n        :param QueueName: 队列名称\n        :type QueueName: str\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Result: 删除结果 0成功 其他不成功\n        :type Result: int\n        :param ErrMsg: 错误消息\n        :type ErrMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Endpoint = None
        self.QueueName = None
        self.ProductID = None
        self.Result = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.QueueName = params.get("QueueName")
        self.ProductID = params.get("ProductID")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAIModelApplicationsRequest(AbstractModel):
    """DescribeAIModelApplications请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 模型ID\n        :type ModelId: str\n        :param Limit: 分页的大小，最大100\n        :type Limit: int\n        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.ModelId = None
        self.Limit = None
        self.Offset = None
        self.ProductId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelApplicationsResponse(AbstractModel):
    """DescribeAIModelApplications返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 申请记录数量\n        :type TotalCount: int\n        :param Applications: 申请记录数组\n        :type Applications: list of AIModelApplication\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Applications = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Applications") is not None:
            self.Applications = []
            for item in params.get("Applications"):
                obj = AIModelApplication()
                obj._deserialize(item)
                self.Applications.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAIModelChannelRequest(AbstractModel):
    """DescribeAIModelChannel请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 模型ID\n        :type ModelId: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.ModelId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelChannelResponse(AbstractModel):
    """DescribeAIModelChannel返回参数结构体

    """

    def __init__(self):
        """
        :param Type: 推送类型。ckafka：消息队列；forward：http/https推送\n        :type Type: str\n        :param ForwardAddress: 第三方推送地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForwardAddress: str\n        :param ForwardKey: 第三方推送密钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForwardKey: str\n        :param CKafkaRegion: ckafka地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type CKafkaRegion: str\n        :param CKafkaInstance: ckafka实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type CKafkaInstance: str\n        :param CKafkaTopic: ckafka订阅主题
注意：此字段可能返回 null，表示取不到有效值。\n        :type CKafkaTopic: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Type = None
        self.ForwardAddress = None
        self.ForwardKey = None
        self.CKafkaRegion = None
        self.CKafkaInstance = None
        self.CKafkaTopic = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ForwardAddress = params.get("ForwardAddress")
        self.ForwardKey = params.get("ForwardKey")
        self.CKafkaRegion = params.get("CKafkaRegion")
        self.CKafkaInstance = params.get("CKafkaInstance")
        self.CKafkaTopic = params.get("CKafkaTopic")
        self.RequestId = params.get("RequestId")


class DescribeAIModelUsageRequest(AbstractModel):
    """DescribeAIModelUsage请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 模型ID\n        :type ModelId: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Offset: 偏移量，从0开始\n        :type Offset: int\n        :param Limit: 分页的大小，最大100\n        :type Limit: int\n        """
        self.ModelId = None
        self.ProductId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelUsageResponse(AbstractModel):
    """DescribeAIModelUsage返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: AI模型资源包总量\n        :type TotalCount: int\n        :param UsageInfo: AI模型资源包信息数组\n        :type UsageInfo: list of AIModelUsageInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.UsageInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UsageInfo") is not None:
            self.UsageInfo = []
            for item in params.get("UsageInfo"):
                obj = AIModelUsageInfo()
                obj._deserialize(item)
                self.UsageInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAIModelsRequest(AbstractModel):
    """DescribeAIModels请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 模型ID\n        :type ModelId: str\n        :param Status: 申请状态：1-已申请；2-已取消；3-已拒绝；4-已通过\n        :type Status: int\n        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        :param Limit: 分页的大小，最大100\n        :type Limit: int\n        """
        self.ModelId = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelsResponse(AbstractModel):
    """DescribeAIModels返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: AI模型数量\n        :type TotalCount: int\n        :param Models: AI模型信息数组\n        :type Models: list of AIModelInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Models = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Models") is not None:
            self.Models = []
            for item in params.get("Models"):
                obj = AIModelInfo()
                obj._deserialize(item)
                self.Models.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBalanceRequest(AbstractModel):
    """DescribeBalance请求参数结构体

    """

    def __init__(self):
        """
        :param AccountType: 账户类型：1-设备接入；2-云存。\n        :type AccountType: int\n        """
        self.AccountType = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBalanceResponse(AbstractModel):
    """DescribeBalance返回参数结构体

    """

    def __init__(self):
        """
        :param Balance: 账户余额，单位：分（人民币）。\n        :type Balance: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Balance = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.RequestId = params.get("RequestId")


class DescribeBalanceTransactionsRequest(AbstractModel):
    """DescribeBalanceTransactions请求参数结构体

    """

    def __init__(self):
        """
        :param AccountType: 账户类型：1-设备接入；2-云存。\n        :type AccountType: int\n        :param Offset: 分页游标开始，默认为0开始拉取第一条。\n        :type Offset: int\n        :param Limit: 分页每页数量。\n        :type Limit: int\n        :param Operation: 流水类型：All-全部类型；Recharge-充值；CreateOrder-新购。默认为All\n        :type Operation: str\n        """
        self.AccountType = None
        self.Offset = None
        self.Limit = None
        self.Operation = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBalanceTransactionsResponse(AbstractModel):
    """DescribeBalanceTransactions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 账户流水总数。\n        :type TotalCount: int\n        :param Transactions: 账户流水详情数组。\n        :type Transactions: list of BalanceTransaction\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Transactions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Transactions") is not None:
            self.Transactions = []
            for item in params.get("Transactions"):
                obj = BalanceTransaction()
                obj._deserialize(item)
                self.Transactions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBatchRequest(AbstractModel):
    """DescribeBatch请求参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID\n        :type BatchId: int\n        """
        self.BatchId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchResponse(AbstractModel):
    """DescribeBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 批次详情\n        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoBatch`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoBatch()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeBatchsRequest(AbstractModel):
    """DescribeBatchs请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Limit: 分页的大小，最大100\n        :type Limit: int\n        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        """
        self.ProductId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchsResponse(AbstractModel):
    """DescribeBatchs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批次数量\n        :type TotalCount: int\n        :param Data: 批次列表详情\n        :type Data: list of VideoBatch\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VideoBatch()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCategoryRequest(AbstractModel):
    """DescribeCategory请求参数结构体

    """

    def __init__(self):
        """
        :param Id: Category ID。\n        :type Id: int\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCategoryResponse(AbstractModel):
    """DescribeCategory返回参数结构体

    """

    def __init__(self):
        """
        :param Data: Category详情\n        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.ProductTemplate`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ProductTemplate()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCloudStorageDateRequest(AbstractModel):
    """DescribeCloudStorageDate请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param UserId: 用户ID\n        :type UserId: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.UserId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageDateResponse(AbstractModel):
    """DescribeCloudStorageDate返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 云存日期数组，["2021-01-05","2021-01-06"]\n        :type Data: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeCloudStorageEventsRequest(AbstractModel):
    """DescribeCloudStorageEvents请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h\n        :type StartTime: int\n        :param EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间\n        :type EndTime: int\n        :param Context: 请求上下文, 用作查询游标\n        :type Context: str\n        :param Size: 单次获取的历史数据项目的最大数量, 缺省10\n        :type Size: int\n        :param EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。\n        :type EventId: str\n        :param UserId: 用户ID\n        :type UserId: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.StartTime = None
        self.EndTime = None
        self.Context = None
        self.Size = None
        self.EventId = None
        self.UserId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Context = params.get("Context")
        self.Size = params.get("Size")
        self.EventId = params.get("EventId")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageEventsResponse(AbstractModel):
    """DescribeCloudStorageEvents返回参数结构体

    """

    def __init__(self):
        """
        :param Events: 云存事件列表\n        :type Events: list of CloudStorageEvent\n        :param Context: 请求上下文, 用作查询游标\n        :type Context: str\n        :param Listover: 拉取结果是否已经结束\n        :type Listover: bool\n        :param Total: 拉取结果数量\n        :type Total: int\n        :param VideoURL: 视频播放URL\n        :type VideoURL: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Events = None
        self.Context = None
        self.Listover = None
        self.Total = None
        self.VideoURL = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = CloudStorageEvent()
                obj._deserialize(item)
                self.Events.append(obj)
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        self.Total = params.get("Total")
        self.VideoURL = params.get("VideoURL")
        self.RequestId = params.get("RequestId")


class DescribeCloudStorageRequest(AbstractModel):
    """DescribeCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param UserId: 云存用户ID\n        :type UserId: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.UserId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageResponse(AbstractModel):
    """DescribeCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 云存开启状态，1为开启，0为未开启或已过期\n        :type Status: int\n        :param Type: 云存类型，1为全时云存，2为事件云存\n        :type Type: int\n        :param ExpireTime: 云存套餐过期时间\n        :type ExpireTime: int\n        :param ShiftDuration: 云存回看时长\n        :type ShiftDuration: int\n        :param UserId: 云存用户ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.Type = None
        self.ExpireTime = None
        self.ShiftDuration = None
        self.UserId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.ShiftDuration = params.get("ShiftDuration")
        self.UserId = params.get("UserId")
        self.RequestId = params.get("RequestId")


class DescribeCloudStorageThumbnailRequest(AbstractModel):
    """DescribeCloudStorageThumbnail请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Thumbnail: 缩略图文件名\n        :type Thumbnail: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Thumbnail = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageThumbnailResponse(AbstractModel):
    """DescribeCloudStorageThumbnail返回参数结构体

    """

    def __init__(self):
        """
        :param ThumbnailURL: 缩略图访问地址\n        :type ThumbnailURL: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ThumbnailURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ThumbnailURL = params.get("ThumbnailURL")
        self.RequestId = params.get("RequestId")


class DescribeCloudStorageTimeRequest(AbstractModel):
    """DescribeCloudStorageTime请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Date: 云存日期，例如"2020-01-05"\n        :type Date: str\n        :param StartTime: 开始时间，unix时间\n        :type StartTime: int\n        :param EndTime: 结束时间，unix时间\n        :type EndTime: int\n        :param UserId: 用户ID\n        :type UserId: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Date = None
        self.StartTime = None
        self.EndTime = None
        self.UserId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Date = params.get("Date")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageTimeResponse(AbstractModel):
    """DescribeCloudStorageTime返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 接口返回数据\n        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.CloudStorageTimeData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CloudStorageTimeData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCloudStorageUsersRequest(AbstractModel):
    """DescribeCloudStorageUsers请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Limit: 分页拉取数量\n        :type Limit: int\n        :param Offset: 分页拉取偏移\n        :type Offset: int\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageUsersResponse(AbstractModel):
    """DescribeCloudStorageUsers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 用户总数\n        :type TotalCount: int\n        :param Users: 用户信息\n        :type Users: list of CloudStorageUserInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = CloudStorageUserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDataForwardListRequest(AbstractModel):
    """DescribeDataForwardList请求参数结构体

    """

    def __init__(self):
        """
        :param ProductIds: 产品ID列表\n        :type ProductIds: str\n        """
        self.ProductIds = None


    def _deserialize(self, params):
        self.ProductIds = params.get("ProductIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataForwardListResponse(AbstractModel):
    """DescribeDataForwardList返回参数结构体

    """

    def __init__(self):
        """
        :param DataForwardList: 数据转发列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataForwardList: list of DataForward\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DataForwardList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataForwardList") is not None:
            self.DataForwardList = []
            for item in params.get("DataForwardList"):
                obj = DataForward()
                obj._deserialize(item)
                self.DataForwardList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceActionHistoryRequest(AbstractModel):
    """DescribeDeviceActionHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param MinTime: 开始范围的 unix 毫秒时间戳\n        :type MinTime: int\n        :param MaxTime: 结束范围的 unix 毫秒时间戳\n        :type MaxTime: int\n        :param ActionId: 动作Id\n        :type ActionId: str\n        :param Limit: 查询条数 默认为0 最大不超过500\n        :type Limit: int\n        :param Context: 游标，标识查询位置。\n        :type Context: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.MinTime = None
        self.MaxTime = None
        self.ActionId = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ActionId = params.get("ActionId")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceActionHistoryResponse(AbstractModel):
    """DescribeDeviceActionHistory返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCounts: 总条数\n        :type TotalCounts: int\n        :param ActionHistories: 动作历史
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActionHistories: list of ActionHistory\n        :param Context: 用于标识查询结果的上下文，翻页用。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Context: str\n        :param Listover: 搜索结果是否已经结束。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listover: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCounts = None
        self.ActionHistories = None
        self.Context = None
        self.Listover = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCounts = params.get("TotalCounts")
        if params.get("ActionHistories") is not None:
            self.ActionHistories = []
            for item in params.get("ActionHistories"):
                obj = ActionHistory()
                obj._deserialize(item)
                self.ActionHistories.append(obj)
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        self.RequestId = params.get("RequestId")


class DescribeDeviceCommLogRequest(AbstractModel):
    """DescribeDeviceCommLog请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 开始时间 13位时间戳 单位毫秒\n        :type MinTime: int\n        :param MaxTime: 结束时间 13位时间戳 单位毫秒\n        :type MaxTime: int\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Limit: 返回条数 默认为50\n        :type Limit: int\n        :param Context: 检索上下文\n        :type Context: str\n        :param Type: 类型：shadow 下行，device 上行 默认为空则全部查询\n        :type Type: str\n        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.Limit = None
        self.Context = None
        self.Type = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceCommLogResponse(AbstractModel):
    """DescribeDeviceCommLog返回参数结构体

    """

    def __init__(self):
        """
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。\n        :type Listover: bool\n        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据\n        :type Context: str\n        :param Results: 日志数据结果数组，返回对应时间点及取值。\n        :type Results: list of DeviceCommLogItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceCommLogItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 区间开始时间（Unix 时间戳，毫秒级）\n        :type MinTime: int\n        :param MaxTime: 区间结束时间（Unix 时间戳，毫秒级）\n        :type MaxTime: int\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符\n        :type FieldName: str\n        :param Limit: 返回条数\n        :type Limit: list of int non-negative\n        :param Context: 检索上下文\n        :type Context: str\n        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.FieldName = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.FieldName = params.get("FieldName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        """
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
注意：此字段可能返回 null，表示取不到有效值。\n        :type FieldName: str\n        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listover: bool\n        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Context: str\n        :param Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Results: list of DeviceDataHistoryItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FieldName = None
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备数据\n        :type Data: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDeviceEventHistoryRequest(AbstractModel):
    """DescribeDeviceEventHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Type: 搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件\n        :type Type: str\n        :param StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h\n        :type StartTime: int\n        :param EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间\n        :type EndTime: int\n        :param Context: 搜索上下文, 用作查询游标\n        :type Context: str\n        :param Size: 单次获取的历史数据项目的最大数量, 缺省10\n        :type Size: int\n        :param EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。\n        :type EventId: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Context = None
        self.Size = None
        self.EventId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Context = params.get("Context")
        self.Size = params.get("Size")
        self.EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceEventHistoryResponse(AbstractModel):
    """DescribeDeviceEventHistory返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。\n        :type Context: str\n        :param Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listover: bool\n        :param EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。\n        :type EventHistory: list of EventHistoryItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Context = None
        self.Total = None
        self.Listover = None
        self.EventHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Total = params.get("Total")
        self.Listover = params.get("Listover")
        if params.get("EventHistory") is not None:
            self.EventHistory = []
            for item in params.get("EventHistory"):
                obj = EventHistoryItem()
                obj._deserialize(item)
                self.EventHistory.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活\n        :type Online: int\n        :param LoginTime: 设备最后上线时间\n        :type LoginTime: int\n        :param DevicePsk: 设备密钥\n        :type DevicePsk: str\n        :param EnableState: 设备启用状态\n        :type EnableState: int\n        :param ExpireTime: 设备过期时间\n        :type ExpireTime: int\n        :param LogLevel: 设备的sdk日志等级，0：关闭，1：错误，2：告警，3：信息，4：调试
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogLevel: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.DevicePsk = None
        self.EnableState = None
        self.ExpireTime = None
        self.LogLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.DevicePsk = params.get("DevicePsk")
        self.EnableState = params.get("EnableState")
        self.ExpireTime = params.get("ExpireTime")
        self.LogLevel = params.get("LogLevel")
        self.RequestId = params.get("RequestId")


class DescribeDeviceStatusLogRequest(AbstractModel):
    """DescribeDeviceStatusLog请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 开始时间（毫秒）\n        :type MinTime: int\n        :param MaxTime: 结束时间（毫秒）\n        :type MaxTime: int\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Limit: 返回条数\n        :type Limit: int\n        :param Context: 检索上下文\n        :type Context: str\n        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStatusLogResponse(AbstractModel):
    """DescribeDeviceStatusLog返回参数结构体

    """

    def __init__(self):
        """
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listover: bool\n        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Context: str\n        :param Results: 日志数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Results: list of DeviceStatusLogItem\n        :param TotalCount: 日志数据结果总条数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Listover = None
        self.Context = None
        self.Results = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceStatusLogItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID\n        :type ProductId: str\n        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        :param Limit: 分页的大小，最大100\n        :type Limit: int\n        :param DeviceName: 需要过滤的设备名称\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 设备总数\n        :type TotalCount: int\n        :param Devices: 设备详细信息列表\n        :type Devices: list of DeviceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFirmwareRequest(AbstractModel):
    """DescribeFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareResponse(AbstractModel):
    """DescribeFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param Version: 固件版本号\n        :type Version: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param Md5sum: 固件Md5值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Md5sum: str\n        :param Createtime: 固件上传的秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type Createtime: int\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Version = None
        self.ProductId = None
        self.Name = None
        self.Description = None
        self.Md5sum = None
        self.Createtime = None
        self.ProductName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.ProductId = params.get("ProductId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Md5sum = params.get("Md5sum")
        self.Createtime = params.get("Createtime")
        self.ProductName = params.get("ProductName")
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskDevicesRequest(AbstractModel):
    """DescribeFirmwareTaskDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本\n        :type FirmwareVersion: str\n        :param Filters: 筛选条件\n        :type Filters: list of SearchKeyword\n        :param Offset: 查询偏移量 默认为0\n        :type Offset: int\n        :param Limit: 查询的数量 默认为50\n        :type Limit: int\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDevicesResponse(AbstractModel):
    """DescribeFirmwareTaskDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param Devices: 固件升级任务的设备列表\n        :type Devices: list of DeviceUpdateStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceUpdateStatus()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskDistributionRequest(AbstractModel):
    """DescribeFirmwareTaskDistribution请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件升级任务ID\n        :type TaskId: int\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDistributionResponse(AbstractModel):
    """DescribeFirmwareTaskDistribution返回参数结构体

    """

    def __init__(self):
        """
        :param StatusInfos: 固件升级任务状态分布信息\n        :type StatusInfos: list of StatusStatistic\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StatusInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatusInfos") is not None:
            self.StatusInfos = []
            for item in params.get("StatusInfos"):
                obj = StatusStatistic()
                obj._deserialize(item)
                self.StatusInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskRequest(AbstractModel):
    """DescribeFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件任务ID\n        :type TaskId: int\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskResponse(AbstractModel):
    """DescribeFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 固件任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        :param Status: 固件任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param CreateTime: 固件任务创建时间，单位:秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param Type: 固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductName: str\n        :param UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpgradeMode: str\n        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param OriginalVersion: 原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginalVersion: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.Status = None
        self.CreateTime = None
        self.Type = None
        self.ProductName = None
        self.UpgradeMode = None
        self.ProductId = None
        self.OriginalVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.Type = params.get("Type")
        self.ProductName = params.get("ProductName")
        self.UpgradeMode = params.get("UpgradeMode")
        self.ProductId = params.get("ProductId")
        self.OriginalVersion = params.get("OriginalVersion")
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTaskStatisticsRequest(AbstractModel):
    """DescribeFirmwareTaskStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskStatisticsResponse(AbstractModel):
    """DescribeFirmwareTaskStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessTotal: 升级成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessTotal: int\n        :param FailureTotal: 升级失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailureTotal: int\n        :param UpgradingTotal: 正在升级的设备总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpgradingTotal: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccessTotal = None
        self.FailureTotal = None
        self.UpgradingTotal = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessTotal = params.get("SuccessTotal")
        self.FailureTotal = params.get("FailureTotal")
        self.UpgradingTotal = params.get("UpgradingTotal")
        self.RequestId = params.get("RequestId")


class DescribeFirmwareTasksRequest(AbstractModel):
    """DescribeFirmwareTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param Offset: 查询偏移量\n        :type Offset: int\n        :param Limit: 返回查询结果条数\n        :type Limit: int\n        :param Filters: 搜索过滤条件\n        :type Filters: list of SearchKeyword\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTasksResponse(AbstractModel):
    """DescribeFirmwareTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskInfos: 固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskInfos: list of FirmwareTaskInfo\n        :param Total: 固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskInfos = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = FirmwareTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeForwardRuleRequest(AbstractModel):
    """DescribeForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Skey: 控制台Skey\n        :type Skey: str\n        :param QueueType: 队列类型，0：CMQ，1：Ckafka\n        :type QueueType: int\n        :param Consecretid: 临时密钥\n        :type Consecretid: str\n        """
        self.ProductID = None
        self.Skey = None
        self.QueueType = None
        self.Consecretid = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")
        self.Consecretid = params.get("Consecretid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeForwardRuleResponse(AbstractModel):
    """DescribeForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号\n        :type Endpoint: str\n        :param QueueName: 队列名称\n        :type QueueName: str\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param MsgType: 消息类型 1设备上报信息 2设备状态变化通知 3为全选\n        :type MsgType: int\n        :param Result: 结果 2表示禁用 其他为成功\n        :type Result: int\n        :param RoleName: 角色名\n        :type RoleName: str\n        :param RoleID: 角色ID\n        :type RoleID: int\n        :param QueueRegion: 队列区域\n        :type QueueRegion: str\n        :param QueueType: 队列类型，0：CMQ，1：Ckafka\n        :type QueueType: int\n        :param InstanceId: 实例id， 目前只有Ckafaka会用到\n        :type InstanceId: str\n        :param InstanceName: 实例名称，目前只有Ckafaka会用到\n        :type InstanceName: str\n        :param ErrMsg: 错误消息\n        :type ErrMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Endpoint = None
        self.QueueName = None
        self.ProductID = None
        self.MsgType = None
        self.Result = None
        self.RoleName = None
        self.RoleID = None
        self.QueueRegion = None
        self.QueueType = None
        self.InstanceId = None
        self.InstanceName = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.QueueName = params.get("QueueName")
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Result = params.get("Result")
        self.RoleName = params.get("RoleName")
        self.RoleID = params.get("RoleID")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param Model: 产品数据模板\n        :type Model: :class:`tencentcloud.iotvideo.v20201215.models.ProductModelDefinition`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = ProductModelDefinition()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id\n        :type ProductId: str\n        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详情\n        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoProduct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页的大小，最大100\n        :type Limit: int\n        :param Offset: 偏移量，Offset从0开始\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数\n        :type TotalCount: int\n        :param Data: 产品详情列表\n        :type Data: list of VideoProduct\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VideoProduct()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSDKLogRequest(AbstractModel):
    """DescribeSDKLog请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 日志开始时间\n        :type MinTime: int\n        :param MaxTime: 日志结束时间\n        :type MaxTime: int\n        :param Keywords: 查询关键字，可以同时支持键值查询和文本查询，
例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。
键值或文本可以包含多个，以空格隔开。
其中可以索引的key包括：productid、devicename、loglevel
一个典型的查询示例：productid:7JK1G72JNE devicename:name publish loglevel:WARN一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW publish\n        :type Keywords: str\n        :param Context: 日志检索上下文\n        :type Context: str\n        :param MaxNum: 查询条数\n        :type MaxNum: int\n        """
        self.MinTime = None
        self.MaxTime = None
        self.Keywords = None
        self.Context = None
        self.MaxNum = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.Keywords = params.get("Keywords")
        self.Context = params.get("Context")
        self.MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSDKLogResponse(AbstractModel):
    """DescribeSDKLog返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 日志检索上下文\n        :type Context: str\n        :param Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context\n        :type Listover: bool\n        :param Results: 日志列表\n        :type Results: list of SDKLogItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Context = None
        self.Listover = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = SDKLogItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceCommLogItem(AbstractModel):
    """设备通讯日志查询返回条目

    """

    def __init__(self):
        """
        :param Time: 时间\n        :type Time: str\n        :param Type: 日志类型，device 设备上行，shadow 服务端下行。\n        :type Type: str\n        :param Data: 通讯数据。\n        :type Data: str\n        """
        self.Time = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Type = params.get("Type")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        """
        :param Time: 时间点，毫秒时间戳\n        :type Time: str\n        :param Value: 字段取值\n        :type Value: str\n        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活\n        :type Online: int\n        :param LoginTime: 设备最后上线时间\n        :type LoginTime: int\n        :param DevicePsk: 设备密钥\n        :type DevicePsk: str\n        :param EnableState: 设备启用状态 0为停用 1为可用\n        :type EnableState: int\n        :param ExpireTime: 设备过期时间\n        :type ExpireTime: int\n        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.DevicePsk = None
        self.EnableState = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.DevicePsk = params.get("DevicePsk")
        self.EnableState = params.get("EnableState")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatusLogItem(AbstractModel):
    """设备上下线日志记录

    """

    def __init__(self):
        """
        :param Time: 时间\n        :type Time: str\n        :param Type: 状态类型： Online 上线，Offline 下线\n        :type Type: str\n        :param Data: 日志信息\n        :type Data: str\n        """
        self.Time = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Type = params.get("Type")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceUpdateStatus(AbstractModel):
    """设备固件更新状态

    """

    def __init__(self):
        """
        :param DeviceName: 设备名\n        :type DeviceName: str\n        :param LastProcessTime: 最后处理时间\n        :type LastProcessTime: int\n        :param Status: 状态\n        :type Status: int\n        :param ErrMsg: 错误消息\n        :type ErrMsg: str\n        :param Retcode: 返回码\n        :type Retcode: int\n        :param DstVersion: 目标更新版本\n        :type DstVersion: str\n        :param Percent: 下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Percent: int\n        :param OriVersion: 原版本号
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriVersion: str\n        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        """
        self.DeviceName = None
        self.LastProcessTime = None
        self.Status = None
        self.ErrMsg = None
        self.Retcode = None
        self.DstVersion = None
        self.Percent = None
        self.OriVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.LastProcessTime = params.get("LastProcessTime")
        self.Status = params.get("Status")
        self.ErrMsg = params.get("ErrMsg")
        self.Retcode = params.get("Retcode")
        self.DstVersion = params.get("DstVersion")
        self.Percent = params.get("Percent")
        self.OriVersion = params.get("OriVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditFirmwareRequest(AbstractModel):
    """EditFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID。\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号。\n        :type FirmwareVersion: str\n        :param FirmwareName: 固件名称。\n        :type FirmwareName: str\n        :param FirmwareDescription: 固件描述。\n        :type FirmwareDescription: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.FirmwareName = None
        self.FirmwareDescription = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.FirmwareName = params.get("FirmwareName")
        self.FirmwareDescription = params.get("FirmwareDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditFirmwareResponse(AbstractModel):
    """EditFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        """
        :param TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeStamp: int\n        :param ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        :param DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceName: str\n        :param EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type EventId: str\n        :param Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: str\n        """
        self.TimeStamp = None
        self.ProductId = None
        self.DeviceName = None
        self.EventId = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.TimeStamp = params.get("TimeStamp")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EventId = params.get("EventId")
        self.Type = params.get("Type")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirmwareInfo(AbstractModel):
    """设备固件详细信息

    """

    def __init__(self):
        """
        :param Version: 固件版本\n        :type Version: str\n        :param Md5sum: 固件MD5值\n        :type Md5sum: str\n        :param CreateTime: 固件创建时间\n        :type CreateTime: int\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param Name: 固件名称\n        :type Name: str\n        :param Description: 固件描述\n        :type Description: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        """
        self.Version = None
        self.Md5sum = None
        self.CreateTime = None
        self.ProductName = None
        self.Name = None
        self.Description = None
        self.ProductId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Md5sum = params.get("Md5sum")
        self.CreateTime = params.get("CreateTime")
        self.ProductName = params.get("ProductName")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirmwareTaskInfo(AbstractModel):
    """固件升级任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        """
        self.TaskId = None
        self.Status = None
        self.Type = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateSignedVideoURLRequest(AbstractModel):
    """GenerateSignedVideoURL请求参数结构体

    """

    def __init__(self):
        """
        :param VideoURL: 视频播放原始URL地址\n        :type VideoURL: str\n        :param ExpireTime: 播放链接过期时间\n        :type ExpireTime: int\n        """
        self.VideoURL = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.VideoURL = params.get("VideoURL")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateSignedVideoURLResponse(AbstractModel):
    """GenerateSignedVideoURL返回参数结构体

    """

    def __init__(self):
        """
        :param SignedVideoURL: 视频防盗链播放URL\n        :type SignedVideoURL: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SignedVideoURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignedVideoURL = params.get("SignedVideoURL")
        self.RequestId = params.get("RequestId")


class GetAllFirmwareVersionRequest(AbstractModel):
    """GetAllFirmwareVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        """
        self.ProductID = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAllFirmwareVersionResponse(AbstractModel):
    """GetAllFirmwareVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Version: 固件可用版本列表\n        :type Version: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Version = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.RequestId = params.get("RequestId")


class GetFirmwareURLRequest(AbstractModel):
    """GetFirmwareURL请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本\n        :type FirmwareVersion: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFirmwareURLResponse(AbstractModel):
    """GetFirmwareURL返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 固件URL\n        :type Url: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class ImportModelDefinitionRequest(AbstractModel):
    """ImportModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ModelSchema: 数据模板定义\n        :type ModelSchema: str\n        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportModelDefinitionResponse(AbstractModel):
    """ImportModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InheritCloudStorageUserRequest(AbstractModel):
    """InheritCloudStorageUser请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param UserId: 原始用户ID\n        :type UserId: str\n        :param ToUserId: 目标用户ID\n        :type ToUserId: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.UserId = None
        self.ToUserId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.UserId = params.get("UserId")
        self.ToUserId = params.get("ToUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InheritCloudStorageUserResponse(AbstractModel):
    """InheritCloudStorageUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ListFirmwaresRequest(AbstractModel):
    """ListFirmwares请求参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 获取的页数\n        :type PageNum: int\n        :param PageSize: 分页的大小\n        :type PageSize: int\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Filters: 搜索过滤条件\n        :type Filters: list of SearchKeyword\n        """
        self.PageNum = None
        self.PageSize = None
        self.ProductID = None
        self.Filters = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.ProductID = params.get("ProductID")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFirmwaresResponse(AbstractModel):
    """ListFirmwares返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 固件总数\n        :type TotalCount: int\n        :param Firmwares: 固件列表\n        :type Firmwares: list of FirmwareInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Firmwares = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Firmwares") is not None:
            self.Firmwares = []
            for item in params.get("Firmwares"):
                obj = FirmwareInfo()
                obj._deserialize(item)
                self.Firmwares.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyDataForwardRequest(AbstractModel):
    """ModifyDataForward请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。\n        :type ProductId: str\n        :param ForwardAddr: 转发地址。\n        :type ForwardAddr: str\n        :param DataChose: 1-数据信息转发 2-设备上下线状态转发 3-数据信息转发&设备上下线状态转发\n        :type DataChose: int\n        """
        self.ProductId = None
        self.ForwardAddr = None
        self.DataChose = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ForwardAddr = params.get("ForwardAddr")
        self.DataChose = params.get("DataChose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataForwardResponse(AbstractModel):
    """ModifyDataForward返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDataForwardStatusRequest(AbstractModel):
    """ModifyDataForwardStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。\n        :type ProductId: str\n        :param Status: 转发状态，1启用，0禁用。\n        :type Status: int\n        """
        self.ProductId = None
        self.Status = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataForwardStatusResponse(AbstractModel):
    """ModifyDataForwardStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceLogLevelRequest(AbstractModel):
    """ModifyDeviceLogLevel请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param LogLevel: 日志级别，0：关闭，1：错误，2：告警，3：信息，4：调试\n        :type LogLevel: int\n        """
        self.ProductId = None
        self.DeviceName = None
        self.LogLevel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceLogLevelResponse(AbstractModel):
    """ModifyDeviceLogLevel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属产品id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param EnableState: 要设置的设备状态，1为启用，0为禁用\n        :type EnableState: int\n        """
        self.ProductId = None
        self.DeviceName = None
        self.EnableState = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyForwardRuleRequest(AbstractModel):
    """ModifyForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param MsgType: 消息类型\n        :type MsgType: int\n        :param Skey: 控制台Skey\n        :type Skey: str\n        :param QueueRegion: 队列区域\n        :type QueueRegion: str\n        :param QueueType: 队列类型 0.CMQ 1.CKafka\n        :type QueueType: int\n        :param Consecretid: 临时密钥\n        :type Consecretid: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param QueueID: 队列或主题ID\n        :type QueueID: str\n        :param QueueName: 队列或主题名称\n        :type QueueName: str\n        """
        self.ProductID = None
        self.MsgType = None
        self.Skey = None
        self.QueueRegion = None
        self.QueueType = None
        self.Consecretid = None
        self.InstanceId = None
        self.InstanceName = None
        self.QueueID = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Skey = params.get("Skey")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.Consecretid = params.get("Consecretid")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.QueueID = params.get("QueueID")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardRuleResponse(AbstractModel):
    """ModifyForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号\n        :type Endpoint: str\n        :param ProductID: 产品ID\n        :type ProductID: str\n        :param Result: 结果\n        :type Result: int\n        :param ErrMsg: 错误信息\n        :type ErrMsg: str\n        :param QueueType: 队列类型 0.CMQ 1.CKafka\n        :type QueueType: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Endpoint = None
        self.ProductID = None
        self.Result = None
        self.ErrMsg = None
        self.QueueType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.ProductID = params.get("ProductID")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.QueueType = params.get("QueueType")
        self.RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ModelSchema: 数据模板定义\n        :type ModelSchema: str\n        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id\n        :type ProductId: str\n        :param ProductName: 修改的产品名称 （支持中文、英文、数字、下划线组合，最多不超过20个字符）\n        :type ProductName: str\n        :param ProductDescription: 修改的产品描述 （最多不超过128个字符）\n        :type ProductDescription: str\n        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDescription = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ModelDefine: 模型定义\n        :type ModelDefine: str\n        :param UpdateTime: 更新时间，秒级时间戳\n        :type UpdateTime: int\n        :param CreateTime: 创建时间，秒级时间戳\n        :type CreateTime: int\n        :param CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。\n        :type CategoryModel: str\n        :param NetTypeModel: 产品的连接类型的模型
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetTypeModel: str\n        """
        self.ProductId = None
        self.ModelDefine = None
        self.UpdateTime = None
        self.CreateTime = None
        self.CategoryModel = None
        self.NetTypeModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelDefine = params.get("ModelDefine")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.CategoryModel = params.get("CategoryModel")
        self.NetTypeModel = params.get("NetTypeModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductTemplate(AbstractModel):
    """产品分类实体

    """

    def __init__(self):
        """
        :param Id: 实体ID\n        :type Id: int\n        :param CategoryKey: 分类字段\n        :type CategoryKey: str\n        :param CategoryName: 分类名称\n        :type CategoryName: str\n        :param ParentId: 上层实体ID\n        :type ParentId: int\n        :param ModelTemplate: 物模型\n        :type ModelTemplate: str\n        :param ListOrder: 排列顺序
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListOrder: int\n        :param IconUrl: 分类图标地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type IconUrl: str\n        :param IconUrlGrid: 九宫格图片地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type IconUrlGrid: str\n        """
        self.Id = None
        self.CategoryKey = None
        self.CategoryName = None
        self.ParentId = None
        self.ModelTemplate = None
        self.ListOrder = None
        self.IconUrl = None
        self.IconUrlGrid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CategoryKey = params.get("CategoryKey")
        self.CategoryName = params.get("CategoryName")
        self.ParentId = params.get("ParentId")
        self.ModelTemplate = params.get("ModelTemplate")
        self.ListOrder = params.get("ListOrder")
        self.IconUrl = params.get("IconUrl")
        self.IconUrlGrid = params.get("IconUrlGrid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Topic: 消息发往的主题\n        :type Topic: str\n        :param Payload: 云端下发到设备的控制报文\n        :type Payload: str\n        :param Qos: 消息服务质量等级，取值为0或1\n        :type Qos: int\n        :param PayloadEncoding: Payload的内容编码格式，取值为base64或空。base64表示云端将接收到的base64编码后的报文再转换成二进制报文下发至设备，为空表示不作转换，透传下发至设备\n        :type PayloadEncoding: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.Topic = None
        self.Payload = None
        self.Qos = None
        self.PayloadEncoding = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.Qos = params.get("Qos")
        self.PayloadEncoding = params.get("PayloadEncoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReportAliveDeviceRequest(AbstractModel):
    """ReportAliveDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportAliveDeviceResponse(AbstractModel):
    """ReportAliveDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetCloudStorageRequest(AbstractModel):
    """ResetCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetCloudStorageResponse(AbstractModel):
    """ResetCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RetryDeviceFirmwareTaskRequest(AbstractModel):
    """RetryDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param TaskId: 固件升级任务ID\n        :type TaskId: int\n        """
        self.ProductID = None
        self.DeviceName = None
        self.FirmwareVersion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDeviceFirmwareTaskResponse(AbstractModel):
    """RetryDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SDKLogItem(AbstractModel):
    """SDK日志项

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Level: 日志等级\n        :type Level: str\n        :param DateTime: 日志时间\n        :type DateTime: str\n        :param Content: 日志内容\n        :type Content: str\n        """
        self.ProductID = None
        self.DeviceName = None
        self.Level = None
        self.DateTime = None
        self.Content = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")
        self.Level = params.get("Level")
        self.DateTime = params.get("DateTime")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKeyword(AbstractModel):
    """搜索关键词

    """

    def __init__(self):
        """
        :param Key: 搜索条件的Key\n        :type Key: str\n        :param Value: 搜索条件的值\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetForwardAuthRequest(AbstractModel):
    """SetForwardAuth请求参数结构体

    """

    def __init__(self):
        """
        :param Skey: 控制台Skey\n        :type Skey: str\n        :param QueueType: 消息队列类型  0.CMQ 1.CKafka\n        :type QueueType: int\n        """
        self.Skey = None
        self.QueueType = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetForwardAuthResponse(AbstractModel):
    """SetForwardAuth返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号\n        :type Endpoint: str\n        :param Result: 结果\n        :type Result: int\n        :param RoleName: 角色名\n        :type RoleName: str\n        :param RoleID: 角色ID\n        :type RoleID: int\n        :param QueueType: 消息队列类型  0.CMQ 1.CKafka\n        :type QueueType: int\n        :param ErrMsg: 错误消息\n        :type ErrMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Endpoint = None
        self.Result = None
        self.RoleName = None
        self.RoleID = None
        self.QueueType = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.Result = params.get("Result")
        self.RoleName = params.get("RoleName")
        self.RoleID = params.get("RoleID")
        self.QueueType = params.get("QueueType")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class StatusStatistic(AbstractModel):
    """状态统计信息

    """

    def __init__(self):
        """
        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param Total: 统计总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        """
        self.Status = None
        self.Total = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferCloudStorageRequest(AbstractModel):
    """TransferCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 已开通云存的设备名称\n        :type DeviceName: str\n        :param ToDeviceName: 未开通云存的设备名称\n        :type ToDeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.ToDeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ToDeviceName = params.get("ToDeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferCloudStorageResponse(AbstractModel):
    """TransferCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAIModelChannelRequest(AbstractModel):
    """UpdateAIModelChannel请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 模型ID\n        :type ModelId: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Type: 推送类型。ckafka：消息队列；forward：http/https推送\n        :type Type: str\n        :param ForwardAddress: 第三方推送地址\n        :type ForwardAddress: str\n        :param ForwardKey: 第三方推送密钥，不填写则腾讯云自动生成。\n        :type ForwardKey: str\n        :param CKafkaRegion: ckafka地域\n        :type CKafkaRegion: str\n        :param CKafkaInstance: ckafka实例\n        :type CKafkaInstance: str\n        :param CKafkaTopic: ckafka订阅主题\n        :type CKafkaTopic: str\n        """
        self.ModelId = None
        self.ProductId = None
        self.Type = None
        self.ForwardAddress = None
        self.ForwardKey = None
        self.CKafkaRegion = None
        self.CKafkaInstance = None
        self.CKafkaTopic = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.ProductId = params.get("ProductId")
        self.Type = params.get("Type")
        self.ForwardAddress = params.get("ForwardAddress")
        self.ForwardKey = params.get("ForwardKey")
        self.CKafkaRegion = params.get("CKafkaRegion")
        self.CKafkaInstance = params.get("CKafkaInstance")
        self.CKafkaTopic = params.get("CKafkaTopic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIModelChannelResponse(AbstractModel):
    """UpdateAIModelChannel返回参数结构体

    """

    def __init__(self):
        """
        :param ForwardKey: 第三方推送密钥，如果选择自动生成则会返回此字段
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForwardKey: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ForwardKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ForwardKey = params.get("ForwardKey")
        self.RequestId = params.get("RequestId")


class UploadFirmwareRequest(AbstractModel):
    """UploadFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID\n        :type ProductID: str\n        :param FirmwareVersion: 固件版本号\n        :type FirmwareVersion: str\n        :param Md5sum: 固件的MD5值\n        :type Md5sum: str\n        :param FileSize: 固件的大小\n        :type FileSize: int\n        :param FirmwareName: 固件名称\n        :type FirmwareName: str\n        :param FirmwareDescription: 固件描述\n        :type FirmwareDescription: str\n        """
        self.ProductID = None
        self.FirmwareVersion = None
        self.Md5sum = None
        self.FileSize = None
        self.FirmwareName = None
        self.FirmwareDescription = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.FirmwareVersion = params.get("FirmwareVersion")
        self.Md5sum = params.get("Md5sum")
        self.FileSize = params.get("FileSize")
        self.FirmwareName = params.get("FirmwareName")
        self.FirmwareDescription = params.get("FirmwareDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFirmwareResponse(AbstractModel):
    """UploadFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VideoBatch(AbstractModel):
    """批次元数据

    """

    def __init__(self):
        """
        :param Id: 批次ID\n        :type Id: int\n        :param UserId: 用户ID\n        :type UserId: str\n        :param ProductId: 产品ID\n        :type ProductId: str\n        :param Status: 状态：1：待创建设备 2：创建中 3：已完成\n        :type Status: int\n        :param DevPre: 设备前缀\n        :type DevPre: str\n        :param DevNum: 设备数量\n        :type DevNum: int\n        :param DevNumCreated: 已创建设备数量\n        :type DevNumCreated: int\n        :param BatchURL: 批次下载地址\n        :type BatchURL: str\n        :param CreateTime: 创建时间。unix时间戳\n        :type CreateTime: int\n        :param UpdateTime: 修改时间。unix时间戳\n        :type UpdateTime: int\n        """
        self.Id = None
        self.UserId = None
        self.ProductId = None
        self.Status = None
        self.DevPre = None
        self.DevNum = None
        self.DevNumCreated = None
        self.BatchURL = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.UserId = params.get("UserId")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.DevPre = params.get("DevPre")
        self.DevNum = params.get("DevNum")
        self.DevNumCreated = params.get("DevNumCreated")
        self.BatchURL = params.get("BatchURL")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoProduct(AbstractModel):
    """video产品元数据

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param ProductName: 产品名称\n        :type ProductName: str\n        :param DeviceType: 产品设备类型（普通设备)	1.普通设备\n        :type DeviceType: int\n        :param EncryptionType: 认证方式：2：PSK\n        :type EncryptionType: int\n        :param Features: 设备功能码\n        :type Features: list of str\n        :param ChipOs: 操作系统\n        :type ChipOs: str\n        :param ChipManufactureId: 芯片厂商id\n        :type ChipManufactureId: str\n        :param ChipId: 芯片id\n        :type ChipId: str\n        :param ProductDescription: 产品描述信息\n        :type ProductDescription: str\n        :param CreateTime: 创建时间unix时间戳\n        :type CreateTime: int\n        :param UpdateTime: 修改时间unix时间戳\n        :type UpdateTime: int\n        """
        self.ProductId = None
        self.ProductName = None
        self.DeviceType = None
        self.EncryptionType = None
        self.Features = None
        self.ChipOs = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductDescription = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.DeviceType = params.get("DeviceType")
        self.EncryptionType = params.get("EncryptionType")
        self.Features = params.get("Features")
        self.ChipOs = params.get("ChipOs")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductDescription = params.get("ProductDescription")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WakeUpDeviceRequest(AbstractModel):
    """WakeUpDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WakeUpDeviceResponse(AbstractModel):
    """WakeUpDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")