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


class BindDevInfo(AbstractModel):
    """终端用户绑定的设备

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceModel: 设备型号
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceModel: str
        :param _Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        """
        self._Tid = None
        self._DeviceName = None
        self._DeviceModel = None
        self._Role = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceModel(self):
        """设备型号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeviceModel

    @DeviceModel.setter
    def DeviceModel(self, DeviceModel):
        self._DeviceModel = DeviceModel

    @property
    def Role(self):
        """用户角色，owner：主人，guest：访客
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._DeviceName = params.get("DeviceName")
        self._DeviceModel = params.get("DeviceModel")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindUsrInfo(AbstractModel):
    """设备绑定的终端用户

    """

    def __init__(self):
        r"""
        :param _AccessId: IotVideo平台分配给终端用户的用户id
        :type AccessId: str
        :param _Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        """
        self._AccessId = None
        self._Role = None

    @property
    def AccessId(self):
        """IotVideo平台分配给终端用户的用户id
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def Role(self):
        """用户角色，owner：主人，guest：访客
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfo(AbstractModel):
    """证书信息

    """

    def __init__(self):
        r"""
        :param _SecretId: SecretId
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretId: str
        :param _SecretKey: SecretKey
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _Token: Token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _ExpiredTime: 过期时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: int
        """
        self._SecretId = None
        self._SecretKey = None
        self._Token = None
        self._ExpiredTime = None

    @property
    def SecretId(self):
        """SecretId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        """SecretKey
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Token(self):
        """Token
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        """过期时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


    def _deserialize(self, params):
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Token = params.get("Token")
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearDeviceActiveCodeRequest(AbstractModel):
    """ClearDeviceActiveCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID列表，0<元素数量<=100
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID列表，0<元素数量<=100
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearDeviceActiveCodeResponse(AbstractModel):
    """ClearDeviceActiveCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Contents(AbstractModel):
    """版本发布的描述信息，需要国际化，可以为空

    """

    def __init__(self):
        r"""
        :param _En: 英文，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type En: str
        :param _Cn: 中文简体，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Cn: str
        :param _Tc: 中文繁体(Traditional Chinese)，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Tc: str
        :param _Default: 默认语言，最多不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Default: str
        """
        self._En = None
        self._Cn = None
        self._Tc = None
        self._Default = None

    @property
    def En(self):
        """英文，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._En

    @En.setter
    def En(self, En):
        self._En = En

    @property
    def Cn(self):
        """中文简体，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cn

    @Cn.setter
    def Cn(self, Cn):
        self._Cn = Cn

    @property
    def Tc(self):
        """中文繁体(Traditional Chinese)，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Tc

    @Tc.setter
    def Tc(self, Tc):
        self._Tc = Tc

    @property
    def Default(self):
        """默认语言，最多不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default


    def _deserialize(self, params):
        self._En = params.get("En")
        self._Cn = params.get("Cn")
        self._Tc = params.get("Tc")
        self._Default = params.get("Default")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosCertificate(AbstractModel):
    """申请上传证书回包

    """

    def __init__(self):
        r"""
        :param _StorageBucket: cos存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageBucket: str
        :param _StorageRegion: cos存储园区
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageRegion: str
        :param _StoragePath: 存储路径，录制场景下该值为存储目录
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePath: str
        :param _TempCertificate: 证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TempCertificate: :class:`tencentcloud.iotvideo.v20191126.models.CertificateInfo`
        :param _SessionKey: SessionKey
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionKey: str
        """
        self._StorageBucket = None
        self._StorageRegion = None
        self._StoragePath = None
        self._TempCertificate = None
        self._SessionKey = None

    @property
    def StorageBucket(self):
        """cos存储桶
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageBucket

    @StorageBucket.setter
    def StorageBucket(self, StorageBucket):
        self._StorageBucket = StorageBucket

    @property
    def StorageRegion(self):
        """cos存储园区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def StoragePath(self):
        """存储路径，录制场景下该值为存储目录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StoragePath

    @StoragePath.setter
    def StoragePath(self, StoragePath):
        self._StoragePath = StoragePath

    @property
    def TempCertificate(self):
        """证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CertificateInfo`
        """
        return self._TempCertificate

    @TempCertificate.setter
    def TempCertificate(self, TempCertificate):
        self._TempCertificate = TempCertificate

    @property
    def SessionKey(self):
        """SessionKey
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionKey

    @SessionKey.setter
    def SessionKey(self, SessionKey):
        self._SessionKey = SessionKey


    def _deserialize(self, params):
        self._StorageBucket = params.get("StorageBucket")
        self._StorageRegion = params.get("StorageRegion")
        self._StoragePath = params.get("StoragePath")
        if params.get("TempCertificate") is not None:
            self._TempCertificate = CertificateInfo()
            self._TempCertificate._deserialize(params.get("TempCertificate"))
        self._SessionKey = params.get("SessionKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnonymousAccessTokenRequest(AbstractModel):
    """CreateAnonymousAccessToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TtlMinutes: Token的TTL(time to alive)分钟数,最大值1440(即24小时)
        :type TtlMinutes: int
        :param _Tid: 设备ID。创建Token时, 此参数为必须项
        :type Tid: str
        :param _OldAccessToken: 旧的AccessToken。续期Token时，此参数为必须
        :type OldAccessToken: str
        """
        self._TtlMinutes = None
        self._Tid = None
        self._OldAccessToken = None

    @property
    def TtlMinutes(self):
        """Token的TTL(time to alive)分钟数,最大值1440(即24小时)
        :rtype: int
        """
        return self._TtlMinutes

    @TtlMinutes.setter
    def TtlMinutes(self, TtlMinutes):
        self._TtlMinutes = TtlMinutes

    @property
    def Tid(self):
        """设备ID。创建Token时, 此参数为必须项
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def OldAccessToken(self):
        """旧的AccessToken。续期Token时，此参数为必须
        :rtype: str
        """
        return self._OldAccessToken

    @OldAccessToken.setter
    def OldAccessToken(self, OldAccessToken):
        self._OldAccessToken = OldAccessToken


    def _deserialize(self, params):
        self._TtlMinutes = params.get("TtlMinutes")
        self._Tid = params.get("Tid")
        self._OldAccessToken = params.get("OldAccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnonymousAccessTokenResponse(AbstractModel):
    """CreateAnonymousAccessToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param _AccessToken: IoT Video平台的AccessToken
        :type AccessToken: str
        :param _ExpireTime: Token的过期时间，单位秒(UTC时间)
        :type ExpireTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessId = None
        self._AccessToken = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def AccessId(self):
        """终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def AccessToken(self):
        """IoT Video平台的AccessToken
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ExpireTime(self):
        """Token的过期时间，单位秒(UTC时间)
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

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
        self._AccessId = params.get("AccessId")
        self._AccessToken = params.get("AccessToken")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class CreateAppUsrRequest(AbstractModel):
    """CreateAppUsr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CunionId: 标识用户的唯一ID，防止同一个用户多次注册
        :type CunionId: str
        :param _Mobile: 用于小程序关联手机号
        :type Mobile: str
        """
        self._CunionId = None
        self._Mobile = None

    @property
    def CunionId(self):
        """标识用户的唯一ID，防止同一个用户多次注册
        :rtype: str
        """
        return self._CunionId

    @CunionId.setter
    def CunionId(self, CunionId):
        self._CunionId = CunionId

    @property
    def Mobile(self):
        """用于小程序关联手机号
        :rtype: str
        """
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile


    def _deserialize(self, params):
        self._CunionId = params.get("CunionId")
        self._Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppUsrResponse(AbstractModel):
    """CreateAppUsr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CunionId: 厂商云标识用户的唯一ID
        :type CunionId: str
        :param _AccessId: 客户的终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param _NewRegist: 用户是否为新创建
        :type NewRegist: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CunionId = None
        self._AccessId = None
        self._NewRegist = None
        self._RequestId = None

    @property
    def CunionId(self):
        """厂商云标识用户的唯一ID
        :rtype: str
        """
        return self._CunionId

    @CunionId.setter
    def CunionId(self, CunionId):
        self._CunionId = CunionId

    @property
    def AccessId(self):
        """客户的终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def NewRegist(self):
        """用户是否为新创建
        :rtype: bool
        """
        return self._NewRegist

    @NewRegist.setter
    def NewRegist(self, NewRegist):
        self._NewRegist = NewRegist

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
        self._CunionId = params.get("CunionId")
        self._AccessId = params.get("AccessId")
        self._NewRegist = params.get("NewRegist")
        self._RequestId = params.get("RequestId")


class CreateBindingRequest(AbstractModel):
    """CreateBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        :param _ForceBind: 是否踢掉之前的主人，true：踢掉；false：不踢掉。当role为guest时，可以不填
        :type ForceBind: bool
        :param _Nick: 设备昵称，最多不超过64个字符
        :type Nick: str
        :param _BindToken: 绑定过程中的会话token，由设备通过SDK接口确认是否允许绑定的token，用于增加设备被绑定的安全性
        :type BindToken: str
        """
        self._AccessId = None
        self._Tid = None
        self._Role = None
        self._ForceBind = None
        self._Nick = None
        self._BindToken = None

    @property
    def AccessId(self):
        """终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Role(self):
        """用户角色，owner：主人，guest：访客
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def ForceBind(self):
        """是否踢掉之前的主人，true：踢掉；false：不踢掉。当role为guest时，可以不填
        :rtype: bool
        """
        return self._ForceBind

    @ForceBind.setter
    def ForceBind(self, ForceBind):
        self._ForceBind = ForceBind

    @property
    def Nick(self):
        """设备昵称，最多不超过64个字符
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick

    @property
    def BindToken(self):
        """绑定过程中的会话token，由设备通过SDK接口确认是否允许绑定的token，用于增加设备被绑定的安全性
        :rtype: str
        """
        return self._BindToken

    @BindToken.setter
    def BindToken(self, BindToken):
        self._BindToken = BindToken


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        self._Tid = params.get("Tid")
        self._Role = params.get("Role")
        self._ForceBind = params.get("ForceBind")
        self._Nick = params.get("Nick")
        self._BindToken = params.get("BindToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBindingResponse(AbstractModel):
    """CreateBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessToken: 访问设备的AccessToken
        :type AccessToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessToken = None
        self._RequestId = None

    @property
    def AccessToken(self):
        """访问设备的AccessToken
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

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
        self._AccessToken = params.get("AccessToken")
        self._RequestId = params.get("RequestId")


class CreateDevTokenRequest(AbstractModel):
    """CreateDevToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 客户的终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param _Tids: 设备TID列表,0<元素数量<=100
        :type Tids: list of str
        :param _TtlMinutes: Token的TTL(time to alive)分钟数
        :type TtlMinutes: int
        """
        self._AccessId = None
        self._Tids = None
        self._TtlMinutes = None

    @property
    def AccessId(self):
        """客户的终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def Tids(self):
        """设备TID列表,0<元素数量<=100
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids

    @property
    def TtlMinutes(self):
        """Token的TTL(time to alive)分钟数
        :rtype: int
        """
        return self._TtlMinutes

    @TtlMinutes.setter
    def TtlMinutes(self, TtlMinutes):
        self._TtlMinutes = TtlMinutes


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        self._Tids = params.get("Tids")
        self._TtlMinutes = params.get("TtlMinutes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDevTokenResponse(AbstractModel):
    """CreateDevToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回的用户token列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DevTokenInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """返回的用户token列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DevTokenInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DevTokenInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class CreateDevicesRequest(AbstractModel):
    """CreateDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Number: 创建设备的数量，数量范围1-100
        :type Number: int
        :param _NamePrefix: 设备名称前缀，支持英文、数字，不超过10字符
        :type NamePrefix: str
        :param _Operator: 操作人
        :type Operator: str
        """
        self._ProductId = None
        self._Number = None
        self._NamePrefix = None
        self._Operator = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Number(self):
        """创建设备的数量，数量范围1-100
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def NamePrefix(self):
        """设备名称前缀，支持英文、数字，不超过10字符
        :rtype: str
        """
        return self._NamePrefix

    @NamePrefix.setter
    def NamePrefix(self, NamePrefix):
        self._NamePrefix = NamePrefix

    @property
    def Operator(self):
        """操作人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Number = params.get("Number")
        self._NamePrefix = params.get("NamePrefix")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDevicesResponse(AbstractModel):
    """CreateDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 新创建设备的认证信息
        :type Data: list of DeviceCertificate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """新创建设备的认证信息
        :rtype: list of DeviceCertificate
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DeviceCertificate()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class CreateGencodeRequest(AbstractModel):
    """CreateGencode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Revision: 物模型发布版本号,-1代表未发布的，保存的是草稿箱的版本。1代表已发布的物模型。
        :type Revision: int
        """
        self._ProductId = None
        self._Revision = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Revision(self):
        """物模型发布版本号,-1代表未发布的，保存的是草稿箱的版本。1代表已发布的物模型。
        :rtype: int
        """
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Revision = params.get("Revision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGencodeResponse(AbstractModel):
    """CreateGencode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZipCode: 生成的源代码(zip压缩后的base64编码)
注意：此字段可能返回 null，表示取不到有效值。
        :type ZipCode: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZipCode = None
        self._RequestId = None

    @property
    def ZipCode(self):
        """生成的源代码(zip压缩后的base64编码)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZipCode

    @ZipCode.setter
    def ZipCode(self, ZipCode):
        self._ZipCode = ZipCode

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
        self._ZipCode = params.get("ZipCode")
        self._RequestId = params.get("RequestId")


class CreateIotDataTypeRequest(AbstractModel):
    """CreateIotDataType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IotDataType: 用户自定义数据类型，json格式的字符串
        :type IotDataType: str
        """
        self._IotDataType = None

    @property
    def IotDataType(self):
        """用户自定义数据类型，json格式的字符串
        :rtype: str
        """
        return self._IotDataType

    @IotDataType.setter
    def IotDataType(self, IotDataType):
        self._IotDataType = IotDataType


    def _deserialize(self, params):
        self._IotDataType = params.get("IotDataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIotDataTypeResponse(AbstractModel):
    """CreateIotDataType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateIotModelRequest(AbstractModel):
    """CreateIotModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _IotModel: 物模型json串
        :type IotModel: str
        """
        self._ProductId = None
        self._IotModel = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def IotModel(self):
        """物模型json串
        :rtype: str
        """
        return self._IotModel

    @IotModel.setter
    def IotModel(self, IotModel):
        self._IotModel = IotModel


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._IotModel = params.get("IotModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIotModelResponse(AbstractModel):
    """CreateIotModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductModel: 产器型号(APP产品,为APP包名)
        :type ProductModel: str
        :param _ProductName: 产品名称
仅支持中文、英文、数字、下划线，不超过32个字符
        :type ProductName: str
        :param _ProductDescription: 产品描述信息
不支持单引号、双引号、退格符、回车符、换行符、制表符、反斜杠、下划线、“%”、“#”、“$”，不超过128字符
        :type ProductDescription: str
        :param _Features: 设备功能码（ypsxth:音频双向通话 ，spdxth:视频单向通话）
        :type Features: list of str
        :param _ChipManufactureId: 主芯片产商ID
        :type ChipManufactureId: str
        :param _ChipId: 主芯片ID
        :type ChipId: str
        :param _ProductRegion: 地域：
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
Other-Overseas（其他境外地区）
        :type ProductRegion: str
        :param _ProductCate: 设备类型, 0-普通视频设备，1-NVR设备
        :type ProductCate: int
        :param _AccessMode: 接入模型，bit0是0：公版小程序未接入，bit0是1：公版小程序已接入
        :type AccessMode: int
        :param _Os: Linux,Android,Liteos等系统
        :type Os: str
        :param _ChipArch: 芯片架构，只是针对操作系统为android的
        :type ChipArch: str
        """
        self._ProductModel = None
        self._ProductName = None
        self._ProductDescription = None
        self._Features = None
        self._ChipManufactureId = None
        self._ChipId = None
        self._ProductRegion = None
        self._ProductCate = None
        self._AccessMode = None
        self._Os = None
        self._ChipArch = None

    @property
    def ProductModel(self):
        """产器型号(APP产品,为APP包名)
        :rtype: str
        """
        return self._ProductModel

    @ProductModel.setter
    def ProductModel(self, ProductModel):
        self._ProductModel = ProductModel

    @property
    def ProductName(self):
        """产品名称
仅支持中文、英文、数字、下划线，不超过32个字符
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductDescription(self):
        """产品描述信息
不支持单引号、双引号、退格符、回车符、换行符、制表符、反斜杠、下划线、“%”、“#”、“$”，不超过128字符
        :rtype: str
        """
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def Features(self):
        """设备功能码（ypsxth:音频双向通话 ，spdxth:视频单向通话）
        :rtype: list of str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def ChipManufactureId(self):
        """主芯片产商ID
        :rtype: str
        """
        return self._ChipManufactureId

    @ChipManufactureId.setter
    def ChipManufactureId(self, ChipManufactureId):
        self._ChipManufactureId = ChipManufactureId

    @property
    def ChipId(self):
        """主芯片ID
        :rtype: str
        """
        return self._ChipId

    @ChipId.setter
    def ChipId(self, ChipId):
        self._ChipId = ChipId

    @property
    def ProductRegion(self):
        """地域：
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
Other-Overseas（其他境外地区）
        :rtype: str
        """
        return self._ProductRegion

    @ProductRegion.setter
    def ProductRegion(self, ProductRegion):
        self._ProductRegion = ProductRegion

    @property
    def ProductCate(self):
        """设备类型, 0-普通视频设备，1-NVR设备
        :rtype: int
        """
        return self._ProductCate

    @ProductCate.setter
    def ProductCate(self, ProductCate):
        self._ProductCate = ProductCate

    @property
    def AccessMode(self):
        """接入模型，bit0是0：公版小程序未接入，bit0是1：公版小程序已接入
        :rtype: int
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def Os(self):
        """Linux,Android,Liteos等系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def ChipArch(self):
        """芯片架构，只是针对操作系统为android的
        :rtype: str
        """
        return self._ChipArch

    @ChipArch.setter
    def ChipArch(self, ChipArch):
        self._ChipArch = ChipArch


    def _deserialize(self, params):
        self._ProductModel = params.get("ProductModel")
        self._ProductName = params.get("ProductName")
        self._ProductDescription = params.get("ProductDescription")
        self._Features = params.get("Features")
        self._ChipManufactureId = params.get("ChipManufactureId")
        self._ChipId = params.get("ChipId")
        self._ProductRegion = params.get("ProductRegion")
        self._ProductCate = params.get("ProductCate")
        self._AccessMode = params.get("AccessMode")
        self._Os = params.get("Os")
        self._ChipArch = params.get("ChipArch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 产品详细信息
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.ProductBase`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """产品详细信息
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ProductBase`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ProductBase()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateStorageRequest(AbstractModel):
    """CreateStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgId: 云存套餐ID
        :type PkgId: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _UserTag: 用户唯一标识，由厂商保证内部唯一性
        :type UserTag: str
        """
        self._PkgId = None
        self._Tid = None
        self._UserTag = None

    @property
    def PkgId(self):
        """云存套餐ID
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def UserTag(self):
        """用户唯一标识，由厂商保证内部唯一性
        :rtype: str
        """
        return self._UserTag

    @UserTag.setter
    def UserTag(self, UserTag):
        self._UserTag = UserTag


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        self._Tid = params.get("Tid")
        self._UserTag = params.get("UserTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStorageResponse(AbstractModel):
    """CreateStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateStorageServiceRequest(AbstractModel):
    """CreateStorageService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgId: 云存套餐ID：
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
        :type PkgId: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _OrderCount: 订单数量,可一次性创建多个订单
        :type OrderCount: int
        :param _StorageRegion: 云存服务所在的区域,如ap-guangzhou,ap-singapore, na-siliconvalley, eu-frankfurt
        :type StorageRegion: str
        :param _ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param _AccessId: 设备主人用户在IoT Video平台的注册ID。该参数用于验证Paas/Saas平台的设备/用户关系链是否一致
        :type AccessId: str
        :param _EnableTime: 服务生效时间,若不指定此参数，服务立即生效
        :type EnableTime: int
        """
        self._PkgId = None
        self._Tid = None
        self._OrderCount = None
        self._StorageRegion = None
        self._ChnNum = None
        self._AccessId = None
        self._EnableTime = None

    @property
    def PkgId(self):
        """云存套餐ID：
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
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def OrderCount(self):
        """订单数量,可一次性创建多个订单
        :rtype: int
        """
        return self._OrderCount

    @OrderCount.setter
    def OrderCount(self, OrderCount):
        self._OrderCount = OrderCount

    @property
    def StorageRegion(self):
        """云存服务所在的区域,如ap-guangzhou,ap-singapore, na-siliconvalley, eu-frankfurt
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def ChnNum(self):
        """视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :rtype: int
        """
        return self._ChnNum

    @ChnNum.setter
    def ChnNum(self, ChnNum):
        self._ChnNum = ChnNum

    @property
    def AccessId(self):
        """设备主人用户在IoT Video平台的注册ID。该参数用于验证Paas/Saas平台的设备/用户关系链是否一致
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def EnableTime(self):
        """服务生效时间,若不指定此参数，服务立即生效
        :rtype: int
        """
        return self._EnableTime

    @EnableTime.setter
    def EnableTime(self, EnableTime):
        self._EnableTime = EnableTime


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        self._Tid = params.get("Tid")
        self._OrderCount = params.get("OrderCount")
        self._StorageRegion = params.get("StorageRegion")
        self._ChnNum = params.get("ChnNum")
        self._AccessId = params.get("AccessId")
        self._EnableTime = params.get("EnableTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStorageServiceResponse(AbstractModel):
    """CreateStorageService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsRenew: 标志是否为续订
        :type IsRenew: bool
        :param _ServiceId: 云存服务ID
        :type ServiceId: str
        :param _StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param _AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param _StartTime: 服务开始时间
        :type StartTime: int
        :param _EndTime: 服务失效时间
        :type EndTime: int
        :param _Status: 服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :type Status: int
        :param _Data: 新增的云存定单列表
        :type Data: list of StorageOrder
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsRenew = None
        self._ServiceId = None
        self._StorageRegion = None
        self._Tid = None
        self._ChnNum = None
        self._AccessId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Data = None
        self._RequestId = None

    @property
    def IsRenew(self):
        """标志是否为续订
        :rtype: bool
        """
        return self._IsRenew

    @IsRenew.setter
    def IsRenew(self, IsRenew):
        self._IsRenew = IsRenew

    @property
    def ServiceId(self):
        """云存服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StorageRegion(self):
        """云存服务所在的区域
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def ChnNum(self):
        """视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :rtype: int
        """
        return self._ChnNum

    @ChnNum.setter
    def ChnNum(self, ChnNum):
        self._ChnNum = ChnNum

    @property
    def AccessId(self):
        """终端用户在IoT Video平台的注册ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def StartTime(self):
        """服务开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """服务失效时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Data(self):
        """新增的云存定单列表
        :rtype: list of StorageOrder
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._IsRenew = params.get("IsRenew")
        self._ServiceId = params.get("ServiceId")
        self._StorageRegion = params.get("StorageRegion")
        self._Tid = params.get("Tid")
        self._ChnNum = params.get("ChnNum")
        self._AccessId = params.get("AccessId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTraceIdsRequest(AbstractModel):
    """CreateTraceIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID列表
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID列表
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTraceIdsResponse(AbstractModel):
    """CreateTraceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateUploadPathRequest(AbstractModel):
    """CreateUploadPath请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _FileName: 固件文件名
        :type FileName: str
        """
        self._ProductId = None
        self._FileName = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FileName(self):
        """固件文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUploadPathResponse(AbstractModel):
    """CreateUploadPath返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 固件上传地址URL，用户可将本地的固件文件通过该URL以PUT的请求方式上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """固件上传地址URL，用户可将本地的固件文件通过该URL以PUT的请求方式上传。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class CreateUploadTestRequest(AbstractModel):
    """CreateUploadTest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgId: package ID
        :type PkgId: str
        :param _Tid: 设备TID
        :type Tid: str
        """
        self._PkgId = None
        self._Tid = None

    @property
    def PkgId(self):
        """package ID
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        self._Tid = params.get("Tid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUploadTestResponse(AbstractModel):
    """CreateUploadTest返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 申请设备证书返回的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.CosCertificate`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """申请设备证书返回的信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CosCertificate`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = CosCertificate()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateUsrTokenRequest(AbstractModel):
    """CreateUsrToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param _UniqueId: 终端唯一ID，用于区分同一个用户的多个终端
        :type UniqueId: str
        :param _TtlMinutes: Token的TTL(time to alive)分钟数
        :type TtlMinutes: int
        :param _OldAccessToken: 旧的AccessToken。续期Token时，此参数为必须。
        :type OldAccessToken: str
        """
        self._AccessId = None
        self._UniqueId = None
        self._TtlMinutes = None
        self._OldAccessToken = None

    @property
    def AccessId(self):
        """终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def UniqueId(self):
        """终端唯一ID，用于区分同一个用户的多个终端
        :rtype: str
        """
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId

    @property
    def TtlMinutes(self):
        """Token的TTL(time to alive)分钟数
        :rtype: int
        """
        return self._TtlMinutes

    @TtlMinutes.setter
    def TtlMinutes(self, TtlMinutes):
        self._TtlMinutes = TtlMinutes

    @property
    def OldAccessToken(self):
        """旧的AccessToken。续期Token时，此参数为必须。
        :rtype: str
        """
        return self._OldAccessToken

    @OldAccessToken.setter
    def OldAccessToken(self, OldAccessToken):
        self._OldAccessToken = OldAccessToken


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        self._UniqueId = params.get("UniqueId")
        self._TtlMinutes = params.get("TtlMinutes")
        self._OldAccessToken = params.get("OldAccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsrTokenResponse(AbstractModel):
    """CreateUsrToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param _AccessToken: IoT Video平台的AccessToken
        :type AccessToken: str
        :param _ExpireTime: Token的过期时间，单位秒(UTC时间)
        :type ExpireTime: int
        :param _TerminalId: 终端ID
        :type TerminalId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessId = None
        self._AccessToken = None
        self._ExpireTime = None
        self._TerminalId = None
        self._RequestId = None

    @property
    def AccessId(self):
        """终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def AccessToken(self):
        """IoT Video平台的AccessToken
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ExpireTime(self):
        """Token的过期时间，单位秒(UTC时间)
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TerminalId(self):
        """终端ID
        :rtype: str
        """
        return self._TerminalId

    @TerminalId.setter
    def TerminalId(self, TerminalId):
        self._TerminalId = TerminalId

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
        self._AccessId = params.get("AccessId")
        self._AccessToken = params.get("AccessToken")
        self._ExpireTime = params.get("ExpireTime")
        self._TerminalId = params.get("TerminalId")
        self._RequestId = params.get("RequestId")


class Data(AbstractModel):
    """接口DescribeStream输出参数

    """

    def __init__(self):
        r"""
        :param _Protocol: 直播协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _URI: 流媒体播放地址
注意：此字段可能返回 null，表示取不到有效值。
        :type URI: str
        :param _ExpireTime: 流媒体地址过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param _VideoCodec: 视频编码
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoCodec: str
        :param _AudioCodec: 音频编码
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioCodec: str
        """
        self._Protocol = None
        self._URI = None
        self._ExpireTime = None
        self._VideoCodec = None
        self._AudioCodec = None

    @property
    def Protocol(self):
        """直播协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def URI(self):
        """流媒体播放地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._URI

    @URI.setter
    def URI(self, URI):
        self._URI = URI

    @property
    def ExpireTime(self):
        """流媒体地址过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def VideoCodec(self):
        """视频编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VideoCodec

    @VideoCodec.setter
    def VideoCodec(self, VideoCodec):
        self._VideoCodec = VideoCodec

    @property
    def AudioCodec(self):
        """音频编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AudioCodec

    @AudioCodec.setter
    def AudioCodec(self, AudioCodec):
        self._AudioCodec = AudioCodec


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._URI = params.get("URI")
        self._ExpireTime = params.get("ExpireTime")
        self._VideoCodec = params.get("VideoCodec")
        self._AudioCodec = params.get("AudioCodec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppUsrRequest(AbstractModel):
    """DeleteAppUsr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 客户的终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        """
        self._AccessId = None

    @property
    def AccessId(self):
        """客户的终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppUsrResponse(AbstractModel):
    """DeleteAppUsr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteBindingRequest(AbstractModel):
    """DeleteBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        """
        self._AccessId = None
        self._Tid = None
        self._Role = None

    @property
    def AccessId(self):
        """终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Role(self):
        """用户角色，owner：主人，guest：访客
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        self._Tid = params.get("Tid")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBindingResponse(AbstractModel):
    """DeleteBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID列表
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID列表
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteIotDataTypeRequest(AbstractModel):
    """DeleteIotDataType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeId: 自定义数据类型的标识符
        :type TypeId: str
        """
        self._TypeId = None

    @property
    def TypeId(self):
        """自定义数据类型的标识符
        :rtype: str
        """
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIotDataTypeResponse(AbstractModel):
    """DeleteIotDataType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteMessageQueueRequest(AbstractModel):
    """DeleteMessageQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        """产品ID
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
        


class DeleteMessageQueueResponse(AbstractModel):
    """DeleteMessageQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOtaVersionRequest(AbstractModel):
    """DeleteOtaVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param _Operator: 操作人
        :type Operator: str
        """
        self._ProductId = None
        self._OtaVersion = None
        self._Operator = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def Operator(self):
        """操作人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOtaVersionResponse(AbstractModel):
    """DeleteOtaVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        """产品ID
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
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteTraceIdsRequest(AbstractModel):
    """DeleteTraceIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID列表
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID列表
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTraceIdsResponse(AbstractModel):
    """DeleteTraceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeliverStorageServiceRequest(AbstractModel):
    """DeliverStorageService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcServiceId: 待转移的源云存服务ID
        :type SrcServiceId: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param _AccessId: 设备主人用户在IoT Video平台的注册ID。该参数用于验证Paas/Saas平台的设备/用户关系链是否一致
        :type AccessId: str
        """
        self._SrcServiceId = None
        self._Tid = None
        self._ChnNum = None
        self._AccessId = None

    @property
    def SrcServiceId(self):
        """待转移的源云存服务ID
        :rtype: str
        """
        return self._SrcServiceId

    @SrcServiceId.setter
    def SrcServiceId(self, SrcServiceId):
        self._SrcServiceId = SrcServiceId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def ChnNum(self):
        """视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :rtype: int
        """
        return self._ChnNum

    @ChnNum.setter
    def ChnNum(self, ChnNum):
        self._ChnNum = ChnNum

    @property
    def AccessId(self):
        """设备主人用户在IoT Video平台的注册ID。该参数用于验证Paas/Saas平台的设备/用户关系链是否一致
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId


    def _deserialize(self, params):
        self._SrcServiceId = params.get("SrcServiceId")
        self._Tid = params.get("Tid")
        self._ChnNum = params.get("ChnNum")
        self._AccessId = params.get("AccessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeliverStorageServiceResponse(AbstractModel):
    """DeliverStorageService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcServiceId: 被转出的云存服务ID
        :type SrcServiceId: str
        :param _ServiceId: 被转入的云存服务ID
        :type ServiceId: str
        :param _StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param _AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param _StartTime: 服务开始时间
        :type StartTime: int
        :param _EndTime: 服务失效时间
        :type EndTime: int
        :param _Status: 服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :type Status: int
        :param _Data: 新增的云存订单列表
        :type Data: list of StorageOrder
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SrcServiceId = None
        self._ServiceId = None
        self._StorageRegion = None
        self._Tid = None
        self._ChnNum = None
        self._AccessId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Data = None
        self._RequestId = None

    @property
    def SrcServiceId(self):
        """被转出的云存服务ID
        :rtype: str
        """
        return self._SrcServiceId

    @SrcServiceId.setter
    def SrcServiceId(self, SrcServiceId):
        self._SrcServiceId = SrcServiceId

    @property
    def ServiceId(self):
        """被转入的云存服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StorageRegion(self):
        """云存服务所在的区域
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def ChnNum(self):
        """视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :rtype: int
        """
        return self._ChnNum

    @ChnNum.setter
    def ChnNum(self, ChnNum):
        self._ChnNum = ChnNum

    @property
    def AccessId(self):
        """终端用户在IoT Video平台的注册ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def StartTime(self):
        """服务开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """服务失效时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Data(self):
        """新增的云存订单列表
        :rtype: list of StorageOrder
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._SrcServiceId = params.get("SrcServiceId")
        self._ServiceId = params.get("ServiceId")
        self._StorageRegion = params.get("StorageRegion")
        self._Tid = params.get("Tid")
        self._ChnNum = params.get("ChnNum")
        self._AccessId = params.get("AccessId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccountBalanceRequest(AbstractModel):
    """DescribeAccountBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 账户类型 1:设备接入 2:云存
        :type AccountType: int
        """
        self._AccountType = None

    @property
    def AccountType(self):
        """账户类型 1:设备接入 2:云存
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountBalanceResponse(AbstractModel):
    """DescribeAccountBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 账户类型 1=设备接入;2=云存。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountType: int
        :param _Balance: 余额, 单位 : 分(人民币)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Balance: int
        :param _State: 账户状态，1=正常；8=冻结；9=销户。
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _LastUpdateTime: 最后修改时间，UTC值。
注意：此字段可能返回 null，表示取不到有效值。
        :type LastUpdateTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountType = None
        self._Balance = None
        self._State = None
        self._LastUpdateTime = None
        self._RequestId = None

    @property
    def AccountType(self):
        """账户类型 1=设备接入;2=云存。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Balance(self):
        """余额, 单位 : 分(人民币)。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def State(self):
        """账户状态，1=正常；8=冻结；9=销户。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def LastUpdateTime(self):
        """最后修改时间，UTC值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

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
        self._AccountType = params.get("AccountType")
        self._Balance = params.get("Balance")
        self._State = params.get("State")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeBindDevRequest(AbstractModel):
    """DescribeBindDev请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        """
        self._AccessId = None

    @property
    def AccessId(self):
        """终端用户在IoT Video上的唯一标识ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindDevResponse(AbstractModel):
    """DescribeBindDev返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 绑定的设备列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of BindDevInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """绑定的设备列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BindDevInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BindDevInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBindUsrRequest(AbstractModel):
    """DescribeBindUsr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _AccessId: 设备主人的AccessId
        :type AccessId: str
        """
        self._Tid = None
        self._AccessId = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def AccessId(self):
        """设备主人的AccessId
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._AccessId = params.get("AccessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindUsrResponse(AbstractModel):
    """DescribeBindUsr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 具有绑定关系的终端用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of BindUsrInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """具有绑定关系的终端用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BindUsrInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BindUsrInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceModelRequest(AbstractModel):
    """DescribeDeviceModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _Branch: 物模型的分支路径
        :type Branch: str
        """
        self._Tid = None
        self._Branch = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Branch(self):
        """物模型的分支路径
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._Branch = params.get("Branch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceModelResponse(AbstractModel):
    """DescribeDeviceModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备物模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.DeviceModelData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备物模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeviceModelData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeviceModelData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        """
        self._Tid = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.DeviceData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeviceData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ReturnModel: 是否返回全量数据
当该值为false时，返回值中的设备物模型、固件版本、在线状态、最后在线时间字段等字段，都将返回数据类型的零值。
        :type ReturnModel: bool
        :param _Limit: 分页数量,0<取值范围<=100
        :type Limit: int
        :param _Offset: 分页偏移，取值＞0
        :type Offset: int
        :param _OtaVersion: 指定固件版本号，为空查询此产品下所有设备
        :type OtaVersion: str
        :param _DeviceName: 设备名称，支持左前缀模糊匹配
        :type DeviceName: str
        """
        self._ProductId = None
        self._ReturnModel = None
        self._Limit = None
        self._Offset = None
        self._OtaVersion = None
        self._DeviceName = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ReturnModel(self):
        """是否返回全量数据
当该值为false时，返回值中的设备物模型、固件版本、在线状态、最后在线时间字段等字段，都将返回数据类型的零值。
        :rtype: bool
        """
        return self._ReturnModel

    @ReturnModel.setter
    def ReturnModel(self, ReturnModel):
        self._ReturnModel = ReturnModel

    @property
    def Limit(self):
        """分页数量,0<取值范围<=100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移，取值＞0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OtaVersion(self):
        """指定固件版本号，为空查询此产品下所有设备
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def DeviceName(self):
        """设备名称，支持左前缀模糊匹配
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ReturnModel = params.get("ReturnModel")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OtaVersion = params.get("OtaVersion")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备信息 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DevicesData
        :param _TotalCount: 设备总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        """设备信息 列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DevicesData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """设备总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DevicesData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIotDataTypeRequest(AbstractModel):
    """DescribeIotDataType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TypeId: 自定义数据类型的标识符，为空则返回全量自定义类型的列表
        :type TypeId: str
        """
        self._TypeId = None

    @property
    def TypeId(self):
        """自定义数据类型的标识符，为空则返回全量自定义类型的列表
        :rtype: str
        """
        return self._TypeId

    @TypeId.setter
    def TypeId(self, TypeId):
        self._TypeId = TypeId


    def _deserialize(self, params):
        self._TypeId = params.get("TypeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIotDataTypeResponse(AbstractModel):
    """DescribeIotDataType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 自定义数据类型，json格式的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """自定义数据类型，json格式的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeIotModelRequest(AbstractModel):
    """DescribeIotModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Revision: 物模型版本号， -1表示最新编辑的（未发布）
        :type Revision: int
        """
        self._ProductId = None
        self._Revision = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Revision(self):
        """物模型版本号， -1表示最新编辑的（未发布）
        :rtype: int
        """
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Revision = params.get("Revision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIotModelResponse(AbstractModel):
    """DescribeIotModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 物模型定义，json格式的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """物模型定义，json格式的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeIotModelsRequest(AbstractModel):
    """DescribeIotModels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        """产品ID
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
        


class DescribeIotModelsResponse(AbstractModel):
    """DescribeIotModels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 历史版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of IotModelData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """历史版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IotModelData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = IotModelData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogsRequest(AbstractModel):
    """DescribeLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _Limit: 当前分页的最大条数,0<取值范围<=100
        :type Limit: int
        :param _Offset: 分页偏移量,取值范围>0
        :type Offset: int
        :param _LogType: 日志类型 1.在线状态变更 2.ProConst变更 3.ProWritable变更 4.Action控制 5.ProReadonly变更 6.Event事件
        :type LogType: int
        :param _StartTime: 查询的起始时间 UNIX时间戳，单位秒
        :type StartTime: int
        :param _DataObject: 物模型对象索引，用于模糊查询，字符长度<=255，每层节点的字符长度<=16
        :type DataObject: str
        :param _EndTime: 查询的结束时间 UNIX时间戳，单位秒
        :type EndTime: int
        """
        self._Tid = None
        self._Limit = None
        self._Offset = None
        self._LogType = None
        self._StartTime = None
        self._DataObject = None
        self._EndTime = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Limit(self):
        """当前分页的最大条数,0<取值范围<=100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量,取值范围>0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def LogType(self):
        """日志类型 1.在线状态变更 2.ProConst变更 3.ProWritable变更 4.Action控制 5.ProReadonly变更 6.Event事件
        :rtype: int
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def StartTime(self):
        """查询的起始时间 UNIX时间戳，单位秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def DataObject(self):
        """物模型对象索引，用于模糊查询，字符长度<=255，每层节点的字符长度<=16
        :rtype: str
        """
        return self._DataObject

    @DataObject.setter
    def DataObject(self, DataObject):
        self._DataObject = DataObject

    @property
    def EndTime(self):
        """查询的结束时间 UNIX时间戳，单位秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._LogType = params.get("LogType")
        self._StartTime = params.get("StartTime")
        self._DataObject = params.get("DataObject")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogsResponse(AbstractModel):
    """DescribeLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备日志信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of LogData
        :param _TotalCount: Data数组所包含的信息条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        """设备日志信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LogData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """Data数组所包含的信息条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = LogData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMessageQueueRequest(AbstractModel):
    """DescribeMessageQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        """产品ID
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
        


class DescribeMessageQueueResponse(AbstractModel):
    """DescribeMessageQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 消息队列配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.MsgQueueData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """消息队列配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.MsgQueueData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = MsgQueueData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeModelDataRetRequest(AbstractModel):
    """DescribeModelDataRet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelDataRetResponse(AbstractModel):
    """DescribeModelDataRet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeOsListRequest(AbstractModel):
    """DescribeOsList请求参数结构体

    """


class DescribeOsListResponse(AbstractModel):
    """DescribeOsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 系统类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.SystemType`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """系统类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.SystemType`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SystemType()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeOtaVersionsRequest(AbstractModel):
    """DescribeOtaVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 每页数量，0<取值范围<=100
        :type Limit: int
        :param _ProductId: 产品ID，为空时查询客户所有产品的版本信息
        :type ProductId: str
        :param _OtaVersion: 版本号，支持模糊匹配
        :type OtaVersion: str
        :param _PubStatus: 版本类型 1未发布 2测试发布 3正式发布 4禁用
        :type PubStatus: int
        """
        self._Offset = None
        self._Limit = None
        self._ProductId = None
        self._OtaVersion = None
        self._PubStatus = None

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，0<取值范围<=100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProductId(self):
        """产品ID，为空时查询客户所有产品的版本信息
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """版本号，支持模糊匹配
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def PubStatus(self):
        """版本类型 1未发布 2测试发布 3正式发布 4禁用
        :rtype: int
        """
        return self._PubStatus

    @PubStatus.setter
    def PubStatus(self, PubStatus):
        self._PubStatus = PubStatus


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._PubStatus = params.get("PubStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOtaVersionsResponse(AbstractModel):
    """DescribeOtaVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 版本数量
        :type TotalCount: int
        :param _Data: 版本详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VersionData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """版本数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """版本详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VersionData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VersionData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        """产品ID
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
        


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 产品详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.ProductData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """产品详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ProductData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ProductData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小，当前页面中显示的最大数量，值范围 1-100
        :type Limit: int
        :param _Offset: 分页偏移，Offset从0开始
        :type Offset: int
        :param _ProductModel: 产器型号(APP产品,为APP包名)
        :type ProductModel: str
        :param _StartTime: 开始时间 ，UNIX 时间戳，单位秒
        :type StartTime: int
        :param _EndTime: 结束时间 ，UNIX 时间戳，单位秒
        :type EndTime: int
        """
        self._Limit = None
        self._Offset = None
        self._ProductModel = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Limit(self):
        """分页大小，当前页面中显示的最大数量，值范围 1-100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移，Offset从0开始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProductModel(self):
        """产器型号(APP产品,为APP包名)
        :rtype: str
        """
        return self._ProductModel

    @ProductModel.setter
    def ProductModel(self, ProductModel):
        self._ProductModel = ProductModel

    @property
    def StartTime(self):
        """开始时间 ，UNIX 时间戳，单位秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间 ，UNIX 时间戳，单位秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProductModel = params.get("ProductModel")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 产品详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ProductData
        :param _TotalCount: 产品总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        """产品详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ProductData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """产品总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ProductData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePubVersionsRequest(AbstractModel):
    """DescribePubVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        """产品ID
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
        


class DescribePubVersionsResponse(AbstractModel):
    """DescribePubVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 历史发布的版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of OtaPubHistory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """历史发布的版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OtaPubHistory
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = OtaPubHistory()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRechargeRecordsRequest(AbstractModel):
    """DescribeRechargeRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 账户类型 1:设备接入 2:云存。
        :type AccountType: int
        :param _Offset: 从第几条记录开始显示, 默认值为0。
        :type Offset: int
        :param _Limit: 总共查询多少条记录，默认为值50。
        :type Limit: int
        """
        self._AccountType = None
        self._Offset = None
        self._Limit = None

    @property
    def AccountType(self):
        """账户类型 1:设备接入 2:云存。
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Offset(self):
        """从第几条记录开始显示, 默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """总共查询多少条记录，默认为值50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRechargeRecordsResponse(AbstractModel):
    """DescribeRechargeRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 账户类型 1:设备接入 2:云存
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountType: int
        :param _Records: 充值记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Records: list of RechargeRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountType = None
        self._Records = None
        self._RequestId = None

    @property
    def AccountType(self):
        """账户类型 1:设备接入 2:云存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Records(self):
        """充值记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RechargeRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

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
        self._AccountType = params.get("AccountType")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = RechargeRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegistrationStatusRequest(AbstractModel):
    """DescribeRegistrationStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CunionIds: 终端用户的唯一ID列表，0<元素数量<=100
        :type CunionIds: list of str
        """
        self._CunionIds = None

    @property
    def CunionIds(self):
        """终端用户的唯一ID列表，0<元素数量<=100
        :rtype: list of str
        """
        return self._CunionIds

    @CunionIds.setter
    def CunionIds(self, CunionIds):
        self._CunionIds = CunionIds


    def _deserialize(self, params):
        self._CunionIds = params.get("CunionIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegistrationStatusResponse(AbstractModel):
    """DescribeRegistrationStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 终端用户注册状态列表
        :type Data: list of RegisteredStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """终端用户注册状态列表
        :rtype: list of RegisteredStatus
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RegisteredStatus()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunLogRequest(AbstractModel):
    """DescribeRunLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        """
        self._Tid = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunLogResponse(AbstractModel):
    """DescribeRunLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备运行日志文本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备运行日志文本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeStorageServiceRequest(AbstractModel):
    """DescribeStorageService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 云存服务ID
        :type ServiceId: str
        :param _GetFinishedOrder: 是否返回已结束的订单信息(已过期/已退订/已转移)
        :type GetFinishedOrder: bool
        """
        self._ServiceId = None
        self._GetFinishedOrder = None

    @property
    def ServiceId(self):
        """云存服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def GetFinishedOrder(self):
        """是否返回已结束的订单信息(已过期/已退订/已转移)
        :rtype: bool
        """
        return self._GetFinishedOrder

    @GetFinishedOrder.setter
    def GetFinishedOrder(self, GetFinishedOrder):
        self._GetFinishedOrder = GetFinishedOrder


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._GetFinishedOrder = params.get("GetFinishedOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStorageServiceResponse(AbstractModel):
    """DescribeStorageService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 云存服务ID
        :type ServiceId: str
        :param _StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param _AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param _StartTime: 服务开始时间
        :type StartTime: int
        :param _EndTime: 服务失效时间
        :type EndTime: int
        :param _Status: 服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :type Status: int
        :param _Data: 云存订单列表
        :type Data: list of StorageOrder
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._StorageRegion = None
        self._Tid = None
        self._ChnNum = None
        self._AccessId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Data = None
        self._RequestId = None

    @property
    def ServiceId(self):
        """云存服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StorageRegion(self):
        """云存服务所在的区域
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def ChnNum(self):
        """视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :rtype: int
        """
        return self._ChnNum

    @ChnNum.setter
    def ChnNum(self, ChnNum):
        self._ChnNum = ChnNum

    @property
    def AccessId(self):
        """终端用户在IoT Video平台的注册ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def StartTime(self):
        """服务开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """服务失效时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Data(self):
        """云存订单列表
        :rtype: list of StorageOrder
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._ServiceId = params.get("ServiceId")
        self._StorageRegion = params.get("StorageRegion")
        self._Tid = params.get("Tid")
        self._ChnNum = params.get("ChnNum")
        self._AccessId = params.get("AccessId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamRequest(AbstractModel):
    """DescribeStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _AccessId: 终端用户ID
        :type AccessId: str
        :param _Protocol: 直播协议, 可选值：RTSP、RTMP、HLS、HLS-fmp4
        :type Protocol: str
        :param _Address: 音视频流地址
        :type Address: str
        :param _AccessToken: 设备访问token，访问用户未绑定的设备时，需提供该参数
        :type AccessToken: str
        """
        self._Tid = None
        self._AccessId = None
        self._Protocol = None
        self._Address = None
        self._AccessToken = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def AccessId(self):
        """终端用户ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def Protocol(self):
        """直播协议, 可选值：RTSP、RTMP、HLS、HLS-fmp4
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Address(self):
        """音视频流地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AccessToken(self):
        """设备访问token，访问用户未绑定的设备时，需提供该参数
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._AccessId = params.get("AccessId")
        self._Protocol = params.get("Protocol")
        self._Address = params.get("Address")
        self._AccessToken = params.get("AccessToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamResponse(AbstractModel):
    """DescribeStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回参数结构
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.Data`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """返回参数结构
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.Data`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = Data()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTraceIdsRequest(AbstractModel):
    """DescribeTraceIds请求参数结构体

    """


class DescribeTraceIdsResponse(AbstractModel):
    """DescribeTraceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备TID列表，列表元素之间以“,”分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备TID列表，列表元素之间以“,”分隔
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeTraceStatusRequest(AbstractModel):
    """DescribeTraceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID列表
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID列表
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTraceStatusResponse(AbstractModel):
    """DescribeTraceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备追踪状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TraceStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备追踪状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TraceStatus
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TraceStatus()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DevTokenInfo(AbstractModel):
    """用于终端用户临时访问设备的token授权信息

    """

    def __init__(self):
        r"""
        :param _AccessId: 客户的终端用户在IotVideo上的唯一标识id
        :type AccessId: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _AccessToken: IotVideo平台的accessToken
        :type AccessToken: str
        :param _ExpireTime: Token的过期时间，单位秒(UTC时间)
        :type ExpireTime: int
        """
        self._AccessId = None
        self._Tid = None
        self._AccessToken = None
        self._ExpireTime = None

    @property
    def AccessId(self):
        """客户的终端用户在IotVideo上的唯一标识id
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def AccessToken(self):
        """IotVideo平台的accessToken
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ExpireTime(self):
        """Token的过期时间，单位秒(UTC时间)
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._AccessId = params.get("AccessId")
        self._Tid = params.get("Tid")
        self._AccessToken = params.get("AccessToken")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceCertificate(AbstractModel):
    """设备证书及密钥

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _Certificate: 设备初始证书信息，base64编码
        :type Certificate: str
        :param _WhiteBoxSoUrl: 设备私钥下载地址
        :type WhiteBoxSoUrl: str
        """
        self._Tid = None
        self._Certificate = None
        self._WhiteBoxSoUrl = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Certificate(self):
        """设备初始证书信息，base64编码
        :rtype: str
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def WhiteBoxSoUrl(self):
        """设备私钥下载地址
        :rtype: str
        """
        return self._WhiteBoxSoUrl

    @WhiteBoxSoUrl.setter
    def WhiteBoxSoUrl(self, WhiteBoxSoUrl):
        self._WhiteBoxSoUrl = WhiteBoxSoUrl


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._Certificate = params.get("Certificate")
        self._WhiteBoxSoUrl = params.get("WhiteBoxSoUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceData(AbstractModel):
    """设备信息

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
注意：此字段可能返回 null，表示取不到有效值。
        :type Tid: str
        :param _ActiveTime: 激活时间 0代表未激活
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: int
        :param _Disabled: 设备是否被禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Disabled: bool
        :param _OtaVersion: 固件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type OtaVersion: str
        :param _Online: 设备在线状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: int
        :param _LastOnlineTime: 设备最后上线时间（mqtt连接成功时间），UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnlineTime: int
        :param _IotModel: 物模型json数据
注意：此字段可能返回 null，表示取不到有效值。
        :type IotModel: str
        :param _DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _Certificate: 设备初始证书信息，base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param _WhiteBoxSoUrl: 设备私钥下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WhiteBoxSoUrl: str
        :param _StreamStatus: 设备推流状态
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamStatus: bool
        """
        self._Tid = None
        self._ActiveTime = None
        self._Disabled = None
        self._OtaVersion = None
        self._Online = None
        self._LastOnlineTime = None
        self._IotModel = None
        self._DeviceName = None
        self._ProductId = None
        self._Certificate = None
        self._WhiteBoxSoUrl = None
        self._StreamStatus = None

    @property
    def Tid(self):
        """设备TID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def ActiveTime(self):
        """激活时间 0代表未激活
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def Disabled(self):
        """设备是否被禁用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def OtaVersion(self):
        """固件版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def Online(self):
        """设备在线状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LastOnlineTime(self):
        """设备最后上线时间（mqtt连接成功时间），UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastOnlineTime

    @LastOnlineTime.setter
    def LastOnlineTime(self, LastOnlineTime):
        self._LastOnlineTime = LastOnlineTime

    @property
    def IotModel(self):
        """物模型json数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IotModel

    @IotModel.setter
    def IotModel(self, IotModel):
        self._IotModel = IotModel

    @property
    def DeviceName(self):
        """设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ProductId(self):
        """产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Certificate(self):
        """设备初始证书信息，base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def WhiteBoxSoUrl(self):
        """设备私钥下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WhiteBoxSoUrl

    @WhiteBoxSoUrl.setter
    def WhiteBoxSoUrl(self, WhiteBoxSoUrl):
        self._WhiteBoxSoUrl = WhiteBoxSoUrl

    @property
    def StreamStatus(self):
        """设备推流状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._StreamStatus

    @StreamStatus.setter
    def StreamStatus(self, StreamStatus):
        self._StreamStatus = StreamStatus


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._ActiveTime = params.get("ActiveTime")
        self._Disabled = params.get("Disabled")
        self._OtaVersion = params.get("OtaVersion")
        self._Online = params.get("Online")
        self._LastOnlineTime = params.get("LastOnlineTime")
        self._IotModel = params.get("IotModel")
        self._DeviceName = params.get("DeviceName")
        self._ProductId = params.get("ProductId")
        self._Certificate = params.get("Certificate")
        self._WhiteBoxSoUrl = params.get("WhiteBoxSoUrl")
        self._StreamStatus = params.get("StreamStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceModelData(AbstractModel):
    """设备物模型数据

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _Branch: 物模型分支路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param _IotModel: 物模型数据
注意：此字段可能返回 null，表示取不到有效值。
        :type IotModel: str
        """
        self._Tid = None
        self._Branch = None
        self._IotModel = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Branch(self):
        """物模型分支路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def IotModel(self):
        """物模型数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IotModel

    @IotModel.setter
    def IotModel(self, IotModel):
        self._IotModel = IotModel


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._Branch = params.get("Branch")
        self._IotModel = params.get("IotModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DevicesData(AbstractModel):
    """设备列表元素所包含的设备基本信息

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ActiveTime: 激活时间 0代表未激活
        :type ActiveTime: int
        :param _Disabled: 设备是否被禁用
        :type Disabled: bool
        :param _StreamStatus: 设备推流状态
        :type StreamStatus: bool
        :param _OtaVersion: 固件版本
        :type OtaVersion: str
        :param _Online: 设备在线状态
        :type Online: int
        :param _LastOnlineTime: 设备最后上线时间（mqtt连接成功时间），UNIX时间戳，单位秒
        :type LastOnlineTime: int
        :param _IotModel: 物模型json数据
        :type IotModel: str
        :param _LastUpdateTime: 设备固件最新更新时间，UNIX时间戳，单位秒
        :type LastUpdateTime: int
        """
        self._Tid = None
        self._DeviceName = None
        self._ActiveTime = None
        self._Disabled = None
        self._StreamStatus = None
        self._OtaVersion = None
        self._Online = None
        self._LastOnlineTime = None
        self._IotModel = None
        self._LastUpdateTime = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def DeviceName(self):
        """设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ActiveTime(self):
        """激活时间 0代表未激活
        :rtype: int
        """
        return self._ActiveTime

    @ActiveTime.setter
    def ActiveTime(self, ActiveTime):
        self._ActiveTime = ActiveTime

    @property
    def Disabled(self):
        """设备是否被禁用
        :rtype: bool
        """
        return self._Disabled

    @Disabled.setter
    def Disabled(self, Disabled):
        self._Disabled = Disabled

    @property
    def StreamStatus(self):
        """设备推流状态
        :rtype: bool
        """
        return self._StreamStatus

    @StreamStatus.setter
    def StreamStatus(self, StreamStatus):
        self._StreamStatus = StreamStatus

    @property
    def OtaVersion(self):
        """固件版本
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def Online(self):
        """设备在线状态
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LastOnlineTime(self):
        """设备最后上线时间（mqtt连接成功时间），UNIX时间戳，单位秒
        :rtype: int
        """
        return self._LastOnlineTime

    @LastOnlineTime.setter
    def LastOnlineTime(self, LastOnlineTime):
        self._LastOnlineTime = LastOnlineTime

    @property
    def IotModel(self):
        """物模型json数据
        :rtype: str
        """
        return self._IotModel

    @IotModel.setter
    def IotModel(self, IotModel):
        self._IotModel = IotModel

    @property
    def LastUpdateTime(self):
        """设备固件最新更新时间，UNIX时间戳，单位秒
        :rtype: int
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._DeviceName = params.get("DeviceName")
        self._ActiveTime = params.get("ActiveTime")
        self._Disabled = params.get("Disabled")
        self._StreamStatus = params.get("StreamStatus")
        self._OtaVersion = params.get("OtaVersion")
        self._Online = params.get("Online")
        self._LastOnlineTime = params.get("LastOnlineTime")
        self._IotModel = params.get("IotModel")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableDeviceRequest(AbstractModel):
    """DisableDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID ≤100
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID ≤100
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableDeviceResponse(AbstractModel):
    """DisableDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DisableDeviceStreamRequest(AbstractModel):
    """DisableDeviceStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID列表
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID列表
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableDeviceStreamResponse(AbstractModel):
    """DisableDeviceStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DisableOtaVersionRequest(AbstractModel):
    """DisableOtaVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param _Operator: 操作人
        :type Operator: str
        """
        self._ProductId = None
        self._OtaVersion = None
        self._Operator = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def Operator(self):
        """操作人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableOtaVersionResponse(AbstractModel):
    """DisableOtaVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class IotModelData(AbstractModel):
    """物模型历史版本

    """

    def __init__(self):
        r"""
        :param _Revision: 版本号
        :type Revision: int
        :param _ReleaseTime: 发布时间
        :type ReleaseTime: int
        """
        self._Revision = None
        self._ReleaseTime = None

    @property
    def Revision(self):
        """版本号
        :rtype: int
        """
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision

    @property
    def ReleaseTime(self):
        """发布时间
        :rtype: int
        """
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime


    def _deserialize(self, params):
        self._Revision = params.get("Revision")
        self._ReleaseTime = params.get("ReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogData(AbstractModel):
    """设备日志信息

    """

    def __init__(self):
        r"""
        :param _Occurtime: 发生时间 UNIX时间戳，单位秒
        :type Occurtime: int
        :param _LogType: 日志类型 1在线状态变更 2FP变更 3SP变更 4CO控制 5ST变更 6EV事件
        :type LogType: int
        :param _DataObject: 物模型对象索引
注意：此字段可能返回 null，表示取不到有效值。
        :type DataObject: str
        :param _OldValue: 物模型旧值  json串
注意：此字段可能返回 null，表示取不到有效值。
        :type OldValue: str
        :param _NewValue: 物模型新值  json串
注意：此字段可能返回 null，表示取不到有效值。
        :type NewValue: str
        """
        self._Occurtime = None
        self._LogType = None
        self._DataObject = None
        self._OldValue = None
        self._NewValue = None

    @property
    def Occurtime(self):
        """发生时间 UNIX时间戳，单位秒
        :rtype: int
        """
        return self._Occurtime

    @Occurtime.setter
    def Occurtime(self, Occurtime):
        self._Occurtime = Occurtime

    @property
    def LogType(self):
        """日志类型 1在线状态变更 2FP变更 3SP变更 4CO控制 5ST变更 6EV事件
        :rtype: int
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def DataObject(self):
        """物模型对象索引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataObject

    @DataObject.setter
    def DataObject(self, DataObject):
        self._DataObject = DataObject

    @property
    def OldValue(self):
        """物模型旧值  json串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OldValue

    @OldValue.setter
    def OldValue(self, OldValue):
        self._OldValue = OldValue

    @property
    def NewValue(self):
        """物模型新值  json串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NewValue

    @NewValue.setter
    def NewValue(self, NewValue):
        self._NewValue = NewValue


    def _deserialize(self, params):
        self._Occurtime = params.get("Occurtime")
        self._LogType = params.get("LogType")
        self._DataObject = params.get("DataObject")
        self._OldValue = params.get("OldValue")
        self._NewValue = params.get("NewValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceActionRequest(AbstractModel):
    """ModifyDeviceAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _Wakeup: 如果设备处于休眠状态，是否唤醒设备
        :type Wakeup: bool
        :param _Branch: 物模型的分支路径
        :type Branch: str
        :param _Value: 写入的物模型数据，如果是json需要转义成字符串
        :type Value: str
        :param _IsNum: Value字段的类型是否为数值（float、int）
        :type IsNum: bool
        """
        self._Tid = None
        self._Wakeup = None
        self._Branch = None
        self._Value = None
        self._IsNum = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Wakeup(self):
        """如果设备处于休眠状态，是否唤醒设备
        :rtype: bool
        """
        return self._Wakeup

    @Wakeup.setter
    def Wakeup(self, Wakeup):
        self._Wakeup = Wakeup

    @property
    def Branch(self):
        """物模型的分支路径
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def Value(self):
        """写入的物模型数据，如果是json需要转义成字符串
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def IsNum(self):
        """Value字段的类型是否为数值（float、int）
        :rtype: bool
        """
        return self._IsNum

    @IsNum.setter
    def IsNum(self, IsNum):
        self._IsNum = IsNum


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._Wakeup = params.get("Wakeup")
        self._Branch = params.get("Branch")
        self._Value = params.get("Value")
        self._IsNum = params.get("IsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceActionResponse(AbstractModel):
    """ModifyDeviceAction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备端的响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _TaskId: 任务ID
若设备端未能及时响应时，会返回此字段，用户可以通过DescribeModelDataRet获取设备的最终响应结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Data(self):
        """设备端的响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TaskId(self):
        """任务ID
若设备端未能及时响应时，会返回此字段，用户可以通过DescribeModelDataRet获取设备的最终响应结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._Data = params.get("Data")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDevicePropertyRequest(AbstractModel):
    """ModifyDeviceProperty请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _Wakeup: 如果设备处于休眠状态，是否唤醒设备
        :type Wakeup: bool
        :param _Branch: 物模型的分支路径
        :type Branch: str
        :param _Value: 写入的物模型数据，如果是json需要转义成字符串
        :type Value: str
        :param _IsNum: Value字段是否为数值（float、int）
        :type IsNum: bool
        """
        self._Tid = None
        self._Wakeup = None
        self._Branch = None
        self._Value = None
        self._IsNum = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Wakeup(self):
        """如果设备处于休眠状态，是否唤醒设备
        :rtype: bool
        """
        return self._Wakeup

    @Wakeup.setter
    def Wakeup(self, Wakeup):
        self._Wakeup = Wakeup

    @property
    def Branch(self):
        """物模型的分支路径
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def Value(self):
        """写入的物模型数据，如果是json需要转义成字符串
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def IsNum(self):
        """Value字段是否为数值（float、int）
        :rtype: bool
        """
        return self._IsNum

    @IsNum.setter
    def IsNum(self, IsNum):
        self._IsNum = IsNum


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._Wakeup = params.get("Wakeup")
        self._Branch = params.get("Branch")
        self._Value = params.get("Value")
        self._IsNum = params.get("IsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDevicePropertyResponse(AbstractModel):
    """ModifyDeviceProperty返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备ID
        :type Tid: str
        :param _AccessId: 用户ID
        :type AccessId: str
        :param _Nick: 设备昵称，最多不超过64个字符
        :type Nick: str
        """
        self._Tid = None
        self._AccessId = None
        self._Nick = None

    @property
    def Tid(self):
        """设备ID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def AccessId(self):
        """用户ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def Nick(self):
        """设备昵称，最多不超过64个字符
        :rtype: str
        """
        return self._Nick

    @Nick.setter
    def Nick(self, Nick):
        self._Nick = Nick


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._AccessId = params.get("AccessId")
        self._Nick = params.get("Nick")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ProductDescription: 产品描述
        :type ProductDescription: str
        :param _ChipManufactureId: 主芯片产商ID
        :type ChipManufactureId: str
        :param _ChipId: 主芯片ID
        :type ChipId: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductDescription = None
        self._ChipManufactureId = None
        self._ChipId = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductDescription(self):
        """产品描述
        :rtype: str
        """
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def ChipManufactureId(self):
        """主芯片产商ID
        :rtype: str
        """
        return self._ChipManufactureId

    @ChipManufactureId.setter
    def ChipManufactureId(self, ChipManufactureId):
        self._ChipManufactureId = ChipManufactureId

    @property
    def ChipId(self):
        """主芯片ID
        :rtype: str
        """
        return self._ChipId

    @ChipId.setter
    def ChipId(self, ChipId):
        self._ChipId = ChipId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._ProductDescription = params.get("ProductDescription")
        self._ChipManufactureId = params.get("ChipManufactureId")
        self._ChipId = params.get("ChipId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyVerContentRequest(AbstractModel):
    """ModifyVerContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: str
        :param _OtaVersion: 需要修改的版本号
        :type OtaVersion: str
        :param _Operator: 操作人,字符长度<=64
        :type Operator: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _Contents: 版本发布的描述信息，需要国际化，可以为空
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        self._ProductId = None
        self._OtaVersion = None
        self._Operator = None
        self._Remark = None
        self._Contents = None

    @property
    def ProductId(self):
        """产品id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """需要修改的版本号
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def Operator(self):
        """操作人,字符长度<=64
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Contents(self):
        """版本发布的描述信息，需要国际化，可以为空
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._Operator = params.get("Operator")
        self._Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self._Contents = Contents()
            self._Contents._deserialize(params.get("Contents"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVerContentResponse(AbstractModel):
    """ModifyVerContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class MsgQueueData(AbstractModel):
    """产品转发消息队列配置

    """

    def __init__(self):
        r"""
        :param _MsgQueueType: 消息队列类型 1：CMQ 2：kafka
        :type MsgQueueType: int
        :param _MsgType: 消息类型列表，整型值（0-31）之间以“,”分隔
        :type MsgType: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Instance: 实例名称
        :type Instance: str
        :param _MsgRegion: 消息地域
        :type MsgRegion: str
        """
        self._MsgQueueType = None
        self._MsgType = None
        self._Topic = None
        self._Instance = None
        self._MsgRegion = None

    @property
    def MsgQueueType(self):
        """消息队列类型 1：CMQ 2：kafka
        :rtype: int
        """
        return self._MsgQueueType

    @MsgQueueType.setter
    def MsgQueueType(self, MsgQueueType):
        self._MsgQueueType = MsgQueueType

    @property
    def MsgType(self):
        """消息类型列表，整型值（0-31）之间以“,”分隔
        :rtype: str
        """
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Instance(self):
        """实例名称
        :rtype: str
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def MsgRegion(self):
        """消息地域
        :rtype: str
        """
        return self._MsgRegion

    @MsgRegion.setter
    def MsgRegion(self, MsgRegion):
        self._MsgRegion = MsgRegion


    def _deserialize(self, params):
        self._MsgQueueType = params.get("MsgQueueType")
        self._MsgType = params.get("MsgType")
        self._Topic = params.get("Topic")
        self._Instance = params.get("Instance")
        self._MsgRegion = params.get("MsgRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsData(AbstractModel):
    """操作系统信息

    """

    def __init__(self):
        r"""
        :param _ChipId: 芯片型号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipId: str
        :param _ChipManufacture: 芯片厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipManufacture: str
        """
        self._ChipId = None
        self._ChipManufacture = None

    @property
    def ChipId(self):
        """芯片型号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChipId

    @ChipId.setter
    def ChipId(self, ChipId):
        self._ChipId = ChipId

    @property
    def ChipManufacture(self):
        """芯片厂商
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChipManufacture

    @ChipManufacture.setter
    def ChipManufacture(self, ChipManufacture):
        self._ChipManufacture = ChipManufacture


    def _deserialize(self, params):
        self._ChipId = params.get("ChipId")
        self._ChipManufacture = params.get("ChipManufacture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OtaPubHistory(AbstractModel):
    """产品发布过的全部版本

    """

    def __init__(self):
        r"""
        :param _OtaVersion: 版本名称
        :type OtaVersion: str
        :param _PublishTime: 发布时间，unix时间戳，单位：秒
        :type PublishTime: int
        """
        self._OtaVersion = None
        self._PublishTime = None

    @property
    def OtaVersion(self):
        """版本名称
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def PublishTime(self):
        """发布时间，unix时间戳，单位：秒
        :rtype: int
        """
        return self._PublishTime

    @PublishTime.setter
    def PublishTime(self, PublishTime):
        self._PublishTime = PublishTime


    def _deserialize(self, params):
        self._OtaVersion = params.get("OtaVersion")
        self._PublishTime = params.get("PublishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductBase(AbstractModel):
    """产品信息摘要

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductModel: 产器型号(APP产品,为APP包名)
        :type ProductModel: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param _CreateTime: 创建时间，UNIX 时间戳，单位秒
        :type CreateTime: int
        :param _IotModelRevision: 物模型发布版本号,0代表物模型尚未发布
        :type IotModelRevision: int
        :param _SecretKey: 产品密钥
        :type SecretKey: str
        :param _FuncCode: 设备功能码
ypsxth : 音频双向通话;	
spdxth : 视频单向通话(监控);
NVR0824 : NVR设备,大于8路，小于等于24路;
WifiKeepalive : Wifi保活(低功耗产品);
Alexa : Alexa接入;
Google : Google接入;
注意：此字段可能返回 null，表示取不到有效值。
        :type FuncCode: list of str
        :param _ProductCate: 产品类别，0 : 普通视频设备；1 : NVR设备
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCate: int
        :param _ProductRegion: 产品地域
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
Other-Overseas（其他境外地区）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductRegion: str
        """
        self._ProductId = None
        self._ProductModel = None
        self._ProductName = None
        self._ProductDescription = None
        self._CreateTime = None
        self._IotModelRevision = None
        self._SecretKey = None
        self._FuncCode = None
        self._ProductCate = None
        self._ProductRegion = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductModel(self):
        """产器型号(APP产品,为APP包名)
        :rtype: str
        """
        return self._ProductModel

    @ProductModel.setter
    def ProductModel(self, ProductModel):
        self._ProductModel = ProductModel

    @property
    def ProductName(self):
        """产品名称
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductDescription(self):
        """产品描述信息
        :rtype: str
        """
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def CreateTime(self):
        """创建时间，UNIX 时间戳，单位秒
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IotModelRevision(self):
        """物模型发布版本号,0代表物模型尚未发布
        :rtype: int
        """
        return self._IotModelRevision

    @IotModelRevision.setter
    def IotModelRevision(self, IotModelRevision):
        self._IotModelRevision = IotModelRevision

    @property
    def SecretKey(self):
        """产品密钥
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FuncCode(self):
        """设备功能码
ypsxth : 音频双向通话;	
spdxth : 视频单向通话(监控);
NVR0824 : NVR设备,大于8路，小于等于24路;
WifiKeepalive : Wifi保活(低功耗产品);
Alexa : Alexa接入;
Google : Google接入;
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FuncCode

    @FuncCode.setter
    def FuncCode(self, FuncCode):
        self._FuncCode = FuncCode

    @property
    def ProductCate(self):
        """产品类别，0 : 普通视频设备；1 : NVR设备
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProductCate

    @ProductCate.setter
    def ProductCate(self, ProductCate):
        self._ProductCate = ProductCate

    @property
    def ProductRegion(self):
        """产品地域
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
Other-Overseas（其他境外地区）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductRegion

    @ProductRegion.setter
    def ProductRegion(self, ProductRegion):
        self._ProductRegion = ProductRegion


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductModel = params.get("ProductModel")
        self._ProductName = params.get("ProductName")
        self._ProductDescription = params.get("ProductDescription")
        self._CreateTime = params.get("CreateTime")
        self._IotModelRevision = params.get("IotModelRevision")
        self._SecretKey = params.get("SecretKey")
        self._FuncCode = params.get("FuncCode")
        self._ProductCate = params.get("ProductCate")
        self._ProductRegion = params.get("ProductRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductData(AbstractModel):
    """产品信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _ProductDescription: 产品描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductDescription: str
        :param _CreateTime: 创建时间，UNIX 时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _IotModelRevision: 物模型发布版本号,0代表物模型尚未发布
注意：此字段可能返回 null，表示取不到有效值。
        :type IotModelRevision: int
        :param _SecretKey: 产品密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _Features: 设备功能码
注意：此字段可能返回 null，表示取不到有效值。
        :type Features: list of str
        :param _ProductModel: 产器型号(APP产品,为APP包名)
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductModel: str
        :param _ChipManufactureId: 主芯片厂商id
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipManufactureId: str
        :param _ChipId: 主芯片型号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipId: str
        :param _ProductCate: 产品类别，0：普通视频设备；1：NVR设备
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCate: int
        :param _ProductRegion: 产品地区
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
India（印度）
Other-Overseas（其他境外地区）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductRegion: str
        :param _AccessMode: 接入模型，bit0是0：公版小程序未接入，bit0是1：公版小程序已接入
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessMode: int
        :param _Os: linux,android,liteos
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductDescription = None
        self._CreateTime = None
        self._IotModelRevision = None
        self._SecretKey = None
        self._Features = None
        self._ProductModel = None
        self._ChipManufactureId = None
        self._ChipId = None
        self._ProductCate = None
        self._ProductRegion = None
        self._AccessMode = None
        self._Os = None

    @property
    def ProductId(self):
        """产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        """产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductDescription(self):
        """产品描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def CreateTime(self):
        """创建时间，UNIX 时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IotModelRevision(self):
        """物模型发布版本号,0代表物模型尚未发布
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IotModelRevision

    @IotModelRevision.setter
    def IotModelRevision(self, IotModelRevision):
        self._IotModelRevision = IotModelRevision

    @property
    def SecretKey(self):
        """产品密钥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Features(self):
        """设备功能码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def ProductModel(self):
        """产器型号(APP产品,为APP包名)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductModel

    @ProductModel.setter
    def ProductModel(self, ProductModel):
        self._ProductModel = ProductModel

    @property
    def ChipManufactureId(self):
        """主芯片厂商id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChipManufactureId

    @ChipManufactureId.setter
    def ChipManufactureId(self, ChipManufactureId):
        self._ChipManufactureId = ChipManufactureId

    @property
    def ChipId(self):
        """主芯片型号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChipId

    @ChipId.setter
    def ChipId(self, ChipId):
        self._ChipId = ChipId

    @property
    def ProductCate(self):
        """产品类别，0：普通视频设备；1：NVR设备
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProductCate

    @ProductCate.setter
    def ProductCate(self, ProductCate):
        self._ProductCate = ProductCate

    @property
    def ProductRegion(self):
        """产品地区
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
India（印度）
Other-Overseas（其他境外地区）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductRegion

    @ProductRegion.setter
    def ProductRegion(self, ProductRegion):
        self._ProductRegion = ProductRegion

    @property
    def AccessMode(self):
        """接入模型，bit0是0：公版小程序未接入，bit0是1：公版小程序已接入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def Os(self):
        """linux,android,liteos
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._ProductDescription = params.get("ProductDescription")
        self._CreateTime = params.get("CreateTime")
        self._IotModelRevision = params.get("IotModelRevision")
        self._SecretKey = params.get("SecretKey")
        self._Features = params.get("Features")
        self._ProductModel = params.get("ProductModel")
        self._ChipManufactureId = params.get("ChipManufactureId")
        self._ChipId = params.get("ChipId")
        self._ProductCate = params.get("ProductCate")
        self._ProductRegion = params.get("ProductRegion")
        self._AccessMode = params.get("AccessMode")
        self._Os = params.get("Os")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeRecord(AbstractModel):
    """充值记录列表

    """

    def __init__(self):
        r"""
        :param _WaterId: 流水记录号。
注意：此字段可能返回 null，表示取不到有效值。
        :type WaterId: int
        :param _BalanceBeforeRecharge: 充值前的余额，单位0.01元。
注意：此字段可能返回 null，表示取不到有效值。
        :type BalanceBeforeRecharge: int
        :param _Money: 充值金额，单位0.01元。
注意：此字段可能返回 null，表示取不到有效值。
        :type Money: int
        :param _OperateTime: 充值时间, UTC值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateTime: int
        """
        self._WaterId = None
        self._BalanceBeforeRecharge = None
        self._Money = None
        self._OperateTime = None

    @property
    def WaterId(self):
        """流水记录号。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WaterId

    @WaterId.setter
    def WaterId(self, WaterId):
        self._WaterId = WaterId

    @property
    def BalanceBeforeRecharge(self):
        """充值前的余额，单位0.01元。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BalanceBeforeRecharge

    @BalanceBeforeRecharge.setter
    def BalanceBeforeRecharge(self, BalanceBeforeRecharge):
        self._BalanceBeforeRecharge = BalanceBeforeRecharge

    @property
    def Money(self):
        """充值金额，单位0.01元。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Money

    @Money.setter
    def Money(self, Money):
        self._Money = Money

    @property
    def OperateTime(self):
        """充值时间, UTC值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OperateTime

    @OperateTime.setter
    def OperateTime(self, OperateTime):
        self._OperateTime = OperateTime


    def _deserialize(self, params):
        self._WaterId = params.get("WaterId")
        self._BalanceBeforeRecharge = params.get("BalanceBeforeRecharge")
        self._Money = params.get("Money")
        self._OperateTime = params.get("OperateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundStorageServiceRequest(AbstractModel):
    """RefundStorageService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 云存服务ID
        :type ServiceId: str
        :param _OrderId: 云存子订单ID。如果指定子订单ID,则仅退订该子订单，如果未指定子定单ID，则退订所有子订单
        :type OrderId: str
        """
        self._ServiceId = None
        self._OrderId = None

    @property
    def ServiceId(self):
        """云存服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def OrderId(self):
        """云存子订单ID。如果指定子订单ID,则仅退订该子订单，如果未指定子定单ID，则退订所有子订单
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundStorageServiceResponse(AbstractModel):
    """RefundStorageService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 云存服务ID
        :type ServiceId: str
        :param _StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param _AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param _StartTime: 服务开始时间
        :type StartTime: int
        :param _EndTime: 服务失效时间
        :type EndTime: int
        :param _Status: 服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :type Status: int
        :param _Data: 有效云存定单列表
        :type Data: list of StorageOrder
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._StorageRegion = None
        self._Tid = None
        self._ChnNum = None
        self._AccessId = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Data = None
        self._RequestId = None

    @property
    def ServiceId(self):
        """云存服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StorageRegion(self):
        """云存服务所在的区域
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def ChnNum(self):
        """视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :rtype: int
        """
        return self._ChnNum

    @ChnNum.setter
    def ChnNum(self, ChnNum):
        self._ChnNum = ChnNum

    @property
    def AccessId(self):
        """终端用户在IoT Video平台的注册ID
        :rtype: str
        """
        return self._AccessId

    @AccessId.setter
    def AccessId(self, AccessId):
        self._AccessId = AccessId

    @property
    def StartTime(self):
        """服务开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """服务失效时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """服务状态
1：正常使用中
2：待续费。设备云存服务已到期，但是历史云存数据未过期。续费后仍可查看这些历史数据。
3：已过期。查询不到设备保存在云端的数据。
4：等待服务生效。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Data(self):
        """有效云存定单列表
        :rtype: list of StorageOrder
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._ServiceId = params.get("ServiceId")
        self._StorageRegion = params.get("StorageRegion")
        self._Tid = params.get("Tid")
        self._ChnNum = params.get("ChnNum")
        self._AccessId = params.get("AccessId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class RegisteredStatus(AbstractModel):
    """终端用户注册状态

    """

    def __init__(self):
        r"""
        :param _CunionId: 终端用户的唯一ID
        :type CunionId: str
        :param _IsRegisted: 注册状态
        :type IsRegisted: bool
        """
        self._CunionId = None
        self._IsRegisted = None

    @property
    def CunionId(self):
        """终端用户的唯一ID
        :rtype: str
        """
        return self._CunionId

    @CunionId.setter
    def CunionId(self, CunionId):
        self._CunionId = CunionId

    @property
    def IsRegisted(self):
        """注册状态
        :rtype: bool
        """
        return self._IsRegisted

    @IsRegisted.setter
    def IsRegisted(self, IsRegisted):
        self._IsRegisted = IsRegisted


    def _deserialize(self, params):
        self._CunionId = params.get("CunionId")
        self._IsRegisted = params.get("IsRegisted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewCertificate(AbstractModel):
    """刷新证书信息

    """

    def __init__(self):
        r"""
        :param _TempCertificate: 刷新证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TempCertificate: :class:`tencentcloud.iotvideo.v20191126.models.CertificateInfo`
        """
        self._TempCertificate = None

    @property
    def TempCertificate(self):
        """刷新证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CertificateInfo`
        """
        return self._TempCertificate

    @TempCertificate.setter
    def TempCertificate(self, TempCertificate):
        self._TempCertificate = TempCertificate


    def _deserialize(self, params):
        if params.get("TempCertificate") is not None:
            self._TempCertificate = CertificateInfo()
            self._TempCertificate._deserialize(params.get("TempCertificate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewUploadTestRequest(AbstractModel):
    """RenewUploadTest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PkgId: package ID
        :type PkgId: str
        :param _Tid: 设备TID
        :type Tid: str
        :param _SessionKey: SessionKeys
        :type SessionKey: str
        """
        self._PkgId = None
        self._Tid = None
        self._SessionKey = None

    @property
    def PkgId(self):
        """package ID
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def SessionKey(self):
        """SessionKeys
        :rtype: str
        """
        return self._SessionKey

    @SessionKey.setter
    def SessionKey(self, SessionKey):
        self._SessionKey = SessionKey


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        self._Tid = params.get("Tid")
        self._SessionKey = params.get("SessionKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewUploadTestResponse(AbstractModel):
    """RenewUploadTest返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 刷新证书返回的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.RenewCertificate`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """刷新证书返回的信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RenewCertificate`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RenewCertificate()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RunDeviceRequest(AbstractModel):
    """RunDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: TID列表 ≤100
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """TID列表 ≤100
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunDeviceResponse(AbstractModel):
    """RunDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RunDeviceStreamRequest(AbstractModel):
    """RunDeviceStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tids: 设备TID 列表
        :type Tids: list of str
        """
        self._Tids = None

    @property
    def Tids(self):
        """设备TID 列表
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids


    def _deserialize(self, params):
        self._Tids = params.get("Tids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunDeviceStreamResponse(AbstractModel):
    """RunDeviceStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RunIotModelRequest(AbstractModel):
    """RunIotModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _IotModel: 物模型定义，json格式的字符串
        :type IotModel: str
        """
        self._ProductId = None
        self._IotModel = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def IotModel(self):
        """物模型定义，json格式的字符串
        :rtype: str
        """
        return self._IotModel

    @IotModel.setter
    def IotModel(self, IotModel):
        self._IotModel = IotModel


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._IotModel = params.get("IotModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunIotModelResponse(AbstractModel):
    """RunIotModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RunOtaVersionRequest(AbstractModel):
    """RunOtaVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param _GrayValue: 灰度值,取值范围0-100，为0时相当于暂停发布
        :type GrayValue: int
        :param _OldVersions: 指定的旧版本
        :type OldVersions: list of str
        :param _Operator: 操作人
        :type Operator: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _Contents: 版本发布的描述信息，需要国际化，可以为空
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        self._ProductId = None
        self._OtaVersion = None
        self._GrayValue = None
        self._OldVersions = None
        self._Operator = None
        self._Remark = None
        self._Contents = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def GrayValue(self):
        """灰度值,取值范围0-100，为0时相当于暂停发布
        :rtype: int
        """
        return self._GrayValue

    @GrayValue.setter
    def GrayValue(self, GrayValue):
        self._GrayValue = GrayValue

    @property
    def OldVersions(self):
        """指定的旧版本
        :rtype: list of str
        """
        return self._OldVersions

    @OldVersions.setter
    def OldVersions(self, OldVersions):
        self._OldVersions = OldVersions

    @property
    def Operator(self):
        """操作人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Contents(self):
        """版本发布的描述信息，需要国际化，可以为空
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._GrayValue = params.get("GrayValue")
        self._OldVersions = params.get("OldVersions")
        self._Operator = params.get("Operator")
        self._Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self._Contents = Contents()
            self._Contents._deserialize(params.get("Contents"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunOtaVersionResponse(AbstractModel):
    """RunOtaVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RunTestOtaVersionRequest(AbstractModel):
    """RunTestOtaVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param _Tids: 指定可升级的设备TID
        :type Tids: list of str
        :param _Operator: 操作人
        :type Operator: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._ProductId = None
        self._OtaVersion = None
        self._Tids = None
        self._Operator = None
        self._Remark = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def Tids(self):
        """指定可升级的设备TID
        :rtype: list of str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids

    @property
    def Operator(self):
        """操作人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._Tids = params.get("Tids")
        self._Operator = params.get("Operator")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunTestOtaVersionResponse(AbstractModel):
    """RunTestOtaVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class SendOnlineMsgRequest(AbstractModel):
    """SendOnlineMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _Wakeup: 如果设备处于休眠状态，是否唤醒设备
        :type Wakeup: bool
        :param _WaitResp: 等待回应类型
0：不等待设备回应直接响应请求;
1：要求设备确认消息已接收,或等待超时后返回;
2：要求设备进行响应处理,收到设备的响应数据后,将设备响应数据回应给请求方;
        :type WaitResp: int
        :param _MsgTopic: 消息主题
        :type MsgTopic: str
        :param _MsgContent: 消息内容，最大长度不超过8k字节
        :type MsgContent: str
        """
        self._Tid = None
        self._Wakeup = None
        self._WaitResp = None
        self._MsgTopic = None
        self._MsgContent = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def Wakeup(self):
        """如果设备处于休眠状态，是否唤醒设备
        :rtype: bool
        """
        return self._Wakeup

    @Wakeup.setter
    def Wakeup(self, Wakeup):
        self._Wakeup = Wakeup

    @property
    def WaitResp(self):
        """等待回应类型
0：不等待设备回应直接响应请求;
1：要求设备确认消息已接收,或等待超时后返回;
2：要求设备进行响应处理,收到设备的响应数据后,将设备响应数据回应给请求方;
        :rtype: int
        """
        return self._WaitResp

    @WaitResp.setter
    def WaitResp(self, WaitResp):
        self._WaitResp = WaitResp

    @property
    def MsgTopic(self):
        """消息主题
        :rtype: str
        """
        return self._MsgTopic

    @MsgTopic.setter
    def MsgTopic(self, MsgTopic):
        self._MsgTopic = MsgTopic

    @property
    def MsgContent(self):
        """消息内容，最大长度不超过8k字节
        :rtype: str
        """
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._Wakeup = params.get("Wakeup")
        self._WaitResp = params.get("WaitResp")
        self._MsgTopic = params.get("MsgTopic")
        self._MsgContent = params.get("MsgContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendOnlineMsgResponse(AbstractModel):
    """SendOnlineMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 若返回此项则表明需要用户用此taskID进行查询请求是否成功(只有waitresp不等于0的情况下才可能会返回该taskID项)
        :type TaskId: str
        :param _Data: 设备响应信息
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Data = None
        self._RequestId = None

    @property
    def TaskId(self):
        """若返回此项则表明需要用户用此taskID进行查询请求是否成功(只有waitresp不等于0的情况下才可能会返回该taskID项)
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Data(self):
        """设备响应信息
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._TaskId = params.get("TaskId")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class SetMessageQueueRequest(AbstractModel):
    """SetMessageQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _MsgQueueType: 消息队列类型 1-CMQ; 2-Ckafka
        :type MsgQueueType: int
        :param _MsgType: 消息类型,整型值（0-31）之间以“,”分隔
0.设备在线状态变更
1.常亮属性(ProConst)变更
2.可写属性(ProWritable)变更
3.只读属性(ProReadonly)变更
4.设备控制(Action)
5.设备事件(Event)
6.系统事件(System)
        :type MsgType: str
        :param _Topic: 消息队列主题，不超过32字符
        :type Topic: str
        :param _Instance: kafka消息队列的实例名，不超过64字符
        :type Instance: str
        :param _MsgRegion: 消息地域，不超过32字符
        :type MsgRegion: str
        """
        self._ProductId = None
        self._MsgQueueType = None
        self._MsgType = None
        self._Topic = None
        self._Instance = None
        self._MsgRegion = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def MsgQueueType(self):
        """消息队列类型 1-CMQ; 2-Ckafka
        :rtype: int
        """
        return self._MsgQueueType

    @MsgQueueType.setter
    def MsgQueueType(self, MsgQueueType):
        self._MsgQueueType = MsgQueueType

    @property
    def MsgType(self):
        """消息类型,整型值（0-31）之间以“,”分隔
0.设备在线状态变更
1.常亮属性(ProConst)变更
2.可写属性(ProWritable)变更
3.只读属性(ProReadonly)变更
4.设备控制(Action)
5.设备事件(Event)
6.系统事件(System)
        :rtype: str
        """
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def Topic(self):
        """消息队列主题，不超过32字符
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Instance(self):
        """kafka消息队列的实例名，不超过64字符
        :rtype: str
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

    @property
    def MsgRegion(self):
        """消息地域，不超过32字符
        :rtype: str
        """
        return self._MsgRegion

    @MsgRegion.setter
    def MsgRegion(self, MsgRegion):
        self._MsgRegion = MsgRegion


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._MsgQueueType = params.get("MsgQueueType")
        self._MsgType = params.get("MsgType")
        self._Topic = params.get("Topic")
        self._Instance = params.get("Instance")
        self._MsgRegion = params.get("MsgRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetMessageQueueResponse(AbstractModel):
    """SetMessageQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StorageOrder(AbstractModel):
    """云存订单信息

    """

    def __init__(self):
        r"""
        :param _OrderId: 定单唯一性ID
        :type OrderId: str
        :param _PkgId: 云存套餐ID
        :type PkgId: str
        :param _Status: 定单服务状态
1;订单正在使用。
2:订单未开始。
3:订单已经使用过，现在暂时未开始使用(该订单从其他服务转移而来)。
4:订单已过期。
5:订单已被退订。
6:定单已被转移到其他云存服务。
        :type Status: int
        :param _StartTime: 定单服务生效时间
        :type StartTime: int
        :param _EndTime: 定单服务失效时间
        :type EndTime: int
        """
        self._OrderId = None
        self._PkgId = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None

    @property
    def OrderId(self):
        """定单唯一性ID
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PkgId(self):
        """云存套餐ID
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def Status(self):
        """定单服务状态
1;订单正在使用。
2:订单未开始。
3:订单已经使用过，现在暂时未开始使用(该订单从其他服务转移而来)。
4:订单已过期。
5:订单已被退订。
6:定单已被转移到其他云存服务。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        """定单服务生效时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """定单服务失效时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._PkgId = params.get("PkgId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemType(AbstractModel):
    """系统类型

    """

    def __init__(self):
        r"""
        :param _Android: 安卓系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Android: list of OsData
        :param _Linux: linux系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Linux: list of OsData
        :param _LiteOs: LiteOs系统
注意：此字段可能返回 null，表示取不到有效值。
        :type LiteOs: list of OsData
        """
        self._Android = None
        self._Linux = None
        self._LiteOs = None

    @property
    def Android(self):
        """安卓系统
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OsData
        """
        return self._Android

    @Android.setter
    def Android(self, Android):
        self._Android = Android

    @property
    def Linux(self):
        """linux系统
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OsData
        """
        return self._Linux

    @Linux.setter
    def Linux(self, Linux):
        self._Linux = Linux

    @property
    def LiteOs(self):
        """LiteOs系统
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OsData
        """
        return self._LiteOs

    @LiteOs.setter
    def LiteOs(self, LiteOs):
        self._LiteOs = LiteOs


    def _deserialize(self, params):
        if params.get("Android") is not None:
            self._Android = []
            for item in params.get("Android"):
                obj = OsData()
                obj._deserialize(item)
                self._Android.append(obj)
        if params.get("Linux") is not None:
            self._Linux = []
            for item in params.get("Linux"):
                obj = OsData()
                obj._deserialize(item)
                self._Linux.append(obj)
        if params.get("LiteOs") is not None:
            self._LiteOs = []
            for item in params.get("LiteOs"):
                obj = OsData()
                obj._deserialize(item)
                self._LiteOs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TraceStatus(AbstractModel):
    """布尔值，标识指定设备是否在白名单中

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _IsExist: 设备追踪状态
        :type IsExist: bool
        """
        self._Tid = None
        self._IsExist = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def IsExist(self):
        """设备追踪状态
        :rtype: bool
        """
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._IsExist = params.get("IsExist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDeviceRequest(AbstractModel):
    """UpgradeDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tid: 设备TID
        :type Tid: str
        :param _OtaVersion: 固件版本号
        :type OtaVersion: str
        :param _UpgradeNow: 是否立即升级
        :type UpgradeNow: bool
        """
        self._Tid = None
        self._OtaVersion = None
        self._UpgradeNow = None

    @property
    def Tid(self):
        """设备TID
        :rtype: str
        """
        return self._Tid

    @Tid.setter
    def Tid(self, Tid):
        self._Tid = Tid

    @property
    def OtaVersion(self):
        """固件版本号
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def UpgradeNow(self):
        """是否立即升级
        :rtype: bool
        """
        return self._UpgradeNow

    @UpgradeNow.setter
    def UpgradeNow(self, UpgradeNow):
        self._UpgradeNow = UpgradeNow


    def _deserialize(self, params):
        self._Tid = params.get("Tid")
        self._OtaVersion = params.get("OtaVersion")
        self._UpgradeNow = params.get("UpgradeNow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeDeviceResponse(AbstractModel):
    """UpgradeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备端返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """设备端返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class UploadOtaVersionRequest(AbstractModel):
    """UploadOtaVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param _VersionUrl: 固件版本URL
        :type VersionUrl: str
        :param _FileSize: 文件大小，单位：byte
        :type FileSize: int
        :param _Md5: 文件md5校验码（32字符）
        :type Md5: str
        :param _Operator: 操作人
        :type Operator: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _Contents: 版本发布的描述信息，需要国际化，可以为空
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        self._ProductId = None
        self._OtaVersion = None
        self._VersionUrl = None
        self._FileSize = None
        self._Md5 = None
        self._Operator = None
        self._Remark = None
        self._Contents = None

    @property
    def ProductId(self):
        """产品ID
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def VersionUrl(self):
        """固件版本URL
        :rtype: str
        """
        return self._VersionUrl

    @VersionUrl.setter
    def VersionUrl(self, VersionUrl):
        self._VersionUrl = VersionUrl

    @property
    def FileSize(self):
        """文件大小，单位：byte
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Md5(self):
        """文件md5校验码（32字符）
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def Operator(self):
        """操作人
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Contents(self):
        """版本发布的描述信息，需要国际化，可以为空
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._VersionUrl = params.get("VersionUrl")
        self._FileSize = params.get("FileSize")
        self._Md5 = params.get("Md5")
        self._Operator = params.get("Operator")
        self._Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self._Contents = Contents()
            self._Contents._deserialize(params.get("Contents"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadOtaVersionResponse(AbstractModel):
    """UploadOtaVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class VersionData(AbstractModel):
    """固件版本详细信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _OtaVersion: 固件版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OtaVersion: str
        :param _PubStatus: 版本类型 1未发布 2测试发布 3正式发布 4禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type PubStatus: int
        :param _VersionUrl: 固件版本存储路径URL
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionUrl: str
        :param _FileSize: 文件大小，byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param _Md5: 文件校验码
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param _OldVersions: 指定的允许升级的旧版本，PubStatus=3时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type OldVersions: str
        :param _Tids: 指定的允许升级的旧设备id，PubStatus=2时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Tids: str
        :param _GrayValue: 灰度值（0-100）,PubStatus=3时有效，表示n%的升级总量
注意：此字段可能返回 null，表示取不到有效值。
        :type GrayValue: int
        :param _PublishTime: 最近一次发布时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishTime: int
        :param _ActiveCount: 此版本激活的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveCount: int
        :param _OnlineCount: 此版本在线的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineCount: int
        :param _UpdateTime: 上传固件文件的时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _UploadTime: 发布记录的最后变更时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadTime: int
        :param _ModifyTimes: 该固件版本发布的变更次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTimes: int
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _Contents: 版本发布的描述信息，需要国际化，可以为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        :param _AliveInMonthCnt: 月活设备数，当月第一天开始有上线的设备数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type AliveInMonthCnt: int
        """
        self._ProductId = None
        self._OtaVersion = None
        self._PubStatus = None
        self._VersionUrl = None
        self._FileSize = None
        self._Md5 = None
        self._OldVersions = None
        self._Tids = None
        self._GrayValue = None
        self._PublishTime = None
        self._ActiveCount = None
        self._OnlineCount = None
        self._UpdateTime = None
        self._UploadTime = None
        self._ModifyTimes = None
        self._Remark = None
        self._Contents = None
        self._AliveInMonthCnt = None

    @property
    def ProductId(self):
        """产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OtaVersion(self):
        """固件版本号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OtaVersion

    @OtaVersion.setter
    def OtaVersion(self, OtaVersion):
        self._OtaVersion = OtaVersion

    @property
    def PubStatus(self):
        """版本类型 1未发布 2测试发布 3正式发布 4禁用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PubStatus

    @PubStatus.setter
    def PubStatus(self, PubStatus):
        self._PubStatus = PubStatus

    @property
    def VersionUrl(self):
        """固件版本存储路径URL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionUrl

    @VersionUrl.setter
    def VersionUrl(self, VersionUrl):
        self._VersionUrl = VersionUrl

    @property
    def FileSize(self):
        """文件大小，byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Md5(self):
        """文件校验码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def OldVersions(self):
        """指定的允许升级的旧版本，PubStatus=3时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OldVersions

    @OldVersions.setter
    def OldVersions(self, OldVersions):
        self._OldVersions = OldVersions

    @property
    def Tids(self):
        """指定的允许升级的旧设备id，PubStatus=2时有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Tids

    @Tids.setter
    def Tids(self, Tids):
        self._Tids = Tids

    @property
    def GrayValue(self):
        """灰度值（0-100）,PubStatus=3时有效，表示n%的升级总量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._GrayValue

    @GrayValue.setter
    def GrayValue(self, GrayValue):
        self._GrayValue = GrayValue

    @property
    def PublishTime(self):
        """最近一次发布时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PublishTime

    @PublishTime.setter
    def PublishTime(self, PublishTime):
        self._PublishTime = PublishTime

    @property
    def ActiveCount(self):
        """此版本激活的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ActiveCount

    @ActiveCount.setter
    def ActiveCount(self, ActiveCount):
        self._ActiveCount = ActiveCount

    @property
    def OnlineCount(self):
        """此版本在线的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OnlineCount

    @OnlineCount.setter
    def OnlineCount(self, OnlineCount):
        self._OnlineCount = OnlineCount

    @property
    def UpdateTime(self):
        """上传固件文件的时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def UploadTime(self):
        """发布记录的最后变更时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UploadTime

    @UploadTime.setter
    def UploadTime(self, UploadTime):
        self._UploadTime = UploadTime

    @property
    def ModifyTimes(self):
        """该固件版本发布的变更次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ModifyTimes

    @ModifyTimes.setter
    def ModifyTimes(self, ModifyTimes):
        self._ModifyTimes = ModifyTimes

    @property
    def Remark(self):
        """备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Contents(self):
        """版本发布的描述信息，需要国际化，可以为空
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def AliveInMonthCnt(self):
        """月活设备数，当月第一天开始有上线的设备数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AliveInMonthCnt

    @AliveInMonthCnt.setter
    def AliveInMonthCnt(self, AliveInMonthCnt):
        self._AliveInMonthCnt = AliveInMonthCnt


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._OtaVersion = params.get("OtaVersion")
        self._PubStatus = params.get("PubStatus")
        self._VersionUrl = params.get("VersionUrl")
        self._FileSize = params.get("FileSize")
        self._Md5 = params.get("Md5")
        self._OldVersions = params.get("OldVersions")
        self._Tids = params.get("Tids")
        self._GrayValue = params.get("GrayValue")
        self._PublishTime = params.get("PublishTime")
        self._ActiveCount = params.get("ActiveCount")
        self._OnlineCount = params.get("OnlineCount")
        self._UpdateTime = params.get("UpdateTime")
        self._UploadTime = params.get("UploadTime")
        self._ModifyTimes = params.get("ModifyTimes")
        self._Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self._Contents = Contents()
            self._Contents._deserialize(params.get("Contents"))
        self._AliveInMonthCnt = params.get("AliveInMonthCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        