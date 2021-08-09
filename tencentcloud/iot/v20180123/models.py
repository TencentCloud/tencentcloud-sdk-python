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


class Action(AbstractModel):
    """规则引擎转发动作

    """

    def __init__(self):
        """
        :param Topic: 转发至topic
注意：此字段可能返回 null，表示取不到有效值。\n        :type Topic: :class:`tencentcloud.iot.v20180123.models.TopicAction`\n        :param Service: 转发至第三发
注意：此字段可能返回 null，表示取不到有效值。\n        :type Service: :class:`tencentcloud.iot.v20180123.models.ServiceAction`\n        :param Ckafka: 转发至第三发Ckafka
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ckafka: :class:`tencentcloud.iot.v20180123.models.CkafkaAction`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateRuleRequest(AbstractModel):
    """ActivateRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id\n        :type RuleId: str\n        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateRuleResponse(AbstractModel):
    """ActivateRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddDeviceRequest(AbstractModel):
    """AddDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称，唯一标识某产品下的一个设备\n        :type DeviceName: str\n        """
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
        


class AddDeviceResponse(AbstractModel):
    """AddDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Device: 设备信息\n        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Name: 产品名称，同一区域产品名称需唯一，支持中文、英文字母、中划线和下划线，长度不超过31个字符，中文占两个字符\n        :type Name: str\n        :param Description: 产品描述\n        :type Description: str\n        :param DataTemplate: 数据模版\n        :type DataTemplate: list of DataTemplate\n        :param DataProtocol: 产品版本（native表示基础版，template表示高级版，默认值为template）\n        :type DataProtocol: str\n        :param AuthType: 设备认证方式（1：动态令牌，2：签名直连鉴权）\n        :type AuthType: int\n        :param CommProtocol: 通信方式（other/wifi/cellular/nb-iot）\n        :type CommProtocol: str\n        :param DeviceType: 产品的设备类型（device: 直连设备；sub_device：子设备；gateway：网关设备）\n        :type DeviceType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddProductResponse(AbstractModel):
    """AddProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品信息\n        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Name: 名称\n        :type Name: str\n        :param Description: 描述\n        :type Description: str\n        :param Query: 查询\n        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`\n        :param Actions: 转发动作列表\n        :type Actions: list of Action\n        :param DataType: 数据类型（0：文本，1：二进制）\n        :type DataType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRuleResponse(AbstractModel):
    """AddRule返回参数结构体

    """

    def __init__(self):
        """
        :param Rule: 规则\n        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param TopicName: Topic名称\n        :type TopicName: str\n        """
        self.ProductId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTopicResponse(AbstractModel):
    """AddTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Topic: Topic信息\n        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param UserName: 用户名\n        :type UserName: str\n        :param Password: 密码\n        :type Password: str\n        """
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAddUserResponse(AbstractModel):
    """AppAddUser返回参数结构体

    """

    def __init__(self):
        """
        :param AppUser: 应用用户\n        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppDeleteDeviceResponse(AbstractModel):
    """AppDeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppDevice(AbstractModel):
    """绑定设备

    """

    def __init__(self):
        """
        :param DeviceId: 设备Id\n        :type DeviceId: str\n        :param ProductId: 所属产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param AliasName: 别名\n        :type AliasName: str\n        :param Region: 地区\n        :type Region: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppDeviceDetail(AbstractModel):
    """绑定设备详情

    """

    def __init__(self):
        """
        :param DeviceId: 设备Id\n        :type DeviceId: str\n        :param ProductId: 所属产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param AliasName: 别名\n        :type AliasName: str\n        :param Region: 地区\n        :type Region: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param DeviceInfo: 设备信息（json）\n        :type DeviceInfo: str\n        :param DataTemplate: 数据模板\n        :type DataTemplate: list of DataTemplate\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceDataRequest(AbstractModel):
    """AppGetDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceDataResponse(AbstractModel):
    """AppGetDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceData: 设备数据。\n        :type DeviceData: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceResponse(AbstractModel):
    """AppGetDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppDevice: 绑定设备详情\n        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDeviceDetail`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param DeviceIds: 设备Id列表（单次限制1000个设备）\n        :type DeviceIds: list of str\n        """
        self.AccessToken = None
        self.DeviceIds = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceStatusesResponse(AbstractModel):
    """AppGetDeviceStatuses返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceStatuses: 设备状态\n        :type DeviceStatuses: list of DeviceStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        """
        self.AccessToken = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDevicesResponse(AbstractModel):
    """AppGetDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Devices: 绑定设备列表\n        :type Devices: list of AppDevice\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param UserName: 用户名\n        :type UserName: str\n        :param Password: 密码\n        :type Password: str\n        :param Expire: TTL\n        :type Expire: int\n        """
        self.UserName = None
        self.Password = None
        self.Expire = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetTokenResponse(AbstractModel):
    """AppGetToken返回参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        """
        self.AccessToken = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetUserResponse(AbstractModel):
    """AppGetUser返回参数结构体

    """

    def __init__(self):
        """
        :param AppUser: 用户信息\n        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param ControlData: 控制数据（json）\n        :type ControlData: str\n        :param Metadata: 是否发送metadata字段\n        :type Metadata: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppIssueDeviceControlResponse(AbstractModel):
    """AppIssueDeviceControl返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppResetPasswordRequest(AbstractModel):
    """AppResetPassword请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param OldPassword: 旧密码\n        :type OldPassword: str\n        :param NewPassword: 新密码\n        :type NewPassword: str\n        """
        self.AccessToken = None
        self.OldPassword = None
        self.NewPassword = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.OldPassword = params.get("OldPassword")
        self.NewPassword = params.get("NewPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppResetPasswordResponse(AbstractModel):
    """AppResetPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppSecureAddDeviceRequest(AbstractModel):
    """AppSecureAddDevice请求参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param DeviceSignature: 设备签名\n        :type DeviceSignature: str\n        """
        self.AccessToken = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.DeviceSignature = params.get("DeviceSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSecureAddDeviceResponse(AbstractModel):
    """AppSecureAddDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppDevice: 绑定设备信息\n        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param AliasName: 设备别名\n        :type AliasName: str\n        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppUpdateDeviceResponse(AbstractModel):
    """AppUpdateDevice返回参数结构体

    """

    def __init__(self):
        """
        :param AppDevice: 设备信息\n        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccessToken: 访问Token\n        :type AccessToken: str\n        :param NickName: 昵称\n        :type NickName: str\n        """
        self.AccessToken = None
        self.NickName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppUpdateUserResponse(AbstractModel):
    """AppUpdateUser返回参数结构体

    """

    def __init__(self):
        """
        :param AppUser: 应用用户\n        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ApplicationId: 应用Id\n        :type ApplicationId: str\n        :param UserName: 用户名\n        :type UserName: str\n        :param NickName: 昵称\n        :type NickName: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 修改时间\n        :type UpdateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSubDeviceToGatewayProductRequest(AbstractModel):
    """AssociateSubDeviceToGatewayProduct请求参数结构体

    """

    def __init__(self):
        """
        :param SubDeviceProductId: 子设备产品Id\n        :type SubDeviceProductId: str\n        :param GatewayProductId: 网关产品Id\n        :type GatewayProductId: str\n        """
        self.SubDeviceProductId = None
        self.GatewayProductId = None


    def _deserialize(self, params):
        self.SubDeviceProductId = params.get("SubDeviceProductId")
        self.GatewayProductId = params.get("GatewayProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSubDeviceToGatewayProductResponse(AbstractModel):
    """AssociateSubDeviceToGatewayProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BoolData(AbstractModel):
    """布尔类型数据

    """

    def __init__(self):
        """
        :param Name: 名称\n        :type Name: str\n        :param Desc: 描述\n        :type Desc: str\n        :param Mode: 读写模式\n        :type Mode: str\n        :param Range: 取值列表\n        :type Range: list of bool\n        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaAction(AbstractModel):
    """转发至Ckafka

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param TopicName: topic名称\n        :type TopicName: str\n        :param Region: 地域\n        :type Region: str\n        """
        self.InstanceId = None
        self.TopicName = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataHistoryEntry(AbstractModel):
    """数据历史条目

    """

    def __init__(self):
        """
        :param Id: 日志id\n        :type Id: str\n        :param Timestamp: 时间戳\n        :type Timestamp: int\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Data: 数据\n        :type Data: str\n        """
        self.Id = None
        self.Timestamp = None
        self.DeviceName = None
        self.Data = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Timestamp = params.get("Timestamp")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTemplate(AbstractModel):
    """数据模版

    """

    def __init__(self):
        """
        :param Number: 数字类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Number: :class:`tencentcloud.iot.v20180123.models.NumberData`\n        :param String: 字符串类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type String: :class:`tencentcloud.iot.v20180123.models.StringData`\n        :param Enum: 枚举类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Enum: :class:`tencentcloud.iot.v20180123.models.EnumData`\n        :param Bool: 布尔类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bool: :class:`tencentcloud.iot.v20180123.models.BoolData`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateRuleRequest(AbstractModel):
    """DeactivateRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id\n        :type RuleId: str\n        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateRuleResponse(AbstractModel):
    """DeactivateRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DebugLogEntry(AbstractModel):
    """设备日志条目

    """

    def __init__(self):
        """
        :param Id: 日志id\n        :type Id: str\n        :param Event: 行为（事件）\n        :type Event: str\n        :param LogType: shadow/action/mqtt, 分别表示：影子/规则引擎/上下线日志\n        :type LogType: str\n        :param Timestamp: 时间戳\n        :type Timestamp: int\n        :param Result: success/fail\n        :type Result: str\n        :param Data: 日志详细内容\n        :type Data: str\n        :param Topic: 数据来源topic\n        :type Topic: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        """
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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 规则Id\n        :type RuleId: str\n        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: TopicId\n        :type TopicId: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        """
        self.TopicId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Device(AbstractModel):
    """设备

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param DeviceSecret: 设备密钥\n        :type DeviceSecret: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param DeviceInfo: 设备信息（json）\n        :type DeviceInfo: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceEntry(AbstractModel):
    """设备条目

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param DeviceSecret: 设备密钥\n        :type DeviceSecret: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceSecret = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceSecret = params.get("DeviceSecret")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceLogEntry(AbstractModel):
    """设备日志条目

    """

    def __init__(self):
        """
        :param Id: 日志id\n        :type Id: str\n        :param Msg: 日志内容\n        :type Msg: str\n        :param Code: 状态码\n        :type Code: str\n        :param Timestamp: 时间戳\n        :type Timestamp: int\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Method: 设备动作\n        :type Method: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceSignature(AbstractModel):
    """设备签名

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param DeviceSignature: 设备签名\n        :type DeviceSignature: str\n        """
        self.DeviceName = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DeviceSignature = params.get("DeviceSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatData(AbstractModel):
    """设备统计数据

    """

    def __init__(self):
        """
        :param Datetime: 时间点\n        :type Datetime: str\n        :param DeviceOnline: 在线设备数\n        :type DeviceOnline: int\n        :param DeviceActive: 激活设备数\n        :type DeviceActive: int\n        :param DeviceTotal: 设备总数\n        :type DeviceTotal: int\n        """
        self.Datetime = None
        self.DeviceOnline = None
        self.DeviceActive = None
        self.DeviceTotal = None


    def _deserialize(self, params):
        self.Datetime = params.get("Datetime")
        self.DeviceOnline = params.get("DeviceOnline")
        self.DeviceActive = params.get("DeviceActive")
        self.DeviceTotal = params.get("DeviceTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatus(AbstractModel):
    """设备状态

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param Status: 设备状态（inactive, online, offline）\n        :type Status: str\n        :param FirstOnline: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstOnline: str\n        :param LastOnline: 最后上线时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastOnline: str\n        :param OnlineTimes: 上线次数\n        :type OnlineTimes: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnumData(AbstractModel):
    """枚举类型数据

    """

    def __init__(self):
        """
        :param Name: 名称\n        :type Name: str\n        :param Desc: 描述\n        :type Desc: str\n        :param Mode: 读写模式\n        :type Mode: str\n        :param Range: 取值列表\n        :type Range: list of str\n        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDataHistoryRequest(AbstractModel):
    """GetDataHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceNames: 设备名称列表，允许最多一次100台\n        :type DeviceNames: list of str\n        :param StartTime: 查询开始时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间\n        :type EndTime: str\n        :param Size: 查询数据量\n        :type Size: int\n        :param Order: 时间排序（desc/asc）\n        :type Order: str\n        :param ScrollId: 查询游标\n        :type ScrollId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDataHistoryResponse(AbstractModel):
    """GetDataHistory返回参数结构体

    """

    def __init__(self):
        """
        :param DataHistory: 数据历史\n        :type DataHistory: list of DataHistoryEntry\n        :param ScrollId: 查询游标\n        :type ScrollId: str\n        :param ScrollTimeout: 查询游标超时\n        :type ScrollTimeout: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceNames: 设备名称列表，最大支持100台\n        :type DeviceNames: list of str\n        :param StartTime: 查询开始时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间\n        :type EndTime: str\n        :param Size: 查询数据量\n        :type Size: int\n        :param Order: 时间排序（desc/asc）\n        :type Order: str\n        :param ScrollId: 查询游标\n        :type ScrollId: str\n        :param Type: 日志类型（shadow/action/mqtt）\n        :type Type: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDebugLogResponse(AbstractModel):
    """GetDebugLog返回参数结构体

    """

    def __init__(self):
        """
        :param DebugLog: 调试日志\n        :type DebugLog: list of DebugLogEntry\n        :param ScrollId: 查询游标\n        :type ScrollId: str\n        :param ScrollTimeout: 游标超时\n        :type ScrollTimeout: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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
        


class GetDeviceDataResponse(AbstractModel):
    """GetDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceData: 设备数据\n        :type DeviceData: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceNames: 设备名称列表，最大支持100台\n        :type DeviceNames: list of str\n        :param StartTime: 查询开始时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间\n        :type EndTime: str\n        :param Size: 查询数据量\n        :type Size: int\n        :param Order: 时间排序（desc/asc）\n        :type Order: str\n        :param ScrollId: 查询游标\n        :type ScrollId: str\n        :param Type: 日志类型（comm/status）\n        :type Type: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLogResponse(AbstractModel):
    """GetDeviceLog返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceLog: 设备日志\n        :type DeviceLog: list of DeviceLogEntry\n        :param ScrollId: 查询游标\n        :type ScrollId: str\n        :param ScrollTimeout: 游标超时\n        :type ScrollTimeout: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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
        


class GetDeviceResponse(AbstractModel):
    """GetDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Device: 设备信息\n        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceNames: 设备名称列表（单次限制1000个设备）\n        :type DeviceNames: list of str\n        :param Expire: 过期时间\n        :type Expire: int\n        """
        self.ProductId = None
        self.DeviceNames = None
        self.Expire = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceSignaturesResponse(AbstractModel):
    """GetDeviceSignatures返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceSignatures: 设备绑定签名列表\n        :type DeviceSignatures: list of DeviceSignature\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Products: 产品Id列表\n        :type Products: list of str\n        :param StartDate: 开始日期\n        :type StartDate: str\n        :param EndDate: 结束日期\n        :type EndDate: str\n        """
        self.Products = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.Products = params.get("Products")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceStatisticsResponse(AbstractModel):
    """GetDeviceStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceStatistics: 统计数据\n        :type DeviceStatistics: list of DeviceStatData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品ID\n        :type ProductId: str\n        :param DeviceNames: 设备名称列表（单次限制1000个设备）\n        :type DeviceNames: list of str\n        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceStatusesResponse(AbstractModel):
    """GetDeviceStatuses返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceStatuses: 设备状态列表\n        :type DeviceStatuses: list of DeviceStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param Offset: 偏移\n        :type Offset: int\n        :param Length: 长度\n        :type Length: int\n        :param Keyword: 关键字查询\n        :type Keyword: str\n        """
        self.ProductId = None
        self.Offset = None
        self.Length = None
        self.Keyword = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicesResponse(AbstractModel):
    """GetDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Devices: 设备列表\n        :type Devices: list of DeviceEntry\n        :param Total: 设备总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProductResponse(AbstractModel):
    """GetProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 产品信息\n        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移\n        :type Offset: int\n        :param Length: 长度\n        :type Length: int\n        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProductsResponse(AbstractModel):
    """GetProducts返回参数结构体

    """

    def __init__(self):
        """
        :param Products: Product列表\n        :type Products: list of ProductEntry\n        :param Total: Product总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleId: 规则Id\n        :type RuleId: str\n        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuleResponse(AbstractModel):
    """GetRule返回参数结构体

    """

    def __init__(self):
        """
        :param Rule: 规则\n        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移\n        :type Offset: int\n        :param Length: 长度\n        :type Length: int\n        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRulesResponse(AbstractModel):
    """GetRules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 规则列表\n        :type Rules: list of Rule\n        :param Total: 规则总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TopicId: TopicId\n        :type TopicId: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        """
        self.TopicId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTopicResponse(AbstractModel):
    """GetTopic返回参数结构体

    """

    def __init__(self):
        """
        :param Topic: Topic信息\n        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param Offset: 偏移\n        :type Offset: int\n        :param Length: 长度\n        :type Length: int\n        """
        self.ProductId = None
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTopicsResponse(AbstractModel):
    """GetTopics返回参数结构体

    """

    def __init__(self):
        """
        :param Topics: Topic列表\n        :type Topics: list of Topic\n        :param Total: Topic总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        :param ControlData: 控制数据（json）\n        :type ControlData: str\n        :param Metadata: 是否发送metadata字段\n        :type Metadata: bool\n        """
        self.ProductId = None
        self.DeviceName = None
        self.ControlData = None
        self.Metadata = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ControlData = params.get("ControlData")
        self.Metadata = params.get("Metadata")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueDeviceControlResponse(AbstractModel):
    """IssueDeviceControl返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NumberData(AbstractModel):
    """数字类型数据

    """

    def __init__(self):
        """
        :param Name: 名称\n        :type Name: str\n        :param Desc: 描述\n        :type Desc: str\n        :param Mode: 读写模式\n        :type Mode: str\n        :param Range: 取值范围\n        :type Range: list of float\n        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Product(AbstractModel):
    """产品

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param ProductKey: 产品Key\n        :type ProductKey: str\n        :param AppId: AppId\n        :type AppId: int\n        :param Name: 产品名称\n        :type Name: str\n        :param Description: 产品描述\n        :type Description: str\n        :param Domain: 连接域名\n        :type Domain: str\n        :param Standard: 产品规格\n        :type Standard: int\n        :param AuthType: 鉴权类型（0：直连，1：Token）\n        :type AuthType: int\n        :param Deleted: 删除（0未删除）\n        :type Deleted: int\n        :param Message: 备注\n        :type Message: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param DataTemplate: 数据模版\n        :type DataTemplate: list of DataTemplate\n        :param DataProtocol: 数据协议（native/template）\n        :type DataProtocol: str\n        :param Username: 直连用户名\n        :type Username: str\n        :param Password: 直连密码\n        :type Password: str\n        :param CommProtocol: 通信方式\n        :type CommProtocol: str\n        :param Qps: qps\n        :type Qps: int\n        :param Region: 地域\n        :type Region: str\n        :param DeviceType: 产品的设备类型\n        :type DeviceType: str\n        :param AssociatedProducts: 关联的产品列表\n        :type AssociatedProducts: list of str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductEntry(AbstractModel):
    """产品条目

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param ProductKey: 产品Key\n        :type ProductKey: str\n        :param AppId: AppId\n        :type AppId: int\n        :param Name: 产品名称\n        :type Name: str\n        :param Description: 产品描述\n        :type Description: str\n        :param Domain: 连接域名\n        :type Domain: str\n        :param AuthType: 鉴权类型（0：直连，1：Token）\n        :type AuthType: int\n        :param DataProtocol: 数据协议（native/template）\n        :type DataProtocol: str\n        :param Deleted: 删除（0未删除）\n        :type Deleted: int\n        :param Message: 备注\n        :type Message: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param CommProtocol: 通信方式\n        :type CommProtocol: str\n        :param Region: 地域\n        :type Region: str\n        :param DeviceType: 设备类型\n        :type DeviceType: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMsgRequest(AbstractModel):
    """PublishMsg请求参数结构体

    """

    def __init__(self):
        """
        :param Topic: Topic\n        :type Topic: str\n        :param Message: 消息内容\n        :type Message: str\n        :param Qos: Qos(目前QoS支持0与1)\n        :type Qos: int\n        """
        self.Topic = None
        self.Message = None
        self.Qos = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Message = params.get("Message")
        self.Qos = params.get("Qos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMsgResponse(AbstractModel):
    """PublishMsg返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceRequest(AbstractModel):
    """ResetDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param DeviceName: 设备名称\n        :type DeviceName: str\n        """
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
        


class ResetDeviceResponse(AbstractModel):
    """ResetDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Device: 设备信息\n        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleId: 规则Id\n        :type RuleId: str\n        :param AppId: AppId\n        :type AppId: int\n        :param Name: 名称\n        :type Name: str\n        :param Description: 描述\n        :type Description: str\n        :param Query: 查询\n        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`\n        :param Actions: 转发\n        :type Actions: list of Action\n        :param Active: 已启动\n        :type Active: int\n        :param Deleted: 已删除\n        :type Deleted: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param MsgOrder: 消息顺序\n        :type MsgOrder: int\n        :param DataType: 数据类型（0：文本，1：二进制）\n        :type DataType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleQuery(AbstractModel):
    """查询

    """

    def __init__(self):
        """
        :param Field: 字段\n        :type Field: str\n        :param Condition: 过滤规则\n        :type Condition: str\n        :param Topic: Topic
注意：此字段可能返回 null，表示取不到有效值。\n        :type Topic: str\n        :param ProductId: 产品Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductId: str\n        """
        self.Field = None
        self.Condition = None
        self.Topic = None
        self.ProductId = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Condition = params.get("Condition")
        self.Topic = params.get("Topic")
        self.ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceAction(AbstractModel):
    """转发到第三方http(s)服务

    """

    def __init__(self):
        """
        :param Url: 服务url地址\n        :type Url: str\n        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StringData(AbstractModel):
    """数字类型数据

    """

    def __init__(self):
        """
        :param Name: 名称\n        :type Name: str\n        :param Desc: 描述\n        :type Desc: str\n        :param Mode: 读写模式\n        :type Mode: str\n        :param Range: 长度范围\n        :type Range: list of int non-negative\n        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Topic(AbstractModel):
    """Topic

    """

    def __init__(self):
        """
        :param TopicId: TopicId\n        :type TopicId: str\n        :param TopicName: Topic名称\n        :type TopicName: str\n        :param ProductId: 产品Id\n        :type ProductId: str\n        :param MsgLife: 消息最大生命周期\n        :type MsgLife: int\n        :param MsgSize: 消息最大大小\n        :type MsgSize: int\n        :param MsgCount: 消息最大数量\n        :type MsgCount: int\n        :param Deleted: 已删除\n        :type Deleted: int\n        :param Path: Topic完整路径\n        :type Path: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicAction(AbstractModel):
    """转发到topic动作

    """

    def __init__(self):
        """
        :param Topic: 目标topic\n        :type Topic: str\n        """
        self.Topic = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassociateSubDeviceFromGatewayProductRequest(AbstractModel):
    """UnassociateSubDeviceFromGatewayProduct请求参数结构体

    """

    def __init__(self):
        """
        :param SubDeviceProductId: 子设备产品Id\n        :type SubDeviceProductId: str\n        :param GatewayProductId: 网关设备产品Id\n        :type GatewayProductId: str\n        """
        self.SubDeviceProductId = None
        self.GatewayProductId = None


    def _deserialize(self, params):
        self.SubDeviceProductId = params.get("SubDeviceProductId")
        self.GatewayProductId = params.get("GatewayProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassociateSubDeviceFromGatewayProductResponse(AbstractModel):
    """UnassociateSubDeviceFromGatewayProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateProductRequest(AbstractModel):
    """UpdateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id\n        :type ProductId: str\n        :param Name: 产品名称\n        :type Name: str\n        :param Description: 产品描述\n        :type Description: str\n        :param DataTemplate: 数据模版\n        :type DataTemplate: list of DataTemplate\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProductResponse(AbstractModel):
    """UpdateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Product: 更新后的产品信息\n        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RuleId: 规则Id\n        :type RuleId: str\n        :param Name: 名称\n        :type Name: str\n        :param Description: 描述\n        :type Description: str\n        :param Query: 查询\n        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`\n        :param Actions: 转发动作列表\n        :type Actions: list of Action\n        :param DataType: 数据类型（0：文本，1：二进制）\n        :type DataType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuleResponse(AbstractModel):
    """UpdateRule返回参数结构体

    """

    def __init__(self):
        """
        :param Rule: 规则\n        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = Rule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")