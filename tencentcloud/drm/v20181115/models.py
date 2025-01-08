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


class AddFairPlayPemRequest(AbstractModel):
    """AddFairPlayPem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Pem: 加密后的fairplay方案申请时使用的私钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。
        :type Pem: str
        :param _Ask: 加密后的fairplay方案申请返回的ask数据。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。
        :type Ask: str
        :param _PemDecryptKey: 私钥的解密密钥。
openssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :type PemDecryptKey: str
        :param _BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :type BailorId: int
        :param _Priority: 私钥的优先级，优先级数值越高，优先级越高。
该值可以不传，后台将自动分配一个优先级。
        :type Priority: int
        """
        self._Pem = None
        self._Ask = None
        self._PemDecryptKey = None
        self._BailorId = None
        self._Priority = None

    @property
    def Pem(self):
        """加密后的fairplay方案申请时使用的私钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._Pem

    @Pem.setter
    def Pem(self, Pem):
        self._Pem = Pem

    @property
    def Ask(self):
        """加密后的fairplay方案申请返回的ask数据。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._Ask

    @Ask.setter
    def Ask(self, Ask):
        self._Ask = Ask

    @property
    def PemDecryptKey(self):
        """私钥的解密密钥。
openssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._PemDecryptKey

    @PemDecryptKey.setter
    def PemDecryptKey(self, PemDecryptKey):
        self._PemDecryptKey = PemDecryptKey

    @property
    def BailorId(self):
        """委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :rtype: int
        """
        return self._BailorId

    @BailorId.setter
    def BailorId(self, BailorId):
        self._BailorId = BailorId

    @property
    def Priority(self):
        """私钥的优先级，优先级数值越高，优先级越高。
该值可以不传，后台将自动分配一个优先级。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._Pem = params.get("Pem")
        self._Ask = params.get("Ask")
        self._PemDecryptKey = params.get("PemDecryptKey")
        self._BailorId = params.get("BailorId")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddFairPlayPemResponse(AbstractModel):
    """AddFairPlayPem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FairPlayPemId: 设置私钥后，后台返回的pem id，用来唯一标识一个私钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type FairPlayPemId: int
        :param _Priority: 私钥的优先级，优先级数值越高，优先级越高。
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FairPlayPemId = None
        self._Priority = None
        self._RequestId = None

    @property
    def FairPlayPemId(self):
        """设置私钥后，后台返回的pem id，用来唯一标识一个私钥。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FairPlayPemId

    @FairPlayPemId.setter
    def FairPlayPemId(self, FairPlayPemId):
        self._FairPlayPemId = FairPlayPemId

    @property
    def Priority(self):
        """私钥的优先级，优先级数值越高，优先级越高。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

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
        self._FairPlayPemId = params.get("FairPlayPemId")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class CreateEncryptKeysRequest(AbstractModel):
    """CreateEncryptKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrmType: 使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。
        :type DrmType: str
        :param _Keys: 设置的加密密钥列表。
        :type Keys: list of KeyParam
        :param _ContentId: 一个加密内容的唯一标识。
        :type ContentId: str
        :param _ContentType: 内容类型。接口取值VodVideo,LiveVideo。
        :type ContentType: str
        """
        self._DrmType = None
        self._Keys = None
        self._ContentId = None
        self._ContentType = None

    @property
    def DrmType(self):
        """使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。
        :rtype: str
        """
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType

    @property
    def Keys(self):
        """设置的加密密钥列表。
        :rtype: list of KeyParam
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def ContentId(self):
        """一个加密内容的唯一标识。
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def ContentType(self):
        """内容类型。接口取值VodVideo,LiveVideo。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._DrmType = params.get("DrmType")
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = KeyParam()
                obj._deserialize(item)
                self._Keys.append(obj)
        self._ContentId = params.get("ContentId")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEncryptKeysResponse(AbstractModel):
    """CreateEncryptKeys返回参数结构体

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


class CreateLicenseRequest(AbstractModel):
    """CreateLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrmType: DRM方案类型，接口取值：WIDEVINE，FAIRPLAY。
        :type DrmType: str
        :param _LicenseRequest: Base64编码的终端设备License Request数据。
        :type LicenseRequest: str
        :param _ContentType: 内容类型，接口取值：VodVideo,LiveVideo。
        :type ContentType: str
        :param _Tracks: 授权播放的Track列表。
该值为空时，默认授权所有track播放。
        :type Tracks: list of str
        :param _PlaybackPolicy: 播放策略参数。
        :type PlaybackPolicy: :class:`tencentcloud.drm.v20181115.models.PlaybackPolicy`
        :param _WidevineSecurityLevel: Widevine安全级别，接口取值[L1, L2, L3]。
安全级别定义参考Widevine安全级别定义。
        :type WidevineSecurityLevel: str
        """
        self._DrmType = None
        self._LicenseRequest = None
        self._ContentType = None
        self._Tracks = None
        self._PlaybackPolicy = None
        self._WidevineSecurityLevel = None

    @property
    def DrmType(self):
        """DRM方案类型，接口取值：WIDEVINE，FAIRPLAY。
        :rtype: str
        """
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType

    @property
    def LicenseRequest(self):
        """Base64编码的终端设备License Request数据。
        :rtype: str
        """
        return self._LicenseRequest

    @LicenseRequest.setter
    def LicenseRequest(self, LicenseRequest):
        self._LicenseRequest = LicenseRequest

    @property
    def ContentType(self):
        """内容类型，接口取值：VodVideo,LiveVideo。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Tracks(self):
        """授权播放的Track列表。
该值为空时，默认授权所有track播放。
        :rtype: list of str
        """
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks

    @property
    def PlaybackPolicy(self):
        """播放策略参数。
        :rtype: :class:`tencentcloud.drm.v20181115.models.PlaybackPolicy`
        """
        return self._PlaybackPolicy

    @PlaybackPolicy.setter
    def PlaybackPolicy(self, PlaybackPolicy):
        self._PlaybackPolicy = PlaybackPolicy

    @property
    def WidevineSecurityLevel(self):
        """Widevine安全级别，接口取值[L1, L2, L3]。
安全级别定义参考Widevine安全级别定义。
        :rtype: str
        """
        return self._WidevineSecurityLevel

    @WidevineSecurityLevel.setter
    def WidevineSecurityLevel(self, WidevineSecurityLevel):
        self._WidevineSecurityLevel = WidevineSecurityLevel


    def _deserialize(self, params):
        self._DrmType = params.get("DrmType")
        self._LicenseRequest = params.get("LicenseRequest")
        self._ContentType = params.get("ContentType")
        self._Tracks = params.get("Tracks")
        if params.get("PlaybackPolicy") is not None:
            self._PlaybackPolicy = PlaybackPolicy()
            self._PlaybackPolicy._deserialize(params.get("PlaybackPolicy"))
        self._WidevineSecurityLevel = params.get("WidevineSecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLicenseResponse(AbstractModel):
    """CreateLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _License: Base64 编码的许可证二进制数据。
        :type License: str
        :param _ContentId: 加密内容的内容ID
        :type ContentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._License = None
        self._ContentId = None
        self._RequestId = None

    @property
    def License(self):
        """Base64 编码的许可证二进制数据。
        :rtype: str
        """
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def ContentId(self):
        """加密内容的内容ID
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

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
        self._License = params.get("License")
        self._ContentId = params.get("ContentId")
        self._RequestId = params.get("RequestId")


class DeleteFairPlayPemRequest(AbstractModel):
    """DeleteFairPlayPem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :type BailorId: int
        :param _FairPlayPemId: 要删除的pem id。
当未传入该值时，将删除所有的私钥。
        :type FairPlayPemId: int
        """
        self._BailorId = None
        self._FairPlayPemId = None

    @property
    def BailorId(self):
        """委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :rtype: int
        """
        return self._BailorId

    @BailorId.setter
    def BailorId(self, BailorId):
        self._BailorId = BailorId

    @property
    def FairPlayPemId(self):
        """要删除的pem id。
当未传入该值时，将删除所有的私钥。
        :rtype: int
        """
        return self._FairPlayPemId

    @FairPlayPemId.setter
    def FairPlayPemId(self, FairPlayPemId):
        self._FairPlayPemId = FairPlayPemId


    def _deserialize(self, params):
        self._BailorId = params.get("BailorId")
        self._FairPlayPemId = params.get("FairPlayPemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFairPlayPemResponse(AbstractModel):
    """DeleteFairPlayPem返回参数结构体

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


class DescribeAllKeysRequest(AbstractModel):
    """DescribeAllKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrmType: 使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。
        :type DrmType: str
        :param _RsaPublicKey: Base64编码的Rsa公钥，用来加密出参中的SessionKey。
如果该参数为空，则出参中SessionKey为明文。
        :type RsaPublicKey: str
        :param _ContentId: 一个加密内容的唯一标识。
        :type ContentId: str
        :param _ContentType: 内容类型。接口取值VodVideo,LiveVideo。
        :type ContentType: str
        """
        self._DrmType = None
        self._RsaPublicKey = None
        self._ContentId = None
        self._ContentType = None

    @property
    def DrmType(self):
        """使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。
        :rtype: str
        """
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType

    @property
    def RsaPublicKey(self):
        """Base64编码的Rsa公钥，用来加密出参中的SessionKey。
如果该参数为空，则出参中SessionKey为明文。
        :rtype: str
        """
        return self._RsaPublicKey

    @RsaPublicKey.setter
    def RsaPublicKey(self, RsaPublicKey):
        self._RsaPublicKey = RsaPublicKey

    @property
    def ContentId(self):
        """一个加密内容的唯一标识。
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def ContentType(self):
        """内容类型。接口取值VodVideo,LiveVideo。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._DrmType = params.get("DrmType")
        self._RsaPublicKey = params.get("RsaPublicKey")
        self._ContentId = params.get("ContentId")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllKeysResponse(AbstractModel):
    """DescribeAllKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Keys: 加密密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of Key
        :param _SessionKey: 用来加密密钥。
如果入参中带有RsaPublicKey，则SessionKey为使用Rsa公钥加密后的二进制数据，Base64编码字符串。
如果入参中没有RsaPublicKey，则SessionKey为原始数据的字符串形式。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionKey: str
        :param _ContentId: 内容ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Keys = None
        self._SessionKey = None
        self._ContentId = None
        self._RequestId = None

    @property
    def Keys(self):
        """加密密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Key
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def SessionKey(self):
        """用来加密密钥。
如果入参中带有RsaPublicKey，则SessionKey为使用Rsa公钥加密后的二进制数据，Base64编码字符串。
如果入参中没有RsaPublicKey，则SessionKey为原始数据的字符串形式。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionKey

    @SessionKey.setter
    def SessionKey(self, SessionKey):
        self._SessionKey = SessionKey

    @property
    def ContentId(self):
        """内容ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

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
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self._Keys.append(obj)
        self._SessionKey = params.get("SessionKey")
        self._ContentId = params.get("ContentId")
        self._RequestId = params.get("RequestId")


class DescribeDRMLicenseRequest(AbstractModel):
    """DescribeDRMLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrmType: 使用的DRM方案类型，接口取值 NORMALAES 。
        :type DrmType: str
        :param _Tracks: 加密的track列表，接口取值 SD 。
        :type Tracks: list of str
        :param _ContentId: 一个加密内容的唯一标识。
        :type ContentId: str
        :param _ContentType: 内容类型。接口取值 LiveVideo 。
        :type ContentType: str
        """
        self._DrmType = None
        self._Tracks = None
        self._ContentId = None
        self._ContentType = None

    @property
    def DrmType(self):
        """使用的DRM方案类型，接口取值 NORMALAES 。
        :rtype: str
        """
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType

    @property
    def Tracks(self):
        """加密的track列表，接口取值 SD 。
        :rtype: list of str
        """
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks

    @property
    def ContentId(self):
        """一个加密内容的唯一标识。
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def ContentType(self):
        """内容类型。接口取值 LiveVideo 。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._DrmType = params.get("DrmType")
        self._Tracks = params.get("Tracks")
        self._ContentId = params.get("ContentId")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDRMLicenseResponse(AbstractModel):
    """DescribeDRMLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContentId: 内容ID。
        :type ContentId: str
        :param _TXEncryptionToken: 加密密钥。
        :type TXEncryptionToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ContentId = None
        self._TXEncryptionToken = None
        self._RequestId = None

    @property
    def ContentId(self):
        """内容ID。
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def TXEncryptionToken(self):
        """加密密钥。
        :rtype: str
        """
        return self._TXEncryptionToken

    @TXEncryptionToken.setter
    def TXEncryptionToken(self, TXEncryptionToken):
        self._TXEncryptionToken = TXEncryptionToken

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
        self._ContentId = params.get("ContentId")
        self._TXEncryptionToken = params.get("TXEncryptionToken")
        self._RequestId = params.get("RequestId")


class DescribeFairPlayPemRequest(AbstractModel):
    """DescribeFairPlayPem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :type BailorId: int
        :param _FairPlayPemId: 需要查询的pem id。
当该值未填入时，将返回所有的私钥信息。
        :type FairPlayPemId: int
        """
        self._BailorId = None
        self._FairPlayPemId = None

    @property
    def BailorId(self):
        """委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :rtype: int
        """
        return self._BailorId

    @BailorId.setter
    def BailorId(self, BailorId):
        self._BailorId = BailorId

    @property
    def FairPlayPemId(self):
        """需要查询的pem id。
当该值未填入时，将返回所有的私钥信息。
        :rtype: int
        """
        return self._FairPlayPemId

    @FairPlayPemId.setter
    def FairPlayPemId(self, FairPlayPemId):
        self._FairPlayPemId = FairPlayPemId


    def _deserialize(self, params):
        self._BailorId = params.get("BailorId")
        self._FairPlayPemId = params.get("FairPlayPemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFairPlayPemResponse(AbstractModel):
    """DescribeFairPlayPem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FairPlayPems: 该账户下，所有设置的FairPlay私钥摘要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FairPlayPems: list of FairPlayPemDigestInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FairPlayPems = None
        self._RequestId = None

    @property
    def FairPlayPems(self):
        """该账户下，所有设置的FairPlay私钥摘要信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FairPlayPemDigestInfo
        """
        return self._FairPlayPems

    @FairPlayPems.setter
    def FairPlayPems(self, FairPlayPems):
        self._FairPlayPems = FairPlayPems

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
        if params.get("FairPlayPems") is not None:
            self._FairPlayPems = []
            for item in params.get("FairPlayPems"):
                obj = FairPlayPemDigestInfo()
                obj._deserialize(item)
                self._FairPlayPems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrmType: 使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。
        :type DrmType: str
        :param _Tracks: 加密的track列表，接口取值VIDEO、AUDIO。
        :type Tracks: list of str
        :param _ContentType: 内容类型。接口取值VodVideo,LiveVideo
        :type ContentType: str
        :param _RsaPublicKey: Base64编码的Rsa公钥，用来加密出参中的SessionKey。
如果该参数为空，则出参中SessionKey为明文。
        :type RsaPublicKey: str
        :param _ContentId: 一个加密内容的唯一标识。
如果该参数为空，则后台自动生成
        :type ContentId: str
        """
        self._DrmType = None
        self._Tracks = None
        self._ContentType = None
        self._RsaPublicKey = None
        self._ContentId = None

    @property
    def DrmType(self):
        """使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。
        :rtype: str
        """
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType

    @property
    def Tracks(self):
        """加密的track列表，接口取值VIDEO、AUDIO。
        :rtype: list of str
        """
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks

    @property
    def ContentType(self):
        """内容类型。接口取值VodVideo,LiveVideo
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def RsaPublicKey(self):
        """Base64编码的Rsa公钥，用来加密出参中的SessionKey。
如果该参数为空，则出参中SessionKey为明文。
        :rtype: str
        """
        return self._RsaPublicKey

    @RsaPublicKey.setter
    def RsaPublicKey(self, RsaPublicKey):
        self._RsaPublicKey = RsaPublicKey

    @property
    def ContentId(self):
        """一个加密内容的唯一标识。
如果该参数为空，则后台自动生成
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId


    def _deserialize(self, params):
        self._DrmType = params.get("DrmType")
        self._Tracks = params.get("Tracks")
        self._ContentType = params.get("ContentType")
        self._RsaPublicKey = params.get("RsaPublicKey")
        self._ContentId = params.get("ContentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Keys: 加密密钥列表
        :type Keys: list of Key
        :param _SessionKey: 用来加密密钥。
如果入参中带有RsaPublicKey，则SessionKey为使用Rsa公钥加密后的二进制数据，Base64编码字符串。
如果入参中没有RsaPublicKey，则SessionKey为原始数据的字符串形式。
        :type SessionKey: str
        :param _ContentId: 内容ID
        :type ContentId: str
        :param _Pssh: Widevine方案的Pssh数据，Base64编码。
Fairplay方案无该值。
        :type Pssh: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Keys = None
        self._SessionKey = None
        self._ContentId = None
        self._Pssh = None
        self._RequestId = None

    @property
    def Keys(self):
        """加密密钥列表
        :rtype: list of Key
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def SessionKey(self):
        """用来加密密钥。
如果入参中带有RsaPublicKey，则SessionKey为使用Rsa公钥加密后的二进制数据，Base64编码字符串。
如果入参中没有RsaPublicKey，则SessionKey为原始数据的字符串形式。
        :rtype: str
        """
        return self._SessionKey

    @SessionKey.setter
    def SessionKey(self, SessionKey):
        self._SessionKey = SessionKey

    @property
    def ContentId(self):
        """内容ID
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def Pssh(self):
        """Widevine方案的Pssh数据，Base64编码。
Fairplay方案无该值。
        :rtype: str
        """
        return self._Pssh

    @Pssh.setter
    def Pssh(self, Pssh):
        self._Pssh = Pssh

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
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self._Keys.append(obj)
        self._SessionKey = params.get("SessionKey")
        self._ContentId = params.get("ContentId")
        self._Pssh = params.get("Pssh")
        self._RequestId = params.get("RequestId")


class DrmOutputObject(AbstractModel):
    """DRM加密后的输出对象

    """

    def __init__(self):
        r"""
        :param _BucketName: 输出的桶名称。
        :type BucketName: str
        :param _ObjectName: 输出的对象名称。
        :type ObjectName: str
        :param _Para: 输出对象参数。
        :type Para: :class:`tencentcloud.drm.v20181115.models.DrmOutputPara`
        """
        self._BucketName = None
        self._ObjectName = None
        self._Para = None

    @property
    def BucketName(self):
        """输出的桶名称。
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def ObjectName(self):
        """输出的对象名称。
        :rtype: str
        """
        return self._ObjectName

    @ObjectName.setter
    def ObjectName(self, ObjectName):
        self._ObjectName = ObjectName

    @property
    def Para(self):
        """输出对象参数。
        :rtype: :class:`tencentcloud.drm.v20181115.models.DrmOutputPara`
        """
        return self._Para

    @Para.setter
    def Para(self, Para):
        self._Para = Para


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._ObjectName = params.get("ObjectName")
        if params.get("Para") is not None:
            self._Para = DrmOutputPara()
            self._Para._deserialize(params.get("Para"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmOutputPara(AbstractModel):
    """Drm加密对象输出参数

    """

    def __init__(self):
        r"""
        :param _Type: 内容类型。例:video，audio，mpd，m3u8
        :type Type: str
        :param _Language: 语言,例: en, zh-cn
        :type Language: str
        """
        self._Type = None
        self._Language = None

    @property
    def Type(self):
        """内容类型。例:video，audio，mpd，m3u8
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Language(self):
        """语言,例: en, zh-cn
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmSourceObject(AbstractModel):
    """用于DRM加密的源对象

    """

    def __init__(self):
        r"""
        :param _BucketName: 输入的桶名称。
        :type BucketName: str
        :param _ObjectName: 输入对象名称。
        :type ObjectName: str
        """
        self._BucketName = None
        self._ObjectName = None

    @property
    def BucketName(self):
        """输入的桶名称。
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def ObjectName(self):
        """输入对象名称。
        :rtype: str
        """
        return self._ObjectName

    @ObjectName.setter
    def ObjectName(self, ObjectName):
        self._ObjectName = ObjectName


    def _deserialize(self, params):
        self._BucketName = params.get("BucketName")
        self._ObjectName = params.get("ObjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FairPlayPemDigestInfo(AbstractModel):
    """FairPlay 私钥摘要信息。

    """

    def __init__(self):
        r"""
        :param _FairPlayPemId: fairplay 私钥pem id。
注意：此字段可能返回 null，表示取不到有效值。
        :type FairPlayPemId: int
        :param _Priority: 私钥的优先级。
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _Md5Pem: 私钥的md5 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5Pem: str
        :param _Md5Ask: ASK的md5信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5Ask: str
        :param _Md5PemDecryptKey: 私钥解密密钥的md5值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5PemDecryptKey: str
        """
        self._FairPlayPemId = None
        self._Priority = None
        self._Md5Pem = None
        self._Md5Ask = None
        self._Md5PemDecryptKey = None

    @property
    def FairPlayPemId(self):
        """fairplay 私钥pem id。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FairPlayPemId

    @FairPlayPemId.setter
    def FairPlayPemId(self, FairPlayPemId):
        self._FairPlayPemId = FairPlayPemId

    @property
    def Priority(self):
        """私钥的优先级。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Md5Pem(self):
        """私钥的md5 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Md5Pem

    @Md5Pem.setter
    def Md5Pem(self, Md5Pem):
        self._Md5Pem = Md5Pem

    @property
    def Md5Ask(self):
        """ASK的md5信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Md5Ask

    @Md5Ask.setter
    def Md5Ask(self, Md5Ask):
        self._Md5Ask = Md5Ask

    @property
    def Md5PemDecryptKey(self):
        """私钥解密密钥的md5值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Md5PemDecryptKey

    @Md5PemDecryptKey.setter
    def Md5PemDecryptKey(self, Md5PemDecryptKey):
        self._Md5PemDecryptKey = Md5PemDecryptKey


    def _deserialize(self, params):
        self._FairPlayPemId = params.get("FairPlayPemId")
        self._Priority = params.get("Priority")
        self._Md5Pem = params.get("Md5Pem")
        self._Md5Ask = params.get("Md5Ask")
        self._Md5PemDecryptKey = params.get("Md5PemDecryptKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateTDRMKeyRequest(AbstractModel):
    """GenerateTDRMKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DrmType: 使用的DRM方案类型，接口取值 NORMALAES 。
        :type DrmType: str
        :param _Tracks: 加密的track列表，接口取值 SD 。
        :type Tracks: list of str
        :param _ContentId: 一个加密内容的唯一标识。
        :type ContentId: str
        :param _ContentType: 内容类型。接口取值 LiveVideo 。
        :type ContentType: str
        """
        self._DrmType = None
        self._Tracks = None
        self._ContentId = None
        self._ContentType = None

    @property
    def DrmType(self):
        """使用的DRM方案类型，接口取值 NORMALAES 。
        :rtype: str
        """
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType

    @property
    def Tracks(self):
        """加密的track列表，接口取值 SD 。
        :rtype: list of str
        """
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks

    @property
    def ContentId(self):
        """一个加密内容的唯一标识。
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def ContentType(self):
        """内容类型。接口取值 LiveVideo 。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._DrmType = params.get("DrmType")
        self._Tracks = params.get("Tracks")
        self._ContentId = params.get("ContentId")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateTDRMKeyResponse(AbstractModel):
    """GenerateTDRMKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ContentId: 内容ID。
        :type ContentId: str
        :param _TXEncryptionToken: 加密密钥。
        :type TXEncryptionToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ContentId = None
        self._TXEncryptionToken = None
        self._RequestId = None

    @property
    def ContentId(self):
        """内容ID。
        :rtype: str
        """
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def TXEncryptionToken(self):
        """加密密钥。
        :rtype: str
        """
        return self._TXEncryptionToken

    @TXEncryptionToken.setter
    def TXEncryptionToken(self, TXEncryptionToken):
        self._TXEncryptionToken = TXEncryptionToken

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
        self._ContentId = params.get("ContentId")
        self._TXEncryptionToken = params.get("TXEncryptionToken")
        self._RequestId = params.get("RequestId")


class Key(AbstractModel):
    """DRM加密密钥

    """

    def __init__(self):
        r"""
        :param _Track: 加密track类型。Widevine支持SD、HD、UHD1、UHD2、AUDIO。Fairplay只支持HD。
        :type Track: str
        :param _KeyId: 密钥ID。
        :type KeyId: str
        :param _Key: 原始Key使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。
        :type Key: str
        :param _Iv: 原始IV使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。
        :type Iv: str
        :param _InsertTimestamp: 该key生成时的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTimestamp: int
        """
        self._Track = None
        self._KeyId = None
        self._Key = None
        self._Iv = None
        self._InsertTimestamp = None

    @property
    def Track(self):
        """加密track类型。Widevine支持SD、HD、UHD1、UHD2、AUDIO。Fairplay只支持HD。
        :rtype: str
        """
        return self._Track

    @Track.setter
    def Track(self, Track):
        self._Track = Track

    @property
    def KeyId(self):
        """密钥ID。
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Key(self):
        """原始Key使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Iv(self):
        """原始IV使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。
        :rtype: str
        """
        return self._Iv

    @Iv.setter
    def Iv(self, Iv):
        self._Iv = Iv

    @property
    def InsertTimestamp(self):
        """该key生成时的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InsertTimestamp

    @InsertTimestamp.setter
    def InsertTimestamp(self, InsertTimestamp):
        self._InsertTimestamp = InsertTimestamp


    def _deserialize(self, params):
        self._Track = params.get("Track")
        self._KeyId = params.get("KeyId")
        self._Key = params.get("Key")
        self._Iv = params.get("Iv")
        self._InsertTimestamp = params.get("InsertTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyParam(AbstractModel):
    """设置加密密钥所需的参数

    """

    def __init__(self):
        r"""
        :param _Track: 加密track类型。取值范围：
SD、HD、UHD1、UHD2、AUDIO
        :type Track: str
        :param _Key: 请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :type Key: str
        :param _KeyId: 密钥ID。
        :type KeyId: str
        :param _Iv: 请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :type Iv: str
        """
        self._Track = None
        self._Key = None
        self._KeyId = None
        self._Iv = None

    @property
    def Track(self):
        """加密track类型。取值范围：
SD、HD、UHD1、UHD2、AUDIO
        :rtype: str
        """
        return self._Track

    @Track.setter
    def Track(self, Track):
        self._Track = Track

    @property
    def Key(self):
        """请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def KeyId(self):
        """密钥ID。
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Iv(self):
        """请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._Iv

    @Iv.setter
    def Iv(self, Iv):
        self._Iv = Iv


    def _deserialize(self, params):
        self._Track = params.get("Track")
        self._Key = params.get("Key")
        self._KeyId = params.get("KeyId")
        self._Iv = params.get("Iv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFairPlayPemRequest(AbstractModel):
    """ModifyFairPlayPem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Pem: 加密后的fairplay方案申请时使用的私钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。
        :type Pem: str
        :param _Ask: 加密后的fairplay方案申请返回的ask数据。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。
        :type Ask: str
        :param _FairPlayPemId: 要修改的私钥id
        :type FairPlayPemId: int
        :param _PemDecryptKey: 私钥的解密密钥。
openssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :type PemDecryptKey: str
        :param _BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :type BailorId: int
        :param _Priority: 私钥的优先级，优先级数值越高，优先级越高。
该值可以不传，后台将自动分配一个优先级。
        :type Priority: int
        """
        self._Pem = None
        self._Ask = None
        self._FairPlayPemId = None
        self._PemDecryptKey = None
        self._BailorId = None
        self._Priority = None

    @property
    def Pem(self):
        """加密后的fairplay方案申请时使用的私钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._Pem

    @Pem.setter
    def Pem(self, Pem):
        self._Pem = Pem

    @property
    def Ask(self):
        """加密后的fairplay方案申请返回的ask数据。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._Ask

    @Ask.setter
    def Ask(self, Ask):
        self._Ask = Ask

    @property
    def FairPlayPemId(self):
        """要修改的私钥id
        :rtype: int
        """
        return self._FairPlayPemId

    @FairPlayPemId.setter
    def FairPlayPemId(self, FairPlayPemId):
        self._FairPlayPemId = FairPlayPemId

    @property
    def PemDecryptKey(self):
        """私钥的解密密钥。
openssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。
        :rtype: str
        """
        return self._PemDecryptKey

    @PemDecryptKey.setter
    def PemDecryptKey(self, PemDecryptKey):
        self._PemDecryptKey = PemDecryptKey

    @property
    def BailorId(self):
        """委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。
        :rtype: int
        """
        return self._BailorId

    @BailorId.setter
    def BailorId(self, BailorId):
        self._BailorId = BailorId

    @property
    def Priority(self):
        """私钥的优先级，优先级数值越高，优先级越高。
该值可以不传，后台将自动分配一个优先级。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._Pem = params.get("Pem")
        self._Ask = params.get("Ask")
        self._FairPlayPemId = params.get("FairPlayPemId")
        self._PemDecryptKey = params.get("PemDecryptKey")
        self._BailorId = params.get("BailorId")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFairPlayPemResponse(AbstractModel):
    """ModifyFairPlayPem返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FairPlayPemId: 设置私钥后，后台返回的pem id，用来唯一标识一个私钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type FairPlayPemId: int
        :param _Priority: 私钥的优先级，优先级数值越高，优先级越高。
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FairPlayPemId = None
        self._Priority = None
        self._RequestId = None

    @property
    def FairPlayPemId(self):
        """设置私钥后，后台返回的pem id，用来唯一标识一个私钥。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FairPlayPemId

    @FairPlayPemId.setter
    def FairPlayPemId(self, FairPlayPemId):
        self._FairPlayPemId = FairPlayPemId

    @property
    def Priority(self):
        """私钥的优先级，优先级数值越高，优先级越高。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

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
        self._FairPlayPemId = params.get("FairPlayPemId")
        self._Priority = params.get("Priority")
        self._RequestId = params.get("RequestId")


class PlaybackPolicy(AbstractModel):
    """播放控制参数

    """

    def __init__(self):
        r"""
        :param _LicenseDurationSeconds: 播放许可证的有效期
        :type LicenseDurationSeconds: int
        :param _PlaybackDurationSeconds: 开始播放后，允许最长播放时间
        :type PlaybackDurationSeconds: int
        """
        self._LicenseDurationSeconds = None
        self._PlaybackDurationSeconds = None

    @property
    def LicenseDurationSeconds(self):
        """播放许可证的有效期
        :rtype: int
        """
        return self._LicenseDurationSeconds

    @LicenseDurationSeconds.setter
    def LicenseDurationSeconds(self, LicenseDurationSeconds):
        self._LicenseDurationSeconds = LicenseDurationSeconds

    @property
    def PlaybackDurationSeconds(self):
        """开始播放后，允许最长播放时间
        :rtype: int
        """
        return self._PlaybackDurationSeconds

    @PlaybackDurationSeconds.setter
    def PlaybackDurationSeconds(self, PlaybackDurationSeconds):
        self._PlaybackDurationSeconds = PlaybackDurationSeconds


    def _deserialize(self, params):
        self._LicenseDurationSeconds = params.get("LicenseDurationSeconds")
        self._PlaybackDurationSeconds = params.get("PlaybackDurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartEncryptionRequest(AbstractModel):
    """StartEncryption请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CosEndPoint: cos的end point。
        :type CosEndPoint: str
        :param _CosSecretId: cos api密钥id。
        :type CosSecretId: str
        :param _CosSecretKey: cos api密钥。
        :type CosSecretKey: str
        :param _DrmType: 使用的DRM方案类型，接口取值WIDEVINE,FAIRPLAY
        :type DrmType: str
        :param _SourceObject: 存储在COS上的原始内容信息
        :type SourceObject: :class:`tencentcloud.drm.v20181115.models.DrmSourceObject`
        :param _OutputObjects: 加密后的内容存储到COS的对象
        :type OutputObjects: list of DrmOutputObject
        """
        self._CosEndPoint = None
        self._CosSecretId = None
        self._CosSecretKey = None
        self._DrmType = None
        self._SourceObject = None
        self._OutputObjects = None

    @property
    def CosEndPoint(self):
        """cos的end point。
        :rtype: str
        """
        return self._CosEndPoint

    @CosEndPoint.setter
    def CosEndPoint(self, CosEndPoint):
        self._CosEndPoint = CosEndPoint

    @property
    def CosSecretId(self):
        """cos api密钥id。
        :rtype: str
        """
        return self._CosSecretId

    @CosSecretId.setter
    def CosSecretId(self, CosSecretId):
        self._CosSecretId = CosSecretId

    @property
    def CosSecretKey(self):
        """cos api密钥。
        :rtype: str
        """
        return self._CosSecretKey

    @CosSecretKey.setter
    def CosSecretKey(self, CosSecretKey):
        self._CosSecretKey = CosSecretKey

    @property
    def DrmType(self):
        """使用的DRM方案类型，接口取值WIDEVINE,FAIRPLAY
        :rtype: str
        """
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType

    @property
    def SourceObject(self):
        """存储在COS上的原始内容信息
        :rtype: :class:`tencentcloud.drm.v20181115.models.DrmSourceObject`
        """
        return self._SourceObject

    @SourceObject.setter
    def SourceObject(self, SourceObject):
        self._SourceObject = SourceObject

    @property
    def OutputObjects(self):
        """加密后的内容存储到COS的对象
        :rtype: list of DrmOutputObject
        """
        return self._OutputObjects

    @OutputObjects.setter
    def OutputObjects(self, OutputObjects):
        self._OutputObjects = OutputObjects


    def _deserialize(self, params):
        self._CosEndPoint = params.get("CosEndPoint")
        self._CosSecretId = params.get("CosSecretId")
        self._CosSecretKey = params.get("CosSecretKey")
        self._DrmType = params.get("DrmType")
        if params.get("SourceObject") is not None:
            self._SourceObject = DrmSourceObject()
            self._SourceObject._deserialize(params.get("SourceObject"))
        if params.get("OutputObjects") is not None:
            self._OutputObjects = []
            for item in params.get("OutputObjects"):
                obj = DrmOutputObject()
                obj._deserialize(item)
                self._OutputObjects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartEncryptionResponse(AbstractModel):
    """StartEncryption返回参数结构体

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