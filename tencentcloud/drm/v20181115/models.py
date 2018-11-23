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


class CreateLicenseRequest(AbstractModel):
    """CreateLicense请求参数结构体

    """

    def __init__(self):
        """
        :param DrmType: DRM方案类型，接口取值：WIDEVINE，FAIRPLAY。
        :type DrmType: str
        :param LicenseRequest: Base64编码的终端设备License Request数据。
        :type LicenseRequest: str
        :param ContentType: 内容类型，接口取值：VodVideo,LiveVideo。
        :type ContentType: str
        :param Tracks: 授权播放的Track列表。
该值为空时，默认授权所有track播放。
        :type Tracks: list of str
        :param PlaybackPolicy: 播放策略参数。
        :type PlaybackPolicy: :class:`tencentcloud.drm.v20181115.models.PlaybackPolicy`
        """
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


class CreateLicenseResponse(AbstractModel):
    """CreateLicense返回参数结构体

    """

    def __init__(self):
        """
        :param License: Base64 编码的许可证二进制数据。
        :type License: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.License = None
        self.RequestId = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys请求参数结构体

    """

    def __init__(self):
        """
        :param DrmType: 使用的DRM方案类型，接口取值WIDEVINE、FAIRPLAY、NORMALAES。
        :type DrmType: str
        :param Tracks: 加密的track列表，接口取值VIDEO、AUDIO。
        :type Tracks: list of str
        :param ContentType: 内容类型。接口取值VodVideo,LiveVideo
        :type ContentType: str
        :param RsaPublicKey: Base64编码的Rsa公钥，用来加密出参中的SessionKey。
如果该参数为空，则出参中SessionKey为明文。
        :type RsaPublicKey: str
        :param ContentId: 一个加密内容的唯一标识。
如果该参数为空，则后台自动生成
        :type ContentId: str
        """
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


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回参数结构体

    """

    def __init__(self):
        """
        :param Keys: 加密密钥列表
        :type Keys: list of Key
        :param SessionKey: 用来加密密钥。
如果入参中带有RsaPublicKey，则SessionKey为使用Rsa公钥加密后的二进制数据，Base64编码字符串。
如果入参中没有RsaPublicKey，则SessionKey为原始数据的字符串形式。
        :type SessionKey: str
        :param ContentId: 内容ID
        :type ContentId: str
        :param Pssh: Widevine方案的Pssh数据，Base64编码。
Fairplay方案无该值。
        :type Pssh: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param BucketName: 输出的桶名称。
        :type BucketName: str
        :param ObjectName: 输出的对象名称。
        :type ObjectName: str
        :param Para: 输出对象参数。
        :type Para: :class:`tencentcloud.drm.v20181115.models.DrmOutputPara`
        """
        self.BucketName = None
        self.ObjectName = None
        self.Para = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ObjectName = params.get("ObjectName")
        if params.get("Para") is not None:
            self.Para = DrmOutputPara()
            self.Para._deserialize(params.get("Para"))


class DrmOutputPara(AbstractModel):
    """Drm加密对象输出参数

    """

    def __init__(self):
        """
        :param Type: 内容类型。例:video，audio，mpd，m3u8
        :type Type: str
        :param Language: 语言,例: en, zh-cn
        :type Language: str
        """
        self.Type = None
        self.Language = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Language = params.get("Language")


class DrmSourceObject(AbstractModel):
    """用于DRM加密的源对象

    """

    def __init__(self):
        """
        :param BucketName: 输入的桶名称。
        :type BucketName: str
        :param ObjectName: 输入对象名称。
        :type ObjectName: str
        """
        self.BucketName = None
        self.ObjectName = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ObjectName = params.get("ObjectName")


class Key(AbstractModel):
    """DRM加密密钥

    """

    def __init__(self):
        """
        :param Track: 加密track类型。
        :type Track: str
        :param KeyId: 密钥ID。
        :type KeyId: str
        :param Key: 原始Key使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。
        :type Key: str
        :param Iv: 原始IV使用AES-128 ECB模式和SessionKey加密的后的二进制数据，Base64编码的字符串。
        :type Iv: str
        """
        self.Track = None
        self.KeyId = None
        self.Key = None
        self.Iv = None


    def _deserialize(self, params):
        self.Track = params.get("Track")
        self.KeyId = params.get("KeyId")
        self.Key = params.get("Key")
        self.Iv = params.get("Iv")


class PlaybackPolicy(AbstractModel):
    """播放控制参数

    """

    def __init__(self):
        """
        :param LicenseDurationSeconds: 播放许可证的有效期
        :type LicenseDurationSeconds: int
        :param PlaybackDurationSeconds: 开始播放后，允许最长播放时间
        :type PlaybackDurationSeconds: int
        """
        self.LicenseDurationSeconds = None
        self.PlaybackDurationSeconds = None


    def _deserialize(self, params):
        self.LicenseDurationSeconds = params.get("LicenseDurationSeconds")
        self.PlaybackDurationSeconds = params.get("PlaybackDurationSeconds")


class StartEncryptionRequest(AbstractModel):
    """StartEncryption请求参数结构体

    """

    def __init__(self):
        """
        :param CosEndPoint: cos的end point。
        :type CosEndPoint: str
        :param CosSecretId: cos api密钥id。
        :type CosSecretId: str
        :param CosSecretKey: cos api密钥。
        :type CosSecretKey: str
        :param DrmType: 使用的DRM方案类型，接口取值WIDEVINE,FAIRPLAY
        :type DrmType: str
        :param SourceObject: 存储在COS上的原始内容信息
        :type SourceObject: :class:`tencentcloud.drm.v20181115.models.DrmSourceObject`
        :param OutputObjects: 加密后的内容存储到COS的对象
        :type OutputObjects: list of DrmOutputObject
        """
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


class StartEncryptionResponse(AbstractModel):
    """StartEncryption返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")