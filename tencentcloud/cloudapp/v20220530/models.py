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


class License(AbstractModel):
    """表示应用实例的软件授权，包含颁发信息、激活信息等内容。

    """

    def __init__(self):
        r"""
        :param _LicenseId: License ID
        :type LicenseId: str
        :param _LicenseMode: 软件授权模式。<table><thead><tr><th>枚举值</th><th>说明</th></tr></thead><tbody><tr><td>Permanent</td><td>永久授权。该授权不受有效期限制。</td></tr><tr><td>Subscription</td><td>订阅授权。授权如果过了有效期，则会进入过期状态。</td></tr><tr><td>Accept</td><td>验收期授权。用于需要验收的软件处于验收期间的授权，授权如果过了验收有效期，则会进入过期状态。</td></tr></tbody></table>
        :type LicenseMode: str
        :param _LicenseStatus: 软件的授权状态。<table><thead><tr><th>枚举值</th><th>说明</th></tr></thead><tbody><tr><td>Issued</td><td>已颁发，等待激活。一般来说，如果软件已经在运行，不会出现该状态。</td></tr><tr><td>Active</td><td>授权在有效期内，这是软件运行期间最常见的状态。</td></tr><tr><td>Expired</td><td>授权已过期。订阅类的软件授权有有效期，如果服务器时间已晚于有效期，则会进入过期状态。</td></tr><tr><td>Isolated</td><td>授权已隔离。有截止日期的授权，当用户授权到期时，先进入此状态，用户可以去续费，超过7天不续费则授权进入Destroyed状态。</td></tr><tr><td>Destroyed</td><td>授权已失效/销毁。用户如果退货软件，则授权会自动失效。</td></tr></tbody></table>
        :type LicenseStatus: str
        :param _ProviderId: 软件供应方 ID。
        :type ProviderId: int
        :param _SoftwarePackageId: 软件包 ID。
        :type SoftwarePackageId: str
        :param _SoftwarePackageVersion: 软件包版本。
        :type SoftwarePackageVersion: str
        :param _AuthorizedUserUin: 被授权的用户 UIN。
        :type AuthorizedUserUin: str
        :param _AuthorizedCloudappId: 被授权的应用实例 ID。
        :type AuthorizedCloudappId: str
        :param _AuthorizedCloudappRoleId: 被授权的角色 ID。
        :type AuthorizedCloudappRoleId: str
        :param _AuthorizedSpecification: 被授权的软件规格，具体字段请参考结构SaleParam
        :type AuthorizedSpecification: list of SaleParam
        :param _BillingMode: 被授权的软件的计费模式。<table><thead><tr><th>枚举值</th><th>说明</th></tr></thead><tbody><tr><td>1</td><td>线上计费，软件的授权从腾讯云线上购买，支持续费、退款等操作。</td></tr><tr><td>2</td><td>线下计费，软件的授权线下签订合同购买，定向客户交付，无法从线上续费和退款。</td></tr><tr><td>4</td><td>免费</td></tr></tbody></table>
        :type BillingMode: int
        :param _LifeSpan: 授权时长（单位由LifeSpanUnit确定，枚举值有Y年/M月/D日三种）
        :type LifeSpan: int
        :param _IssueDate: 授权颁发时间。
        :type IssueDate: str
        :param _ActivationDate: 授权激活时间，如从未激活则返回 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivationDate: str
        :param _ExpirationDate: 授权过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpirationDate: str
        :param _LifeSpanUnit: 授权时长单位，枚举值有Y年/M月/D日三种
        :type LifeSpanUnit: str
        :param _LicenseType: 授权的类型：Standard正式版/Development开发版/Trial体验版
        :type LicenseType: str
        :param _LicenseLevel: 授权的层级：Master 主授权；Child 子授权/增强型授权
        :type LicenseLevel: str
        """
        self._LicenseId = None
        self._LicenseMode = None
        self._LicenseStatus = None
        self._ProviderId = None
        self._SoftwarePackageId = None
        self._SoftwarePackageVersion = None
        self._AuthorizedUserUin = None
        self._AuthorizedCloudappId = None
        self._AuthorizedCloudappRoleId = None
        self._AuthorizedSpecification = None
        self._BillingMode = None
        self._LifeSpan = None
        self._IssueDate = None
        self._ActivationDate = None
        self._ExpirationDate = None
        self._LifeSpanUnit = None
        self._LicenseType = None
        self._LicenseLevel = None

    @property
    def LicenseId(self):
        """License ID
        :rtype: str
        """
        return self._LicenseId

    @LicenseId.setter
    def LicenseId(self, LicenseId):
        self._LicenseId = LicenseId

    @property
    def LicenseMode(self):
        """软件授权模式。<table><thead><tr><th>枚举值</th><th>说明</th></tr></thead><tbody><tr><td>Permanent</td><td>永久授权。该授权不受有效期限制。</td></tr><tr><td>Subscription</td><td>订阅授权。授权如果过了有效期，则会进入过期状态。</td></tr><tr><td>Accept</td><td>验收期授权。用于需要验收的软件处于验收期间的授权，授权如果过了验收有效期，则会进入过期状态。</td></tr></tbody></table>
        :rtype: str
        """
        return self._LicenseMode

    @LicenseMode.setter
    def LicenseMode(self, LicenseMode):
        self._LicenseMode = LicenseMode

    @property
    def LicenseStatus(self):
        """软件的授权状态。<table><thead><tr><th>枚举值</th><th>说明</th></tr></thead><tbody><tr><td>Issued</td><td>已颁发，等待激活。一般来说，如果软件已经在运行，不会出现该状态。</td></tr><tr><td>Active</td><td>授权在有效期内，这是软件运行期间最常见的状态。</td></tr><tr><td>Expired</td><td>授权已过期。订阅类的软件授权有有效期，如果服务器时间已晚于有效期，则会进入过期状态。</td></tr><tr><td>Isolated</td><td>授权已隔离。有截止日期的授权，当用户授权到期时，先进入此状态，用户可以去续费，超过7天不续费则授权进入Destroyed状态。</td></tr><tr><td>Destroyed</td><td>授权已失效/销毁。用户如果退货软件，则授权会自动失效。</td></tr></tbody></table>
        :rtype: str
        """
        return self._LicenseStatus

    @LicenseStatus.setter
    def LicenseStatus(self, LicenseStatus):
        self._LicenseStatus = LicenseStatus

    @property
    def ProviderId(self):
        """软件供应方 ID。
        :rtype: int
        """
        return self._ProviderId

    @ProviderId.setter
    def ProviderId(self, ProviderId):
        self._ProviderId = ProviderId

    @property
    def SoftwarePackageId(self):
        """软件包 ID。
        :rtype: str
        """
        return self._SoftwarePackageId

    @SoftwarePackageId.setter
    def SoftwarePackageId(self, SoftwarePackageId):
        self._SoftwarePackageId = SoftwarePackageId

    @property
    def SoftwarePackageVersion(self):
        """软件包版本。
        :rtype: str
        """
        return self._SoftwarePackageVersion

    @SoftwarePackageVersion.setter
    def SoftwarePackageVersion(self, SoftwarePackageVersion):
        self._SoftwarePackageVersion = SoftwarePackageVersion

    @property
    def AuthorizedUserUin(self):
        """被授权的用户 UIN。
        :rtype: str
        """
        return self._AuthorizedUserUin

    @AuthorizedUserUin.setter
    def AuthorizedUserUin(self, AuthorizedUserUin):
        self._AuthorizedUserUin = AuthorizedUserUin

    @property
    def AuthorizedCloudappId(self):
        """被授权的应用实例 ID。
        :rtype: str
        """
        return self._AuthorizedCloudappId

    @AuthorizedCloudappId.setter
    def AuthorizedCloudappId(self, AuthorizedCloudappId):
        self._AuthorizedCloudappId = AuthorizedCloudappId

    @property
    def AuthorizedCloudappRoleId(self):
        """被授权的角色 ID。
        :rtype: str
        """
        return self._AuthorizedCloudappRoleId

    @AuthorizedCloudappRoleId.setter
    def AuthorizedCloudappRoleId(self, AuthorizedCloudappRoleId):
        self._AuthorizedCloudappRoleId = AuthorizedCloudappRoleId

    @property
    def AuthorizedSpecification(self):
        """被授权的软件规格，具体字段请参考结构SaleParam
        :rtype: list of SaleParam
        """
        return self._AuthorizedSpecification

    @AuthorizedSpecification.setter
    def AuthorizedSpecification(self, AuthorizedSpecification):
        self._AuthorizedSpecification = AuthorizedSpecification

    @property
    def BillingMode(self):
        """被授权的软件的计费模式。<table><thead><tr><th>枚举值</th><th>说明</th></tr></thead><tbody><tr><td>1</td><td>线上计费，软件的授权从腾讯云线上购买，支持续费、退款等操作。</td></tr><tr><td>2</td><td>线下计费，软件的授权线下签订合同购买，定向客户交付，无法从线上续费和退款。</td></tr><tr><td>4</td><td>免费</td></tr></tbody></table>
        :rtype: int
        """
        return self._BillingMode

    @BillingMode.setter
    def BillingMode(self, BillingMode):
        self._BillingMode = BillingMode

    @property
    def LifeSpan(self):
        """授权时长（单位由LifeSpanUnit确定，枚举值有Y年/M月/D日三种）
        :rtype: int
        """
        return self._LifeSpan

    @LifeSpan.setter
    def LifeSpan(self, LifeSpan):
        self._LifeSpan = LifeSpan

    @property
    def IssueDate(self):
        """授权颁发时间。
        :rtype: str
        """
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, IssueDate):
        self._IssueDate = IssueDate

    @property
    def ActivationDate(self):
        """授权激活时间，如从未激活则返回 null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActivationDate

    @ActivationDate.setter
    def ActivationDate(self, ActivationDate):
        self._ActivationDate = ActivationDate

    @property
    def ExpirationDate(self):
        """授权过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, ExpirationDate):
        self._ExpirationDate = ExpirationDate

    @property
    def LifeSpanUnit(self):
        """授权时长单位，枚举值有Y年/M月/D日三种
        :rtype: str
        """
        return self._LifeSpanUnit

    @LifeSpanUnit.setter
    def LifeSpanUnit(self, LifeSpanUnit):
        self._LifeSpanUnit = LifeSpanUnit

    @property
    def LicenseType(self):
        """授权的类型：Standard正式版/Development开发版/Trial体验版
        :rtype: str
        """
        return self._LicenseType

    @LicenseType.setter
    def LicenseType(self, LicenseType):
        self._LicenseType = LicenseType

    @property
    def LicenseLevel(self):
        """授权的层级：Master 主授权；Child 子授权/增强型授权
        :rtype: str
        """
        return self._LicenseLevel

    @LicenseLevel.setter
    def LicenseLevel(self, LicenseLevel):
        self._LicenseLevel = LicenseLevel


    def _deserialize(self, params):
        self._LicenseId = params.get("LicenseId")
        self._LicenseMode = params.get("LicenseMode")
        self._LicenseStatus = params.get("LicenseStatus")
        self._ProviderId = params.get("ProviderId")
        self._SoftwarePackageId = params.get("SoftwarePackageId")
        self._SoftwarePackageVersion = params.get("SoftwarePackageVersion")
        self._AuthorizedUserUin = params.get("AuthorizedUserUin")
        self._AuthorizedCloudappId = params.get("AuthorizedCloudappId")
        self._AuthorizedCloudappRoleId = params.get("AuthorizedCloudappRoleId")
        if params.get("AuthorizedSpecification") is not None:
            self._AuthorizedSpecification = []
            for item in params.get("AuthorizedSpecification"):
                obj = SaleParam()
                obj._deserialize(item)
                self._AuthorizedSpecification.append(obj)
        self._BillingMode = params.get("BillingMode")
        self._LifeSpan = params.get("LifeSpan")
        self._IssueDate = params.get("IssueDate")
        self._ActivationDate = params.get("ActivationDate")
        self._ExpirationDate = params.get("ExpirationDate")
        self._LifeSpanUnit = params.get("LifeSpanUnit")
        self._LicenseType = params.get("LicenseType")
        self._LicenseLevel = params.get("LicenseLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleParam(AbstractModel):
    """表示商品 SKU 的单个售卖参数

    """

    def __init__(self):
        r"""
        :param _ParamKey: 售卖参数标识
        :type ParamKey: str
        :param _ParamKeyName: 售卖参数的展示名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamKeyName: str
        :param _ParamValue: 售卖参数值，当ParamType=Quant时，该值有可能为Null
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValue: str
        :param _ParamValueName: 售卖参数值的展示名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamValueName: str
        :param _ParamType: 售卖参数的类型，目前支持枚举类Enum/数量类Quant
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamType: str
        """
        self._ParamKey = None
        self._ParamKeyName = None
        self._ParamValue = None
        self._ParamValueName = None
        self._ParamType = None

    @property
    def ParamKey(self):
        """售卖参数标识
        :rtype: str
        """
        return self._ParamKey

    @ParamKey.setter
    def ParamKey(self, ParamKey):
        self._ParamKey = ParamKey

    @property
    def ParamKeyName(self):
        """售卖参数的展示名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamKeyName

    @ParamKeyName.setter
    def ParamKeyName(self, ParamKeyName):
        self._ParamKeyName = ParamKeyName

    @property
    def ParamValue(self):
        """售卖参数值，当ParamType=Quant时，该值有可能为Null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue

    @property
    def ParamValueName(self):
        """售卖参数值的展示名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamValueName

    @ParamValueName.setter
    def ParamValueName(self, ParamValueName):
        self._ParamValueName = ParamValueName

    @property
    def ParamType(self):
        """售卖参数的类型，目前支持枚举类Enum/数量类Quant
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType


    def _deserialize(self, params):
        self._ParamKey = params.get("ParamKey")
        self._ParamKeyName = params.get("ParamKeyName")
        self._ParamValue = params.get("ParamValue")
        self._ParamValueName = params.get("ParamValueName")
        self._ParamType = params.get("ParamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyLicenseRequest(AbstractModel):
    """VerifyLicense请求参数结构体

    """


class VerifyLicenseResponse(AbstractModel):
    """VerifyLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 软件的详细授权信息。
        :type License: :class:`tencentcloud.cloudapp.v20220530.models.License`
        :param _Timestamp: 当前请求服务端的时间戳，格式为RFC3339
        :type Timestamp: str
        :param _Signature: 对License字段对应的json数据的签名
        :type Signature: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._License = None
        self._Timestamp = None
        self._Signature = None
        self._RequestId = None

    @property
    def License(self):
        """软件的详细授权信息。
        :rtype: :class:`tencentcloud.cloudapp.v20220530.models.License`
        """
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def Timestamp(self):
        """当前请求服务端的时间戳，格式为RFC3339
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Signature(self):
        """对License字段对应的json数据的签名
        :rtype: str
        """
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("License") is not None:
            self._License = License()
            self._License._deserialize(params.get("License"))
        self._Timestamp = params.get("Timestamp")
        self._Signature = params.get("Signature")
        self._RequestId = params.get("RequestId")