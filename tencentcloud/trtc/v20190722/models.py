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


class AbnormalEvent(AbstractModel):
    """造成异常体验可能的异常事件类型

    """

    def __init__(self):
        r"""
        :param AbnormalEventId: 异常事件ID，具体值查看附录：异常体验ID映射表：https://cloud.tencent.com/document/product/647/44916
        :type AbnormalEventId: int
        :param PeerId: 远端用户ID,""：表示异常事件不是由远端用户产生
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerId: str
        """
        self.AbnormalEventId = None
        self.PeerId = None


    def _deserialize(self, params):
        self.AbnormalEventId = params.get("AbnormalEventId")
        self.PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalExperience(AbstractModel):
    """用户的异常体验及可能的原因

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID
        :type UserId: str
        :param ExperienceId: 异常体验ID
        :type ExperienceId: int
        :param RoomId: 字符串房间号
        :type RoomId: str
        :param AbnormalEventList: 异常事件数组
        :type AbnormalEventList: list of AbnormalEvent
        :param EventTime: 异常事件的上报时间
        :type EventTime: int
        """
        self.UserId = None
        self.ExperienceId = None
        self.RoomId = None
        self.AbnormalEventList = None
        self.EventTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.ExperienceId = params.get("ExperienceId")
        self.RoomId = params.get("RoomId")
        if params.get("AbnormalEventList") is not None:
            self.AbnormalEventList = []
            for item in params.get("AbnormalEventList"):
                obj = AbnormalEvent()
                obj._deserialize(item)
                self.AbnormalEventList.append(obj)
        self.EventTime = params.get("EventTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioParams(AbstractModel):
    """录制音频转码参数。

    """

    def __init__(self):
        r"""
        :param SampleRate: 音频采样率:
1：48000Hz（默认）;
2：44100Hz
3：16000Hz。
        :type SampleRate: int
        :param Channel: 声道数:
1：单声道;
2：双声道（默认）。
        :type Channel: int
        :param BitRate: 音频码率: 取值范围[32000, 128000] ，单位bps，默认64000bps。
        :type BitRate: int
        """
        self.SampleRate = None
        self.Channel = None
        self.BitRate = None


    def _deserialize(self, params):
        self.SampleRate = params.get("SampleRate")
        self.Channel = params.get("Channel")
        self.BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorage(AbstractModel):
    """第三方云存储的账号信息。

    """

    def __init__(self):
        r"""
        :param Vendor: 第三方云储存的供应商:
0：腾讯云存储 COS，暂不支持其他家。
        :type Vendor: int
        :param Region: 第三方云存储的地域信息。
        :type Region: str
        :param Bucket: 第三方存储桶信息。
        :type Bucket: str
        :param AccessKey: 第三方存储的access_key账号信息。
        :type AccessKey: str
        :param SecretKey: 第三方存储的secret_key账号信息。
        :type SecretKey: str
        :param FileNamePrefix: 第三方云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围a~z,A~Z,0~9,'_'和'-'，举个例子，录制文件xxx.m3u8在 ["prefix1", "prefix2"]作用下，会变成prefix1/prefix2/TaskId/xxx.m3u8。
        :type FileNamePrefix: list of str
        """
        self.Vendor = None
        self.Region = None
        self.Bucket = None
        self.AccessKey = None
        self.SecretKey = None
        self.FileNamePrefix = None


    def _deserialize(self, params):
        self.Vendor = params.get("Vendor")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")
        self.FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudVod(AbstractModel):
    """点播相关参数。

    """

    def __init__(self):
        r"""
        :param TencentVod: 腾讯云点播相关参数。
        :type TencentVod: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        self.TencentVod = None


    def _deserialize(self, params):
        if params.get("TencentVod") is not None:
            self.TencentVod = TencentVod()
            self.TencentVod._deserialize(params.get("TencentVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingRequest(AbstractModel):
    """CreateCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和录制的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，录制的TRTC房间所对应的RoomId。
        :type RoomId: str
        :param UserId: 录制机器人用于进入TRTC房间拉流的[UserId](https://cloud.tencent.com/document/product/647/46351#userid)，注意这个UserId不能与其他TRTC功能或者录制服务等已经使用的UserId重复，建议可以把房间ID作为userId的标识的一部分。
        :type UserId: str
        :param UserSig: 录制机器人用于进入TRTC房间拉流的用户签名，当前 UserId 对应的验证签名，相当于登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :type UserSig: str
        :param RecordParams: 云端录制控制参数。
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        :param StorageParams: 云端录制文件上传到云存储的参数(目前只支持使用腾讯云点播作为存储)。
        :type StorageParams: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        :param RoomIdType: TRTC房间号的类型，必须和录制的房间所对应的RoomId类型相同:
0: 字符串类型的RoomId
1: 32位整型的RoomId
        :type RoomIdType: int
        :param MixTranscodeParams: 混流的转码参数，录制模式为混流的时候可以设置。
        :type MixTranscodeParams: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        :param MixLayoutParams: 混流的布局参数，录制模式为混流的时候可以设置。
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param ResourceExpiredHour: 接口可以调用的时效性，从成功开启录制并获得任务ID后开始计算，超时后无法调用查询、更新和停止等接口，但是录制任务不会停止。 参数的单位是小时，默认72小时（3天），最大可设置720小时（30天），最小设置6小时。举例说明：如果不设置该参数，那么开始录制成功后，查询、更新和停止录制的调用时效为72个小时。
        :type ResourceExpiredHour: int
        :param PrivateMapKey: TRTC房间权限加密串，只有在TRTC控制台启用了高级权限控制的时候需要携带，在TRTC控制台如果开启高级权限控制后，TRTC 的后台服务系统会校验一个叫做 [PrivateMapKey]（https://cloud.tencent.com/document/product/647/32240） 的“权限票据”，权限票据中包含了一个加密后的 RoomId 和一个加密后的“权限位列表”。由于 PrivateMapKey 中包含 RoomId，所以只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。
        :type PrivateMapKey: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserId = None
        self.UserSig = None
        self.RecordParams = None
        self.StorageParams = None
        self.RoomIdType = None
        self.MixTranscodeParams = None
        self.MixLayoutParams = None
        self.ResourceExpiredHour = None
        self.PrivateMapKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserId = params.get("UserId")
        self.UserSig = params.get("UserSig")
        if params.get("RecordParams") is not None:
            self.RecordParams = RecordParams()
            self.RecordParams._deserialize(params.get("RecordParams"))
        if params.get("StorageParams") is not None:
            self.StorageParams = StorageParams()
            self.StorageParams._deserialize(params.get("StorageParams"))
        self.RoomIdType = params.get("RoomIdType")
        if params.get("MixTranscodeParams") is not None:
            self.MixTranscodeParams = MixTranscodeParams()
            self.MixTranscodeParams._deserialize(params.get("MixTranscodeParams"))
        if params.get("MixLayoutParams") is not None:
            self.MixLayoutParams = MixLayoutParams()
            self.MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        self.ResourceExpiredHour = params.get("ResourceExpiredHour")
        self.PrivateMapKey = params.get("PrivateMapKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingResponse(AbstractModel):
    """CreateCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。任务 ID需要业务保存下来，作为下次针对这个录制任务操作的参数。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreatePictureRequest(AbstractModel):
    """CreatePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用id
        :type SdkAppId: int
        :param Content: 图片内容经base64编码后的string格式
        :type Content: str
        :param Suffix: 图片后缀名
        :type Suffix: str
        :param Height: 图片长度
        :type Height: int
        :param Width: 图片宽度
        :type Width: int
        :param XPosition: 显示位置x轴方向
        :type XPosition: int
        :param YPosition: 显示位置y轴方向
        :type YPosition: int
        """
        self.SdkAppId = None
        self.Content = None
        self.Suffix = None
        self.Height = None
        self.Width = None
        self.XPosition = None
        self.YPosition = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Content = params.get("Content")
        self.Suffix = params.get("Suffix")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePictureResponse(AbstractModel):
    """CreatePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param PictureId: 图片id
        :type PictureId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PictureId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PictureId = params.get("PictureId")
        self.RequestId = params.get("RequestId")


class DeleteCloudRecordingRequest(AbstractModel):
    """DeleteCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param TaskId: 录制任务的唯一Id，在启动录制成功后会返回。
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRecordingResponse(AbstractModel):
    """DeleteCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeletePictureRequest(AbstractModel):
    """DeletePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param PictureId: 图片id
        :type PictureId: int
        :param SdkAppId: 应用id
        :type SdkAppId: int
        """
        self.PictureId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.PictureId = params.get("PictureId")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePictureResponse(AbstractModel):
    """DeletePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCallDetailInfoRequest(AbstractModel):
    """DescribeCallDetailInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CommId: 通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :type CommId: str
        :param StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777），
注意：支持查询14天内的数据。
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：DataType 不为null ，与StartTime间隔时间不超过1小时；DataType 为null，与StartTime间隔时间不超过4小时。
        :type EndTime: int
        :param SdkAppId: 用户SdkAppId（如：1400xxxxxx）。
        :type SdkAppId: int
        :param UserIds: 需查询的用户数组，默认不填返回6个用户。
        :type UserIds: list of str
        :param DataType: 需查询的指标，不填则只返回用户列表，填all则返回所有指标。
appCpu：APP CPU使用率；
sysCpu：系统 CPU使用率；
aBit：上/下行音频码率；单位：bps
aBlock：音频卡顿时长；单位：ms
bigvBit：上/下行视频码率；单位：bps
bigvCapFps：视频采集帧率；
bigvEncFps：视频发送帧率；
bigvDecFps：渲染帧率；
bigvBlock：视频卡顿时长；单位：ms
aLoss：上/下行音频丢包率；
bigvLoss：上/下行视频丢包率；
bigvWidth：上/下行分辨率宽；
bigvHeight：上/下行分辨率高
        :type DataType: list of str
        :param PageNumber: 当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回6条数据。
        :type PageNumber: int
        :param PageSize: 每页个数，默认为6，
范围：[1，100]
注意：DataType不为null，UserIds长度不能超过6，PageSize最大值不超过6；
DataType 为null，UserIds长度不超过100，PageSize最大不超过100。
        :type PageSize: int
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.DataType = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.DataType = params.get("DataType")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallDetailInfoResponse(AbstractModel):
    """DescribeCallDetailInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回的用户总条数
        :type Total: int
        :param UserList: 用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param Data: 质量数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of QualityData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudRecordingRequest(AbstractModel):
    """DescribeCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param TaskId: 录制任务的唯一Id，在启动录制成功后会返回。
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRecordingResponse(AbstractModel):
    """DescribeCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 录制任务的唯一Id。
        :type TaskId: str
        :param Status: 云端录制任务的状态信息。
Idle：表示当前录制任务空闲中
InProgress：表示当前录制任务正在进行中。
Exited：表示当前录制任务正在退出的过程中。
        :type Status: str
        :param StorageFileList: 录制文件信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageFileList: list of StorageFile
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Status = None
        self.StorageFileList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        if params.get("StorageFileList") is not None:
            self.StorageFileList = []
            for item in params.get("StorageFileList"):
                obj = StorageFile()
                obj._deserialize(item)
                self.StorageFileList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExternalTrtcMeasureRequest(AbstractModel):
    """DescribeExternalTrtcMeasure请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询开始日期。
        :type StartTime: str
        :param EndTime: 查询结束日期。
        :type EndTime: str
        :param SdkAppId: 对应的应用。如果没有这个参数，表示获取用户名下全部实时音视频应用的汇总。
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalTrtcMeasureResponse(AbstractModel):
    """DescribeExternalTrtcMeasure返回参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppIdTrtrTimeUsages: 每个SdkAppId的时长使用信息
        :type SdkAppIdTrtrTimeUsages: list of SdkAppIdNewTrtcTimeUsage
        :param AnchorUsageMode: 主播的用量统计方式。取值"InRoomTime":房间时长,"SubscribeTime":"订阅时长","Bandwidth":带宽
        :type AnchorUsageMode: str
        :param AudienceUsageMode: 观众的用量统计方式。取值"InRoomTime":在房间时长,"SubscribeTime":"订阅时长","Bandwidth":带宽,"MergeWithAnchor":"不区分麦上麦下"
        :type AudienceUsageMode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SdkAppIdTrtrTimeUsages = None
        self.AnchorUsageMode = None
        self.AudienceUsageMode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SdkAppIdTrtrTimeUsages") is not None:
            self.SdkAppIdTrtrTimeUsages = []
            for item in params.get("SdkAppIdTrtrTimeUsages"):
                obj = SdkAppIdNewTrtcTimeUsage()
                obj._deserialize(item)
                self.SdkAppIdTrtrTimeUsages.append(obj)
        self.AnchorUsageMode = params.get("AnchorUsageMode")
        self.AudienceUsageMode = params.get("AudienceUsageMode")
        self.RequestId = params.get("RequestId")


class DescribePictureRequest(AbstractModel):
    """DescribePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param PictureId: 图片ID，不填时返回该应用下所有图片
        :type PictureId: int
        :param PageSize: 每页数量，不填时默认为10
        :type PageSize: int
        :param PageNo: 页码，不填时默认为1
        :type PageNo: int
        """
        self.SdkAppId = None
        self.PictureId = None
        self.PageSize = None
        self.PageNo = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.PictureId = params.get("PictureId")
        self.PageSize = params.get("PageSize")
        self.PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePictureResponse(AbstractModel):
    """DescribePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回的图片记录数
        :type Total: int
        :param PictureInfo: 图片信息列表
        :type PictureInfo: list of PictureInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.PictureInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("PictureInfo") is not None:
            self.PictureInfo = []
            for item in params.get("PictureInfo"):
                obj = PictureInfo()
                obj._deserialize(item)
                self.PictureInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRecordStatisticRequest(AbstractModel):
    """DescribeRecordStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询开始日期，格式为YYYY-MM-DD。
        :type StartTime: str
        :param EndTime: 查询结束日期，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param SdkAppId: 应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStatisticResponse(AbstractModel):
    """DescribeRecordStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppIdUsages: 应用的用量信息数组。
        :type SdkAppIdUsages: list of SdkAppIdRecordUsage
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SdkAppIdUsages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SdkAppIdUsages") is not None:
            self.SdkAppIdUsages = []
            for item in params.get("SdkAppIdUsages"):
                obj = SdkAppIdRecordUsage()
                obj._deserialize(item)
                self.SdkAppIdUsages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoomInfoRequest(AbstractModel):
    """DescribeRoomInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：与StartTime间隔时间不超过24小时。
        :type EndTime: int
        :param RoomId: 房间号（如：223)
        :type RoomId: str
        :param PageNumber: 当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回10条数据。
        :type PageNumber: int
        :param PageSize: 每页个数，默认为10，
范围：[1，100]
        :type PageSize: int
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomInfoResponse(AbstractModel):
    """DescribeRoomInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回当页数据总数
        :type Total: int
        :param RoomList: 房间信息列表
        :type RoomList: list of RoomState
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.RoomList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RoomList") is not None:
            self.RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self.RoomList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScaleInfoRequest(AbstractModel):
    """DescribeScaleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据。
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877），建议与StartTime间隔时间超过24小时。
注意：按天统计，结束时间小于前一天，否则查询数据为空（如：需查询20号数据，结束时间需小于20号0点）。
        :type EndTime: int
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScaleInfoResponse(AbstractModel):
    """DescribeScaleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回的数据条数
        :type Total: int
        :param ScaleList: 返回的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleList: list of ScaleInfomation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ScaleList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ScaleList") is not None:
            self.ScaleList = []
            for item in params.get("ScaleList"):
                obj = ScaleInfomation()
                obj._deserialize(item)
                self.ScaleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrtcMcuTranscodeTimeRequest(AbstractModel):
    """DescribeTrtcMcuTranscodeTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param SdkAppId: 应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :type SdkAppId: int
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcMcuTranscodeTimeResponse(AbstractModel):
    """DescribeTrtcMcuTranscodeTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param Usages: 应用的用量信息数组。
        :type Usages: list of OneSdkAppIdTranscodeTimeUsagesInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Usages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = OneSdkAppIdTranscodeTimeUsagesInfo()
                obj._deserialize(item)
                self.Usages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUnusualEventRequest(AbstractModel):
    """DescribeUnusualEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）注意：与StartTime间隔时间不超过1小时。
        :type EndTime: int
        :param RoomId: 房间号，查询房间内任意20条以内异常体验事件
        :type RoomId: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnusualEventResponse(AbstractModel):
    """DescribeUnusualEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回的数据总条数
范围：[0，20]
        :type Total: int
        :param AbnormalExperienceList: 异常体验列表
        :type AbnormalExperienceList: list of AbnormalExperience
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.AbnormalExperienceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AbnormalExperienceList") is not None:
            self.AbnormalExperienceList = []
            for item in params.get("AbnormalExperienceList"):
                obj = AbnormalExperience()
                obj._deserialize(item)
                self.AbnormalExperienceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserEventRequest(AbstractModel):
    """DescribeUserEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param CommId: 通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :type CommId: str
        :param StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：查询时间大于房间结束时间，以房间结束时间为准。
        :type EndTime: int
        :param UserId: 用户UserId
        :type UserId: str
        :param RoomId: 房间号（如：223）
        :type RoomId: str
        :param SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.UserId = None
        self.RoomId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.UserId = params.get("UserId")
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserEventResponse(AbstractModel):
    """DescribeUserEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回的事件列表，若没有数据，会返回空数组。
        :type Data: list of EventList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = EventList()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CommId: 通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :type CommId: str
        :param StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :type StartTime: int
        :param EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：与StartTime间隔时间不超过4小时。
        :type EndTime: int
        :param SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param UserIds: 需查询的用户数组，不填默认返回6个用户
范围：[1，100]。
        :type UserIds: list of str
        :param PageNumber: 当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回6条数据。
        :type PageNumber: int
        :param PageSize: 每页个数，默认为6，
范围：[1，100]。
        :type PageSize: int
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 返回的用户总条数
        :type Total: int
        :param UserList: 用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        self.RequestId = params.get("RequestId")


class DismissRoomByStrRoomIdRequest(AbstractModel):
    """DismissRoomByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: str
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomByStrRoomIdResponse(AbstractModel):
    """DismissRoomByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    """DismissRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncodeParams(AbstractModel):
    """MCU混流输出流编码参数

    """

    def __init__(self):
        r"""
        :param AudioSampleRate: 混流-输出流音频采样率。取值为[48000, 44100, 32000, 24000, 16000, 8000]，单位是Hz。
        :type AudioSampleRate: int
        :param AudioBitrate: 混流-输出流音频码率。取值范围[8,500]，单位为kbps。
        :type AudioBitrate: int
        :param AudioChannels: 混流-输出流音频声道数，取值范围[1,2]，1表示混流输出音频为单声道，2表示混流输出音频为双声道。
        :type AudioChannels: int
        :param VideoWidth: 混流-输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :type VideoWidth: int
        :param VideoHeight: 混流-输出流高，音视频输出时必填。取值范围[0,1080]，单位为像素值。
        :type VideoHeight: int
        :param VideoBitrate: 混流-输出流码率，音视频输出时必填。取值范围[1,10000]，单位为kbps。
        :type VideoBitrate: int
        :param VideoFramerate: 混流-输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :type VideoFramerate: int
        :param VideoGop: 混流-输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :type VideoGop: int
        :param BackgroundColor: 混流-输出流背景色，取值是十进制整数。常用的颜色有：
红色：0xff0000，对应的十进制整数是16724736。
黄色：0xffff00。对应的十进制整数是16776960。
绿色：0x33cc00。对应的十进制整数是3394560。
蓝色：0x0066ff。对应的十进制整数是26367。
黑色：0x000000。对应的十进制整数是0。
白色：0xFFFFFF。对应的十进制整数是16777215。
灰色：0x999999。对应的十进制整数是10066329。
        :type BackgroundColor: int
        :param BackgroundImageId: 混流-输出流背景图片，取值为实时音视频控制台上传的图片ID。
        :type BackgroundImageId: int
        :param AudioCodec: 混流-输出流音频编码类型，取值范围[0,1, 2]，0为LC-AAC，1为HE-AAC，2为HE-AACv2。默认值为0。当音频编码设置为HE-AACv2时，只支持输出流音频声道数为双声道。HE-AAC和HE-AACv2支持的输出流音频采样率范围为[48000, 44100, 32000, 24000, 16000]
        :type AudioCodec: int
        :param BackgroundImageUrl: 混流-输出流背景图片URL地址，支持png、jpg、jpeg、bmp格式，暂不支持透明通道。URL链接长度限制为512字节。BackgroundImageUrl和BackgroundImageId参数都填时，以BackgroundImageUrl为准。图片大小限制不超过2MB。
        :type BackgroundImageUrl: str
        """
        self.AudioSampleRate = None
        self.AudioBitrate = None
        self.AudioChannels = None
        self.VideoWidth = None
        self.VideoHeight = None
        self.VideoBitrate = None
        self.VideoFramerate = None
        self.VideoGop = None
        self.BackgroundColor = None
        self.BackgroundImageId = None
        self.AudioCodec = None
        self.BackgroundImageUrl = None


    def _deserialize(self, params):
        self.AudioSampleRate = params.get("AudioSampleRate")
        self.AudioBitrate = params.get("AudioBitrate")
        self.AudioChannels = params.get("AudioChannels")
        self.VideoWidth = params.get("VideoWidth")
        self.VideoHeight = params.get("VideoHeight")
        self.VideoBitrate = params.get("VideoBitrate")
        self.VideoFramerate = params.get("VideoFramerate")
        self.VideoGop = params.get("VideoGop")
        self.BackgroundColor = params.get("BackgroundColor")
        self.BackgroundImageId = params.get("BackgroundImageId")
        self.AudioCodec = params.get("AudioCodec")
        self.BackgroundImageUrl = params.get("BackgroundImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventList(AbstractModel):
    """sdk或webrtc的事件列表。

    """

    def __init__(self):
        r"""
        :param Content: 数据内容
        :type Content: list of EventMessage
        :param PeerId: 发送端的userId
        :type PeerId: str
        """
        self.Content = None
        self.PeerId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = EventMessage()
                obj._deserialize(item)
                self.Content.append(obj)
        self.PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventMessage(AbstractModel):
    """事件信息，包括，事件时间戳，事件ID,

    """

    def __init__(self):
        r"""
        :param Type: 视频流类型：
0：与视频无关的事件；
2：视频为大画面；
3：视频为小画面；
7：视频为旁路画面；
        :type Type: int
        :param Time: 事件上报的时间戳，unix时间（1589891188801ms)
        :type Time: int
        :param EventId: 事件Id：分为sdk的事件和webrtc的事件，详情见：附录/事件 ID 映射表：https://cloud.tencent.com/document/product/647/44916
        :type EventId: int
        :param ParamOne: 事件的第一个参数，如视频分辨率宽
        :type ParamOne: int
        :param ParamTwo: 事件的第二个参数，如视频分辨率高
        :type ParamTwo: int
        """
        self.Type = None
        self.Time = None
        self.EventId = None
        self.ParamOne = None
        self.ParamTwo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Time = params.get("Time")
        self.EventId = params.get("EventId")
        self.ParamOne = params.get("ParamOne")
        self.ParamTwo = params.get("ParamTwo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayoutParams(AbstractModel):
    """MCU混流布局参数

    """

    def __init__(self):
        r"""
        :param Template: 混流布局模板ID，0为悬浮模板(默认);1为九宫格模板;2为屏幕分享模板;3为画中画模板;4为自定义模板。
        :type Template: int
        :param MainVideoUserId: 屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的用户ID。
        :type MainVideoUserId: str
        :param MainVideoStreamType: 屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的流类型，0为摄像头，1为屏幕分享。左侧大画面为web用户时此值填0。
        :type MainVideoStreamType: int
        :param SmallVideoLayoutParams: 画中画模板中有效，代表小画面的布局参数。
        :type SmallVideoLayoutParams: :class:`tencentcloud.trtc.v20190722.models.SmallVideoLayoutParams`
        :param MainVideoRightAlign: 屏幕分享模板有效。设置为1时代表大画面居右，小画面居左布局。默认为0。
        :type MainVideoRightAlign: int
        :param MixVideoUids: 悬浮模板、九宫格、屏幕分享模板有效。设置此参数后，输出流混合此参数中包含用户的音视频，以及其他用户的纯音频。最多可设置16个用户。
        :type MixVideoUids: list of str
        :param PresetLayoutConfig: 自定义模板中有效，指定用户视频在混合画面中的位置。
        :type PresetLayoutConfig: list of PresetLayoutConfig
        :param PlaceHolderMode: 自定义模板中有效，设置为1时代表启用占位图功能，0时代表不启用占位图功能，默认为0。启用占位图功能时，在预设位置的用户没有上行视频时可显示对应的占位图。
        :type PlaceHolderMode: int
        :param PureAudioHoldPlaceMode: 悬浮模板、九宫格、屏幕分享模板生效，用于控制纯音频上行是否占用画面布局位置。设置为0是代表后台默认处理方式，悬浮小画面占布局位置，九宫格画面占布局位置、屏幕分享小画面不占布局位置；设置为1时代表纯音频上行占布局位置；设置为2时代表纯音频上行不占布局位置。默认为0。
        :type PureAudioHoldPlaceMode: int
        :param WaterMarkParams: 水印参数。
        :type WaterMarkParams: :class:`tencentcloud.trtc.v20190722.models.WaterMarkParams`
        """
        self.Template = None
        self.MainVideoUserId = None
        self.MainVideoStreamType = None
        self.SmallVideoLayoutParams = None
        self.MainVideoRightAlign = None
        self.MixVideoUids = None
        self.PresetLayoutConfig = None
        self.PlaceHolderMode = None
        self.PureAudioHoldPlaceMode = None
        self.WaterMarkParams = None


    def _deserialize(self, params):
        self.Template = params.get("Template")
        self.MainVideoUserId = params.get("MainVideoUserId")
        self.MainVideoStreamType = params.get("MainVideoStreamType")
        if params.get("SmallVideoLayoutParams") is not None:
            self.SmallVideoLayoutParams = SmallVideoLayoutParams()
            self.SmallVideoLayoutParams._deserialize(params.get("SmallVideoLayoutParams"))
        self.MainVideoRightAlign = params.get("MainVideoRightAlign")
        self.MixVideoUids = params.get("MixVideoUids")
        if params.get("PresetLayoutConfig") is not None:
            self.PresetLayoutConfig = []
            for item in params.get("PresetLayoutConfig"):
                obj = PresetLayoutConfig()
                obj._deserialize(item)
                self.PresetLayoutConfig.append(obj)
        self.PlaceHolderMode = params.get("PlaceHolderMode")
        self.PureAudioHoldPlaceMode = params.get("PureAudioHoldPlaceMode")
        if params.get("WaterMarkParams") is not None:
            self.WaterMarkParams = WaterMarkParams()
            self.WaterMarkParams._deserialize(params.get("WaterMarkParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayout(AbstractModel):
    """用户自定义混流布局参数列表。

    """

    def __init__(self):
        r"""
        :param Top: 画布上该画面左上角的 y 轴坐标，取值范围 [0, 1920]，不能超过画布的高。
        :type Top: int
        :param Left: 画布上该画面左上角的 x 轴坐标，取值范围 [0, 1920]，不能超过画布的宽。
        :type Left: int
        :param Width: 画布上该画面宽度的相对值，取值范围 [0, 1920]，与Left相加不应超过画布的宽。
        :type Width: int
        :param Height: 画布上该画面高度的相对值，取值范围 [0, 1920]，与Top相加不应超过画布的高。
        :type Height: int
        :param UserId: 字符串内容为待显示在该画面的主播对应的UserId，如果不指定，会按照主播加入房间的顺序匹配。
        :type UserId: str
        :param Alpha: 画布的透明度值，取值范围[0, 255]。0表示不透明，255表示全透明。默认值为0。
        :type Alpha: int
        :param RenderMode: 0 ：拉伸模式，这个模式下整个视频内容会全部显示，并填满子画面，在源视频和目的视频宽高比不一致的时候，画面不会缺少内容，但是画面可能产生形变；

1 ：剪裁模式（默认），这个模式下会严格按照目的视频的宽高比对源视频剪裁之后再拉伸，并填满子画面画布，在源视频和目的视频宽高比不一致的时候，画面保持不变形，但是会被剪裁；

2 ：填黑模式，这个模式下会严格保持源视频的宽高比进行等比缩放，在源视频和目的视频宽高比不一致的时候，画面的上下侧边缘或者左右侧边缘会露出子画面画布的背景；

3 ：智能拉伸模式，这个模式类似剪裁模式，区别是在源视频和目的视频宽高比不一致的时候，限制了最大剪裁比例为画面的宽度或者高度的20%；
        :type RenderMode: int
        :param MediaId: 对应订阅流的主辅路标识：
0：主流（默认）；
1：辅流；
        :type MediaId: int
        :param ImageLayer: 该画布的图层顺序, 这个值越小表示图层越靠后。默认值为0。
        :type ImageLayer: int
        :param SubBackgroundImage: 下载的url地址， 只支持jpg， png，大小限制不超过5M，宽高比不一致的处理方案同 RenderMode。
        :type SubBackgroundImage: str
        """
        self.Top = None
        self.Left = None
        self.Width = None
        self.Height = None
        self.UserId = None
        self.Alpha = None
        self.RenderMode = None
        self.MediaId = None
        self.ImageLayer = None
        self.SubBackgroundImage = None


    def _deserialize(self, params):
        self.Top = params.get("Top")
        self.Left = params.get("Left")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.UserId = params.get("UserId")
        self.Alpha = params.get("Alpha")
        self.RenderMode = params.get("RenderMode")
        self.MediaId = params.get("MediaId")
        self.ImageLayer = params.get("ImageLayer")
        self.SubBackgroundImage = params.get("SubBackgroundImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayoutParams(AbstractModel):
    """录制的混流布局参数。

    """

    def __init__(self):
        r"""
        :param MixLayoutMode: 布局模式:
1：悬浮布局；
2：屏幕分享布局；
3：九宫格布局（默认）；
4：自定义布局；

悬浮布局：默认第一个进入房间的主播（也可以指定一个主播）的视频画面会铺满整个屏幕。其他主播的视频画面从左下角开始依次按照进房顺序水平排列，显示为小画面，小画面悬浮于大画面之上。当画面数量小于等于17个时，每行4个（4 x 4排列）。当画面数量大于17个时，重新布局小画面为每行5个（5 x 5）排列。最多支持25个画面，如果用户只发送音频，仍然会占用画面位置。

屏幕分享布局：指定一个主播在屏幕左侧的大画面位置（如果不指定，那么大画面位置为背景色），其他主播自上而下依次垂直排列于右侧。当画面数量少于17个的时候，右侧每列最多8人，最多占据两列。当画面数量多于17个的时候，超过17个画面的主播从左下角开始依次水平排列。最多支持25个画面，如果主播只发送音频，仍然会占用画面位置。

九宫格布局：根据主播的数量自动调整每个画面的大小，每个主播的画面大小一致，最多支持25个画面。

自定义布局：根据需要在MixLayoutList内定制每个主播画面的布局。
        :type MixLayoutMode: int
        :param MixLayoutList: 如果MixLayoutMode 选择为4自定义布局模式的话，设置此参数为每个主播所对应的布局画面的详细信息，最大不超过25个。
        :type MixLayoutList: list of MixLayout
        :param BackGroundColor: 录制背景颜色，RGB的颜色表的16进制表示，每个颜色通过8bit长度标识，默认为黑色。比如橙色对应的RGB为 R:255 G:165 B:0, 那么对应的字符串描述为#FFA500，格式规范：‘#‘开头，后面跟固定RGB的颜色值
        :type BackGroundColor: str
        :param MaxResolutionUserId: 在布局模式为1：悬浮布局和 2：屏幕分享布局时，设定为显示大视频画面的UserId。不填的话：悬浮布局默认是第一个进房间的主播，屏幕分享布局默认是背景色
        :type MaxResolutionUserId: str
        :param MediaId: 主辅路标识，
0：主流（默认）；
1：辅流（屏幕分享）；
这个位置的MediaId代表的是对应MaxResolutionUserId的主辅路，MixLayoutList内代表的是自定义用户的主辅路。
        :type MediaId: int
        :param BackgroundImageUrl: 下载的url地址， 只支持jpg， png，大小限制不超过5M。
        :type BackgroundImageUrl: str
        :param PlaceHolderMode: 设置为1时代表启用占位图功能，0时代表不启用占位图功能，默认为0。启用占位图功能时，在预设位置的用户没有上行视频时可显示对应的占位图。
        :type PlaceHolderMode: int
        :param BackgroundImageRenderMode: 背景画面宽高比不一致的时候处理方案，与MixLayoufList定义的RenderMode一致。
        :type BackgroundImageRenderMode: int
        :param DefaultSubBackgroundImage: 下载的url地址， 只支持jpg， png，大小限制不超过5M，宽高比不一致的处理方案同 RenderMode。
        :type DefaultSubBackgroundImage: str
        :param WaterMarkList: 水印布局参数， 最多支持25个。
        :type WaterMarkList: list of WaterMark
        """
        self.MixLayoutMode = None
        self.MixLayoutList = None
        self.BackGroundColor = None
        self.MaxResolutionUserId = None
        self.MediaId = None
        self.BackgroundImageUrl = None
        self.PlaceHolderMode = None
        self.BackgroundImageRenderMode = None
        self.DefaultSubBackgroundImage = None
        self.WaterMarkList = None


    def _deserialize(self, params):
        self.MixLayoutMode = params.get("MixLayoutMode")
        if params.get("MixLayoutList") is not None:
            self.MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = MixLayout()
                obj._deserialize(item)
                self.MixLayoutList.append(obj)
        self.BackGroundColor = params.get("BackGroundColor")
        self.MaxResolutionUserId = params.get("MaxResolutionUserId")
        self.MediaId = params.get("MediaId")
        self.BackgroundImageUrl = params.get("BackgroundImageUrl")
        self.PlaceHolderMode = params.get("PlaceHolderMode")
        self.BackgroundImageRenderMode = params.get("BackgroundImageRenderMode")
        self.DefaultSubBackgroundImage = params.get("DefaultSubBackgroundImage")
        if params.get("WaterMarkList") is not None:
            self.WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = WaterMark()
                obj._deserialize(item)
                self.WaterMarkList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixTranscodeParams(AbstractModel):
    """录制的音视频转码参数。

    """

    def __init__(self):
        r"""
        :param VideoParams: 录制视频转码参数，注意如果设置了这个参数，那么里面的字段都是必填的，没有默认值，如果不填这个参数，那么取值为默认值。
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        :param AudioParams: 录制音频转码参数，注意如果设置了这个参数，那么里面的字段都是必填的，没有默认值，如果不填这个参数，那么取值为默认值。
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        self.VideoParams = None
        self.AudioParams = None


    def _deserialize(self, params):
        if params.get("VideoParams") is not None:
            self.VideoParams = VideoParams()
            self.VideoParams._deserialize(params.get("VideoParams"))
        if params.get("AudioParams") is not None:
            self.AudioParams = AudioParams()
            self.AudioParams._deserialize(params.get("AudioParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingRequest(AbstractModel):
    """ModifyCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param TaskId: 录制任务的唯一Id，在启动录制成功后会返回。
        :type TaskId: str
        :param MixLayoutParams: 需要更新的混流的布局参数。
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self.SdkAppId = None
        self.TaskId = None
        self.MixLayoutParams = None
        self.SubscribeStreamUserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        if params.get("MixLayoutParams") is not None:
            self.MixLayoutParams = MixLayoutParams()
            self.MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        if params.get("SubscribeStreamUserIds") is not None:
            self.SubscribeStreamUserIds = SubscribeStreamUserIds()
            self.SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingResponse(AbstractModel):
    """ModifyCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyPictureRequest(AbstractModel):
    """ModifyPicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param PictureId: 图片id
        :type PictureId: int
        :param SdkAppId: 应用id
        :type SdkAppId: int
        :param Height: 图片长度
        :type Height: int
        :param Width: 图片宽度
        :type Width: int
        :param XPosition: 显示位置x轴方向
        :type XPosition: int
        :param YPosition: 显示位置y轴方向
        :type YPosition: int
        """
        self.PictureId = None
        self.SdkAppId = None
        self.Height = None
        self.Width = None
        self.XPosition = None
        self.YPosition = None


    def _deserialize(self, params):
        self.PictureId = params.get("PictureId")
        self.SdkAppId = params.get("SdkAppId")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPictureResponse(AbstractModel):
    """ModifyPicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OneSdkAppIdTranscodeTimeUsagesInfo(AbstractModel):
    """旁路转码时长的查询结果

    """

    def __init__(self):
        r"""
        :param SdkAppIdTranscodeTimeUsages: 旁路转码时长查询结果数组
        :type SdkAppIdTranscodeTimeUsages: list of SdkAppIdTrtcMcuTranscodeTimeUsage
        :param TotalNum: 查询记录数量
        :type TotalNum: int
        :param SdkAppId: 所查询的应用ID，可能值为:1-应用的应用ID，2-total，显示为total则表示查询的是所有应用的用量合计值。
        :type SdkAppId: str
        """
        self.SdkAppIdTranscodeTimeUsages = None
        self.TotalNum = None
        self.SdkAppId = None


    def _deserialize(self, params):
        if params.get("SdkAppIdTranscodeTimeUsages") is not None:
            self.SdkAppIdTranscodeTimeUsages = []
            for item in params.get("SdkAppIdTranscodeTimeUsages"):
                obj = SdkAppIdTrtcMcuTranscodeTimeUsage()
                obj._deserialize(item)
                self.SdkAppIdTranscodeTimeUsages.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputParams(AbstractModel):
    """MCU混流的输出参数

    """

    def __init__(self):
        r"""
        :param StreamId: 直播流 ID，由用户自定义设置，该流 ID 不能与用户旁路的流 ID 相同。
        :type StreamId: str
        :param PureAudioStream: 取值范围[0,1]， 填0：直播流为音视频(默认); 填1：直播流为纯音频
        :type PureAudioStream: int
        :param RecordId: 自定义录制文件名称前缀。请先在实时音视频控制台开通录制功能，https://cloud.tencent.com/document/product/647/50768
        :type RecordId: str
        :param RecordAudioOnly: 取值范围[0,1]，填0无实际含义; 填1：指定录制文件格式为mp3。此参数不建议使用，建议在实时音视频控制台配置纯音频录制模板。
        :type RecordAudioOnly: int
        """
        self.StreamId = None
        self.PureAudioStream = None
        self.RecordId = None
        self.RecordAudioOnly = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.PureAudioStream = params.get("PureAudioStream")
        self.RecordId = params.get("RecordId")
        self.RecordAudioOnly = params.get("RecordAudioOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PictureInfo(AbstractModel):
    """图片列表信息

    """

    def __init__(self):
        r"""
        :param Height: 图片长度
        :type Height: int
        :param Width: 图片宽度
        :type Width: int
        :param XPosition: 显示位置x轴方向
        :type XPosition: int
        :param YPosition: 显示位置y轴方向
        :type YPosition: int
        :param SdkAppId: 应用id
        :type SdkAppId: int
        :param PictureId: 图片id
        :type PictureId: int
        """
        self.Height = None
        self.Width = None
        self.XPosition = None
        self.YPosition = None
        self.SdkAppId = None
        self.PictureId = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.SdkAppId = params.get("SdkAppId")
        self.PictureId = params.get("PictureId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PresetLayoutConfig(AbstractModel):
    """自定义模板中有效，指定用户视频在混合画面中的位置。

    """

    def __init__(self):
        r"""
        :param UserId: 指定显示在该画面上的用户ID。如果不指定用户ID，会按照用户加入房间的顺序自动匹配PresetLayoutConfig中的画面设置。
        :type UserId: str
        :param StreamType: 当该画面指定用户时，代表用户的流类型。0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :type StreamType: int
        :param ImageWidth: 该画面在输出时的宽度，单位为像素值，不填默认为0。
        :type ImageWidth: int
        :param ImageHeight: 该画面在输出时的高度，单位为像素值，不填默认为0。
        :type ImageHeight: int
        :param LocationX: 该画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :type LocationX: int
        :param LocationY: 该画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :type LocationY: int
        :param ZOrder: 该画面在输出时的层级，不填默认为0。
        :type ZOrder: int
        :param RenderMode: 该画面在输出时的显示模式：0为裁剪，1为缩放，2为缩放并显示黑底。不填默认为0。
        :type RenderMode: int
        :param MixInputType: 该当前位置用户混入的流类型：0为混入音视频，1为只混入视频，2为只混入音频。默认为0，建议配合指定用户ID使用。
        :type MixInputType: int
        :param PlaceImageId: 占位图ID。启用占位图功能时，在当前位置的用户没有上行视频时显示占位图。占位图大小不能超过2M，在实时音视频控制台上传并生成，https://cloud.tencent.com/document/product/647/50769
        :type PlaceImageId: int
        """
        self.UserId = None
        self.StreamType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.ZOrder = None
        self.RenderMode = None
        self.MixInputType = None
        self.PlaceImageId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StreamType = params.get("StreamType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.ZOrder = params.get("ZOrder")
        self.RenderMode = params.get("RenderMode")
        self.MixInputType = params.get("MixInputType")
        self.PlaceImageId = params.get("PlaceImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCdnParams(AbstractModel):
    """第三方CDN转推参数

    """

    def __init__(self):
        r"""
        :param BizId: 腾讯云直播BizId。
        :type BizId: int
        :param PublishCdnUrls: 第三方CDN转推的目的地址，同时只支持转推一个第三方CDN地址。
        :type PublishCdnUrls: list of str
        """
        self.BizId = None
        self.PublishCdnUrls = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.PublishCdnUrls = params.get("PublishCdnUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityData(AbstractModel):
    """Es返回的质量数据

    """

    def __init__(self):
        r"""
        :param Content: 数据内容
        :type Content: list of TimeValue
        :param UserId: 用户ID
        :type UserId: str
        :param PeerId: 对端Id,为空时表示上行数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PeerId: str
        :param DataType: 数据类型
        :type DataType: str
        """
        self.Content = None
        self.UserId = None
        self.PeerId = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.UserId = params.get("UserId")
        self.PeerId = params.get("PeerId")
        self.DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordParams(AbstractModel):
    """云端录制控制参数。

    """

    def __init__(self):
        r"""
        :param RecordMode: 录制模式：
1：单流录制，分别录制房间的订阅UserId的音频和视频，将录制文件上传至云存储；
2：混流录制，将房间内订阅UserId的音视频混录成一个音视频文件，将录制文件上传至云存储；
        :type RecordMode: int
        :param MaxIdleTime: 房间内持续没有主播的状态超过MaxIdleTime的时长，自动停止录制，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
        :type MaxIdleTime: int
        :param StreamType: 录制的媒体流类型：
0：录制音频+视频流（默认）;
1：仅录制音频流；
2：仅录制视频流，
        :type StreamType: int
        :param SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        :param OutputFormat: 输出文件的格式，上传到云点播时此参数无效。0：(默认)输出文件为hls格式。1：输出文件格式为hls+mp4（hls录制完成后转mp4文件）
        :type OutputFormat: int
        """
        self.RecordMode = None
        self.MaxIdleTime = None
        self.StreamType = None
        self.SubscribeStreamUserIds = None
        self.OutputFormat = None


    def _deserialize(self, params):
        self.RecordMode = params.get("RecordMode")
        self.MaxIdleTime = params.get("MaxIdleTime")
        self.StreamType = params.get("StreamType")
        if params.get("SubscribeStreamUserIds") is not None:
            self.SubscribeStreamUserIds = SubscribeStreamUserIds()
            self.SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self.OutputFormat = params.get("OutputFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordUsage(AbstractModel):
    """录制的使用信息。

    """

    def __init__(self):
        r"""
        :param TimeKey: 本组数据对应的时间点，格式如:2020-09-07或2020-09-07 00:05:05。
        :type TimeKey: str
        :param Class1VideoTime: 视频时长-标清SD，单位：秒。
        :type Class1VideoTime: int
        :param Class2VideoTime: 视频时长-高清HD，单位：秒。
        :type Class2VideoTime: int
        :param Class3VideoTime: 视频时长-超清HD，单位：秒。
        :type Class3VideoTime: int
        :param AudioTime: 语音时长，单位：秒。
        :type AudioTime: int
        """
        self.TimeKey = None
        self.Class1VideoTime = None
        self.Class2VideoTime = None
        self.Class3VideoTime = None
        self.AudioTime = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.Class1VideoTime = params.get("Class1VideoTime")
        self.Class2VideoTime = params.get("Class2VideoTime")
        self.Class3VideoTime = params.get("Class3VideoTime")
        self.AudioTime = params.get("AudioTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdRequest(AbstractModel):
    """RemoveUserByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: str
        :param UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdResponse(AbstractModel):
    """RemoveUserByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserRequest(AbstractModel):
    """RemoveUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        :param UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserResponse(AbstractModel):
    """RemoveUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoomState(AbstractModel):
    """房间信息列表

    """

    def __init__(self):
        r"""
        :param CommId: 通话ID（唯一标识一次通话）
        :type CommId: str
        :param RoomString: 房间号
        :type RoomString: str
        :param CreateTime: 房间创建时间
        :type CreateTime: int
        :param DestroyTime: 房间销毁时间
        :type DestroyTime: int
        :param IsFinished: 房间是否已经结束
        :type IsFinished: bool
        :param UserId: 房间创建者Id
        :type UserId: str
        """
        self.CommId = None
        self.RoomString = None
        self.CreateTime = None
        self.DestroyTime = None
        self.IsFinished = None
        self.UserId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.RoomString = params.get("RoomString")
        self.CreateTime = params.get("CreateTime")
        self.DestroyTime = params.get("DestroyTime")
        self.IsFinished = params.get("IsFinished")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInfomation(AbstractModel):
    """历史规模信息

    """

    def __init__(self):
        r"""
        :param Time: 每天开始的时间
        :type Time: int
        :param UserNumber: 房间人数，用户重复进入同一个房间为1次
注意：此字段可能返回 null，表示取不到有效值。
        :type UserNumber: int
        :param UserCount: 房间人次，用户每次进入房间为一次
注意：此字段可能返回 null，表示取不到有效值。
        :type UserCount: int
        :param RoomNumbers: sdkappid下一天内的房间数
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomNumbers: int
        """
        self.Time = None
        self.UserNumber = None
        self.UserCount = None
        self.RoomNumbers = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.UserNumber = params.get("UserNumber")
        self.UserCount = params.get("UserCount")
        self.RoomNumbers = params.get("RoomNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdNewTrtcTimeUsage(AbstractModel):
    """SdkAppId级别实时音视频的用量数据

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId的值。
        :type SdkAppId: str
        :param TrtcTimeUsages: 统计的时间点数据。
        :type TrtcTimeUsages: list of TrtcTimeNewUsage
        :param AudienceTrtcTimeUsages: 统计的麦下用量的时间点数据。
        :type AudienceTrtcTimeUsages: list of TrtcTimeNewUsage
        """
        self.SdkAppId = None
        self.TrtcTimeUsages = None
        self.AudienceTrtcTimeUsages = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("TrtcTimeUsages") is not None:
            self.TrtcTimeUsages = []
            for item in params.get("TrtcTimeUsages"):
                obj = TrtcTimeNewUsage()
                obj._deserialize(item)
                self.TrtcTimeUsages.append(obj)
        if params.get("AudienceTrtcTimeUsages") is not None:
            self.AudienceTrtcTimeUsages = []
            for item in params.get("AudienceTrtcTimeUsages"):
                obj = TrtcTimeNewUsage()
                obj._deserialize(item)
                self.AudienceTrtcTimeUsages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdRecordUsage(AbstractModel):
    """SdkAppId级别录制时长数据。

    """

    def __init__(self):
        r"""
        :param SdkAppId: SdkAppId的值。
        :type SdkAppId: str
        :param Usages: 统计的时间点数据。
        :type Usages: list of RecordUsage
        """
        self.SdkAppId = None
        self.Usages = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("Usages") is not None:
            self.Usages = []
            for item in params.get("Usages"):
                obj = RecordUsage()
                obj._deserialize(item)
                self.Usages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdTrtcMcuTranscodeTimeUsage(AbstractModel):
    """查询旁路转码计费时长。
    查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。

    """

    def __init__(self):
        r"""
        :param TimeKey: 本组数据对应的时间点，格式如：2020-09-07或2020-09-07 00:05:05。
        :type TimeKey: str
        :param AudioTime: 语音时长，单位：秒。
        :type AudioTime: int
        :param VideoTimeSd: 视频时长-标清SD，单位：秒。
        :type VideoTimeSd: int
        :param VideoTimeHd: 视频时长-高清HD，单位：秒。
        :type VideoTimeHd: int
        :param VideoTimeFhd: 视频时长-全高清FHD，单位：秒。
        :type VideoTimeFhd: int
        """
        self.TimeKey = None
        self.AudioTime = None
        self.VideoTimeSd = None
        self.VideoTimeHd = None
        self.VideoTimeFhd = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.AudioTime = params.get("AudioTime")
        self.VideoTimeSd = params.get("VideoTimeSd")
        self.VideoTimeHd = params.get("VideoTimeHd")
        self.VideoTimeFhd = params.get("VideoTimeFhd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmallVideoLayoutParams(AbstractModel):
    """画中画模板中有效，代表小画面的布局参数

    """

    def __init__(self):
        r"""
        :param UserId: 代表小画面对应的用户ID。
        :type UserId: str
        :param StreamType: 代表小画面对应的流类型，0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :type StreamType: int
        :param ImageWidth: 小画面在输出时的宽度，单位为像素值，不填默认为0。
        :type ImageWidth: int
        :param ImageHeight: 小画面在输出时的高度，单位为像素值，不填默认为0。
        :type ImageHeight: int
        :param LocationX: 小画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :type LocationX: int
        :param LocationY: 小画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :type LocationY: int
        """
        self.UserId = None
        self.StreamType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.StreamType = params.get("StreamType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    """StartMCUMixTranscodeByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param StrRoomId: 字符串房间号。
        :type StrRoomId: str
        :param OutputParams: 混流输出控制参数。
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param EncodeParams: 混流输出编码参数。
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param LayoutParams: 混流输出布局参数。
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        :param PublishCdnParams: 第三方CDN转推参数。
        :type PublishCdnParams: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        self.SdkAppId = None
        self.StrRoomId = None
        self.OutputParams = None
        self.EncodeParams = None
        self.LayoutParams = None
        self.PublishCdnParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StrRoomId = params.get("StrRoomId")
        if params.get("OutputParams") is not None:
            self.OutputParams = OutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self.EncodeParams = EncodeParams()
            self.EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("PublishCdnParams") is not None:
            self.PublishCdnParams = PublishCdnParams()
            self.PublishCdnParams._deserialize(params.get("PublishCdnParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    """StartMCUMixTranscodeByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartMCUMixTranscodeRequest(AbstractModel):
    """StartMCUMixTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        :param OutputParams: 混流输出控制参数。
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param EncodeParams: 混流输出编码参数。
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param LayoutParams: 混流输出布局参数。
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        :param PublishCdnParams: 第三方CDN转推参数。
        :type PublishCdnParams: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        self.SdkAppId = None
        self.RoomId = None
        self.OutputParams = None
        self.EncodeParams = None
        self.LayoutParams = None
        self.PublishCdnParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        if params.get("OutputParams") is not None:
            self.OutputParams = OutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self.EncodeParams = EncodeParams()
            self.EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("PublishCdnParams") is not None:
            self.PublishCdnParams = PublishCdnParams()
            self.PublishCdnParams._deserialize(params.get("PublishCdnParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeResponse(AbstractModel):
    """StartMCUMixTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    """StopMCUMixTranscodeByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param StrRoomId: 字符串房间号。
        :type StrRoomId: str
        """
        self.SdkAppId = None
        self.StrRoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StrRoomId = params.get("StrRoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    """StopMCUMixTranscodeByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMCUMixTranscodeRequest(AbstractModel):
    """StopMCUMixTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMCUMixTranscodeResponse(AbstractModel):
    """StopMCUMixTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StorageFile(AbstractModel):
    """云端录制查询接口，录制文件的信息

    """

    def __init__(self):
        r"""
        :param UserId: 录制文件对应的UserId，如果是混流的话的这里返回的是空串。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param FileName: 录制索引文件名。
        :type FileName: str
        :param TrackType: 录制文件流信息。
video：视频录制文件
audio：音频录制文件
audio_video：音视频录制文件
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackType: str
        :param BeginTimeStamp: 录制文件开始Unix时间戳。
        :type BeginTimeStamp: int
        """
        self.UserId = None
        self.FileName = None
        self.TrackType = None
        self.BeginTimeStamp = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.FileName = params.get("FileName")
        self.TrackType = params.get("TrackType")
        self.BeginTimeStamp = params.get("BeginTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageParams(AbstractModel):
    """第三方存储参数。

    """

    def __init__(self):
        r"""
        :param CloudStorage: 第三方云存储的账号信息。
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param CloudVod: 第三方云点播的账号信息。
        :type CloudVod: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        self.CloudStorage = None
        self.CloudVod = None


    def _deserialize(self, params):
        if params.get("CloudStorage") is not None:
            self.CloudStorage = CloudStorage()
            self.CloudStorage._deserialize(params.get("CloudStorage"))
        if params.get("CloudVod") is not None:
            self.CloudVod = CloudVod()
            self.CloudVod._deserialize(params.get("CloudVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeStreamUserIds(AbstractModel):
    """指定订阅流白名单或者黑名单，音频的白名单和音频黑名单不能同时设置，视频亦然。同时实际并发订阅的媒体流路数最大支持25路流，混流场景下视频的多画面最大支持24画面。支持通过设置".*$"通配符，来前缀匹配黑白名单的UserId，注意房间里不能有和通配符规则相同的用户，否则将视为订阅具体用户，前缀规则会失效。

    """

    def __init__(self):
        r"""
        :param SubscribeAudioUserIds: 订阅音频流白名单，指定订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表订阅UserId 1，2，3的音频流；["1.*$"], 代表订阅UserId前缀为1的音频流。默认不填订阅房间内所有的音频流，订阅列表用户数不超过32。
        :type SubscribeAudioUserIds: list of str
        :param UnSubscribeAudioUserIds: 订阅音频流黑名单，指定不订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表不订阅UserId 1，2，3的音频流；["1.*$"], 代表不订阅UserId前缀为1的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过32。
        :type UnSubscribeAudioUserIds: list of str
        :param SubscribeVideoUserIds: 订阅视频流白名单，指定订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表订阅UserId  1，2，3的视频流；["1.*$"], 代表订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
        :type SubscribeVideoUserIds: list of str
        :param UnSubscribeVideoUserIds: 订阅视频流黑名单，指定不订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表不订阅UserId  1，2，3的视频流；["1.*$"], 代表不订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
        :type UnSubscribeVideoUserIds: list of str
        """
        self.SubscribeAudioUserIds = None
        self.UnSubscribeAudioUserIds = None
        self.SubscribeVideoUserIds = None
        self.UnSubscribeVideoUserIds = None


    def _deserialize(self, params):
        self.SubscribeAudioUserIds = params.get("SubscribeAudioUserIds")
        self.UnSubscribeAudioUserIds = params.get("UnSubscribeAudioUserIds")
        self.SubscribeVideoUserIds = params.get("SubscribeVideoUserIds")
        self.UnSubscribeVideoUserIds = params.get("UnSubscribeVideoUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TencentVod(AbstractModel):
    """腾讯云点播相关参数。

    """

    def __init__(self):
        r"""
        :param Procedure: 媒体后续任务处理操作，即完成媒体上传后，可自动发起任务流操作。参数值为任务流模板名，云点播支持 创建任务流模板 并为模板命名。
        :type Procedure: str
        :param ExpireTime: 媒体文件过期时间，为当前时间的绝对过期时间；保存一天，就填"86400"，永久保存就填"0"，默认永久保存。
        :type ExpireTime: int
        :param StorageRegion: 指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :type StorageRegion: str
        :param ClassId: 分类ID，用于对媒体进行分类管理，可通过 创建分类 接口，创建分类，获得分类 ID。
默认值：0，表示其他分类。
        :type ClassId: int
        :param SubAppId: 点播 子应用 ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param SessionContext: 任务流上下文，任务完成回调时透传。
        :type SessionContext: str
        :param SourceContext: 上传上下文，上传完成回调时透传。
        :type SourceContext: str
        """
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SubAppId = None
        self.SessionContext = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SubAppId = params.get("SubAppId")
        self.SessionContext = params.get("SessionContext")
        self.SourceContext = params.get("SourceContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeValue(AbstractModel):
    """返回的质量数据，时间:值

    """

    def __init__(self):
        r"""
        :param Time: 时间，unix时间戳（1590065877s)
        :type Time: int
        :param Value: 当前时间返回参数取值，如（bigvCapFps在1590065877取值为0，则Value：0 ）
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrtcTimeNewUsage(AbstractModel):
    """实时音视频用量的某一时间段的统计信息.

    """

    def __init__(self):
        r"""
        :param TimeKey: 时间点。
        :type TimeKey: str
        :param VoiceUserNum: 通话人数。仅供参考。在线人数以仪表盘查询结果为准。
        :type VoiceUserNum: int
        :param VideoTime: 音视频通话时长。单位：秒。
        :type VideoTime: int
        :param Class1VideoTime: 标清视频通话时长。单位：秒。
        :type Class1VideoTime: int
        :param Class2VideoTime: 高清视频通话时长。单位：秒。
        :type Class2VideoTime: int
        :param Class3VideoTime: 超高清视频通话时长。单位：秒。
        :type Class3VideoTime: int
        :param AudioTime: 音频通话时长。单位：秒。
        :type AudioTime: int
        :param Bandwidth: 带宽。单位：Mbps。
        :type Bandwidth: float
        :param Video2KTime: 2k视频通话时长。单位：秒。
        :type Video2KTime: int
        :param Video4KTime: 4k视频通话时长。单位：秒。
        :type Video4KTime: int
        """
        self.TimeKey = None
        self.VoiceUserNum = None
        self.VideoTime = None
        self.Class1VideoTime = None
        self.Class2VideoTime = None
        self.Class3VideoTime = None
        self.AudioTime = None
        self.Bandwidth = None
        self.Video2KTime = None
        self.Video4KTime = None


    def _deserialize(self, params):
        self.TimeKey = params.get("TimeKey")
        self.VoiceUserNum = params.get("VoiceUserNum")
        self.VideoTime = params.get("VideoTime")
        self.Class1VideoTime = params.get("Class1VideoTime")
        self.Class2VideoTime = params.get("Class2VideoTime")
        self.Class3VideoTime = params.get("Class3VideoTime")
        self.AudioTime = params.get("AudioTime")
        self.Bandwidth = params.get("Bandwidth")
        self.Video2KTime = params.get("Video2KTime")
        self.Video4KTime = params.get("Video4KTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInformation(AbstractModel):
    """用户信息，包括用户进房时间，退房时间等

    """

    def __init__(self):
        r"""
        :param RoomStr: 房间号
        :type RoomStr: str
        :param UserId: 用户Id
        :type UserId: str
        :param JoinTs: 用户进房时间
        :type JoinTs: int
        :param LeaveTs: 用户退房时间，用户没有退房则返回当前时间
        :type LeaveTs: int
        :param DeviceType: 终端类型
        :type DeviceType: str
        :param SdkVersion: Sdk版本号
        :type SdkVersion: str
        :param ClientIp: 客户端IP地址
        :type ClientIp: str
        :param Finished: 判断用户是否已经离开房间
        :type Finished: bool
        """
        self.RoomStr = None
        self.UserId = None
        self.JoinTs = None
        self.LeaveTs = None
        self.DeviceType = None
        self.SdkVersion = None
        self.ClientIp = None
        self.Finished = None


    def _deserialize(self, params):
        self.RoomStr = params.get("RoomStr")
        self.UserId = params.get("UserId")
        self.JoinTs = params.get("JoinTs")
        self.LeaveTs = params.get("LeaveTs")
        self.DeviceType = params.get("DeviceType")
        self.SdkVersion = params.get("SdkVersion")
        self.ClientIp = params.get("ClientIp")
        self.Finished = params.get("Finished")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoParams(AbstractModel):
    """录制视频转码参数。

    """

    def __init__(self):
        r"""
        :param Width: 视频的宽度值，单位为像素，默认值360。不能超过1920，与height的乘积不能超过1920*1080。
        :type Width: int
        :param Height: 视频的高度值，单位为像素，默认值640。不能超过1920，与width的乘积不能超过1920*1080。
        :type Height: int
        :param Fps: 视频的帧率，范围[1, 60]，默认15。
        :type Fps: int
        :param BitRate: 视频的码率,单位是bps，范围[64000, 8192000]，默认550000bps。
        :type BitRate: int
        :param Gop: 视频关键帧时间间隔，单位秒，默认值10秒。
        :type Gop: int
        """
        self.Width = None
        self.Height = None
        self.Fps = None
        self.BitRate = None
        self.Gop = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.BitRate = params.get("BitRate")
        self.Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMark(AbstractModel):
    """水印布局参数

    """

    def __init__(self):
        r"""
        :param WaterMarkType: 水印类型，0为图片（默认），1为文字（暂不支持）。
        :type WaterMarkType: int
        :param WaterMarkImage: 水印为图片时的参数列表，水印为图片时校验必填。
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        """
        self.WaterMarkType = None
        self.WaterMarkImage = None


    def _deserialize(self, params):
        self.WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self.WaterMarkImage = WaterMarkImage()
            self.WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkImage(AbstractModel):
    """水印类型为图片的参数列表

    """

    def __init__(self):
        r"""
        :param WaterMarkUrl: 下载的url地址， 只支持jpg， png，大小限制不超过5M。
        :type WaterMarkUrl: str
        :param Top: 画布上该画面左上角的 y 轴坐标，取值范围 [0, 2560]，不能超过画布的高。
        :type Top: int
        :param Left: 画布上该画面左上角的 x 轴坐标，取值范围 [0, 2560]，不能超过画布的宽。
        :type Left: int
        :param Width: 画布上该画面宽度的相对值，取值范围 [0, 2560]，与Left相加不应超过画布的宽。
        :type Width: int
        :param Height: 画布上该画面高度的相对值，取值范围 [0, 2560]，与Top相加不应超过画布的高。
        :type Height: int
        """
        self.WaterMarkUrl = None
        self.Top = None
        self.Left = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WaterMarkUrl = params.get("WaterMarkUrl")
        self.Top = params.get("Top")
        self.Left = params.get("Left")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkParams(AbstractModel):
    """MCU混流水印参数

    """

    def __init__(self):
        r"""
        :param WaterMarkId: 混流-水印图片ID。取值为实时音视频控制台上传的图片ID。
        :type WaterMarkId: int
        :param WaterMarkWidth: 混流-水印宽。单位为像素值。水印宽+X偏移不能超过整个画布宽。
        :type WaterMarkWidth: int
        :param WaterMarkHeight: 混流-水印高。单位为像素值。水印高+Y偏移不能超过整个画布高。
        :type WaterMarkHeight: int
        :param LocationX: 水印在输出时的X偏移。单位为像素值。水印宽+X偏移不能超过整个画布宽。
        :type LocationX: int
        :param LocationY: 水印在输出时的Y偏移。单位为像素值。水印高+Y偏移不能超过整个画布高。
        :type LocationY: int
        :param WaterMarkUrl: 混流-水印图片URL地址，支持png、jpg、jpeg、bmp格式，暂不支持透明通道。URL链接长度限制为512字节。WaterMarkUrl和WaterMarkId参数都填时，以WaterMarkUrl为准。图片大小限制不超过2MB。
        :type WaterMarkUrl: str
        """
        self.WaterMarkId = None
        self.WaterMarkWidth = None
        self.WaterMarkHeight = None
        self.LocationX = None
        self.LocationY = None
        self.WaterMarkUrl = None


    def _deserialize(self, params):
        self.WaterMarkId = params.get("WaterMarkId")
        self.WaterMarkWidth = params.get("WaterMarkWidth")
        self.WaterMarkHeight = params.get("WaterMarkHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.WaterMarkUrl = params.get("WaterMarkUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        