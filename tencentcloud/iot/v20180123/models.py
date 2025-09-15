# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""规则引擎转发动作

    """

    def __init__(self):
        r"""
        :param _Topic: 转发至topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: :class:`tencentcloud.iot.v20180123.models.TopicAction`
        :param _Service: 转发至第三发
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.iot.v20180123.models.ServiceAction`
        :param _Ckafka: 转发至第三发Ckafka
注意：此字段可能返回 null，表示取不到有效值。
        :type Ckafka: :class:`tencentcloud.iot.v20180123.models.CkafkaAction`
        """
        self._Topic = None
        self._Service = None
        self._Ckafka = None

    @property
    def Topic(self):
        r"""转发至topic
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iot.v20180123.models.TopicAction`
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Service(self):
        r"""转发至第三发
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iot.v20180123.models.ServiceAction`
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Ckafka(self):
        r"""转发至第三发Ckafka
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iot.v20180123.models.CkafkaAction`
        """
        return self._Ckafka

    @Ckafka.setter
    def Ckafka(self, Ckafka):
        self._Ckafka = Ckafka


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self._Topic = TopicAction()
            self._Topic._deserialize(params.get("Topic"))
        if params.get("Service") is not None:
            self._Service = ServiceAction()
            self._Service._deserialize(params.get("Service"))
        if params.get("Ckafka") is not None:
            self._Ckafka = CkafkaAction()
            self._Ckafka._deserialize(params.get("Ckafka"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateRuleRequest(AbstractModel):
    r"""ActivateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateRuleResponse(AbstractModel):
    r"""ActivateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AddDeviceRequest(AbstractModel):
    r"""AddDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称，唯一标识某产品下的一个设备
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称，唯一标识某产品下的一个设备
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDeviceResponse(AbstractModel):
    r"""AddDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Device: 设备信息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Device = None
        self._RequestId = None

    @property
    def Device(self):
        r"""设备信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        self._RequestId = params.get("RequestId")


class AddProductRequest(AbstractModel):
    r"""AddProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 产品名称，同一区域产品名称需唯一，支持中文、英文字母、中划线和下划线，长度不超过31个字符，中文占两个字符
        :type Name: str
        :param _Description: 产品描述
        :type Description: str
        :param _DataTemplate: 数据模版
        :type DataTemplate: list of DataTemplate
        :param _DataProtocol: 产品版本（native表示基础版，template表示高级版，默认值为template）
        :type DataProtocol: str
        :param _AuthType: 设备认证方式（1：动态令牌，2：签名直连鉴权）
        :type AuthType: int
        :param _CommProtocol: 通信方式（other/wifi/cellular/nb-iot）
        :type CommProtocol: str
        :param _DeviceType: 产品的设备类型（device: 直连设备；sub_device：子设备；gateway：网关设备）
        :type DeviceType: str
        """
        self._Name = None
        self._Description = None
        self._DataTemplate = None
        self._DataProtocol = None
        self._AuthType = None
        self._CommProtocol = None
        self._DeviceType = None

    @property
    def Name(self):
        r"""产品名称，同一区域产品名称需唯一，支持中文、英文字母、中划线和下划线，长度不超过31个字符，中文占两个字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""产品描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DataTemplate(self):
        r"""数据模版
        :rtype: list of DataTemplate
        """
        return self._DataTemplate

    @DataTemplate.setter
    def DataTemplate(self, DataTemplate):
        self._DataTemplate = DataTemplate

    @property
    def DataProtocol(self):
        r"""产品版本（native表示基础版，template表示高级版，默认值为template）
        :rtype: str
        """
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def AuthType(self):
        r"""设备认证方式（1：动态令牌，2：签名直连鉴权）
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def CommProtocol(self):
        r"""通信方式（other/wifi/cellular/nb-iot）
        :rtype: str
        """
        return self._CommProtocol

    @CommProtocol.setter
    def CommProtocol(self, CommProtocol):
        self._CommProtocol = CommProtocol

    @property
    def DeviceType(self):
        r"""产品的设备类型（device: 直连设备；sub_device：子设备；gateway：网关设备）
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("DataTemplate") is not None:
            self._DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self._DataTemplate.append(obj)
        self._DataProtocol = params.get("DataProtocol")
        self._AuthType = params.get("AuthType")
        self._CommProtocol = params.get("CommProtocol")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddProductResponse(AbstractModel):
    r"""AddProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Product = None
        self._RequestId = None

    @property
    def Product(self):
        r"""产品信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Product`
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self._Product = Product()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class AddRuleRequest(AbstractModel):
    r"""AddRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _Query: 查询
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param _Actions: 转发动作列表
        :type Actions: list of Action
        :param _DataType: 数据类型（0：文本，1：二进制）
        :type DataType: int
        """
        self._Name = None
        self._Description = None
        self._Query = None
        self._Actions = None
        self._DataType = None

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Query(self):
        r"""查询
        :rtype: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Actions(self):
        r"""转发动作列表
        :rtype: list of Action
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def DataType(self):
        r"""数据类型（0：文本，1：二进制）
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Query") is not None:
            self._Query = RuleQuery()
            self._Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self._Actions.append(obj)
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRuleResponse(AbstractModel):
    r"""AddRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._RequestId = None

    @property
    def Rule(self):
        r"""规则
        :rtype: :class:`tencentcloud.iot.v20180123.models.Rule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = Rule()
            self._Rule._deserialize(params.get("Rule"))
        self._RequestId = params.get("RequestId")


class AddTopicRequest(AbstractModel):
    r"""AddTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _TopicName: Topic名称
        :type TopicName: str
        """
        self._ProductId = None
        self._TopicName = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def TopicName(self):
        r"""Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTopicResponse(AbstractModel):
    r"""AddTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: Topic信息
        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topic = None
        self._RequestId = None

    @property
    def Topic(self):
        r"""Topic信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Topic`
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self._Topic = Topic()
            self._Topic._deserialize(params.get("Topic"))
        self._RequestId = params.get("RequestId")


class AppAddUserRequest(AbstractModel):
    r"""AppAddUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Password: 密码
        :type Password: str
        """
        self._UserName = None
        self._Password = None

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAddUserResponse(AbstractModel):
    r"""AppAddUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppUser: 应用用户
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppUser = None
        self._RequestId = None

    @property
    def AppUser(self):
        r"""应用用户
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppUser`
        """
        return self._AppUser

    @AppUser.setter
    def AppUser(self, AppUser):
        self._AppUser = AppUser

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self._AppUser = AppUser()
            self._AppUser._deserialize(params.get("AppUser"))
        self._RequestId = params.get("RequestId")


class AppDeleteDeviceRequest(AbstractModel):
    r"""AppDeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._AccessToken = None
        self._ProductId = None
        self._DeviceName = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppDeleteDeviceResponse(AbstractModel):
    r"""AppDeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AppDevice(AbstractModel):
    r"""绑定设备

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _ProductId: 所属产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _AliasName: 别名
        :type AliasName: str
        :param _Region: 地区
        :type Region: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._DeviceId = None
        self._ProductId = None
        self._DeviceName = None
        self._AliasName = None
        self._Region = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def DeviceId(self):
        r"""设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ProductId(self):
        r"""所属产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def AliasName(self):
        r"""别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def Region(self):
        r"""地区
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._AliasName = params.get("AliasName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppDeviceDetail(AbstractModel):
    r"""绑定设备详情

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备Id
        :type DeviceId: str
        :param _ProductId: 所属产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _AliasName: 别名
        :type AliasName: str
        :param _Region: 地区
        :type Region: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _DeviceInfo: 设备信息（json）
        :type DeviceInfo: str
        :param _DataTemplate: 数据模板
        :type DataTemplate: list of DataTemplate
        """
        self._DeviceId = None
        self._ProductId = None
        self._DeviceName = None
        self._AliasName = None
        self._Region = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DeviceInfo = None
        self._DataTemplate = None

    @property
    def DeviceId(self):
        r"""设备Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ProductId(self):
        r"""所属产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def AliasName(self):
        r"""别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def Region(self):
        r"""地区
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DeviceInfo(self):
        r"""设备信息（json）
        :rtype: str
        """
        return self._DeviceInfo

    @DeviceInfo.setter
    def DeviceInfo(self, DeviceInfo):
        self._DeviceInfo = DeviceInfo

    @property
    def DataTemplate(self):
        r"""数据模板
        :rtype: list of DataTemplate
        """
        return self._DataTemplate

    @DataTemplate.setter
    def DataTemplate(self, DataTemplate):
        self._DataTemplate = DataTemplate


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._AliasName = params.get("AliasName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DeviceInfo = params.get("DeviceInfo")
        if params.get("DataTemplate") is not None:
            self._DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self._DataTemplate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceDataRequest(AbstractModel):
    r"""AppGetDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._AccessToken = None
        self._ProductId = None
        self._DeviceName = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceDataResponse(AbstractModel):
    r"""AppGetDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceData: 设备数据。
        :type DeviceData: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceData = None
        self._RequestId = None

    @property
    def DeviceData(self):
        r"""设备数据。
        :rtype: str
        """
        return self._DeviceData

    @DeviceData.setter
    def DeviceData(self, DeviceData):
        self._DeviceData = DeviceData

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceData = params.get("DeviceData")
        self._RequestId = params.get("RequestId")


class AppGetDeviceRequest(AbstractModel):
    r"""AppGetDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._AccessToken = None
        self._ProductId = None
        self._DeviceName = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceResponse(AbstractModel):
    r"""AppGetDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppDevice: 绑定设备详情
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDeviceDetail`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppDevice = None
        self._RequestId = None

    @property
    def AppDevice(self):
        r"""绑定设备详情
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppDeviceDetail`
        """
        return self._AppDevice

    @AppDevice.setter
    def AppDevice(self, AppDevice):
        self._AppDevice = AppDevice

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self._AppDevice = AppDeviceDetail()
            self._AppDevice._deserialize(params.get("AppDevice"))
        self._RequestId = params.get("RequestId")


class AppGetDeviceStatusesRequest(AbstractModel):
    r"""AppGetDeviceStatuses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _DeviceIds: 设备Id列表（单次限制1000个设备）
        :type DeviceIds: list of str
        """
        self._AccessToken = None
        self._DeviceIds = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def DeviceIds(self):
        r"""设备Id列表（单次限制1000个设备）
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDeviceStatusesResponse(AbstractModel):
    r"""AppGetDeviceStatuses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceStatuses: 设备状态
        :type DeviceStatuses: list of DeviceStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceStatuses = None
        self._RequestId = None

    @property
    def DeviceStatuses(self):
        r"""设备状态
        :rtype: list of DeviceStatus
        """
        return self._DeviceStatuses

    @DeviceStatuses.setter
    def DeviceStatuses(self, DeviceStatuses):
        self._DeviceStatuses = DeviceStatuses

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceStatuses") is not None:
            self._DeviceStatuses = []
            for item in params.get("DeviceStatuses"):
                obj = DeviceStatus()
                obj._deserialize(item)
                self._DeviceStatuses.append(obj)
        self._RequestId = params.get("RequestId")


class AppGetDevicesRequest(AbstractModel):
    r"""AppGetDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        """
        self._AccessToken = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetDevicesResponse(AbstractModel):
    r"""AppGetDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 绑定设备列表
        :type Devices: list of AppDevice
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._RequestId = None

    @property
    def Devices(self):
        r"""绑定设备列表
        :rtype: list of AppDevice
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = AppDevice()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class AppGetTokenRequest(AbstractModel):
    r"""AppGetToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserName: 用户名
        :type UserName: str
        :param _Password: 密码
        :type Password: str
        :param _Expire: TTL
        :type Expire: int
        """
        self._UserName = None
        self._Password = None
        self._Expire = None

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        r"""密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Expire(self):
        r"""TTL
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetTokenResponse(AbstractModel):
    r"""AppGetToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessToken = None
        self._RequestId = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._RequestId = params.get("RequestId")


class AppGetUserRequest(AbstractModel):
    r"""AppGetUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        """
        self._AccessToken = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGetUserResponse(AbstractModel):
    r"""AppGetUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppUser: 用户信息
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppUser = None
        self._RequestId = None

    @property
    def AppUser(self):
        r"""用户信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppUser`
        """
        return self._AppUser

    @AppUser.setter
    def AppUser(self, AppUser):
        self._AppUser = AppUser

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self._AppUser = AppUser()
            self._AppUser._deserialize(params.get("AppUser"))
        self._RequestId = params.get("RequestId")


class AppIssueDeviceControlRequest(AbstractModel):
    r"""AppIssueDeviceControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ControlData: 控制数据（json）
        :type ControlData: str
        :param _Metadata: 是否发送metadata字段
        :type Metadata: bool
        """
        self._AccessToken = None
        self._ProductId = None
        self._DeviceName = None
        self._ControlData = None
        self._Metadata = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ControlData(self):
        r"""控制数据（json）
        :rtype: str
        """
        return self._ControlData

    @ControlData.setter
    def ControlData(self, ControlData):
        self._ControlData = ControlData

    @property
    def Metadata(self):
        r"""是否发送metadata字段
        :rtype: bool
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ControlData = params.get("ControlData")
        self._Metadata = params.get("Metadata")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppIssueDeviceControlResponse(AbstractModel):
    r"""AppIssueDeviceControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AppResetPasswordRequest(AbstractModel):
    r"""AppResetPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _OldPassword: 旧密码
        :type OldPassword: str
        :param _NewPassword: 新密码
        :type NewPassword: str
        """
        self._AccessToken = None
        self._OldPassword = None
        self._NewPassword = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def OldPassword(self):
        r"""旧密码
        :rtype: str
        """
        return self._OldPassword

    @OldPassword.setter
    def OldPassword(self, OldPassword):
        self._OldPassword = OldPassword

    @property
    def NewPassword(self):
        r"""新密码
        :rtype: str
        """
        return self._NewPassword

    @NewPassword.setter
    def NewPassword(self, NewPassword):
        self._NewPassword = NewPassword


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._OldPassword = params.get("OldPassword")
        self._NewPassword = params.get("NewPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppResetPasswordResponse(AbstractModel):
    r"""AppResetPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AppSecureAddDeviceRequest(AbstractModel):
    r"""AppSecureAddDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _DeviceSignature: 设备签名
        :type DeviceSignature: str
        """
        self._AccessToken = None
        self._DeviceSignature = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def DeviceSignature(self):
        r"""设备签名
        :rtype: str
        """
        return self._DeviceSignature

    @DeviceSignature.setter
    def DeviceSignature(self, DeviceSignature):
        self._DeviceSignature = DeviceSignature


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._DeviceSignature = params.get("DeviceSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSecureAddDeviceResponse(AbstractModel):
    r"""AppSecureAddDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppDevice: 绑定设备信息
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppDevice = None
        self._RequestId = None

    @property
    def AppDevice(self):
        r"""绑定设备信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        """
        return self._AppDevice

    @AppDevice.setter
    def AppDevice(self, AppDevice):
        self._AppDevice = AppDevice

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self._AppDevice = AppDevice()
            self._AppDevice._deserialize(params.get("AppDevice"))
        self._RequestId = params.get("RequestId")


class AppUpdateDeviceRequest(AbstractModel):
    r"""AppUpdateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _AliasName: 设备别名
        :type AliasName: str
        """
        self._AccessToken = None
        self._ProductId = None
        self._DeviceName = None
        self._AliasName = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def AliasName(self):
        r"""设备别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._AliasName = params.get("AliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppUpdateDeviceResponse(AbstractModel):
    r"""AppUpdateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppDevice: 设备信息
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppDevice = None
        self._RequestId = None

    @property
    def AppDevice(self):
        r"""设备信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        """
        return self._AppDevice

    @AppDevice.setter
    def AppDevice(self, AppDevice):
        self._AppDevice = AppDevice

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self._AppDevice = AppDevice()
            self._AppDevice._deserialize(params.get("AppDevice"))
        self._RequestId = params.get("RequestId")


class AppUpdateUserRequest(AbstractModel):
    r"""AppUpdateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问Token
        :type AccessToken: str
        :param _NickName: 昵称
        :type NickName: str
        """
        self._AccessToken = None
        self._NickName = None

    @property
    def AccessToken(self):
        r"""访问Token
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def NickName(self):
        r"""昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName


    def _deserialize(self, params):
        self._AccessToken = params.get("AccessToken")
        self._NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppUpdateUserResponse(AbstractModel):
    r"""AppUpdateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppUser: 应用用户
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppUser = None
        self._RequestId = None

    @property
    def AppUser(self):
        r"""应用用户
        :rtype: :class:`tencentcloud.iot.v20180123.models.AppUser`
        """
        return self._AppUser

    @AppUser.setter
    def AppUser(self, AppUser):
        self._AppUser = AppUser

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self._AppUser = AppUser()
            self._AppUser._deserialize(params.get("AppUser"))
        self._RequestId = params.get("RequestId")


class AppUser(AbstractModel):
    r"""应用用户

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用Id
        :type ApplicationId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _NickName: 昵称
        :type NickName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        """
        self._ApplicationId = None
        self._UserName = None
        self._NickName = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ApplicationId(self):
        r"""应用Id
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def UserName(self):
        r"""用户名
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def NickName(self):
        r"""昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._UserName = params.get("UserName")
        self._NickName = params.get("NickName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSubDeviceToGatewayProductRequest(AbstractModel):
    r"""AssociateSubDeviceToGatewayProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubDeviceProductId: 子设备产品Id
        :type SubDeviceProductId: str
        :param _GatewayProductId: 网关产品Id
        :type GatewayProductId: str
        """
        self._SubDeviceProductId = None
        self._GatewayProductId = None

    @property
    def SubDeviceProductId(self):
        r"""子设备产品Id
        :rtype: str
        """
        return self._SubDeviceProductId

    @SubDeviceProductId.setter
    def SubDeviceProductId(self, SubDeviceProductId):
        self._SubDeviceProductId = SubDeviceProductId

    @property
    def GatewayProductId(self):
        r"""网关产品Id
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId


    def _deserialize(self, params):
        self._SubDeviceProductId = params.get("SubDeviceProductId")
        self._GatewayProductId = params.get("GatewayProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSubDeviceToGatewayProductResponse(AbstractModel):
    r"""AssociateSubDeviceToGatewayProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BoolData(AbstractModel):
    r"""布尔类型数据

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Desc: 描述
        :type Desc: str
        :param _Mode: 读写模式
        :type Mode: str
        :param _Range: 取值列表
        :type Range: list of bool
        """
        self._Name = None
        self._Desc = None
        self._Mode = None
        self._Range = None

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Mode(self):
        r"""读写模式
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Range(self):
        r"""取值列表
        :rtype: list of bool
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Mode = params.get("Mode")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaAction(AbstractModel):
    r"""转发至Ckafka

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _TopicName: topic名称
        :type TopicName: str
        :param _Region: 地域
        :type Region: str
        """
        self._InstanceId = None
        self._TopicName = None
        self._Region = None

    @property
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TopicName(self):
        r"""topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._TopicName = params.get("TopicName")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataHistoryEntry(AbstractModel):
    r"""数据历史条目

    """

    def __init__(self):
        r"""
        :param _Id: 日志id
        :type Id: str
        :param _Timestamp: 时间戳
        :type Timestamp: int
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Data: 数据
        :type Data: str
        """
        self._Id = None
        self._Timestamp = None
        self._DeviceName = None
        self._Data = None

    @property
    def Id(self):
        r"""日志id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Timestamp(self):
        r"""时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Data(self):
        r"""数据
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Timestamp = params.get("Timestamp")
        self._DeviceName = params.get("DeviceName")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataTemplate(AbstractModel):
    r"""数据模版

    """

    def __init__(self):
        r"""
        :param _Number: 数字类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Number: :class:`tencentcloud.iot.v20180123.models.NumberData`
        :param _String: 字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :type String: :class:`tencentcloud.iot.v20180123.models.StringData`
        :param _Enum: 枚举类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Enum: :class:`tencentcloud.iot.v20180123.models.EnumData`
        :param _Bool: 布尔类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Bool: :class:`tencentcloud.iot.v20180123.models.BoolData`
        """
        self._Number = None
        self._String = None
        self._Enum = None
        self._Bool = None

    @property
    def Number(self):
        r"""数字类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iot.v20180123.models.NumberData`
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def String(self):
        r"""字符串类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iot.v20180123.models.StringData`
        """
        return self._String

    @String.setter
    def String(self, String):
        self._String = String

    @property
    def Enum(self):
        r"""枚举类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iot.v20180123.models.EnumData`
        """
        return self._Enum

    @Enum.setter
    def Enum(self, Enum):
        self._Enum = Enum

    @property
    def Bool(self):
        r"""布尔类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iot.v20180123.models.BoolData`
        """
        return self._Bool

    @Bool.setter
    def Bool(self, Bool):
        self._Bool = Bool


    def _deserialize(self, params):
        if params.get("Number") is not None:
            self._Number = NumberData()
            self._Number._deserialize(params.get("Number"))
        if params.get("String") is not None:
            self._String = StringData()
            self._String._deserialize(params.get("String"))
        if params.get("Enum") is not None:
            self._Enum = EnumData()
            self._Enum._deserialize(params.get("Enum"))
        if params.get("Bool") is not None:
            self._Bool = BoolData()
            self._Bool._deserialize(params.get("Bool"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateRuleRequest(AbstractModel):
    r"""DeactivateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateRuleResponse(AbstractModel):
    r"""DeactivateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DebugLogEntry(AbstractModel):
    r"""设备日志条目

    """

    def __init__(self):
        r"""
        :param _Id: 日志id
        :type Id: str
        :param _Event: 行为（事件）
        :type Event: str
        :param _LogType: shadow/action/mqtt, 分别表示：影子/规则引擎/上下线日志
        :type LogType: str
        :param _Timestamp: 时间戳
        :type Timestamp: int
        :param _Result: success/fail
        :type Result: str
        :param _Data: 日志详细内容
        :type Data: str
        :param _Topic: 数据来源topic
        :type Topic: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._Id = None
        self._Event = None
        self._LogType = None
        self._Timestamp = None
        self._Result = None
        self._Data = None
        self._Topic = None
        self._DeviceName = None

    @property
    def Id(self):
        r"""日志id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Event(self):
        r"""行为（事件）
        :rtype: str
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def LogType(self):
        r"""shadow/action/mqtt, 分别表示：影子/规则引擎/上下线日志
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def Timestamp(self):
        r"""时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Result(self):
        r"""success/fail
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Data(self):
        r"""日志详细内容
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Topic(self):
        r"""数据来源topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Event = params.get("Event")
        self._LogType = params.get("LogType")
        self._Timestamp = params.get("Timestamp")
        self._Result = params.get("Result")
        self._Data = params.get("Data")
        self._Topic = params.get("Topic")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceRequest(AbstractModel):
    r"""DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    r"""DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    r"""DeleteProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    r"""DeleteProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    r"""DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    r"""DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    r"""DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: TopicId
        :type TopicId: str
        :param _ProductId: 产品Id
        :type ProductId: str
        """
        self._TopicId = None
        self._ProductId = None

    @property
    def TopicId(self):
        r"""TopicId
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    r"""DeleteTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Device(AbstractModel):
    r"""设备

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceSecret: 设备密钥
        :type DeviceSecret: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _DeviceInfo: 设备信息（json）
        :type DeviceInfo: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._DeviceSecret = None
        self._UpdateTime = None
        self._CreateTime = None
        self._DeviceInfo = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceSecret(self):
        r"""设备密钥
        :rtype: str
        """
        return self._DeviceSecret

    @DeviceSecret.setter
    def DeviceSecret(self, DeviceSecret):
        self._DeviceSecret = DeviceSecret

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeviceInfo(self):
        r"""设备信息（json）
        :rtype: str
        """
        return self._DeviceInfo

    @DeviceInfo.setter
    def DeviceInfo(self, DeviceInfo):
        self._DeviceInfo = DeviceInfo


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceSecret = params.get("DeviceSecret")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._DeviceInfo = params.get("DeviceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceEntry(AbstractModel):
    r"""设备条目

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceSecret: 设备密钥
        :type DeviceSecret: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._DeviceSecret = None
        self._CreateTime = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceSecret(self):
        r"""设备密钥
        :rtype: str
        """
        return self._DeviceSecret

    @DeviceSecret.setter
    def DeviceSecret(self, DeviceSecret):
        self._DeviceSecret = DeviceSecret

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceSecret = params.get("DeviceSecret")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceLogEntry(AbstractModel):
    r"""设备日志条目

    """

    def __init__(self):
        r"""
        :param _Id: 日志id
        :type Id: str
        :param _Msg: 日志内容
        :type Msg: str
        :param _Code: 状态码
        :type Code: str
        :param _Timestamp: 时间戳
        :type Timestamp: int
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Method: 设备动作
        :type Method: str
        """
        self._Id = None
        self._Msg = None
        self._Code = None
        self._Timestamp = None
        self._DeviceName = None
        self._Method = None

    @property
    def Id(self):
        r"""日志id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Msg(self):
        r"""日志内容
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        r"""状态码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Timestamp(self):
        r"""时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Method(self):
        r"""设备动作
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        self._Timestamp = params.get("Timestamp")
        self._DeviceName = params.get("DeviceName")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceSignature(AbstractModel):
    r"""设备签名

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceSignature: 设备签名
        :type DeviceSignature: str
        """
        self._DeviceName = None
        self._DeviceSignature = None

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceSignature(self):
        r"""设备签名
        :rtype: str
        """
        return self._DeviceSignature

    @DeviceSignature.setter
    def DeviceSignature(self, DeviceSignature):
        self._DeviceSignature = DeviceSignature


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._DeviceSignature = params.get("DeviceSignature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatData(AbstractModel):
    r"""设备统计数据

    """

    def __init__(self):
        r"""
        :param _Datetime: 时间点
        :type Datetime: str
        :param _DeviceOnline: 在线设备数
        :type DeviceOnline: int
        :param _DeviceActive: 激活设备数
        :type DeviceActive: int
        :param _DeviceTotal: 设备总数
        :type DeviceTotal: int
        """
        self._Datetime = None
        self._DeviceOnline = None
        self._DeviceActive = None
        self._DeviceTotal = None

    @property
    def Datetime(self):
        r"""时间点
        :rtype: str
        """
        return self._Datetime

    @Datetime.setter
    def Datetime(self, Datetime):
        self._Datetime = Datetime

    @property
    def DeviceOnline(self):
        r"""在线设备数
        :rtype: int
        """
        return self._DeviceOnline

    @DeviceOnline.setter
    def DeviceOnline(self, DeviceOnline):
        self._DeviceOnline = DeviceOnline

    @property
    def DeviceActive(self):
        r"""激活设备数
        :rtype: int
        """
        return self._DeviceActive

    @DeviceActive.setter
    def DeviceActive(self, DeviceActive):
        self._DeviceActive = DeviceActive

    @property
    def DeviceTotal(self):
        r"""设备总数
        :rtype: int
        """
        return self._DeviceTotal

    @DeviceTotal.setter
    def DeviceTotal(self, DeviceTotal):
        self._DeviceTotal = DeviceTotal


    def _deserialize(self, params):
        self._Datetime = params.get("Datetime")
        self._DeviceOnline = params.get("DeviceOnline")
        self._DeviceActive = params.get("DeviceActive")
        self._DeviceTotal = params.get("DeviceTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatus(AbstractModel):
    r"""设备状态

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Status: 设备状态（inactive, online, offline）
        :type Status: str
        :param _FirstOnline: 首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstOnline: str
        :param _LastOnline: 最后上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnline: str
        :param _OnlineTimes: 上线次数
        :type OnlineTimes: int
        """
        self._DeviceName = None
        self._Status = None
        self._FirstOnline = None
        self._LastOnline = None
        self._OnlineTimes = None

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Status(self):
        r"""设备状态（inactive, online, offline）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FirstOnline(self):
        r"""首次上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FirstOnline

    @FirstOnline.setter
    def FirstOnline(self, FirstOnline):
        self._FirstOnline = FirstOnline

    @property
    def LastOnline(self):
        r"""最后上线时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastOnline

    @LastOnline.setter
    def LastOnline(self, LastOnline):
        self._LastOnline = LastOnline

    @property
    def OnlineTimes(self):
        r"""上线次数
        :rtype: int
        """
        return self._OnlineTimes

    @OnlineTimes.setter
    def OnlineTimes(self, OnlineTimes):
        self._OnlineTimes = OnlineTimes


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Status = params.get("Status")
        self._FirstOnline = params.get("FirstOnline")
        self._LastOnline = params.get("LastOnline")
        self._OnlineTimes = params.get("OnlineTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnumData(AbstractModel):
    r"""枚举类型数据

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Desc: 描述
        :type Desc: str
        :param _Mode: 读写模式
        :type Mode: str
        :param _Range: 取值列表
        :type Range: list of str
        """
        self._Name = None
        self._Desc = None
        self._Mode = None
        self._Range = None

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Mode(self):
        r"""读写模式
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Range(self):
        r"""取值列表
        :rtype: list of str
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Mode = params.get("Mode")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDataHistoryRequest(AbstractModel):
    r"""GetDataHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceNames: 设备名称列表，允许最多一次100台
        :type DeviceNames: list of str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _Size: 查询数据量
        :type Size: int
        :param _Order: 时间排序（desc/asc）
        :type Order: str
        :param _ScrollId: 查询游标
        :type ScrollId: str
        """
        self._ProductId = None
        self._DeviceNames = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Order = None
        self._ScrollId = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        r"""设备名称列表，允许最多一次100台
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def StartTime(self):
        r"""查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        r"""查询数据量
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Order(self):
        r"""时间排序（desc/asc）
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def ScrollId(self):
        r"""查询游标
        :rtype: str
        """
        return self._ScrollId

    @ScrollId.setter
    def ScrollId(self, ScrollId):
        self._ScrollId = ScrollId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Order = params.get("Order")
        self._ScrollId = params.get("ScrollId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDataHistoryResponse(AbstractModel):
    r"""GetDataHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataHistory: 数据历史
        :type DataHistory: list of DataHistoryEntry
        :param _ScrollId: 查询游标
        :type ScrollId: str
        :param _ScrollTimeout: 查询游标超时
        :type ScrollTimeout: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataHistory = None
        self._ScrollId = None
        self._ScrollTimeout = None
        self._RequestId = None

    @property
    def DataHistory(self):
        r"""数据历史
        :rtype: list of DataHistoryEntry
        """
        return self._DataHistory

    @DataHistory.setter
    def DataHistory(self, DataHistory):
        self._DataHistory = DataHistory

    @property
    def ScrollId(self):
        r"""查询游标
        :rtype: str
        """
        return self._ScrollId

    @ScrollId.setter
    def ScrollId(self, ScrollId):
        self._ScrollId = ScrollId

    @property
    def ScrollTimeout(self):
        r"""查询游标超时
        :rtype: int
        """
        return self._ScrollTimeout

    @ScrollTimeout.setter
    def ScrollTimeout(self, ScrollTimeout):
        self._ScrollTimeout = ScrollTimeout

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataHistory") is not None:
            self._DataHistory = []
            for item in params.get("DataHistory"):
                obj = DataHistoryEntry()
                obj._deserialize(item)
                self._DataHistory.append(obj)
        self._ScrollId = params.get("ScrollId")
        self._ScrollTimeout = params.get("ScrollTimeout")
        self._RequestId = params.get("RequestId")


class GetDebugLogRequest(AbstractModel):
    r"""GetDebugLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceNames: 设备名称列表，最大支持100台
        :type DeviceNames: list of str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _Size: 查询数据量
        :type Size: int
        :param _Order: 时间排序（desc/asc）
        :type Order: str
        :param _ScrollId: 查询游标
        :type ScrollId: str
        :param _Type: 日志类型（shadow/action/mqtt）
        :type Type: str
        """
        self._ProductId = None
        self._DeviceNames = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Order = None
        self._ScrollId = None
        self._Type = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        r"""设备名称列表，最大支持100台
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def StartTime(self):
        r"""查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        r"""查询数据量
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Order(self):
        r"""时间排序（desc/asc）
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def ScrollId(self):
        r"""查询游标
        :rtype: str
        """
        return self._ScrollId

    @ScrollId.setter
    def ScrollId(self, ScrollId):
        self._ScrollId = ScrollId

    @property
    def Type(self):
        r"""日志类型（shadow/action/mqtt）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Order = params.get("Order")
        self._ScrollId = params.get("ScrollId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDebugLogResponse(AbstractModel):
    r"""GetDebugLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DebugLog: 调试日志
        :type DebugLog: list of DebugLogEntry
        :param _ScrollId: 查询游标
        :type ScrollId: str
        :param _ScrollTimeout: 游标超时
        :type ScrollTimeout: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DebugLog = None
        self._ScrollId = None
        self._ScrollTimeout = None
        self._RequestId = None

    @property
    def DebugLog(self):
        r"""调试日志
        :rtype: list of DebugLogEntry
        """
        return self._DebugLog

    @DebugLog.setter
    def DebugLog(self, DebugLog):
        self._DebugLog = DebugLog

    @property
    def ScrollId(self):
        r"""查询游标
        :rtype: str
        """
        return self._ScrollId

    @ScrollId.setter
    def ScrollId(self, ScrollId):
        self._ScrollId = ScrollId

    @property
    def ScrollTimeout(self):
        r"""游标超时
        :rtype: int
        """
        return self._ScrollTimeout

    @ScrollTimeout.setter
    def ScrollTimeout(self, ScrollTimeout):
        self._ScrollTimeout = ScrollTimeout

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DebugLog") is not None:
            self._DebugLog = []
            for item in params.get("DebugLog"):
                obj = DebugLogEntry()
                obj._deserialize(item)
                self._DebugLog.append(obj)
        self._ScrollId = params.get("ScrollId")
        self._ScrollTimeout = params.get("ScrollTimeout")
        self._RequestId = params.get("RequestId")


class GetDeviceDataRequest(AbstractModel):
    r"""GetDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceDataResponse(AbstractModel):
    r"""GetDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceData: 设备数据
        :type DeviceData: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceData = None
        self._RequestId = None

    @property
    def DeviceData(self):
        r"""设备数据
        :rtype: str
        """
        return self._DeviceData

    @DeviceData.setter
    def DeviceData(self, DeviceData):
        self._DeviceData = DeviceData

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceData = params.get("DeviceData")
        self._RequestId = params.get("RequestId")


class GetDeviceLogRequest(AbstractModel):
    r"""GetDeviceLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceNames: 设备名称列表，最大支持100台
        :type DeviceNames: list of str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        :param _Size: 查询数据量
        :type Size: int
        :param _Order: 时间排序（desc/asc）
        :type Order: str
        :param _ScrollId: 查询游标
        :type ScrollId: str
        :param _Type: 日志类型（comm/status）
        :type Type: str
        """
        self._ProductId = None
        self._DeviceNames = None
        self._StartTime = None
        self._EndTime = None
        self._Size = None
        self._Order = None
        self._ScrollId = None
        self._Type = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        r"""设备名称列表，最大支持100台
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def StartTime(self):
        r"""查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Size(self):
        r"""查询数据量
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Order(self):
        r"""时间排序（desc/asc）
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def ScrollId(self):
        r"""查询游标
        :rtype: str
        """
        return self._ScrollId

    @ScrollId.setter
    def ScrollId(self, ScrollId):
        self._ScrollId = ScrollId

    @property
    def Type(self):
        r"""日志类型（comm/status）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Size = params.get("Size")
        self._Order = params.get("Order")
        self._ScrollId = params.get("ScrollId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLogResponse(AbstractModel):
    r"""GetDeviceLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceLog: 设备日志
        :type DeviceLog: list of DeviceLogEntry
        :param _ScrollId: 查询游标
        :type ScrollId: str
        :param _ScrollTimeout: 游标超时
        :type ScrollTimeout: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceLog = None
        self._ScrollId = None
        self._ScrollTimeout = None
        self._RequestId = None

    @property
    def DeviceLog(self):
        r"""设备日志
        :rtype: list of DeviceLogEntry
        """
        return self._DeviceLog

    @DeviceLog.setter
    def DeviceLog(self, DeviceLog):
        self._DeviceLog = DeviceLog

    @property
    def ScrollId(self):
        r"""查询游标
        :rtype: str
        """
        return self._ScrollId

    @ScrollId.setter
    def ScrollId(self, ScrollId):
        self._ScrollId = ScrollId

    @property
    def ScrollTimeout(self):
        r"""游标超时
        :rtype: int
        """
        return self._ScrollTimeout

    @ScrollTimeout.setter
    def ScrollTimeout(self, ScrollTimeout):
        self._ScrollTimeout = ScrollTimeout

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceLog") is not None:
            self._DeviceLog = []
            for item in params.get("DeviceLog"):
                obj = DeviceLogEntry()
                obj._deserialize(item)
                self._DeviceLog.append(obj)
        self._ScrollId = params.get("ScrollId")
        self._ScrollTimeout = params.get("ScrollTimeout")
        self._RequestId = params.get("RequestId")


class GetDeviceRequest(AbstractModel):
    r"""GetDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceResponse(AbstractModel):
    r"""GetDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Device: 设备信息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Device = None
        self._RequestId = None

    @property
    def Device(self):
        r"""设备信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        self._RequestId = params.get("RequestId")


class GetDeviceSignaturesRequest(AbstractModel):
    r"""GetDeviceSignatures请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceNames: 设备名称列表（单次限制1000个设备）
        :type DeviceNames: list of str
        :param _Expire: 过期时间
        :type Expire: int
        """
        self._ProductId = None
        self._DeviceNames = None
        self._Expire = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        r"""设备名称列表（单次限制1000个设备）
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames

    @property
    def Expire(self):
        r"""过期时间
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        self._Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceSignaturesResponse(AbstractModel):
    r"""GetDeviceSignatures返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceSignatures: 设备绑定签名列表
        :type DeviceSignatures: list of DeviceSignature
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceSignatures = None
        self._RequestId = None

    @property
    def DeviceSignatures(self):
        r"""设备绑定签名列表
        :rtype: list of DeviceSignature
        """
        return self._DeviceSignatures

    @DeviceSignatures.setter
    def DeviceSignatures(self, DeviceSignatures):
        self._DeviceSignatures = DeviceSignatures

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceSignatures") is not None:
            self._DeviceSignatures = []
            for item in params.get("DeviceSignatures"):
                obj = DeviceSignature()
                obj._deserialize(item)
                self._DeviceSignatures.append(obj)
        self._RequestId = params.get("RequestId")


class GetDeviceStatisticsRequest(AbstractModel):
    r"""GetDeviceStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 产品Id列表
        :type Products: list of str
        :param _StartDate: 开始日期
        :type StartDate: str
        :param _EndDate: 结束日期
        :type EndDate: str
        """
        self._Products = None
        self._StartDate = None
        self._EndDate = None

    @property
    def Products(self):
        r"""产品Id列表
        :rtype: list of str
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def StartDate(self):
        r"""开始日期
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        r"""结束日期
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._Products = params.get("Products")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceStatisticsResponse(AbstractModel):
    r"""GetDeviceStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceStatistics: 统计数据
        :type DeviceStatistics: list of DeviceStatData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceStatistics = None
        self._RequestId = None

    @property
    def DeviceStatistics(self):
        r"""统计数据
        :rtype: list of DeviceStatData
        """
        return self._DeviceStatistics

    @DeviceStatistics.setter
    def DeviceStatistics(self, DeviceStatistics):
        self._DeviceStatistics = DeviceStatistics

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceStatistics") is not None:
            self._DeviceStatistics = []
            for item in params.get("DeviceStatistics"):
                obj = DeviceStatData()
                obj._deserialize(item)
                self._DeviceStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class GetDeviceStatusesRequest(AbstractModel):
    r"""GetDeviceStatuses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceNames: 设备名称列表（单次限制1000个设备）
        :type DeviceNames: list of str
        """
        self._ProductId = None
        self._DeviceNames = None

    @property
    def ProductId(self):
        r"""产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceNames(self):
        r"""设备名称列表（单次限制1000个设备）
        :rtype: list of str
        """
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceStatusesResponse(AbstractModel):
    r"""GetDeviceStatuses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceStatuses: 设备状态列表
        :type DeviceStatuses: list of DeviceStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceStatuses = None
        self._RequestId = None

    @property
    def DeviceStatuses(self):
        r"""设备状态列表
        :rtype: list of DeviceStatus
        """
        return self._DeviceStatuses

    @DeviceStatuses.setter
    def DeviceStatuses(self, DeviceStatuses):
        self._DeviceStatuses = DeviceStatuses

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceStatuses") is not None:
            self._DeviceStatuses = []
            for item in params.get("DeviceStatuses"):
                obj = DeviceStatus()
                obj._deserialize(item)
                self._DeviceStatuses.append(obj)
        self._RequestId = params.get("RequestId")


class GetDevicesRequest(AbstractModel):
    r"""GetDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _Offset: 偏移
        :type Offset: int
        :param _Length: 长度
        :type Length: int
        :param _Keyword: 关键字查询
        :type Keyword: str
        """
        self._ProductId = None
        self._Offset = None
        self._Length = None
        self._Keyword = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        r"""偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Length(self):
        r"""长度
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Keyword(self):
        r"""关键字查询
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Length = params.get("Length")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicesResponse(AbstractModel):
    r"""GetDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 设备列表
        :type Devices: list of DeviceEntry
        :param _Total: 设备总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._Total = None
        self._RequestId = None

    @property
    def Devices(self):
        r"""设备列表
        :rtype: list of DeviceEntry
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def Total(self):
        r"""设备总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceEntry()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetProductRequest(AbstractModel):
    r"""GetProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProductResponse(AbstractModel):
    r"""GetProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Product = None
        self._RequestId = None

    @property
    def Product(self):
        r"""产品信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Product`
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self._Product = Product()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class GetProductsRequest(AbstractModel):
    r"""GetProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移
        :type Offset: int
        :param _Length: 长度
        :type Length: int
        """
        self._Offset = None
        self._Length = None

    @property
    def Offset(self):
        r"""偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Length(self):
        r"""长度
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProductsResponse(AbstractModel):
    r"""GetProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: Product列表
        :type Products: list of ProductEntry
        :param _Total: Product总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._Total = None
        self._RequestId = None

    @property
    def Products(self):
        r"""Product列表
        :rtype: list of ProductEntry
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def Total(self):
        r"""Product总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self._Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self._Products.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetRuleRequest(AbstractModel):
    r"""GetRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuleResponse(AbstractModel):
    r"""GetRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._RequestId = None

    @property
    def Rule(self):
        r"""规则
        :rtype: :class:`tencentcloud.iot.v20180123.models.Rule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = Rule()
            self._Rule._deserialize(params.get("Rule"))
        self._RequestId = params.get("RequestId")


class GetRulesRequest(AbstractModel):
    r"""GetRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移
        :type Offset: int
        :param _Length: 长度
        :type Length: int
        """
        self._Offset = None
        self._Length = None

    @property
    def Offset(self):
        r"""偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Length(self):
        r"""长度
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRulesResponse(AbstractModel):
    r"""GetRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
        :type Rules: list of Rule
        :param _Total: 规则总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._Total = None
        self._RequestId = None

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of Rule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Total(self):
        r"""规则总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetTopicRequest(AbstractModel):
    r"""GetTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: TopicId
        :type TopicId: str
        :param _ProductId: 产品Id
        :type ProductId: str
        """
        self._TopicId = None
        self._ProductId = None

    @property
    def TopicId(self):
        r"""TopicId
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTopicResponse(AbstractModel):
    r"""GetTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: Topic信息
        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topic = None
        self._RequestId = None

    @property
    def Topic(self):
        r"""Topic信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Topic`
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self._Topic = Topic()
            self._Topic._deserialize(params.get("Topic"))
        self._RequestId = params.get("RequestId")


class GetTopicsRequest(AbstractModel):
    r"""GetTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _Offset: 偏移
        :type Offset: int
        :param _Length: 长度
        :type Length: int
        """
        self._ProductId = None
        self._Offset = None
        self._Length = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Offset(self):
        r"""偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Length(self):
        r"""长度
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTopicsResponse(AbstractModel):
    r"""GetTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Topics: Topic列表
        :type Topics: list of Topic
        :param _Total: Topic总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Topics = None
        self._Total = None
        self._RequestId = None

    @property
    def Topics(self):
        r"""Topic列表
        :rtype: list of Topic
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def Total(self):
        r"""Topic总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = Topic()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class IssueDeviceControlRequest(AbstractModel):
    r"""IssueDeviceControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ControlData: 控制数据（json）
        :type ControlData: str
        :param _Metadata: 是否发送metadata字段
        :type Metadata: bool
        """
        self._ProductId = None
        self._DeviceName = None
        self._ControlData = None
        self._Metadata = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ControlData(self):
        r"""控制数据（json）
        :rtype: str
        """
        return self._ControlData

    @ControlData.setter
    def ControlData(self, ControlData):
        self._ControlData = ControlData

    @property
    def Metadata(self):
        r"""是否发送metadata字段
        :rtype: bool
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ControlData = params.get("ControlData")
        self._Metadata = params.get("Metadata")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IssueDeviceControlResponse(AbstractModel):
    r"""IssueDeviceControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NumberData(AbstractModel):
    r"""数字类型数据

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Desc: 描述
        :type Desc: str
        :param _Mode: 读写模式
        :type Mode: str
        :param _Range: 取值范围
        :type Range: list of float
        """
        self._Name = None
        self._Desc = None
        self._Mode = None
        self._Range = None

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Mode(self):
        r"""读写模式
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Range(self):
        r"""取值范围
        :rtype: list of float
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Mode = params.get("Mode")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Product(AbstractModel):
    r"""产品

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _ProductKey: 产品Key
        :type ProductKey: str
        :param _AppId: AppId
        :type AppId: int
        :param _Name: 产品名称
        :type Name: str
        :param _Description: 产品描述
        :type Description: str
        :param _Domain: 连接域名
        :type Domain: str
        :param _Standard: 产品规格
        :type Standard: int
        :param _AuthType: 鉴权类型（0：直连，1：Token）
        :type AuthType: int
        :param _Deleted: 删除（0未删除）
        :type Deleted: int
        :param _Message: 备注
        :type Message: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _DataTemplate: 数据模版
        :type DataTemplate: list of DataTemplate
        :param _DataProtocol: 数据协议（native/template）
        :type DataProtocol: str
        :param _Username: 直连用户名
        :type Username: str
        :param _Password: 直连密码
        :type Password: str
        :param _CommProtocol: 通信方式
        :type CommProtocol: str
        :param _Qps: qps
        :type Qps: int
        :param _Region: 地域
        :type Region: str
        :param _DeviceType: 产品的设备类型
        :type DeviceType: str
        :param _AssociatedProducts: 关联的产品列表
        :type AssociatedProducts: list of str
        """
        self._ProductId = None
        self._ProductKey = None
        self._AppId = None
        self._Name = None
        self._Description = None
        self._Domain = None
        self._Standard = None
        self._AuthType = None
        self._Deleted = None
        self._Message = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DataTemplate = None
        self._DataProtocol = None
        self._Username = None
        self._Password = None
        self._CommProtocol = None
        self._Qps = None
        self._Region = None
        self._DeviceType = None
        self._AssociatedProducts = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductKey(self):
        r"""产品Key
        :rtype: str
        """
        return self._ProductKey

    @ProductKey.setter
    def ProductKey(self, ProductKey):
        self._ProductKey = ProductKey

    @property
    def AppId(self):
        r"""AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Name(self):
        r"""产品名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""产品描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Domain(self):
        r"""连接域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Standard(self):
        r"""产品规格
        :rtype: int
        """
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard

    @property
    def AuthType(self):
        r"""鉴权类型（0：直连，1：Token）
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def Deleted(self):
        r"""删除（0未删除）
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def Message(self):
        r"""备注
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DataTemplate(self):
        r"""数据模版
        :rtype: list of DataTemplate
        """
        return self._DataTemplate

    @DataTemplate.setter
    def DataTemplate(self, DataTemplate):
        self._DataTemplate = DataTemplate

    @property
    def DataProtocol(self):
        r"""数据协议（native/template）
        :rtype: str
        """
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def Username(self):
        r"""直连用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""直连密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CommProtocol(self):
        r"""通信方式
        :rtype: str
        """
        return self._CommProtocol

    @CommProtocol.setter
    def CommProtocol(self, CommProtocol):
        self._CommProtocol = CommProtocol

    @property
    def Qps(self):
        r"""qps
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DeviceType(self):
        r"""产品的设备类型
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def AssociatedProducts(self):
        r"""关联的产品列表
        :rtype: list of str
        """
        return self._AssociatedProducts

    @AssociatedProducts.setter
    def AssociatedProducts(self, AssociatedProducts):
        self._AssociatedProducts = AssociatedProducts


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductKey = params.get("ProductKey")
        self._AppId = params.get("AppId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Domain = params.get("Domain")
        self._Standard = params.get("Standard")
        self._AuthType = params.get("AuthType")
        self._Deleted = params.get("Deleted")
        self._Message = params.get("Message")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("DataTemplate") is not None:
            self._DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self._DataTemplate.append(obj)
        self._DataProtocol = params.get("DataProtocol")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._CommProtocol = params.get("CommProtocol")
        self._Qps = params.get("Qps")
        self._Region = params.get("Region")
        self._DeviceType = params.get("DeviceType")
        self._AssociatedProducts = params.get("AssociatedProducts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductEntry(AbstractModel):
    r"""产品条目

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _ProductKey: 产品Key
        :type ProductKey: str
        :param _AppId: AppId
        :type AppId: int
        :param _Name: 产品名称
        :type Name: str
        :param _Description: 产品描述
        :type Description: str
        :param _Domain: 连接域名
        :type Domain: str
        :param _AuthType: 鉴权类型（0：直连，1：Token）
        :type AuthType: int
        :param _DataProtocol: 数据协议（native/template）
        :type DataProtocol: str
        :param _Deleted: 删除（0未删除）
        :type Deleted: int
        :param _Message: 备注
        :type Message: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _CommProtocol: 通信方式
        :type CommProtocol: str
        :param _Region: 地域
        :type Region: str
        :param _DeviceType: 设备类型
        :type DeviceType: str
        """
        self._ProductId = None
        self._ProductKey = None
        self._AppId = None
        self._Name = None
        self._Description = None
        self._Domain = None
        self._AuthType = None
        self._DataProtocol = None
        self._Deleted = None
        self._Message = None
        self._CreateTime = None
        self._CommProtocol = None
        self._Region = None
        self._DeviceType = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductKey(self):
        r"""产品Key
        :rtype: str
        """
        return self._ProductKey

    @ProductKey.setter
    def ProductKey(self, ProductKey):
        self._ProductKey = ProductKey

    @property
    def AppId(self):
        r"""AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Name(self):
        r"""产品名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""产品描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Domain(self):
        r"""连接域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AuthType(self):
        r"""鉴权类型（0：直连，1：Token）
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def DataProtocol(self):
        r"""数据协议（native/template）
        :rtype: str
        """
        return self._DataProtocol

    @DataProtocol.setter
    def DataProtocol(self, DataProtocol):
        self._DataProtocol = DataProtocol

    @property
    def Deleted(self):
        r"""删除（0未删除）
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def Message(self):
        r"""备注
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CommProtocol(self):
        r"""通信方式
        :rtype: str
        """
        return self._CommProtocol

    @CommProtocol.setter
    def CommProtocol(self, CommProtocol):
        self._CommProtocol = CommProtocol

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def DeviceType(self):
        r"""设备类型
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductKey = params.get("ProductKey")
        self._AppId = params.get("AppId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Domain = params.get("Domain")
        self._AuthType = params.get("AuthType")
        self._DataProtocol = params.get("DataProtocol")
        self._Deleted = params.get("Deleted")
        self._Message = params.get("Message")
        self._CreateTime = params.get("CreateTime")
        self._CommProtocol = params.get("CommProtocol")
        self._Region = params.get("Region")
        self._DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMsgRequest(AbstractModel):
    r"""PublishMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Topic: Topic
        :type Topic: str
        :param _Message: 消息内容
        :type Message: str
        :param _Qos: Qos(目前QoS支持0与1)
        :type Qos: int
        """
        self._Topic = None
        self._Message = None
        self._Qos = None

    @property
    def Topic(self):
        r"""Topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Message(self):
        r"""消息内容
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Qos(self):
        r"""Qos(目前QoS支持0与1)
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Message = params.get("Message")
        self._Qos = params.get("Qos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMsgResponse(AbstractModel):
    r"""PublishMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResetDeviceRequest(AbstractModel):
    r"""ResetDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetDeviceResponse(AbstractModel):
    r"""ResetDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Device: 设备信息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Device = None
        self._RequestId = None

    @property
    def Device(self):
        r"""设备信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Device`
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        self._RequestId = params.get("RequestId")


class Rule(AbstractModel):
    r"""规则

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: str
        :param _AppId: AppId
        :type AppId: int
        :param _Name: 名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _Query: 查询
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param _Actions: 转发
        :type Actions: list of Action
        :param _Active: 已启动
        :type Active: int
        :param _Deleted: 已删除
        :type Deleted: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _MsgOrder: 消息顺序
        :type MsgOrder: int
        :param _DataType: 数据类型（0：文本，1：二进制）
        :type DataType: int
        """
        self._RuleId = None
        self._AppId = None
        self._Name = None
        self._Description = None
        self._Query = None
        self._Actions = None
        self._Active = None
        self._Deleted = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MsgOrder = None
        self._DataType = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AppId(self):
        r"""AppId
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Query(self):
        r"""查询
        :rtype: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Actions(self):
        r"""转发
        :rtype: list of Action
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Active(self):
        r"""已启动
        :rtype: int
        """
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active

    @property
    def Deleted(self):
        r"""已删除
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MsgOrder(self):
        r"""消息顺序
        :rtype: int
        """
        return self._MsgOrder

    @MsgOrder.setter
    def MsgOrder(self, MsgOrder):
        self._MsgOrder = MsgOrder

    @property
    def DataType(self):
        r"""数据类型（0：文本，1：二进制）
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AppId = params.get("AppId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Query") is not None:
            self._Query = RuleQuery()
            self._Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self._Actions.append(obj)
        self._Active = params.get("Active")
        self._Deleted = params.get("Deleted")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._MsgOrder = params.get("MsgOrder")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleQuery(AbstractModel):
    r"""查询

    """

    def __init__(self):
        r"""
        :param _Field: 字段
        :type Field: str
        :param _Condition: 过滤规则
        :type Condition: str
        :param _Topic: Topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Topic: str
        :param _ProductId: 产品Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        """
        self._Field = None
        self._Condition = None
        self._Topic = None
        self._ProductId = None

    @property
    def Field(self):
        r"""字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Condition(self):
        r"""过滤规则
        :rtype: str
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def Topic(self):
        r"""Topic
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def ProductId(self):
        r"""产品Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Condition = params.get("Condition")
        self._Topic = params.get("Topic")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceAction(AbstractModel):
    r"""转发到第三方http(s)服务

    """

    def __init__(self):
        r"""
        :param _Url: 服务url地址
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""服务url地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StringData(AbstractModel):
    r"""数字类型数据

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Desc: 描述
        :type Desc: str
        :param _Mode: 读写模式
        :type Mode: str
        :param _Range: 长度范围
        :type Range: list of int non-negative
        """
        self._Name = None
        self._Desc = None
        self._Mode = None
        self._Range = None

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Mode(self):
        r"""读写模式
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Range(self):
        r"""长度范围
        :rtype: list of int non-negative
        """
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Mode = params.get("Mode")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Topic(AbstractModel):
    r"""Topic

    """

    def __init__(self):
        r"""
        :param _TopicId: TopicId
        :type TopicId: str
        :param _TopicName: Topic名称
        :type TopicName: str
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _MsgLife: 消息最大生命周期
        :type MsgLife: int
        :param _MsgSize: 消息最大大小
        :type MsgSize: int
        :param _MsgCount: 消息最大数量
        :type MsgCount: int
        :param _Deleted: 已删除
        :type Deleted: int
        :param _Path: Topic完整路径
        :type Path: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._TopicId = None
        self._TopicName = None
        self._ProductId = None
        self._MsgLife = None
        self._MsgSize = None
        self._MsgCount = None
        self._Deleted = None
        self._Path = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TopicId(self):
        r"""TopicId
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        r"""Topic名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def MsgLife(self):
        r"""消息最大生命周期
        :rtype: int
        """
        return self._MsgLife

    @MsgLife.setter
    def MsgLife(self, MsgLife):
        self._MsgLife = MsgLife

    @property
    def MsgSize(self):
        r"""消息最大大小
        :rtype: int
        """
        return self._MsgSize

    @MsgSize.setter
    def MsgSize(self, MsgSize):
        self._MsgSize = MsgSize

    @property
    def MsgCount(self):
        r"""消息最大数量
        :rtype: int
        """
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def Deleted(self):
        r"""已删除
        :rtype: int
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def Path(self):
        r"""Topic完整路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._ProductId = params.get("ProductId")
        self._MsgLife = params.get("MsgLife")
        self._MsgSize = params.get("MsgSize")
        self._MsgCount = params.get("MsgCount")
        self._Deleted = params.get("Deleted")
        self._Path = params.get("Path")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicAction(AbstractModel):
    r"""转发到topic动作

    """

    def __init__(self):
        r"""
        :param _Topic: 目标topic
        :type Topic: str
        """
        self._Topic = None

    @property
    def Topic(self):
        r"""目标topic
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassociateSubDeviceFromGatewayProductRequest(AbstractModel):
    r"""UnassociateSubDeviceFromGatewayProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubDeviceProductId: 子设备产品Id
        :type SubDeviceProductId: str
        :param _GatewayProductId: 网关设备产品Id
        :type GatewayProductId: str
        """
        self._SubDeviceProductId = None
        self._GatewayProductId = None

    @property
    def SubDeviceProductId(self):
        r"""子设备产品Id
        :rtype: str
        """
        return self._SubDeviceProductId

    @SubDeviceProductId.setter
    def SubDeviceProductId(self, SubDeviceProductId):
        self._SubDeviceProductId = SubDeviceProductId

    @property
    def GatewayProductId(self):
        r"""网关设备产品Id
        :rtype: str
        """
        return self._GatewayProductId

    @GatewayProductId.setter
    def GatewayProductId(self, GatewayProductId):
        self._GatewayProductId = GatewayProductId


    def _deserialize(self, params):
        self._SubDeviceProductId = params.get("SubDeviceProductId")
        self._GatewayProductId = params.get("GatewayProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassociateSubDeviceFromGatewayProductResponse(AbstractModel):
    r"""UnassociateSubDeviceFromGatewayProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateProductRequest(AbstractModel):
    r"""UpdateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _Name: 产品名称
        :type Name: str
        :param _Description: 产品描述
        :type Description: str
        :param _DataTemplate: 数据模版
        :type DataTemplate: list of DataTemplate
        """
        self._ProductId = None
        self._Name = None
        self._Description = None
        self._DataTemplate = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Name(self):
        r"""产品名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""产品描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DataTemplate(self):
        r"""数据模版
        :rtype: list of DataTemplate
        """
        return self._DataTemplate

    @DataTemplate.setter
    def DataTemplate(self, DataTemplate):
        self._DataTemplate = DataTemplate


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("DataTemplate") is not None:
            self._DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self._DataTemplate.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProductResponse(AbstractModel):
    r"""UpdateProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 更新后的产品信息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Product = None
        self._RequestId = None

    @property
    def Product(self):
        r"""更新后的产品信息
        :rtype: :class:`tencentcloud.iot.v20180123.models.Product`
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self._Product = Product()
            self._Product._deserialize(params.get("Product"))
        self._RequestId = params.get("RequestId")


class UpdateRuleRequest(AbstractModel):
    r"""UpdateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: str
        :param _Name: 名称
        :type Name: str
        :param _Description: 描述
        :type Description: str
        :param _Query: 查询
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param _Actions: 转发动作列表
        :type Actions: list of Action
        :param _DataType: 数据类型（0：文本，1：二进制）
        :type DataType: int
        """
        self._RuleId = None
        self._Name = None
        self._Description = None
        self._Query = None
        self._Actions = None
        self._DataType = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Query(self):
        r"""查询
        :rtype: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Actions(self):
        r"""转发动作列表
        :rtype: list of Action
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def DataType(self):
        r"""数据类型（0：文本，1：二进制）
        :rtype: int
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Query") is not None:
            self._Query = RuleQuery()
            self._Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self._Actions.append(obj)
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuleResponse(AbstractModel):
    r"""UpdateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._RequestId = None

    @property
    def Rule(self):
        r"""规则
        :rtype: :class:`tencentcloud.iot.v20180123.models.Rule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = Rule()
            self._Rule._deserialize(params.get("Rule"))
        self._RequestId = params.get("RequestId")