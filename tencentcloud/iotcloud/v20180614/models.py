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

from tencentcloud.common.abstract_model import AbstractModel


class Attribute(AbstractModel):
    """设备属性

    """

    def __init__(self):
        """
        :param Tags: 属性列表
        :type Tags: list of DeviceTag
        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)


class BatchPublishMessage(AbstractModel):
    """批量发消息请求

    """

    def __init__(self):
        """
        :param Topic: 消息发往的主题。为 Topic 权限中去除 ProductID 和 DeviceName 的部分，如 “event”
        :type Topic: str
        :param Payload: 消息内容
        :type Payload: str
        """
        self.Topic = None
        self.Payload = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")


class BatchUpdateShadow(AbstractModel):
    """批量更新设备影子任务

    """

    def __init__(self):
        """
        :param Desired: 设备影子的期望状态，格式为 Json 对象序列化之后的字符串
        :type Desired: str
        """
        self.Desired = None


    def _deserialize(self, params):
        self.Desired = params.get("Desired")


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 任务 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID 。创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。
        :type DeviceName: str
        :param Attribute: 设备属性
        :type Attribute: :class:`tencentcloud.iotcloud.v20180614.models.Attribute`
        :param DefinedPsk: 是否使用自定义PSK，默认不使用
        :type DefinedPsk: str
        :param Isp: 运营商类型，当产品是NB-IoT产品时，此字段必填。1表示中国电信，2表示中国移动，3表示中国联通
        :type Isp: int
        :param Imei: IMEI，当产品是NB-IoT产品时，此字段必填
        :type Imei: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Attribute = None
        self.DefinedPsk = None
        self.Isp = None
        self.Imei = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        if params.get("Attribute") is not None:
            self.Attribute = Attribute()
            self.Attribute._deserialize(params.get("Attribute"))
        self.DefinedPsk = params.get("DefinedPsk")
        self.Isp = params.get("Isp")
        self.Imei = params.get("Imei")


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DevicePsk: 对称加密密钥，base64编码。采用对称加密时返回该参数
        :type DevicePsk: str
        :param DeviceCert: 设备证书，用于 TLS 建立链接时校验客户端身份。采用非对称加密时返回该参数
        :type DeviceCert: str
        :param DevicePrivateKey: 设备私钥，用于 TLS 建立链接时校验客户端身份，腾讯云后台不保存，请妥善保管。采用非对称加密时返回该参数
        :type DevicePrivateKey: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.RequestId = params.get("RequestId")


class CreateMultiDeviceRequest(AbstractModel):
    """CreateMultiDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID。创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param DeviceNames: 批量创建的设备名数组，单次最多创建 100 个设备。命名规则：[a-zA-Z0-9:_-]{1,48}
        :type DeviceNames: list of str
        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")


class CreateMultiDeviceResponse(AbstractModel):
    """CreateMultiDevice返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，腾讯云生成全局唯一的任务 ID，有效期一个月，一个月之后任务失效。可以调用获取创建多设备任务状态接口获取该任务的执行状态，当状态为成功时，可以调用获取创建多设备任务结果接口获取该任务的结果
        :type TaskId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        """
        self.ProductName = None
        self.ProductProperties = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductId: 产品 ID，腾讯云生成全局唯一 ID
        :type ProductId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ProductName = None
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskType: 任务类型，取值为 “UpdateShadow” 或者 “PublishMessage”
        :type TaskType: str
        :param ProductId: 执行任务的产品ID
        :type ProductId: str
        :param DeviceNameFilter: 执行任务的设备名的正则表达式
        :type DeviceNameFilter: str
        :param ScheduleTimeInSeconds: 任务开始执行的时间。 取值为 Unix 时间戳，单位秒，且需大于等于当前时间时间戳，0为系统当前时间时间戳，即立即执行，最大为当前时间86400秒后，超过则取值为当前时间86400秒后
        :type ScheduleTimeInSeconds: int
        :param Tasks: 任务描述细节，描述见下 Task
        :type Tasks: :class:`tencentcloud.iotcloud.v20180614.models.Task`
        :param MaxExecutionTimeInSeconds: 最长执行时间，单位秒，被调度后超过此时间仍未有结果则视为任务失败。取值为0-86400，默认为86400
        :type MaxExecutionTimeInSeconds: int
        """
        self.TaskType = None
        self.ProductId = None
        self.DeviceNameFilter = None
        self.ScheduleTimeInSeconds = None
        self.Tasks = None
        self.MaxExecutionTimeInSeconds = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProductId = params.get("ProductId")
        self.DeviceNameFilter = params.get("DeviceNameFilter")
        self.ScheduleTimeInSeconds = params.get("ScheduleTimeInSeconds")
        if params.get("Tasks") is not None:
            self.Tasks = Task()
            self.Tasks._deserialize(params.get("Tasks"))
        self.MaxExecutionTimeInSeconds = params.get("MaxExecutionTimeInSeconds")


class CreateTaskResponse(AbstractModel):
    """CreateTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 创建的任务ID
        :type TaskId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属的产品 ID
        :type ProductId: str
        :param DeviceName: 需要删除的设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要删除的产品 ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceShadowRequest(AbstractModel):
    """DescribeDeviceShadow请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID
        :type ProductId: str
        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceShadowResponse(AbstractModel):
    """DescribeDeviceShadow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备影子数据
        :type Data: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页的大小，数值范围 10-250
        :type Limit: int
        :param FirmwareVersion: 设备固件版本号，若不带此参数会返回所有固件版本的设备
        :type FirmwareVersion: str
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FirmwareVersion = params.get("FirmwareVersion")


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 设备总数
        :type TotalCount: int
        :param Devices: 设备详细信息列表
        :type Devices: list of DeviceInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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


class DescribeMultiDevTaskRequest(AbstractModel):
    """DescribeMultiDevTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID，由批量创建设备接口返回
        :type TaskId: str
        :param ProductId: 产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        """
        self.TaskId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProductId = params.get("ProductId")


class DescribeMultiDevTaskResponse(AbstractModel):
    """DescribeMultiDevTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID
        :type TaskId: str
        :param TaskStatus: 任务是否完成。0 代表任务未开始，1 代表任务正在执行，2 代表任务已完成
        :type TaskStatus: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.RequestId = params.get("RequestId")


class DescribeMultiDevicesRequest(AbstractModel):
    """DescribeMultiDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param TaskId: 任务 ID，由批量创建设备接口返回
        :type TaskId: str
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 分页大小，每页返回的设备个数
        :type Limit: int
        """
        self.ProductId = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMultiDevicesResponse(AbstractModel):
    """DescribeMultiDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID，由批量创建设备接口返回
        :type TaskId: str
        :param DevicesInfo: 设备详细信息列表
        :type DevicesInfo: list of MultiDevicesInfo
        :param TotalDevNum: 该任务创建设备的总数
        :type TotalDevNum: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.DevicesInfo = None
        self.TotalDevNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("DevicesInfo") is not None:
            self.DevicesInfo = []
            for item in params.get("DevicesInfo"):
                obj = MultiDevicesInfo()
                obj._deserialize(item)
                self.DevicesInfo.append(obj)
        self.TotalDevNum = params.get("TotalDevNum")
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移，Offset从0开始
        :type Offset: int
        :param Limit: 分页大小，当前页面中显示的最大数量，值范围 10-250。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 产品总数
        :type TotalCount: int
        :param Products: 产品详细信息列表
        :type Products: list of ProductInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductInfo()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 任务ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        """
        :param Type: 任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”
        :type Type: str
        :param Id: 任务 ID
        :type Id: str
        :param ProductId: 产品 ID
        :type ProductId: str
        :param Status: 状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消
        :type Status: int
        :param CreateTime: 任务创建时间，Unix 时间戳
        :type CreateTime: int
        :param UpdateTime: 最后任务更新时间，Unix 时间戳
        :type UpdateTime: int
        :param DoneTime: 任务完成时间，Unix 时间戳
        :type DoneTime: int
        :param ScheduleTime: 被调度时间，Unix 时间戳
        :type ScheduleTime: int
        :param RetCode: 返回的错误码
        :type RetCode: int
        :param ErrMsg: 返回的错误信息
        :type ErrMsg: str
        :param Percent: 完成任务的设备比例
        :type Percent: int
        :param AllDeviceCnt: 匹配到的需执行任务的设备数目
        :type AllDeviceCnt: int
        :param DoneDeviceCnt: 已完成任务的设备数目
        :type DoneDeviceCnt: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Type = None
        self.Id = None
        self.ProductId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DoneTime = None
        self.ScheduleTime = None
        self.RetCode = None
        self.ErrMsg = None
        self.Percent = None
        self.AllDeviceCnt = None
        self.DoneDeviceCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.DoneTime = params.get("DoneTime")
        self.ScheduleTime = params.get("ScheduleTime")
        self.RetCode = params.get("RetCode")
        self.ErrMsg = params.get("ErrMsg")
        self.Percent = params.get("Percent")
        self.AllDeviceCnt = params.get("AllDeviceCnt")
        self.DoneDeviceCnt = params.get("DoneDeviceCnt")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移，从0开始
        :type Offset: int
        :param Limit: 分页的大小，数值范围 1-250
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 用户一个月内创建的任务总数
        :type TotalCount: int
        :param Tasks: 此页任务对象的数组，按创建时间排序
        :type Tasks: list of TaskInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线
        :type Online: int
        :param LoginTime: 设备登陆时间
        :type LoginTime: int
        :param Version: 设备版本
        :type Version: str
        :param DeviceCert: 设备证书，证书加密的设备返回
        :type DeviceCert: str
        :param DevicePsk: 设备密钥，密钥加密的设备返回
        :type DevicePsk: str
        :param Tags: 设备属性
        :type Tags: list of DeviceTag
        :param DeviceType: 设备类型
        :type DeviceType: int
        :param Imei: IMEI
        :type Imei: str
        :param Isp: 运营商类型
        :type Isp: int
        :param NbiotDeviceID: NB IOT运营商处的DeviceID
        :type NbiotDeviceID: str
        :param ConnIP: IP地址
        :type ConnIP: int
        :param LastUpdateTime: 设备最后更新时间
        :type LastUpdateTime: int
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.NbiotDeviceID = None
        self.ConnIP = None
        self.LastUpdateTime = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.Imei = params.get("Imei")
        self.Isp = params.get("Isp")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.ConnIP = params.get("ConnIP")
        self.LastUpdateTime = params.get("LastUpdateTime")


class DeviceTag(AbstractModel):
    """设备属性

    """

    def __init__(self):
        """
        :param Tag: 属性名称
        :type Tag: str
        :param Type: 属性值的类型，1 int，2 string
        :type Type: int
        :param Value: 属性的值
        :type Value: str
        """
        self.Tag = None
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Type = params.get("Type")
        self.Value = params.get("Value")


class GetDeviceShadowRequest(AbstractModel):
    """GetDeviceShadow请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品 ID
        :type ProductID: str
        :param DeviceName: 设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}
        :type DeviceName: str
        """
        self.ProductID = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")


class GetDeviceShadowResponse(AbstractModel):
    """GetDeviceShadow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备影子数据
        :type Data: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class MultiDevicesInfo(AbstractModel):
    """创建设备时返回的设备信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param DevicePsk: 对称加密密钥，base64 编码，采用对称加密时返回该参数
        :type DevicePsk: str
        :param DeviceCert: 设备证书，采用非对称加密时返回该参数
        :type DeviceCert: str
        :param DevicePrivateKey: 设备私钥，采用非对称加密时返回该参数，腾讯云为用户缓存起来，其生命周期与任务生命周期一致
        :type DevicePrivateKey: str
        :param Result: 错误码
        :type Result: int
        :param ErrMsg: 错误信息
        :type ErrMsg: str
        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.Result = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")


class ProductInfo(AbstractModel):
    """产品详细信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名
        :type ProductName: str
        :param ProductMetadata: 产品元数据
        :type ProductMetadata: :class:`tencentcloud.iotcloud.v20180614.models.ProductMetadata`
        :param ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductMetadata = None
        self.ProductProperties = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self.ProductMetadata = ProductMetadata()
            self.ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))


class ProductMetadata(AbstractModel):
    """产品元数据

    """

    def __init__(self):
        """
        :param CreationDate: 产品创建时间
        :type CreationDate: int
        """
        self.CreationDate = None


    def _deserialize(self, params):
        self.CreationDate = params.get("CreationDate")


class ProductProperties(AbstractModel):
    """产品属性

    """

    def __init__(self):
        """
        :param ProductDescription: 产品描述
        :type ProductDescription: str
        :param EncryptionType: 加密类型，1表示非对称加密，2表示对称加密。如不填写，默认值是1
        :type EncryptionType: str
        :param Region: 产品所属区域，目前只支持广州（gz）
        :type Region: str
        :param ProductType: 产品类型，0表示正常设备，2表示NB-IoT设备，默认值是0
        :type ProductType: int
        :param Format: 数据格式，取值为json或者custom，默认值是json
        :type Format: str
        """
        self.ProductDescription = None
        self.EncryptionType = None
        self.Region = None
        self.ProductType = None
        self.Format = None


    def _deserialize(self, params):
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.Format = params.get("Format")


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        """
        :param Topic: 消息发往的主题。命名规则：${ProductId}/${DeviceName}/[a-zA-Z0-9:_-]{1,128}
        :type Topic: str
        :param Payload: 消息内容
        :type Payload: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Qos: 服务质量等级，取值为0， 1
        :type Qos: int
        """
        self.Topic = None
        self.Payload = None
        self.ProductId = None
        self.DeviceName = None
        self.Qos = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Qos = params.get("Qos")


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Task(AbstractModel):
    """任务描述细节

    """

    def __init__(self):
        """
        :param UpdateShadowTask: 批量更新影子任务的描述细节，当 taskType 取值为 “UpdateShadow” 时，此字段必填。描述见下 BatchUpdateShadow
        :type UpdateShadowTask: :class:`tencentcloud.iotcloud.v20180614.models.BatchUpdateShadow`
        :param PublishMessageTask: 批量下发消息任务的描述细节，当 taskType 取值为 “PublishMessage” 时，此字段必填。描述见下 BatchPublishMessage
        :type PublishMessageTask: :class:`tencentcloud.iotcloud.v20180614.models.BatchPublishMessage`
        """
        self.UpdateShadowTask = None
        self.PublishMessageTask = None


    def _deserialize(self, params):
        if params.get("UpdateShadowTask") is not None:
            self.UpdateShadowTask = BatchUpdateShadow()
            self.UpdateShadowTask._deserialize(params.get("UpdateShadowTask"))
        if params.get("PublishMessageTask") is not None:
            self.PublishMessageTask = BatchPublishMessage()
            self.PublishMessageTask._deserialize(params.get("PublishMessageTask"))


class TaskInfo(AbstractModel):
    """任务列表详细信息

    """

    def __init__(self):
        """
        :param Type: 任务类型，目前取值为 “UpdateShadow” 或者 “PublishMessage”
        :type Type: str
        :param Id: 任务 ID
        :type Id: str
        :param ProductId: 产品 ID
        :type ProductId: str
        :param Status: 状态。1表示等待处理，2表示调度处理中，3表示已完成，4表示失败，5表示已取消
        :type Status: int
        :param CreateTime: 任务创建时间，Unix 时间戳
        :type CreateTime: int
        :param UpdateTime: 最后任务更新时间，Unix 时间戳
        :type UpdateTime: int
        :param RetCode: 返回的错误码
        :type RetCode: int
        :param ErrMsg: 返回的错误信息
        :type ErrMsg: str
        """
        self.Type = None
        self.Id = None
        self.ProductId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.RetCode = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.RetCode = params.get("RetCode")
        self.ErrMsg = params.get("ErrMsg")


class UpdateDeviceShadowRequest(AbstractModel):
    """UpdateDeviceShadow请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param State: 虚拟设备的状态，JSON字符串格式，由desired结构组成
        :type State: str
        :param ShadowVersion: 当前版本号，需要和后台的version保持一致，才能更新成功
        :type ShadowVersion: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.State = None
        self.ShadowVersion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.State = params.get("State")
        self.ShadowVersion = params.get("ShadowVersion")


class UpdateDeviceShadowResponse(AbstractModel):
    """UpdateDeviceShadow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备影子数据，JSON字符串格式
        :type Data: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")