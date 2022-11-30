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


class AppCustomContent(AbstractModel):
    """应用自定义内容

    """

    def __init__(self):
        r"""
        :param Scene: 场景参数，一个应用下可以设置多个不同场景。
        :type Scene: str
        :param LogoUrl: logo地址。
        :type LogoUrl: str
        :param HomeUrl: 主页地址，可设置用于跳转。
        :type HomeUrl: str
        :param JsUrl: 自定义的js。
        :type JsUrl: str
        :param CssUrl: 自定义的css。
        :type CssUrl: str
        """
        self.Scene = None
        self.LogoUrl = None
        self.HomeUrl = None
        self.JsUrl = None
        self.CssUrl = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.LogoUrl = params.get("LogoUrl")
        self.HomeUrl = params.get("HomeUrl")
        self.JsUrl = params.get("JsUrl")
        self.CssUrl = params.get("CssUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomRequest(AbstractModel):
    """BindDocumentToRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间ID。
        :type RoomId: int
        :param DocumentId: 文档ID。
        :type DocumentId: str
        :param BindType: 绑定类型。后台可透传到客户端，默认为0。客户端可以根据这个字段实现业务逻辑。
        :type BindType: int
        """
        self.RoomId = None
        self.DocumentId = None
        self.BindType = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.DocumentId = params.get("DocumentId")
        self.BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomResponse(AbstractModel):
    """BindDocumentToRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDocumentRequest(AbstractModel):
    """CreateDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param DocumentUrl: 文档地址。
        :type DocumentUrl: str
        :param DocumentName: 文档名称。
        :type DocumentName: str
        :param Owner: 文档所有者的Id
        :type Owner: str
        :param TranscodeType: 转码类型，可以有如下取值：
0 无需转码（默认）
1 需要转码的文档，ppt，pptx，pdf，doc，docx
2 需要转码的视频，mp4，3pg，mpeg，avi，flv，wmv，rm，h264等
2 需要转码的音频，mp3，wav，wma，aac，flac，opus
        :type TranscodeType: int
        :param Permission: 权限，可以有如下取值：
0 私有文档（默认）
1 公共文档
        :type Permission: int
        :param DocumentType: 文档后缀名。
        :type DocumentType: str
        :param DocumentSize: 文档大小，单位 字节
        :type DocumentSize: int
        """
        self.SdkAppId = None
        self.DocumentUrl = None
        self.DocumentName = None
        self.Owner = None
        self.TranscodeType = None
        self.Permission = None
        self.DocumentType = None
        self.DocumentSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.DocumentUrl = params.get("DocumentUrl")
        self.DocumentName = params.get("DocumentName")
        self.Owner = params.get("Owner")
        self.TranscodeType = params.get("TranscodeType")
        self.Permission = params.get("Permission")
        self.DocumentType = params.get("DocumentType")
        self.DocumentSize = params.get("DocumentSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentResponse(AbstractModel):
    """CreateDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param DocumentId: 文档ID。
        :type DocumentId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DocumentId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.RequestId = params.get("RequestId")


class CreateRoomRequest(AbstractModel):
    """CreateRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 房间名称。
        :type Name: str
        :param StartTime: 预定的房间开始时间，unix时间戳。
        :type StartTime: int
        :param EndTime: 预定的房间结束时间，unix时间戳。
        :type EndTime: int
        :param SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param Resolution: 分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :type Resolution: int
        :param MaxMicNumber: 最大连麦人数（不包括老师）。取值范围[0, 17)
        :type MaxMicNumber: int
        :param SubType: 房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
coteaching 双师
        :type SubType: str
        :param TeacherId: 老师ID。
        :type TeacherId: str
        :param AutoMic: 进入房间时是否自动连麦。可以有以下取值：
0 不自动连麦（默认值）
1 自动连麦
        :type AutoMic: int
        :param AudioQuality: 高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
        :type AudioQuality: int
        :param DisableRecord: 禁止录制。可以有以下取值：
0 不禁止录制（默认值）
1 禁止录制
        :type DisableRecord: int
        :param Assistants: 助教Id列表。
        :type Assistants: list of str
        :param RecordLayout: 录制布局。
        :type RecordLayout: int
        """
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.SubType = None
        self.TeacherId = None
        self.AutoMic = None
        self.AudioQuality = None
        self.DisableRecord = None
        self.Assistants = None
        self.RecordLayout = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.SubType = params.get("SubType")
        self.TeacherId = params.get("TeacherId")
        self.AutoMic = params.get("AutoMic")
        self.AudioQuality = params.get("AudioQuality")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        self.RecordLayout = params.get("RecordLayout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoomResponse(AbstractModel):
    """CreateRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间ID。
        :type RoomId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoomId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.RequestId = params.get("RequestId")


class CreateSupervisorRequest(AbstractModel):
    """CreateSupervisor请求参数结构体

    """


class CreateSupervisorResponse(AbstractModel):
    """CreateSupervisor返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoomRequest(AbstractModel):
    """DeleteRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间ID。
        :type RoomId: int
        """
        self.RoomId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomResponse(AbstractModel):
    """DeleteRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeRoomRequest(AbstractModel):
    """DescribeRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间Id。
        :type RoomId: int
        """
        self.RoomId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomResponse(AbstractModel):
    """DescribeRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 房间名称。
        :type Name: str
        :param StartTime: 预定的房间开始时间，unix时间戳。
        :type StartTime: int
        :param EndTime: 预定的房间结束时间，unix时间戳。
        :type EndTime: int
        :param TeacherId: 老师ID。
        :type TeacherId: str
        :param SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param Resolution: 分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :type Resolution: int
        :param MaxMicNumber: 最大连麦人数（不包括老师）。取值范围[0, 16]
        :type MaxMicNumber: int
        :param AutoMic: 进入房间时是否自动连麦。可以有以下取值：
0 不自动连麦（默认值）
1 自动连麦
        :type AutoMic: int
        :param AudioQuality: 高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
        :type AudioQuality: int
        :param SubType: 房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
coteaching 双师
        :type SubType: str
        :param DisableRecord: 禁止录制。可以有以下取值：
0 不禁止录制（默认值）
1 禁止录制
        :type DisableRecord: int
        :param Assistants: 助教Id列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Assistants: list of str
        :param RecordUrl: 录制地址。仅在房间结束后存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.TeacherId = None
        self.SdkAppId = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.AutoMic = None
        self.AudioQuality = None
        self.SubType = None
        self.DisableRecord = None
        self.Assistants = None
        self.RecordUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TeacherId = params.get("TeacherId")
        self.SdkAppId = params.get("SdkAppId")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.AutoMic = params.get("AutoMic")
        self.AudioQuality = params.get("AudioQuality")
        self.SubType = params.get("SubType")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        self.RecordUrl = params.get("RecordUrl")
        self.RequestId = params.get("RequestId")


class DescribeRoomStatisticsRequest(AbstractModel):
    """DescribeRoomStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间Id。
        :type RoomId: int
        :param Page: 分页查询当前页数，从1开始递增。
        :type Page: int
        :param Limit: 每页数据量，最大1000。
        :type Limit: int
        """
        self.RoomId = None
        self.Page = None
        self.Limit = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomStatisticsResponse(AbstractModel):
    """DescribeRoomStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param PeakMemberNumber: 峰值在线成员人数。
        :type PeakMemberNumber: int
        :param MemberNumber: 累计在线人数。
        :type MemberNumber: int
        :param Total: 记录总数。包含进入房间或者应到未到的。
        :type Total: int
        :param MemberRecords: 成员记录列表。
        :type MemberRecords: list of MemberRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PeakMemberNumber = None
        self.MemberNumber = None
        self.Total = None
        self.MemberRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PeakMemberNumber = params.get("PeakMemberNumber")
        self.MemberNumber = params.get("MemberNumber")
        self.Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self.MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self.MemberRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户Id。
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用Id。
        :type SdkAppId: int
        :param UserId: 用户Id。
        :type UserId: str
        :param Name: 用户昵称。
        :type Name: str
        :param Avatar: 用户头像Url。
        :type Avatar: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.Name = None
        self.Avatar = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.Avatar = params.get("Avatar")
        self.RequestId = params.get("RequestId")


class LoginOriginIdRequest(AbstractModel):
    """LoginOriginId请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param OriginId: 用户在客户系统的Id，需要在同一应用下唯一。
        :type OriginId: str
        """
        self.SdkAppId = None
        self.OriginId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginOriginIdResponse(AbstractModel):
    """LoginOriginId返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户Id。
        :type UserId: str
        :param Token: 登录/注册成功后返回登录态token。有效期7天。
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class LoginUserRequest(AbstractModel):
    """LoginUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 注册获取的用户id。
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginUserResponse(AbstractModel):
    """LoginUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户Id。
        :type UserId: str
        :param Token: 登录/注册成功后返回登录态token。有效期7天。
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class MemberRecord(AbstractModel):
    """成员记录信息。

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID。
        :type UserId: str
        :param UserName: 用户名称。
        :type UserName: str
        :param PresentTime: 在线时长，单位秒。
        :type PresentTime: int
        :param Camera: 是否开启摄像头。
        :type Camera: int
        :param Mic: 是否开启麦克风。
        :type Mic: int
        :param Silence: 是否禁言。
        :type Silence: int
        :param AnswerQuestions: 回答问题数量。
        :type AnswerQuestions: int
        :param HandUps: 举手数量。
        :type HandUps: int
        :param FirstJoinTimestamp: 首次进入房间的unix时间戳。
        :type FirstJoinTimestamp: int
        :param LastQuitTimestamp: 最后一次退出房间的unix时间戳。
        :type LastQuitTimestamp: int
        :param Rewords: 奖励次数。
        :type Rewords: int
        """
        self.UserId = None
        self.UserName = None
        self.PresentTime = None
        self.Camera = None
        self.Mic = None
        self.Silence = None
        self.AnswerQuestions = None
        self.HandUps = None
        self.FirstJoinTimestamp = None
        self.LastQuitTimestamp = None
        self.Rewords = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserName = params.get("UserName")
        self.PresentTime = params.get("PresentTime")
        self.Camera = params.get("Camera")
        self.Mic = params.get("Mic")
        self.Silence = params.get("Silence")
        self.AnswerQuestions = params.get("AnswerQuestions")
        self.HandUps = params.get("HandUps")
        self.FirstJoinTimestamp = params.get("FirstJoinTimestamp")
        self.LastQuitTimestamp = params.get("LastQuitTimestamp")
        self.Rewords = params.get("Rewords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppRequest(AbstractModel):
    """ModifyApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param Callback: 回调地址。
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppResponse(AbstractModel):
    """ModifyApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterUserRequest(AbstractModel):
    """RegisterUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param Name: 用户名称。
        :type Name: str
        :param OriginId: 用户在客户系统的Id，需要在同一应用下唯一。
        :type OriginId: str
        :param Avatar: 用户头像。
        :type Avatar: str
        """
        self.SdkAppId = None
        self.Name = None
        self.OriginId = None
        self.Avatar = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Name = params.get("Name")
        self.OriginId = params.get("OriginId")
        self.Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterUserResponse(AbstractModel):
    """RegisterUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户Id。
        :type UserId: str
        :param Token: 登录/注册成功后返回登录态token。有效期7天。
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class SetAppCustomContentRequest(AbstractModel):
    """SetAppCustomContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param CustomContent: 自定义内容。
        :type CustomContent: list of AppCustomContent
        :param SdkAppId: 应用ID。
        :type SdkAppId: int
        """
        self.CustomContent = None
        self.SdkAppId = None


    def _deserialize(self, params):
        if params.get("CustomContent") is not None:
            self.CustomContent = []
            for item in params.get("CustomContent"):
                obj = AppCustomContent()
                obj._deserialize(item)
                self.CustomContent.append(obj)
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAppCustomContentResponse(AbstractModel):
    """SetAppCustomContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindDocumentFromRoomRequest(AbstractModel):
    """UnbindDocumentFromRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间ID。
        :type RoomId: int
        :param DocumentId: 文档ID。
        :type DocumentId: str
        """
        self.RoomId = None
        self.DocumentId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDocumentFromRoomResponse(AbstractModel):
    """UnbindDocumentFromRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")