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


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param DelayTime: 延播时间，单位：秒，上限：600秒。
        :type DelayTime: int
        :param ExpireTime: 延播设置的过期时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：默认7天后过期，且最长支持7天内生效。
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
        :type PlayType: int
        :param IsDelayLive: 默认 0 ：普通直播，
1：慢直播。
        :type IsDelayLive: int
        """
        self.DomainName = None
        self.DomainType = None
        self.PlayType = None
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")


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


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param PictureUrl: 水印图片url。
        :type PictureUrl: str
        :param WatermarkName: 水印名称。
        :type WatermarkName: str
        :param XPosition: 显示位置,X轴偏移。
        :type XPosition: int
        :param YPosition: 显示位置,Y轴偏移。
        :type YPosition: int
        """
        self.PictureUrl = None
        self.WatermarkName = None
        self.XPosition = None
        self.YPosition = None


    def _deserialize(self, params):
        self.PictureUrl = params.get("PictureUrl")
        self.WatermarkName = params.get("WatermarkName")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")


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


class BindLiveDomainCertRequest(AbstractModel):
    """BindLiveDomainCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书Id。
        :type CertId: int
        :param DomainName: 播放域名。
        :type DomainName: str
        :param Status: 状态，0： 关闭  1：打开。
        :type Status: int
        """
        self.CertId = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")


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


class CallBackRuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        """
        :param CreateTime: 规则创建时间。
        :type CreateTime: str
        :param UpdateTime: 规则更新时间。
        :type UpdateTime: str
        :param TemplateId: 模板Id。
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


class CallBackTemplateInfo(AbstractModel):
    """回调模板信息

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param StreamBeginNotifyUrl: 开播回调URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 断流回调URL。
        :type StreamEndNotifyUrl: str
        :param StreamMixNotifyUrl: 混流回调URL。
        :type StreamMixNotifyUrl: str
        :param RecordNotifyUrl: 录制回调URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截图回调URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鉴黄回调URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回调的鉴权key
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


class CertInfo(AbstractModel):
    """证书信息

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
0：腾讯云托管证书
1：用户添加证书。
        :type CertType: int
        :param CertExpireTime: 证书过期时间，UTC格式。
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


class CreateLiveCallbackRuleRequest(AbstractModel):
    """CreateLiveCallbackRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
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


class CreateLiveCallbackTemplateRequest(AbstractModel):
    """CreateLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称。非空的字符串
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param StreamBeginNotifyUrl: 开播回调URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 断流回调URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 录制回调URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截图回调URL，
相关协议文档：[事件消息通知](/document/product/267/32744)。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鉴黄回调URL，
相关协议文档：[事件消息通知](/document/product/267/32741)。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回调key，回调URL公用，鉴权回调说明详见回调格式文档
        :type CallbackKey: str
        """
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")


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


class CreateLiveCertRequest(AbstractModel):
    """CreateLiveCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertType: 证书类型。0-用户添加证书；1-腾讯云托管证书。
        :type CertType: int
        :param HttpsCrt: 证书内容，即公钥。
        :type HttpsCrt: str
        :param HttpsKey: 私钥。
        :type HttpsKey: str
        :param CertName: 证书名称。
        :type CertName: str
        :param Description: 描述。
        :type Description: str
        """
        self.CertType = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.CertName = None
        self.Description = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")


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


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param AppName: 推流App名。
        :type AppName: str
        :param DomainName: 推流域名。多域名推流必须设置。
        :type DomainName: str
        :param StartTime: 录制开始时间。中国标准时间，需要URLEncode。如 2017-01-01 10:10:01，编码为：2017-01-01+10%3a10%3a01。
定时录制模式，必须设置该字段；实时视频录制模式，忽略该字段。
        :type StartTime: str
        :param EndTime: 录制结束时间。中国标准时间，需要URLEncode。如 2017-01-01 10:30:01，编码为：2017-01-01+10%3a30%3a01。
定时录制模式，必须设置该字段；实时录制模式，为可选字段。如果通过Highlight参数，设置录制为实时视频录制模式，其设置的结束时间不应超过当前时间+30分钟，如果设置的结束时间超过当前时间+30分钟或者小于当前时间或者不设置该参数，则实际结束时间为当前时间+30分钟。
        :type EndTime: str
        :param RecordType: 录制类型。
“video” : 音视频录制【默认】。
“audio” : 纯音频录制。
在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。
        :type RecordType: str
        :param FileFormat: 录制文件格式。其值为：
“flv”,“hls”,”mp4”,“aac”,”mp3”，默认“flv”。
在定时录制模式或实时视频录制模式下，该参数均有效，不区分大小写。
        :type FileFormat: str
        :param Highlight: 开启实时视频录制模式标志。0：不开启实时视频录制模式，即采用定时录制模式【默认】；1：开启实时视频录制模式。
        :type Highlight: int
        :param MixStream: 开启A+B=C混流C流录制标志。0：不开启A+B=C混流C流录制【默认】；1：开启A+B=C混流C流录制。
在定时录制模式或实时视频录制模式下，该参数均有效。
        :type MixStream: int
        :param StreamParam: 录制流参数。当前支持以下参数：
record_interval - 录制分片时长，单位 秒，1800 - 7200
storage_time - 录制文件存储时长，单位 秒
eg. record_interval=3600&storage_time=2592000
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


class CreateLiveRecordResponse(AbstractModel):
    """CreateLiveRecord返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，全局唯一标识录制任务。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRuleRequest(AbstractModel):
    """CreateLiveRecordRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param AppName: 推流路径。
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


class CreateLiveRecordTemplateRequest(AbstractModel):
    """CreateLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名。非空的字符串
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
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS专属录制参数。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        """
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None


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


class CreateLiveSnapshotRuleRequest(AbstractModel):
    """CreateLiveSnapshotRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param TemplateId: 模板Id。
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


class CreateLiveSnapshotTemplateRequest(AbstractModel):
    """CreateLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称。非空的字符串。
        :type TemplateName: str
        :param CosAppId: Cos AppId。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名称。
        :type CosBucket: str
        :param CosRegion: Cos地区。
        :type CosRegion: str
        :param Description: 描述信息。
        :type Description: str
        :param SnapshotInterval: 截图间隔，单位s，默认10s。
        :type SnapshotInterval: int
        :param Width: 截图宽度。默认：0（原始宽）。
        :type Width: int
        :param Height: 截图高度。默认：0（原始高）。
        :type Height: int
        :param PornFlag: 是否开启鉴黄，0：不开启，1：开启。默认：0。
        :type PornFlag: int
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


class CreateLiveTranscodeRuleRequest(AbstractModel):
    """CreateLiveTranscodeRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param StreamName: 流名称。
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


class CreateLiveTranscodeTemplateRequest(AbstractModel):
    """CreateLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateName: 模板名称，例：900 900p 仅支持字母和数字的组合。
        :type TemplateName: str
        :param VideoBitrate: 视频码率。范围：100-8000。
        :type VideoBitrate: int
        :param Vcodec: 视频编码：h264/h265，默认h264。
注意：当前该参数未生效，待后续支持！
        :type Vcodec: str
        :param Acodec: 音频编码：aac，默认原始音频格式。
注意：当前该参数未生效，待后续支持！
        :type Acodec: str
        :param AudioBitrate: 音频码率：默认0。0-500。
        :type AudioBitrate: int
        :param Description: 模板描述。
        :type Description: str
        :param Width: 宽，默认0。
        :type Width: int
        :param NeedVideo: 是否保留视频，0：否，1：是。默认1。
注意：当前该参数未生效，待后续支持！
        :type NeedVideo: int
        :param NeedAudio: 是否保留音频，0：否，1：是。默认1。
注意：当前该参数未生效，待后续支持！
        :type NeedAudio: int
        :param Height: 高，默认0。
        :type Height: int
        :param Fps: 帧率，默认0。
        :type Fps: int
        :param Gop: 关键帧间隔，单位：秒。默认原始的间隔
        :type Gop: int
        :param Rotate: 是否旋转，0：否，1：是。默认0。
        :type Rotate: int
        :param Profile: 编码质量：
baseline/main/high。默认baseline
        :type Profile: str
        :param BitrateToOrig: 是否不超过原始码率，0：否，1：是。默认0。
        :type BitrateToOrig: int
        :param HeightToOrig: 是否不超过原始高，0：否，1：是。默认0。
        :type HeightToOrig: int
        :param FpsToOrig: 是否不超过原始帧率，0：否，1：是。默认0。
        :type FpsToOrig: int
        """
        self.TemplateName = None
        self.VideoBitrate = None
        self.Vcodec = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Description = None
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


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Vcodec = params.get("Vcodec")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Description = params.get("Description")
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


class CreateLiveWatermarkRuleRequest(AbstractModel):
    """CreateLiveWatermarkRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
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


class CreatePullStreamConfigRequest(AbstractModel):
    """CreatePullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url，目前限制该目标地址为腾讯域名。
        :type ToUrl: str
        :param AreaId: 区域id,1-深圳,2-上海，3-天津,4-香港。
        :type AreaId: int
        :param IspId: 运营商id,1-电信,2-移动,3-联通,4-其他,AreaId为4的时候,IspId只能为其他。
        :type IspId: int
        :param StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
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


class CreatePullStreamConfigResponse(AbstractModel):
    """CreatePullStreamConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置成功后的id。
        :type ConfigId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")


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


class DeleteLiveCallbackRuleRequest(AbstractModel):
    """DeleteLiveCallbackRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
        :type AppName: str
        """
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


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


class DeleteLiveCallbackTemplateRequest(AbstractModel):
    """DeleteLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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


class DeleteLiveCertRequest(AbstractModel):
    """DeleteLiveCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书Id。
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")


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


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TaskId: 任务ID，全局唯一标识录制任务。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


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


class DeleteLiveRecordRuleRequest(AbstractModel):
    """DeleteLiveRecordRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配
        :type DomainName: str
        :param AppName: 推流路径。域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配
        :type AppName: str
        :param StreamName: 流名称。域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


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


class DeleteLiveRecordTemplateRequest(AbstractModel):
    """DeleteLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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


class DeleteLiveSnapshotRuleRequest(AbstractModel):
    """DeleteLiveSnapshotRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
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


class DeleteLiveSnapshotTemplateRequest(AbstractModel):
    """DeleteLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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


class DeleteLiveTranscodeRuleRequest(AbstractModel):
    """DeleteLiveTranscodeRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。域名维度转码，域名+AppName+StreamName唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配
        :type DomainName: str
        :param AppName: 推流路径。域名+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配
        :type AppName: str
        :param StreamName: 流名称。域名+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配
        :type StreamName: str
        :param TemplateId: 模板ID域名+AppName+StreamName+TemplateId唯一标识单个转码规则，如需删除需要强匹配，比如AppName为空也需要传空字符串进行强匹配
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


class DeleteLiveTranscodeTemplateRequest(AbstractModel):
    """DeleteLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")


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


class DeleteLiveWatermarkRuleRequest(AbstractModel):
    """DeleteLiveWatermarkRule请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路径。
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


class DeletePullStreamConfigRequest(AbstractModel):
    """DeletePullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


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


class DescribeLiveCallbackTemplateRequest(AbstractModel):
    """DescribeLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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


class DescribeLiveCertRequest(AbstractModel):
    """DescribeLiveCert请求参数结构体

    """

    def __init__(self):
        """
        :param CertId: 证书Id。
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")


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


class DescribeLiveDomainResponse(AbstractModel):
    """DescribeLiveDomain返回参数结构体

    """

    def __init__(self):
        """
        :param DomainInfo: 域名信息。
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


class DescribeLiveDomainsRequest(AbstractModel):
    """DescribeLiveDomains请求参数结构体

    """

    def __init__(self):
        """
        :param DomainStatus: 域名状态过滤。0-停用，1-启用
        :type DomainStatus: int
        :param DomainType: 域名类型过滤。0-推流，1-播放
        :type DomainType: int
        :param PageSize: 分页大小，范围：10~100。默认10
        :type PageSize: int
        :param PageNum: 取第几页，范围：1~100000。默认1
        :type PageNum: int
        :param IsDelayLive: 0 普通直播 1慢直播 默认0
        :type IsDelayLive: int
        """
        self.DomainStatus = None
        self.DomainType = None
        self.PageSize = None
        self.PageNum = None
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.DomainStatus = params.get("DomainStatus")
        self.DomainType = params.get("DomainType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.IsDelayLive = params.get("IsDelayLive")


class DescribeLiveDomainsResponse(AbstractModel):
    """DescribeLiveDomains返回参数结构体

    """

    def __init__(self):
        """
        :param AllCount: 总记录数
        :type AllCount: int
        :param DomainList: 域名详细信息列表
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
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


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


class DescribeLiveRecordTemplateRequest(AbstractModel):
    """DescribeLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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


class DescribeLiveRecordTemplatesRequest(AbstractModel):
    """DescribeLiveRecordTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param IsDelayLive: 是否属于慢直播模板
        :type IsDelayLive: int
        """
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.IsDelayLive = params.get("IsDelayLive")


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


class DescribeLiveSnapshotTemplateRequest(AbstractModel):
    """DescribeLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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
        :param AppName: 应用名称。
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
取值范围：1~100 之前的任意整数。
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


class DescribeLiveStreamOnlineInfoRequest(AbstractModel):
    """DescribeLiveStreamOnlineInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 取得第几页。
默认值：1。
        :type PageNum: int
        :param PageSize: 分页大小。
最大值：100。
取值范围：1~100 之前的任意整数。
默认值：10。
        :type PageSize: int
        :param Status: 0:未开始推流 1:正在推流
        :type Status: int
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.PageNum = None
        self.PageSize = None
        self.Status = None
        self.StreamName = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.Status = params.get("Status")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamOnlineInfoResponse(AbstractModel):
    """DescribeLiveStreamOnlineInfo返回参数结构体

    """

    def __init__(self):
        """
        :param PageNum: 分页的页码。
        :type PageNum: int
        :param PageSize: 每页大小。
        :type PageSize: int
        :param TotalNum: 符合条件的总个数。
        :type TotalNum: int
        :param TotalPage: 总页数。
        :type TotalPage: int
        :param StreamInfoList: 流信息列表。
        :type StreamInfoList: list of StreamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.StreamInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("StreamInfoList") is not None:
            self.StreamInfoList = []
            for item in params.get("StreamInfoList"):
                obj = StreamInfo()
                obj._deserialize(item)
                self.StreamInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 应用名称。
        :type AppName: str
        :param PageNum: 取得第几页，默认1。
        :type PageNum: int
        :param PageSize: 每页大小，最大100。 
取值：10~100之间的任意整数。
默认值：10。
        :type PageSize: int
        :param StreamName: 流名称，精确查询。
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


class DescribeLiveStreamPublishedListRequest(AbstractModel):
    """DescribeLiveStreamPublishedList请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 您的域名。
        :type DomainName: str
        :param EndTime: 结束时间。
UTC 格式，例如：2016-06-30T19:00:00Z。
不超过当前时间。
        :type EndTime: str
        :param StartTime: 起始时间。 
UTC 格式，例如：2016-06-29T19:00:00Z。
和当前时间相隔不超过7天。
        :type StartTime: str
        :param AppName: 直播流所属应用名称。
        :type AppName: str
        :param PageNum: 取得第几页。
默认值：1。
        :type PageNum: int
        :param PageSize: 分页大小。
最大值：100。
取值范围：1~100 之前的任意整数。
默认值：10。
        :type PageSize: int
        """
        self.DomainName = None
        self.EndTime = None
        self.StartTime = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


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


class DescribeLiveStreamPushInfoListRequest(AbstractModel):
    """DescribeLiveStreamPushInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param AppName: 推流路径。
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


class DescribeLiveStreamStateRequest(AbstractModel):
    """DescribeLiveStreamState请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
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


class DescribeLiveTranscodeDetailInfoRequest(AbstractModel):
    """DescribeLiveTranscodeDetailInfo请求参数结构体

    """

    def __init__(self):
        """
        :param DayTime: 起始时间，北京时间，
格式：yyyymmdd。
注意：当前只支持查询近30天内某天的详细数据。
        :type DayTime: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param PageNum: 页数，默认1，
不超过100页。
        :type PageNum: int
        :param PageSize: 每页个数，默认20，
范围：[10,1000]。
        :type PageSize: int
        """
        self.DayTime = None
        self.PushDomain = None
        self.StreamName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DayTime = params.get("DayTime")
        self.PushDomain = params.get("PushDomain")
        self.StreamName = params.get("StreamName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


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


class DescribeLiveTranscodeRulesRequest(AbstractModel):
    """DescribeLiveTranscodeRules请求参数结构体

    """


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


class DescribeLiveTranscodeTemplateRequest(AbstractModel):
    """DescribeLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


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


class DescribeLiveWatermarkRequest(AbstractModel):
    """DescribeLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")


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
        :param StatType: 统计的类型，可选值包括”Province”，”Isp”
        :type StatType: str
        :param PlayDomains: 不填则为总体数据。
        :type PlayDomains: list of str
        :param PageNum: 页号，
范围是[1,1000]，
默认值是1
        :type PageNum: int
        :param PageSize: 每页个数，范围是[1,1000]，
默认值是20
        :type PageSize: int
        """
        self.StartTime = None
        self.EndTime = None
        self.StatType = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


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
        :param PageSize: 每页的记录数
        :type PageSize: int
        :param PageNum: 页号
        :type PageNum: int
        :param TotalNum: 总记录数
        :type TotalNum: int
        :param TotalPage: 总页数
        :type TotalPage: int
        :param DataInfoList: 省份或运营商汇总数据列表
        :type DataInfoList: list of ProIspPlaySumInfo
        :param AvgFluxPerSecond: 平均带宽
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
        :param ProvinceNames: 非必传参数，要查询的省份（地区）英文名称列表，如 Beijing
        :type ProvinceNames: list of str
        :param IspNames: 非必传参数，要查询的运营商英文名称列表，如 China Mobile ，如果为空，查询所有运营商的数据
        :type IspNames: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")


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


class DescribePullStreamConfigsRequest(AbstractModel):
    """DescribePullStreamConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


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


class DescribeStreamDayPlayInfoListRequest(AbstractModel):
    """DescribeStreamDayPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param DayTime: 日期，
格式：YYYY-mm-dd。
        :type DayTime: str
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param PageNum: 页号，范围[1,10]，默认值是1。
        :type PageNum: int
        :param PageSize: 每页个数，范围[100,1000]，默认值是1000。
        :type PageSize: int
        """
        self.DayTime = None
        self.PlayDomain = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DayTime = params.get("DayTime")
        self.PlayDomain = params.get("PlayDomain")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


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


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间，北京时间，格式为yyyy-mm-dd HH:MM:SS，
当前时间 和 开始时间 间隔不超过30天。
        :type StartTime: str
        :param EndTime: 结束时间，北京时间，格式为yyyy-mm-dd HH:MM:SS，
结束时间 和 开始时间  必须在同一天内。
        :type EndTime: str
        :param PlayDomain: 播放域名，
若不填，则为查询所有播放域名的在线流数据。
        :type PlayDomain: str
        :param StreamName: 流名称，精确匹配。
若不填，则为查询总体播放数据。
        :type StreamName: str
        :param AppName: 播放路径，精确匹配，不支持。
若不填，则为查询总体播放数据。
        :type AppName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomain = None
        self.StreamName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomain = params.get("PlayDomain")
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")


class DescribeStreamPlayInfoListResponse(AbstractModel):
    """DescribeStreamPlayInfoList返回参数结构体

    """

    def __init__(self):
        """
        :param DataInfoList: 统计信息列表。
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
0：腾讯云托管证书
1：用户添加证书。
        :type CertType: int
        :param CertExpireTime: 证书过期时间，UTC格式。
        :type CertExpireTime: str
        :param DomainName: 使用此证书的域名名称。
        :type DomainName: str
        :param Status: 证书状态
        :type Status: int
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


class DomainInfo(AbstractModel):
    """直播域名信息

    """

    def __init__(self):
        """
        :param Name: 直播域名
        :type Name: str
        :param Type: 域名类型。0-推流，1-播放
        :type Type: int
        :param Status: 域名状态。0-停用，1-启用
        :type Status: int
        :param CreateTime: 添加时间
        :type CreateTime: str
        :param BCName: 是否有CName到固定规则域名。0-否，1-是
        :type BCName: int
        :param TargetDomain: cname对应的域名
        :type TargetDomain: str
        :param PlayType: 播放区域，只在Type=1时该参数有意义。
1-国内，2-全球，3-海外。
        :type PlayType: int
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.BCName = None
        self.TargetDomain = None
        self.PlayType = None
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BCName = params.get("BCName")
        self.TargetDomain = params.get("TargetDomain")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")


class DropLiveStreamRequest(AbstractModel):
    """DropLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param AppName: 应用名称。
        :type AppName: str
        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


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


class EnableLiveDomainRequest(AbstractModel):
    """EnableLiveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 待启用的直播域名
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


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


class ForbidLiveDomainRequest(AbstractModel):
    """ForbidLiveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 停用的直播域名
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


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


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名称。
        :type StreamName: str
        :param ResumeTime: 恢复流的时间。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：默认禁播90天，且最长支持禁播90天。
        :type ResumeTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")


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


class HlsSpecialParam(AbstractModel):
    """HLS专属录制参数

    """

    def __init__(self):
        """
        :param FlowContinueDuration: HLS续流超时时间。
        :type FlowContinueDuration: int
        """
        self.FlowContinueDuration = None


    def _deserialize(self, params):
        self.FlowContinueDuration = params.get("FlowContinueDuration")


class LogInfo(AbstractModel):
    """日志url信息

    """

    def __init__(self):
        """
        :param LogName: 日志名称。
        :type LogName: str
        :param LogUrl: 日志Url。
        :type LogUrl: str
        :param LogTime: 日志生成时间
        :type LogTime: str
        """
        self.LogName = None
        self.LogUrl = None
        self.LogTime = None


    def _deserialize(self, params):
        self.LogName = params.get("LogName")
        self.LogUrl = params.get("LogUrl")
        self.LogTime = params.get("LogTime")


class ModifyLiveCallbackTemplateRequest(AbstractModel):
    """ModifyLiveCallbackTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param StreamBeginNotifyUrl: 开播回调URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 断流回调URL。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 录制回调URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截图回调URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鉴黄回调URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回调key，回调URL公用，鉴权回调说明详见回调格式文档
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


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param AuthKey: 鉴权key。
        :type AuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        :param AuthBackKey: 鉴权backkey。
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


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param MasterAuthKey: 主鉴权key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 备鉴权key。
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


class ModifyLiveRecordTemplateRequest(AbstractModel):
    """ModifyLiveRecordTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param TemplateName: 模板名称。
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
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None


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


class ModifyLiveSnapshotTemplateRequest(AbstractModel):
    """ModifyLiveSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param SnapshotInterval: 截图时间间隔
        :type SnapshotInterval: int
        :param Width: 截图宽度。
        :type Width: int
        :param Height: 截图高度。
        :type Height: int
        :param PornFlag: 是否开启鉴黄，0：不开启，1：开启。
        :type PornFlag: int
        :param CosAppId: Cos AppId。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名称。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
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


class ModifyLiveTranscodeTemplateRequest(AbstractModel):
    """ModifyLiveTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param Vcodec: 视频编码：
h264/h265。
        :type Vcodec: str
        :param Acodec: 音频编码：
aac/mp3。
        :type Acodec: str
        :param AudioBitrate: 音频码率，默认0。0-500
        :type AudioBitrate: int
        :param Description: 模板描述。
        :type Description: str
        :param VideoBitrate: 视频码率。100-8000
        :type VideoBitrate: int
        :param Width: 宽。0-3000
        :type Width: int
        :param NeedVideo: 是否保留视频，0：否，1：是。默认1。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音频，0：否，1：是。默认1。
        :type NeedAudio: int
        :param Height: 高。0-3000
        :type Height: int
        :param Fps: 帧率。0-200
        :type Fps: int
        :param Gop: 关键帧间隔，单位：秒。0-50
        :type Gop: int
        :param Rotate: 旋转角度。0 90 180 270
        :type Rotate: int
        :param Profile: 编码质量：
baseline/main/high。
        :type Profile: str
        :param BitrateToOrig: 是否不超过原始码率。0：否，1：是。默认0。
        :type BitrateToOrig: int
        :param HeightToOrig: 是否不超过原始高。0：否，1：是。默认0。
        :type HeightToOrig: int
        :param FpsToOrig: 是否不超过原始帧率。0：否，1：是。默认0。
        :type FpsToOrig: int
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


class ModifyPullStreamConfigRequest(AbstractModel):
    """ModifyPullStreamConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url。
        :type ToUrl: str
        :param AreaId: 区域id,1-深圳,2-上海，3-天津,4-香港。如有改动，需同时传入IspId。
        :type AreaId: int
        :param IspId: 运营商id,1-电信,2-移动,3-联通,4-其他,AreaId为4的时候,IspId只能为其他。如有改动，需同时传入AreaId。
        :type IspId: int
        :param StartTime: 开始时间。
使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
        :type StartTime: str
        :param EndTime: 结束时间，注意：
1. 结束时间必须大于开始时间；
2. 结束时间和开始时间必须大于当前时间；
3. 结束时间 和 开始时间 间隔必须小于七天。

使用UTC格式时间，
例如：2019-01-08T10:00:00Z。
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


class ModifyPullStreamStatusRequest(AbstractModel):
    """ModifyPullStreamStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ConfigIds: 配置id列表。
        :type ConfigIds: list of str
        :param Status: 目标状态。0无效，2正在运行，4暂停。
        :type Status: str
        """
        self.ConfigIds = None
        self.Status = None


    def _deserialize(self, params):
        self.ConfigIds = params.get("ConfigIds")
        self.Status = params.get("Status")


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


class PlayAuthKeyInfo(AbstractModel):
    """播放鉴权key信息

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param AuthKey: 鉴权key。
        :type AuthKey: str
        :param AuthDelta: 有效时间，单位：秒。
        :type AuthDelta: int
        :param AuthBackKey: 鉴权BackKey。
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


class PlayDataInfoByStream(AbstractModel):
    """流维度的播放信息

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TotalFlux: 总流量（单位MB）。
        :type TotalFlux: float
        """
        self.StreamName = None
        self.TotalFlux = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TotalFlux = params.get("TotalFlux")


class PlayStatInfo(AbstractModel):
    """按省份运营商查询的播放信息

    """

    def __init__(self):
        """
        :param Time: 数据时间点。
        :type Time: str
        :param Value: 带宽/流量/请求数/并发连接数/下载速度的值，若没数据返回时该值为0
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class ProIspPlaySumInfo(AbstractModel):
    """获取省份/运营商的播放信息

    """

    def __init__(self):
        """
        :param Name: 省份/运营商。
        :type Name: str
        :param TotalFlux: 总流量，单位：MB。
        :type TotalFlux: float
        :param TotalRequest: 总请求数。
        :type TotalRequest: int
        :param AvgFluxPerSecond: 平均下载流量，单位：MB/s
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


class PublishTime(AbstractModel):
    """推流时间

    """

    def __init__(self):
        """
        :param PublishTime: 推流时间
UTC 格式，例如：2018-06-29T19:00:00Z。
        :type PublishTime: str
        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")


class PullStreamConfig(AbstractModel):
    """拉流配置

    """

    def __init__(self):
        """
        :param ConfigId: 拉流配置Id。
        :type ConfigId: str
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url。
        :type ToUrl: str
        :param AreaName: 区域名。
        :type AreaName: str
        :param IspName: 运营商名。
        :type IspName: str
        :param StartTime: 开始时间。
UTC格式时间，
例如：2019-01-08T10:00:00Z。
        :type StartTime: str
        :param EndTime: 结束时间。

UTC格式时间，
例如：2019-01-08T10:00:00Z。
        :type EndTime: str
        :param Status: 0无效，1初始状态，2正在运行，3拉起失败，4暂停。
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


class PushAuthKeyInfo(AbstractModel):
    """推流鉴权key信息

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否启用，0：关闭，1：启用。
        :type Enable: int
        :param MasterAuthKey: 主鉴权key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 备鉴权key。
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


class PushDataInfo(AbstractModel):
    """推流数据信息

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param AppName: 推流路径。
        :type AppName: str
        :param ClientIp: 推流客户端ip。
        :type ClientIp: str
        :param ServerIp: 接流服务器ip。
        :type ServerIp: str
        :param VideoFps: 推流视频帧率，单位是Hz。
        :type VideoFps: int
        :param VideoSpeed: 推流视频码率，单位是bps。
        :type VideoSpeed: int
        :param AudioFps: 推流音频帧率，单位是Hz。
        :type AudioFps: int
        :param AudioSpeed: 推流音频码率，单位是bps。
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


class RecordParam(AbstractModel):
    """录制模板参数

    """

    def __init__(self):
        """
        :param RecordInterval: 录制间隔。
单位秒，默认值1800。
取值范围:300-7200。
此参数对 HLS 无效，当录制 HLS 时从推流到断流生成一个文件。
        :type RecordInterval: int
        :param StorageTime: 录制存储时长。
单位秒，取值范围： 0-5184000。
0表示永久存储。
        :type StorageTime: int
        :param Enable: 是否开启当前格式录制，0 否 1是。默认值0。
        :type Enable: int
        """
        self.RecordInterval = None
        self.StorageTime = None
        self.Enable = None


    def _deserialize(self, params):
        self.RecordInterval = params.get("RecordInterval")
        self.StorageTime = params.get("StorageTime")
        self.Enable = params.get("Enable")


class RecordTemplateInfo(AbstractModel):
    """录制模板信息

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param Description: 描述信息。
        :type Description: str
        :param FlvParam: Flv录制参数。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: Hls录制参数。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4录制参数。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: Aac录制参数。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS录制定制参数
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
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


class ResumeDelayLiveStreamRequest(AbstractModel):
    """ResumeDelayLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
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


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param AppName: 应用名称。
        :type AppName: str
        :param DomainName: 您的加速域名。
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


class RuleInfo(AbstractModel):
    """规则信息

    """

    def __init__(self):
        """
        :param CreateTime: 规则创建时间。
        :type CreateTime: str
        :param UpdateTime: 规则更新时间。
        :type UpdateTime: str
        :param TemplateId: 模板Id。
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


class SetLiveWatermarkStatusRequest(AbstractModel):
    """SetLiveWatermarkStatus请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param Status: 状态。0：停用，1:启用
        :type Status: int
        """
        self.WatermarkId = None
        self.Status = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.Status = params.get("Status")


class SetLiveWatermarkStatusResponse(AbstractModel):
    """SetLiveWatermarkStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnapshotTemplateInfo(AbstractModel):
    """截图模板信息

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param SnapshotInterval: 截图时间间隔。5-300
        :type SnapshotInterval: int
        :param Width: 截图宽度。0-3000 0原始宽度并适配原始比例
        :type Width: int
        :param Height: 截图高度。0-2000 0原始高度并适配原始比例
        :type Height: int
        :param PornFlag: 是否开启鉴黄，0：不开启，1：开启。
        :type PornFlag: int
        :param CosAppId: Cos AppId。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名称。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
        :param Description: 模板描述
        :type Description: str
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


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord请求参数结构体

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param TaskId: 任务ID，全局唯一标识录制任务。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


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
UTC格式时间，
例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param StreamEndTime: 推流结束时间。
UTC格式时间，
例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param StopReason: 停止原因。
        :type StopReason: str
        :param Duration: 推流持续时长，单位：秒。
        :type Duration: int
        :param ClientIp: 主播IP。
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


class StreamInfo(AbstractModel):
    """推流信息

    """

    def __init__(self):
        """
        :param AppName: 直播流所属应用名称
        :type AppName: str
        :param CreateMode: 创建模式
        :type CreateMode: str
        :param CreateTime: 创建时间，如: 2018-07-13 14:48:23
        :type CreateTime: str
        :param Status: 流状态
        :type Status: int
        :param StreamId: 流id
        :type StreamId: str
        :param StreamName: 流名称
        :type StreamName: str
        :param WaterMarkId: 水印id
        :type WaterMarkId: str
        """
        self.AppName = None
        self.CreateMode = None
        self.CreateTime = None
        self.Status = None
        self.StreamId = None
        self.StreamName = None
        self.WaterMarkId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.CreateMode = params.get("CreateMode")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.StreamId = params.get("StreamId")
        self.StreamName = params.get("StreamName")
        self.WaterMarkId = params.get("WaterMarkId")


class StreamName(AbstractModel):
    """流名称列表

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        """
        self.StreamName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")


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


class TemplateInfo(AbstractModel):
    """转码模板信息

    """

    def __init__(self):
        """
        :param Vcodec: 视频编码：
h264/h265。
        :type Vcodec: str
        :param VideoBitrate: 视频码率。100-8000kbps
        :type VideoBitrate: int
        :param Acodec: 音频编码：aac/mp3
aac/mp3。
        :type Acodec: str
        :param AudioBitrate: 音频码率。0-500
        :type AudioBitrate: int
        :param Width: 宽。0-3000
        :type Width: int
        :param Height: 高。0-3000
        :type Height: int
        :param Fps: 帧率。0-200
        :type Fps: int
        :param Gop: 关键帧间隔，单位：秒。1-50
        :type Gop: int
        :param Rotate: 旋转角度。0 90 180 270
        :type Rotate: int
        :param Profile: 编码质量：
baseline/main/high。
        :type Profile: str
        :param BitrateToOrig: 是否不超过原始码率。0：否，1：是。
        :type BitrateToOrig: int
        :param HeightToOrig: 是否不超过原始高度。0：否，1：是。
        :type HeightToOrig: int
        :param FpsToOrig: 是否不超过原始帧率。0：否，1：是。
        :type FpsToOrig: int
        :param NeedVideo: 是否保留视频。0：否，1：是。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音频。0：否，1：是。
        :type NeedAudio: int
        :param TemplateId: 模板Id。
        :type TemplateId: int
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param Description: 模板描述
        :type Description: str
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


class TranscodeDetailInfo(AbstractModel):
    """转码详细信息

    """

    def __init__(self):
        """
        :param StreamName: 流名称。
        :type StreamName: str
        :param StartTime: 开始时间，北京时间，
格式：yyyy-mm-dd HH:MM。
        :type StartTime: str
        :param EndTime: 结束时间，北京时间，
格式：yyyy-mm-dd HH:MM。
        :type EndTime: str
        :param Duration: 转码时长，单位：分钟。
注意：因推流过程中可能有中断重推情况，此处时长为真实转码时长累加值，并非结束时间和开始时间的间隔。
        :type Duration: int
        :param ModuleCodec: 编码方式，带模块，
示例：
liveprocessor_H264 =》直播转码-H264，
liveprocessor_H265 =》 直播转码-H265，
topspeed_H264 =》极速高清-H264，
topspeed_H265 =》极速高清-H265。
        :type ModuleCodec: str
        :param Bitrate: 码率。
        :type Bitrate: int
        :param Type: 类型，包含：转码(Transcode)，混流(MixStream)，水印(WaterMark)。
        :type Type: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.Duration = None
        self.ModuleCodec = None
        self.Bitrate = None
        self.Type = None
        self.PushDomain = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Duration = params.get("Duration")
        self.ModuleCodec = params.get("ModuleCodec")
        self.Bitrate = params.get("Bitrate")
        self.Type = params.get("Type")
        self.PushDomain = params.get("PushDomain")


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


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark请求参数结构体

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param PictureUrl: 水印图片url。
        :type PictureUrl: str
        :param XPosition: 显示位置，X轴偏移。
        :type XPosition: int
        :param YPosition: 显示位置，Y轴偏移。
        :type YPosition: int
        :param WatermarkName: 水印名称。
        :type WatermarkName: str
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")


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


class WatermarkInfo(AbstractModel):
    """水印信息

    """

    def __init__(self):
        """
        :param WatermarkId: 水印ID。
        :type WatermarkId: int
        :param PictureUrl: 水印图片url。
        :type PictureUrl: str
        :param XPosition: 显示位置，X轴偏移。
        :type XPosition: int
        :param YPosition: 显示位置，Y轴偏移。
        :type YPosition: int
        :param WatermarkName: 水印名称。
        :type WatermarkName: str
        :param Status: 当前状态。0：未使用，1:使用中。
        :type Status: int
        :param CreateTime: 添加时间。
        :type CreateTime: str
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")