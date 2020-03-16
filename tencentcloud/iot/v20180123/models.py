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


class Action(AbstractModel):
    """规则引擎转发动作

    """

    def __init__(self):
        """
        :param Topic: 转发至topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: :class:`tencentcloud.iot.v20180123.models.TopicAction`
        :param Service: 转发至第三发
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.iot.v20180123.models.ServiceAction`
        :param Ckafka: 转发至第三发Ckafka
注意：此字段可能返回 null，表示取不到有效值。
        :type Ckafka: :class:`tencentcloud.iot.v20180123.models.CkafkaAction`
        """
        self.Topic = None
        self.Service = None
        self.Ckafka = None


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self.Topic = TopicAction()
            self.Topic._deserialize(params.get("Topic"))
        if params.get("Service") is not None:
            self.Service = ServiceAction()
            self.Service._deserialize(params.get("Service"))
        if params.get("Ckafka") is not None:
            self.Ckafka = CkafkaAction()
            self.Ckafka._deserialize(params.get("Ckafka"))


class ActivateRuleRequest(AbstractModel):
    """ActivateRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class ActivateRuleResponse(AbstractModel):
    """ActivateRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddDeviceRequest(AbstractModel):
    """AddDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称，唯一标识某产品下的一个设备
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AddDeviceResponse(AbstractModel):
    """AddDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Device: 设备信息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class AddProductRequest(AbstractModel):
    """AddProduct请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 产品名称，同一区域产品名称需唯一，支持中文、英文字母、中划线和下划线，长度不超过31个字符，中文占两个字符
        :type Name: str
        :param Description: 产品描述
        :type Description: str
        :param DataTemplate: 数据模版
        :type DataTemplate: list of DataTemplate
        :param DataProtocol: 产品版本（native表示基础版，template表示高级版，默认值为template）
        :type DataProtocol: str
        :param AuthType: 设备认证方式（1：动态令牌，2：签名直连鉴权）
        :type AuthType: int
        :param CommProtocol: 通信方式（other/wifi/cellular/nb-iot）
        :type CommProtocol: str
        :param DeviceType: 产品的设备类型（device: 直连设备；sub_device：子设备；gateway：网关设备）
        :type DeviceType: str
        """
        self.Name = None
        self.Description = None
        self.DataTemplate = None
        self.DataProtocol = None
        self.AuthType = None
        self.CommProtocol = None
        self.DeviceType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)
        self.DataProtocol = params.get("DataProtocol")
        self.AuthType = params.get("AuthType")
        self.CommProtocol = params.get("CommProtocol")
        self.DeviceType = params.get("DeviceType")


class AddProductResponse(AbstractModel):
    """AddProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = Product()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class AddRuleRequest(AbstractModel):
    """AddRule请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Description: 描述
        :type Description: str
        :param Query: 查询
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param Actions: 转发动作列表
        :type Actions: list of Action
        :param DataType: 数据类型（0：文本，1：二进制）
        :type DataType: int
        """
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None
        self.DataType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Query") is not None:
            self.Query = RuleQuery()
            self.Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.DataType = params.get("DataType")


class AddRuleResponse(AbstractModel):
    """AddRule返回参数结构体

    """

    def __init__(self):
        """
        :param Rule: 规则
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = Rule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")


class AddTopicRequest(AbstractModel):
    """AddTopic请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param TopicName: Topic名称
        :type TopicName: str
        """
        self.ProductId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")


class AddTopicResponse(AbstractModel):
    """AddTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Topic: Topic信息
        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Topic = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self.Topic = Topic()
            self.Topic._deserialize(params.get("Topic"))
        self.RequestId = params.get("RequestId")


class AppAddUserRequest(AbstractModel):
    """AppAddUser请求参数结构体

    """

    def __init__(self):
        """
        :param UserName: 用户名
        :type UserName: str
        :param Password: 密码
        :type Password: str
        """
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class AppAddUserResponse(AbstractModel):
    """AppAddUser返回参数结构体

    """

    def __init__(self):
        """
        :param AppUser: 应用用户
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self.AppUser = AppUser()
            self.AppUser._deserialize(params.get("AppUser"))
        self.RequestId = params.get("RequestId")


class AppDeleteDeviceRequest(AbstractModel):
    """AppDeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AppDeleteDeviceResponse(AbstractModel):
    """AppDeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppDevice(AbstractModel):
    """绑定设备

    """

    def __init__(self):
        """
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param ProductId: 所属产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param AliasName: 别名
        :type AliasName: str
        :param Region: 地区
        :type Region: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.DeviceId = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None
        self.Region = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")
        self.Region = params.get("Region")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AppDeviceDetail(AbstractModel):
    """绑定设备详情

    """

    def __init__(self):
        """
        :param DeviceId: 设备Id
        :type DeviceId: str
        :param ProductId: 所属产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param AliasName: 别名
        :type AliasName: str
        :param Region: 地区
        :type Region: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param DeviceInfo: 设备信息（json）
        :type DeviceInfo: str
        :param DataTemplate: 数据模板
        :type DataTemplate: list of DataTemplate
        """
        self.DeviceId = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None
        self.Region = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DeviceInfo = None
        self.DataTemplate = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")
        self.Region = params.get("Region")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.DeviceInfo = params.get("DeviceInfo")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)


class AppGetDeviceDataRequest(AbstractModel):
    """AppGetDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AppGetDeviceDataResponse(AbstractModel):
    """AppGetDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceData: 设备数据。
        :type DeviceData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceData = params.get("DeviceData")
        self.RequestId = params.get("RequestId")


class AppGetDeviceRequest(AbstractModel):
    """AppGetDevice请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AppGetDeviceResponse(AbstractModel):
    """AppGetDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppDevice: 绑定设备详情
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDeviceDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppDevice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self.AppDevice = AppDeviceDetail()
            self.AppDevice._deserialize(params.get("AppDevice"))
        self.RequestId = params.get("RequestId")


class AppGetDeviceStatusesRequest(AbstractModel):
    """AppGetDeviceStatuses请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param DeviceIds: 设备Id列表（单次限制1000个设备）
        :type DeviceIds: list of str
        """
        self.AccessToken = None
        self.DeviceIds = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.DeviceIds = params.get("DeviceIds")


class AppGetDeviceStatusesResponse(AbstractModel):
    """AppGetDeviceStatuses返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceStatuses: 设备状态
        :type DeviceStatuses: list of DeviceStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceStatuses = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceStatuses") is not None:
            self.DeviceStatuses = []
            for item in params.get("DeviceStatuses"):
                obj = DeviceStatus()
                obj._deserialize(item)
                self.DeviceStatuses.append(obj)
        self.RequestId = params.get("RequestId")


class AppGetDevicesRequest(AbstractModel):
    """AppGetDevices请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        """
        self.AccessToken = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")


class AppGetDevicesResponse(AbstractModel):
    """AppGetDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Devices: 绑定设备列表
        :type Devices: list of AppDevice
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = AppDevice()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class AppGetTokenRequest(AbstractModel):
    """AppGetToken请求参数结构体

    """

    def __init__(self):
        """
        :param UserName: 用户名
        :type UserName: str
        :param Password: 密码
        :type Password: str
        :param Expire: TTL
        :type Expire: int
        """
        self.UserName = None
        self.Password = None
        self.Expire = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Expire = params.get("Expire")


class AppGetTokenResponse(AbstractModel):
    """AppGetToken返回参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.RequestId = params.get("RequestId")


class AppGetUserRequest(AbstractModel):
    """AppGetUser请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        """
        self.AccessToken = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")


class AppGetUserResponse(AbstractModel):
    """AppGetUser返回参数结构体

    """

    def __init__(self):
        """
        :param AppUser: 用户信息
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self.AppUser = AppUser()
            self.AppUser._deserialize(params.get("AppUser"))
        self.RequestId = params.get("RequestId")


class AppIssueDeviceControlRequest(AbstractModel):
    """AppIssueDeviceControl请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ControlData: 控制数据（json）
        :type ControlData: str
        :param Metadata: 是否发送metadata字段
        :type Metadata: bool
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None
        self.ControlData = None
        self.Metadata = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ControlData = params.get("ControlData")
        self.Metadata = params.get("Metadata")


class AppIssueDeviceControlResponse(AbstractModel):
    """AppIssueDeviceControl返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppResetPasswordRequest(AbstractModel):
    """AppResetPassword请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param OldPassword: 旧密码
        :type OldPassword: str
        :param NewPassword: 新密码
        :type NewPassword: str
        """
        self.AccessToken = None
        self.OldPassword = None
        self.NewPassword = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.OldPassword = params.get("OldPassword")
        self.NewPassword = params.get("NewPassword")


class AppResetPasswordResponse(AbstractModel):
    """AppResetPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppSecureAddDeviceRequest(AbstractModel):
    """AppSecureAddDevice请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param DeviceSignature: 设备签名
        :type DeviceSignature: str
        """
        self.AccessToken = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.DeviceSignature = params.get("DeviceSignature")


class AppSecureAddDeviceResponse(AbstractModel):
    """AppSecureAddDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppDevice: 绑定设备信息
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppDevice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self.AppDevice = AppDevice()
            self.AppDevice._deserialize(params.get("AppDevice"))
        self.RequestId = params.get("RequestId")


class AppUpdateDeviceRequest(AbstractModel):
    """AppUpdateDevice请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param AliasName: 设备别名
        :type AliasName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")


class AppUpdateDeviceResponse(AbstractModel):
    """AppUpdateDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppDevice: 设备信息
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppDevice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self.AppDevice = AppDevice()
            self.AppDevice._deserialize(params.get("AppDevice"))
        self.RequestId = params.get("RequestId")


class AppUpdateUserRequest(AbstractModel):
    """AppUpdateUser请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token
        :type AccessToken: str
        :param NickName: 昵称
        :type NickName: str
        """
        self.AccessToken = None
        self.NickName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.NickName = params.get("NickName")


class AppUpdateUserResponse(AbstractModel):
    """AppUpdateUser返回参数结构体

    """

    def __init__(self):
        """
        :param AppUser: 应用用户
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self.AppUser = AppUser()
            self.AppUser._deserialize(params.get("AppUser"))
        self.RequestId = params.get("RequestId")


class AppUser(AbstractModel):
    """应用用户

    """

    def __init__(self):
        """
        :param ApplicationId: 应用Id
        :type ApplicationId: str
        :param UserName: 用户名
        :type UserName: str
        :param NickName: 昵称
        :type NickName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self.ApplicationId = None
        self.UserName = None
        self.NickName = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.UserName = params.get("UserName")
        self.NickName = params.get("NickName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AssociateSubDeviceToGatewayProductRequest(AbstractModel):
    """AssociateSubDeviceToGatewayProduct请求参数结构体

    """

    def __init__(self):
        """
        :param SubDeviceProductId: 子设备产品Id
        :type SubDeviceProductId: str
        :param GatewayProductId: 网关产品Id
        :type GatewayProductId: str
        """
        self.SubDeviceProductId = None
        self.GatewayProductId = None


    def _deserialize(self, params):
        self.SubDeviceProductId = params.get("SubDeviceProductId")
        self.GatewayProductId = params.get("GatewayProductId")


class AssociateSubDeviceToGatewayProductResponse(AbstractModel):
    """AssociateSubDeviceToGatewayProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BoolData(AbstractModel):
    """布尔类型数据

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 读写模式
        :type Mode: str
        :param Range: 取值列表
        :type Range: list of bool
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class CkafkaAction(AbstractModel):
    """转发至Ckafka

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param TopicName: topic名称
        :type TopicName: str
        :param Region: 地域
        :type Region: str
        """
        self.InstanceId = None
        self.TopicName = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Region = params.get("Region")


class DataHistoryEntry(AbstractModel):
    """数据历史条目

    """

    def __init__(self):
        """
        :param Id: 日志id
        :type Id: str
        :param Timestamp: 时间戳
        :type Timestamp: int
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Data: 数据
        :type Data: str
        """
        self.Id = None
        self.Timestamp = None
        self.DeviceName = None
        self.Data = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Timestamp = params.get("Timestamp")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")


class DataTemplate(AbstractModel):
    """数据模版

    """

    def __init__(self):
        """
        :param Number: 数字类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Number: :class:`tencentcloud.iot.v20180123.models.NumberData`
        :param String: 字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :type String: :class:`tencentcloud.iot.v20180123.models.StringData`
        :param Enum: 枚举类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Enum: :class:`tencentcloud.iot.v20180123.models.EnumData`
        :param Bool: 布尔类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Bool: :class:`tencentcloud.iot.v20180123.models.BoolData`
        """
        self.Number = None
        self.String = None
        self.Enum = None
        self.Bool = None


    def _deserialize(self, params):
        if params.get("Number") is not None:
            self.Number = NumberData()
            self.Number._deserialize(params.get("Number"))
        if params.get("String") is not None:
            self.String = StringData()
            self.String._deserialize(params.get("String"))
        if params.get("Enum") is not None:
            self.Enum = EnumData()
            self.Enum._deserialize(params.get("Enum"))
        if params.get("Bool") is not None:
            self.Bool = BoolData()
            self.Bool._deserialize(params.get("Bool"))


class DeactivateRuleRequest(AbstractModel):
    """DeactivateRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class DeactivateRuleResponse(AbstractModel):
    """DeactivateRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DebugLogEntry(AbstractModel):
    """设备日志条目

    """

    def __init__(self):
        """
        :param Id: 日志id
        :type Id: str
        :param Event: 行为（事件）
        :type Event: str
        :param LogType: shadow/action/mqtt, 分别表示：影子/规则引擎/上下线日志
        :type LogType: str
        :param Timestamp: 时间戳
        :type Timestamp: int
        :param Result: success/fail
        :type Result: str
        :param Data: 日志详细内容
        :type Data: str
        :param Topic: 数据来源topic
        :type Topic: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.Id = None
        self.Event = None
        self.LogType = None
        self.Timestamp = None
        self.Result = None
        self.Data = None
        self.Topic = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Event = params.get("Event")
        self.LogType = params.get("LogType")
        self.Timestamp = params.get("Timestamp")
        self.Result = params.get("Result")
        self.Data = params.get("Data")
        self.Topic = params.get("Topic")
        self.DeviceName = params.get("DeviceName")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
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
        :param ProductId: 产品Id
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: TopicId
        :type TopicId: str
        :param ProductId: 产品Id
        :type ProductId: str
        """
        self.TopicId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ProductId = params.get("ProductId")


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Device(AbstractModel):
    """设备

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceSecret: 设备密钥
        :type DeviceSecret: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param DeviceInfo: 设备信息（json）
        :type DeviceInfo: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceSecret = None
        self.UpdateTime = None
        self.CreateTime = None
        self.DeviceInfo = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceSecret = params.get("DeviceSecret")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.DeviceInfo = params.get("DeviceInfo")


class DeviceEntry(AbstractModel):
    """设备条目

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceSecret: 设备密钥
        :type DeviceSecret: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceSecret = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceSecret = params.get("DeviceSecret")
        self.CreateTime = params.get("CreateTime")


class DeviceLogEntry(AbstractModel):
    """设备日志条目

    """

    def __init__(self):
        """
        :param Id: 日志id
        :type Id: str
        :param Msg: 日志内容
        :type Msg: str
        :param Code: 状态码
        :type Code: str
        :param Timestamp: 时间戳
        :type Timestamp: int
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Method: 设备动作
        :type Method: str
        """
        self.Id = None
        self.Msg = None
        self.Code = None
        self.Timestamp = None
        self.DeviceName = None
        self.Method = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Msg = params.get("Msg")
        self.Code = params.get("Code")
        self.Timestamp = params.get("Timestamp")
        self.DeviceName = params.get("DeviceName")
        self.Method = params.get("Method")


class DeviceSignature(AbstractModel):
    """设备签名

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceSignature: 设备签名
        :type DeviceSignature: str
        """
        self.DeviceName = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DeviceSignature = params.get("DeviceSignature")


class DeviceStatData(AbstractModel):
    """设备统计数据

    """

    def __init__(self):
        """
        :param Datetime: 时间点
        :type Datetime: str
        :param DeviceOnline: 在线设备数
        :type DeviceOnline: int
        :param DeviceActive: 激活设备数
        :type DeviceActive: int
        :param DeviceTotal: 设备总数
        :type DeviceTotal: int
        """
        self.Datetime = None
        self.DeviceOnline = None
        self.DeviceActive = None
        self.DeviceTotal = None


    def _deserialize(self, params):
        self.Datetime = params.get("Datetime")
        self.DeviceOnline = params.get("DeviceOnline")
        self.DeviceActive = params.get("DeviceActive")
        self.DeviceTotal = params.get("DeviceTotal")


class DeviceStatus(AbstractModel):
    """设备状态

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Status: 设备状态（inactive, online, offline）
        :type Status: str
        :param FirstOnline: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnline: str
        :param LastOnline: 最后上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnline: str
        :param OnlineTimes: 上线次数
        :type OnlineTimes: int
        """
        self.DeviceName = None
        self.Status = None
        self.FirstOnline = None
        self.LastOnline = None
        self.OnlineTimes = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")
        self.FirstOnline = params.get("FirstOnline")
        self.LastOnline = params.get("LastOnline")
        self.OnlineTimes = params.get("OnlineTimes")


class EnumData(AbstractModel):
    """枚举类型数据

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 读写模式
        :type Mode: str
        :param Range: 取值列表
        :type Range: list of str
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class GetDataHistoryRequest(AbstractModel):
    """GetDataHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceNames: 设备名称列表，允许最多一次100台
        :type DeviceNames: list of str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Size: 查询数据量
        :type Size: int
        :param Order: 时间排序（desc/asc）
        :type Order: str
        :param ScrollId: 查询游标
        :type ScrollId: str
        """
        self.ProductId = None
        self.DeviceNames = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Order = None
        self.ScrollId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Order = params.get("Order")
        self.ScrollId = params.get("ScrollId")


class GetDataHistoryResponse(AbstractModel):
    """GetDataHistory返回参数结构体

    """

    def __init__(self):
        """
        :param DataHistory: 数据历史
        :type DataHistory: list of DataHistoryEntry
        :param ScrollId: 查询游标
        :type ScrollId: str
        :param ScrollTimeout: 查询游标超时
        :type ScrollTimeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataHistory = None
        self.ScrollId = None
        self.ScrollTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataHistory") is not None:
            self.DataHistory = []
            for item in params.get("DataHistory"):
                obj = DataHistoryEntry()
                obj._deserialize(item)
                self.DataHistory.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.ScrollTimeout = params.get("ScrollTimeout")
        self.RequestId = params.get("RequestId")


class GetDebugLogRequest(AbstractModel):
    """GetDebugLog请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceNames: 设备名称列表，最大支持100台
        :type DeviceNames: list of str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Size: 查询数据量
        :type Size: int
        :param Order: 时间排序（desc/asc）
        :type Order: str
        :param ScrollId: 查询游标
        :type ScrollId: str
        :param Type: 日志类型（shadow/action/mqtt）
        :type Type: str
        """
        self.ProductId = None
        self.DeviceNames = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Order = None
        self.ScrollId = None
        self.Type = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Order = params.get("Order")
        self.ScrollId = params.get("ScrollId")
        self.Type = params.get("Type")


class GetDebugLogResponse(AbstractModel):
    """GetDebugLog返回参数结构体

    """

    def __init__(self):
        """
        :param DebugLog: 调试日志
        :type DebugLog: list of DebugLogEntry
        :param ScrollId: 查询游标
        :type ScrollId: str
        :param ScrollTimeout: 游标超时
        :type ScrollTimeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DebugLog = None
        self.ScrollId = None
        self.ScrollTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DebugLog") is not None:
            self.DebugLog = []
            for item in params.get("DebugLog"):
                obj = DebugLogEntry()
                obj._deserialize(item)
                self.DebugLog.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.ScrollTimeout = params.get("ScrollTimeout")
        self.RequestId = params.get("RequestId")


class GetDeviceDataRequest(AbstractModel):
    """GetDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class GetDeviceDataResponse(AbstractModel):
    """GetDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceData: 设备数据
        :type DeviceData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceData = params.get("DeviceData")
        self.RequestId = params.get("RequestId")


class GetDeviceLogRequest(AbstractModel):
    """GetDeviceLog请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceNames: 设备名称列表，最大支持100台
        :type DeviceNames: list of str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        :param Size: 查询数据量
        :type Size: int
        :param Order: 时间排序（desc/asc）
        :type Order: str
        :param ScrollId: 查询游标
        :type ScrollId: str
        :param Type: 日志类型（comm/status）
        :type Type: str
        """
        self.ProductId = None
        self.DeviceNames = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Order = None
        self.ScrollId = None
        self.Type = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Order = params.get("Order")
        self.ScrollId = params.get("ScrollId")
        self.Type = params.get("Type")


class GetDeviceLogResponse(AbstractModel):
    """GetDeviceLog返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceLog: 设备日志
        :type DeviceLog: list of DeviceLogEntry
        :param ScrollId: 查询游标
        :type ScrollId: str
        :param ScrollTimeout: 游标超时
        :type ScrollTimeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceLog = None
        self.ScrollId = None
        self.ScrollTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceLog") is not None:
            self.DeviceLog = []
            for item in params.get("DeviceLog"):
                obj = DeviceLogEntry()
                obj._deserialize(item)
                self.DeviceLog.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.ScrollTimeout = params.get("ScrollTimeout")
        self.RequestId = params.get("RequestId")


class GetDeviceRequest(AbstractModel):
    """GetDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class GetDeviceResponse(AbstractModel):
    """GetDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Device: 设备信息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class GetDeviceSignaturesRequest(AbstractModel):
    """GetDeviceSignatures请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceNames: 设备名称列表（单次限制1000个设备）
        :type DeviceNames: list of str
        :param Expire: 过期时间
        :type Expire: int
        """
        self.ProductId = None
        self.DeviceNames = None
        self.Expire = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Expire = params.get("Expire")


class GetDeviceSignaturesResponse(AbstractModel):
    """GetDeviceSignatures返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceSignatures: 设备绑定签名列表
        :type DeviceSignatures: list of DeviceSignature
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceSignatures = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceSignatures") is not None:
            self.DeviceSignatures = []
            for item in params.get("DeviceSignatures"):
                obj = DeviceSignature()
                obj._deserialize(item)
                self.DeviceSignatures.append(obj)
        self.RequestId = params.get("RequestId")


class GetDeviceStatisticsRequest(AbstractModel):
    """GetDeviceStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Products: 产品Id列表
        :type Products: list of str
        :param StartDate: 开始日期
        :type StartDate: str
        :param EndDate: 结束日期
        :type EndDate: str
        """
        self.Products = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.Products = params.get("Products")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class GetDeviceStatisticsResponse(AbstractModel):
    """GetDeviceStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceStatistics: 统计数据
        :type DeviceStatistics: list of DeviceStatData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceStatistics") is not None:
            self.DeviceStatistics = []
            for item in params.get("DeviceStatistics"):
                obj = DeviceStatData()
                obj._deserialize(item)
                self.DeviceStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class GetDeviceStatusesRequest(AbstractModel):
    """GetDeviceStatuses请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceNames: 设备名称列表（单次限制1000个设备）
        :type DeviceNames: list of str
        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")


class GetDeviceStatusesResponse(AbstractModel):
    """GetDeviceStatuses返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceStatuses: 设备状态列表
        :type DeviceStatuses: list of DeviceStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceStatuses = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceStatuses") is not None:
            self.DeviceStatuses = []
            for item in params.get("DeviceStatuses"):
                obj = DeviceStatus()
                obj._deserialize(item)
                self.DeviceStatuses.append(obj)
        self.RequestId = params.get("RequestId")


class GetDevicesRequest(AbstractModel):
    """GetDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param Offset: 偏移
        :type Offset: int
        :param Length: 长度
        :type Length: int
        :param Keyword: 关键字查询
        :type Keyword: str
        """
        self.ProductId = None
        self.Offset = None
        self.Length = None
        self.Keyword = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        self.Keyword = params.get("Keyword")


class GetDevicesResponse(AbstractModel):
    """GetDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Devices: 设备列表
        :type Devices: list of DeviceEntry
        :param Total: 设备总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceEntry()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetProductRequest(AbstractModel):
    """GetProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class GetProductResponse(AbstractModel):
    """GetProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = Product()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class GetProductsRequest(AbstractModel):
    """GetProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移
        :type Offset: int
        :param Length: 长度
        :type Length: int
        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class GetProductsResponse(AbstractModel):
    """GetProducts返回参数结构体

    """

    def __init__(self):
        """
        :param Products: Product列表
        :type Products: list of ProductEntry
        :param Total: Product总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetRuleRequest(AbstractModel):
    """GetRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class GetRuleResponse(AbstractModel):
    """GetRule返回参数结构体

    """

    def __init__(self):
        """
        :param Rule: 规则
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = Rule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")


class GetRulesRequest(AbstractModel):
    """GetRules请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移
        :type Offset: int
        :param Length: 长度
        :type Length: int
        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class GetRulesResponse(AbstractModel):
    """GetRules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 规则列表
        :type Rules: list of Rule
        :param Total: 规则总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetTopicRequest(AbstractModel):
    """GetTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: TopicId
        :type TopicId: str
        :param ProductId: 产品Id
        :type ProductId: str
        """
        self.TopicId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ProductId = params.get("ProductId")


class GetTopicResponse(AbstractModel):
    """GetTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Topic: Topic信息
        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Topic = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self.Topic = Topic()
            self.Topic._deserialize(params.get("Topic"))
        self.RequestId = params.get("RequestId")


class GetTopicsRequest(AbstractModel):
    """GetTopics请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param Offset: 偏移
        :type Offset: int
        :param Length: 长度
        :type Length: int
        """
        self.ProductId = None
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class GetTopicsResponse(AbstractModel):
    """GetTopics返回参数结构体

    """

    def __init__(self):
        """
        :param Topics: Topic列表
        :type Topics: list of Topic
        :param Total: Topic总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Topics = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = Topic()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class IssueDeviceControlRequest(AbstractModel):
    """IssueDeviceControl请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ControlData: 控制数据（json）
        :type ControlData: str
        :param Metadata: 是否发送metadata字段
        :type Metadata: bool
        """
        self.ProductId = None
        self.DeviceName = None
        self.ControlData = None
        self.Metadata = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ControlData = params.get("ControlData")
        self.Metadata = params.get("Metadata")


class IssueDeviceControlResponse(AbstractModel):
    """IssueDeviceControl返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NumberData(AbstractModel):
    """数字类型数据

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 读写模式
        :type Mode: str
        :param Range: 取值范围
        :type Range: list of float
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class Product(AbstractModel):
    """产品

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param ProductKey: 产品Key
        :type ProductKey: str
        :param AppId: AppId
        :type AppId: int
        :param Name: 产品名称
        :type Name: str
        :param Description: 产品描述
        :type Description: str
        :param Domain: 连接域名
        :type Domain: str
        :param Standard: 产品规格
        :type Standard: int
        :param AuthType: 鉴权类型（0：直连，1：Token）
        :type AuthType: int
        :param Deleted: 删除（0未删除）
        :type Deleted: int
        :param Message: 备注
        :type Message: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param DataTemplate: 数据模版
        :type DataTemplate: list of DataTemplate
        :param DataProtocol: 数据协议（native/template）
        :type DataProtocol: str
        :param Username: 直连用户名
        :type Username: str
        :param Password: 直连密码
        :type Password: str
        :param CommProtocol: 通信方式
        :type CommProtocol: str
        :param Qps: qps
        :type Qps: int
        :param Region: 地域
        :type Region: str
        :param DeviceType: 产品的设备类型
        :type DeviceType: str
        :param AssociatedProducts: 关联的产品列表
        :type AssociatedProducts: list of str
        """
        self.ProductId = None
        self.ProductKey = None
        self.AppId = None
        self.Name = None
        self.Description = None
        self.Domain = None
        self.Standard = None
        self.AuthType = None
        self.Deleted = None
        self.Message = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DataTemplate = None
        self.DataProtocol = None
        self.Username = None
        self.Password = None
        self.CommProtocol = None
        self.Qps = None
        self.Region = None
        self.DeviceType = None
        self.AssociatedProducts = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductKey = params.get("ProductKey")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Domain = params.get("Domain")
        self.Standard = params.get("Standard")
        self.AuthType = params.get("AuthType")
        self.Deleted = params.get("Deleted")
        self.Message = params.get("Message")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)
        self.DataProtocol = params.get("DataProtocol")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.CommProtocol = params.get("CommProtocol")
        self.Qps = params.get("Qps")
        self.Region = params.get("Region")
        self.DeviceType = params.get("DeviceType")
        self.AssociatedProducts = params.get("AssociatedProducts")


class ProductEntry(AbstractModel):
    """产品条目

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param ProductKey: 产品Key
        :type ProductKey: str
        :param AppId: AppId
        :type AppId: int
        :param Name: 产品名称
        :type Name: str
        :param Description: 产品描述
        :type Description: str
        :param Domain: 连接域名
        :type Domain: str
        :param AuthType: 鉴权类型（0：直连，1：Token）
        :type AuthType: int
        :param DataProtocol: 数据协议（native/template）
        :type DataProtocol: str
        :param Deleted: 删除（0未删除）
        :type Deleted: int
        :param Message: 备注
        :type Message: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param CommProtocol: 通信方式
        :type CommProtocol: str
        :param Region: 地域
        :type Region: str
        :param DeviceType: 设备类型
        :type DeviceType: str
        """
        self.ProductId = None
        self.ProductKey = None
        self.AppId = None
        self.Name = None
        self.Description = None
        self.Domain = None
        self.AuthType = None
        self.DataProtocol = None
        self.Deleted = None
        self.Message = None
        self.CreateTime = None
        self.CommProtocol = None
        self.Region = None
        self.DeviceType = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductKey = params.get("ProductKey")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Domain = params.get("Domain")
        self.AuthType = params.get("AuthType")
        self.DataProtocol = params.get("DataProtocol")
        self.Deleted = params.get("Deleted")
        self.Message = params.get("Message")
        self.CreateTime = params.get("CreateTime")
        self.CommProtocol = params.get("CommProtocol")
        self.Region = params.get("Region")
        self.DeviceType = params.get("DeviceType")


class PublishMsgRequest(AbstractModel):
    """PublishMsg请求参数结构体

    """

    def __init__(self):
        """
        :param Topic: Topic
        :type Topic: str
        :param Message: 消息内容
        :type Message: str
        :param Qos: Qos(目前QoS支持0与1)
        :type Qos: int
        """
        self.Topic = None
        self.Message = None
        self.Qos = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Message = params.get("Message")
        self.Qos = params.get("Qos")


class PublishMsgResponse(AbstractModel):
    """PublishMsg返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceRequest(AbstractModel):
    """ResetDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class ResetDeviceResponse(AbstractModel):
    """ResetDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Device: 设备信息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class Rule(AbstractModel):
    """规则

    """

    def __init__(self):
        """
        :param RuleId: 规则Id
        :type RuleId: str
        :param AppId: AppId
        :type AppId: int
        :param Name: 名称
        :type Name: str
        :param Description: 描述
        :type Description: str
        :param Query: 查询
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param Actions: 转发
        :type Actions: list of Action
        :param Active: 已启动
        :type Active: int
        :param Deleted: 已删除
        :type Deleted: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param MsgOrder: 消息顺序
        :type MsgOrder: int
        :param DataType: 数据类型（0：文本，1：二进制）
        :type DataType: int
        """
        self.RuleId = None
        self.AppId = None
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None
        self.Active = None
        self.Deleted = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MsgOrder = None
        self.DataType = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Query") is not None:
            self.Query = RuleQuery()
            self.Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.Active = params.get("Active")
        self.Deleted = params.get("Deleted")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MsgOrder = params.get("MsgOrder")
        self.DataType = params.get("DataType")


class RuleQuery(AbstractModel):
    """查询

    """

    def __init__(self):
        """
        :param Field: 字段
        :type Field: str
        :param Condition: 过滤规则
        :type Condition: str
        :param Topic: Topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: str
        :param ProductId: 产品Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        """
        self.Field = None
        self.Condition = None
        self.Topic = None
        self.ProductId = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Condition = params.get("Condition")
        self.Topic = params.get("Topic")
        self.ProductId = params.get("ProductId")


class ServiceAction(AbstractModel):
    """转发到第三方http(s)服务

    """

    def __init__(self):
        """
        :param Url: 服务url地址
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")


class StringData(AbstractModel):
    """数字类型数据

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 读写模式
        :type Mode: str
        :param Range: 长度范围
        :type Range: list of int non-negative
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class Topic(AbstractModel):
    """Topic

    """

    def __init__(self):
        """
        :param TopicId: TopicId
        :type TopicId: str
        :param TopicName: Topic名称
        :type TopicName: str
        :param ProductId: 产品Id
        :type ProductId: str
        :param MsgLife: 消息最大生命周期
        :type MsgLife: int
        :param MsgSize: 消息最大大小
        :type MsgSize: int
        :param MsgCount: 消息最大数量
        :type MsgCount: int
        :param Deleted: 已删除
        :type Deleted: int
        :param Path: Topic完整路径
        :type Path: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.TopicId = None
        self.TopicName = None
        self.ProductId = None
        self.MsgLife = None
        self.MsgSize = None
        self.MsgCount = None
        self.Deleted = None
        self.Path = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.ProductId = params.get("ProductId")
        self.MsgLife = params.get("MsgLife")
        self.MsgSize = params.get("MsgSize")
        self.MsgCount = params.get("MsgCount")
        self.Deleted = params.get("Deleted")
        self.Path = params.get("Path")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class TopicAction(AbstractModel):
    """转发到topic动作

    """

    def __init__(self):
        """
        :param Topic: 目标topic
        :type Topic: str
        """
        self.Topic = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")


class UnassociateSubDeviceFromGatewayProductRequest(AbstractModel):
    """UnassociateSubDeviceFromGatewayProduct请求参数结构体

    """

    def __init__(self):
        """
        :param SubDeviceProductId: 子设备产品Id
        :type SubDeviceProductId: str
        :param GatewayProductId: 网关设备产品Id
        :type GatewayProductId: str
        """
        self.SubDeviceProductId = None
        self.GatewayProductId = None


    def _deserialize(self, params):
        self.SubDeviceProductId = params.get("SubDeviceProductId")
        self.GatewayProductId = params.get("GatewayProductId")


class UnassociateSubDeviceFromGatewayProductResponse(AbstractModel):
    """UnassociateSubDeviceFromGatewayProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateProductRequest(AbstractModel):
    """UpdateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param Name: 产品名称
        :type Name: str
        :param Description: 产品描述
        :type Description: str
        :param DataTemplate: 数据模版
        :type DataTemplate: list of DataTemplate
        """
        self.ProductId = None
        self.Name = None
        self.Description = None
        self.DataTemplate = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)


class UpdateProductResponse(AbstractModel):
    """UpdateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 更新后的产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = Product()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class UpdateRuleRequest(AbstractModel):
    """UpdateRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id
        :type RuleId: str
        :param Name: 名称
        :type Name: str
        :param Description: 描述
        :type Description: str
        :param Query: 查询
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param Actions: 转发动作列表
        :type Actions: list of Action
        :param DataType: 数据类型（0：文本，1：二进制）
        :type DataType: int
        """
        self.RuleId = None
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None
        self.DataType = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Query") is not None:
            self.Query = RuleQuery()
            self.Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.DataType = params.get("DataType")


class UpdateRuleResponse(AbstractModel):
    """UpdateRule返回参数结构体

    """

    def __init__(self):
        """
        :param Rule: 规则
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = Rule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")