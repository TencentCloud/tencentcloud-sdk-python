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


class AppConfig(AbstractModel):
    """应用配置信息

    """


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
        


class BackgroundPictureConfig(AbstractModel):
    """背景图片配置

    """

    def __init__(self):
        r"""
        :param Url: 背景图片的url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateRoomRequest(AbstractModel):
    """BatchCreateRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码平台的SdkAppId。
        :type SdkAppId: int
        :param RoomInfos: 创建房间ID列表
        :type RoomInfos: list of RoomInfo
        """
        self.SdkAppId = None
        self.RoomInfos = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("RoomInfos") is not None:
            self.RoomInfos = []
            for item in params.get("RoomInfos"):
                obj = RoomInfo()
                obj._deserialize(item)
                self.RoomInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateRoomResponse(AbstractModel):
    """BatchCreateRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoomIds: 创建成功课堂ID，与传入课堂信息顺序一致
        :type RoomIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoomIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoomIds = params.get("RoomIds")
        self.RequestId = params.get("RequestId")


class BatchDeleteRecordRequest(AbstractModel):
    """BatchDeleteRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomIds: 房间ID列表
        :type RoomIds: list of int
        :param SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        """
        self.RoomIds = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.RoomIds = params.get("RoomIds")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteRecordResponse(AbstractModel):
    """BatchDeleteRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param RoomIds: 本次操作删除成功的房间ID列表。如果入参列表中某个房间ID的录制文件已经删除，则出参列表中无对应的房间ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomIds: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RoomIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoomIds = params.get("RoomIds")
        self.RequestId = params.get("RequestId")


class BatchRegisterRequest(AbstractModel):
    """BatchRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param Users: 批量注册用户信息列表
        :type Users: list of BatchUserRequest
        """
        self.Users = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = BatchUserRequest()
                obj._deserialize(item)
                self.Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterResponse(AbstractModel):
    """BatchRegister返回参数结构体

    """

    def __init__(self):
        r"""
        :param Users: 注册成功的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of BatchUserInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = BatchUserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class BatchUserInfo(AbstractModel):
    """批量注册用户信息

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        :param UserId: 用户ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param OriginId: 用户在客户系统的Id。 若用户注册时该字段为空，则默认为 UserId 值一致。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginId: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.OriginId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUserRequest(AbstractModel):
    """用户注册请求信息

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。

注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppId: int
        :param Name: 用户名称。

注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param OriginId: 用户在客户系统的Id，需要在同一应用下唯一。

注意：此字段可能返回 null，表示取不到有效值。
        :type OriginId: str
        :param Avatar: 用户头像。

注意：此字段可能返回 null，表示取不到有效值。
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
        :param MaxMicNumber: 最大连麦人数（不包括老师）。取值范围[0, 16]
        :type MaxMicNumber: int
        :param SubType: 房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
coteaching 双师
        :type SubType: str
        :param TeacherId: 老师ID。通过[注册用户]接口获取的UserId。指定后该用户在房间内拥有老师权限。
        :type TeacherId: str
        :param AutoMic: 进入课堂时是否自动连麦。可以有以下取值：
0 不自动连麦（需要手动申请上麦，默认值）
1 自动连麦
        :type AutoMic: int
        :param AudioQuality: 高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
        :type AudioQuality: int
        :param DisableRecord: 上课后是否禁止自动录制。可以有以下取值：
0 不禁止录制（自动开启录制，默认值）
1 禁止录制
注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :type DisableRecord: int
        :param Assistants: 助教Id列表。通过[注册用户]接口获取的UserId。指定后该用户在房间内拥有助教权限。
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


class DeleteDocumentRequest(AbstractModel):
    """DeleteDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param DocumentId: 文档ID。
        :type DocumentId: str
        """
        self.DocumentId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocumentResponse(AbstractModel):
    """DeleteDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间Id。
        :type RoomId: int
        :param SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        """
        self.RoomId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    """DeleteRecord返回参数结构体

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


class DescribeAppDetailRequest(AbstractModel):
    """DescribeAppDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID。低代码互动课堂的SdkAppId。

        :type ApplicationId: str
        :param DeveloperId: 开发商ID
        :type DeveloperId: str
        """
        self.ApplicationId = None
        self.DeveloperId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.DeveloperId = params.get("DeveloperId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppDetailResponse(AbstractModel):
    """DescribeAppDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: SDK 对应的AppId 
        :type SdkAppId: str
        :param AppConfig: 应用配置
        :type AppConfig: :class:`tencentcloud.lcic.v20220817.models.AppConfig`
        :param SceneConfig: 场景配置
        :type SceneConfig: list of SceneItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SdkAppId = None
        self.AppConfig = None
        self.SceneConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        if params.get("AppConfig") is not None:
            self.AppConfig = AppConfig()
            self.AppConfig._deserialize(params.get("AppConfig"))
        if params.get("SceneConfig") is not None:
            self.SceneConfig = []
            for item in params.get("SceneConfig"):
                obj = SceneItem()
                obj._deserialize(item)
                self.SceneConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCurrentMemberListRequest(AbstractModel):
    """DescribeCurrentMemberList请求参数结构体

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
        


class DescribeCurrentMemberListResponse(AbstractModel):
    """DescribeCurrentMemberList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数。当前房间的总人数。
        :type Total: int
        :param MemberRecords: 成员记录列表。
        :type MemberRecords: list of MemberRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.MemberRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self.MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self.MemberRecords.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDocumentRequest(AbstractModel):
    """DescribeDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param DocumentId: 文档Id（唯一id）
        :type DocumentId: str
        """
        self.DocumentId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentResponse(AbstractModel):
    """DescribeDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param DocumentId: 文档Id
        :type DocumentId: str
        :param DocumentUrl: 文档原址url
        :type DocumentUrl: str
        :param DocumentName: 文档名称
        :type DocumentName: str
        :param Owner: 文档所有者UserId
        :type Owner: str
        :param SdkAppId: 应用Id
        :type SdkAppId: int
        :param Permission: 文档权限
        :type Permission: int
        :param TranscodeResult: 转码结果，无需转码为空，转码成功为结果url，转码失败为错误码
        :type TranscodeResult: str
        :param TranscodeType: 转码类型
        :type TranscodeType: int
        :param TranscodeProgress: 转码进度， 0 - 100 表示（0% - 100%）
        :type TranscodeProgress: int
        :param TranscodeState: 转码状态，0为无需转码，1为正在转码，2为转码失败，3为转码成功
        :type TranscodeState: int
        :param TranscodeInfo: 转码失败后的错误信息
        :type TranscodeInfo: str
        :param DocumentType: 文档类型
        :type DocumentType: str
        :param DocumentSize: 文档大小，单位：字节
        :type DocumentSize: int
        :param UpdateTime: 更新的UNIX时间戳
        :type UpdateTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DocumentId = None
        self.DocumentUrl = None
        self.DocumentName = None
        self.Owner = None
        self.SdkAppId = None
        self.Permission = None
        self.TranscodeResult = None
        self.TranscodeType = None
        self.TranscodeProgress = None
        self.TranscodeState = None
        self.TranscodeInfo = None
        self.DocumentType = None
        self.DocumentSize = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.DocumentUrl = params.get("DocumentUrl")
        self.DocumentName = params.get("DocumentName")
        self.Owner = params.get("Owner")
        self.SdkAppId = params.get("SdkAppId")
        self.Permission = params.get("Permission")
        self.TranscodeResult = params.get("TranscodeResult")
        self.TranscodeType = params.get("TranscodeType")
        self.TranscodeProgress = params.get("TranscodeProgress")
        self.TranscodeState = params.get("TranscodeState")
        self.TranscodeInfo = params.get("TranscodeInfo")
        self.DocumentType = params.get("DocumentType")
        self.DocumentSize = params.get("DocumentSize")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")


class DescribeDocumentsByRoomRequest(AbstractModel):
    """DescribeDocumentsByRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间ID。
        :type RoomId: int
        :param SdkAppId: 低代码互动课堂的SdkAppId
        :type SdkAppId: int
        :param Page: 分页查询当前页数，从1开始递增，默认值为1
        :type Page: int
        :param Limit: 每页数据量，最大1000，默认值为100
        :type Limit: int
        :param Permission: 课件权限。
[0]：获取owner的私有课件；
[1]：获取owner的公开课件;
[0,1]：则获取owner的私有课件和公开课件；
[2]：获取owner的私有课件和所有人(包括owner)的公开课件。
默认值为[2]
        :type Permission: list of int non-negative
        :param Owner: 文档所有者的user_id，不填默认获取SdkAppId下所有课件
        :type Owner: str
        """
        self.RoomId = None
        self.SdkAppId = None
        self.Page = None
        self.Limit = None
        self.Permission = None
        self.Owner = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        self.Permission = params.get("Permission")
        self.Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentsByRoomResponse(AbstractModel):
    """DescribeDocumentsByRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param Documents: 文档信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Documents: list of DocumentInfo
        :param Total: 符合查询条件文档总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Documents = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Documents") is not None:
            self.Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self.Documents.append(obj)
        self.Total = params.get("Total")
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
        :param TeacherId: 老师的UserId。
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
        :param AutoMic: 进入课堂时是否自动连麦。可以有以下取值：
0 不自动连麦（需要手动申请上麦，默认值）
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
        :param DisableRecord: 上课后是否禁止自动录制。可以有以下取值：
0 不禁止录制（自动开启录制，默认值）
1 禁止录制
注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :type DisableRecord: int
        :param Assistants: 助教UserId列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Assistants: list of str
        :param RecordUrl: 录制地址。仅在房间结束后存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordUrl: str
        :param Status: 课堂状态。0为未开始，1为正在上课，2为已结束，3为已过期。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
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
        self.Status = None
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
        self.Status = params.get("Status")
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
        :param RealStartTime: 秒级unix时间戳，实际房间开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealStartTime: int
        :param RealEndTime: 秒级unix时间戳，实际房间结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealEndTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PeakMemberNumber = None
        self.MemberNumber = None
        self.Total = None
        self.MemberRecords = None
        self.RealStartTime = None
        self.RealEndTime = None
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
        self.RealStartTime = params.get("RealStartTime")
        self.RealEndTime = params.get("RealEndTime")
        self.RequestId = params.get("RequestId")


class DescribeSdkAppIdUsersRequest(AbstractModel):
    """DescribeSdkAppIdUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用ID
        :type SdkAppId: int
        :param Page: 分页，默认值为1
        :type Page: int
        :param Limit: 分页数据限制，默认值为20
        :type Limit: int
        """
        self.SdkAppId = None
        self.Page = None
        self.Limit = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Page = params.get("Page")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSdkAppIdUsersResponse(AbstractModel):
    """DescribeSdkAppIdUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 用户总数
        :type Total: int
        :param Users: 当前获取用户信息数组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of UserInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
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


class DocumentInfo(AbstractModel):
    """文档信息

    """

    def __init__(self):
        r"""
        :param DocumentId: 文档Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentId: str
        :param DocumentUrl: 文档原址url
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentUrl: str
        :param DocumentName: 文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentName: str
        :param Owner: 文档所有者UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param SdkAppId: 应用Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppId: int
        :param Permission: 文档权限，0：私有课件 1：公共课件
注意：此字段可能返回 null，表示取不到有效值。
        :type Permission: int
        :param TranscodeResult: 转码结果，无需转码为空，转码成功为结果url，转码失败为错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeResult: str
        :param TranscodeType: 转码类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeType: int
        :param TranscodeProgress: 转码进度， 0 - 100 表示（0% - 100%）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeProgress: int
        :param TranscodeState: 转码状态，0为无需转码，1为正在转码，2为转码失败，3为转码成功
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeState: int
        :param TranscodeInfo: 转码失败后的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeInfo: str
        :param DocumentType: 文档类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentType: str
        :param DocumentSize: 文档大小，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentSize: int
        :param UpdateTime: 更新的UNIX时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        """
        self.DocumentId = None
        self.DocumentUrl = None
        self.DocumentName = None
        self.Owner = None
        self.SdkAppId = None
        self.Permission = None
        self.TranscodeResult = None
        self.TranscodeType = None
        self.TranscodeProgress = None
        self.TranscodeState = None
        self.TranscodeInfo = None
        self.DocumentType = None
        self.DocumentSize = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.DocumentUrl = params.get("DocumentUrl")
        self.DocumentName = params.get("DocumentName")
        self.Owner = params.get("Owner")
        self.SdkAppId = params.get("SdkAppId")
        self.Permission = params.get("Permission")
        self.TranscodeResult = params.get("TranscodeResult")
        self.TranscodeType = params.get("TranscodeType")
        self.TranscodeProgress = params.get("TranscodeProgress")
        self.TranscodeState = params.get("TranscodeState")
        self.TranscodeInfo = params.get("TranscodeInfo")
        self.DocumentType = params.get("DocumentType")
        self.DocumentSize = params.get("DocumentSize")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWatermarkRequest(AbstractModel):
    """GetWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWatermarkResponse(AbstractModel):
    """GetWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param TeacherLogo: 老师视频区域的水印参数配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TeacherLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param BoardLogo: 白板区域的水印参数配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BoardLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param BackgroundPicture: 背景图片配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BackgroundPicture: :class:`tencentcloud.lcic.v20220817.models.BackgroundPictureConfig`
        :param Text: 文字水印配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.lcic.v20220817.models.TextMarkConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TeacherLogo = None
        self.BoardLogo = None
        self.BackgroundPicture = None
        self.Text = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TeacherLogo") is not None:
            self.TeacherLogo = WatermarkConfig()
            self.TeacherLogo._deserialize(params.get("TeacherLogo"))
        if params.get("BoardLogo") is not None:
            self.BoardLogo = WatermarkConfig()
            self.BoardLogo._deserialize(params.get("BoardLogo"))
        if params.get("BackgroundPicture") is not None:
            self.BackgroundPicture = BackgroundPictureConfig()
            self.BackgroundPicture._deserialize(params.get("BackgroundPicture"))
        if params.get("Text") is not None:
            self.Text = TextMarkConfig()
            self.Text._deserialize(params.get("Text"))
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
        :param IPAddress: 用户IP。
        :type IPAddress: str
        :param Location: 用户位置信息。
        :type Location: str
        :param Device: 用户设备平台信息。0:unknown  1:windows  2:mac  3:android  4:ios  5:web   6:h5   7:miniprogram （小程序）
        :type Device: int
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
        self.IPAddress = None
        self.Location = None
        self.Device = None


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
        self.IPAddress = params.get("IPAddress")
        self.Location = params.get("Location")
        self.Device = params.get("Device")
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
        :param CallbackKey: 回调key。
        :type CallbackKey: str
        """
        self.SdkAppId = None
        self.Callback = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")
        self.CallbackKey = params.get("CallbackKey")
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


class ModifyRoomRequest(AbstractModel):
    """ModifyRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoomId: 房间ID。
        :type RoomId: int
        :param SdkAppId: 低代码互动课堂的SdkAppId
        :type SdkAppId: int
        :param StartTime: 预定的房间开始时间，unix时间戳。直播开始后不允许修改。
        :type StartTime: int
        :param EndTime: 预定的房间结束时间，unix时间戳。直播开始后不允许修改。
        :type EndTime: int
        :param TeacherId: 老师ID。直播开始后不允许修改。
        :type TeacherId: str
        :param Name: 房间名称。
        :type Name: str
        :param Resolution: 分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
直播开始后不允许修改。
        :type Resolution: int
        :param MaxMicNumber: 最大连麦人数（不包括老师）。取值范围[0, 17)
直播开始后不允许修改。
        :type MaxMicNumber: int
        :param AutoMic: 进入房间时是否自动连麦。可以有以下取值：
0 不自动连麦（默认值）
1 自动连麦
直播开始后不允许修改。
        :type AutoMic: int
        :param AudioQuality: 高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
直播开始后不允许修改。
        :type AudioQuality: int
        :param SubType: 房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
coteaching 双师
直播开始后不允许修改。
        :type SubType: str
        :param DisableRecord: 禁止录制。可以有以下取值：
0 不禁止录制（默认值）
1 禁止录制
直播开始后不允许修改。
        :type DisableRecord: int
        :param Assistants: 助教Id列表。直播开始后不允许修改。
        :type Assistants: list of str
        """
        self.RoomId = None
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.TeacherId = None
        self.Name = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.AutoMic = None
        self.AudioQuality = None
        self.SubType = None
        self.DisableRecord = None
        self.Assistants = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TeacherId = params.get("TeacherId")
        self.Name = params.get("Name")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.AutoMic = params.get("AutoMic")
        self.AudioQuality = params.get("AudioQuality")
        self.SubType = params.get("SubType")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomResponse(AbstractModel):
    """ModifyRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserProfileRequest(AbstractModel):
    """ModifyUserProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 待修改用户ID
        :type UserId: str
        :param Nickname: 待修改的用户名
        :type Nickname: str
        :param Avatar: 待修改头像url
        :type Avatar: str
        """
        self.UserId = None
        self.Nickname = None
        self.Avatar = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Nickname = params.get("Nickname")
        self.Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserProfileResponse(AbstractModel):
    """ModifyUserProfile返回参数结构体

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


class RoomInfo(AbstractModel):
    """批量创建房间的房间信息

    """

    def __init__(self):
        r"""
        :param Name: 房间名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param StartTime: 预定的房间开始时间，unix时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param EndTime: 预定的房间结束时间，unix时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param Resolution: 分辨率。可以有如下取值： 1 标清 2 高清 3 全高清
注意：此字段可能返回 null，表示取不到有效值。
        :type Resolution: int
        :param MaxMicNumber: 最大连麦人数（不包括老师）。取值范围[0, 16]
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMicNumber: int
        :param SubType: 房间子类型，可以有以下取值： videodoc 文档+视频 video 纯视频 coteaching 双师
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param TeacherId: 老师ID。通过[注册用户]接口获取的UserId。
注意：此字段可能返回 null，表示取不到有效值。
        :type TeacherId: str
        :param AutoMic: 进入课堂时是否自动连麦。可以有以下取值： 0 不自动连麦（需要手动申请上麦，默认值） 1 自动连麦
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoMic: int
        :param TurnOffMic: 释放音视频权限后是否自动取消连麦。可以有以下取值： 0 自动取消连麦（默认值） 1 保持连麦状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TurnOffMic: int
        :param AudioQuality: 高音质模式。可以有以下取值： 0 不开启高音质（默认值） 1 开启高音质
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioQuality: int
        :param DisableRecord: 上课后是否禁止自动录制。可以有以下取值： 0 不禁止录制（自动开启录制，默认值） 1 禁止录制 注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableRecord: int
        :param Assistants: 助教Id列表。通过[注册用户]接口获取的UserId。
注意：此字段可能返回 null，表示取不到有效值。
        :type Assistants: list of str
        :param RTCAudienceNumber: rtc人数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RTCAudienceNumber: int
        :param AudienceType: 观看类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudienceType: int
        :param RecordLayout: 录制布局。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLayout: int
        """
        self.Name = None
        self.StartTime = None
        self.EndTime = None
        self.Resolution = None
        self.MaxMicNumber = None
        self.SubType = None
        self.TeacherId = None
        self.AutoMic = None
        self.TurnOffMic = None
        self.AudioQuality = None
        self.DisableRecord = None
        self.Assistants = None
        self.RTCAudienceNumber = None
        self.AudienceType = None
        self.RecordLayout = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Resolution = params.get("Resolution")
        self.MaxMicNumber = params.get("MaxMicNumber")
        self.SubType = params.get("SubType")
        self.TeacherId = params.get("TeacherId")
        self.AutoMic = params.get("AutoMic")
        self.TurnOffMic = params.get("TurnOffMic")
        self.AudioQuality = params.get("AudioQuality")
        self.DisableRecord = params.get("DisableRecord")
        self.Assistants = params.get("Assistants")
        self.RTCAudienceNumber = params.get("RTCAudienceNumber")
        self.AudienceType = params.get("AudienceType")
        self.RecordLayout = params.get("RecordLayout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneItem(AbstractModel):
    """场景配置

    """


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


class SetWatermarkRequest(AbstractModel):
    """SetWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        :param TeacherUrl: 老师视频区域的水印参数地址，设置为空字符串表示删除
        :type TeacherUrl: str
        :param BoardUrl: 白板视频区域的水印参数地址，设置为空字符串表示删除
        :type BoardUrl: str
        :param VideoUrl: 视频默认图片（在没有视频流的时候显示），设置为空字符串表示删除
        :type VideoUrl: str
        :param BoardW: 白板区域水印的宽度，取值:0-100，默认为0，表示区域X方向的百分比
        :type BoardW: float
        :param BoardH: 白板区域水印的高度，取值:0-100，默认为0, 表示区域Y方向的百分比
        :type BoardH: float
        :param BoardX: 白板区域水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type BoardX: float
        :param BoardY: 白板区域水印Y偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type BoardY: float
        :param TeacherW: 老师视频区域水印的宽度，取值:0-100，默认为0，表示区域X方向的百分比
        :type TeacherW: float
        :param TeacherH: 老师视频区域水印的高度，取值:0-100，默认为0, 表示区域Y方向的百分比
        :type TeacherH: float
        :param TeacherX: 老师视频区域水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type TeacherX: float
        :param TeacherY: 老师视频区域水印Y偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type TeacherY: float
        :param Text: 文字水印内容，设置为空字符串表示删除
        :type Text: str
        :param TextColor: 文字水印颜色
        :type TextColor: str
        """
        self.SdkAppId = None
        self.TeacherUrl = None
        self.BoardUrl = None
        self.VideoUrl = None
        self.BoardW = None
        self.BoardH = None
        self.BoardX = None
        self.BoardY = None
        self.TeacherW = None
        self.TeacherH = None
        self.TeacherX = None
        self.TeacherY = None
        self.Text = None
        self.TextColor = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TeacherUrl = params.get("TeacherUrl")
        self.BoardUrl = params.get("BoardUrl")
        self.VideoUrl = params.get("VideoUrl")
        self.BoardW = params.get("BoardW")
        self.BoardH = params.get("BoardH")
        self.BoardX = params.get("BoardX")
        self.BoardY = params.get("BoardY")
        self.TeacherW = params.get("TeacherW")
        self.TeacherH = params.get("TeacherH")
        self.TeacherX = params.get("TeacherX")
        self.TeacherY = params.get("TeacherY")
        self.Text = params.get("Text")
        self.TextColor = params.get("TextColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWatermarkResponse(AbstractModel):
    """SetWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TextMarkConfig(AbstractModel):
    """文字水印配置

    """

    def __init__(self):
        r"""
        :param Text: 文字水印内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Color: 文字水印颜色
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: str
        """
        self.Text = None
        self.Color = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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


class UserInfo(AbstractModel):
    """用户信息结构体

    """

    def __init__(self):
        r"""
        :param SdkAppId: 应用Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppId: int
        :param UserId: 用户Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param Name: 用户昵称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Avatar: 用户头像Url。
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        """
        self.SdkAppId = None
        self.UserId = None
        self.Name = None
        self.Avatar = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkConfig(AbstractModel):
    """水印配置

    """

    def __init__(self):
        r"""
        :param Url: 水印图片的url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Width: 水印宽。为比例值
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: float
        :param Height: 水印高。为比例值
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: float
        :param LocationX: 水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationX: float
        :param LocationY: 水印Y偏移, 取值:0-100, 表示区域Y方向的百分比。比如50，则表示位于Y轴中间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationY: float
        """
        self.Url = None
        self.Width = None
        self.Height = None
        self.LocationX = None
        self.LocationY = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        