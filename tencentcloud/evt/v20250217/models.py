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


class CreateRoleUserRequest(AbstractModel):
    r"""CreateRoleUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleSystemId: 角色体系ID
        :type RoleSystemId: int
        :param _UserId: 人员ID
        :type UserId: str
        :param _Username: 人员名称
        :type Username: str
        :param _Enabled: 是否启用
        :type Enabled: int
        :param _Phone: 手机号
        :type Phone: str
        :param _Attributes: 属性列表
        :type Attributes: list of UserAttribute
        """
        self._RoleSystemId = None
        self._UserId = None
        self._Username = None
        self._Enabled = None
        self._Phone = None
        self._Attributes = None

    @property
    def RoleSystemId(self):
        r"""角色体系ID
        :rtype: int
        """
        return self._RoleSystemId

    @RoleSystemId.setter
    def RoleSystemId(self, RoleSystemId):
        self._RoleSystemId = RoleSystemId

    @property
    def UserId(self):
        r"""人员ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Username(self):
        r"""人员名称
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Enabled(self):
        r"""是否启用
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Phone(self):
        r"""手机号
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Attributes(self):
        r"""属性列表
        :rtype: list of UserAttribute
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes


    def _deserialize(self, params):
        self._RoleSystemId = params.get("RoleSystemId")
        self._UserId = params.get("UserId")
        self._Username = params.get("Username")
        self._Enabled = params.get("Enabled")
        self._Phone = params.get("Phone")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = UserAttribute()
                obj._deserialize(item)
                self._Attributes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleUserResponse(AbstractModel):
    r"""CreateRoleUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 人员ID
        :type UserId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        r"""人员ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class UserAttribute(AbstractModel):
    r"""人员属性

    """

    def __init__(self):
        r"""
        :param _Key: 属性键名
        :type Key: str
        :param _Value: 属性值
        :type Value: list of int
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""属性键名
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""属性值
        :rtype: list of int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        