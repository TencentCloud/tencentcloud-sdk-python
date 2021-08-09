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
        """
        :param Pem: 加密后的fairplay方案申请时使用的私钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。\n        :type Pem: str\n        :param Ask: 加密后的fairplay方案申请返回的ask数据。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。\n        :type Ask: str\n        :param PemDecryptKey: 私钥的解密密钥。
openssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。\n        :type PemDecryptKey: str\n        :param BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。\n        :type BailorId: int\n        :param Priority: 私钥的优先级，优先级数值越高，优先级越高。
该值可以不传，后台将自动分配一个优先级。\n        :type Priority: int\n        """
        self.Pem = None
        self.Ask = None
        self.PemDecryptKey = None
        self.BailorId = None
        self.Priority = None


    def _deserialize(self, params):
        self.Pem = params.get("Pem")
        self.Ask = params.get("Ask")
        self.PemDecryptKey = params.get("PemDecryptKey")
        self.BailorId = params.get("BailorId")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddFairPlayPemResponse(AbstractModel):
    """AddFairPlayPem返回参数结构体

    """

    def __init__(self):
        """
        :param FairPlayPemId: 设置私钥后，后台返回的pem id，用来唯一标识一个私钥。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FairPlayPemId: int\n        :param Priority: 私钥的优先级，优先级数值越高，优先级越高。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Priority: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FairPlayPemId = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class CreateEncryptKeysRequest(AbstractModel):
    """CreateEncryptKeys请求参数结构体

    """

    def __init__(self):
        """
        :param DrmType: 使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。\n        :type DrmType: str\n        :param Keys: 设置的加密密钥列表。\n        :type Keys: list of KeyParam\n        :param ContentId: 一个加密内容的唯一标识。\n        :type ContentId: str\n        :param ContentType: 内容类型。接口取值VodVideo,LiveVideo。\n        :type ContentType: str\n        """
        self.DrmType = None
        self.Keys = None
        self.ContentId = None
        self.ContentType = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = KeyParam()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.ContentId = params.get("ContentId")
        self.ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEncryptKeysResponse(AbstractModel):
    """CreateEncryptKeys返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLicenseRequest(AbstractModel):
    """CreateLicense请求参数结构体

    """

    def __init__(self):
        """
        :param DrmType: DRM方案类型，接口取值：WIDEVINE，FAIRPLAY。\n        :type DrmType: str\n        :param LicenseRequest: Base64编码的终端设备License Request数据。\n        :type LicenseRequest: str\n        :param ContentType: 内容类型，接口取值：VodVideo,LiveVideo。\n        :type ContentType: str\n        :param Tracks: 授权播放的Track列表。
该值为空时，默认授权所有track播放。\n        :type Tracks: list of str\n        :param PlaybackPolicy: 播放策略参数。\n        :type PlaybackPolicy: :class:`tencentcloud.drm.v20181115.models.PlaybackPolicy`\n        """
        self.DrmType = None
        self.LicenseRequest = None
        self.ContentType = None
        self.Tracks = None
        self.PlaybackPolicy = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        self.LicenseRequest = params.get("LicenseRequest")
        self.ContentType = params.get("ContentType")
        self.Tracks = params.get("Tracks")
        if params.get("PlaybackPolicy") is not None:
            self.PlaybackPolicy = PlaybackPolicy()
            self.PlaybackPolicy._deserialize(params.get("PlaybackPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLicenseResponse(AbstractModel):
    """CreateLicense返回参数结构体

    """

    def __init__(self):
        """
        :param License: Base64 编码的许可证二进制数据。\n        :type License: str\n        :param ContentId: 加密内容的内容ID\n        :type ContentId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.License = None
        self.ContentId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.ContentId = params.get("ContentId")
        self.RequestId = params.get("RequestId")


class DeleteFairPlayPemRequest(AbstractModel):
    """DeleteFairPlayPem请求参数结构体

    """

    def __init__(self):
        """
        :param BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。\n        :type BailorId: int\n        :param FairPlayPemId: 要删除的pem id。
当未传入该值时，将删除所有的私钥。\n        :type FairPlayPemId: int\n        """
        self.BailorId = None
        self.FairPlayPemId = None


    def _deserialize(self, params):
        self.BailorId = params.get("BailorId")
        self.FairPlayPemId = params.get("FairPlayPemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFairPlayPemResponse(AbstractModel):
    """DeleteFairPlayPem返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAllKeysRequest(AbstractModel):
    """DescribeAllKeys请求参数结构体

    """

    def __init__(self):
        """
        :param DrmType: 使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。\n        :type DrmType: str\n        :param RsaPublicKey: Base64编码的Rsa公钥，用来加密出参中的SessionKey。
如果该参数为空，则出参中SessionKey为明文。\n        :type RsaPublicKey: str\n        :param ContentId: 一个加密内容的唯一标识。\n        :type ContentId: str\n        :param ContentType: 内容类型。接口取值VodVideo,LiveVideo。\n        :type ContentType: str\n        """
        self.DrmType = None
        self.RsaPublicKey = None
        self.ContentId = None
        self.ContentType = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        self.RsaPublicKey = params.get("RsaPublicKey")
        self.ContentId = params.get("ContentId")
        self.ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllKeysResponse(AbstractModel):
    """DescribeAllKeys返回参数结构体

    """

    def __init__(self):
        """
        :param Keys: 加密密钥列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Keys: list of Key\n        :param SessionKey: 用来加密密钥。
如果入参中带有RsaPublicKey，则SessionKey为使用Rsa公钥加密后的二进制数据，Base64编码字符串。
如果入参中没有RsaPublicKey，则SessionKey为原始数据的字符串形式。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SessionKey: str\n        :param ContentId: 内容ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContentId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Keys = None
        self.SessionKey = None
        self.ContentId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.SessionKey = params.get("SessionKey")
        self.ContentId = params.get("ContentId")
        self.RequestId = params.get("RequestId")


class DescribeFairPlayPemRequest(AbstractModel):
    """DescribeFairPlayPem请求参数结构体

    """

    def __init__(self):
        """
        :param BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。\n        :type BailorId: int\n        :param FairPlayPemId: 需要查询的pem id。
当该值未填入时，将返回所有的私钥信息。\n        :type FairPlayPemId: int\n        """
        self.BailorId = None
        self.FairPlayPemId = None


    def _deserialize(self, params):
        self.BailorId = params.get("BailorId")
        self.FairPlayPemId = params.get("FairPlayPemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFairPlayPemResponse(AbstractModel):
    """DescribeFairPlayPem返回参数结构体

    """

    def __init__(self):
        """
        :param FairPlayPems: 该账户下，所有设置的FairPlay私钥摘要信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type FairPlayPems: list of FairPlayPemDigestInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FairPlayPems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FairPlayPems") is not None:
            self.FairPlayPems = []
            for item in params.get("FairPlayPems"):
                obj = FairPlayPemDigestInfo()
                obj._deserialize(item)
                self.FairPlayPems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys请求参数结构体

    """

    def __init__(self):
        """
        :param DrmType: 使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。\n        :type DrmType: str\n        :param Tracks: 加密的track列表，接口取值VIDEO、AUDIO。\n        :type Tracks: list of str\n        :param ContentType: 内容类型。接口取值VodVideo,LiveVideo\n        :type ContentType: str\n        :param RsaPublicKey: Base64编码的Rsa公钥，用来加密出参中的SessionKey。
如果该参数为空，则出参中SessionKey为明文。\n        :type RsaPublicKey: str\n        :param ContentId: 一个加密内容的唯一标识。
如果该参数为空，则后台自动生成\n        :type ContentId: str\n        """
        self.DrmType = None
        self.Tracks = None
        self.ContentType = None
        self.RsaPublicKey = None
        self.ContentId = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        self.Tracks = params.get("Tracks")
        self.ContentType = params.get("ContentType")
        self.RsaPublicKey = params.get("RsaPublicKey")
        self.ContentId = params.get("ContentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回参数结构体

    """

    def __init__(self):
        """
        :param Keys: 加密密钥列表\n        :type Keys: list of Key\n        :param SessionKey: 用来加密密钥。
如果入参中带有RsaPublicKey，则SessionKey为使用Rsa公钥加密后的二进制数据，Base64编码字符串。
如果入参中没有RsaPublicKey，则SessionKey为原始数据的字符串形式。\n        :type SessionKey: str\n        :param ContentId: 内容ID\n        :type ContentId: str\n        :param Pssh: Widevine方案的Pssh数据，Base64编码。
Fairplay方案无该值。\n        :type Pssh: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Keys = None
        self.SessionKey = None
        self.ContentId = None
        self.Pssh = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.SessionKey = params.get("SessionKey")
        self.ContentId = params.get("ContentId")
        self.Pssh = params.get("Pssh")
        self.RequestId = params.get("RequestId")


class DrmOutputObject(AbstractModel):
    """DRM加密后的输出对象

    """

    def __init__(self):
        """
        :param BucketName: 输出的桶名称。\n        :type BucketName: str\n        :param ObjectName: 输出的对象名称。\n        :type ObjectName: str\n        :param Para: 输出对象参数。\n        :type Para: :class:`tencentcloud.drm.v20181115.models.DrmOutputPara`\n        """
        self.BucketName = None
        self.ObjectName = None
        self.Para = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ObjectName = params.get("ObjectName")
        if params.get("Para") is not None:
            self.Para = DrmOutputPara()
            self.Para._deserialize(params.get("Para"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmOutputPara(AbstractModel):
    """Drm加密对象输出参数

    """

    def __init__(self):
        """
        :param Type: 内容类型。例:video，audio，mpd，m3u8\n        :type Type: str\n        :param Language: 语言,例: en, zh-cn\n        :type Language: str\n        """
        self.Type = None
        self.Language = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmSourceObject(AbstractModel):
    """用于DRM加密的源对象

    """

    def __init__(self):
        """
        :param BucketName: 输入的桶名称。\n        :type BucketName: str\n        :param ObjectName: 输入对象名称。\n        :type ObjectName: str\n        """
        self.BucketName = None
        self.ObjectName = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ObjectName = params.get("ObjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FairPlayPemDigestInfo(AbstractModel):
    """FairPlay 私钥摘要信息。

    """

    def __init__(self):
        """
        :param FairPlayPemId: fairplay 私钥pem id。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FairPlayPemId: int\n        :param Priority: 私钥的优先级。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Priority: int\n        :param Md5Pem: 私钥的md5 信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Md5Pem: str\n        :param Md5Ask: ASK的md5信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Md5Ask: str\n        :param Md5PemDecryptKey: 私钥解密密钥的md5值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Md5PemDecryptKey: str\n        """
        self.FairPlayPemId = None
        self.Priority = None
        self.Md5Pem = None
        self.Md5Ask = None
        self.Md5PemDecryptKey = None


    def _deserialize(self, params):
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.Priority = params.get("Priority")
        self.Md5Pem = params.get("Md5Pem")
        self.Md5Ask = params.get("Md5Ask")
        self.Md5PemDecryptKey = params.get("Md5PemDecryptKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Key(AbstractModel):
    """DRM加密密钥

    """

    def __init__(self):
        """
        :param Track: 加密track类型。Widevine支持SD、HD、UHD1、UHD2、AUDIO。Fairplay只支持HD。\n        :type Track: str\n        :param KeyId: 密钥ID。\n        :type KeyId: str\n        :param Key: 原始Key使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。\n        :type Key: str\n        :param Iv: 原始IV使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。\n        :type Iv: str\n        :param InsertTimestamp: 该key生成时的时间戳
注意：此字段可能返回 null，表示取不到有效值。\n        :type InsertTimestamp: int\n        """
        self.Track = None
        self.KeyId = None
        self.Key = None
        self.Iv = None
        self.InsertTimestamp = None


    def _deserialize(self, params):
        self.Track = params.get("Track")
        self.KeyId = params.get("KeyId")
        self.Key = params.get("Key")
        self.Iv = params.get("Iv")
        self.InsertTimestamp = params.get("InsertTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyParam(AbstractModel):
    """设置加密密钥所需的参数

    """

    def __init__(self):
        """
        :param Track: 加密track类型。取值范围：
SD、HD、UHD1、UHD2、AUDIO\n        :type Track: str\n        :param Key: 请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。\n        :type Key: str\n        :param KeyId: 密钥ID。\n        :type KeyId: str\n        :param Iv: 请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。\n        :type Iv: str\n        """
        self.Track = None
        self.Key = None
        self.KeyId = None
        self.Iv = None


    def _deserialize(self, params):
        self.Track = params.get("Track")
        self.Key = params.get("Key")
        self.KeyId = params.get("KeyId")
        self.Iv = params.get("Iv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFairPlayPemRequest(AbstractModel):
    """ModifyFairPlayPem请求参数结构体

    """

    def __init__(self):
        """
        :param Pem: 加密后的fairplay方案申请时使用的私钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对私钥文件中的字段进行加密，并对加密结果进行base64编码。\n        :type Pem: str\n        :param Ask: 加密后的fairplay方案申请返回的ask数据。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对Ask字符串进行加密，并对加密结果进行base64编码。\n        :type Ask: str\n        :param FairPlayPemId: 要修改的私钥id\n        :type FairPlayPemId: int\n        :param PemDecryptKey: 私钥的解密密钥。
openssl在生成rsa时，可能会需要设置加密密钥，请记住设置的密钥。
请使用腾讯云DRM 提供的公钥，使用rsa加密算法，PKCS1填充方式对解密密钥进行加密，并对加密结果进行base64编码。\n        :type PemDecryptKey: str\n        :param BailorId: 委托者Id,适用于托管自身证书的客户。普通客户无需填该字段。\n        :type BailorId: int\n        :param Priority: 私钥的优先级，优先级数值越高，优先级越高。
该值可以不传，后台将自动分配一个优先级。\n        :type Priority: int\n        """
        self.Pem = None
        self.Ask = None
        self.FairPlayPemId = None
        self.PemDecryptKey = None
        self.BailorId = None
        self.Priority = None


    def _deserialize(self, params):
        self.Pem = params.get("Pem")
        self.Ask = params.get("Ask")
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.PemDecryptKey = params.get("PemDecryptKey")
        self.BailorId = params.get("BailorId")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFairPlayPemResponse(AbstractModel):
    """ModifyFairPlayPem返回参数结构体

    """

    def __init__(self):
        """
        :param FairPlayPemId: 设置私钥后，后台返回的pem id，用来唯一标识一个私钥。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FairPlayPemId: int\n        :param Priority: 私钥的优先级，优先级数值越高，优先级越高。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Priority: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FairPlayPemId = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class PlaybackPolicy(AbstractModel):
    """播放控制参数

    """

    def __init__(self):
        """
        :param LicenseDurationSeconds: 播放许可证的有效期\n        :type LicenseDurationSeconds: int\n        :param PlaybackDurationSeconds: 开始播放后，允许最长播放时间\n        :type PlaybackDurationSeconds: int\n        """
        self.LicenseDurationSeconds = None
        self.PlaybackDurationSeconds = None


    def _deserialize(self, params):
        self.LicenseDurationSeconds = params.get("LicenseDurationSeconds")
        self.PlaybackDurationSeconds = params.get("PlaybackDurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartEncryptionRequest(AbstractModel):
    """StartEncryption请求参数结构体

    """

    def __init__(self):
        """
        :param CosEndPoint: cos的end point。\n        :type CosEndPoint: str\n        :param CosSecretId: cos api密钥id。\n        :type CosSecretId: str\n        :param CosSecretKey: cos api密钥。\n        :type CosSecretKey: str\n        :param DrmType: 使用的DRM方案类型，接口取值WIDEVINE,FAIRPLAY\n        :type DrmType: str\n        :param SourceObject: 存储在COS上的原始内容信息\n        :type SourceObject: :class:`tencentcloud.drm.v20181115.models.DrmSourceObject`\n        :param OutputObjects: 加密后的内容存储到COS的对象\n        :type OutputObjects: list of DrmOutputObject\n        """
        self.CosEndPoint = None
        self.CosSecretId = None
        self.CosSecretKey = None
        self.DrmType = None
        self.SourceObject = None
        self.OutputObjects = None


    def _deserialize(self, params):
        self.CosEndPoint = params.get("CosEndPoint")
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.DrmType = params.get("DrmType")
        if params.get("SourceObject") is not None:
            self.SourceObject = DrmSourceObject()
            self.SourceObject._deserialize(params.get("SourceObject"))
        if params.get("OutputObjects") is not None:
            self.OutputObjects = []
            for item in params.get("OutputObjects"):
                obj = DrmOutputObject()
                obj._deserialize(item)
                self.OutputObjects.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartEncryptionResponse(AbstractModel):
    """StartEncryption返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")