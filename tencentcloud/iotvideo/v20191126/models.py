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


class BindDevInfo(AbstractModel):
    """终端用户绑定的设备

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param DeviceModel: 设备型号
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceModel: str
        :param Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        """
        self.Tid = None
        self.DeviceName = None
        self.DeviceModel = None
        self.Role = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.DeviceName = params.get("DeviceName")
        self.DeviceModel = params.get("DeviceModel")
        self.Role = params.get("Role")


class BindUsrInfo(AbstractModel):
    """设备绑定的终端用户

    """

    def __init__(self):
        """
        :param AccessId: IotVideo平台分配给终端用户的用户id
        :type AccessId: str
        :param Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        """
        self.AccessId = None
        self.Role = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Role = params.get("Role")


class ClearDeviceActiveCodeRequest(AbstractModel):
    """ClearDeviceActiveCode请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: 设备TID列表，0<元素数量<=100
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class ClearDeviceActiveCodeResponse(AbstractModel):
    """ClearDeviceActiveCode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Contents(AbstractModel):
    """版本发布的描述信息，需要国际化，可以为空

    """

    def __init__(self):
        """
        :param En: 英文，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type En: str
        :param Cn: 中文简体，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Cn: str
        :param Tc: 中文繁体(Traditional Chinese)，长度不超过300个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type Tc: str
        """
        self.En = None
        self.Cn = None
        self.Tc = None


    def _deserialize(self, params):
        self.En = params.get("En")
        self.Cn = params.get("Cn")
        self.Tc = params.get("Tc")


class CreateAnonymousAccessTokenRequest(AbstractModel):
    """CreateAnonymousAccessToken请求参数结构体

    """

    def __init__(self):
        """
        :param TtlMinutes: Token的TTL(time to alive)分钟数,最大值1440(即24小时)
        :type TtlMinutes: int
        :param Tid: 设备ID。创建Token时, 此参数为必须项
        :type Tid: str
        :param OldAccessToken: 旧的AccessToken。续期Token时，此参数为必须
        :type OldAccessToken: str
        """
        self.TtlMinutes = None
        self.Tid = None
        self.OldAccessToken = None


    def _deserialize(self, params):
        self.TtlMinutes = params.get("TtlMinutes")
        self.Tid = params.get("Tid")
        self.OldAccessToken = params.get("OldAccessToken")


class CreateAnonymousAccessTokenResponse(AbstractModel):
    """CreateAnonymousAccessToken返回参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param AccessToken: IoT Video平台的AccessToken
        :type AccessToken: str
        :param ExpireTime: Token的过期时间，单位秒(UTC时间)
        :type ExpireTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessId = None
        self.AccessToken = None
        self.ExpireTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.AccessToken = params.get("AccessToken")
        self.ExpireTime = params.get("ExpireTime")
        self.RequestId = params.get("RequestId")


class CreateAppUsrRequest(AbstractModel):
    """CreateAppUsr请求参数结构体

    """

    def __init__(self):
        """
        :param CunionId: 标识用户的唯一ID，防止同一个用户多次注册
        :type CunionId: str
        :param Mobile: 用于小程序关联手机号
        :type Mobile: str
        """
        self.CunionId = None
        self.Mobile = None


    def _deserialize(self, params):
        self.CunionId = params.get("CunionId")
        self.Mobile = params.get("Mobile")


class CreateAppUsrResponse(AbstractModel):
    """CreateAppUsr返回参数结构体

    """

    def __init__(self):
        """
        :param CunionId: 厂商云标识用户的唯一ID
        :type CunionId: str
        :param AccessId: 客户的终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param NewRegist: 用户是否为新创建
        :type NewRegist: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CunionId = None
        self.AccessId = None
        self.NewRegist = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CunionId = params.get("CunionId")
        self.AccessId = params.get("AccessId")
        self.NewRegist = params.get("NewRegist")
        self.RequestId = params.get("RequestId")


class CreateBindingRequest(AbstractModel):
    """CreateBinding请求参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param Tid: 设备TID
        :type Tid: str
        :param Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        :param ForceBind: 是否踢掉之前的主人，true：踢掉；false：不踢掉。当role为guest时，可以不填
        :type ForceBind: bool
        """
        self.AccessId = None
        self.Tid = None
        self.Role = None
        self.ForceBind = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tid = params.get("Tid")
        self.Role = params.get("Role")
        self.ForceBind = params.get("ForceBind")


class CreateBindingResponse(AbstractModel):
    """CreateBinding返回参数结构体

    """

    def __init__(self):
        """
        :param AccessToken: 访问设备的AccessToken
        :type AccessToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.RequestId = params.get("RequestId")


class CreateDevTokenRequest(AbstractModel):
    """CreateDevToken请求参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 客户的终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param Tids: 设备TID列表,0<元素数量<=100
        :type Tids: list of str
        :param TtlMinutes: Token的TTL(time to alive)分钟数
        :type TtlMinutes: int
        """
        self.AccessId = None
        self.Tids = None
        self.TtlMinutes = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tids = params.get("Tids")
        self.TtlMinutes = params.get("TtlMinutes")


class CreateDevTokenResponse(AbstractModel):
    """CreateDevToken返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回的用户token列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DevTokenInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DevTokenInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class CreateDevicesRequest(AbstractModel):
    """CreateDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param Number: 创建设备的数量，数量范围1-100
        :type Number: int
        :param NamePrefix: 设备名称前缀，支持英文、数字，不超过10字符
        :type NamePrefix: str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.Number = None
        self.NamePrefix = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Number = params.get("Number")
        self.NamePrefix = params.get("NamePrefix")
        self.Operator = params.get("Operator")


class CreateDevicesResponse(AbstractModel):
    """CreateDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 新创建设备的认证信息
        :type Data: list of DeviceCertificate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DeviceCertificate()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class CreateGencodeRequest(AbstractModel):
    """CreateGencode请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param Revision: 物模型发布版本号,-1代表未发布的，保存的是草稿箱的版本。1代表已发布的物模型。
        :type Revision: int
        """
        self.ProductId = None
        self.Revision = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Revision = params.get("Revision")


class CreateGencodeResponse(AbstractModel):
    """CreateGencode返回参数结构体

    """

    def __init__(self):
        """
        :param ZipCode: 生成的源代码(zip压缩后的base64编码)
注意：此字段可能返回 null，表示取不到有效值。
        :type ZipCode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ZipCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZipCode = params.get("ZipCode")
        self.RequestId = params.get("RequestId")


class CreateIotDataTypeRequest(AbstractModel):
    """CreateIotDataType请求参数结构体

    """

    def __init__(self):
        """
        :param IotDataType: 用户自定义数据类型，json格式的字符串
        :type IotDataType: str
        """
        self.IotDataType = None


    def _deserialize(self, params):
        self.IotDataType = params.get("IotDataType")


class CreateIotDataTypeResponse(AbstractModel):
    """CreateIotDataType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateIotModelRequest(AbstractModel):
    """CreateIotModel请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param IotModel: 物模型json串
        :type IotModel: str
        """
        self.ProductId = None
        self.IotModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.IotModel = params.get("IotModel")


class CreateIotModelResponse(AbstractModel):
    """CreateIotModel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductModel: 产器型号(APP产品,为APP包名)
        :type ProductModel: str
        :param ProductName: 产品名称
仅支持中文、英文、数字、下划线，不超过32个字符
        :type ProductName: str
        :param ProductDescription: 产品描述信息
不支持单引号、双引号、退格符、回车符、换行符、制表符、反斜杠、下划线、“%”、“#”、“$”，不超过128字符
        :type ProductDescription: str
        :param Features: 设备功能码（ypsxth:音频双向通话 ，spdxth:视频单向通话）
        :type Features: list of str
        :param ChipManufactureId: 主芯片产商ID
        :type ChipManufactureId: str
        :param ChipId: 主芯片ID
        :type ChipId: str
        :param ProductRegion: 地域：
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
India（印度）
Other-Overseas（其他境外地区）
        :type ProductRegion: str
        :param ProductCate: 设备类型, 0-普通视频设备，1-NVR设备
        :type ProductCate: int
        :param AccessMode: 接入模型，bit0是0：公版小程序未接入，bit0是1：公版小程序已接入
        :type AccessMode: int
        :param Os: Linux,Android,Liteos等系统
        :type Os: str
        """
        self.ProductModel = None
        self.ProductName = None
        self.ProductDescription = None
        self.Features = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductRegion = None
        self.ProductCate = None
        self.AccessMode = None
        self.Os = None


    def _deserialize(self, params):
        self.ProductModel = params.get("ProductModel")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.Features = params.get("Features")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductRegion = params.get("ProductRegion")
        self.ProductCate = params.get("ProductCate")
        self.AccessMode = params.get("AccessMode")
        self.Os = params.get("Os")


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详细信息
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.ProductBase`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ProductBase()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateStorageRequest(AbstractModel):
    """CreateStorage请求参数结构体

    """

    def __init__(self):
        """
        :param PkgId: 云存套餐ID
        :type PkgId: str
        :param Tid: 设备TID
        :type Tid: str
        :param UserTag: 用户唯一标识，由厂商保证内部唯一性
        :type UserTag: str
        """
        self.PkgId = None
        self.Tid = None
        self.UserTag = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.Tid = params.get("Tid")
        self.UserTag = params.get("UserTag")


class CreateStorageResponse(AbstractModel):
    """CreateStorage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateStorageServiceRequest(AbstractModel):
    """CreateStorageService请求参数结构体

    """

    def __init__(self):
        """
        :param PkgId: 云存套餐ID：
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
        :type PkgId: str
        :param Tid: 设备TID
        :type Tid: str
        :param OrderCount: 订单数量,可一次性创建多个订单
        :type OrderCount: int
        :param StorageRegion: 云存服务所在的区域,如ap-guangzhou,ap-singapore
        :type StorageRegion: str
        :param ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param AccessId: 设备主人用户在IoT Video平台的注册ID。该参数用于验证Paas/Saas平台的设备/用户关系链是否一致
        :type AccessId: str
        :param EnableTime: 服务生效时间,若不指定此参数，服务立即生效
        :type EnableTime: int
        """
        self.PkgId = None
        self.Tid = None
        self.OrderCount = None
        self.StorageRegion = None
        self.ChnNum = None
        self.AccessId = None
        self.EnableTime = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.Tid = params.get("Tid")
        self.OrderCount = params.get("OrderCount")
        self.StorageRegion = params.get("StorageRegion")
        self.ChnNum = params.get("ChnNum")
        self.AccessId = params.get("AccessId")
        self.EnableTime = params.get("EnableTime")


class CreateStorageServiceResponse(AbstractModel):
    """CreateStorageService返回参数结构体

    """

    def __init__(self):
        """
        :param IsRenew: 标志是否为续订
        :type IsRenew: bool
        :param ServiceId: 云存服务ID
        :type ServiceId: str
        :param StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param Tid: 设备TID
        :type Tid: str
        :param ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param StartTime: 服务开始时间
        :type StartTime: int
        :param EndTime: 服务失效时间
        :type EndTime: int
        :param Status: 服务状态
        :type Status: int
        :param Data: 新增的云存定单列表
        :type Data: list of StorageOrder
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsRenew = None
        self.ServiceId = None
        self.StorageRegion = None
        self.Tid = None
        self.ChnNum = None
        self.AccessId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsRenew = params.get("IsRenew")
        self.ServiceId = params.get("ServiceId")
        self.StorageRegion = params.get("StorageRegion")
        self.Tid = params.get("Tid")
        self.ChnNum = params.get("ChnNum")
        self.AccessId = params.get("AccessId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class CreateTraceIdsRequest(AbstractModel):
    """CreateTraceIds请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: 设备TID列表
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class CreateTraceIdsResponse(AbstractModel):
    """CreateTraceIds返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUploadPathRequest(AbstractModel):
    """CreateUploadPath请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param FileName: 固件文件名
        :type FileName: str
        """
        self.ProductId = None
        self.FileName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.FileName = params.get("FileName")


class CreateUploadPathResponse(AbstractModel):
    """CreateUploadPath返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 固件上传地址URL，用户可将本地的固件文件通过该URL以PUT的请求方式上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateUsrTokenRequest(AbstractModel):
    """CreateUsrToken请求参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param UniqueId: 终端唯一ID，用于区分同一个用户的多个终端
        :type UniqueId: str
        :param TtlMinutes: Token的TTL(time to alive)分钟数
        :type TtlMinutes: int
        """
        self.AccessId = None
        self.UniqueId = None
        self.TtlMinutes = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.UniqueId = params.get("UniqueId")
        self.TtlMinutes = params.get("TtlMinutes")


class CreateUsrTokenResponse(AbstractModel):
    """CreateUsrToken返回参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param AccessToken: IoT Video平台的AccessToken
        :type AccessToken: str
        :param ExpireTime: Token的过期时间，单位秒(UTC时间)
        :type ExpireTime: int
        :param TerminalId: 终端ID
        :type TerminalId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessId = None
        self.AccessToken = None
        self.ExpireTime = None
        self.TerminalId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.AccessToken = params.get("AccessToken")
        self.ExpireTime = params.get("ExpireTime")
        self.TerminalId = params.get("TerminalId")
        self.RequestId = params.get("RequestId")


class DeleteAppUsrRequest(AbstractModel):
    """DeleteAppUsr请求参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 客户的终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        """
        self.AccessId = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")


class DeleteAppUsrResponse(AbstractModel):
    """DeleteAppUsr返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBindingRequest(AbstractModel):
    """DeleteBinding请求参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        :param Tid: 设备TID
        :type Tid: str
        :param Role: 用户角色，owner：主人，guest：访客
        :type Role: str
        """
        self.AccessId = None
        self.Tid = None
        self.Role = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tid = params.get("Tid")
        self.Role = params.get("Role")


class DeleteBindingResponse(AbstractModel):
    """DeleteBinding返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param Tids: 设备TID列表
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIotDataTypeRequest(AbstractModel):
    """DeleteIotDataType请求参数结构体

    """

    def __init__(self):
        """
        :param TypeId: 自定义数据类型的标识符
        :type TypeId: str
        """
        self.TypeId = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")


class DeleteIotDataTypeResponse(AbstractModel):
    """DeleteIotDataType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMessageQueueRequest(AbstractModel):
    """DeleteMessageQueue请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteMessageQueueResponse(AbstractModel):
    """DeleteMessageQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOtaVersionRequest(AbstractModel):
    """DeleteOtaVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.Operator = params.get("Operator")


class DeleteOtaVersionResponse(AbstractModel):
    """DeleteOtaVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param ProductId: 产品ID
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTraceIdsRequest(AbstractModel):
    """DeleteTraceIds请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: 设备TID列表
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DeleteTraceIdsResponse(AbstractModel):
    """DeleteTraceIds返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeliverStorageServiceRequest(AbstractModel):
    """DeliverStorageService请求参数结构体

    """

    def __init__(self):
        """
        :param SrcServiceId: 待转移的源云存服务ID
        :type SrcServiceId: str
        :param Tid: 设备TID
        :type Tid: str
        :param ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param AccessId: 设备主人用户在IoT Video平台的注册ID。该参数用于验证Paas/Saas平台的设备/用户关系链是否一致
        :type AccessId: str
        """
        self.SrcServiceId = None
        self.Tid = None
        self.ChnNum = None
        self.AccessId = None


    def _deserialize(self, params):
        self.SrcServiceId = params.get("SrcServiceId")
        self.Tid = params.get("Tid")
        self.ChnNum = params.get("ChnNum")
        self.AccessId = params.get("AccessId")


class DeliverStorageServiceResponse(AbstractModel):
    """DeliverStorageService返回参数结构体

    """

    def __init__(self):
        """
        :param SrcServiceId: 被转出的云存服务ID
        :type SrcServiceId: str
        :param ServiceId: 被转入的云存服务ID
        :type ServiceId: str
        :param StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param Tid: 设备TID
        :type Tid: str
        :param ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param StartTime: 服务开始时间
        :type StartTime: int
        :param EndTime: 服务失效时间
        :type EndTime: int
        :param Status: 服务状态
        :type Status: int
        :param Data: 新增的云存定单列表
        :type Data: list of StorageOrder
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SrcServiceId = None
        self.ServiceId = None
        self.StorageRegion = None
        self.Tid = None
        self.ChnNum = None
        self.AccessId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SrcServiceId = params.get("SrcServiceId")
        self.ServiceId = params.get("ServiceId")
        self.StorageRegion = params.get("StorageRegion")
        self.Tid = params.get("Tid")
        self.ChnNum = params.get("ChnNum")
        self.AccessId = params.get("AccessId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBindDevRequest(AbstractModel):
    """DescribeBindDev请求参数结构体

    """

    def __init__(self):
        """
        :param AccessId: 终端用户在IoT Video上的唯一标识ID
        :type AccessId: str
        """
        self.AccessId = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")


class DescribeBindDevResponse(AbstractModel):
    """DescribeBindDev返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 绑定的设备列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of BindDevInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BindDevInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBindUsrRequest(AbstractModel):
    """DescribeBindUsr请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param AccessId: 设备主人的AccessId
        :type AccessId: str
        """
        self.Tid = None
        self.AccessId = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.AccessId = params.get("AccessId")


class DescribeBindUsrResponse(AbstractModel):
    """DescribeBindUsr返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 具有绑定关系的终端用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of BindUsrInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BindUsrInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceModelRequest(AbstractModel):
    """DescribeDeviceModel请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param Branch: 物模型的分支路径
        :type Branch: str
        """
        self.Tid = None
        self.Branch = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Branch = params.get("Branch")


class DescribeDeviceModelResponse(AbstractModel):
    """DescribeDeviceModel返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备物模型信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.DeviceModelData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DeviceModelData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        """
        self.Tid = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.DeviceData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DeviceData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ReturnModel: 是否返回全量数据
当该值为false时，返回值中的设备物模型、固件版本、在线状态、最后在线时间字段等字段，都将返回数据类型的零值。
        :type ReturnModel: bool
        :param Limit: 分页数量,0<取值范围<=100
        :type Limit: int
        :param Offset: 分页偏移，取值＞0
        :type Offset: int
        :param OtaVersion: 指定固件版本号，为空查询此产品下所有设备
        :type OtaVersion: str
        :param DeviceName: 设备名称，支持左前缀模糊匹配
        :type DeviceName: str
        """
        self.ProductId = None
        self.ReturnModel = None
        self.Limit = None
        self.Offset = None
        self.OtaVersion = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ReturnModel = params.get("ReturnModel")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OtaVersion = params.get("OtaVersion")
        self.DeviceName = params.get("DeviceName")


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备信息 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DevicesData
        :param TotalCount: 设备总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DevicesData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIotDataTypeRequest(AbstractModel):
    """DescribeIotDataType请求参数结构体

    """

    def __init__(self):
        """
        :param TypeId: 自定义数据类型的标识符，为空则返回全量自定义类型的列表
        :type TypeId: str
        """
        self.TypeId = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")


class DescribeIotDataTypeResponse(AbstractModel):
    """DescribeIotDataType返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 自定义数据类型，json格式的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeIotModelRequest(AbstractModel):
    """DescribeIotModel请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param Revision: 物模型版本号， -1表示最新编辑的（未发布）
        :type Revision: int
        """
        self.ProductId = None
        self.Revision = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Revision = params.get("Revision")


class DescribeIotModelResponse(AbstractModel):
    """DescribeIotModel返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 物模型定义，json格式的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeIotModelsRequest(AbstractModel):
    """DescribeIotModels请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeIotModelsResponse(AbstractModel):
    """DescribeIotModels返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 历史版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of IotModelData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = IotModelData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogsRequest(AbstractModel):
    """DescribeLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param Limit: 当前分页的最大条数,0<取值范围<=100
        :type Limit: int
        :param Offset: 分页偏移量,取值范围>0
        :type Offset: int
        :param LogType: 日志类型 1.在线状态变更 2.ProConst变更 3.ProWritable变更 4.Action控制 5.ProReadonly变更 6.Event事件
        :type LogType: int
        :param StartTime: 查询的起始时间 UNIX时间戳，单位秒
        :type StartTime: int
        :param DataObject: 物模型对象索引，用于模糊查询，字符长度<=255，每层节点的字符长度<=16
        :type DataObject: str
        :param EndTime: 查询的结束时间 UNIX时间戳，单位秒
        :type EndTime: int
        """
        self.Tid = None
        self.Limit = None
        self.Offset = None
        self.LogType = None
        self.StartTime = None
        self.DataObject = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.LogType = params.get("LogType")
        self.StartTime = params.get("StartTime")
        self.DataObject = params.get("DataObject")
        self.EndTime = params.get("EndTime")


class DescribeLogsResponse(AbstractModel):
    """DescribeLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备日志信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of LogData
        :param TotalCount: Data数组所包含的信息条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = LogData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMessageQueueRequest(AbstractModel):
    """DescribeMessageQueue请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeMessageQueueResponse(AbstractModel):
    """DescribeMessageQueue返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 消息队列配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.MsgQueueData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = MsgQueueData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeModelDataRetRequest(AbstractModel):
    """DescribeModelDataRet请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeModelDataRetResponse(AbstractModel):
    """DescribeModelDataRet返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeOsListRequest(AbstractModel):
    """DescribeOsList请求参数结构体

    """


class DescribeOsListResponse(AbstractModel):
    """DescribeOsList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 系统类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.SystemType`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SystemType()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeOtaVersionsRequest(AbstractModel):
    """DescribeOtaVersions请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移量
        :type Offset: int
        :param Limit: 每页数量，0<取值范围<=100
        :type Limit: int
        :param ProductId: 产品ID，为空时查询客户所有产品的版本信息
        :type ProductId: str
        :param OtaVersion: 版本号，支持模糊匹配
        :type OtaVersion: str
        :param PubStatus: 版本类型 1未发布 2测试发布 3正式发布 4禁用
        :type PubStatus: int
        """
        self.Offset = None
        self.Limit = None
        self.ProductId = None
        self.OtaVersion = None
        self.PubStatus = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.PubStatus = params.get("PubStatus")


class DescribeOtaVersionsResponse(AbstractModel):
    """DescribeOtaVersions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 版本数量
        :type TotalCount: int
        :param Data: 版本详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VersionData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VersionData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.iotvideo.v20191126.models.ProductData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ProductData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页大小，当前页面中显示的最大数量，值范围 1-100
        :type Limit: int
        :param Offset: 分页偏移，Offset从0开始
        :type Offset: int
        :param ProductModel: 产器型号(APP产品,为APP包名)
        :type ProductModel: str
        :param StartTime: 开始时间 ，UNIX 时间戳，单位秒
        :type StartTime: int
        :param EndTime: 结束时间 ，UNIX 时间戳，单位秒
        :type EndTime: int
        """
        self.Limit = None
        self.Offset = None
        self.ProductModel = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProductModel = params.get("ProductModel")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详细信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ProductData
        :param TotalCount: 产品总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ProductData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePubVersionsRequest(AbstractModel):
    """DescribePubVersions请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribePubVersionsResponse(AbstractModel):
    """DescribePubVersions返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 历史发布的版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of OtaPubHistory
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = OtaPubHistory()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegistrationStatusRequest(AbstractModel):
    """DescribeRegistrationStatus请求参数结构体

    """

    def __init__(self):
        """
        :param CunionIds: 终端用户的唯一ID列表，0<元素数量<=100
        :type CunionIds: list of str
        """
        self.CunionIds = None


    def _deserialize(self, params):
        self.CunionIds = params.get("CunionIds")


class DescribeRegistrationStatusResponse(AbstractModel):
    """DescribeRegistrationStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 终端用户注册状态列表
        :type Data: list of RegisteredStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RegisteredStatus()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRunLogRequest(AbstractModel):
    """DescribeRunLog请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        """
        self.Tid = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")


class DescribeRunLogResponse(AbstractModel):
    """DescribeRunLog返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备运行日志文本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeStorageServiceRequest(AbstractModel):
    """DescribeStorageService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 云存服务ID
        :type ServiceId: str
        :param GetFinishedOrder: 是否返回已结束的订单信息(已过期/已退订/已转移)
        :type GetFinishedOrder: bool
        """
        self.ServiceId = None
        self.GetFinishedOrder = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.GetFinishedOrder = params.get("GetFinishedOrder")


class DescribeStorageServiceResponse(AbstractModel):
    """DescribeStorageService返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 云存服务ID
        :type ServiceId: str
        :param StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param Tid: 设备TID
        :type Tid: str
        :param ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param StartTime: 服务开始时间
        :type StartTime: int
        :param EndTime: 服务失效时间
        :type EndTime: int
        :param Status: 服务状态
        :type Status: int
        :param Data: 云存定单列表
        :type Data: list of StorageOrder
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceId = None
        self.StorageRegion = None
        self.Tid = None
        self.ChnNum = None
        self.AccessId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StorageRegion = params.get("StorageRegion")
        self.Tid = params.get("Tid")
        self.ChnNum = params.get("ChnNum")
        self.AccessId = params.get("AccessId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTraceIdsRequest(AbstractModel):
    """DescribeTraceIds请求参数结构体

    """


class DescribeTraceIdsResponse(AbstractModel):
    """DescribeTraceIds返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备TID列表，列表元素之间以“,”分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeTraceStatusRequest(AbstractModel):
    """DescribeTraceStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: 设备TID列表
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DescribeTraceStatusResponse(AbstractModel):
    """DescribeTraceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备追踪状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TraceStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TraceStatus()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DevTokenInfo(AbstractModel):
    """用于终端用户临时访问设备的token授权信息

    """

    def __init__(self):
        """
        :param AccessId: 客户的终端用户在IotVideo上的唯一标识id
        :type AccessId: str
        :param Tid: 设备TID
        :type Tid: str
        :param AccessToken: IotVideo平台的accessToken
        :type AccessToken: str
        :param ExpireTime: Token的过期时间，单位秒(UTC时间)
        :type ExpireTime: int
        """
        self.AccessId = None
        self.Tid = None
        self.AccessToken = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tid = params.get("Tid")
        self.AccessToken = params.get("AccessToken")
        self.ExpireTime = params.get("ExpireTime")


class DeviceCertificate(AbstractModel):
    """设备证书及密钥

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param Certificate: 设备初始证书信息，base64编码
        :type Certificate: str
        :param WhiteBoxSoUrl: 设备私钥下载地址
        :type WhiteBoxSoUrl: str
        """
        self.Tid = None
        self.Certificate = None
        self.WhiteBoxSoUrl = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Certificate = params.get("Certificate")
        self.WhiteBoxSoUrl = params.get("WhiteBoxSoUrl")


class DeviceData(AbstractModel):
    """设备信息

    """

    def __init__(self):
        """
        :param Tid: 设备TID
注意：此字段可能返回 null，表示取不到有效值。
        :type Tid: str
        :param ActiveTime: 激活时间 0代表未激活
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveTime: int
        :param Disabled: 设备是否被禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type Disabled: bool
        :param OtaVersion: 固件版本
注意：此字段可能返回 null，表示取不到有效值。
        :type OtaVersion: str
        :param Online: 设备在线状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: int
        :param LastOnlineTime: 设备最后上线时间（mqtt连接成功时间），UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOnlineTime: int
        :param IotModel: 物模型json数据
注意：此字段可能返回 null，表示取不到有效值。
        :type IotModel: str
        :param DeviceName: 设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param Certificate: 设备初始证书信息，base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param WhiteBoxSoUrl: 设备私钥下载地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WhiteBoxSoUrl: str
        :param StreamStatus: 设备推流状态
注意：此字段可能返回 null，表示取不到有效值。
        :type StreamStatus: bool
        """
        self.Tid = None
        self.ActiveTime = None
        self.Disabled = None
        self.OtaVersion = None
        self.Online = None
        self.LastOnlineTime = None
        self.IotModel = None
        self.DeviceName = None
        self.ProductId = None
        self.Certificate = None
        self.WhiteBoxSoUrl = None
        self.StreamStatus = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.ActiveTime = params.get("ActiveTime")
        self.Disabled = params.get("Disabled")
        self.OtaVersion = params.get("OtaVersion")
        self.Online = params.get("Online")
        self.LastOnlineTime = params.get("LastOnlineTime")
        self.IotModel = params.get("IotModel")
        self.DeviceName = params.get("DeviceName")
        self.ProductId = params.get("ProductId")
        self.Certificate = params.get("Certificate")
        self.WhiteBoxSoUrl = params.get("WhiteBoxSoUrl")
        self.StreamStatus = params.get("StreamStatus")


class DeviceModelData(AbstractModel):
    """设备物模型数据

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param Branch: 物模型分支路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Branch: str
        :param IotModel: 物模型数据
注意：此字段可能返回 null，表示取不到有效值。
        :type IotModel: str
        """
        self.Tid = None
        self.Branch = None
        self.IotModel = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Branch = params.get("Branch")
        self.IotModel = params.get("IotModel")


class DevicesData(AbstractModel):
    """设备列表元素所包含的设备基本信息

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ActiveTime: 激活时间 0代表未激活
        :type ActiveTime: int
        :param Disabled: 设备是否被禁用
        :type Disabled: bool
        :param StreamStatus: 设备推流状态
        :type StreamStatus: bool
        :param OtaVersion: 固件版本
        :type OtaVersion: str
        :param Online: 设备在线状态
        :type Online: int
        :param LastOnlineTime: 设备最后上线时间（mqtt连接成功时间），UNIX时间戳，单位秒
        :type LastOnlineTime: int
        :param IotModel: 物模型json数据
        :type IotModel: str
        :param LastUpdateTime: 设备固件最新更新时间，UNIX时间戳，单位秒
        :type LastUpdateTime: int
        """
        self.Tid = None
        self.DeviceName = None
        self.ActiveTime = None
        self.Disabled = None
        self.StreamStatus = None
        self.OtaVersion = None
        self.Online = None
        self.LastOnlineTime = None
        self.IotModel = None
        self.LastUpdateTime = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.DeviceName = params.get("DeviceName")
        self.ActiveTime = params.get("ActiveTime")
        self.Disabled = params.get("Disabled")
        self.StreamStatus = params.get("StreamStatus")
        self.OtaVersion = params.get("OtaVersion")
        self.Online = params.get("Online")
        self.LastOnlineTime = params.get("LastOnlineTime")
        self.IotModel = params.get("IotModel")
        self.LastUpdateTime = params.get("LastUpdateTime")


class DisableDeviceRequest(AbstractModel):
    """DisableDevice请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: 设备TID ≤100
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DisableDeviceResponse(AbstractModel):
    """DisableDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableDeviceStreamRequest(AbstractModel):
    """DisableDeviceStream请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: 设备TID列表
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DisableDeviceStreamResponse(AbstractModel):
    """DisableDeviceStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableOtaVersionRequest(AbstractModel):
    """DisableOtaVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.Operator = params.get("Operator")


class DisableOtaVersionResponse(AbstractModel):
    """DisableOtaVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IotModelData(AbstractModel):
    """物模型历史版本

    """

    def __init__(self):
        """
        :param Revision: 版本号
        :type Revision: int
        :param ReleaseTime: 发布时间
        :type ReleaseTime: int
        """
        self.Revision = None
        self.ReleaseTime = None


    def _deserialize(self, params):
        self.Revision = params.get("Revision")
        self.ReleaseTime = params.get("ReleaseTime")


class LogData(AbstractModel):
    """设备日志信息

    """

    def __init__(self):
        """
        :param Occurtime: 发生时间 UNIX时间戳，单位秒
        :type Occurtime: int
        :param LogType: 日志类型 1在线状态变更 2FP变更 3SP变更 4CO控制 5ST变更 6EV事件
        :type LogType: int
        :param DataObject: 物模型对象索引
注意：此字段可能返回 null，表示取不到有效值。
        :type DataObject: str
        :param OldValue: 物模型旧值  json串
注意：此字段可能返回 null，表示取不到有效值。
        :type OldValue: str
        :param NewValue: 物模型新值  json串
注意：此字段可能返回 null，表示取不到有效值。
        :type NewValue: str
        """
        self.Occurtime = None
        self.LogType = None
        self.DataObject = None
        self.OldValue = None
        self.NewValue = None


    def _deserialize(self, params):
        self.Occurtime = params.get("Occurtime")
        self.LogType = params.get("LogType")
        self.DataObject = params.get("DataObject")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")


class ModifyDeviceActionRequest(AbstractModel):
    """ModifyDeviceAction请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param Wakeup: 如果设备处于休眠状态，是否唤醒设备
        :type Wakeup: bool
        :param Branch: 物模型的分支路径
        :type Branch: str
        :param Value: 写入的物模型数据，如果是json需要转义成字符串
        :type Value: str
        :param IsNum: Value字段的类型是否为数值（float、int）
        :type IsNum: bool
        """
        self.Tid = None
        self.Wakeup = None
        self.Branch = None
        self.Value = None
        self.IsNum = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Wakeup = params.get("Wakeup")
        self.Branch = params.get("Branch")
        self.Value = params.get("Value")
        self.IsNum = params.get("IsNum")


class ModifyDeviceActionResponse(AbstractModel):
    """ModifyDeviceAction返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备端的响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param TaskId: 任务ID
若设备端未能及时响应时，会返回此字段，用户可以通过DescribeModelDataRet获取设备的最终响应结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyDevicePropertyRequest(AbstractModel):
    """ModifyDeviceProperty请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param Wakeup: 如果设备处于休眠状态，是否唤醒设备
        :type Wakeup: bool
        :param Branch: 物模型的分支路径
        :type Branch: str
        :param Value: 写入的物模型数据，如果是json需要转义成字符串
        :type Value: str
        :param IsNum: Value字段是否为数值（float、int）
        :type IsNum: bool
        """
        self.Tid = None
        self.Wakeup = None
        self.Branch = None
        self.Value = None
        self.IsNum = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Wakeup = params.get("Wakeup")
        self.Branch = params.get("Branch")
        self.Value = params.get("Value")
        self.IsNum = params.get("IsNum")


class ModifyDevicePropertyResponse(AbstractModel):
    """ModifyDeviceProperty返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductDescription: 产品描述
        :type ProductDescription: str
        :param ChipManufactureId: 主芯片产商ID
        :type ChipManufactureId: str
        :param ChipId: 主芯片ID
        :type ChipId: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDescription = None
        self.ChipManufactureId = None
        self.ChipId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVerContentRequest(AbstractModel):
    """ModifyVerContent请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id,大于0的有符号长整型
        :type ProductId: int
        :param OtaVersion: 需要修改的版本号
        :type OtaVersion: str
        :param Operator: 操作人,字符长度<=64
        :type Operator: str
        :param Remark: 备注信息
        :type Remark: str
        :param Contents: 版本发布的描述信息，需要国际化，可以为空
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        self.ProductId = None
        self.OtaVersion = None
        self.Operator = None
        self.Remark = None
        self.Contents = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.Operator = params.get("Operator")
        self.Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self.Contents = Contents()
            self.Contents._deserialize(params.get("Contents"))


class ModifyVerContentResponse(AbstractModel):
    """ModifyVerContent返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MsgQueueData(AbstractModel):
    """产品转发消息队列配置

    """

    def __init__(self):
        """
        :param MsgQueueType: 消息队列类型 1：CMQ 2：kafka
        :type MsgQueueType: int
        :param MsgType: 消息类型列表，整型值（0-31）之间以“,”分隔
        :type MsgType: str
        :param Topic: 主题名称
        :type Topic: str
        :param Instance: 实例名称
        :type Instance: str
        :param MsgRegion: 消息地域
        :type MsgRegion: str
        """
        self.MsgQueueType = None
        self.MsgType = None
        self.Topic = None
        self.Instance = None
        self.MsgRegion = None


    def _deserialize(self, params):
        self.MsgQueueType = params.get("MsgQueueType")
        self.MsgType = params.get("MsgType")
        self.Topic = params.get("Topic")
        self.Instance = params.get("Instance")
        self.MsgRegion = params.get("MsgRegion")


class OsData(AbstractModel):
    """操作系统信息

    """

    def __init__(self):
        """
        :param ChipId: 芯片型号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipId: str
        :param ChipManufacture: 芯片厂商
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipManufacture: str
        """
        self.ChipId = None
        self.ChipManufacture = None


    def _deserialize(self, params):
        self.ChipId = params.get("ChipId")
        self.ChipManufacture = params.get("ChipManufacture")


class OtaPubHistory(AbstractModel):
    """产品发布过的全部版本

    """

    def __init__(self):
        """
        :param OtaVersion: 版本名称
        :type OtaVersion: str
        :param PublishTime: 发布时间，unix时间戳，单位：秒
        :type PublishTime: int
        """
        self.OtaVersion = None
        self.PublishTime = None


    def _deserialize(self, params):
        self.OtaVersion = params.get("OtaVersion")
        self.PublishTime = params.get("PublishTime")


class ProductBase(AbstractModel):
    """产品信息摘要

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductModel: 产器型号(APP产品,为APP包名)
        :type ProductModel: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param CreateTime: 创建时间，UNIX 时间戳，单位秒
        :type CreateTime: int
        :param IotModelRevision: 物模型发布版本号,0代表物模型尚未发布
        :type IotModelRevision: int
        :param SecretKey: 产品密钥
        :type SecretKey: str
        :param FuncCode: 设备功能码
ypsxth : 音频双向通话;	
spdxth : 视频单向通话(监控);
NVR0824 : NVR设备,大于8路，小于等于24路;
WifiKeepalive : Wifi保活(低功耗产品);
Alexa : Alexa接入;
Google : Google接入;
注意：此字段可能返回 null，表示取不到有效值。
        :type FuncCode: list of str
        :param ProductCate: 产品类别，0 : 普通视频设备；1 : NVR设备
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCate: int
        :param ProductRegion: 产品地域
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
India（印度）
Other-Overseas（其他境外地区）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductRegion: str
        """
        self.ProductId = None
        self.ProductModel = None
        self.ProductName = None
        self.ProductDescription = None
        self.CreateTime = None
        self.IotModelRevision = None
        self.SecretKey = None
        self.FuncCode = None
        self.ProductCate = None
        self.ProductRegion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductModel = params.get("ProductModel")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.CreateTime = params.get("CreateTime")
        self.IotModelRevision = params.get("IotModelRevision")
        self.SecretKey = params.get("SecretKey")
        self.FuncCode = params.get("FuncCode")
        self.ProductCate = params.get("ProductCate")
        self.ProductRegion = params.get("ProductRegion")


class ProductData(AbstractModel):
    """产品信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param ProductDescription: 产品描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductDescription: str
        :param CreateTime: 创建时间，UNIX 时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param IotModelRevision: 物模型发布版本号,0代表物模型尚未发布
注意：此字段可能返回 null，表示取不到有效值。
        :type IotModelRevision: int
        :param SecretKey: 产品密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param Features: 设备功能码
注意：此字段可能返回 null，表示取不到有效值。
        :type Features: list of str
        :param ProductModel: 产器型号(APP产品,为APP包名)
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductModel: str
        :param ChipManufactureId: 主芯片厂商id
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipManufactureId: str
        :param ChipId: 主芯片型号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChipId: str
        :param ProductCate: 产品类别，0：普通视频设备；1：NVR设备
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCate: int
        :param ProductRegion: 产品地区
China-Mainland（中国大陆）
China-Hong Kong, Macao and Taiwan（港澳台地区）
America（美国）
Europe（欧洲）
India（印度）
Other-Overseas（其他境外地区）
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductRegion: str
        :param AccessMode: 接入模型，bit0是0：公版小程序未接入，bit0是1：公版小程序已接入
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessMode: int
        :param Os: linux,android,liteos
注意：此字段可能返回 null，表示取不到有效值。
        :type Os: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDescription = None
        self.CreateTime = None
        self.IotModelRevision = None
        self.SecretKey = None
        self.Features = None
        self.ProductModel = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductCate = None
        self.ProductRegion = None
        self.AccessMode = None
        self.Os = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.CreateTime = params.get("CreateTime")
        self.IotModelRevision = params.get("IotModelRevision")
        self.SecretKey = params.get("SecretKey")
        self.Features = params.get("Features")
        self.ProductModel = params.get("ProductModel")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductCate = params.get("ProductCate")
        self.ProductRegion = params.get("ProductRegion")
        self.AccessMode = params.get("AccessMode")
        self.Os = params.get("Os")


class RefundStorageServiceRequest(AbstractModel):
    """RefundStorageService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 云存服务ID
        :type ServiceId: str
        :param OrderId: 云存子订单ID。如果指定子订单ID,则仅退订该子订单，如果未指定子定单ID，则退订所有子订单
        :type OrderId: str
        """
        self.ServiceId = None
        self.OrderId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.OrderId = params.get("OrderId")


class RefundStorageServiceResponse(AbstractModel):
    """RefundStorageService返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 云存服务ID
        :type ServiceId: str
        :param StorageRegion: 云存服务所在的区域
        :type StorageRegion: str
        :param Tid: 设备TID
        :type Tid: str
        :param ChnNum: 视频流通道号。(对于存在多路视频流的设备，如NVR设备，与设备实际视频流通道号对应)
        :type ChnNum: int
        :param AccessId: 终端用户在IoT Video平台的注册ID
        :type AccessId: str
        :param StartTime: 服务开始时间
        :type StartTime: int
        :param EndTime: 服务失效时间
        :type EndTime: int
        :param Status: 服务状态
        :type Status: int
        :param Data: 有效云存定单列表
        :type Data: list of StorageOrder
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceId = None
        self.StorageRegion = None
        self.Tid = None
        self.ChnNum = None
        self.AccessId = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StorageRegion = params.get("StorageRegion")
        self.Tid = params.get("Tid")
        self.ChnNum = params.get("ChnNum")
        self.AccessId = params.get("AccessId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = StorageOrder()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class RegisteredStatus(AbstractModel):
    """终端用户注册状态

    """

    def __init__(self):
        """
        :param CunionId: 终端用户的唯一ID
        :type CunionId: str
        :param IsRegisted: 注册状态
        :type IsRegisted: bool
        """
        self.CunionId = None
        self.IsRegisted = None


    def _deserialize(self, params):
        self.CunionId = params.get("CunionId")
        self.IsRegisted = params.get("IsRegisted")


class RunDeviceRequest(AbstractModel):
    """RunDevice请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: TID列表 ≤100
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class RunDeviceResponse(AbstractModel):
    """RunDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunDeviceStreamRequest(AbstractModel):
    """RunDeviceStream请求参数结构体

    """

    def __init__(self):
        """
        :param Tids: 设备TID 列表
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class RunDeviceStreamResponse(AbstractModel):
    """RunDeviceStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunIotModelRequest(AbstractModel):
    """RunIotModel请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param IotModel: 物模型定义，json格式的字符串
        :type IotModel: str
        """
        self.ProductId = None
        self.IotModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.IotModel = params.get("IotModel")


class RunIotModelResponse(AbstractModel):
    """RunIotModel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunOtaVersionRequest(AbstractModel):
    """RunOtaVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param GrayValue: 灰度值,取值范围0-100，为0时相当于暂停发布
        :type GrayValue: int
        :param OldVersions: 指定的旧版本
        :type OldVersions: list of str
        :param Operator: 操作人
        :type Operator: str
        :param Remark: 备注信息
        :type Remark: str
        :param Contents: 版本发布的描述信息，需要国际化，可以为空
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        self.ProductId = None
        self.OtaVersion = None
        self.GrayValue = None
        self.OldVersions = None
        self.Operator = None
        self.Remark = None
        self.Contents = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.GrayValue = params.get("GrayValue")
        self.OldVersions = params.get("OldVersions")
        self.Operator = params.get("Operator")
        self.Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self.Contents = Contents()
            self.Contents._deserialize(params.get("Contents"))


class RunOtaVersionResponse(AbstractModel):
    """RunOtaVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunTestOtaVersionRequest(AbstractModel):
    """RunTestOtaVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param Tids: 指定可升级的设备TID
        :type Tids: list of str
        :param Operator: 操作人
        :type Operator: str
        :param Remark: 备注信息
        :type Remark: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.Tids = None
        self.Operator = None
        self.Remark = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.Tids = params.get("Tids")
        self.Operator = params.get("Operator")
        self.Remark = params.get("Remark")


class RunTestOtaVersionResponse(AbstractModel):
    """RunTestOtaVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendOnlineMsgRequest(AbstractModel):
    """SendOnlineMsg请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param Wakeup: 如果设备处于休眠状态，是否唤醒设备
        :type Wakeup: bool
        :param WaitResp: 等待回应类型
0：不等待设备回应直接响应请求;
1：要求设备确认消息已接收,或等待超时后返回;
2：要求设备进行响应处理,收到设备的响应数据后,将设备响应数据回应给请求方;
        :type WaitResp: int
        :param MsgTopic: 消息主题
        :type MsgTopic: str
        :param MsgContent: 消息内容，最大长度不超过8k字节
        :type MsgContent: str
        """
        self.Tid = None
        self.Wakeup = None
        self.WaitResp = None
        self.MsgTopic = None
        self.MsgContent = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Wakeup = params.get("Wakeup")
        self.WaitResp = params.get("WaitResp")
        self.MsgTopic = params.get("MsgTopic")
        self.MsgContent = params.get("MsgContent")


class SendOnlineMsgResponse(AbstractModel):
    """SendOnlineMsg返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 若返回此项则表明需要用户用此taskID进行查询请求是否成功(只有waitresp不等于0的情况下才可能会返回该taskID项)
        :type TaskId: str
        :param Data: 设备响应信息
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class SetMessageQueueRequest(AbstractModel):
    """SetMessageQueue请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param MsgQueueType: 消息队列类型 1-CMQ; 2-Ckafka
        :type MsgQueueType: int
        :param MsgType: 消息类型,整型值（0-31）之间以“,”分隔
0：在线状态变更
1.固件版本变更
2.设置参数变更
3.控制状态变更
4.状态信息变更
5.事件发布
        :type MsgType: str
        :param Topic: 消息队列主题，不超过32字符
        :type Topic: str
        :param Instance: kafka消息队列的实例名，不超过64字符
        :type Instance: str
        :param MsgRegion: 消息地域，不超过32字符
        :type MsgRegion: str
        """
        self.ProductId = None
        self.MsgQueueType = None
        self.MsgType = None
        self.Topic = None
        self.Instance = None
        self.MsgRegion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.MsgQueueType = params.get("MsgQueueType")
        self.MsgType = params.get("MsgType")
        self.Topic = params.get("Topic")
        self.Instance = params.get("Instance")
        self.MsgRegion = params.get("MsgRegion")


class SetMessageQueueResponse(AbstractModel):
    """SetMessageQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StorageOrder(AbstractModel):
    """云存订单信息

    """

    def __init__(self):
        """
        :param OrderId: 定单唯一性ID
        :type OrderId: str
        :param PkgId: 云存套餐ID
        :type PkgId: str
        :param Status: 定单服务状态
        :type Status: int
        :param StartTime: 定单服务生效时间
        :type StartTime: int
        :param EndTime: 定单服务失效时间
        :type EndTime: int
        """
        self.OrderId = None
        self.PkgId = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.PkgId = params.get("PkgId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class SystemType(AbstractModel):
    """系统类型

    """

    def __init__(self):
        """
        :param Android: 安卓系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Android: list of OsData
        :param Linux: linux系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Linux: list of OsData
        :param LiteOs: LiteOs系统
注意：此字段可能返回 null，表示取不到有效值。
        :type LiteOs: list of OsData
        """
        self.Android = None
        self.Linux = None
        self.LiteOs = None


    def _deserialize(self, params):
        if params.get("Android") is not None:
            self.Android = []
            for item in params.get("Android"):
                obj = OsData()
                obj._deserialize(item)
                self.Android.append(obj)
        if params.get("Linux") is not None:
            self.Linux = []
            for item in params.get("Linux"):
                obj = OsData()
                obj._deserialize(item)
                self.Linux.append(obj)
        if params.get("LiteOs") is not None:
            self.LiteOs = []
            for item in params.get("LiteOs"):
                obj = OsData()
                obj._deserialize(item)
                self.LiteOs.append(obj)


class TraceStatus(AbstractModel):
    """布尔值，标识指定设备是否在白名单中

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param IsExist: 设备追踪状态
        :type IsExist: bool
        """
        self.Tid = None
        self.IsExist = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.IsExist = params.get("IsExist")


class UpgradeDeviceRequest(AbstractModel):
    """UpgradeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param Tid: 设备TID
        :type Tid: str
        :param OtaVersion: 固件版本号
        :type OtaVersion: str
        :param UpgradeNow: 是否立即升级
        :type UpgradeNow: bool
        """
        self.Tid = None
        self.OtaVersion = None
        self.UpgradeNow = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.OtaVersion = params.get("OtaVersion")
        self.UpgradeNow = params.get("UpgradeNow")


class UpgradeDeviceResponse(AbstractModel):
    """UpgradeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备端返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UploadOtaVersionRequest(AbstractModel):
    """UploadOtaVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param OtaVersion: 固件版本号，格式为x.y.z， x，y 范围0-63，z范围1~524288
        :type OtaVersion: str
        :param VersionUrl: 固件版本URL
        :type VersionUrl: str
        :param FileSize: 文件大小，单位：byte
        :type FileSize: int
        :param Md5: 文件md5校验码（32字符）
        :type Md5: str
        :param Operator: 操作人
        :type Operator: str
        :param Remark: 备注信息
        :type Remark: str
        :param Contents: 版本发布的描述信息，需要国际化，可以为空
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        self.ProductId = None
        self.OtaVersion = None
        self.VersionUrl = None
        self.FileSize = None
        self.Md5 = None
        self.Operator = None
        self.Remark = None
        self.Contents = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.VersionUrl = params.get("VersionUrl")
        self.FileSize = params.get("FileSize")
        self.Md5 = params.get("Md5")
        self.Operator = params.get("Operator")
        self.Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self.Contents = Contents()
            self.Contents._deserialize(params.get("Contents"))


class UploadOtaVersionResponse(AbstractModel):
    """UploadOtaVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VersionData(AbstractModel):
    """固件版本详细信息

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param OtaVersion: 固件版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OtaVersion: str
        :param PubStatus: 版本类型 1未发布 2测试发布 3正式发布 4禁用
注意：此字段可能返回 null，表示取不到有效值。
        :type PubStatus: int
        :param VersionUrl: 固件版本存储路径URL
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionUrl: str
        :param FileSize: 文件大小，byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param Md5: 文件校验码
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param OldVersions: 指定的允许升级的旧版本，PubStatus=3时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type OldVersions: str
        :param Tids: 指定的允许升级的旧设备id，PubStatus=2时有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Tids: str
        :param GrayValue: 灰度值（0-100）,PubStatus=3时有效，表示n%的升级总量
注意：此字段可能返回 null，表示取不到有效值。
        :type GrayValue: int
        :param PublishTime: 最近一次发布时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishTime: int
        :param ActiveCount: 此版本激活的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveCount: int
        :param OnlineCount: 此版本在线的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineCount: int
        :param UpdateTime: 上传固件文件的时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param UploadTime: 发布记录的最后变更时间，UNIX时间戳，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadTime: int
        :param ModifyTimes: 该固件版本发布的变更次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTimes: int
        :param Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Contents: 版本发布的描述信息，需要国际化，可以为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Contents: :class:`tencentcloud.iotvideo.v20191126.models.Contents`
        """
        self.ProductId = None
        self.OtaVersion = None
        self.PubStatus = None
        self.VersionUrl = None
        self.FileSize = None
        self.Md5 = None
        self.OldVersions = None
        self.Tids = None
        self.GrayValue = None
        self.PublishTime = None
        self.ActiveCount = None
        self.OnlineCount = None
        self.UpdateTime = None
        self.UploadTime = None
        self.ModifyTimes = None
        self.Remark = None
        self.Contents = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.PubStatus = params.get("PubStatus")
        self.VersionUrl = params.get("VersionUrl")
        self.FileSize = params.get("FileSize")
        self.Md5 = params.get("Md5")
        self.OldVersions = params.get("OldVersions")
        self.Tids = params.get("Tids")
        self.GrayValue = params.get("GrayValue")
        self.PublishTime = params.get("PublishTime")
        self.ActiveCount = params.get("ActiveCount")
        self.OnlineCount = params.get("OnlineCount")
        self.UpdateTime = params.get("UpdateTime")
        self.UploadTime = params.get("UploadTime")
        self.ModifyTimes = params.get("ModifyTimes")
        self.Remark = params.get("Remark")
        if params.get("Contents") is not None:
            self.Contents = Contents()
            self.Contents._deserialize(params.get("Contents"))