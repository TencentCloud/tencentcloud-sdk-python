# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class ActionHistory(AbstractModel):
    """查询设备历史

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ActionId: 动作Id
        :type ActionId: str
        :param ActionName: 动作名称
        :type ActionName: str
        :param ReqTime: 请求时间
        :type ReqTime: int
        :param RspTime: 响应时间
        :type RspTime: int
        :param InputParams: 输入参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InputParams: str
        :param OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param Calling: 调用方式
        :type Calling: str
        :param ClientToken: 调用Id
        :type ClientToken: str
        :param Status: 调用状态
        :type Status: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BalanceTransaction(AbstractModel):
    """账户流水

    """

    def __init__(self):
        """
        :param AccountType: 账户类型：1-设备接入 2-云存。
        :type AccountType: int
        :param Operation: 账户变更类型：Rechareg-充值；CreateOrder-新购。
        :type Operation: str
        :param DealId: 流水ID。
        :type DealId: str
        :param Amount: 变更金额，单位：分（人民币）。
        :type Amount: int
        :param Balance: 变更后账户余额，单位：分（人民币）。
        :type Balance: int
        :param OperationTime: 变更时间。
        :type OperationTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchUpdateFirmwareRequest(AbstractModel):
    """BatchUpdateFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件新版本号
        :type FirmwareVersion: str
        :param FirmwareOriVersion: 固件原版本号，根据文件列表升级固件不需要填写此参数
        :type FirmwareOriVersion: str
        :param UpgradeMethod: 升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式
        :type UpgradeMethod: int
        :param FileName: 设备列表文件名称，根据文件列表升级固件需要填写此参数
        :type FileName: str
        :param FileMd5: 设备列表的文件md5值
        :type FileMd5: str
        :param FileSize: 设备列表的文件大小值
        :type FileSize: int
        :param DeviceNames: 需要升级的设备名称列表
        :type DeviceNames: list of str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BatchUpdateFirmwareResponse(AbstractModel):
    """BatchUpdateFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelDeviceFirmwareTaskRequest(AbstractModel):
    """CancelDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件升级任务ID
        :type TaskId: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelDeviceFirmwareTaskResponse(AbstractModel):
    """CancelDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CheckForwardAuthRequest(AbstractModel):
    """CheckForwardAuth请求参数结构体

    """

    def __init__(self):
        """
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 队列类型
        :type QueueType: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CheckForwardAuthResponse(AbstractModel):
    """CheckForwardAuth返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param Result: 结果
        :type Result: int
        :param Productid: 产品ID
        :type Productid: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloudStorageEvent(AbstractModel):
    """云存事件

    """

    def __init__(self):
        """
        :param StartTime: 事件起始时间（Unix 时间戳，秒级
        :type StartTime: int
        :param EndTime: 事件结束时间（Unix 时间戳，秒级
        :type EndTime: int
        :param Thumbnail: 事件缩略图
        :type Thumbnail: str
        :param EventId: 事件ID
        :type EventId: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloudStorageTimeData(AbstractModel):
    """云存时间轴接口返回数据

    """

    def __init__(self):
        """
        :param TimeList: 云存时间轴信息列表
        :type TimeList: list of CloudStorageTimeInfo
        :param VideoURL: 播放地址
        :type VideoURL: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CloudStorageTimeInfo(AbstractModel):
    """云存时间轴信息

    """

    def __init__(self):
        """
        :param StartTime: 开始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateBatchRequest(AbstractModel):
    """CreateBatch请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DevNum: 批次创建的设备数量
        :type DevNum: int
        :param DevPre: 批次创建的设备前缀。不超过24个字符
        :type DevPre: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateBatchResponse(AbstractModel):
    """CreateBatch返回参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID
        :type BatchId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCloudStorageRequest(AbstractModel):
    """CreateCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param PackageId: 云存套餐ID：
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
ye1w7d : 事件7天存储周套餐。
        :type PackageId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.PackageId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.PackageId = params.get("PackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCloudStorageResponse(AbstractModel):
    """CreateCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateForwardRuleRequest(AbstractModel):
    """CreateForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueRegion: 队列区域
        :type QueueRegion: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param Consecretid: 临时密钥
        :type Consecretid: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param QueueID: 队列或主题ID
        :type QueueID: str
        :param QueueName: 队列或主题名称
        :type QueueName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateForwardRuleResponse(AbstractModel):
    """CreateForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param QueueName: 队列名
        :type QueueName: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Result: 结果
        :type Result: int
        :param RoleName: 角色名称
        :type RoleName: str
        :param RoleID: 角色ID
        :type RoleID: int
        :param QueueRegion: 队列区
        :type QueueRegion: str
        :param QueueType: 消息队列的类型。 0：CMQ，1：CKafaka
        :type QueueType: int
        :param InstanceId: 实例id， 目前只有Ckafaka会用到
        :type InstanceId: str
        :param InstanceName: 实例名称，目前只有Ckafaka会用到
        :type InstanceName: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称
        :type ProductName: str
        :param DeviceType: 产品设备类型
        :type DeviceType: int
        :param ProductVaildYears: 产品有效期
        :type ProductVaildYears: int
        :param Features: 设备功能码
        :type Features: list of str
        :param ChipOs: 设备操作系统
        :type ChipOs: str
        :param ChipManufactureId: 芯片厂商id
        :type ChipManufactureId: str
        :param ChipId: 芯片id
        :type ChipId: str
        :param ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param EncryptionType: 认证方式。2 PSK
        :type EncryptionType: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoProduct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTaskFileUrlRequest(AbstractModel):
    """CreateTaskFileUrl请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateTaskFileUrlResponse(AbstractModel):
    """CreateTaskFileUrl返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 任务文件上传链接
        :type Url: str
        :param FileName: 任务文件名
        :type FileName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.FileName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileName = params.get("FileName")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。
        :type ProductId: str
        :param DeviceName: 设备名称。
        :type DeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteFirmwareRequest(AbstractModel):
    """DeleteFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteFirmwareResponse(AbstractModel):
    """DeleteFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteForwardRuleRequest(AbstractModel):
    """DeleteForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param QueueName: 队列名称
        :type QueueName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteForwardRuleResponse(AbstractModel):
    """DeleteForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param QueueName: 队列名称
        :type QueueName: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param Result: 删除结果
        :type Result: int
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBalanceRequest(AbstractModel):
    """DescribeBalance请求参数结构体

    """

    def __init__(self):
        """
        :param AccountType: 账户类型：1-设备接入；2-云存。
        :type AccountType: int
        """
        self.AccountType = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBalanceResponse(AbstractModel):
    """DescribeBalance返回参数结构体

    """

    def __init__(self):
        """
        :param Balance: 账户余额，单位：分（人民币）。
        :type Balance: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Balance = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBalanceTransactionsRequest(AbstractModel):
    """DescribeBalanceTransactions请求参数结构体

    """

    def __init__(self):
        """
        :param AccountType: 账户类型：1-设备接入；2-云存。
        :type AccountType: int
        :param Offset: 分页游标开始，默认为0开始拉取第一条。
        :type Offset: int
        :param Limit: 分页每页数量。
        :type Limit: int
        :param Operation: 流水类型：All-全部类型；Recharge-充值；CreateOrder-新购。
        :type Operation: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBalanceTransactionsResponse(AbstractModel):
    """DescribeBalanceTransactions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 账户流水总数。
        :type TotalCount: int
        :param Transactions: 账户流水详情数组。
        :type Transactions: list of BalanceTransaction
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBatchRequest(AbstractModel):
    """DescribeBatch请求参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID
        :type BatchId: int
        """
        self.BatchId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBatchResponse(AbstractModel):
    """DescribeBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 批次详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoBatch`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoBatch()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBatchsRequest(AbstractModel):
    """DescribeBatchs请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param Limit: 分页的大小，最大100
        :type Limit: int
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBatchsResponse(AbstractModel):
    """DescribeBatchs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批次数量
        :type TotalCount: int
        :param Data: 批次列表详情
        :type Data: list of VideoBatch
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCategoryRequest(AbstractModel):
    """DescribeCategory请求参数结构体

    """

    def __init__(self):
        """
        :param Id: Category ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCategoryResponse(AbstractModel):
    """DescribeCategory返回参数结构体

    """

    def __init__(self):
        """
        :param Data: Category详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.ProductTemplate`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ProductTemplate()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageDateRequest(AbstractModel):
    """DescribeCloudStorageDate请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageDateResponse(AbstractModel):
    """DescribeCloudStorageDate返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 云存日期数组，["2021-01-05","2021-01-06"]
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageEventsRequest(AbstractModel):
    """DescribeCloudStorageEvents请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param Context: 请求上下文, 用作查询游标
        :type Context: str
        :param Size: 单次获取的历史数据项目的最大数量, 缺省10
        :type Size: int
        :param EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.StartTime = None
        self.EndTime = None
        self.Context = None
        self.Size = None
        self.EventId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageEventsResponse(AbstractModel):
    """DescribeCloudStorageEvents返回参数结构体

    """

    def __init__(self):
        """
        :param Events: 云存事件列表
        :type Events: list of CloudStorageEvent
        :param Context: 请求上下文, 用作查询游标
        :type Context: str
        :param Listover: 拉取结果是否已经结束
        :type Listover: bool
        :param Total: 拉取结果数量
        :type Total: int
        :param VideoURL: 视频播放URL
        :type VideoURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageRequest(AbstractModel):
    """DescribeCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageResponse(AbstractModel):
    """DescribeCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 云存开启状态，1为开启，0为未开启或已过期
        :type Status: int
        :param Type: 云存类型，1为全时云存，2为事件云存
        :type Type: int
        :param ExpireTime: 云存套餐过期时间
        :type ExpireTime: int
        :param ShiftDuration: 云存回看时长
        :type ShiftDuration: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Type = None
        self.ExpireTime = None
        self.ShiftDuration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.ExpireTime = params.get("ExpireTime")
        self.ShiftDuration = params.get("ShiftDuration")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageThumbnailRequest(AbstractModel):
    """DescribeCloudStorageThumbnail请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Thumbnail: 缩略图文件名
        :type Thumbnail: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageThumbnailResponse(AbstractModel):
    """DescribeCloudStorageThumbnail返回参数结构体

    """

    def __init__(self):
        """
        :param ThumbnailURL: 缩略图访问地址
        :type ThumbnailURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ThumbnailURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ThumbnailURL = params.get("ThumbnailURL")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageTimeRequest(AbstractModel):
    """DescribeCloudStorageTime请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Date: 云存日期，例如"2020-01-05"
        :type Date: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Date = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCloudStorageTimeResponse(AbstractModel):
    """DescribeCloudStorageTime返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 接口返回数据
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.CloudStorageTimeData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CloudStorageTimeData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceActionHistoryRequest(AbstractModel):
    """DescribeDeviceActionHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param MinTime: 开始范围的 unix 毫秒时间戳
        :type MinTime: int
        :param MaxTime: 结束范围的 unix 毫秒时间戳
        :type MaxTime: int
        :param ActionId: 动作Id
        :type ActionId: str
        :param Limit: 查询条数
        :type Limit: int
        :param Context: 游标，标识查询位置。
        :type Context: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceActionHistoryResponse(AbstractModel):
    """DescribeDeviceActionHistory返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCounts: 总条数
        :type TotalCounts: int
        :param ActionHistories: 动作历史
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionHistories: list of ActionHistory
        :param Context: 用于标识查询结果的上下文，翻页用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Listover: 搜索结果是否已经结束。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceCommLogRequest(AbstractModel):
    """DescribeDeviceCommLog请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 开始时间
        :type MinTime: int
        :param MaxTime: 结束时间
        :type MaxTime: int
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Limit: 返回条数
        :type Limit: int
        :param Context: 检索上下文
        :type Context: str
        :param Type: 类型：shadow 下行，device 上行
        :type Type: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceCommLogResponse(AbstractModel):
    """DescribeDeviceCommLog返回参数结构体

    """

    def __init__(self):
        """
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
        :type Listover: bool
        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
        :type Context: str
        :param Results: 日志数据结果数组，返回对应时间点及取值。
        :type Results: list of DeviceCommLogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 区间开始时间（Unix 时间戳，毫秒级）
        :type MinTime: int
        :param MaxTime: 区间结束时间（Unix 时间戳，毫秒级）
        :type MaxTime: int
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
        :type FieldName: str
        :param Limit: 返回条数
        :type Limit: list of int non-negative
        :param Context: 检索上下文
        :type Context: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        """
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备数据
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceEventHistoryRequest(AbstractModel):
    """DescribeDeviceEventHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Type: 搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件
        :type Type: str
        :param StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param Context: 搜索上下文, 用作查询游标
        :type Context: str
        :param Size: 单次获取的历史数据项目的最大数量, 缺省10
        :type Size: int
        :param EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceEventHistoryResponse(AbstractModel):
    """DescribeDeviceEventHistory返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type EventHistory: list of EventHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活
        :type Online: int
        :param LoginTime: 设备最后上线时间
        :type LoginTime: int
        :param DevicePsk: 设备密钥
        :type DevicePsk: str
        :param EnableState: 设备启用状态
        :type EnableState: int
        :param ExpireTime: 设备过期时间
        :type ExpireTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.DevicePsk = None
        self.EnableState = None
        self.ExpireTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.DevicePsk = params.get("DevicePsk")
        self.EnableState = params.get("EnableState")
        self.ExpireTime = params.get("ExpireTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param Limit: 分页的大小，最大100
        :type Limit: int
        :param DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 设备总数
        :type TotalCount: int
        :param Devices: 设备详细信息列表
        :type Devices: list of DeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareRequest(AbstractModel):
    """DescribeFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareResponse(AbstractModel):
    """DescribeFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param Version: 固件版本号
        :type Version: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Md5sum: 固件Md5值
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5sum: str
        :param Createtime: 固件上传的秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Createtime: int
        :param ProductName: 产品名称
        :type ProductName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskDevicesRequest(AbstractModel):
    """DescribeFirmwareTaskDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param Filters: 筛选条件
        :type Filters: list of SearchKeyword
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询的数量
        :type Limit: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskDevicesResponse(AbstractModel):
    """DescribeFirmwareTaskDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Devices: 固件升级任务的设备列表
        :type Devices: list of DeviceUpdateStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskDistributionRequest(AbstractModel):
    """DescribeFirmwareTaskDistribution请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件升级任务ID
        :type TaskId: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskDistributionResponse(AbstractModel):
    """DescribeFirmwareTaskDistribution返回参数结构体

    """

    def __init__(self):
        """
        :param StatusInfos: 固件升级任务状态分布信息
        :type StatusInfos: list of StatusStatistic
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskRequest(AbstractModel):
    """DescribeFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件任务ID
        :type TaskId: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskResponse(AbstractModel):
    """DescribeFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 固件任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param Status: 固件任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreateTime: 固件任务创建时间，单位:秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param Type: 固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeMode: str
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param OriginalVersion: 原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskStatisticsRequest(AbstractModel):
    """DescribeFirmwareTaskStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTaskStatisticsResponse(AbstractModel):
    """DescribeFirmwareTaskStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessTotal: 升级成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotal: int
        :param FailureTotal: 升级失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureTotal: int
        :param UpgradingTotal: 正在升级的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradingTotal: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessTotal = None
        self.FailureTotal = None
        self.UpgradingTotal = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessTotal = params.get("SuccessTotal")
        self.FailureTotal = params.get("FailureTotal")
        self.UpgradingTotal = params.get("UpgradingTotal")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTasksRequest(AbstractModel):
    """DescribeFirmwareTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 返回查询结果条数
        :type Limit: int
        :param Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFirmwareTasksResponse(AbstractModel):
    """DescribeFirmwareTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskInfos: 固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfos: list of FirmwareTaskInfo
        :param Total: 固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeForwardRuleRequest(AbstractModel):
    """DescribeForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 队列类型，0：CMQ，1：Ckafka
        :type QueueType: int
        :param Consecretid: 临时密钥
        :type Consecretid: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeForwardRuleResponse(AbstractModel):
    """DescribeForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param QueueName: 队列名称
        :type QueueName: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Result: 结果
        :type Result: int
        :param RoleName: 角色名
        :type RoleName: str
        :param RoleID: 角色ID
        :type RoleID: int
        :param QueueRegion: 队列区域
        :type QueueRegion: str
        :param QueueType: 队列类型，0：CMQ，1：Ckafka
        :type QueueType: int
        :param InstanceId: 实例id， 目前只有Ckafaka会用到
        :type InstanceId: str
        :param InstanceName: 实例名称，目前只有Ckafaka会用到
        :type InstanceName: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param Model: 产品数据模板
        :type Model: :class:`tencentcloud.iotvideo.v20201215.models.ProductModelDefinition`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = ProductModelDefinition()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoProduct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页的大小，最大100
        :type Limit: int
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param Data: 产品详情列表
        :type Data: list of VideoProduct
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeviceCommLogItem(AbstractModel):
    """设备通讯日志查询返回条目

    """

    def __init__(self):
        """
        :param Time: 时间
        :type Time: str
        :param Type: 日志类型，device 设备上行，shadow 服务端下行。
        :type Type: str
        :param Data: 通讯数据。
        :type Data: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        """
        :param Time: 时间点，毫秒时间戳
        :type Time: str
        :param Value: 字段取值
        :type Value: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活
        :type Online: int
        :param LoginTime: 设备最后上线时间
        :type LoginTime: int
        :param DevicePsk: 设备密钥
        :type DevicePsk: str
        :param EnableState: 设备启用状态
        :type EnableState: int
        :param ExpireTime: 设备过期时间
        :type ExpireTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeviceUpdateStatus(AbstractModel):
    """设备固件更新状态

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param LastProcessTime: 最后处理时间
        :type LastProcessTime: int
        :param Status: 状态
        :type Status: int
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param Retcode: 返回码
        :type Retcode: int
        :param DstVersion: 目标更新版本
        :type DstVersion: str
        :param Percent: 下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param OriVersion: 原版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriVersion: str
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EditFirmwareRequest(AbstractModel):
    """EditFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID。
        :type ProductID: str
        :param FirmwareVersion: 固件版本号。
        :type FirmwareVersion: str
        :param FirmwareName: 固件名称。
        :type FirmwareName: str
        :param FirmwareDescription: 固件描述。
        :type FirmwareDescription: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EditFirmwareResponse(AbstractModel):
    """EditFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        """
        :param TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        :param ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FirmwareInfo(AbstractModel):
    """设备固件详细信息

    """

    def __init__(self):
        """
        :param Version: 固件版本
        :type Version: str
        :param Md5sum: 固件MD5值
        :type Md5sum: str
        :param CreateTime: 固件创建时间
        :type CreateTime: int
        :param ProductName: 产品名称
        :type ProductName: str
        :param Name: 固件名称
        :type Name: str
        :param Description: 固件描述
        :type Description: str
        :param ProductId: 产品ID
        :type ProductId: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FirmwareTaskInfo(AbstractModel):
    """固件升级任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GenerateSignedVideoURLRequest(AbstractModel):
    """GenerateSignedVideoURL请求参数结构体

    """

    def __init__(self):
        """
        :param VideoURL: 视频播放原始URL地址
        :type VideoURL: str
        :param ExpireTime: 播放链接过期时间
        :type ExpireTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GenerateSignedVideoURLResponse(AbstractModel):
    """GenerateSignedVideoURL返回参数结构体

    """

    def __init__(self):
        """
        :param SignedVideoURL: 视频防盗链播放URL
        :type SignedVideoURL: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SignedVideoURL = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignedVideoURL = params.get("SignedVideoURL")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetAllFirmwareVersionRequest(AbstractModel):
    """GetAllFirmwareVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        """
        self.ProductID = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetAllFirmwareVersionResponse(AbstractModel):
    """GetAllFirmwareVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Version: 无
        :type Version: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Version = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetFirmwareURLRequest(AbstractModel):
    """GetFirmwareURL请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetFirmwareURLResponse(AbstractModel):
    """GetFirmwareURL返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 固件URL
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportModelDefinitionRequest(AbstractModel):
    """ImportModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportModelDefinitionResponse(AbstractModel):
    """ImportModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListFirmwaresRequest(AbstractModel):
    """ListFirmwares请求参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 获取的页数
        :type PageNum: int
        :param PageSize: 分页的大小
        :type PageSize: int
        :param ProductID: 产品ID
        :type ProductID: str
        :param Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListFirmwaresResponse(AbstractModel):
    """ListFirmwares返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 固件总数
        :type TotalCount: int
        :param Firmwares: 固件列表
        :type Firmwares: list of FirmwareInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属产品id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param EnableState: 要设置的设备状态，1为启用，0为禁用
        :type EnableState: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyForwardRuleRequest(AbstractModel):
    """ModifyForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueRegion: 队列区域
        :type QueueRegion: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param Consecretid: 临时密钥
        :type Consecretid: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param QueueID: 队列或主题ID
        :type QueueID: str
        :param QueueName: 队列或主题名称
        :type QueueName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyForwardRuleResponse(AbstractModel):
    """ModifyForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param Result: 结果
        :type Result: int
        :param ErrMsg: 错误信息
        :type ErrMsg: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id
        :type ProductId: str
        :param ProductName: 修改的产品名称
        :type ProductName: str
        :param ProductDescription: 修改的产品描述
        :type ProductDescription: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelDefine: 模型定义
        :type ModelDefine: str
        :param UpdateTime: 更新时间，秒级时间戳
        :type UpdateTime: int
        :param CreateTime: 创建时间，秒级时间戳
        :type CreateTime: int
        :param CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryModel: str
        :param NetTypeModel: 产品的连接类型的模型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetTypeModel: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ProductTemplate(AbstractModel):
    """产品分类实体

    """

    def __init__(self):
        """
        :param Id: 实体ID
        :type Id: int
        :param CategoryKey: 分类字段
        :type CategoryKey: str
        :param CategoryName: 分类名称
        :type CategoryName: str
        :param ParentId: 上层实体ID
        :type ParentId: int
        :param ModelTemplate: 物模型
        :type ModelTemplate: str
        :param ListOrder: 排列顺序
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOrder: int
        :param IconUrl: 分类图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param IconUrlGrid: 九宫格图片地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrlGrid: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetCloudStorageRequest(AbstractModel):
    """ResetCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetCloudStorageResponse(AbstractModel):
    """ResetCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RetryDeviceFirmwareTaskRequest(AbstractModel):
    """RetryDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param TaskId: 固件升级任务ID
        :type TaskId: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RetryDeviceFirmwareTaskResponse(AbstractModel):
    """RetryDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SearchKeyword(AbstractModel):
    """搜索关键词

    """

    def __init__(self):
        """
        :param Key: 搜索条件的Key
        :type Key: str
        :param Value: 搜索条件的值
        :type Value: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetForwardAuthRequest(AbstractModel):
    """SetForwardAuth请求参数结构体

    """

    def __init__(self):
        """
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 消息队列类型
        :type QueueType: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetForwardAuthResponse(AbstractModel):
    """SetForwardAuth返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param Result: 结果
        :type Result: int
        :param RoleName: 角色名
        :type RoleName: str
        :param RoleID: 角色ID
        :type RoleID: int
        :param QueueType: 消息队列类型
        :type QueueType: int
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StatusStatistic(AbstractModel):
    """状态统计信息

    """

    def __init__(self):
        """
        :param Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Total: 统计总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TransferCloudStorageRequest(AbstractModel):
    """TransferCloudStorage请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 已开通云存的设备名称
        :type DeviceName: str
        :param ToDeviceName: 未开通云存的设备名称
        :type ToDeviceName: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TransferCloudStorageResponse(AbstractModel):
    """TransferCloudStorage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UploadFirmwareRequest(AbstractModel):
    """UploadFirmware请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param Md5sum: 固件的MD5值
        :type Md5sum: str
        :param FileSize: 固件的大小
        :type FileSize: int
        :param FirmwareName: 固件名称
        :type FirmwareName: str
        :param FirmwareDescription: 固件描述
        :type FirmwareDescription: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UploadFirmwareResponse(AbstractModel):
    """UploadFirmware返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoBatch(AbstractModel):
    """批次元数据

    """

    def __init__(self):
        """
        :param Id: 批次ID
        :type Id: int
        :param UserId: 用户ID
        :type UserId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param Status: 状态：1：待创建设备 2：创建中 3：已完成
        :type Status: int
        :param DevPre: 设备前缀
        :type DevPre: str
        :param DevNum: 设备数量
        :type DevNum: int
        :param DevNumCreated: 已创建设备数量
        :type DevNumCreated: int
        :param BatchURL: 批次下载地址
        :type BatchURL: str
        :param CreateTime: 创建时间。unix时间戳
        :type CreateTime: int
        :param UpdateTime: 修改时间。unix时间戳
        :type UpdateTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoProduct(AbstractModel):
    """video产品元数据

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param DeviceType: 产品设备类型（普通设备)	1.普通设备
        :type DeviceType: int
        :param EncryptionType: 认证方式：2：PSK
        :type EncryptionType: int
        :param Features: 设备功能码
        :type Features: list of str
        :param ChipOs: 操作系统
        :type ChipOs: str
        :param ChipManufactureId: 芯片厂商id
        :type ChipManufactureId: str
        :param ChipId: 芯片id
        :type ChipId: str
        :param ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param CreateTime: 创建时间unix时间戳
        :type CreateTime: int
        :param UpdateTime: 修改时间unix时间戳
        :type UpdateTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        