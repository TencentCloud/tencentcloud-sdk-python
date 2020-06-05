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


class BindDevicesRequest(AbstractModel):
    """BindDevices请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param ProductId: 被绑定设备的产品ID
        :type ProductId: str
        :param DeviceNames: 被绑定的多个设备名
        :type DeviceNames: list of str
        :param Skey: 中兴CLAA设备的绑定需要skey，普通的设备不需要
        :type Skey: str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None
        self.Skey = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Skey = params.get("Skey")


class BindDevicesResponse(AbstractModel):
    """BindDevices返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BrokerSubscribe(AbstractModel):
    """代理订阅信息

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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param LoraDevEui: LoRa设备的DevEui，当创建LoRa时，此字段必填
        :type LoraDevEui: str
        :param LoraMoteType: LoRa设备的MoteType
        :type LoraMoteType: int
        :param Skey: 创建LoRa设备需要skey
        :type Skey: str
        :param LoraAppKey: LoRa设备的AppKey
        :type LoraAppKey: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Attribute = None
        self.DefinedPsk = None
        self.Isp = None
        self.Imei = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.Skey = None
        self.LoraAppKey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        if params.get("Attribute") is not None:
            self.Attribute = Attribute()
            self.Attribute._deserialize(params.get("Attribute"))
        self.DefinedPsk = params.get("DefinedPsk")
        self.Isp = params.get("Isp")
        self.Imei = params.get("Imei")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.Skey = params.get("Skey")
        self.LoraAppKey = params.get("LoraAppKey")


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
        :param LoraDevEui: LoRa设备的DevEui，当设备是LoRa设备时，会返回该字段
        :type LoraDevEui: str
        :param LoraMoteType: LoRa设备的MoteType，当设备是LoRa设备时，会返回该字段
        :type LoraMoteType: int
        :param LoraAppKey: LoRa设备的AppKey，当设备是LoRa设备时，会返回该字段
        :type LoraAppKey: str
        :param LoraNwkKey: LoRa设备的NwkKey，当设备是LoRa设备时，会返回该字段
        :type LoraNwkKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LoraAppKey = None
        self.LoraNwkKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LoraAppKey = params.get("LoraAppKey")
        self.LoraNwkKey = params.get("LoraNwkKey")
        self.RequestId = params.get("RequestId")


class CreateLoraDeviceRequest(AbstractModel):
    """CreateLoraDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品 ID ，创建产品时腾讯云为用户分配全局唯一的 ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceType: 设备类型 ，目前支持A、B、C三种
        :type DeviceType: str
        :param AppEui: LoRa应用UUID
        :type AppEui: str
        :param DeviceEui: LoRa设备UUID
        :type DeviceEui: str
        :param AppKey: LoRa应用密钥
        :type AppKey: str
        :param AuthKey: LoRa设备验证密钥
        :type AuthKey: str
        :param Memo: 设备备注
        :type Memo: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceType = None
        self.AppEui = None
        self.DeviceEui = None
        self.AppKey = None
        self.AuthKey = None
        self.Memo = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceType = params.get("DeviceType")
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.AppKey = params.get("AppKey")
        self.AuthKey = params.get("AuthKey")
        self.Memo = params.get("Memo")


class CreateLoraDeviceResponse(AbstractModel):
    """CreateLoraDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppEui: LoRa应用UUID
        :type AppEui: str
        :param DeviceEui: LoRa设备UUID
        :type DeviceEui: str
        :param ClassType: 设备类型,目前支持A、B、C三种
        :type ClassType: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppEui = None
        self.DeviceEui = None
        self.ClassType = None
        self.DeviceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.ClassType = params.get("ClassType")
        self.DeviceName = params.get("DeviceName")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateMultiDevicesTaskRequest(AbstractModel):
    """CreateMultiDevicesTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ParametersType: 参数类型 cosfile-文件上传 random-随机创建
        :type ParametersType: str
        :param FileName: 文件上传类型时文件名
        :type FileName: str
        :param FileSize: 文件上传类型时文件大小
        :type FileSize: int
        :param BatchCount: 随机创建时设备创建个数
        :type BatchCount: int
        :param Hash: 文件上传类型时文件md5值
        :type Hash: str
        """
        self.ProductId = None
        self.ParametersType = None
        self.FileName = None
        self.FileSize = None
        self.BatchCount = None
        self.Hash = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ParametersType = params.get("ParametersType")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.BatchCount = params.get("BatchCount")
        self.Hash = params.get("Hash")


class CreateMultiDevicesTaskResponse(AbstractModel):
    """CreateMultiDevicesTask返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 任务ID
        :type Id: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
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
        :param Skey: 创建CLAA产品时，需要Skey
        :type Skey: str
        """
        self.ProductName = None
        self.ProductProperties = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.Skey = params.get("Skey")


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductId: 产品 ID，腾讯云生成全局唯一 ID
        :type ProductId: str
        :param ProductProperties: 产品属性
        :type ProductProperties: :class:`tencentcloud.iotcloud.v20180614.models.ProductProperties`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProductName = None
        self.ProductId = None
        self.ProductProperties = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.ProductId = params.get("ProductId")
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.RequestId = params.get("RequestId")


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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品自身ID
        :type ProductID: str
        :param TopicName: Topic名称
        :type TopicName: str
        :param Privilege: Topic权限，1发布，2订阅，3订阅和发布
        :type Privilege: int
        :param BrokerSubscribe: 代理订阅信息，网关产品为绑定的子产品创建topic时需要填写，内容为子产品的ID和设备信息。
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        self.ProductID = None
        self.TopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.TopicName = params.get("TopicName")
        self.Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self.BrokerSubscribe = BrokerSubscribe()
            self.BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))


class CreateTopicPolicyResponse(AbstractModel):
    """CreateTopicPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTopicRuleRequest(AbstractModel):
    """CreateTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称
        :type RuleName: str
        :param TopicRulePayload: 规则内容
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`
        """
        self.RuleName = None
        self.TopicRulePayload = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self.TopicRulePayload = TopicRulePayload()
            self.TopicRulePayload._deserialize(params.get("TopicRulePayload"))


class CreateTopicRuleResponse(AbstractModel):
    """CreateTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param Skey: 删除LoRa设备以及LoRa网关设备需要skey
        :type Skey: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Skey = params.get("Skey")


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


class DeleteLoraDeviceRequest(AbstractModel):
    """DeleteLoraDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DeleteLoraDeviceResponse(AbstractModel):
    """DeleteLoraDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param Skey: 删除LoRa产品需要skey
        :type Skey: str
        """
        self.ProductId = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Skey = params.get("Skey")


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


class DeleteTopicRuleRequest(AbstractModel):
    """DeleteTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class DeleteTopicRuleResponse(AbstractModel):
    """DeleteTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceClientKeyRequest(AbstractModel):
    """DescribeDeviceClientKey请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 所属产品的Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceClientKeyResponse(AbstractModel):
    """DescribeDeviceClientKey返回参数结构体

    """

    def __init__(self):
        """
        :param ClientKey: 设备的私钥
        :type ClientKey: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClientKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientKey = params.get("ClientKey")
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param DeviceName: 设备名
        :type DeviceName: str
        """
        self.ProductID = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线
        :type Online: int
        :param LoginTime: 设备登录时间
        :type LoginTime: int
        :param Version: 设备固件版本
        :type Version: str
        :param LastUpdateTime: 设备最后更新时间
        :type LastUpdateTime: int
        :param DeviceCert: 设备证书
        :type DeviceCert: str
        :param DevicePsk: 设备密钥
        :type DevicePsk: str
        :param Tags: 设备属性
        :type Tags: list of DeviceTag
        :param DeviceType: 设备类型
        :type DeviceType: int
        :param Imei: 国际移动设备识别码 IMEI
        :type Imei: str
        :param Isp: 运营商类型
        :type Isp: int
        :param ConnIP: IP地址
        :type ConnIP: int
        :param NbiotDeviceID: NB IoT运营商处的DeviceID
        :type NbiotDeviceID: str
        :param LoraDevEui: Lora设备的dev eui
        :type LoraDevEui: str
        :param LoraMoteType: Lora设备的mote type
        :type LoraMoteType: int
        :param LogLevel: 设备的sdk日志等级
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param CertState: 设备证书获取状态，0 未获取过设备密钥, 1 已获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertState: int
        :param EnableState: 设备启用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
        :param ClientIP: MQTT客户端IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIP: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.LastUpdateTime = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.ConnIP = None
        self.NbiotDeviceID = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LogLevel = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None
        self.ClientIP = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.LastUpdateTime = params.get("LastUpdateTime")
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
        self.ConnIP = params.get("ConnIP")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LogLevel = params.get("LogLevel")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.ClientIP = params.get("ClientIP")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param Offset: 偏移量，Offset从0开始
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


class DescribeLoraDeviceRequest(AbstractModel):
    """DescribeLoraDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeLoraDeviceResponse(AbstractModel):
    """DescribeLoraDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param AppEui: LoRa应用UUID
        :type AppEui: str
        :param DeviceEui: LoRa设备UUID
        :type DeviceEui: str
        :param AppKey: LoRa应用密钥
        :type AppKey: str
        :param ClassType: 设备类型,目前支持A、B、C三种
        :type ClassType: str
        :param ProductId: 设备所属产品id
        :type ProductId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.AppEui = None
        self.DeviceEui = None
        self.AppKey = None
        self.ClassType = None
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.AppKey = params.get("AppKey")
        self.ClassType = params.get("ClassType")
        self.ProductId = params.get("ProductId")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeProductTaskRequest(AbstractModel):
    """DescribeProductTask请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.ProductId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TaskId = params.get("TaskId")


class DescribeProductTaskResponse(AbstractModel):
    """DescribeProductTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskInfo: 产品任务详细信息
        :type TaskInfo: :class:`tencentcloud.iotcloud.v20180614.models.ProductTaskInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfo") is not None:
            self.TaskInfo = ProductTaskInfo()
            self.TaskInfo._deserialize(params.get("TaskInfo"))
        self.RequestId = params.get("RequestId")


class DescribeProductTasksRequest(AbstractModel):
    """DescribeProductTasks请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param Offset: 产品级别任务列表偏移量
        :type Offset: int
        :param Limit: 产品级别任务列表拉取个数
        :type Limit: int
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeProductTasksResponse(AbstractModel):
    """DescribeProductTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的任务总个数
        :type TotalCount: int
        :param TaskInfos: 任务详细信息列表
        :type TaskInfos: list of ProductTaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = ProductTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，Offset从0开始
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param Offset: 偏移量，从0开始
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param LoginTime: 设备登录时间
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
        :param LoraDevEui: LoRa设备的dev eui
        :type LoraDevEui: str
        :param LoraMoteType: LoRa设备的Mote type
        :type LoraMoteType: int
        :param FirstOnlineTime: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LastOfflineTime: 最近下线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param CreateTime: 设备创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LogLevel: 设备日志级别
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param CertState: 设备证书获取状态, 1 已获取过设备密钥，0 未获取过设备密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertState: int
        :param EnableState: 设备可用状态，0禁用，1启用
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param Labels: 设备标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
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
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.LogLevel = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None


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
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.LogLevel = params.get("LogLevel")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)


class DeviceLabel(AbstractModel):
    """设备标签

    """

    def __init__(self):
        """
        :param Key: 标签标识
        :type Key: str
        :param Value: 标签值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


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
        :param Name: 属性描述名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.Tag = None
        self.Type = None
        self.Value = None
        self.Name = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        self.Name = params.get("Name")


class DisableTopicRuleRequest(AbstractModel):
    """DisableTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class DisableTopicRuleResponse(AbstractModel):
    """DisableTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableTopicRuleRequest(AbstractModel):
    """EnableTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class EnableTopicRuleResponse(AbstractModel):
    """EnableTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param EncryptionType: 加密类型，1表示证书认证，2表示签名认证。如不填写，默认值是1
        :type EncryptionType: str
        :param Region: 产品所属区域，目前只支持广州（gz）
        :type Region: str
        :param ProductType: 产品类型，各个类型值代表的节点-类型如下：
0 普通产品，2 NB-IoT产品，4 LoRa产品，3 LoRa网关产品，5 普通网关产品   默认值是0
        :type ProductType: int
        :param Format: 数据格式，取值为json或者custom，默认值是json
        :type Format: str
        :param Platform: 产品所属平台，默认值是0
        :type Platform: str
        :param Appeui: LoRa产品运营侧APPEUI，只有LoRa产品需要填写
        :type Appeui: str
        :param ModelId: 产品绑定的物模型ID，-1表示不绑定
        :type ModelId: str
        :param ModelName: 产品绑定的物模型名称
        :type ModelName: str
        :param ProductKey: 产品密钥，suite产品才会有
        :type ProductKey: str
        :param RegisterType: 动态注册类型 0-关闭, 1-预定义设备名 2-动态定义设备名
        :type RegisterType: int
        :param ProductSecret: 动态注册产品秘钥
        :type ProductSecret: str
        :param RegisterLimit: RegisterType为2时，设备动态创建的限制数量
        :type RegisterLimit: int
        """
        self.ProductDescription = None
        self.EncryptionType = None
        self.Region = None
        self.ProductType = None
        self.Format = None
        self.Platform = None
        self.Appeui = None
        self.ModelId = None
        self.ModelName = None
        self.ProductKey = None
        self.RegisterType = None
        self.ProductSecret = None
        self.RegisterLimit = None


    def _deserialize(self, params):
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.Format = params.get("Format")
        self.Platform = params.get("Platform")
        self.Appeui = params.get("Appeui")
        self.ModelId = params.get("ModelId")
        self.ModelName = params.get("ModelName")
        self.ProductKey = params.get("ProductKey")
        self.RegisterType = params.get("RegisterType")
        self.ProductSecret = params.get("ProductSecret")
        self.RegisterLimit = params.get("RegisterLimit")


class ProductTaskInfo(AbstractModel):
    """产品级任务详细信息

    """

    def __init__(self):
        """
        :param Id: 任务ID
        :type Id: int
        :param Type: 任务类型 0-批量创建设备类型
        :type Type: int
        :param State: 任务状态 0-创建中 1-待执行 2-执行中 3-执行失败 4-子任务部分失败 5-执行成功
        :type State: int
        :param ParametersType: 任务参数类型 cosfile-文件输入 random-随机生成
        :type ParametersType: str
        :param Parameters: 任务参数
        :type Parameters: str
        :param ResultType: 任务执行结果类型 cosfile-文件输出 errmsg-错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param Result: 任务执行结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param BatchCount: 子任务总个数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchCount: int
        :param BatchOffset: 子任务已执行个数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchOffset: int
        :param CreateTime: 任务创建时间
        :type CreateTime: int
        :param UpdateTime: 任务更新时间
        :type UpdateTime: int
        :param CompleteTime: 任务完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CompleteTime: int
        """
        self.Id = None
        self.Type = None
        self.State = None
        self.ParametersType = None
        self.Parameters = None
        self.ResultType = None
        self.Result = None
        self.BatchCount = None
        self.BatchOffset = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CompleteTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.State = params.get("State")
        self.ParametersType = params.get("ParametersType")
        self.Parameters = params.get("Parameters")
        self.ResultType = params.get("ResultType")
        self.Result = params.get("Result")
        self.BatchCount = params.get("BatchCount")
        self.BatchOffset = params.get("BatchOffset")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CompleteTime = params.get("CompleteTime")


class PublishAsDeviceRequest(AbstractModel):
    """PublishAsDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Port: LoRa 设备端口
        :type Port: int
        :param Payload: 消息内容
        :type Payload: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Port = None
        self.Payload = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Port = params.get("Port")
        self.Payload = params.get("Payload")


class PublishAsDeviceResponse(AbstractModel):
    """PublishAsDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :param Qos: 服务质量等级，取值为0或1
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PublishToDeviceRequest(AbstractModel):
    """PublishToDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Port: LoRa 端口
        :type Port: int
        :param Payload: 消息内容
        :type Payload: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Port = None
        self.Payload = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Port = params.get("Port")
        self.Payload = params.get("Payload")


class PublishToDeviceResponse(AbstractModel):
    """PublishToDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceTopicRuleRequest(AbstractModel):
    """ReplaceTopicRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleName: 规则名称
        :type RuleName: str
        :param TopicRulePayload: 替换的规则包体
        :type TopicRulePayload: :class:`tencentcloud.iotcloud.v20180614.models.TopicRulePayload`
        :param ModifyType: 修改类型，0：其他，1：创建行为，2：更新行为，3：删除行为
        :type ModifyType: int
        :param ActionIndex: action增删改变更填对应topicRulePayload里面第几个action
        :type ActionIndex: int
        """
        self.RuleName = None
        self.TopicRulePayload = None
        self.ModifyType = None
        self.ActionIndex = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self.TopicRulePayload = TopicRulePayload()
            self.TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        self.ModifyType = params.get("ModifyType")
        self.ActionIndex = params.get("ActionIndex")


class ReplaceTopicRuleResponse(AbstractModel):
    """ReplaceTopicRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceResult(AbstractModel):
    """重置设备状态结果

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Success: 是否成功
        :type Success: bool
        :param Reason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self.DeviceName = None
        self.Success = None
        self.Reason = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Success = params.get("Success")
        self.Reason = params.get("Reason")


class ResetDeviceStateRequest(AbstractModel):
    """ResetDeviceState请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceNames: 设备名称
        :type DeviceNames: list of str
        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")


class ResetDeviceStateResponse(AbstractModel):
    """ResetDeviceState返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessCount: 批量重置设备成功数
        :type SuccessCount: int
        :param ResetDeviceResults: 批量重置设备结果
        :type ResetDeviceResults: list of ResetDeviceResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCount = None
        self.ResetDeviceResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCount = params.get("SuccessCount")
        if params.get("ResetDeviceResults") is not None:
            self.ResetDeviceResults = []
            for item in params.get("ResetDeviceResults"):
                obj = ResetDeviceResult()
                obj._deserialize(item)
                self.ResetDeviceResults.append(obj)
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


class TopicRulePayload(AbstractModel):
    """创建规则请求包体

    """

    def __init__(self):
        """
        :param Sql: 规则的SQL语句，如： SELECT * FROM 'pid/dname/event'，然后对其进行base64编码，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :type Sql: str
        :param Actions: 行为的JSON字符串，大部分种类举例如下：
[
    {
        "republish": {
            "topic": "TEST/test"
        }
    },
    {
        "forward": {
            "api": "http://127.0.0.1:8080"
        }
    },
    {
        "ckafka": {
            "instance": {
                "id": "ckafka-test",
                "name": ""
            },
            "topic": {
                "id": "topic-test",
                "name": "test"
            },
            "region": "gz"
        }
    },
    {
        "cmqqueue": {
            "queuename": "queue-test-TEST",
            "region": "gz"
        }
    },
    {
        "mysql": {
            "instanceid": "cdb-test",
            "region": "gz",
            "username": "test",
            "userpwd": "*****",
            "dbname": "d_mqtt",
            "tablename": "t_test",
            "fieldpairs": [
                {
                    "field": "test",
                    "value": "test"
                }
            ],
            "devicetype": "CUSTOM"
        }
    }
]
        :type Actions: str
        :param Description: 规则描述
        :type Description: str
        :param RuleDisabled: 是否禁用规则
        :type RuleDisabled: bool
        """
        self.Sql = None
        self.Actions = None
        self.Description = None
        self.RuleDisabled = None


    def _deserialize(self, params):
        self.Sql = params.get("Sql")
        self.Actions = params.get("Actions")
        self.Description = params.get("Description")
        self.RuleDisabled = params.get("RuleDisabled")


class UnbindDevicesRequest(AbstractModel):
    """UnbindDevices请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayProductId: 网关设备的产品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 网关设备的设备名
        :type GatewayDeviceName: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceNames: 多个设备名
        :type DeviceNames: list of str
        :param Skey: 中兴CLAA设备的解绑需要Skey，普通设备不需要
        :type Skey: str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None
        self.Skey = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Skey = params.get("Skey")


class UnbindDevicesResponse(AbstractModel):
    """UnbindDevices返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceAvailableStateRequest(AbstractModel):
    """UpdateDeviceAvailableState请求参数结构体

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


class UpdateDeviceAvailableStateResponse(AbstractModel):
    """UpdateDeviceAvailableState返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :param Prefix: 下发delta消息的topic前缀，可选类型: "$shadow","$template"。不填写默认"$shadow"。
        :type Prefix: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.State = None
        self.ShadowVersion = None
        self.Prefix = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.State = params.get("State")
        self.ShadowVersion = params.get("ShadowVersion")
        self.Prefix = params.get("Prefix")


class UpdateDeviceShadowResponse(AbstractModel):
    """UpdateDeviceShadow返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备影子数据，JSON字符串格式
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UpdateTopicPolicyRequest(AbstractModel):
    """UpdateTopicPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param TopicName: 更新前Topic名
        :type TopicName: str
        :param NewTopicName: 更新后Topic名
        :type NewTopicName: str
        :param Privilege: Topic权限
        :type Privilege: int
        :param BrokerSubscribe: 代理订阅信息
        :type BrokerSubscribe: :class:`tencentcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        self.ProductID = None
        self.TopicName = None
        self.NewTopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.TopicName = params.get("TopicName")
        self.NewTopicName = params.get("NewTopicName")
        self.Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self.BrokerSubscribe = BrokerSubscribe()
            self.BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))


class UpdateTopicPolicyResponse(AbstractModel):
    """UpdateTopicPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")