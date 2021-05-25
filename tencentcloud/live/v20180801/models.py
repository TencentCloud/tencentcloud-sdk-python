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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param DelayTime: 延播时间，单位：秒，上限：600秒。
        :type DelayTime: int
        :param ExpireTime: 延播设置的过期时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：
1. 默认7天后过期，且最长支持7天内生效。
2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ExpireTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.DelayTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.DelayTime = params.get("DelayTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddDelayLiveStreamResponse(AbstractModel):
    """AddDelayLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddLiveDomainRequest(AbstractModel):
    """AddLiveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 域名名称。
        :type DomainName: str
        :param DomainType: 域名类型，
0：推流域名，
1：播放域名。
        :type DomainType: int
        :param PlayType: 拉流域名类型：
1：国内，
2：全球，
3：境外。
默认值：1。
        :type PlayType: int
        :param IsDelayLive: 是否是慢直播：
0： 普通直播，
1 ：慢直播 。
默认值： 0。
        :type IsDelayLive: int
        :param IsMiniProgramLive: 是否是小程序直播：
0： 标准直播，
1 ：小程序直播 。
默认值： 0。
        :type IsMiniProgramLive: int
        """
        self.DomainName = None
        self.DomainType = None
        self.PlayType = None
        self.IsDelayLive = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddLiveDomainResponse(AbstractModel):
    """AddLiveDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param PictureUrl: 水印图片 URL。
URL中禁止包含的字符：
 ;(){}$>`#"\'|
        :type PictureUrl: str
        :param WatermarkName: 水印名称。
最长16字节。
        :type WatermarkName: str
        :param XPosition: 显示位置，X轴偏移，单位是百分比，默认 0。
        :type XPosition: int
        :param YPosition: 显示位置，Y轴偏移，单位是百分比，默认 0。
        :type YPosition: int
        :param Width: 水印宽度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始宽度。
        :type Width: int
        :param Height: 水印高度，占直播原始画面高度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始高度。
        :type Height: int
        """
        self.PictureUrl = None
        self.WatermarkName = None
        self.XPosition = None
        self.YPosition = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.PictureUrl = params.get("PictureUrl")
        self.WatermarkName = params.get("WatermarkName")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddLiveWatermarkResponse(AbstractModel):
    """AddLiveWatermark返回参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WatermarkId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BandwidthInfo(AbstractModel):
    """带宽信息

    """

    def __init__(self):
        """
        :param Time: 返回格式：
yyyy-mm-dd HH:MM:SS
根据粒度会有不同程度的缩减。
        :type Time: str
        :param Bandwidth: 带宽。
        :type Bandwidth: float
        """
        self.Time = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BillAreaInfo(AbstractModel):
    """海外分区直播带宽出参，分区信息

    """

    def __init__(self):
        """
        :param Name: 大区名称
        :type Name: str
        :param Countrys: 国家明细数据
        :type Countrys: list of BillCountryInfo
        """
        self.Name = None
        self.Countrys = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Countrys") is not None:
            self.Countrys = []
            for item in params.get("Countrys"):
                obj = BillCountryInfo()
                obj._deserialize(item)
                self.Countrys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BillCountryInfo(AbstractModel):
    """海外分区直播带宽出参国家带宽信息

    """

    def __init__(self):
        """
        :param Name: 国家名称
        :type Name: str
        :param BandInfoList: 带宽明细数据信息。
        :type BandInfoList: list of BillDataInfo
        """
        self.Name = None
        self.BandInfoList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("BandInfoList") is not None:
            self.BandInfoList = []
            for item in params.get("BandInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self.BandInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BillDataInfo(AbstractModel):
    """带宽和流量信息。

    """

    def __init__(self):
        """
        :param Time: 时间点，格式: yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Bandwidth: 带宽，单位是 Mbps。
        :type Bandwidth: float
        :param Flux: 流量，单位是 MB。
        :type Flux: float
        :param PeakTime: 峰值时间点，格式: yyyy-mm-dd HH:MM:SS，原始数据为5分钟粒度，如果查询小时和天粒度数据，则返回对应粒度内的带宽峰值时间点。
        :type PeakTime: str
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.PeakTime = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.PeakTime = params.get("PeakTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BindLiveDomainCertRequest(AbstractModel):
    """BindLiveDomainCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书Id。使用添加证书接口获取证书Id。
        :type CertId: int
        :param DomainName: 播放域名。
        :type DomainName: str
        :param Status: HTTPS开启状态，0： 关闭  1：打开。
        :type Status: int
        """
        self.CertId = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BindLiveDomainCertResponse(AbstractModel):
    """BindLiveDomainCert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CallBackRuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        """
        :param CreateTime: 规则创建时间。
        :type CreateTime: str
        :param UpdateTime: 规则更新时间。
        :type UpdateTime: str
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CallBackTemplateInfo(AbstractModel):
    """回调模板信息。

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param StreamBeginNotifyUrl: 开播回调 URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 断流回调 URL。
        :type StreamEndNotifyUrl: str
        :param StreamMixNotifyUrl: 混流回调 URL。
        :type StreamMixNotifyUrl: str
        :param RecordNotifyUrl: 录制回调 URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截图回调 URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鉴黄回调 URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回调的鉴权 key。
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.StreamMixNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CallbackEventInfo(AbstractModel):
    """回调事件信息

    """

    def __init__(self):
        """
        :param EventTime: 事件时间
        :type EventTime: str
        :param EventType: 事件类型
        :type EventType: int
        :param Request: 回调请求
        :type Request: str
        :param Response: 回调响应
        :type Response: str
        :param ResponseTime: 客户接口响应时间
        :type ResponseTime: str
        :param ResultCode: 回调结果
        :type ResultCode: int
        :param StreamId: 流名称
        :type StreamId: str
        """
        self.EventTime = None
        self.EventType = None
        self.Request = None
        self.Response = None
        self.ResponseTime = None
        self.ResultCode = None
        self.StreamId = None


    def _deserialize(self, params):
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Request = params.get("Request")
        self.Response = params.get("Response")
        self.ResponseTime = params.get("ResponseTime")
        self.ResultCode = params.get("ResultCode")
        self.StreamId = params.get("StreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelCommonMixStreamRequest(AbstractModel):
    """CancelCommonMixStream请求参数结构体

    """

    def __init__(self):
        """
        :param MixStreamSessionId: 混流会话（申请混流开始到取消混流结束）标识 ID。
该值与CreateCommonMixStream中的MixStreamSessionId保持一致。
        :type MixStreamSessionId: str
        """
        self.MixStreamSessionId = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelCommonMixStreamResponse(AbstractModel):
    """CancelCommonMixStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CdnPlayStatData(AbstractModel):
    """下行播放统计指标

    """

    def __init__(self):
        """
        :param Time: 时间点，格式: yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Bandwidth: 带宽，单位: Mbps。
        :type Bandwidth: float
        :param Flux: 流量，单位: MB。
        :type Flux: float
        :param Request: 新增请求数。
        :type Request: int
        :param Online: 并发连接数。
        :type Online: int
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.Request = None
        self.Online = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Request = params.get("Request")
        self.Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CertInfo(AbstractModel):
    """证书信息。

    """

    def __init__(self):
        """
        :param CertId: 证书 ID。
        :type CertId: int
        :param CertName: 证书名称。
        :type CertName: str
        :param Description: 描述信息。
        :type Description: str
        :param CreateTime: 创建时间，UTC 格式。
        :type CreateTime: str
        :param HttpsCrt: 证书内容。
        :type HttpsCrt: str
        :param CertType: 证书类型。
0：用户添加证书，
1：腾讯云托管证书。
        :type CertType: int
        :param CertExpireTime: 证书过期时间，UTC 格式。
        :type CertExpireTime: str
        :param DomainList: 使用此证书的域名列表。
        :type DomainList: list of str
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainList = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClientIpPlaySumInfo(AbstractModel):
    """客户端ip播放汇总信息。

    """

    def __init__(self):
        """
        :param ClientIp: 客户端 IP，点分型。
        :type ClientIp: str
        :param Province: 客户端所在省份。
        :type Province: str
        :param TotalFlux: 总流量。
        :type TotalFlux: float
        :param TotalRequest: 总请求数。
        :type TotalRequest: int
        :param TotalFailedRequest: 总失败请求数。
        :type TotalFailedRequest: int
        :param CountryArea: 客户端所在国家。
        :type CountryArea: str
        """
        self.ClientIp = None
        self.Province = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.TotalFailedRequest = None
        self.CountryArea = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.Province = params.get("Province")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.TotalFailedRequest = params.get("TotalFailedRequest")
        self.CountryArea = params.get("CountryArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommonMixControlParams(AbstractModel):
    """通用混流控制参数

    """

    def __init__(self):
        """
        :param UseMixCropCenter: 取值范围[0,1]。
填1时，当参数中图层分辨率参数与视频实际分辨率不一致时，自动从视频中按图层设置的分辨率比例进行裁剪。
        :type UseMixCropCenter: int
        :param AllowCopy: 取值范围[0,1]
填1时，当InputStreamList中个数为1时，且OutputParams.OutputStreamType为1时，不执行取消操作，执行拷贝流操作
        :type AllowCopy: int
        :param PassInputSei: 取值范围[0,1]
填1时，透传原始流的sei
        :type PassInputSei: int
        """
        self.UseMixCropCenter = None
        self.AllowCopy = None
        self.PassInputSei = None


    def _deserialize(self, params):
        self.UseMixCropCenter = params.get("UseMixCropCenter")
        self.AllowCopy = params.get("AllowCopy")
        self.PassInputSei = params.get("PassInputSei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommonMixCropParams(AbstractModel):
    """通用混流输入裁剪参数。

    """

    def __init__(self):
        """
        :param CropWidth: 裁剪的宽度。取值范围[0，2000]。
        :type CropWidth: float
        :param CropHeight: 裁剪的高度。取值范围[0，2000]。
        :type CropHeight: float
        :param CropStartLocationX: 裁剪的起始X坐标。取值范围[0，2000]。
        :type CropStartLocationX: float
        :param CropStartLocationY: 裁剪的起始Y坐标。取值范围[0，2000]。
        :type CropStartLocationY: float
        """
        self.CropWidth = None
        self.CropHeight = None
        self.CropStartLocationX = None
        self.CropStartLocationY = None


    def _deserialize(self, params):
        self.CropWidth = params.get("CropWidth")
        self.CropHeight = params.get("CropHeight")
        self.CropStartLocationX = params.get("CropStartLocationX")
        self.CropStartLocationY = params.get("CropStartLocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommonMixInputParam(AbstractModel):
    """通用混流输入参数。

    """

    def __init__(self):
        """
        :param InputStreamName: 输入流名称。80字节以内，仅含字母、数字以及下划线的字符串。
        :type InputStreamName: str
        :param LayoutParams: 输入流布局参数。
        :type LayoutParams: :class:`tencentcloud.live.v20180801.models.CommonMixLayoutParams`
        :param CropParams: 输入流裁剪参数。
        :type CropParams: :class:`tencentcloud.live.v20180801.models.CommonMixCropParams`
        """
        self.InputStreamName = None
        self.LayoutParams = None
        self.CropParams = None


    def _deserialize(self, params):
        self.InputStreamName = params.get("InputStreamName")
        if params.get("LayoutParams") is not None:
            self.LayoutParams = CommonMixLayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("CropParams") is not None:
            self.CropParams = CommonMixCropParams()
            self.CropParams._deserialize(params.get("CropParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommonMixLayoutParams(AbstractModel):
    """通用混流布局参数。

    """

    def __init__(self):
        """
        :param ImageLayer: 输入图层。取值范围[1，16]。
1)背景流（即大主播画面或画布）的 image_layer 填1。
2)纯音频混流，该参数也需填。
        :type ImageLayer: int
        :param InputType: 输入类型。取值范围[0，5]。
不填默认为0。
0表示输入流为音视频。
2表示输入流为图片。
3表示输入流为画布。 
4表示输入流为音频。
5表示输入流为纯视频。
        :type InputType: int
        :param ImageWidth: 输入画面在输出时的宽度。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为输入流的宽度。
使用百分比时，期望输出为（百分比 * 背景宽）。
        :type ImageWidth: float
        :param ImageHeight: 输入画面在输出时的高度。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为输入流的高度。
使用百分比时，期望输出为（百分比 * 背景高）。
        :type ImageHeight: float
        :param LocationX: 输入在输出画面的X偏移。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为0。
相对于大主播背景画面左上角的横向偏移。 
使用百分比时，期望输出为（百分比 * 背景宽）。
        :type LocationX: float
        :param LocationY: 输入在输出画面的Y偏移。取值范围：
像素：[0，2000]
百分比：[0.01，0.99]
不填默认为0。
相对于大主播背景画面左上角的纵向偏移。 
使用百分比时，期望输出为（百分比 * 背景宽）
        :type LocationY: float
        :param Color: 当InputType为3(画布)时，该值表示画布的颜色。
常用的颜色有：
红色：0xcc0033。
黄色：0xcc9900。
绿色：0xcccc33。
蓝色：0x99CCFF。
黑色：0x000000。
白色：0xFFFFFF。
灰色：0x999999。
        :type Color: str
        :param WatermarkId: 当InputType为2(图片)时，该值是水印ID。
        :type WatermarkId: int
        """
        self.ImageLayer = None
        self.InputType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.Color = None
        self.WatermarkId = None


    def _deserialize(self, params):
        self.ImageLayer = params.get("ImageLayer")
        self.InputType = params.get("InputType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.Color = params.get("Color")
        self.WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommonMixOutputParams(AbstractModel):
    """通用混流输出参数。

    """

    def __init__(self):
        """
        :param OutputStreamName: 输出流名称。
        :type OutputStreamName: str
        :param OutputStreamType: 输出流类型，取值范围[0,1]。
不填默认为0。
当输出流为输入流 list 中的一条时，填写0。
当期望生成的混流结果成为一条新流时，该值填为1。
该值为1时，output_stream_id 不能出现在 input_stram_list 中，且直播后台中，不能存在相同 ID 的流。
        :type OutputStreamType: int
        :param OutputStreamBitRate: 输出流比特率。取值范围[1，50000]。
不填的情况下，系统会自动判断。
        :type OutputStreamBitRate: int
        :param OutputStreamGop: 输出流GOP大小。取值范围[1,10]。
不填的情况下，系统会自动判断。
        :type OutputStreamGop: int
        :param OutputStreamFrameRate: 输出流帧率大小。取值范围[1,60]。
不填的情况下，系统会自动判断。
        :type OutputStreamFrameRate: int
        :param OutputAudioBitRate: 输出流音频比特率。取值范围[1,500]
不填的情况下，系统会自动判断。
        :type OutputAudioBitRate: int
        :param OutputAudioSampleRate: 输出流音频采样率。取值范围[96000, 88200, 64000, 48000, 44100, 32000,24000, 22050, 16000, 12000, 11025, 8000]。
不填的情况下，系统会自动判断。
        :type OutputAudioSampleRate: int
        :param OutputAudioChannels: 输出流音频声道数。取值范围[1,2]。
不填的情况下，系统会自动判断。
        :type OutputAudioChannels: int
        :param MixSei: 输出流中的sei信息。如果无特殊需要，不填。
        :type MixSei: str
        """
        self.OutputStreamName = None
        self.OutputStreamType = None
        self.OutputStreamBitRate = None
        self.OutputStreamGop = None
        self.OutputStreamFrameRate = None
        self.OutputAudioBitRate = None
        self.OutputAudioSampleRate = None
        self.OutputAudioChannels = None
        self.MixSei = None


    def _deserialize(self, params):
        self.OutputStreamName = params.get("OutputStreamName")
        self.OutputStreamType = params.get("OutputStreamType")
        self.OutputStreamBitRate = params.get("OutputStreamBitRate")
        self.OutputStreamGop = params.get("OutputStreamGop")
        self.OutputStreamFrameRate = params.get("OutputStreamFrameRate")
        self.OutputAudioBitRate = params.get("OutputAudioBitRate")
        self.OutputAudioSampleRate = params.get("OutputAudioSampleRate")
        self.OutputAudioChannels = params.get("OutputAudioChannels")
        self.MixSei = params.get("MixSei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ConcurrentRecordStreamNum(AbstractModel):
    """并发录制路数

    """

    def __init__(self):
        """
        :param Time: 时间点。
        :type Time: str
        :param Num: 路数。
        :type Num: int
        """
        self.Time = None
        self.Num = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCommonMixStreamRequest(AbstractModel):
    """CreateCommonMixStream请求参数结构体

    """

    def __init__(self):
        """
        :param MixStreamSessionId: 混流会话（申请混流开始到取消混流结束）标识 ID。
        :type MixStreamSessionId: str
        :param InputStreamList: 混流输入流列表。
        :type InputStreamList: list of CommonMixInputParam
        :param OutputParams: 混流输出流参数。
        :type OutputParams: :class:`tencentcloud.live.v20180801.models.CommonMixOutputParams`
        :param MixStreamTemplateId: 输入模板 ID，若设置该参数，将按默认模板布局输出，无需填入自定义位置参数。
不填默认为0。
两输入源支持10，20，30，40，50。
三输入源支持310，390，391。
四输入源支持410。
五输入源支持510，590。
六输入源支持610。
        :type MixStreamTemplateId: int
        :param ControlParams: 混流的特殊控制参数。如无特殊需求，无需填写。
        :type ControlParams: :class:`tencentcloud.live.v20180801.models.CommonMixControlParams`
        """
        self.MixStreamSessionId = None
        self.InputStreamList = None
        self.OutputParams = None
        self.MixStreamTemplateId = None
        self.ControlParams = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = CommonMixInputParam()
                obj._deserialize(item)
                self.InputStreamList.append(obj)
        if params.get("OutputParams") is not None:
            self.OutputParams = CommonMixOutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        self.MixStreamTemplateId = params.get("MixStreamTemplateId")
        if params.get("ControlParams") is not None:
            self.ControlParams = CommonMixControlParams()
            self.ControlParams._deserialize(params.get("ControlParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCommonMixStreamResponse(AbstractModel):
    """CreateCommonMixStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveCallbackRuleRequest(AbstractModel):
    """CreateLiveCallbackRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param TemplateId: 模板ID。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveCallbackRuleResponse(AbstractModel):
    """CreateLiveCallbackRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveCallbackTemplateRequest(AbstractModel):
    """CreateLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称。
长度上限：255字节。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param Description: 描述信息。
长度上限：1024字节。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param StreamBeginNotifyUrl: 开播回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 断流回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 录制回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截图回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鉴黄回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32741)。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回调 Key，回调 URL 公用，回调签名详见事件消息通知文档。
[事件消息通知](/document/product/267/32744)。
        :type CallbackKey: str
        :param StreamMixNotifyUrl: 混流回调 URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type StreamMixNotifyUrl: str
        """
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None
        self.StreamMixNotifyUrl = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")
        self.StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveCallbackTemplateResponse(AbstractModel):
    """CreateLiveCallbackTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID。
        :type TemplateId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveCertRequest(AbstractModel):
    """CreateLiveCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertType: 证书类型。0-用户添加证书；1-腾讯云托管证书。
注意：当证书类型为0时，HttpsCrt和HttpsKey必选；
当证书类型为1时，优先使用CloudCertId对应证书，若CloudCertId为空则使用HttpsCrt和HttpsKey。
        :type CertType: int
        :param CertName: 证书名称。
        :type CertName: str
        :param HttpsCrt: 证书内容，即公钥。
        :type HttpsCrt: str
        :param HttpsKey: 私钥。
        :type HttpsKey: str
        :param Description: 描述。
        :type Description: str
        :param CloudCertId: 腾讯云证书托管ID。
        :type CloudCertId: str
        """
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None
        self.CloudCertId = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")
        self.CloudCertId = params.get("CloudCertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveCertResponse(AbstractModel):
    """CreateLiveCert返回参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书ID
        :type CertId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLivePullStreamTaskRequest(AbstractModel):
    """CreateLivePullStreamTask请求参数结构体

    """

    def __init__(self):
        """
        :param SourceType: 拉流源的类型：
PullLivePushLive -直播，
PullVodPushLive -点播。
        :type SourceType: str
        :param SourceUrls: 拉流源 url 列表。
SourceType 为直播（PullLivePushLive）只可以填1个，
SourceType 为点播（PullVodPushLive）可以填多个，上限30个。
当前支持的文件格式：flv，mp4，hls。
当前支持的拉流协议：http，https，rtmp。
        :type SourceUrls: list of str
        :param DomainName: 推流域名。
将拉取过来的流推到该域名。
注意：请使用已在云直播配置的推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
将拉取过来的流推到该路径。
        :type AppName: str
        :param StreamName: 推流名称。
将拉取过来的流推到该流名称。
        :type StreamName: str
        :param StartTime: 开始时间。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param Operator: 任务操作人备注。
        :type Operator: str
        :param PushArgs: 推流参数。
推流时携带自定义参数。
示例：
bak=1&test=2 。
        :type PushArgs: str
        :param CallbackEvents: 选择需要回调的事件（不填则回调全部）：
TaskStart：任务启动回调，
TaskExit：任务停止回调，
VodSourceFileStart：从点播源文件开始拉流回调，
VodSourceFileFinish：从点播源文件拉流结束回调，
ResetTaskConfig：任务更新回调。
        :type CallbackEvents: list of str
        :param VodLoopTimes: 点播拉流转推循环次数。默认：-1。
-1：无限循环，直到任务结束。
0：不循环。
>0：具体循环次数。次数和时间以先结束的为准。
注意：该配置仅对拉流源为点播时生效。
        :type VodLoopTimes: str
        :param VodRefreshType: 点播更新SourceUrls后的播放方式：
ImmediateNewSource：立即播放新的拉流源内容；
ContinueBreakPoint：播放完当前正在播放的点播 url 后再使用新的拉流源播放。（旧拉流源未播放的点播 url 不会再播放）

注意：该配置生效仅对变更前拉流源为点播时生效。
        :type VodRefreshType: str
        :param CallbackUrl: 自定义回调地址。
拉流转推任务相关事件会回调到该地址。
        :type CallbackUrl: str
        :param ExtraCmd: 其他参数。
示例: ignore_region  用于忽略传入地域, 内部按负载分配。
        :type ExtraCmd: str
        :param Comment: 任务描述，限制 512 字节。
        :type Comment: str
        """
        self.SourceType = None
        self.SourceUrls = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.Operator = None
        self.PushArgs = None
        self.CallbackEvents = None
        self.VodLoopTimes = None
        self.VodRefreshType = None
        self.CallbackUrl = None
        self.ExtraCmd = None
        self.Comment = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceUrls = params.get("SourceUrls")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Operator = params.get("Operator")
        self.PushArgs = params.get("PushArgs")
        self.CallbackEvents = params.get("CallbackEvents")
        self.VodLoopTimes = params.get("VodLoopTimes")
        self.VodRefreshType = params.get("VodRefreshType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.ExtraCmd = params.get("ExtraCmd")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLivePullStreamTaskResponse(AbstractModel):
    """CreateLivePullStreamTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 Id 。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param AppName: 推流路径，与推流和播放地址中的 AppName保持一致，默认为 live。
        :type AppName: str
        :param DomainName: 推流域名。多域名推流必须设置。
        :type DomainName: str
        :param StartTime: 录制开始时间。中国标准时间，需要 URLEncode(rfc3986)。如 2017-01-01 10:10:01，编码为：2017-01-01+10%3a10%3a01。
定时录制模式，必须设置该字段；实时视频录制模式，忽略该字段。
        :type StartTime: str
        :param EndTime: 录制结束时间。中国标准时间，需要 URLEncode(rfc3986)。如 2017-01-01 10:30:01，编码为：2017-01-01+10%3a30%3a01。
定时录制模式，必须设置该字段；实时录制模式，为可选字段。如果通过Highlight参数，设置录制为实时视频录制模式，其设置的结束时间不应超过当前时间+30分钟，如果设置的结束时间超过当前时间+30分钟或者小于当前时间或者不设置该参数，则实际结束时间为当前时间+30分钟。
        :type EndTime: str
        :param RecordType: 录制类型。
“video” : 音视频录制【默认】。
“audio” : 纯音频录制。
在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。
        :type RecordType: str
        :param FileFormat: 录制文件格式。其值为：
“flv”【默认】,“hls”,”mp4”,“aac”,”mp3”。
在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。
        :type FileFormat: str
        :param Highlight: 开启实时视频录制模式标志。
0：不开启实时视频录制模式，即定时录制模式【默认】。见[示例一](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。
1：开启实时视频录制模式。见[示例二](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。
        :type Highlight: int
        :param MixStream: 开启 A+B=C混流C流录制标志。
0：不开启 A+B=C混流C流录制【默认】。
1：开启 A+B=C混流C流录制。
在定时录制模式或实时视频录制模式下，该参数均有效。
        :type MixStream: int
        :param StreamParam: 录制流参数。当前支持以下参数：
record_interval - 录制分片时长，单位 秒，1800 - 7200。
storage_time - 录制文件存储时长，单位 秒。
eg. record_interval=3600&storage_time=2592000。
注：参数需要url encode。
在定时录制模式或实时视频录制模式下，该参数均有效。
        :type StreamParam: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StartTime = None
        self.EndTime = None
        self.RecordType = None
        self.FileFormat = None
        self.Highlight = None
        self.MixStream = None
        self.StreamParam = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RecordType = params.get("RecordType")
        self.FileFormat = params.get("FileFormat")
        self.Highlight = params.get("Highlight")
        self.MixStream = params.get("MixStream")
        self.StreamParam = params.get("StreamParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveRecordResponse(AbstractModel):
    """CreateLiveRecord返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID，全局唯一标识录制任务。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveRecordRuleRequest(AbstractModel):
    """CreateLiveRecordRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param StreamName: 流名称。
注：如果本参数设置为非空字符串，规则将只对此推流起作用。
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveRecordRuleResponse(AbstractModel):
    """CreateLiveRecordRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveRecordTemplateRequest(AbstractModel):
    """CreateLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名。仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param FlvParam: Flv录制参数，开启Flv录制时设置。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: Hls录制参数，开启hls录制时设置。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4录制参数，开启Mp4录制时设置。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: Aac录制参数，开启Aac录制时设置。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 直播类型，默认 0。
0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS专属录制参数。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: Mp3录制参数，开启Mp3录制时设置。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveRecordTemplateResponse(AbstractModel):
    """CreateLiveRecordTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveSnapshotRuleRequest(AbstractModel):
    """CreateLiveSnapshotRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        :param StreamName: 流名称。
注：如果本参数设置为非空字符串，规则将只对此推流起作用。
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveSnapshotRuleResponse(AbstractModel):
    """CreateLiveSnapshotRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveSnapshotTemplateRequest(AbstractModel):
    """CreateLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称。
长度上限：255字节。
仅支持中文、英文、数字、_、-。
        :type TemplateName: str
        :param CosAppId: Cos 应用 ID。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名称。
注：CosBucket参数值不能包含-[appid] 部分。
        :type CosBucket: str
        :param CosRegion: Cos地区。
        :type CosRegion: str
        :param Description: 描述信息。
长度上限：1024字节。
仅支持中文、英文、数字、_、-。
        :type Description: str
        :param SnapshotInterval: 截图间隔，单位s，默认10s。
范围： 5s ~ 300s。
        :type SnapshotInterval: int
        :param Width: 截图宽度。默认：0（原始宽）。
        :type Width: int
        :param Height: 截图高度。默认：0（原始高）。
        :type Height: int
        :param PornFlag: 是否开启鉴黄，0：不开启，1：开启。默认：0。
        :type PornFlag: int
        :param CosPrefix: Cos Bucket文件夹前缀。
如不传，实际按默认值
/{Year}-{Month}-{Day}
生效
        :type CosPrefix: str
        :param CosFileName: Cos 文件名称。
如不传，实际按默认值
{StreamID}-screenshot-{Hour}-{Minute}-{Second}-{Width}x{Height}{Ext}
生效
        :type CosFileName: str
        """
        self.TemplateName = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveSnapshotTemplateResponse(AbstractModel):
    """CreateLiveSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveTranscodeRuleRequest(AbstractModel):
    """CreateLiveTranscodeRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致。如果只绑定域名，则此处填空。
        :type AppName: str
        :param StreamName: 流名称。如果只绑定域名或路径，则此处填空。
        :type StreamName: str
        :param TemplateId: 指定已有的模板Id。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveTranscodeRuleResponse(AbstractModel):
    """CreateLiveTranscodeRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveTranscodeTemplateRequest(AbstractModel):
    """CreateLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称，例： 900p 仅支持字母和数字的组合。
长度限制：
  标准转码：1-10个字符
  极速高清转码：3-10个字符
        :type TemplateName: str
        :param VideoBitrate: 视频码率。范围：0kbps - 8000kbps。
0为保持原始码率。
注: 转码模板有码率唯一要求，最终保存的码率可能与输入码率有所差别。
        :type VideoBitrate: int
        :param Acodec: 音频编码：aac，默认aac。
注意：当前该参数未生效，待后续支持！
        :type Acodec: str
        :param AudioBitrate: 音频码率，默认0。
范围：0-500。
        :type AudioBitrate: int
        :param Vcodec: 视频编码：h264/h265/origin，默认origin。

origin: 保持原始编码格式
        :type Vcodec: str
        :param Description: 模板描述。
        :type Description: str
        :param NeedVideo: 是否保留视频，0：否，1：是。默认1。
        :type NeedVideo: int
        :param Width: 宽，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始宽度
        :type Width: int
        :param NeedAudio: 是否保留音频，0：否，1：是。默认1。
        :type NeedAudio: int
        :param Height: 高，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始高度。
        :type Height: int
        :param Fps: 帧率，默认0。
范围0-60fps
        :type Fps: int
        :param Gop: 关键帧间隔，单位：秒。
默认原始的间隔
范围2-6
        :type Gop: int
        :param Rotate: 旋转角度，默认0。
可取值：0，90，180，270
        :type Rotate: int
        :param Profile: 编码质量：
baseline/main/high。默认baseline
        :type Profile: str
        :param BitrateToOrig: 当设置的码率>原始码率时，是否以原始码率为准。
0：否， 1：是
默认 0。
        :type BitrateToOrig: int
        :param HeightToOrig: 当设置的高度>原始高度时，是否以原始高度为准。
0：否， 1：是
默认 0。
        :type HeightToOrig: int
        :param FpsToOrig: 当设置的帧率>原始帧率时，是否以原始帧率为准。
0：否， 1：是
默认 0。
        :type FpsToOrig: int
        :param AiTransCode: 是否是极速高清模板，0：否，1：是。默认0。
        :type AiTransCode: int
        :param AdaptBitratePercent: 极速高清视频码率压缩比。
极速高清目标码率=VideoBitrate * (1-AdaptBitratePercent)

取值范围：0.0到0.5
        :type AdaptBitratePercent: float
        :param ShortEdgeAsHeight: 是否以短边作为高度，0：否，1：是。默认0。
        :type ShortEdgeAsHeight: int
        """
        self.TemplateName = None
        self.VideoBitrate = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Vcodec = None
        self.Description = None
        self.NeedVideo = None
        self.Width = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.AiTransCode = None
        self.AdaptBitratePercent = None
        self.ShortEdgeAsHeight = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Vcodec = params.get("Vcodec")
        self.Description = params.get("Description")
        self.NeedVideo = params.get("NeedVideo")
        self.Width = params.get("Width")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")
        self.ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveTranscodeTemplateResponse(AbstractModel):
    """CreateLiveTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveWatermarkRuleRequest(AbstractModel):
    """CreateLiveWatermarkRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param TemplateId: 水印Id，即调用[AddLiveWatermark](/document/product/267/30154)接口返回的WatermarkId。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateLiveWatermarkRuleResponse(AbstractModel):
    """CreateLiveWatermarkRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePullStreamConfigRequest(AbstractModel):
    """CreatePullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param FromUrl: 源 Url ，用于拉流的地址。目前可支持直播流及点播文件。
注意：
1. 多个点播url之间使用空格拼接。
2. 目前上限支持10个url。
3. 支持拉流文件格式：flv，rtmp，hls，mp4。
        :type FromUrl: str
        :param ToUrl: 目的 Url ，用于推流的地址，目前限制该目标地址为腾讯域名。
仅支持：rtmp 协议。
        :type ToUrl: str
        :param AreaId: 选择完成转拉推的服务所在区域:
1-深圳，
2-上海，
3-天津，
4-中国香港。
        :type AreaId: int
        :param IspId: 选择完成转拉推服务使用的运营商网络：
1-电信，
2-移动，
3-联通，
4-其他。
注：AreaId 为4的时候，IspId 只能为其他。
        :type IspId: int
        :param StartTime: 开始时间。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用 UTC 格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        """
        self.FromUrl = None
        self.ToUrl = None
        self.AreaId = None
        self.IspId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaId = params.get("AreaId")
        self.IspId = params.get("IspId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePullStreamConfigResponse(AbstractModel):
    """CreatePullStreamConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置成功后的 ID。
        :type ConfigId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateRecordTaskRequest(AbstractModel):
    """CreateRecordTask请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param EndTime: 录制任务结束时间，Unix时间戳。设置时间必须大于StartTime，且EndTime - StartTime不能超过24小时。
        :type EndTime: int
        :param StartTime: 录制任务开始时间，Unix时间戳。如果不填表示立即启动录制。不超过从当前时间开始6天之内的时间。
        :type StartTime: int
        :param StreamType: 推流类型，默认0。取值：
0-直播推流。
1-合成流，即 A+B=C 类型混流。
        :type StreamType: int
        :param TemplateId: 录制模板ID，CreateLiveRecordTemplate 返回值。如果不填或者传入错误ID，则默认录制HLS格式、永久存储。
        :type TemplateId: int
        :param Extension: 扩展字段，暂无定义。默认为空。
        :type Extension: str
        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None
        self.EndTime = None
        self.StartTime = None
        self.StreamType = None
        self.TemplateId = None
        self.Extension = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.StreamType = params.get("StreamType")
        self.TemplateId = params.get("TemplateId")
        self.Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateRecordTaskResponse(AbstractModel):
    """CreateRecordTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，全局唯一标识录制任务。返回TaskId字段说明录制任务创建成功。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DayStreamPlayInfo(AbstractModel):
    """流播放信息

    """

    def __init__(self):
        """
        :param Time: 数据时间点，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Bandwidth: 带宽（单位Mbps）。
        :type Bandwidth: float
        :param Flux: 流量 （单位MB）。
        :type Flux: float
        :param Request: 请求数。
        :type Request: int
        :param Online: 在线人数。
        :type Online: int
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.Request = None
        self.Online = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Request = params.get("Request")
        self.Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DelayInfo(AbstractModel):
    """延播信息。

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的 
 AppName 保持一致，默认为 live。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param DelayInterval: 延播时间，单位：秒。
        :type DelayInterval: int
        :param CreateTime: 创建时间，UTC 时间。
注意：UTC时间和北京时间相差8小时。
例如：2019-06-18T12:00:00Z（为北京时间 2019 年 6 月 18 日 20 点 0 分 0 秒）。
        :type CreateTime: str
        :param ExpireTime: 过期时间，UTC 时间。
注意：UTC时间和北京时间相差8小时。
例如：2019-06-18T12:00:00Z（为北京时间 2019 年 6 月 18 日 20 点 0 分 0 秒）。
        :type ExpireTime: str
        :param Status: 当前状态:
-1：已过期。
1： 生效中。
        :type Status: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.DelayInterval = None
        self.CreateTime = None
        self.ExpireTime = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.DelayInterval = params.get("DelayInterval")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveCallbackRuleRequest(AbstractModel):
    """DeleteLiveCallbackRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        """
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveCallbackRuleResponse(AbstractModel):
    """DeleteLiveCallbackRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveCallbackTemplateRequest(AbstractModel):
    """DeleteLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
1. 在创建回调模板接口 [CreateLiveCallbackTemplate](/document/product/267/32637) 调用的返回值中获取模板 ID。
2. 可以从接口 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查询已经创建的过的模板列表。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveCallbackTemplateResponse(AbstractModel):
    """DeleteLiveCallbackTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveCertRequest(AbstractModel):
    """DeleteLiveCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: DescribeLiveCerts接口获取到的证书Id。
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveCertResponse(AbstractModel):
    """DeleteLiveCert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveDomainRequest(AbstractModel):
    """DeleteLiveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 要删除的域名
        :type DomainName: str
        :param DomainType: 类型。0-推流，1-播放
        :type DomainType: int
        """
        self.DomainName = None
        self.DomainType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveDomainResponse(AbstractModel):
    """DeleteLiveDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLivePullStreamTaskRequest(AbstractModel):
    """DeleteLivePullStreamTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 Id。
        :type TaskId: str
        :param Operator: 操作人姓名。
        :type Operator: str
        """
        self.TaskId = None
        self.Operator = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLivePullStreamTaskResponse(AbstractModel):
    """DeleteLivePullStreamTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TaskId: 任务ID，由CreateLiveRecord接口返回。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveRecordResponse(AbstractModel):
    """DeleteLiveRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveRecordRuleRequest(AbstractModel):
    """DeleteLiveRecordRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type AppName: str
        :param StreamName: 流名称。
域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，例如AppName为空也需要传空字符串进行强匹配。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveRecordRuleResponse(AbstractModel):
    """DeleteLiveRecordRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveRecordTemplateRequest(AbstractModel):
    """DeleteLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: DescribeRecordTemplates接口获取到的模板 ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveRecordTemplateResponse(AbstractModel):
    """DeleteLiveRecordTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveSnapshotRuleRequest(AbstractModel):
    """DeleteLiveSnapshotRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveSnapshotRuleResponse(AbstractModel):
    """DeleteLiveSnapshotRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveSnapshotTemplateRequest(AbstractModel):
    """DeleteLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
1. 在创建截图模板接口 [CreateLiveSnapshotTemplate](/document/product/267/32624) 调用的返回值中获取。
2. 可以从接口 [DescribeLiveSnapshotTemplates](/document/product/267/32619) 中查询已创建的截图模板列表。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveSnapshotTemplateResponse(AbstractModel):
    """DeleteLiveSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveTranscodeRuleRequest(AbstractModel):
    """DeleteLiveTranscodeRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param TemplateId: 模板ID。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveTranscodeRuleResponse(AbstractModel):
    """DeleteLiveTranscodeRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveTranscodeTemplateRequest(AbstractModel):
    """DeleteLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
1. 在创建转码模板接口 [CreateLiveTranscodeTemplate](/document/product/267/32646) 调用的返回值中获取模板 ID。
2. 可以从接口 [DescribeLiveTranscodeTemplates](/document/product/267/32641) 查询已经创建的过的模板列表。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveTranscodeTemplateResponse(AbstractModel):
    """DeleteLiveTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印 ID。
在添加水印接口 [AddLiveWatermark](/document/product/267/30154) 调用返回值中获取水印 ID。
或DescribeLiveWatermarks接口返回的水印ID。
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveWatermarkResponse(AbstractModel):
    """DeleteLiveWatermark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveWatermarkRuleRequest(AbstractModel):
    """DeleteLiveWatermarkRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。与推流和播放地址中的 AppName 保持一致，默认为live。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteLiveWatermarkRuleResponse(AbstractModel):
    """DeleteLiveWatermarkRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePullStreamConfigRequest(AbstractModel):
    """DeletePullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置 ID。
1. 在添加拉流配置接口 [CreatePullStreamConfig](/document/api/267/30159) 调用返回值中获取配置 ID。
2. 可以从接口 [DescribePullStreamConfigs](/document/api/267/30158) 中查询已创建过的拉流配置列表。
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePullStreamConfigResponse(AbstractModel):
    """DeletePullStreamConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRecordTaskRequest(AbstractModel):
    """DeleteRecordTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，CreateRecordTask返回。删除TaskId指定的录制任务。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteRecordTaskResponse(AbstractModel):
    """DeleteRecordTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAllStreamPlayInfoListRequest(AbstractModel):
    """DescribeAllStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param QueryTime: 查询时间点，精确到分钟粒度，支持最近1个月的数据查询，数据延迟为5分钟左右，如果要查询实时的数据，建议传递5分钟前的时间点，格式为yyyy-mm-dd HH:MM:00。（只精确至分钟，秒数填00）。
        :type QueryTime: str
        :param PlayDomains: 播放域名列表，若不填，表示总体数据。
        :type PlayDomains: list of str
        """
        self.QueryTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.QueryTime = params.get("QueryTime")
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAllStreamPlayInfoListResponse(AbstractModel):
    """DescribeAllStreamPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param QueryTime: 查询时间点，回传的输入参数中的查询时间。
        :type QueryTime: str
        :param DataInfoList: 数据信息列表。
        :type DataInfoList: list of MonitorStreamPlayInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QueryTime = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueryTime = params.get("QueryTime")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = MonitorStreamPlayInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAreaBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeAreaBillBandwidthAndFluxList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS，起始和结束时间跨度不支持超过1天。
        :type EndTime: str
        :param PlayDomains: 直播播放域名，若不填，表示总体数据。
        :type PlayDomains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAreaBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeAreaBillBandwidthAndFluxList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 明细数据信息。
        :type DataInfoList: list of BillAreaInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillAreaInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeBillBandwidthAndFluxList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS，起始和结束时间跨度不支持超过31天。支持最近3年的数据查询
        :type EndTime: str
        :param PlayDomains: 直播播放域名，若不填，表示总体数据。
        :type PlayDomains: list of str
        :param MainlandOrOversea: 可选值：
Mainland：查询国内数据，
Oversea：则查询国外数据，
默认：查询国内+国外的数据。
注：LEB（快直播）只支持国内+国外数据查询。
        :type MainlandOrOversea: str
        :param Granularity: 数据粒度，支持如下粒度：
5：5分钟粒度，（跨度不支持超过1天），
60：1小时粒度（跨度不支持超过一个月），
1440：天粒度（跨度不支持超过一个月）。
默认值：5。
        :type Granularity: int
        :param ServiceName: 服务名称，可选值包括LVB(标准直播)，LEB(快直播)，不填则查LVB+LEB总值。
        :type ServiceName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.MainlandOrOversea = None
        self.Granularity = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.Granularity = params.get("Granularity")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeBillBandwidthAndFluxList返回参数结构体

    """

    def __init__(self):
        """
        :param PeakBandwidthTime: 峰值带宽所在时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type PeakBandwidthTime: str
        :param PeakBandwidth: 峰值带宽，单位是Mbps。
        :type PeakBandwidth: float
        :param P95PeakBandwidthTime: 95峰值带宽所在时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type P95PeakBandwidthTime: str
        :param P95PeakBandwidth: 95峰值带宽，单位是Mbps。
        :type P95PeakBandwidth: float
        :param SumFlux: 总流量，单位是MB。
        :type SumFlux: float
        :param DataInfoList: 明细数据信息。
        :type DataInfoList: list of BillDataInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PeakBandwidthTime = None
        self.PeakBandwidth = None
        self.P95PeakBandwidthTime = None
        self.P95PeakBandwidth = None
        self.SumFlux = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PeakBandwidthTime = params.get("PeakBandwidthTime")
        self.PeakBandwidth = params.get("PeakBandwidth")
        self.P95PeakBandwidthTime = params.get("P95PeakBandwidthTime")
        self.P95PeakBandwidth = params.get("P95PeakBandwidth")
        self.SumFlux = params.get("SumFlux")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCallbackRecordsListRequest(AbstractModel):
    """DescribeCallbackRecordsList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS，起始和结束时间跨度不支持超过1天。
        :type EndTime: str
        :param StreamName: 流名称，精确匹配。
        :type StreamName: str
        :param PageNum: 页码
        :type PageNum: int
        :param PageSize: 每页条数
        :type PageSize: int
        :param EventType: 事件类型。
0: "断流",
1: "推流",
100: "录制"
        :type EventType: int
        :param ResultCode: 回调结果。0为成功，其他为失败
        :type ResultCode: int
        """
        self.StartTime = None
        self.EndTime = None
        self.StreamName = None
        self.PageNum = None
        self.PageSize = None
        self.EventType = None
        self.ResultCode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StreamName = params.get("StreamName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.EventType = params.get("EventType")
        self.ResultCode = params.get("ResultCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCallbackRecordsListResponse(AbstractModel):
    """DescribeCallbackRecordsList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 回调事件列表
        :type DataInfoList: list of CallbackEventInfo
        :param PageNum: 页码
        :type PageNum: int
        :param PageSize: 每页条数
        :type PageSize: int
        :param TotalNum: 总条数
        :type TotalNum: int
        :param TotalPage: 总页数
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = CallbackEventInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeConcurrentRecordStreamNumRequest(AbstractModel):
    """DescribeConcurrentRecordStreamNum请求参数结构体

    """

    def __init__(self):
        """
        :param LiveType: 直播类型，SlowLive：慢直播。
NormalLive：普通直播。
        :type LiveType: str
        :param StartTime: 起始时间，格式：yyyy-mm-dd HH:MM:SS。
可以查询最近180天的数据。
        :type StartTime: str
        :param EndTime: 结束时间，格式：yyyy-mm-dd HH:MM:SS。
时间跨度最大支持31天。
        :type EndTime: str
        :param MainlandOrOversea: 如果为空，查询所有地区数据；如果为“Mainland”，查询国内数据；如果为“Oversea”，则查询国外数据。
        :type MainlandOrOversea: str
        :param PushDomains: 推流域名列表，不填表示总体数据。
        :type PushDomains: list of str
        """
        self.LiveType = None
        self.StartTime = None
        self.EndTime = None
        self.MainlandOrOversea = None
        self.PushDomains = None


    def _deserialize(self, params):
        self.LiveType = params.get("LiveType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.PushDomains = params.get("PushDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeConcurrentRecordStreamNumResponse(AbstractModel):
    """DescribeConcurrentRecordStreamNum返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 统计信息列表。
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeliverBandwidthListRequest(AbstractModel):
    """DescribeDeliverBandwidthList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间，格式为%Y-%m-%d %H:%M:%S。
        :type StartTime: str
        :param EndTime: 结束时间，格式为%Y-%m-%d %H:%M:%S，支持最近三个月的数据查询，时间跨度最大是1个月。
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDeliverBandwidthListResponse(AbstractModel):
    """DescribeDeliverBandwidthList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 转推计费带宽数据
        :type DataInfoList: list of BandwidthInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BandwidthInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeGroupProIspPlayInfoListRequest(AbstractModel):
    """DescribeGroupProIspPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS
时间跨度在（0,3小时]，支持最近1个月数据查询。
        :type EndTime: str
        :param PlayDomains: 播放域名，默认为不填，表示求总体数据。
        :type PlayDomains: list of str
        :param ProvinceNames: 省份列表，默认不填，则返回各省份的数据。
        :type ProvinceNames: list of str
        :param IspNames: 运营商列表，默认不填，则返回整个运营商的数据。
        :type IspNames: list of str
        :param MainlandOrOversea: 国内还是国外，如果为空，查询所有地区数据；如果为“Mainland”，查询国内数据；如果为“Oversea”，则查询国外数据。
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeGroupProIspPlayInfoListResponse(AbstractModel):
    """DescribeGroupProIspPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 数据内容。
        :type DataInfoList: list of GroupProIspDataInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = GroupProIspDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeHttpStatusInfoListRequest(AbstractModel):
    """DescribeHttpStatusInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
注：最大时间跨度支持1天，支持最近3个月的数据查询。
        :type EndTime: str
        :param PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeHttpStatusInfoListResponse(AbstractModel):
    """DescribeHttpStatusInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 播放状态码列表。
        :type DataInfoList: list of HttpStatusData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = HttpStatusData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveCallbackRulesRequest(AbstractModel):
    """DescribeLiveCallbackRules请求参数结构体

    """


class DescribeLiveCallbackRulesResponse(AbstractModel):
    """DescribeLiveCallbackRules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 规则信息列表。
        :type Rules: list of CallBackRuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = CallBackRuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveCallbackTemplateRequest(AbstractModel):
    """DescribeLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
1. 在创建回调模板接口 [CreateLiveCallbackTemplate](/document/product/267/32637) 调用的返回值中获取模板 ID。
2. 可以从接口 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查询已经创建的过的模板列表。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveCallbackTemplateResponse(AbstractModel):
    """DescribeLiveCallbackTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Template: 回调模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.CallBackTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = CallBackTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveCallbackTemplatesRequest(AbstractModel):
    """DescribeLiveCallbackTemplates请求参数结构体

    """


class DescribeLiveCallbackTemplatesResponse(AbstractModel):
    """DescribeLiveCallbackTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param Templates: 模板信息列表。
        :type Templates: list of CallBackTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = CallBackTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveCertRequest(AbstractModel):
    """DescribeLiveCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: DescribeLiveCerts接口获取到的证书Id。
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveCertResponse(AbstractModel):
    """DescribeLiveCert返回参数结构体

    """

    def __init__(self):
        """
        :param CertInfo: 证书信息。
        :type CertInfo: :class:`tencentcloud.live.v20180801.models.CertInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfo") is not None:
            self.CertInfo = CertInfo()
            self.CertInfo._deserialize(params.get("CertInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveCertsRequest(AbstractModel):
    """DescribeLiveCerts请求参数结构体

    """


class DescribeLiveCertsResponse(AbstractModel):
    """DescribeLiveCerts返回参数结构体

    """

    def __init__(self):
        """
        :param CertInfoSet: 证书信息列表。
        :type CertInfoSet: list of CertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfoSet") is not None:
            self.CertInfoSet = []
            for item in params.get("CertInfoSet"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CertInfoSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDelayInfoListRequest(AbstractModel):
    """DescribeLiveDelayInfoList请求参数结构体

    """


class DescribeLiveDelayInfoListResponse(AbstractModel):
    """DescribeLiveDelayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DelayInfoList: 延播信息列表。
        :type DelayInfoList: list of DelayInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DelayInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DelayInfoList") is not None:
            self.DelayInfoList = []
            for item in params.get("DelayInfoList"):
                obj = DelayInfo()
                obj._deserialize(item)
                self.DelayInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainCertRequest(AbstractModel):
    """DescribeLiveDomainCert请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainCertResponse(AbstractModel):
    """DescribeLiveDomainCert返回参数结构体

    """

    def __init__(self):
        """
        :param DomainCertInfo: 证书信息。
        :type DomainCertInfo: :class:`tencentcloud.live.v20180801.models.DomainCertInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainCertInfo") is not None:
            self.DomainCertInfo = DomainCertInfo()
            self.DomainCertInfo._deserialize(params.get("DomainCertInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainPlayInfoListRequest(AbstractModel):
    """DescribeLiveDomainPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        """
        self.PlayDomains = None


    def _deserialize(self, params):
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainPlayInfoListResponse(AbstractModel):
    """DescribeLiveDomainPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param Time: 数据时间，格式为yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param TotalBandwidth: 实时总带宽。
        :type TotalBandwidth: float
        :param TotalFlux: 实时总流量。
        :type TotalFlux: float
        :param TotalRequest: 总请求数。
        :type TotalRequest: int
        :param TotalOnline: 实时总连接数。
        :type TotalOnline: int
        :param DomainInfoList: 分域名的数据情况。
        :type DomainInfoList: list of DomainInfoList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Time = None
        self.TotalBandwidth = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.TotalOnline = None
        self.DomainInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TotalBandwidth = params.get("TotalBandwidth")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.TotalOnline = params.get("TotalOnline")
        if params.get("DomainInfoList") is not None:
            self.DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = DomainInfoList()
                obj._deserialize(item)
                self.DomainInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainRefererRequest(AbstractModel):
    """DescribeLiveDomainReferer请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainRefererResponse(AbstractModel):
    """DescribeLiveDomainReferer返回参数结构体

    """

    def __init__(self):
        """
        :param RefererAuthConfig: 域名 Referer 黑白名单配置。
        :type RefererAuthConfig: :class:`tencentcloud.live.v20180801.models.RefererAuthConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RefererAuthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RefererAuthConfig") is not None:
            self.RefererAuthConfig = RefererAuthConfig()
            self.RefererAuthConfig._deserialize(params.get("RefererAuthConfig"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainRequest(AbstractModel):
    """DescribeLiveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainResponse(AbstractModel):
    """DescribeLiveDomain返回参数结构体

    """

    def __init__(self):
        """
        :param DomainInfo: 域名信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainInfo: :class:`tencentcloud.live.v20180801.models.DomainInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainsRequest(AbstractModel):
    """DescribeLiveDomains请求参数结构体

    """

    def __init__(self):
        """
        :param DomainStatus: 域名状态过滤。0-停用，1-启用。
        :type DomainStatus: int
        :param DomainType: 域名类型过滤。0-推流，1-播放。
        :type DomainType: int
        :param PageSize: 分页大小，范围：10~100。默认10。
        :type PageSize: int
        :param PageNum: 取第几页，范围：1~100000。默认1。
        :type PageNum: int
        :param IsDelayLive: 0 普通直播 1慢直播 默认0。
        :type IsDelayLive: int
        :param DomainPrefix: 域名前缀。
        :type DomainPrefix: str
        """
        self.DomainStatus = None
        self.DomainType = None
        self.PageSize = None
        self.PageNum = None
        self.IsDelayLive = None
        self.DomainPrefix = None


    def _deserialize(self, params):
        self.DomainStatus = params.get("DomainStatus")
        self.DomainType = params.get("DomainType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.IsDelayLive = params.get("IsDelayLive")
        self.DomainPrefix = params.get("DomainPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveDomainsResponse(AbstractModel):
    """DescribeLiveDomains返回参数结构体

    """

    def __init__(self):
        """
        :param AllCount: 总记录数。
        :type AllCount: int
        :param DomainList: 域名详细信息列表。
        :type DomainList: list of DomainInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllCount = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllCount = params.get("AllCount")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = DomainInfo()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveForbidStreamListRequest(AbstractModel):
    """DescribeLiveForbidStreamList请求参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 取得第几页，默认1。
        :type PageNum: int
        :param PageSize: 每页大小，最大100。 
取值：1~100之前的任意整数。
默认值：10。
        :type PageSize: int
        :param StreamName: 搜索的推流 id 名称。
        :type StreamName: str
        """
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveForbidStreamListResponse(AbstractModel):
    """DescribeLiveForbidStreamList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页显示的条数。
        :type PageSize: int
        :param ForbidStreamList: 禁推流列表。
        :type ForbidStreamList: list of ForbidStreamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.ForbidStreamList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("ForbidStreamList") is not None:
            self.ForbidStreamList = []
            for item in params.get("ForbidStreamList"):
                obj = ForbidStreamInfo()
                obj._deserialize(item)
                self.ForbidStreamList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePackageInfoRequest(AbstractModel):
    """DescribeLivePackageInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PackageType: 包类型，可选值：
0：流量包；
1：转码包。
2: 连麦包。
        :type PackageType: int
        :param OrderBy: 排序规则:
1. BuyTimeDesc： 最新购买的排在最前面
2. BuyTimeAsc： 最老购买的排在最前面
3. ExpireTimeDesc： 最后过期的排在最前面
4. ExpireTimeAsc：最先过期的排在最前面

注意：
1. PackageType 为 2（连麦包） 的时候，不支持 3、4 排序
        :type OrderBy: str
        :param PageNum: 取得第几页的数据，和 PageSize 同时传递才会生效。
        :type PageNum: int
        :param PageSize: 分页大小，和 PageNum 同时传递才会生效。
取值：10 ～ 100 之间的任意整数
        :type PageSize: int
        """
        self.PackageType = None
        self.OrderBy = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PackageType = params.get("PackageType")
        self.OrderBy = params.get("OrderBy")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePackageInfoResponse(AbstractModel):
    """DescribeLivePackageInfo返回参数结构体

    """

    def __init__(self):
        """
        :param LivePackageInfoList: 套餐包信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type LivePackageInfoList: list of LivePackageInfo
        :param PackageBillMode: 套餐包当前计费方式:
-1: 无计费方式或获取失败
0: 无计费方式
201: 月结带宽
202: 月结流量
203: 日结带宽
204: 日结流量
205: 日结时长
206: 月结时长
304: 日结流量
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageBillMode: int
        :param TotalPage: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPage: int
        :param TotalNum: 数据总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param PageNum: 当前页数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNum: int
        :param PageSize: 当前每页数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LivePackageInfoList = None
        self.PackageBillMode = None
        self.TotalPage = None
        self.TotalNum = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LivePackageInfoList") is not None:
            self.LivePackageInfoList = []
            for item in params.get("LivePackageInfoList"):
                obj = LivePackageInfo()
                obj._deserialize(item)
                self.LivePackageInfoList.append(obj)
        self.PackageBillMode = params.get("PackageBillMode")
        self.TotalPage = params.get("TotalPage")
        self.TotalNum = params.get("TotalNum")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePlayAuthKeyRequest(AbstractModel):
    """DescribeLivePlayAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePlayAuthKeyResponse(AbstractModel):
    """DescribeLivePlayAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param PlayAuthKeyInfo: 播放鉴权key信息。
        :type PlayAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PlayAuthKeyInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PlayAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayAuthKeyInfo") is not None:
            self.PlayAuthKeyInfo = PlayAuthKeyInfo()
            self.PlayAuthKeyInfo._deserialize(params.get("PlayAuthKeyInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePullStreamTasksRequest(AbstractModel):
    """DescribeLivePullStreamTasks请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。 
来源：调用 CreateLivePullStreamTask 接口时返回。
不填默认查询所有任务，按更新时间倒序排序。
        :type TaskId: str
        :param PageNum: 取得第几页，默认值：1。
        :type PageNum: int
        :param PageSize: 分页大小，默认值：10。
取值范围：1~20 之前的任意整数。
        :type PageSize: int
        """
        self.TaskId = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePullStreamTasksResponse(AbstractModel):
    """DescribeLivePullStreamTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskInfos: 直播拉流任务信息列表。
        :type TaskInfos: list of PullStreamTaskInfo
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页大小。
        :type PageSize: int
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param LimitTaskNum: 限制可创建的最大任务数。
        :type LimitTaskNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskInfos = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.LimitTaskNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = PullStreamTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.LimitTaskNum = params.get("LimitTaskNum")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePushAuthKeyRequest(AbstractModel):
    """DescribeLivePushAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLivePushAuthKeyResponse(AbstractModel):
    """DescribeLivePushAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param PushAuthKeyInfo: 推流鉴权key信息。
        :type PushAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PushAuthKeyInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PushAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushAuthKeyInfo") is not None:
            self.PushAuthKeyInfo = PushAuthKeyInfo()
            self.PushAuthKeyInfo._deserialize(params.get("PushAuthKeyInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveRecordRulesRequest(AbstractModel):
    """DescribeLiveRecordRules请求参数结构体

    """


class DescribeLiveRecordRulesResponse(AbstractModel):
    """DescribeLiveRecordRules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 规则列表。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveRecordTemplateRequest(AbstractModel):
    """DescribeLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: [DescribeLiveRecordTemplates](/document/product/267/32609)接口获取到的模板 ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveRecordTemplateResponse(AbstractModel):
    """DescribeLiveRecordTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Template: 录制模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.RecordTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = RecordTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveRecordTemplatesRequest(AbstractModel):
    """DescribeLiveRecordTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param IsDelayLive: 是否属于慢直播模板，默认：0。
0： 标准直播。
1：慢直播。
        :type IsDelayLive: int
        """
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.IsDelayLive = params.get("IsDelayLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveRecordTemplatesResponse(AbstractModel):
    """DescribeLiveRecordTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param Templates: 录制模板信息列表。
        :type Templates: list of RecordTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = RecordTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveSnapshotRulesRequest(AbstractModel):
    """DescribeLiveSnapshotRules请求参数结构体

    """


class DescribeLiveSnapshotRulesResponse(AbstractModel):
    """DescribeLiveSnapshotRules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 规则列表。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveSnapshotTemplateRequest(AbstractModel):
    """DescribeLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
调用 [CreateLiveSnapshotTemplate](/document/product/267/32624) 时返回的模板 ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveSnapshotTemplateResponse(AbstractModel):
    """DescribeLiveSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Template: 截图模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.SnapshotTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = SnapshotTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveSnapshotTemplatesRequest(AbstractModel):
    """DescribeLiveSnapshotTemplates请求参数结构体

    """


class DescribeLiveSnapshotTemplatesResponse(AbstractModel):
    """DescribeLiveSnapshotTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param Templates: 截图模板列表。
        :type Templates: list of SnapshotTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = SnapshotTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamEventListRequest(AbstractModel):
    """DescribeLiveStreamEventList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间。 
UTC 格式，例如：2018-12-29T19:00:00Z。
支持查询60天内的历史记录。
        :type StartTime: str
        :param EndTime: 结束时间。
UTC 格式，例如：2018-12-29T20:00:00Z。
不超过当前时间，且和起始时间相差不得超过30天。
        :type EndTime: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名称，不支持通配符（*）查询，默认模糊匹配。
可使用IsStrict字段改为精确查询。
        :type StreamName: str
        :param PageNum: 取得第几页。
默认值：1。
注： 目前只支持10000条内的查询。
        :type PageNum: int
        :param PageSize: 分页大小。
最大值：100。
取值范围：1~100 之间的任意整数。
默认值：10。
注： 目前只支持10000条内的查询。
        :type PageSize: int
        :param IsFilter: 是否过滤，默认不过滤。
0：不进行任何过滤。
1：过滤掉开播失败的，只返回开播成功的。
        :type IsFilter: int
        :param IsStrict: 是否精确查询，默认模糊匹配。
0：模糊匹配。
1：精确查询。
注：使用StreamName时该参数生效。
        :type IsStrict: int
        :param IsAsc: 是否按结束时间正序显示，默认逆序。
0：逆序。
1：正序。
        :type IsAsc: int
        """
        self.StartTime = None
        self.EndTime = None
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.PageNum = None
        self.PageSize = None
        self.IsFilter = None
        self.IsStrict = None
        self.IsAsc = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.IsFilter = params.get("IsFilter")
        self.IsStrict = params.get("IsStrict")
        self.IsAsc = params.get("IsAsc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamEventListResponse(AbstractModel):
    """DescribeLiveStreamEventList返回参数结构体

    """

    def __init__(self):
        """
        :param EventList: 推断流事件列表。
        :type EventList: list of StreamEventInfo
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页大小。
        :type PageSize: int
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = StreamEventInfo()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。多域名用户需要填写 DomainName。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。多路径用户需要填写 AppName。
        :type AppName: str
        :param PageNum: 取得第几页，默认1。
        :type PageNum: int
        :param PageSize: 每页大小，最大100。 
取值：10~100之间的任意整数。
默认值：10。
        :type PageSize: int
        :param StreamName: 流名称，用于精确查询。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamOnlineListResponse(AbstractModel):
    """DescribeLiveStreamOnlineList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页显示的条数。
        :type PageSize: int
        :param OnlineInfo: 正在推送流的信息列表。
        :type OnlineInfo: list of StreamOnlineInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.OnlineInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("OnlineInfo") is not None:
            self.OnlineInfo = []
            for item in params.get("OnlineInfo"):
                obj = StreamOnlineInfo()
                obj._deserialize(item)
                self.OnlineInfo.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamPublishedListRequest(AbstractModel):
    """DescribeLiveStreamPublishedList请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param EndTime: 结束时间。
UTC 格式，例如：2016-06-30T19:00:00Z。
不超过当前时间。
注意：EndTime和StartTime相差不可超过30天。
        :type EndTime: str
        :param StartTime: 起始时间。 
UTC 格式，例如：2016-06-29T19:00:00Z。
最长支持查询60天内数据。
        :type StartTime: str
        :param AppName: 推流路径，与推流和播放地址中的 AppName 保持一致，默认为 live。不支持模糊匹配。
        :type AppName: str
        :param PageNum: 取得第几页。
默认值：1。
        :type PageNum: int
        :param PageSize: 分页大小。
最大值：100。
取值范围：10~100 之前的任意整数。
默认值：10。
        :type PageSize: int
        :param StreamName: 流名称，支持模糊匹配。
        :type StreamName: str
        """
        self.DomainName = None
        self.EndTime = None
        self.StartTime = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamPublishedListResponse(AbstractModel):
    """DescribeLiveStreamPublishedList返回参数结构体

    """

    def __init__(self):
        """
        :param PublishInfo: 推流记录信息。
        :type PublishInfo: list of StreamName
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页大小
        :type PageSize: int
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PublishInfo = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PublishInfo") is not None:
            self.PublishInfo = []
            for item in params.get("PublishInfo"):
                obj = StreamName()
                obj._deserialize(item)
                self.PublishInfo.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamPushInfoListRequest(AbstractModel):
    """DescribeLiveStreamPushInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param PageNum: 页数，
范围[1,10000]，
默认值：1。
        :type PageNum: int
        :param PageSize: 每页个数，
范围：[1,1000]，
默认值： 200。
        :type PageSize: int
        """
        self.PushDomain = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamPushInfoListResponse(AbstractModel):
    """DescribeLiveStreamPushInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 直播流的统计信息列表。
        :type DataInfoList: list of PushDataInfo
        :param TotalNum: 所有在线流的总数量。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param PageNum: 当前数据所在页码。
        :type PageNum: int
        :param PageSize: 每页的在线流的个数。
        :type PageSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamStateRequest(AbstractModel):
    """DescribeLiveStreamState请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveStreamStateResponse(AbstractModel):
    """DescribeLiveStreamState返回参数结构体

    """

    def __init__(self):
        """
        :param StreamState: 流状态，
active：活跃，
inactive：非活跃，
forbid：禁播。
        :type StreamState: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StreamState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StreamState = params.get("StreamState")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveTranscodeDetailInfoRequest(AbstractModel):
    """DescribeLiveTranscodeDetailInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param DayTime: 查询时间，北京时间，
格式：yyyymmdd。
注意：支持查询近1个月内某天的详细数据。
        :type DayTime: str
        :param PageNum: 页数，默认1，
不超过100页。
        :type PageNum: int
        :param PageSize: 每页个数，默认20，
范围：[10,1000]。
        :type PageSize: int
        :param StartDayTime: 起始天时间，北京时间，
格式：yyyymmdd。
注意：支持查询近1个月内的详细数据。
        :type StartDayTime: str
        :param EndDayTime: 结束天时间，北京时间，
格式：yyyymmdd。
注意：支持查询近1个月内的详细数据，注意DayTime 与（StartDayTime，EndDayTime）必须要传一个，如果都传，会以DayTime为准 。
        :type EndDayTime: str
        """
        self.PushDomain = None
        self.StreamName = None
        self.DayTime = None
        self.PageNum = None
        self.PageSize = None
        self.StartDayTime = None
        self.EndDayTime = None


    def _deserialize(self, params):
        self.PushDomain = params.get("PushDomain")
        self.StreamName = params.get("StreamName")
        self.DayTime = params.get("DayTime")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StartDayTime = params.get("StartDayTime")
        self.EndDayTime = params.get("EndDayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveTranscodeDetailInfoResponse(AbstractModel):
    """DescribeLiveTranscodeDetailInfo返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 统计数据列表。
        :type DataInfoList: list of TranscodeDetailInfo
        :param PageNum: 页码。
        :type PageNum: int
        :param PageSize: 每页个数。
        :type PageSize: int
        :param TotalNum: 总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TranscodeDetailInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveTranscodeRulesRequest(AbstractModel):
    """DescribeLiveTranscodeRules请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateIds: 要筛选的模板ID数组。
        :type TemplateIds: list of int
        :param DomainNames: 要筛选的域名数组。
        :type DomainNames: list of str
        """
        self.TemplateIds = None
        self.DomainNames = None


    def _deserialize(self, params):
        self.TemplateIds = params.get("TemplateIds")
        self.DomainNames = params.get("DomainNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveTranscodeRulesResponse(AbstractModel):
    """DescribeLiveTranscodeRules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 转码规则列表。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveTranscodeTemplateRequest(AbstractModel):
    """DescribeLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
注意：在创建转码模板接口 [CreateLiveTranscodeTemplate](/document/product/267/32646) 调用的返回值中获取模板 ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveTranscodeTemplateResponse(AbstractModel):
    """DescribeLiveTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Template: 模板信息。
        :type Template: :class:`tencentcloud.live.v20180801.models.TemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveTranscodeTemplatesRequest(AbstractModel):
    """DescribeLiveTranscodeTemplates请求参数结构体

    """


class DescribeLiveTranscodeTemplatesResponse(AbstractModel):
    """DescribeLiveTranscodeTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param Templates: 转码模板列表。
        :type Templates: list of TemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveWatermarkRequest(AbstractModel):
    """DescribeLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: DescribeLiveWatermarks接口返回的水印 ID。
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveWatermarkResponse(AbstractModel):
    """DescribeLiveWatermark返回参数结构体

    """

    def __init__(self):
        """
        :param Watermark: 水印信息。
        :type Watermark: :class:`tencentcloud.live.v20180801.models.WatermarkInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Watermark = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Watermark") is not None:
            self.Watermark = WatermarkInfo()
            self.Watermark._deserialize(params.get("Watermark"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveWatermarkRulesRequest(AbstractModel):
    """DescribeLiveWatermarkRules请求参数结构体

    """


class DescribeLiveWatermarkRulesResponse(AbstractModel):
    """DescribeLiveWatermarkRules返回参数结构体

    """

    def __init__(self):
        """
        :param Rules: 水印规则列表。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLiveWatermarksRequest(AbstractModel):
    """DescribeLiveWatermarks请求参数结构体

    """


class DescribeLiveWatermarksResponse(AbstractModel):
    """DescribeLiveWatermarks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalNum: 水印总个数。
        :type TotalNum: int
        :param WatermarkList: 水印信息列表。
        :type WatermarkList: list of WatermarkInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.WatermarkList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("WatermarkList") is not None:
            self.WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = WatermarkInfo()
                obj._deserialize(item)
                self.WatermarkList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLogDownloadListRequest(AbstractModel):
    """DescribeLogDownloadList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
注意：结束时间 - 开始时间 <=7天。
        :type EndTime: str
        :param PlayDomains: 域名列表。
        :type PlayDomains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeLogDownloadListResponse(AbstractModel):
    """DescribeLogDownloadList返回参数结构体

    """

    def __init__(self):
        """
        :param LogInfoList: 日志信息列表。
        :type LogInfoList: list of LogInfo
        :param TotalNum: 总条数。
        :type TotalNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogInfoList = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogInfoList") is not None:
            self.LogInfoList = []
            for item in params.get("LogInfoList"):
                obj = LogInfo()
                obj._deserialize(item)
                self.LogInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePlayErrorCodeDetailInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param Granularity: 查询粒度：
1-1分钟粒度。
        :type Granularity: int
        :param StatType: 是，可选值包括”4xx”,”5xx”，支持”4xx,5xx”等这种混合模式。
        :type StatType: str
        :param PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        :param MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePlayErrorCodeDetailInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param HttpCodeList: 统计信息列表。
        :type HttpCodeList: list of HttpCodeInfo
        :param StatType: 统计类型。
        :type StatType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HttpCodeList = None
        self.StatType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HttpCodeList") is not None:
            self.HttpCodeList = []
            for item in params.get("HttpCodeList"):
                obj = HttpCodeInfo()
                obj._deserialize(item)
                self.HttpCodeList.append(obj)
        self.StatType = params.get("StatType")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePlayErrorCodeSumInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeSumInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，北京时间。
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param PlayDomains: 播放域名列表，不填表示总体数据。
        :type PlayDomains: list of str
        :param PageNum: 页数，范围[1,1000]，默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围：[1,1000]，默认值是20。
        :type PageSize: int
        :param MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param GroupType: 分组参数，可选值：CountryProIsp（默认值），Country（国家），默认是按照国家+省份+运营商来进行分组；目前国外的省份和运营商暂时无法识别。
        :type GroupType: str
        :param OutLanguage: 输出字段使用的语言，可选值：Chinese（默认值），English，目前国家，省份和运营商支持多语言。
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.GroupType = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.GroupType = params.get("GroupType")
        self.OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePlayErrorCodeSumInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeSumInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param ProIspInfoList: 分省份分运营商错误码为2或3或4或5开头的状态码数据信息。
        :type ProIspInfoList: list of ProIspPlayCodeDataInfo
        :param TotalCodeAll: 所有状态码的加和的次数。
        :type TotalCodeAll: int
        :param TotalCode4xx: 状态码为4开头的总次数。
        :type TotalCode4xx: int
        :param TotalCode5xx: 状态码为5开头的总次数。
        :type TotalCode5xx: int
        :param TotalCodeList: 各状态码的总次数。
        :type TotalCodeList: list of PlayCodeTotalInfo
        :param PageNum: 页号。
        :type PageNum: int
        :param PageSize: 每页大小。
        :type PageSize: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param TotalNum: 总记录数。
        :type TotalNum: int
        :param TotalCode2xx: 状态码为2开头的总次数。
        :type TotalCode2xx: int
        :param TotalCode3xx: 状态码为3开头的总次数。
        :type TotalCode3xx: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProIspInfoList = None
        self.TotalCodeAll = None
        self.TotalCode4xx = None
        self.TotalCode5xx = None
        self.TotalCodeList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalPage = None
        self.TotalNum = None
        self.TotalCode2xx = None
        self.TotalCode3xx = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProIspInfoList") is not None:
            self.ProIspInfoList = []
            for item in params.get("ProIspInfoList"):
                obj = ProIspPlayCodeDataInfo()
                obj._deserialize(item)
                self.ProIspInfoList.append(obj)
        self.TotalCodeAll = params.get("TotalCodeAll")
        self.TotalCode4xx = params.get("TotalCode4xx")
        self.TotalCode5xx = params.get("TotalCode5xx")
        if params.get("TotalCodeList") is not None:
            self.TotalCodeList = []
            for item in params.get("TotalCodeList"):
                obj = PlayCodeTotalInfo()
                obj._deserialize(item)
                self.TotalCodeList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalPage = params.get("TotalPage")
        self.TotalNum = params.get("TotalNum")
        self.TotalCode2xx = params.get("TotalCode2xx")
        self.TotalCode3xx = params.get("TotalCode3xx")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProIspPlaySumInfoListRequest(AbstractModel):
    """DescribeProIspPlaySumInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间，北京时间，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param StatType: 统计的类型，可选值：”Province”(省份)，”Isp”(运营商)，“CountryOrArea”(国家或地区)。
        :type StatType: str
        :param PlayDomains: 播放域名列表，不填则为全部。
        :type PlayDomains: list of str
        :param PageNum: 页号，范围是[1,1000]，默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围是[1,1000]，默认值是20。
        :type PageSize: int
        :param MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param OutLanguage: 输出字段使用的语言，可选值：Chinese（默认值），English；目前国家，省份和运营商支持多语言。
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.StatType = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProIspPlaySumInfoListResponse(AbstractModel):
    """DescribeProIspPlaySumInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalFlux: 总流量。
        :type TotalFlux: float
        :param TotalRequest: 总请求数。
        :type TotalRequest: int
        :param StatType: 统计的类型。
        :type StatType: str
        :param PageSize: 每页的记录数。
        :type PageSize: int
        :param PageNum: 页号。
        :type PageNum: int
        :param TotalNum: 总记录数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param DataInfoList: 省份，运营商，国家或地区汇总数据列表。
        :type DataInfoList: list of ProIspPlaySumInfo
        :param AvgFluxPerSecond: 下载速度，单位：MB/s，计算方式：总流量/总时长。
        :type AvgFluxPerSecond: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalFlux = None
        self.TotalRequest = None
        self.StatType = None
        self.PageSize = None
        self.PageNum = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.AvgFluxPerSecond = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.StatType = params.get("StatType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ProIspPlaySumInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProvinceIspPlayInfoListRequest(AbstractModel):
    """DescribeProvinceIspPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，当前使用北京时间，
例：2019-02-21 10:00:00。
        :type StartTime: str
        :param EndTime: 结束时间点，当前使用北京时间，
例：2019-02-21 12:00:00。
注：EndTime 和 StartTime 只支持最近1天的数据查询。
        :type EndTime: str
        :param Granularity: 支持如下粒度：
1：1分钟粒度（跨度不支持超过1天）
        :type Granularity: int
        :param StatType: 统计指标类型：
“Bandwidth”：带宽
“FluxPerSecond”：平均流量
“Flux”：流量
“Request”：请求数
“Online”：并发连接数
        :type StatType: str
        :param PlayDomains: 播放域名列表。
        :type PlayDomains: list of str
        :param ProvinceNames: 要查询的省份（地区）英文名称列表，如 Beijing。
        :type ProvinceNames: list of str
        :param IspNames: 要查询的运营商英文名称列表，如 China Mobile ，如果为空，查询所有运营商的数据。
        :type IspNames: list of str
        :param MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param IpType: ip类型：
“Ipv6”：Ipv6数据
如果为空，查询总的数据；
        :type IpType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None
        self.MainlandOrOversea = None
        self.IpType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.IpType = params.get("IpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeProvinceIspPlayInfoListResponse(AbstractModel):
    """DescribeProvinceIspPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 播放信息列表。
        :type DataInfoList: list of PlayStatInfo
        :param StatType: 统计的类型，和输入参数保持一致。
        :type StatType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.StatType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayStatInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.StatType = params.get("StatType")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePullStreamConfigsRequest(AbstractModel):
    """DescribePullStreamConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置 ID。
获取途径：从 CreatePullStreamConfig 接口返回值获取。
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePullStreamConfigsResponse(AbstractModel):
    """DescribePullStreamConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param PullStreamConfigs: 拉流配置。
        :type PullStreamConfigs: list of PullStreamConfig
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PullStreamConfigs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullStreamConfigs") is not None:
            self.PullStreamConfigs = []
            for item in params.get("PullStreamConfigs"):
                obj = PullStreamConfig()
                obj._deserialize(item)
                self.PullStreamConfigs.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRecordTaskRequest(AbstractModel):
    """DescribeRecordTask请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询任务开始时间，Unix 时间戳。设置时间不早于当前时间之前90天的时间，且查询时间跨度不超过一周。
        :type StartTime: int
        :param EndTime: 查询任务结束时间，Unix 时间戳。EndTime 必须大于 StartTime，设置时间不早于当前时间之前90天的时间，且查询时间跨度不超过一周。（注意：任务开始结束时间必须在查询时间范围内）。
        :type EndTime: int
        :param StreamName: 流名称。
        :type StreamName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param ScrollToken: 翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。
        :type ScrollToken: str
        """
        self.StartTime = None
        self.EndTime = None
        self.StreamName = None
        self.DomainName = None
        self.AppName = None
        self.ScrollToken = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.ScrollToken = params.get("ScrollToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRecordTaskResponse(AbstractModel):
    """DescribeRecordTask返回参数结构体

    """

    def __init__(self):
        """
        :param ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 Token。当该字段为空，说明已无更多数据。
        :type ScrollToken: str
        :param TaskList: 录制任务列表。当该字段为空，说明已返回所有数据。
        :type TaskList: list of RecordTask
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScrollToken = None
        self.TaskList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScrollToken = params.get("ScrollToken")
        if params.get("TaskList") is not None:
            self.TaskList = []
            for item in params.get("TaskList"):
                obj = RecordTask()
                obj._deserialize(item)
                self.TaskList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeScreenShotSheetNumListRequest(AbstractModel):
    """DescribeScreenShotSheetNumList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: utc起始时间，格式为yyyy-mm-ddTHH:MM:SSZ
        :type StartTime: str
        :param EndTime: utc结束时间，格式为yyyy-mm-ddTHH:MM:SSZ，支持查询最近1年数据。
        :type EndTime: str
        :param Zone: 地域信息，可选值包括Mainland，Oversea，前者是查询中国大陆范围内的数据，后者是除中国大陆范围之外的数据，若不传该参数，则查询所有地区的数据。
        :type Zone: str
        :param PushDomains: 推流域名（支持查询2019年11 月1日之后的域名维度数据）。
        :type PushDomains: list of str
        :param Granularity: 数据维度，数据延迟1个半小时，可选值包括：1、Minute（5分钟粒度，最大支持查询时间范围是31天），2、Day（天粒度，默认值，最大支持查询时间范围是186天当天）。
        :type Granularity: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Zone = None
        self.PushDomains = None
        self.Granularity = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Zone = params.get("Zone")
        self.PushDomains = params.get("PushDomains")
        self.Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeScreenShotSheetNumListResponse(AbstractModel):
    """DescribeScreenShotSheetNumList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 数据信息列表。
        :type DataInfoList: list of TimeValue
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TimeValue()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamDayPlayInfoListRequest(AbstractModel):
    """DescribeStreamDayPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param DayTime: 日期，格式：YYYY-mm-dd。
第二天凌晨3点出昨天的数据，建议在这个时间点之后查询最新数据。支持最近3个月的数据查询。
        :type DayTime: str
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param PageNum: 页号，范围[1,1000]，默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围[100,1000]，默认值是1000。
        :type PageSize: int
        :param MainlandOrOversea: 可选值：
Mainland：查询国内数据，
Oversea：则查询国外数据，
默认：查询国内+国外的数据。
        :type MainlandOrOversea: str
        :param ServiceName: 服务名称，可选值包括LVB(标准直播)，LEB(快直播)，不填则查LVB+LEB总值。
        :type ServiceName: str
        """
        self.DayTime = None
        self.PlayDomain = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.DayTime = params.get("DayTime")
        self.PlayDomain = params.get("PlayDomain")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamDayPlayInfoListResponse(AbstractModel):
    """DescribeStreamDayPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 播放数据信息列表。
        :type DataInfoList: list of PlayDataInfoByStream
        :param TotalNum: 总数量。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param PageNum: 当前数据所处页码。
        :type PageNum: int
        :param PageSize: 每页个数。
        :type PageSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayDataInfoByStream()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间，北京时间，格式为yyyy-mm-dd HH:MM:SS
        :type StartTime: str
        :param EndTime: 结束时间，北京时间，格式为yyyy-mm-dd HH:MM:SS，
结束时间 和 开始时间跨度不支持超过24小时，支持距当前时间30天内的数据查询。
        :type EndTime: str
        :param PlayDomain: 播放域名，
若不填，则为查询所有播放域名的在线流数据。
        :type PlayDomain: str
        :param StreamName: 流名称，精确匹配。
若不填，则为查询总体播放数据。
        :type StreamName: str
        :param AppName: 推流路径，与播放地址中的AppName保持一致，会精确匹配，在同时传递了StreamName时生效。
若不填，则为查询总体播放数据。
注意：按AppName查询请先联系工单申请，开通后配置生效预计需要5个工作日左右，具体时间以最终回复为准。
        :type AppName: str
        :param ServiceName: 服务名称，可选值包括LVB(标准直播)，LEB(快直播)，不填则查LVB+LEB总值。
        :type ServiceName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomain = None
        self.StreamName = None
        self.AppName = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomain = params.get("PlayDomain")
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamPlayInfoListResponse(AbstractModel):
    """DescribeStreamPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 统计信息列表，时间粒度是1分钟。
        :type DataInfoList: list of DayStreamPlayInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = DayStreamPlayInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamPushInfoListRequest(AbstractModel):
    """DescribeStreamPushInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS，最大时间跨度支持6小时，支持最近6天数据查询。
        :type EndTime: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.PushDomain = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeStreamPushInfoListResponse(AbstractModel):
    """DescribeStreamPushInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 返回的数据列表。
        :type DataInfoList: list of PushQualityData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushQualityData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTopClientIpSumInfoListRequest(AbstractModel):
    """DescribeTopClientIpSumInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS
时间跨度在[0,4小时]，支持最近1天数据查询。
        :type EndTime: str
        :param PlayDomains: 播放域名，默认为不填，表示求总体数据。
        :type PlayDomains: list of str
        :param PageNum: 页号，范围是[1,1000]，默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围是[1,1000]，默认值是20。
        :type PageSize: int
        :param OrderParam: 排序指标，可选值包括TotalRequest（默认值），FailedRequest,TotalFlux。
        :type OrderParam: str
        :param MainlandOrOversea: 地域，可选值：Mainland，Oversea，China，Foreign，Global（默认值）；如果为空，查询总的数据；如果为“Mainland”，查询中国大陆的数据；如果为“Oversea”，则查询中国大陆以外的数据；如果为China，查询中国的数据（包括港澳台）；如果为Foreign，查询国外的数据（不包括港澳台）。
        :type MainlandOrOversea: str
        :param OutLanguage: 输出字段使用的语言，可选值：Chinese（默认值），English；目前国家，省份和运营商支持多语言。
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None
        self.MainlandOrOversea = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTopClientIpSumInfoListResponse(AbstractModel):
    """DescribeTopClientIpSumInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 页号，范围是[1,1000]，默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围是[1,1000]，默认值是20。
        :type PageSize: int
        :param OrderParam: 排序指标，可选值包括”TotalRequest”，”FailedRequest”,“TotalFlux”。
        :type OrderParam: str
        :param TotalNum: 记录总数。
        :type TotalNum: int
        :param TotalPage: 记录总页数。
        :type TotalPage: int
        :param DataInfoList: 数据内容。
        :type DataInfoList: list of ClientIpPlaySumInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ClientIpPlaySumInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUploadStreamNumsRequest(AbstractModel):
    """DescribeUploadStreamNums请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS，起始和结束时间跨度不支持超过31天。支持最近31天的数据查询
        :type EndTime: str
        :param Domains: 直播域名，若不填，表示总体数据。
        :type Domains: list of str
        :param Granularity: 数据粒度，支持如下粒度：
5：5分钟粒度，（跨度不支持超过1天），
1440：天粒度（跨度不支持超过一个月）。
默认值：5。
        :type Granularity: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Domains = None
        self.Granularity = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Domains = params.get("Domains")
        self.Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUploadStreamNumsResponse(AbstractModel):
    """DescribeUploadStreamNums返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 明细数据信息
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeVisitTopSumInfoListRequest(AbstractModel):
    """DescribeVisitTopSumInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 起始时间点，格式为yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 结束时间点，格式为yyyy-mm-dd HH:MM:SS
时间跨度在(0,4小时]，支持最近1天数据查询。
        :type EndTime: str
        :param TopIndex: 峰值指标，可选值包括”Domain”，”StreamId”。
        :type TopIndex: str
        :param PlayDomains: 播放域名，默认为不填，表示求总体数据。
        :type PlayDomains: list of str
        :param PageNum: 页号，
范围是[1,1000]，
默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围是[1,1000]，
默认值是20。
        :type PageSize: int
        :param OrderParam: 排序指标，可选值包括” AvgFluxPerSecond”，”TotalRequest”（默认）,“TotalFlux”。
        :type OrderParam: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TopIndex = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TopIndex = params.get("TopIndex")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeVisitTopSumInfoListResponse(AbstractModel):
    """DescribeVisitTopSumInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 页号，
范围是[1,1000]，
默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围是[1,1000]，
默认值是20。
        :type PageSize: int
        :param TopIndex: 峰值指标，可选值包括”Domain”，”StreamId”。
        :type TopIndex: str
        :param OrderParam: 排序指标，可选值包括” AvgFluxPerSecond”(按每秒平均流量排序)，”TotalRequest”（默认，按总请求数排序）,“TotalFlux”（按总流量排序）。
        :type OrderParam: str
        :param TotalNum: 记录总数。
        :type TotalNum: int
        :param TotalPage: 记录总页数。
        :type TotalPage: int
        :param DataInfoList: 数据内容。
        :type DataInfoList: list of PlaySumStatInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.TopIndex = None
        self.OrderParam = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TopIndex = params.get("TopIndex")
        self.OrderParam = params.get("OrderParam")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlaySumStatInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainCertInfo(AbstractModel):
    """域名证书信息

    """

    def __init__(self):
        """
        :param CertId: 证书Id。
        :type CertId: int
        :param CertName: 证书名称。
        :type CertName: str
        :param Description: 描述信息。
        :type Description: str
        :param CreateTime: 创建时间，UTC格式。
        :type CreateTime: str
        :param HttpsCrt: 证书内容。
        :type HttpsCrt: str
        :param CertType: 证书类型。
0：用户添加证书，
1：腾讯云托管证书。
        :type CertType: int
        :param CertExpireTime: 证书过期时间，UTC格式。
        :type CertExpireTime: str
        :param DomainName: 使用此证书的域名名称。
        :type DomainName: str
        :param Status: 证书状态。
        :type Status: int
        :param CertDomains: 证书本身标识的域名列表。
比如: ["*.x.com"]
注意：此字段可能返回 null，表示取不到有效值。
        :type CertDomains: list of str
        :param CloudCertId: 腾讯云ssl的证书Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudCertId: str
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainName = None
        self.Status = None
        self.CertDomains = None
        self.CloudCertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        self.CertDomains = params.get("CertDomains")
        self.CloudCertId = params.get("CloudCertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainDetailInfo(AbstractModel):
    """每个域名的统计信息。

    """

    def __init__(self):
        """
        :param MainlandOrOversea: 国内还是国外:
Mainland: 表示国内数据。
Oversea: 表示国外数据。
        :type MainlandOrOversea: str
        :param Bandwidth: 带宽，单位: Mbps。
        :type Bandwidth: float
        :param Flux: 流量，单位: MB。
        :type Flux: float
        :param Online: 人数。
        :type Online: int
        :param Request: 请求数。
        :type Request: int
        """
        self.MainlandOrOversea = None
        self.Bandwidth = None
        self.Flux = None
        self.Online = None
        self.Request = None


    def _deserialize(self, params):
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Online = params.get("Online")
        self.Request = params.get("Request")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainInfo(AbstractModel):
    """直播域名信息

    """

    def __init__(self):
        """
        :param Name: 直播域名。
        :type Name: str
        :param Type: 域名类型:
0: 推流。
1: 播放。
        :type Type: int
        :param Status: 域名状态:
0: 停用。
1: 启用。
        :type Status: int
        :param CreateTime: 添加时间。
        :type CreateTime: str
        :param BCName: 是否有 CName 到固定规则域名:
0: 否。
1: 是。
        :type BCName: int
        :param TargetDomain: cname 对应的域名。
        :type TargetDomain: str
        :param PlayType: 播放区域，只在 Type=1 时该参数有意义。
1: 国内。
2: 全球。
3: 海外。
        :type PlayType: int
        :param IsDelayLive: 是否慢直播:
0: 普通直播。
1: 慢直播。
        :type IsDelayLive: int
        :param CurrentCName: 当前客户使用的 cname 信息。
        :type CurrentCName: str
        :param RentTag: 失效参数，可忽略。
        :type RentTag: int
        :param RentExpireTime: 失效参数，可忽略。
        :type RentExpireTime: str
        :param IsMiniProgramLive: 0: 标准直播。
1: 小程序直播。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMiniProgramLive: int
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.BCName = None
        self.TargetDomain = None
        self.PlayType = None
        self.IsDelayLive = None
        self.CurrentCName = None
        self.RentTag = None
        self.RentExpireTime = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BCName = params.get("BCName")
        self.TargetDomain = params.get("TargetDomain")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.CurrentCName = params.get("CurrentCName")
        self.RentTag = params.get("RentTag")
        self.RentExpireTime = params.get("RentExpireTime")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainInfoList(AbstractModel):
    """多个域名信息列表

    """

    def __init__(self):
        """
        :param Domain: 域名。
        :type Domain: str
        :param DetailInfoList: 明细信息。
        :type DetailInfoList: list of DomainDetailInfo
        """
        self.Domain = None
        self.DetailInfoList = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("DetailInfoList") is not None:
            self.DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.DetailInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DropLiveStreamRequest(AbstractModel):
    """DropLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DropLiveStreamResponse(AbstractModel):
    """DropLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableLiveDomainRequest(AbstractModel):
    """EnableLiveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 待启用的直播域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableLiveDomainResponse(AbstractModel):
    """EnableLiveDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForbidLiveDomainRequest(AbstractModel):
    """ForbidLiveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 待停用的直播域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForbidLiveDomainResponse(AbstractModel):
    """ForbidLiveDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param ResumeTime: 恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：
1. 默认禁播7天，且最长支持禁播90天。
2. 北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ResumeTime: str
        :param Reason: 禁推原因。
注明：请务必填写禁推原因，防止误操作。
长度限制：2048字节。
        :type Reason: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None
        self.Reason = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForbidLiveStreamResponse(AbstractModel):
    """ForbidLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForbidStreamInfo(AbstractModel):
    """禁推流列表

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param ExpireTime: 禁推过期时间。
        :type ExpireTime: str
        """
        self.StreamName = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GroupProIspDataInfo(AbstractModel):
    """某省份某运营商在某段时间内的带宽，流量，请求数和并发数

    """

    def __init__(self):
        """
        :param ProvinceName: 省份。
        :type ProvinceName: str
        :param IspName: 运营商。
        :type IspName: str
        :param DetailInfoList: 分钟维度的明细数据。
        :type DetailInfoList: list of CdnPlayStatData
        """
        self.ProvinceName = None
        self.IspName = None
        self.DetailInfoList = None


    def _deserialize(self, params):
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        if params.get("DetailInfoList") is not None:
            self.DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = CdnPlayStatData()
                obj._deserialize(item)
                self.DetailInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HlsSpecialParam(AbstractModel):
    """HLS专属录制参数

    """

    def __init__(self):
        """
        :param FlowContinueDuration: HLS续流超时时间。
取值范围[0，1800]。
        :type FlowContinueDuration: int
        """
        self.FlowContinueDuration = None


    def _deserialize(self, params):
        self.FlowContinueDuration = params.get("FlowContinueDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HttpCodeInfo(AbstractModel):
    """HTTP返回码和统计数据

    """

    def __init__(self):
        """
        :param HttpCode: HTTP协议返回码。
例："2xx", "3xx", "4xx", "5xx"。
        :type HttpCode: str
        :param ValueList: 统计信息，对于无数据的时间点，会补0。
        :type ValueList: list of HttpCodeValue
        """
        self.HttpCode = None
        self.ValueList = None


    def _deserialize(self, params):
        self.HttpCode = params.get("HttpCode")
        if params.get("ValueList") is not None:
            self.ValueList = []
            for item in params.get("ValueList"):
                obj = HttpCodeValue()
                obj._deserialize(item)
                self.ValueList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HttpCodeValue(AbstractModel):
    """HTTP返回码数据信息

    """

    def __init__(self):
        """
        :param Time: 时间，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Numbers: 次数。
        :type Numbers: int
        :param Percentage: 占比。
        :type Percentage: float
        """
        self.Time = None
        self.Numbers = None
        self.Percentage = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Numbers = params.get("Numbers")
        self.Percentage = params.get("Percentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HttpStatusData(AbstractModel):
    """播放错误码信息

    """

    def __init__(self):
        """
        :param Time: 数据时间点，
格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param HttpStatusInfoList: 播放状态码详细信息。
        :type HttpStatusInfoList: list of HttpStatusInfo
        """
        self.Time = None
        self.HttpStatusInfoList = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        if params.get("HttpStatusInfoList") is not None:
            self.HttpStatusInfoList = []
            for item in params.get("HttpStatusInfoList"):
                obj = HttpStatusInfo()
                obj._deserialize(item)
                self.HttpStatusInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HttpStatusInfo(AbstractModel):
    """播放错误码信息

    """

    def __init__(self):
        """
        :param HttpStatus: 播放HTTP状态码。
        :type HttpStatus: str
        :param Num: 个数。
        :type Num: int
        """
        self.HttpStatus = None
        self.Num = None


    def _deserialize(self, params):
        self.HttpStatus = params.get("HttpStatus")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LivePackageInfo(AbstractModel):
    """直播包信息。

    """

    def __init__(self):
        """
        :param Id: 包 ID。
        :type Id: str
        :param Total: 总量。
注意：当为流量包时单位为字节。
当为转码包时单位为分钟。
        :type Total: int
        :param Used: 使用量。
注意：当为流量包时单位为字节。
当为转码包时单位为分钟。
当为连麦包时单位为小时。
        :type Used: int
        :param Left: 剩余量。
注意：当为流量包时单位为字节。
当为转码包时单位为分钟。
当为连麦包时单位为小时。
        :type Left: int
        :param BuyTime: 购买时间。
        :type BuyTime: str
        :param ExpireTime: 过期时间。
        :type ExpireTime: str
        :param Type: 包类型，可选值:
0: 流量包。
1: 普通转码包。
2: 极速高清包。
3: 连麦包。
        :type Type: int
        :param Status: 包状态，可选值:
0: 未使用。
1: 使用中。
2: 已过期。
3: 已冻结。
4: 已耗尽。
5: 已退款
        :type Status: int
        """
        self.Id = None
        self.Total = None
        self.Used = None
        self.Left = None
        self.BuyTime = None
        self.ExpireTime = None
        self.Type = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.Left = params.get("Left")
        self.BuyTime = params.get("BuyTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LogInfo(AbstractModel):
    """日志url信息。

    """

    def __init__(self):
        """
        :param LogName: 日志名称。
        :type LogName: str
        :param LogUrl: 日志 URL。
        :type LogUrl: str
        :param LogTime: 日志生成时间。
        :type LogTime: str
        :param FileSize: 文件大小。
        :type FileSize: int
        """
        self.LogName = None
        self.LogUrl = None
        self.LogTime = None
        self.FileSize = None


    def _deserialize(self, params):
        self.LogName = params.get("LogName")
        self.LogUrl = params.get("LogUrl")
        self.LogTime = params.get("LogTime")
        self.FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveCallbackTemplateRequest(AbstractModel):
    """ModifyLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: DescribeLiveCallbackTemplates接口返回的模板 ID。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param StreamBeginNotifyUrl: 开播回调 URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 断流回调 URL。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 录制回调 URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截图回调 URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鉴黄回调 URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回调 Key，回调 URL 公用，回调签名详见事件消息通知文档。
[事件消息通知](/document/product/267/32744)。
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveCallbackTemplateResponse(AbstractModel):
    """ModifyLiveCallbackTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveCertRequest(AbstractModel):
    """ModifyLiveCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书Id。
        :type CertId: str
        :param CertType: 证书类型。0-用户添加证书；1-腾讯云托管证书。
        :type CertType: int
        :param CertName: 证书名称。
        :type CertName: str
        :param HttpsCrt: 证书内容，即公钥。
        :type HttpsCrt: str
        :param HttpsKey: 私钥。
        :type HttpsKey: str
        :param Description: 描述信息。
        :type Description: str
        """
        self.CertId = None
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveCertResponse(AbstractModel):
    """ModifyLiveCert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveDomainCertRequest(AbstractModel):
    """ModifyLiveDomainCert请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param CertId: 证书Id。
        :type CertId: int
        :param Status: 状态，0：关闭  1：打开。
        :type Status: int
        """
        self.DomainName = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveDomainCertResponse(AbstractModel):
    """ModifyLiveDomainCert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveDomainRefererRequest(AbstractModel):
    """ModifyLiveDomainReferer请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param Enable: 是否开启当前域名的 Referer 黑白名单鉴权。
        :type Enable: int
        :param Type: 名单类型，0：黑名单，1：白名单。
        :type Type: int
        :param AllowEmpty: 是否允许空 Referer，0：不允许，1：允许。
        :type AllowEmpty: int
        :param Rules: Referer 名单列表，以;分隔。
        :type Rules: str
        """
        self.DomainName = None
        self.Enable = None
        self.Type = None
        self.AllowEmpty = None
        self.Rules = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.Type = params.get("Type")
        self.AllowEmpty = params.get("AllowEmpty")
        self.Rules = params.get("Rules")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveDomainRefererResponse(AbstractModel):
    """ModifyLiveDomainReferer返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
不传表示不修改当前值。
        :type Enable: int
        :param AuthKey: 鉴权key。
不传表示不修改当前值。
        :type AuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
不传表示不修改当前值。
        :type AuthDelta: int
        :param AuthBackKey: 鉴权备用key。
不传表示不修改当前值。
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePlayAuthKeyResponse(AbstractModel):
    """ModifyLivePlayAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePlayDomainRequest(AbstractModel):
    """ModifyLivePlayDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param PlayType: 拉流域名类型。1-国内；2-全球；3-境外
        :type PlayType: int
        """
        self.DomainName = None
        self.PlayType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.PlayType = params.get("PlayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePlayDomainResponse(AbstractModel):
    """ModifyLivePlayDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePullStreamTaskRequest(AbstractModel):
    """ModifyLivePullStreamTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务Id。
        :type TaskId: str
        :param Operator: 操作人姓名。
        :type Operator: str
        :param SourceUrls: 拉流源url列表。
SourceType为直播（PullLivePushLive）只可以填1个，
SourceType为点播（PullVodPushLive）可以填多个，上限30个。
        :type SourceUrls: list of str
        :param StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param VodLoopTimes: 点播拉流转推循环次数。
-1：无限循环，直到任务结束。
0：不循环。
>0：具体循环次数。次数和时间以先结束的为准。
注意：拉流源为点播，该配置生效。
        :type VodLoopTimes: int
        :param VodRefreshType: 点播更新SourceUrls后的播放方式：
ImmediateNewSource：立即从更新的拉流源开始播放；
ContinueBreakPoint：从上次断流url源的断点处继续，结束后再使用新的拉流源。
注意：拉流源为点播，该配置生效。
        :type VodRefreshType: str
        :param Status: 任务状态：
enable - 启用，
pause - 暂停。
        :type Status: str
        :param CallbackEvents: 选择需要回调的事件（不填则回调全部）：
TaskStart：任务启动回调，
TaskExit：任务停止回调，
VodSourceFileStart：从点播源文件开始拉流回调，
VodSourceFileFinish：从点播源文件拉流结束回调，
ResetTaskConfig：任务更新回调。
        :type CallbackEvents: list of str
        :param CallbackUrl: 自定义回调地址。
相关事件会回调到该地址。
        :type CallbackUrl: str
        :param FileIndex: 指定播放文件索引。
注意：
1. 从1开始，不大于SourceUrls中文件个数。
2. 只有VodRefreshType为ContinueBeginPoint时指定才有效。
3. 只有当前任务处于暂停时，指定后启动任务才会生效。
        :type FileIndex: int
        :param OffsetTime: 指定播放文件偏移。
注意：
1. 单位：秒，配合FileIndex使用。
2. 只有VodRefreshType为ContinueBeginPoint时指定才有效。
3. 只有当前任务处于暂停时，指定后启动任务才会生效。
        :type OffsetTime: int
        :param Comment: 任务备注。
        :type Comment: str
        """
        self.TaskId = None
        self.Operator = None
        self.SourceUrls = None
        self.StartTime = None
        self.EndTime = None
        self.VodLoopTimes = None
        self.VodRefreshType = None
        self.Status = None
        self.CallbackEvents = None
        self.CallbackUrl = None
        self.FileIndex = None
        self.OffsetTime = None
        self.Comment = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Operator = params.get("Operator")
        self.SourceUrls = params.get("SourceUrls")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.VodLoopTimes = params.get("VodLoopTimes")
        self.VodRefreshType = params.get("VodRefreshType")
        self.Status = params.get("Status")
        self.CallbackEvents = params.get("CallbackEvents")
        self.CallbackUrl = params.get("CallbackUrl")
        self.FileIndex = params.get("FileIndex")
        self.OffsetTime = params.get("OffsetTime")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePullStreamTaskResponse(AbstractModel):
    """ModifyLivePullStreamTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
不传表示不修改当前值。
        :type Enable: int
        :param MasterAuthKey: 主鉴权key。
不传表示不修改当前值。
        :type MasterAuthKey: str
        :param BackupAuthKey: 备鉴权key。
不传表示不修改当前值。
        :type BackupAuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLivePushAuthKeyResponse(AbstractModel):
    """ModifyLivePushAuthKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveRecordTemplateRequest(AbstractModel):
    """ModifyLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: DescribeRecordTemplates接口获取到的模板 ID。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param FlvParam: FLV 录制参数，开启 FLV 录制时设置。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS 录制参数，开启 HLS 录制时设置。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 录制参数，开启 MP4 录制时设置。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC 录制参数，开启 AAC 录制时设置。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsSpecialParam: HLS 录制定制参数。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 录制参数，开启 MP3 录制时设置。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveRecordTemplateResponse(AbstractModel):
    """ModifyLiveRecordTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveSnapshotTemplateRequest(AbstractModel):
    """ModifyLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param TemplateName: 模板名称。
长度上限：255字节。
        :type TemplateName: str
        :param Description: 描述信息。
长度上限：1024字节。
        :type Description: str
        :param SnapshotInterval: 截图间隔，单位s，默认10s。
范围： 5s ~ 300s。
        :type SnapshotInterval: int
        :param Width: 截图宽度。默认：0（原始宽）。
        :type Width: int
        :param Height: 截图高度。默认：0（原始高）。
        :type Height: int
        :param PornFlag: 是否开启鉴黄，默认 0 。
0：不开启。
1：开启。
        :type PornFlag: int
        :param CosAppId: Cos 应用 ID。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名称。
注：CosBucket参数值不能包含-[appid] 部分。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
        :param CosPrefix: Cos Bucket文件夹前缀。
        :type CosPrefix: str
        :param CosFileName: Cos 文件名称。
        :type CosFileName: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveSnapshotTemplateResponse(AbstractModel):
    """ModifyLiveSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveTranscodeTemplateRequest(AbstractModel):
    """ModifyLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 Id。
        :type TemplateId: int
        :param Vcodec: 视频编码：h264/h265/origin，默认origin。

origin: 保持原始编码格式
        :type Vcodec: str
        :param Acodec: 音频编码：aac，默认aac。
注意：当前该参数未生效，待后续支持！
        :type Acodec: str
        :param AudioBitrate: 音频码率，默认0。
范围：0-500。
        :type AudioBitrate: int
        :param Description: 模板描述。
        :type Description: str
        :param VideoBitrate: 视频码率。范围：0kbps - 8000kbps。
0为保持原始码率。
注: 转码模板有码率唯一要求，最终保存的码率可能与输入码率有所差别。
        :type VideoBitrate: int
        :param Width: 宽。0-3000。
数值必须是2的倍数，0是原始宽度
        :type Width: int
        :param NeedVideo: 是否保留视频，0：否，1：是。默认1。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音频，0：否，1：是。默认1。
        :type NeedAudio: int
        :param Height: 高。0-3000。
数值必须是2的倍数，0是原始宽度
        :type Height: int
        :param Fps: 帧率，默认0。
范围0-60
        :type Fps: int
        :param Gop: 关键帧间隔，单位：秒。
范围2-6
        :type Gop: int
        :param Rotate: 旋转角度，默认0。
可取值：0，90，180，270
        :type Rotate: int
        :param Profile: 编码质量：
baseline/main/high。
        :type Profile: str
        :param BitrateToOrig: 当设置的码率>原始码率时，是否以原始码率为准。
0：否， 1：是
默认 0。
        :type BitrateToOrig: int
        :param HeightToOrig: 当设置的高度>原始高度时，是否以原始高度为准。
0：否， 1：是
默认 0。
        :type HeightToOrig: int
        :param FpsToOrig: 当设置的帧率>原始帧率时，是否以原始帧率为准。
0：否， 1：是
默认 0。
        :type FpsToOrig: int
        :param AdaptBitratePercent: 极速高清视频码率压缩比。
极速高清目标码率=VideoBitrate * (1-AdaptBitratePercent)

取值范围：0.0到0.5
        :type AdaptBitratePercent: float
        :param ShortEdgeAsHeight: 是否以短边作为高度，0：否，1：是。默认0。
        :type ShortEdgeAsHeight: int
        """
        self.TemplateId = None
        self.Vcodec = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Description = None
        self.VideoBitrate = None
        self.Width = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.AdaptBitratePercent = None
        self.ShortEdgeAsHeight = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Vcodec = params.get("Vcodec")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Description = params.get("Description")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Width = params.get("Width")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")
        self.ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyLiveTranscodeTemplateResponse(AbstractModel):
    """ModifyLiveTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPullStreamConfigRequest(AbstractModel):
    """ModifyPullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置 ID。
获取来源：
1. 创建拉流配置接口CreatePullStreamConfig返回的配置 ID。
2. 通过查询接口DescribePullStreamConfigs获取配置 ID。
        :type ConfigId: str
        :param FromUrl: 源 URL，用于拉流的地址。目前可支持直播流及点播文件。
注意：
1. 多个点播 URL 之间使用空格拼接。
2. 目前上限支持10个 URL。
3. 支持拉流文件格式：FLV，RTMP，HLS，MP4。
4. 使用标准三层样式，如：http://test.com/live/stream.flv。
        :type FromUrl: str
        :param ToUrl: 目的 URL，用于推流的地址，目前限制该目标地址为腾讯域名。
1. 仅支持 RTMP 协议。
2. 使用标准三层样式，如：http://test.com/live/stream.flv。
        :type ToUrl: str
        :param AreaId: 区域 ID：
1-深圳。
2-上海。
3-天津。
4-中国香港。
如有改动，需同时传入IspId。
        :type AreaId: int
        :param IspId: 运营商 ID，
1：电信。
2：移动。
3：联通。
4：其他。
AreaId为4的时候，IspId只能为其他。如有改动，需同时传入AreaId。
        :type IspId: int
        :param StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。

使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        """
        self.ConfigId = None
        self.FromUrl = None
        self.ToUrl = None
        self.AreaId = None
        self.IspId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaId = params.get("AreaId")
        self.IspId = params.get("IspId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPullStreamConfigResponse(AbstractModel):
    """ModifyPullStreamConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPullStreamStatusRequest(AbstractModel):
    """ModifyPullStreamStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigIds: 配置 ID 列表。
        :type ConfigIds: list of str
        :param Status: 目标状态。0无效，2正在运行，4暂停。
        :type Status: str
        """
        self.ConfigIds = None
        self.Status = None


    def _deserialize(self, params):
        self.ConfigIds = params.get("ConfigIds")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPullStreamStatusResponse(AbstractModel):
    """ModifyPullStreamStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MonitorStreamPlayInfo(AbstractModel):
    """监控播放数据

    """

    def __init__(self):
        """
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param StreamName: 流id。
        :type StreamName: str
        :param Rate: 播放码率，0表示原始码率。
        :type Rate: int
        :param Protocol: 播放协议，可选值包括 Unknown，Flv，Hls，Rtmp，Huyap2p。
        :type Protocol: str
        :param Bandwidth: 带宽，单位是Mbps。
        :type Bandwidth: float
        :param Online: 在线人数，1分钟采样一个点，统计采样点的tcp链接数目。
        :type Online: int
        :param Request: 请求数。
        :type Request: int
        """
        self.PlayDomain = None
        self.StreamName = None
        self.Rate = None
        self.Protocol = None
        self.Bandwidth = None
        self.Online = None
        self.Request = None


    def _deserialize(self, params):
        self.PlayDomain = params.get("PlayDomain")
        self.StreamName = params.get("StreamName")
        self.Rate = params.get("Rate")
        self.Protocol = params.get("Protocol")
        self.Bandwidth = params.get("Bandwidth")
        self.Online = params.get("Online")
        self.Request = params.get("Request")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PlayAuthKeyInfo(AbstractModel):
    """播放鉴权key信息。

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用:
0: 关闭。
1: 启用。
        :type Enable: int
        :param AuthKey: 鉴权 Key。
        :type AuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        :param AuthBackKey: 鉴权 BackKey。
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PlayCodeTotalInfo(AbstractModel):
    """各状态码的总次数，支持大多数的 HTTP 协议返回码。

    """

    def __init__(self):
        """
        :param Code: HTTP code，可选值包括:
400，403，404，500，502，503，504。
        :type Code: str
        :param Num: 总次数。
        :type Num: int
        """
        self.Code = None
        self.Num = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PlayDataInfoByStream(AbstractModel):
    """流维度的播放信息。

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TotalFlux: 总流量，单位: MB。
        :type TotalFlux: float
        """
        self.StreamName = None
        self.TotalFlux = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TotalFlux = params.get("TotalFlux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PlayStatInfo(AbstractModel):
    """按省份运营商查询的播放信息。

    """

    def __init__(self):
        """
        :param Time: 数据时间点。
        :type Time: str
        :param Value: 带宽/流量/请求数/并发连接数/下载速度的值，若没数据返回时该值为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PlaySumStatInfo(AbstractModel):
    """播放汇总统计信息。

    """

    def __init__(self):
        """
        :param Name: 域名或流 ID。
        :type Name: str
        :param AvgFluxPerSecond: 平均下载速度，
单位: MB/s。
计算公式: 每分钟的下载速度求平均值。
        :type AvgFluxPerSecond: float
        :param TotalFlux: 总流量，单位: MB。
        :type TotalFlux: float
        :param TotalRequest: 总请求数。
        :type TotalRequest: int
        """
        self.Name = None
        self.AvgFluxPerSecond = None
        self.TotalFlux = None
        self.TotalRequest = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ProIspPlayCodeDataInfo(AbstractModel):
    """播放错误码信息

    """

    def __init__(self):
        """
        :param CountryAreaName: 国家或地区。
        :type CountryAreaName: str
        :param ProvinceName: 省份。
        :type ProvinceName: str
        :param IspName: 运营商。
        :type IspName: str
        :param Code2xx: 错误码为2开头的次数。
        :type Code2xx: int
        :param Code3xx: 错误码为3开头的次数。
        :type Code3xx: int
        :param Code4xx: 错误码为4开头的次数。
        :type Code4xx: int
        :param Code5xx: 错误码为5开头的次数。
        :type Code5xx: int
        """
        self.CountryAreaName = None
        self.ProvinceName = None
        self.IspName = None
        self.Code2xx = None
        self.Code3xx = None
        self.Code4xx = None
        self.Code5xx = None


    def _deserialize(self, params):
        self.CountryAreaName = params.get("CountryAreaName")
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        self.Code2xx = params.get("Code2xx")
        self.Code3xx = params.get("Code3xx")
        self.Code4xx = params.get("Code4xx")
        self.Code5xx = params.get("Code5xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ProIspPlaySumInfo(AbstractModel):
    """获取省份/运营商的播放信息。

    """

    def __init__(self):
        """
        :param Name: 省份/运营商/国家或地区。
        :type Name: str
        :param TotalFlux: 总流量，单位: MB。
        :type TotalFlux: float
        :param TotalRequest: 总请求数。
        :type TotalRequest: int
        :param AvgFluxPerSecond: 平均下载流量，单位: MB/s。
        :type AvgFluxPerSecond: float
        """
        self.Name = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.AvgFluxPerSecond = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PublishTime(AbstractModel):
    """推流时间。

    """

    def __init__(self):
        """
        :param PublishTime: 推流时间。
UTC 格式，例如：2018-06-29T19:00:00Z。
        :type PublishTime: str
        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PullStreamConfig(AbstractModel):
    """拉流配置。

    """

    def __init__(self):
        """
        :param ConfigId: 拉流配置 ID。
        :type ConfigId: str
        :param FromUrl: 源 URL。
        :type FromUrl: str
        :param ToUrl: 目的 URL。
        :type ToUrl: str
        :param AreaName: 区域名。
        :type AreaName: str
        :param IspName: 运营商名。
        :type IspName: str
        :param StartTime: 开始时间。
UTC格式时间，例如: 2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束时间。

UTC格式时间，例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param Status: 状态:
0: 无效。
1: 初始状态。
2: 正在运行。
3: 拉起失败。
4: 暂停。
        :type Status: str
        """
        self.ConfigId = None
        self.FromUrl = None
        self.ToUrl = None
        self.AreaName = None
        self.IspName = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaName = params.get("AreaName")
        self.IspName = params.get("IspName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PullStreamTaskInfo(AbstractModel):
    """直播拉流任务信息。

    """

    def __init__(self):
        """
        :param TaskId: 拉流任务Id。
        :type TaskId: str
        :param SourceType: 拉流源的类型：
PullLivePushLive -直播，
PullVodPushLive -点播。
        :type SourceType: str
        :param SourceUrls: 拉流源url列表。
SourceType为直播（PullLiveToLive）只可以填1个，
SourceType为点播（PullVodToLive）可以填多个，上限10个。
        :type SourceUrls: list of str
        :param DomainName: 推流域名。
将拉到的源推到该域名。
        :type DomainName: str
        :param AppName: 推流路径。
将拉到的源推到该路径。
        :type AppName: str
        :param StreamName: 流名称。
将拉到的源推到该流名称。
        :type StreamName: str
        :param PushArgs: 推流参数。
推流携带的自定义参数。
        :type PushArgs: str
        :param StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param Region: 拉流源所在地域（请就近选取）：
ap-beijing - 华北地区(北京)，
ap-shanghai -华东地区(上海)，
ap-guangzhou -华南地区(广州)，
ap-mumbai - 印度。
        :type Region: str
        :param VodLoopTimes: 点播拉流转推循环次数。
-1：无限循环，直到任务结束。
0：不循环。
>0：具体循环次数。次数和时间以先结束的为准。
注意：拉流源为点播，该配置生效。
        :type VodLoopTimes: int
        :param VodRefreshType: 点播更新SourceUrls后的播放方式：
ImmediateNewSource：立即从更新的拉流源开始播放；
ContinueBreakPoint：从上次断流url源的断点处继续，结束后再使用新的拉流源。

注意：拉流源为点播，该配置生效。
        :type VodRefreshType: str
        :param CreateTime: 任务创建时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type CreateTime: str
        :param UpdateTime: 任务更新时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
注意：北京时间值为 UTC 时间值 + 8 小时，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type UpdateTime: str
        :param CreateBy: 创建任务的操作者。
        :type CreateBy: str
        :param UpdateBy: 最后更新任务的操作者。
        :type UpdateBy: str
        :param CallbackUrl: 回调地址。
        :type CallbackUrl: str
        :param CallbackEvents: 选择需要回调的事件：
TaskStart：任务启动回调，
TaskExit：任务停止回调，
VodSourceFileStart：从点播源文件开始拉流回调，
VodSourceFileFinish：从点播源文件拉流结束回调，
ResetTaskConfig：任务更新回调。
        :type CallbackEvents: list of str
        :param CallbackInfo: 注意：该信息暂不返回。
最后一次回调信息。
        :type CallbackInfo: str
        :param ErrorInfo: 注意：该信息暂不返回。
错误信息。
        :type ErrorInfo: str
        :param Status: 状态。
enable：生效中。
pause：暂停中。
        :type Status: str
        :param RecentPullInfo: 注意：该信息仅在查询单个任务时返回。
任务最新拉流信息。
包含：源 url，偏移时间，上报时间。
        :type RecentPullInfo: :class:`tencentcloud.live.v20180801.models.RecentPullInfo`
        :param Comment: 任务备注信息。
        :type Comment: str
        """
        self.TaskId = None
        self.SourceType = None
        self.SourceUrls = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.PushArgs = None
        self.StartTime = None
        self.EndTime = None
        self.Region = None
        self.VodLoopTimes = None
        self.VodRefreshType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CreateBy = None
        self.UpdateBy = None
        self.CallbackUrl = None
        self.CallbackEvents = None
        self.CallbackInfo = None
        self.ErrorInfo = None
        self.Status = None
        self.RecentPullInfo = None
        self.Comment = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SourceType = params.get("SourceType")
        self.SourceUrls = params.get("SourceUrls")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.PushArgs = params.get("PushArgs")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Region = params.get("Region")
        self.VodLoopTimes = params.get("VodLoopTimes")
        self.VodRefreshType = params.get("VodRefreshType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateBy = params.get("CreateBy")
        self.UpdateBy = params.get("UpdateBy")
        self.CallbackUrl = params.get("CallbackUrl")
        self.CallbackEvents = params.get("CallbackEvents")
        self.CallbackInfo = params.get("CallbackInfo")
        self.ErrorInfo = params.get("ErrorInfo")
        self.Status = params.get("Status")
        if params.get("RecentPullInfo") is not None:
            self.RecentPullInfo = RecentPullInfo()
            self.RecentPullInfo._deserialize(params.get("RecentPullInfo"))
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushAuthKeyInfo(AbstractModel):
    """推流鉴权key信息。

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param MasterAuthKey: 主鉴权 Key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 备鉴权 Key。
        :type BackupAuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushDataInfo(AbstractModel):
    """推流数据信息

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param ClientIp: 推流客户端 IP。
        :type ClientIp: str
        :param ServerIp: 接流服务器 IP。
        :type ServerIp: str
        :param VideoFps: 推流视频帧率，单位: Hz。
        :type VideoFps: int
        :param VideoSpeed: 推流视频码率，单位: bps。
        :type VideoSpeed: int
        :param AudioFps: 推流音频帧率，单位: Hz。
        :type AudioFps: int
        :param AudioSpeed: 推流音频码率，单位: bps。
        :type AudioSpeed: int
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param BeginPushTime: 推流开始时间。
        :type BeginPushTime: str
        :param Acodec: 音频编码格式，
例："AAC"。
        :type Acodec: str
        :param Vcodec: 视频编码格式，
例："H264"。
        :type Vcodec: str
        :param Resolution: 分辨率。
        :type Resolution: str
        :param AsampleRate: 采样率。
        :type AsampleRate: int
        :param MetaAudioSpeed: metadata 中的音频码率，单位: Kbps。
        :type MetaAudioSpeed: int
        :param MetaVideoSpeed: metadata 中的视频码率，单位: Kbps。
        :type MetaVideoSpeed: int
        :param MetaFps: metadata 中的帧率。
        :type MetaFps: int
        """
        self.StreamName = None
        self.AppName = None
        self.ClientIp = None
        self.ServerIp = None
        self.VideoFps = None
        self.VideoSpeed = None
        self.AudioFps = None
        self.AudioSpeed = None
        self.PushDomain = None
        self.BeginPushTime = None
        self.Acodec = None
        self.Vcodec = None
        self.Resolution = None
        self.AsampleRate = None
        self.MetaAudioSpeed = None
        self.MetaVideoSpeed = None
        self.MetaFps = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.ClientIp = params.get("ClientIp")
        self.ServerIp = params.get("ServerIp")
        self.VideoFps = params.get("VideoFps")
        self.VideoSpeed = params.get("VideoSpeed")
        self.AudioFps = params.get("AudioFps")
        self.AudioSpeed = params.get("AudioSpeed")
        self.PushDomain = params.get("PushDomain")
        self.BeginPushTime = params.get("BeginPushTime")
        self.Acodec = params.get("Acodec")
        self.Vcodec = params.get("Vcodec")
        self.Resolution = params.get("Resolution")
        self.AsampleRate = params.get("AsampleRate")
        self.MetaAudioSpeed = params.get("MetaAudioSpeed")
        self.MetaVideoSpeed = params.get("MetaVideoSpeed")
        self.MetaFps = params.get("MetaFps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushQualityData(AbstractModel):
    """某条流的推流质量详情数据。

    """

    def __init__(self):
        """
        :param Time: 数据时间，格式: %Y-%m-%d %H:%M:%S.%ms，精确到毫秒级。
        :type Time: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param AppName: 推流路径。
        :type AppName: str
        :param ClientIp: 推流客户端 IP。
        :type ClientIp: str
        :param BeginPushTime: 开始推流时间，格式: %Y-%m-%d %H:%M:%S.%ms，精确到毫秒级。
        :type BeginPushTime: str
        :param Resolution: 分辨率信息。
        :type Resolution: str
        :param VCodec: 视频编码格式。
        :type VCodec: str
        :param ACodec: 音频编码格式。
        :type ACodec: str
        :param Sequence: 推流序列号，用来唯一的标志一次推流。
        :type Sequence: str
        :param VideoFps: 视频帧率。
        :type VideoFps: int
        :param VideoRate: 视频码率，单位: bps。
        :type VideoRate: int
        :param AudioFps: 音频帧率。
        :type AudioFps: int
        :param AudioRate: 音频码率，单位: bps。
        :type AudioRate: int
        :param LocalTs: 本地流逝时间，单位: ms，音视频流逝时间与本地流逝时间的差距越大表示推流质量越差，上行卡顿越严重。
        :type LocalTs: int
        :param VideoTs: 视频流逝时间，单位: ms。
        :type VideoTs: int
        :param AudioTs: 音频流逝时间，单位: ms。
        :type AudioTs: int
        :param MetaVideoRate: metadata 中的视频码率，单位: kbps。
        :type MetaVideoRate: int
        :param MetaAudioRate: metadata 中的音频码率，单位: kbps。
        :type MetaAudioRate: int
        :param MateFps: metadata 中的帧率。
        :type MateFps: int
        :param StreamParam: 推流参数
        :type StreamParam: str
        """
        self.Time = None
        self.PushDomain = None
        self.AppName = None
        self.ClientIp = None
        self.BeginPushTime = None
        self.Resolution = None
        self.VCodec = None
        self.ACodec = None
        self.Sequence = None
        self.VideoFps = None
        self.VideoRate = None
        self.AudioFps = None
        self.AudioRate = None
        self.LocalTs = None
        self.VideoTs = None
        self.AudioTs = None
        self.MetaVideoRate = None
        self.MetaAudioRate = None
        self.MateFps = None
        self.StreamParam = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        self.ClientIp = params.get("ClientIp")
        self.BeginPushTime = params.get("BeginPushTime")
        self.Resolution = params.get("Resolution")
        self.VCodec = params.get("VCodec")
        self.ACodec = params.get("ACodec")
        self.Sequence = params.get("Sequence")
        self.VideoFps = params.get("VideoFps")
        self.VideoRate = params.get("VideoRate")
        self.AudioFps = params.get("AudioFps")
        self.AudioRate = params.get("AudioRate")
        self.LocalTs = params.get("LocalTs")
        self.VideoTs = params.get("VideoTs")
        self.AudioTs = params.get("AudioTs")
        self.MetaVideoRate = params.get("MetaVideoRate")
        self.MetaAudioRate = params.get("MetaAudioRate")
        self.MateFps = params.get("MateFps")
        self.StreamParam = params.get("StreamParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RecentPullInfo(AbstractModel):
    """直播拉流当前正在拉的文件信息。

    """

    def __init__(self):
        """
        :param FileUrl: 当前正在拉的文件地址。
        :type FileUrl: str
        :param OffsetTime: 当前正在拉的文件偏移，单位：秒。
        :type OffsetTime: int
        :param ReportTime: 最新上报偏移信息时间。UTC格式。
如：2020-07-23T03:20:39Z。
注意：与北京时间相差八小时。
        :type ReportTime: str
        :param LoopedTimes: 已经轮播的次数。
        :type LoopedTimes: int
        """
        self.FileUrl = None
        self.OffsetTime = None
        self.ReportTime = None
        self.LoopedTimes = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.OffsetTime = params.get("OffsetTime")
        self.ReportTime = params.get("ReportTime")
        self.LoopedTimes = params.get("LoopedTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RecordParam(AbstractModel):
    """录制模板参数。

    """

    def __init__(self):
        """
        :param RecordInterval: 录制间隔。
单位秒，默认：1800。
取值范围：300-7200。
此参数对 HLS 无效，当录制 HLS 时从推流到断流生成一个文件。
        :type RecordInterval: int
        :param StorageTime: 录制存储时长。
单位秒，取值范围： 0 - 93312000。
0：表示永久存储。
        :type StorageTime: int
        :param Enable: 是否开启当前格式录制，默认值为0，0：否， 1：是。
        :type Enable: int
        :param VodSubAppId: 点播子应用 ID。
        :type VodSubAppId: int
        :param VodFileName: 录制文件名。
支持的特殊占位符有：
{StreamID}: 流ID
{StartYear}: 开始时间-年
{StartMonth}: 开始时间-月
{StartDay}: 开始时间-日
{StartHour}: 开始时间-小时
{StartMinute}: 开始时间-分钟
{StartSecond}: 开始时间-秒
{StartMillisecond}: 开始时间-毫秒
{EndYear}: 结束时间-年
{EndMonth}: 结束时间-月
{EndDay}: 结束时间-日
{EndHour}: 结束时间-小时
{EndMinute}: 结束时间-分钟
{EndSecond}: 结束时间-秒
{EndMillisecond}: 结束时间-毫秒

若未设置默认录制文件名为{StreamID}_{StartYear}-{StartMonth}-{StartDay}-{StartHour}-{StartMinute}-{StartSecond}_{EndYear}-{EndMonth}-{EndDay}-{EndHour}-{EndMinute}-{EndSecond}
        :type VodFileName: str
        """
        self.RecordInterval = None
        self.StorageTime = None
        self.Enable = None
        self.VodSubAppId = None
        self.VodFileName = None


    def _deserialize(self, params):
        self.RecordInterval = params.get("RecordInterval")
        self.StorageTime = params.get("StorageTime")
        self.Enable = params.get("Enable")
        self.VodSubAppId = params.get("VodSubAppId")
        self.VodFileName = params.get("VodFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RecordTask(AbstractModel):
    """录制任务

    """

    def __init__(self):
        """
        :param TaskId: 录制任务ID。
        :type TaskId: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param StartTime: 任务开始时间，Unix时间戳。
        :type StartTime: int
        :param EndTime: 任务结束时间，Unix时间戳。
        :type EndTime: int
        :param TemplateId: 录制模板ID。
        :type TemplateId: int
        :param Stopped: 调用 StopRecordTask 停止任务时间，Unix时间戳。值为0表示未曾调用接口停止任务。
        :type Stopped: int
        """
        self.TaskId = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.TemplateId = None
        self.Stopped = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TemplateId = params.get("TemplateId")
        self.Stopped = params.get("Stopped")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RecordTemplateInfo(AbstractModel):
    """录制模板信息

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param FlvParam: FLV 录制参数。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS 录制参数。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 录制参数。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC 录制参数。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS 录制定制参数
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 录制参数。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RefererAuthConfig(AbstractModel):
    """直播域名Referer黑白名单配置

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param Type: 名单类型，0：黑名单，1：白名单。
        :type Type: int
        :param AllowEmpty: 是否允许空Referer，0：不允许，1：允许。
        :type AllowEmpty: int
        :param Rules: 名单列表，以分号(;)分隔。
        :type Rules: str
        """
        self.DomainName = None
        self.Enable = None
        self.Type = None
        self.AllowEmpty = None
        self.Rules = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.Type = params.get("Type")
        self.AllowEmpty = params.get("AllowEmpty")
        self.Rules = params.get("Rules")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResumeDelayLiveStreamRequest(AbstractModel):
    """ResumeDelayLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为live。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResumeDelayLiveStreamResponse(AbstractModel):
    """ResumeDelayLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 推流路径，与推流和播放地址中的AppName保持一致，默认为 live。
        :type AppName: str
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResumeLiveStreamResponse(AbstractModel):
    """ResumeLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleInfo(AbstractModel):
    """规则信息。

    """

    def __init__(self):
        """
        :param CreateTime: 规则创建时间。
        :type CreateTime: str
        :param UpdateTime: 规则更新时间。
        :type UpdateTime: str
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SnapshotTemplateInfo(AbstractModel):
    """截图模板信息。

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param SnapshotInterval: 截图时间间隔，5-300秒。
        :type SnapshotInterval: int
        :param Width: 截图宽度，范围：0-3000。 
0：原始宽度并适配原始比例。
        :type Width: int
        :param Height: 截图高度，范围：0-2000。
0：原始高度并适配原始比例。
        :type Height: int
        :param PornFlag: 是否开启鉴黄，0：不开启，1：开启。
        :type PornFlag: int
        :param CosAppId: Cos 应用 ID。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名称。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
        :param Description: 模板描述。
        :type Description: str
        :param CosPrefix: Cos Bucket文件夹前缀。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPrefix: str
        :param CosFileName: Cos 文件名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosFileName: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TaskId: 任务ID，由CreateLiveRecord接口返回。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopLiveRecordResponse(AbstractModel):
    """StopLiveRecord返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopRecordTaskRequest(AbstractModel):
    """StopRecordTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 录制任务ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopRecordTaskResponse(AbstractModel):
    """StopRecordTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamEventInfo(AbstractModel):
    """推断流事件信息。

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param StreamStartTime: 推流开始时间。
UTC 格式时间，例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param StreamEndTime: 推流结束时间。
UTC 格式时间，例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param StopReason: 停止原因。
        :type StopReason: str
        :param Duration: 推流持续时长，单位：秒。
        :type Duration: int
        :param ClientIp: 主播 IP。
        :type ClientIp: str
        :param Resolution: 分辨率。
        :type Resolution: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamName(AbstractModel):
    """流名称列表。

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamStartTime: 推流开始时间。
UTC格式时间，例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param StreamEndTime: 推流结束时间。
UTC格式时间，例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param StopReason: 停止原因。
        :type StopReason: str
        :param Duration: 推流持续时长，单位：秒。
        :type Duration: int
        :param ClientIp: 主播 IP。
        :type ClientIp: str
        :param Resolution: 分辨率。
        :type Resolution: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamOnlineInfo(AbstractModel):
    """查询当前正在推流的信息

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param PublishTimeList: 推流时间列表
        :type PublishTimeList: list of PublishTime
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        """
        self.StreamName = None
        self.PublishTimeList = None
        self.AppName = None
        self.DomainName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        if params.get("PublishTimeList") is not None:
            self.PublishTimeList = []
            for item in params.get("PublishTimeList"):
                obj = PublishTime()
                obj._deserialize(item)
                self.PublishTimeList.append(obj)
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TemplateInfo(AbstractModel):
    """转码模板信息。

    """

    def __init__(self):
        """
        :param Vcodec: 视频编码：h264/h265/origin，默认h264。

origin: 保持原始编码格式
        :type Vcodec: str
        :param VideoBitrate: 视频码率。范围：0kbps - 8000kbps。
0为保持原始码率。
注: 转码模板有码率唯一要求，最终保存的码率可能与输入码率有所差别。
        :type VideoBitrate: int
        :param Acodec: 音频编码：aac，默认aac。
注意：当前该参数未生效，待后续支持！
        :type Acodec: str
        :param AudioBitrate: 音频码率。取值范围：0kbps - 500kbps。
默认0。
        :type AudioBitrate: int
        :param Width: 宽，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始宽度
        :type Width: int
        :param Height: 高，默认0。
范围[0-3000]
数值必须是2的倍数，0是原始宽度
        :type Height: int
        :param Fps: 帧率，默认0。
范围0-60fps
        :type Fps: int
        :param Gop: 关键帧间隔，单位：秒。
默认原始的间隔
范围2-6
        :type Gop: int
        :param Rotate: 旋转角度，默认0。
可取值：0，90，180，270
        :type Rotate: int
        :param Profile: 编码质量：
baseline/main/high。默认baseline
        :type Profile: str
        :param BitrateToOrig: 当设置的码率>原始码率时，是否以原始码率为准。
0：否， 1：是
默认 0。
        :type BitrateToOrig: int
        :param HeightToOrig: 当设置的高度>原始高度时，是否以原始高度为准。
0：否， 1：是
默认 0。
        :type HeightToOrig: int
        :param FpsToOrig: 当设置的帧率>原始帧率时，是否以原始帧率为准。
0：否， 1：是
默认 0。
        :type FpsToOrig: int
        :param NeedVideo: 是否保留视频。0：否，1：是。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音频。0：否，1：是。
        :type NeedAudio: int
        :param TemplateId: 模板 ID。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 模板描述。
        :type Description: str
        :param AiTransCode: 是否是极速高清模板，0：否，1：是。默认0。
        :type AiTransCode: int
        :param AdaptBitratePercent: 极速高清视频码率压缩比。
极速高清目标码率=VideoBitrate * (1-AdaptBitratePercent)

取值范围：0.0到0.5
        :type AdaptBitratePercent: float
        :param ShortEdgeAsHeight: 是否以短边作为高度，0：否，1：是。默认0。
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortEdgeAsHeight: int
        """
        self.Vcodec = None
        self.VideoBitrate = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.AiTransCode = None
        self.AdaptBitratePercent = None
        self.ShortEdgeAsHeight = None


    def _deserialize(self, params):
        self.Vcodec = params.get("Vcodec")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")
        self.ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TimeValue(AbstractModel):
    """某个时间点的指标的数值是多少。

    """

    def __init__(self):
        """
        :param Time: UTC 时间，时间格式：yyyy-mm-ddTHH:MM:SSZ。
        :type Time: str
        :param Num: 数值。
        :type Num: int
        """
        self.Time = None
        self.Num = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TranscodeDetailInfo(AbstractModel):
    """转码详细信息。

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param StartTime: 开始时间（北京时间），格式：yyyy-mm-dd HH:MM。
        :type StartTime: str
        :param EndTime: 结束时间（北京时间），格式：yyyy-mm-dd HH:MM。
        :type EndTime: str
        :param Duration: 转码时长，单位：分钟。
注意：因推流过程中可能有中断重推情况，此处时长为真实转码时长累加值，并非结束时间和开始时间的间隔。
        :type Duration: int
        :param ModuleCodec: 编码方式，带模块，
示例：
liveprocessor_H264：直播转码-H264，
liveprocessor_H265： 直播转码-H265，
topspeed_H264：极速高清-H264，
topspeed_H265：极速高清-H265。
        :type ModuleCodec: str
        :param Bitrate: 码率。
        :type Bitrate: int
        :param Type: 类型，包含：转码（Transcode），混流（MixStream），水印（WaterMark）。
        :type Type: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param Resolution: 分辨率。
        :type Resolution: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.Duration = None
        self.ModuleCodec = None
        self.Bitrate = None
        self.Type = None
        self.PushDomain = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Duration = params.get("Duration")
        self.ModuleCodec = params.get("ModuleCodec")
        self.Bitrate = params.get("Bitrate")
        self.Type = params.get("Type")
        self.PushDomain = params.get("PushDomain")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UnBindLiveDomainCertRequest(AbstractModel):
    """UnBindLiveDomainCert请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UnBindLiveDomainCertResponse(AbstractModel):
    """UnBindLiveDomainCert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印 ID。
在添加水印接口 [AddLiveWatermark](/document/product/267/30154) 调用返回值中获取水印 ID。
        :type WatermarkId: int
        :param PictureUrl: 水印图片 URL。
URL中禁止包含的字符：
 ;(){}$>`#"\'|
        :type PictureUrl: str
        :param XPosition: 显示位置，X轴偏移，单位是百分比，默认 0。
        :type XPosition: int
        :param YPosition: 显示位置，Y轴偏移，单位是百分比，默认 0。
        :type YPosition: int
        :param WatermarkName: 水印名称。
最长16字节。
        :type WatermarkName: str
        :param Width: 水印宽度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始宽度。
        :type Width: int
        :param Height: 水印高度，占直播原始画面宽度百分比，建议高宽只设置一项，另外一项会自适应缩放，避免变形。默认原始高度。
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateLiveWatermarkResponse(AbstractModel):
    """UpdateLiveWatermark返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WatermarkInfo(AbstractModel):
    """水印信息。

    """

    def __init__(self):
        """
        :param WatermarkId: 水印 ID。
        :type WatermarkId: int
        :param PictureUrl: 水印图片 URL。
        :type PictureUrl: str
        :param XPosition: 显示位置，X 轴偏移。
        :type XPosition: int
        :param YPosition: 显示位置，Y 轴偏移。
        :type YPosition: int
        :param WatermarkName: 水印名称。
        :type WatermarkName: str
        :param Status: 当前状态。0：未使用，1:使用中。
        :type Status: int
        :param CreateTime: 添加时间。
        :type CreateTime: str
        :param Width: 水印宽。
        :type Width: int
        :param Height: 水印高。
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Status = None
        self.CreateTime = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        