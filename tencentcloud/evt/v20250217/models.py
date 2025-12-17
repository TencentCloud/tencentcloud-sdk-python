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


class CompleteApprovalRequest(AbstractModel):
    r"""CompleteApproval请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApprovalId: <p>审批单号</p>
        :type ApprovalId: str
        :param _NodeId: <p>审批节点</p>
        :type NodeId: str
        :param _Result: <p>审批结果，1通过2拒绝</p>
        :type Result: int
        :param _Opinion: <p>审批意见</p>
        :type Opinion: str
        :param _UserToken: <p>审批人的身份认证Token，通过自定义角色体系回调接口分发</p><p>token信息</p>
        :type UserToken: str
        """
        self._ApprovalId = None
        self._NodeId = None
        self._Result = None
        self._Opinion = None
        self._UserToken = None

    @property
    def ApprovalId(self):
        r"""<p>审批单号</p>
        :rtype: str
        """
        return self._ApprovalId

    @ApprovalId.setter
    def ApprovalId(self, ApprovalId):
        self._ApprovalId = ApprovalId

    @property
    def NodeId(self):
        r"""<p>审批节点</p>
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Result(self):
        r"""<p>审批结果，1通过2拒绝</p>
        :rtype: int
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Opinion(self):
        r"""<p>审批意见</p>
        :rtype: str
        """
        return self._Opinion

    @Opinion.setter
    def Opinion(self, Opinion):
        self._Opinion = Opinion

    @property
    def UserToken(self):
        r"""<p>审批人的身份认证Token，通过自定义角色体系回调接口分发</p><p>token信息</p>
        :rtype: str
        """
        return self._UserToken

    @UserToken.setter
    def UserToken(self, UserToken):
        self._UserToken = UserToken


    def _deserialize(self, params):
        self._ApprovalId = params.get("ApprovalId")
        self._NodeId = params.get("NodeId")
        self._Result = params.get("Result")
        self._Opinion = params.get("Opinion")
        self._UserToken = params.get("UserToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteApprovalResponse(AbstractModel):
    r"""CompleteApproval返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateRoleUserRequest(AbstractModel):
    r"""CreateRoleUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleSystemId: <p>自定义角色体系的ID</p><p>角色体系ID</p>
        :type RoleSystemId: int
        :param _UserId: <p>要添加的自定义用户ID，建议与腾讯云-子用户的用户名称保持一致</p><p>人员ID</p>
        :type UserId: str
        :param _Username: <p>自定义用户的名称</p><p>人员名称</p>
        :type Username: str
        :param _Enabled: <p>是否启用当前用户</p>枚举值：<ul><li> 1： 启用</li><li> 2： 禁用</li></ul><p>是否启用</p>
        :type Enabled: int
        :param _Phone: <p>自定义用户的手机号</p><p>手机号</p>
        :type Phone: str
        :param _Attributes: <p>自定义用户的身份属性列表</p><p>属性列表</p>
        :type Attributes: list of UserAttribute
        :param _TencentUin: <p>自定义用户与腾讯云-子用户关联，如果不传默认按照子用户名称进行匹配</p>
        :type TencentUin: int
        """
        self._RoleSystemId = None
        self._UserId = None
        self._Username = None
        self._Enabled = None
        self._Phone = None
        self._Attributes = None
        self._TencentUin = None

    @property
    def RoleSystemId(self):
        r"""<p>自定义角色体系的ID</p><p>角色体系ID</p>
        :rtype: int
        """
        return self._RoleSystemId

    @RoleSystemId.setter
    def RoleSystemId(self, RoleSystemId):
        self._RoleSystemId = RoleSystemId

    @property
    def UserId(self):
        r"""<p>要添加的自定义用户ID，建议与腾讯云-子用户的用户名称保持一致</p><p>人员ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Username(self):
        r"""<p>自定义用户的名称</p><p>人员名称</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Enabled(self):
        r"""<p>是否启用当前用户</p>枚举值：<ul><li> 1： 启用</li><li> 2： 禁用</li></ul><p>是否启用</p>
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Phone(self):
        r"""<p>自定义用户的手机号</p><p>手机号</p>
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Attributes(self):
        r"""<p>自定义用户的身份属性列表</p><p>属性列表</p>
        :rtype: list of UserAttribute
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

    @property
    def TencentUin(self):
        r"""<p>自定义用户与腾讯云-子用户关联，如果不传默认按照子用户名称进行匹配</p>
        :rtype: int
        """
        return self._TencentUin

    @TencentUin.setter
    def TencentUin(self, TencentUin):
        self._TencentUin = TencentUin


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
        self._TencentUin = params.get("TencentUin")
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
        :param _UserId: <p>人员ID</p>
        :type UserId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._RequestId = None

    @property
    def UserId(self):
        r"""<p>人员ID</p>
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
        :param _Key: <p>自定义角色体系中用户属性的ID</p><p>属性键名</p>
        :type Key: str
        :param _Value: <p>自定义角色体系中的用户属性值，只支持传入对应用户属性支持的角色ID</p><p>属性值</p>
        :type Value: list of int
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>自定义角色体系中用户属性的ID</p><p>属性键名</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>自定义角色体系中的用户属性值，只支持传入对应用户属性支持的角色ID</p><p>属性值</p>
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
        