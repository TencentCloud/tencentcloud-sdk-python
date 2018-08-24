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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param AuthType: 鉴权模式（1：动态令牌，推荐使用动态令牌）
        :type AuthType: int
        :param DataTemplate: 数据模版（json数组）
        :type DataTemplate: list of str
        :param DataProtocol: 数据协议（native表示自定义，template表示数据模板，默认值为template）
        :type DataProtocol: str
        """
        self.Name = None
        self.Description = None
        self.AuthType = None
        self.DataTemplate = None
        self.DataProtocol = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.AuthType = params.get("AuthType")
        self.DataTemplate = params.get("DataTemplate")
        self.DataProtocol = params.get("DataProtocol")


class AddProductResponse(AbstractModel):
    """AddProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param Actions: 转发
        :type Actions: list of Object
        """
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Query") is not None:
            self.Query = RuleQuery()
            self.Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Object()
                obj._deserialize(item)
                self.Actions.append(obj)


class AddRuleResponse(AbstractModel):
    """AddRule返回参数结构体

    """

    def __init__(self):
        """
        :param Rule: 规则
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Topic = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self.Topic = Topic()
            self.Topic._deserialize(params.get("Topic"))
        self.RequestId = params.get("RequestId")


class AddUserRequest(AbstractModel):
    """AddUser请求参数结构体

    """


class AddUserResponse(AbstractModel):
    """AddUser返回参数结构体

    """

    def __init__(self):
        """
        :param User: 用户信息
        :type User: :class:`tencentcloud.iot.v20180123.models.User`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param Devices: 绑定设备列表
        :type Devices: list of Object
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self.ApplicationId = None
        self.UserName = None
        self.NickName = None
        self.Devices = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.UserName = params.get("UserName")
        self.NickName = params.get("NickName")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = Object()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param DeviceInfo: 设备信息
        :type DeviceInfo: :class:`tencentcloud.iot.v20180123.models.Object`
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
        if params.get("DeviceInfo") is not None:
            self.DeviceInfo = Object()
            self.DeviceInfo._deserialize(params.get("DeviceInfo"))


class DeviceStatus(AbstractModel):
    """设备状态

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Status: 设备状态（inactive, online, offline）
        :type Status: str
        """
        self.DeviceName = None
        self.Status = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")


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
        :type Size: list of int non-negative
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
        :type DataHistory: list of Object
        :param ScrollId: 查询游标
        :type ScrollId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DataHistory = None
        self.ScrollId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataHistory") is not None:
            self.DataHistory = []
            for item in params.get("DataHistory"):
                obj = Object()
                obj._deserialize(item)
                self.DataHistory.append(obj)
        self.ScrollId = params.get("ScrollId")
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
        :type DeviceData: :class:`tencentcloud.iot.v20180123.models.Object`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DeviceData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceData") is not None:
            self.DeviceData = Object()
            self.DeviceData._deserialize(params.get("DeviceData"))
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
        :type DeviceLog: list of Object
        :param ScrollId: 查询游标
        :type ScrollId: list of str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.DeviceLog = None
        self.ScrollId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceLog") is not None:
            self.DeviceLog = []
            for item in params.get("DeviceLog"):
                obj = Object()
                obj._deserialize(item)
                self.DeviceLog.append(obj)
        self.ScrollId = params.get("ScrollId")
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        """
        self.ProductId = None
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class GetDevicesResponse(AbstractModel):
    """GetDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Devices: 设备列表
        :type Devices: list of Device
        :param Total: 设备总数
        :type Total: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = Device()
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :type Products: list of Product
        :param Total: Product总数
        :type Total: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = Product()
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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


class GetUserRequest(AbstractModel):
    """GetUser请求参数结构体

    """


class GetUserResponse(AbstractModel):
    """GetUser返回参数结构体

    """

    def __init__(self):
        """
        :param User: 用户信息
        :type User: :class:`tencentcloud.iot.v20180123.models.User`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.User = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
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
        """
        self.ProductId = None
        self.DeviceName = None
        self.ControlData = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ControlData = params.get("ControlData")


class IssueDeviceControlResponse(AbstractModel):
    """IssueDeviceControl返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Object(AbstractModel):
    """对象

    """


class Product(AbstractModel):
    """产品

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param ProductKey: 产品Key
        :type ProductKey: str
        :param ProductSecret: 产品直连密钥
        :type ProductSecret: str
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
        :type DataTemplate: :class:`tencentcloud.iot.v20180123.models.Object`
        """
        self.ProductId = None
        self.ProductKey = None
        self.ProductSecret = None
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


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductKey = params.get("ProductKey")
        self.ProductSecret = params.get("ProductSecret")
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
            self.DataTemplate = Object()
            self.DataTemplate._deserialize(params.get("DataTemplate"))


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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :type Actions: list of Object
        :param Active: 已启动
        :type Active: int
        :param Deleted: 已删除
        :type Deleted: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
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
                obj = Object()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.Active = params.get("Active")
        self.Deleted = params.get("Deleted")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class RuleQuery(AbstractModel):
    """查询

    """

    def __init__(self):
        """
        :param Field: 字段
        :type Field: str
        :param Topic: Topic
        :type Topic: str
        :param Condition: 过滤规则
        :type Condition: str
        """
        self.Field = None
        self.Topic = None
        self.Condition = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Topic = params.get("Topic")
        self.Condition = params.get("Condition")


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
        :param DataTemplate: 数据模版（json）
        :type DataTemplate: str
        """
        self.ProductId = None
        self.Name = None
        self.Description = None
        self.DataTemplate = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.DataTemplate = params.get("DataTemplate")


class UpdateProductResponse(AbstractModel):
    """UpdateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 更新后的产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
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
        :param Actions: 转发
        :type Actions: list of Object
        """
        self.RuleId = None
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None


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
                obj = Object()
                obj._deserialize(item)
                self.Actions.append(obj)


class UpdateRuleResponse(AbstractModel):
    """UpdateRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class User(AbstractModel):
    """用户

    """

    def __init__(self):
        """
        :param AppId: app_id
        :type AppId: int
        :param Area: 用户类型（1：国内，2：国际）
        :type Area: int
        :param BillingType: 计费类型（日结、月结）
        :type BillingType: str
        :param Status: 用户状态（0：正常，1：欠费，2：恶意）
        :type Status: int
        :param Message: 备注信息
        :type Message: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self.AppId = None
        self.Area = None
        self.BillingType = None
        self.Status = None
        self.Message = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Area = params.get("Area")
        self.BillingType = params.get("BillingType")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")