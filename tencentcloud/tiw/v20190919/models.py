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


class ApplicationItem(AbstractModel):
    """白板应用

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param _AppName: 应用名
        :type AppName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _TagList: 标签列表
        :type TagList: list of Tag
        """
        self._SdkAppId = None
        self._AppName = None
        self._CreateTime = None
        self._TagList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AppName = params.get("AppName")
        self._CreateTime = params.get("CreateTime")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTiwTrialRequest(AbstractModel):
    """ApplyTiwTrial请求参数结构体

    """


class ApplyTiwTrialResponse(AbstractModel):
    """ApplyTiwTrial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AuthParam(AbstractModel):
    """鉴权参数

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserSig: 用户ID对应的签名
        :type UserSig: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._UserSig = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Canvas(AbstractModel):
    """混流画布参数

    """

    def __init__(self):
        r"""
        :param _LayoutParams: 混流画布宽高配置
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param _BackgroundColor: 背景颜色，默认为黑色，格式为RGB格式，如红色为"#FF0000"
        :type BackgroundColor: str
        """
        self._LayoutParams = None
        self._BackgroundColor = None

    @property
    def LayoutParams(self):
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def BackgroundColor(self):
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self._LayoutParams = LayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        self._BackgroundColor = params.get("BackgroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Concat(AbstractModel):
    """实时录制视频拼接参数

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启拼接功能
在开启了视频拼接功能的情况下，实时录制服务会把同一个用户因为暂停导致的多段视频拼接成一个视频
        :type Enabled: bool
        :param _Image: 视频拼接时使用的垫片图片下载地址，不填默认用全黑的图片进行视频垫片
        :type Image: str
        """
        self._Enabled = None
        self._Image = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Image = params.get("Image")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationRequest(AbstractModel):
    """CreateApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param _AppName: App名字
        :type AppName: str
        :param _SKey: 创建IM应用需要的SKey
        :type SKey: str
        :param _TinyId: 创建IM应用需要的TinyId
        :type TinyId: str
        :param _TagList: 需要绑定的标签列表
        :type TagList: list of Tag
        """
        self._SdkAppId = None
        self._AppName = None
        self._SKey = None
        self._TinyId = None
        self._TagList = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def SKey(self):
        return self._SKey

    @SKey.setter
    def SKey(self, SKey):
        self._SKey = SKey

    @property
    def TinyId(self):
        return self._TinyId

    @TinyId.setter
    def TinyId(self, TinyId):
        self._TinyId = TinyId

    @property
    def TagList(self):
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AppName = params.get("AppName")
        self._SKey = params.get("SKey")
        self._TinyId = params.get("TinyId")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 客户的AppId
        :type AppId: int
        :param _AppName: App名字
        :type AppName: str
        :param _SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._AppName = None
        self._SdkAppId = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppName = params.get("AppName")
        self._SdkAppId = params.get("SdkAppId")
        self._RequestId = params.get("RequestId")


class CreateOfflineRecordRequest(AbstractModel):
    """CreateOfflineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _RoomId: 录制任务对应的房间号
        :type RoomId: int
        :param _GroupId: 录制任务对应的群组Id
        :type GroupId: str
        :param _MixStream: 混流参数配置
目前课后录制暂未支持自定义混流布局Custom参数
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param _Whiteboard: 白板参数配置
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._GroupId = None
        self._MixStream = None
        self._Whiteboard = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MixStream(self):
        return self._MixStream

    @MixStream.setter
    def MixStream(self, MixStream):
        self._MixStream = MixStream

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        if params.get("MixStream") is not None:
            self._MixStream = MixStream()
            self._MixStream._deserialize(params.get("MixStream"))
        if params.get("Whiteboard") is not None:
            self._Whiteboard = Whiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOfflineRecordResponse(AbstractModel):
    """CreateOfflineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreatePPTCheckTaskRequest(AbstractModel):
    """CreatePPTCheckTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Url: 经过URL编码后的PPT文件地址。URL 编码会将字符转换为可通过因特网传输的格式，例如文档地址为http://example.com/测试.pptx，经过URL编码之后为http://example.com/%E6%B5%8B%E8%AF%95.pptx。为了提高URL解析的成功率，请对URL进行编码。
        :type Url: str
        :param _AutoHandleUnsupportedElement: 是否对不支持元素开启自动处理的功能。默认不开启。

在开启自动处理的情况下，会自动进行如下处理：
1. 墨迹：移除不支持的墨迹（比如使用WPS画的）
2. 自动翻页：移除PPT上所有的自动翻页设置，并设置为单击鼠标翻页
3. 已损坏音视频：移除PPT上对损坏音视频的引用
        :type AutoHandleUnsupportedElement: bool
        """
        self._SdkAppId = None
        self._Url = None
        self._AutoHandleUnsupportedElement = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AutoHandleUnsupportedElement(self):
        return self._AutoHandleUnsupportedElement

    @AutoHandleUnsupportedElement.setter
    def AutoHandleUnsupportedElement(self, AutoHandleUnsupportedElement):
        self._AutoHandleUnsupportedElement = AutoHandleUnsupportedElement


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Url = params.get("Url")
        self._AutoHandleUnsupportedElement = params.get("AutoHandleUnsupportedElement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePPTCheckTaskResponse(AbstractModel):
    """CreatePPTCheckTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 检测任务的唯一标识Id，用于查询该任务的进度以及检测结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateSnapshotTaskRequest(AbstractModel):
    """CreateSnapshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Whiteboard: 白板相关参数
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.SnapshotWhiteboard`
        :param _SdkAppId: 白板房间 `SdkAppId`
        :type SdkAppId: int
        :param _RoomId: 白板房间号
        :type RoomId: int
        :param _CallbackURL: 白板板书生成结果通知回调地址
        :type CallbackURL: str
        :param _COS: 白板板书文件 `COS` 存储参数， 不填默认存储在公共存储桶，公共存储桶的数据仅保存3天
        :type COS: :class:`tencentcloud.tiw.v20190919.models.SnapshotCOS`
        :param _SnapshotMode: 白板板书生成模式，默认为 `AllMarks`。取值说明如下：

`AllMarks` - 全量模式，即对于客户端每一次调用 `addSnapshotMark` 接口打上的白板板书生成标志全部都会生成对应的白板板书图片。

`LatestMarksOnly` - 单页去重模式，即对于客户端在同一页白板上多次调用 `addSnapshotMark` 打上的白板板书生成标志仅保留最新一次标志来生成对应白板页的白板板书图片。

（**注意：`LatestMarksOnly` 模式只有客户端使用v2.6.8及以上版本的白板SDK调用 `addSnapshotMark` 时才生效，否则即使在调用本API是指定了 `LatestMarksOnly` 模式，服务后台会使用默认的 `AllMarks` 模式生成白板板书**）
        :type SnapshotMode: str
        """
        self._Whiteboard = None
        self._SdkAppId = None
        self._RoomId = None
        self._CallbackURL = None
        self._COS = None
        self._SnapshotMode = None

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def CallbackURL(self):
        return self._CallbackURL

    @CallbackURL.setter
    def CallbackURL(self, CallbackURL):
        self._CallbackURL = CallbackURL

    @property
    def COS(self):
        return self._COS

    @COS.setter
    def COS(self, COS):
        self._COS = COS

    @property
    def SnapshotMode(self):
        return self._SnapshotMode

    @SnapshotMode.setter
    def SnapshotMode(self, SnapshotMode):
        self._SnapshotMode = SnapshotMode


    def _deserialize(self, params):
        if params.get("Whiteboard") is not None:
            self._Whiteboard = SnapshotWhiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._CallbackURL = params.get("CallbackURL")
        if params.get("COS") is not None:
            self._COS = SnapshotCOS()
            self._COS._deserialize(params.get("COS"))
        self._SnapshotMode = params.get("SnapshotMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotTaskResponse(AbstractModel):
    """CreateSnapshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 白板板书生成任务ID，只有任务创建成功的时候才会返回此字段
        :type TaskID: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskID = None
        self._RequestId = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._RequestId = params.get("RequestId")


class CreateTranscodeRequest(AbstractModel):
    """CreateTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Url: 经过URL编码后的转码文件地址。URL 编码会将字符转换为可通过因特网传输的格式，比如文档地址为http://example.com/测试.pdf，经过URL编码之后为http://example.com/%E6%B5%8B%E8%AF%95.pdf。为了提高URL解析的成功率，请对URL进行编码。
        :type Url: str
        :param _IsStaticPPT: 是否为静态PPT，默认为False；
如果IsStaticPPT为False，后缀名为.ppt或.pptx的文档会动态转码成HTML5页面，其他格式的文档会静态转码成图片；如果IsStaticPPT为True，所有格式的文档会静态转码成图片；
        :type IsStaticPPT: bool
        :param _MinResolution: 注意: 该参数已废弃, 请使用最新的 [云API SDK](https://cloud.tencent.com/document/api/1137/40060#SDK) ，使用 MinScaleResolution字段传递分辨率

转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率

示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
        :type MinResolution: str
        :param _ThumbnailResolution: 动态PPT转码可以为文件生成该分辨率的缩略图，不传、传空字符串或分辨率格式错误则不生成缩略图，分辨率格式同MinResolution
        :type ThumbnailResolution: str
        :param _CompressFileType: 转码文件压缩格式，不传、传空字符串或不是指定的格式则不生成压缩文件，目前支持如下压缩格式：

zip： 生成`.zip`压缩包
tar.gz： 生成`.tar.gz`压缩包
        :type CompressFileType: str
        :param _ExtraData: 内部参数
        :type ExtraData: str
        :param _Priority: 文档转码优先级， 只有对于PPT动态转码生效，支持填入以下值：<br/>
- low: 低优先级转码，对于动态转码，能支持500MB（下载超时时间10分钟）以及2000页文档，但资源有限可能会有比较长时间的排队，请酌情使用该功能。<br/>
- 不填表示正常优先级转码，支持200MB文件（下载超时时间2分钟），500页以内的文档进行转码
<br/>
注意：对于PDF等静态文件转码，无论是正常优先级或者低优先级，最大只能支持200MB
        :type Priority: str
        :param _MinScaleResolution: 转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率。
分辨率越高，效果越清晰，转出来的图片资源体积会越大，课件加载耗时会变长，请根据实际使用场景配置此参数。

示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
        :type MinScaleResolution: str
        :param _AutoHandleUnsupportedElement: 是否对不支持元素开启自动处理的功能。默认不开启。

在开启自动处理的情况下，会自动进行如下处理：
1. 墨迹：移除不支持的墨迹（比如使用WPS画的）
2. 自动翻页：移除PPT上所有的自动翻页设置，并设置为单击鼠标翻页
3. 已损坏音视频：移除PPT上对损坏音视频的引用
        :type AutoHandleUnsupportedElement: bool
        """
        self._SdkAppId = None
        self._Url = None
        self._IsStaticPPT = None
        self._MinResolution = None
        self._ThumbnailResolution = None
        self._CompressFileType = None
        self._ExtraData = None
        self._Priority = None
        self._MinScaleResolution = None
        self._AutoHandleUnsupportedElement = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def IsStaticPPT(self):
        return self._IsStaticPPT

    @IsStaticPPT.setter
    def IsStaticPPT(self, IsStaticPPT):
        self._IsStaticPPT = IsStaticPPT

    @property
    def MinResolution(self):
        return self._MinResolution

    @MinResolution.setter
    def MinResolution(self, MinResolution):
        self._MinResolution = MinResolution

    @property
    def ThumbnailResolution(self):
        return self._ThumbnailResolution

    @ThumbnailResolution.setter
    def ThumbnailResolution(self, ThumbnailResolution):
        self._ThumbnailResolution = ThumbnailResolution

    @property
    def CompressFileType(self):
        return self._CompressFileType

    @CompressFileType.setter
    def CompressFileType(self, CompressFileType):
        self._CompressFileType = CompressFileType

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def MinScaleResolution(self):
        return self._MinScaleResolution

    @MinScaleResolution.setter
    def MinScaleResolution(self, MinScaleResolution):
        self._MinScaleResolution = MinScaleResolution

    @property
    def AutoHandleUnsupportedElement(self):
        return self._AutoHandleUnsupportedElement

    @AutoHandleUnsupportedElement.setter
    def AutoHandleUnsupportedElement(self, AutoHandleUnsupportedElement):
        self._AutoHandleUnsupportedElement = AutoHandleUnsupportedElement


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Url = params.get("Url")
        self._IsStaticPPT = params.get("IsStaticPPT")
        self._MinResolution = params.get("MinResolution")
        self._ThumbnailResolution = params.get("ThumbnailResolution")
        self._CompressFileType = params.get("CompressFileType")
        self._ExtraData = params.get("ExtraData")
        self._Priority = params.get("Priority")
        self._MinScaleResolution = params.get("MinScaleResolution")
        self._AutoHandleUnsupportedElement = params.get("AutoHandleUnsupportedElement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeResponse(AbstractModel):
    """CreateTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 文档转码任务的唯一标识Id，用于查询该任务的进度以及转码结果
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateVideoGenerationTaskRequest(AbstractModel):
    """CreateVideoGenerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OnlineRecordTaskId: 录制任务的TaskId
        :type OnlineRecordTaskId: str
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Whiteboard: 视频生成的白板参数，例如白板宽高等。

此参数与开始录制接口提供的Whiteboard参数互斥，在本接口与开始录制接口都提供了Whiteboard参数时，优先使用本接口指定的Whiteboard参数进行视频生成，否则使用开始录制接口提供的Whiteboard参数进行视频生成。
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param _Concat: 视频拼接参数

此参数与开始录制接口提供的Concat参数互斥，在本接口与开始录制接口都提供了Concat参数时，优先使用本接口指定的Concat参数进行视频拼接，否则使用开始录制接口提供的Concat参数进行视频拼接。
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param _MixStream: 视频生成混流参数

此参数与开始录制接口提供的MixStream参数互斥，在本接口与开始录制接口都提供了MixStream参数时，优先使用本接口指定的MixStream参数进行视频混流，否则使用开始录制接口提供的MixStream参数进行视频拼混流。
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param _RecordControl: 视频生成控制参数，用于更精细地指定需要生成哪些流，某一路流是否禁用音频，是否只录制小画面等

此参数与开始录制接口提供的RecordControl参数互斥，在本接口与开始录制接口都提供了RecordControl参数时，优先使用本接口指定的RecordControl参数进行视频生成控制，否则使用开始录制接口提供的RecordControl参数进行视频拼生成控制。
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param _ExtraData: 内部参数
        :type ExtraData: str
        """
        self._OnlineRecordTaskId = None
        self._SdkAppId = None
        self._Whiteboard = None
        self._Concat = None
        self._MixStream = None
        self._RecordControl = None
        self._ExtraData = None

    @property
    def OnlineRecordTaskId(self):
        return self._OnlineRecordTaskId

    @OnlineRecordTaskId.setter
    def OnlineRecordTaskId(self, OnlineRecordTaskId):
        self._OnlineRecordTaskId = OnlineRecordTaskId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def Concat(self):
        return self._Concat

    @Concat.setter
    def Concat(self, Concat):
        self._Concat = Concat

    @property
    def MixStream(self):
        return self._MixStream

    @MixStream.setter
    def MixStream(self, MixStream):
        self._MixStream = MixStream

    @property
    def RecordControl(self):
        return self._RecordControl

    @RecordControl.setter
    def RecordControl(self, RecordControl):
        self._RecordControl = RecordControl

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData


    def _deserialize(self, params):
        self._OnlineRecordTaskId = params.get("OnlineRecordTaskId")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Whiteboard") is not None:
            self._Whiteboard = Whiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("Concat") is not None:
            self._Concat = Concat()
            self._Concat._deserialize(params.get("Concat"))
        if params.get("MixStream") is not None:
            self._MixStream = MixStream()
            self._MixStream._deserialize(params.get("MixStream"))
        if params.get("RecordControl") is not None:
            self._RecordControl = RecordControl()
            self._RecordControl._deserialize(params.get("RecordControl"))
        self._ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoGenerationTaskResponse(AbstractModel):
    """CreateVideoGenerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 视频生成的任务Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CustomLayout(AbstractModel):
    """自定义混流布局参数

    """

    def __init__(self):
        r"""
        :param _Canvas: 混流画布参数
        :type Canvas: :class:`tencentcloud.tiw.v20190919.models.Canvas`
        :param _InputStreamList: 流布局参数，每路流的布局不能超出画布区域
        :type InputStreamList: list of StreamLayout
        """
        self._Canvas = None
        self._InputStreamList = None

    @property
    def Canvas(self):
        return self._Canvas

    @Canvas.setter
    def Canvas(self, Canvas):
        self._Canvas = Canvas

    @property
    def InputStreamList(self):
        return self._InputStreamList

    @InputStreamList.setter
    def InputStreamList(self, InputStreamList):
        self._InputStreamList = InputStreamList


    def _deserialize(self, params):
        if params.get("Canvas") is not None:
            self._Canvas = Canvas()
            self._Canvas._deserialize(params.get("Canvas"))
        if params.get("InputStreamList") is not None:
            self._InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = StreamLayout()
                obj._deserialize(item)
                self._InputStreamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataItem(AbstractModel):
    """画图数据，Time/Value/Details

    """

    def __init__(self):
        r"""
        :param _Time: 时间
按月格式yyyy-mm
按天格式yyyy-mm-dd
按分钟格式 yyyy-mm-dd HH:MM:SS
        :type Time: str
        :param _Value: 画图所需要的值
        :type Value: int
        :param _Details: 各个具体指标的详情
        :type Details: list of Detail
        """
        self._Time = None
        self._Value = None
        self._Details = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = Detail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceRequest(AbstractModel):
    """DescribeAPIService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 目前支持的Service为cos:GetService，cdn:DescribeDomainsConfig
        :type Service: str
        :param _Data: JSON格式的请求参数
        :type Data: str
        """
        self._Service = None
        self._Data = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIServiceResponse(AbstractModel):
    """DescribeAPIService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResponseData: Json格式的响应数据
        :type ResponseData: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResponseData = params.get("ResponseData")
        self._RequestId = params.get("RequestId")


class DescribeApplicationInfosRequest(AbstractModel):
    """DescribeApplicationInfos请求参数结构体

    """


class DescribeApplicationInfosResponse(AbstractModel):
    """DescribeApplicationInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationInfos: 应用列表
        :type ApplicationInfos: list of ApplicationItem
        :param _AllOption: 是否包含所有的应用，0-不包含，1-包含
        :type AllOption: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationInfos = None
        self._AllOption = None
        self._RequestId = None

    @property
    def ApplicationInfos(self):
        return self._ApplicationInfos

    @ApplicationInfos.setter
    def ApplicationInfos(self, ApplicationInfos):
        self._ApplicationInfos = ApplicationInfos

    @property
    def AllOption(self):
        return self._AllOption

    @AllOption.setter
    def AllOption(self, AllOption):
        self._AllOption = AllOption

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ApplicationInfos") is not None:
            self._ApplicationInfos = []
            for item in params.get("ApplicationInfos"):
                obj = ApplicationItem()
                obj._deserialize(item)
                self._ApplicationInfos.append(obj)
        self._AllOption = params.get("AllOption")
        self._RequestId = params.get("RequestId")


class DescribeApplicationUsageRequest(AbstractModel):
    """DescribeApplicationUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 用量开始时间（包括该时间点）
        :type BeginTime: str
        :param _EndTime: 用量结束时间（不包括该时间点）
        :type EndTime: str
        :param _SubProduct: 白板子产品名
        :type SubProduct: str
        :param _TimeLevel: 时间跨度单位
- MONTHLY：月
- DAILY：天
- MINUTELY：分钟
        :type TimeLevel: str
        :param _SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param _IsWeighted: true: 返回加权求和后的用量数据
false: 返回原始用量数据
        :type IsWeighted: bool
        """
        self._BeginTime = None
        self._EndTime = None
        self._SubProduct = None
        self._TimeLevel = None
        self._SdkAppId = None
        self._IsWeighted = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def TimeLevel(self):
        return self._TimeLevel

    @TimeLevel.setter
    def TimeLevel(self, TimeLevel):
        self._TimeLevel = TimeLevel

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def IsWeighted(self):
        return self._IsWeighted

    @IsWeighted.setter
    def IsWeighted(self, IsWeighted):
        self._IsWeighted = IsWeighted


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._SubProduct = params.get("SubProduct")
        self._TimeLevel = params.get("TimeLevel")
        self._SdkAppId = params.get("SdkAppId")
        self._IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationUsageResponse(AbstractModel):
    """DescribeApplicationUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 画图所需的用量数据
        :type Data: list of DataItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DataItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBoardSDKLogRequest(AbstractModel):
    """DescribeBoardSDKLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param _RoomId: 需要查询日志的白板房间号
        :type RoomId: str
        :param _UserId: 需要查询日志的用户ID
        :type UserId: str
        :param _TimeRange: 查询时间段，Unix时间戳，单位毫秒，第一个值为开始时间戳，第二个值为结束时间
        :type TimeRange: list of int
        :param _AggregationInterval: 聚合日志条数查询的桶的时间范围，如5m, 1h, 4h等
        :type AggregationInterval: str
        :param _Query: 额外的查询条件
        :type Query: str
        :param _Ascending: 是否按时间升序排列
        :type Ascending: bool
        :param _Context: 用于递归拉取的上下文Key，在上一次请求中返回
        :type Context: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._TimeRange = None
        self._AggregationInterval = None
        self._Query = None
        self._Ascending = None
        self._Context = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def AggregationInterval(self):
        return self._AggregationInterval

    @AggregationInterval.setter
    def AggregationInterval(self, AggregationInterval):
        self._AggregationInterval = AggregationInterval

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Ascending(self):
        return self._Ascending

    @Ascending.setter
    def Ascending(self, Ascending):
        self._Ascending = Ascending

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._TimeRange = params.get("TimeRange")
        self._AggregationInterval = params.get("AggregationInterval")
        self._Query = params.get("Query")
        self._Ascending = params.get("Ascending")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBoardSDKLogResponse(AbstractModel):
    """DescribeBoardSDKLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总共能查到日志条数
        :type Total: int
        :param _Sources: 日志详细内容
        :type Sources: list of str
        :param _Buckets: 按时间段聚合后每个时间段的日志条数
        :type Buckets: list of str
        :param _Context: 用于递归拉取的上下文Key，下一次请求的时候带上
        :type Context: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Sources = None
        self._Buckets = None
        self._Context = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Sources(self):
        return self._Sources

    @Sources.setter
    def Sources(self, Sources):
        self._Sources = Sources

    @property
    def Buckets(self):
        return self._Buckets

    @Buckets.setter
    def Buckets(self, Buckets):
        self._Buckets = Buckets

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Sources = params.get("Sources")
        self._Buckets = params.get("Buckets")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeIMApplicationsRequest(AbstractModel):
    """DescribeIMApplications请求参数结构体

    """


class DescribeIMApplicationsResponse(AbstractModel):
    """DescribeIMApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeOfflineRecordCallbackRequest(AbstractModel):
    """DescribeOfflineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineRecordCallbackResponse(AbstractModel):
    """DescribeOfflineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeOfflineRecordRequest(AbstractModel):
    """DescribeOfflineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 课后录制任务的Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineRecordResponse(AbstractModel):
    """DescribeOfflineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeOnlineRecordCallbackRequest(AbstractModel):
    """DescribeOnlineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordCallbackResponse(AbstractModel):
    """DescribeOnlineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Callback: 实时录制事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param _CallbackKey: 实时录制回调鉴权密钥
        :type CallbackKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeOnlineRecordRequest(AbstractModel):
    """DescribeOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 实时录制任务Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOnlineRecordResponse(AbstractModel):
    """DescribeOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FinishReason: 录制结束原因，
- AUTO: 房间内长时间没有音视频上行及白板操作导致自动停止录制
- USER_CALL: 主动调用了停止录制接口
- EXCEPTION: 录制异常结束
- FORCE_STOP: 强制停止录制，一般是因为暂停超过90分钟或者录制总时长超过24小时。
        :type FinishReason: str
        :param _TaskId: 需要查询结果的录制任务Id
        :type TaskId: str
        :param _Status: 录制任务状态
- PREPARED: 表示录制正在准备中（进房/启动录制服务等操作）
- RECORDING: 表示录制已开始
- PAUSED: 表示录制已暂停
- STOPPED: 表示录制已停止，正在处理并上传视频
- FINISHED: 表示视频处理并上传完成，成功生成录制结果
        :type Status: str
        :param _RoomId: 房间号
        :type RoomId: int
        :param _GroupId: 白板的群组 Id
        :type GroupId: str
        :param _RecordUserId: 录制用户Id
        :type RecordUserId: str
        :param _RecordStartTime: 实际开始录制时间，Unix 时间戳，单位秒
        :type RecordStartTime: int
        :param _RecordStopTime: 实际停止录制时间，Unix 时间戳，单位秒
        :type RecordStopTime: int
        :param _TotalTime: 回放视频总时长（单位：毫秒）
        :type TotalTime: int
        :param _ExceptionCnt: 录制过程中出现异常的次数
        :type ExceptionCnt: int
        :param _OmittedDurations: 拼接视频中被忽略的时间段，只有开启视频拼接功能的时候，这个参数才是有效的
        :type OmittedDurations: list of OmittedDuration
        :param _VideoInfos: 录制视频列表
        :type VideoInfos: list of VideoInfo
        :param _ReplayUrl: 回放URL，需配合信令播放器使用。此字段仅适用于`视频生成模式`
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplayUrl: str
        :param _Interrupts: 视频流在录制过程中断流次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Interrupts: list of Interrupt
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FinishReason = None
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._GroupId = None
        self._RecordUserId = None
        self._RecordStartTime = None
        self._RecordStopTime = None
        self._TotalTime = None
        self._ExceptionCnt = None
        self._OmittedDurations = None
        self._VideoInfos = None
        self._ReplayUrl = None
        self._Interrupts = None
        self._RequestId = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RecordUserId(self):
        return self._RecordUserId

    @RecordUserId.setter
    def RecordUserId(self, RecordUserId):
        self._RecordUserId = RecordUserId

    @property
    def RecordStartTime(self):
        return self._RecordStartTime

    @RecordStartTime.setter
    def RecordStartTime(self, RecordStartTime):
        self._RecordStartTime = RecordStartTime

    @property
    def RecordStopTime(self):
        return self._RecordStopTime

    @RecordStopTime.setter
    def RecordStopTime(self, RecordStopTime):
        self._RecordStopTime = RecordStopTime

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def OmittedDurations(self):
        return self._OmittedDurations

    @OmittedDurations.setter
    def OmittedDurations(self, OmittedDurations):
        self._OmittedDurations = OmittedDurations

    @property
    def VideoInfos(self):
        return self._VideoInfos

    @VideoInfos.setter
    def VideoInfos(self, VideoInfos):
        self._VideoInfos = VideoInfos

    @property
    def ReplayUrl(self):
        return self._ReplayUrl

    @ReplayUrl.setter
    def ReplayUrl(self, ReplayUrl):
        self._ReplayUrl = ReplayUrl

    @property
    def Interrupts(self):
        return self._Interrupts

    @Interrupts.setter
    def Interrupts(self, Interrupts):
        self._Interrupts = Interrupts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._RecordUserId = params.get("RecordUserId")
        self._RecordStartTime = params.get("RecordStartTime")
        self._RecordStopTime = params.get("RecordStopTime")
        self._TotalTime = params.get("TotalTime")
        self._ExceptionCnt = params.get("ExceptionCnt")
        if params.get("OmittedDurations") is not None:
            self._OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self._OmittedDurations.append(obj)
        if params.get("VideoInfos") is not None:
            self._VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self._VideoInfos.append(obj)
        self._ReplayUrl = params.get("ReplayUrl")
        if params.get("Interrupts") is not None:
            self._Interrupts = []
            for item in params.get("Interrupts"):
                obj = Interrupt()
                obj._deserialize(item)
                self._Interrupts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePPTCheckCallbackRequest(AbstractModel):
    """DescribePPTCheckCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePPTCheckCallbackResponse(AbstractModel):
    """DescribePPTCheckCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Callback: 回调地址
        :type Callback: str
        :param _CallbackKey: 回调鉴权密钥
        :type CallbackKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribePPTCheckRequest(AbstractModel):
    """DescribePPTCheck请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 任务的唯一标识Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePPTCheckResponse(AbstractModel):
    """DescribePPTCheck返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务的唯一标识Id
        :type TaskId: str
        :param _IsOK: PPT文件是否正常
        :type IsOK: bool
        :param _ResultUrl: 修复后的PPT URL，只有创建任务时参数AutoHandleUnsupportedElement=true，才返回此参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultUrl: str
        :param _Slides: 错误PPT页面列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Slides: list of PPTErrSlide
        :param _Status: 任务的当前状态 - QUEUED: 正在排队等待 - PROCESSING: 执行中 - FINISHED: 执行完成	
        :type Status: str
        :param _Progress: 当前进度,取值范围为0~100
        :type Progress: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._IsOK = None
        self._ResultUrl = None
        self._Slides = None
        self._Status = None
        self._Progress = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def IsOK(self):
        return self._IsOK

    @IsOK.setter
    def IsOK(self, IsOK):
        self._IsOK = IsOK

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def Slides(self):
        return self._Slides

    @Slides.setter
    def Slides(self, Slides):
        self._Slides = Slides

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._IsOK = params.get("IsOK")
        self._ResultUrl = params.get("ResultUrl")
        if params.get("Slides") is not None:
            self._Slides = []
            for item in params.get("Slides"):
                obj = PPTErrSlide()
                obj._deserialize(item)
                self._Slides.append(obj)
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._RequestId = params.get("RequestId")


class DescribePostpaidUsageRequest(AbstractModel):
    """DescribePostpaidUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 开始时间
        :type BeginTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._BeginTime = None
        self._EndTime = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePostpaidUsageResponse(AbstractModel):
    """DescribePostpaidUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeQualityMetricsRequest(AbstractModel):
    """DescribeQualityMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param _StartTime: 开始时间，Unix时间戳，单位秒，时间跨度不能超过7天
        :type StartTime: int
        :param _EndTime: 结束时间，Unix时间戳，单位秒，时间跨度不能超过7天
        :type EndTime: int
        :param _Metric: 查询的指标，目前支持以下值
  - image_load_total_count: 图片加载总数（单位，次）
  - image_load_fail_count: 图片加载失败数量（单位，次）
  - image_load_success_rate: 图片加载成功率（百分比）
  - ppt_load_total_count: PPT加载总数（单位，次）
  - ppt_load_fail_count: PPT加载失败总数（单位，次）
  - ppt_load_success_rate: PPT加载成功率（单位，百分比）
  - verify_sdk_total_count: 白板鉴权总次数（单位，次）
  - verify_sdk_fail_count: 白板鉴权失败次数（单位，次）
  - verify_sdk_success_rate: 白板鉴权成功率（单位，百分比）
  - verify_sdk_in_one_second_rate: 白板鉴权秒开率（单位，百分比）
  - verify_sdk_cost_avg: 白板鉴权耗时平均时间（单位，毫秒）
        :type Metric: str
        :param _Interval: 聚合的时间维度，目前只支持1小时，输入值为"1h"
        :type Interval: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Interval = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQualityMetricsResponse(AbstractModel):
    """DescribeQualityMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Metric: 输入的查询指标
        :type Metric: str
        :param _Content: 时间序列
        :type Content: list of TimeValue
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Metric = None
        self._Content = None
        self._RequestId = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordSearchRequest(AbstractModel):
    """DescribeRecordSearch请求参数结构体

    """


class DescribeRecordSearchResponse(AbstractModel):
    """DescribeRecordSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordTaskSet: 录制任务搜索结果集合
        :type RecordTaskSet: list of RecordTaskSearchResult
        :param _TotalCount: 录制总任务数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RecordTaskSet(self):
        return self._RecordTaskSet

    @RecordTaskSet.setter
    def RecordTaskSet(self, RecordTaskSet):
        self._RecordTaskSet = RecordTaskSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RecordTaskSet") is not None:
            self._RecordTaskSet = []
            for item in params.get("RecordTaskSet"):
                obj = RecordTaskSearchResult()
                obj._deserialize(item)
                self._RecordTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRoomListRequest(AbstractModel):
    """DescribeRoomList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param _TimeRange: 查询时间段，Unix时间戳，单位毫秒，第一个值为开始时间戳，第二个值为结束时间
        :type TimeRange: list of int
        :param _Query: 额外的查询条件
        :type Query: str
        :param _MaxSize: 返回最大的数据条数，默认1000
        :type MaxSize: int
        """
        self._SdkAppId = None
        self._TimeRange = None
        self._Query = None
        self._MaxSize = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TimeRange = params.get("TimeRange")
        self._Query = params.get("Query")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomListResponse(AbstractModel):
    """DescribeRoomList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomList: 白板房间列表
        :type RoomList: list of RoomListItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoomList = None
        self._RequestId = None

    @property
    def RoomList(self):
        return self._RoomList

    @RoomList.setter
    def RoomList(self, RoomList):
        self._RoomList = RoomList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RoomList") is not None:
            self._RoomList = []
            for item in params.get("RoomList"):
                obj = RoomListItem()
                obj._deserialize(item)
                self._RoomList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunningTasksRequest(AbstractModel):
    """DescribeRunningTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppID: 应用的SdkAppID
        :type SdkAppID: int
        :param _TaskType: 指定需要获取的任务类型。
有效取值如下：
- TranscodeH5: 动态转码任务，文档转HTML5页面
- TranscodeJPG: 静态转码任务，文档转图片
- WhiteboardPush: 白板推流任务
- OnlineRecord: 实时录制任务
        :type TaskType: str
        :param _Offset: 分页获取时的任务偏移量，默认为0。
        :type Offset: int
        :param _Limit: 每次获取任务列表时最大获取任务数，默认值为100。
有效取值范围：[1, 500]
        :type Limit: int
        """
        self._SdkAppID = None
        self._TaskType = None
        self._Offset = None
        self._Limit = None

    @property
    def SdkAppID(self):
        return self._SdkAppID

    @SdkAppID.setter
    def SdkAppID(self, SdkAppID):
        self._SdkAppID = SdkAppID

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppID = params.get("SdkAppID")
        self._TaskType = params.get("TaskType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunningTasksResponse(AbstractModel):
    """DescribeRunningTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 当前正在执行中的任务总数
        :type Total: int
        :param _Tasks: 任务信息列表
        :type Tasks: list of RunningTaskItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Tasks = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Tasks(self):
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = RunningTaskItem()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotTaskRequest(AbstractModel):
    """DescribeSnapshotTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 查询任务ID
        :type TaskID: str
        :param _SdkAppId: 任务SdkAppId
        :type SdkAppId: int
        """
        self._TaskID = None
        self._SdkAppId = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotTaskResponse(AbstractModel):
    """DescribeSnapshotTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskID: str
        :param _Status: 任务状态
Running - 任务执行中
Finished - 任务已结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _CreateTime: 任务创建时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _FinishTime: 任务完成时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: int
        :param _Result: 任务结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tiw.v20190919.models.SnapshotResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskID = None
        self._Status = None
        self._CreateTime = None
        self._FinishTime = None
        self._Result = None
        self._RequestId = None

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def FinishTime(self):
        return self._FinishTime

    @FinishTime.setter
    def FinishTime(self, FinishTime):
        self._FinishTime = FinishTime

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._FinishTime = params.get("FinishTime")
        if params.get("Result") is not None:
            self._Result = SnapshotResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTIWDailyUsageRequest(AbstractModel):
    """DescribeTIWDailyUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 互动白板应用SdkAppId
        :type SdkAppId: int
        :param _SubProduct: 需要查询的子产品用量，支持传入以下值
- sp_tiw_board: 互动白板时长，单位为分钟
- sp_tiw_dt: 动态转码页数，单位页
- sp_tiw_st: 静态转码页数，单位页
- sp_tiw_ric: 实时录制时长，单位分钟

注意：动态转码以1:8的比例计算文档转码页数，静态转码以1:1的比例计算文档转码页数
        :type SubProduct: str
        :param _StartTime: 开始时间，格式YYYY-MM-DD，查询结果里包括该天数据
        :type StartTime: str
        :param _EndTime: 结束时间，格式YYYY-MM-DD，查询结果里包括该天数据，单次查询统计区间最多不能超过31天。
        :type EndTime: str
        """
        self._SdkAppId = None
        self._SubProduct = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWDailyUsageResponse(AbstractModel):
    """DescribeTIWDailyUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Usages: 指定区间指定产品的用量汇总
        :type Usages: list of UsageDataItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Usages = None
        self._RequestId = None

    @property
    def Usages(self):
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self._Usages = []
            for item in params.get("Usages"):
                obj = UsageDataItem()
                obj._deserialize(item)
                self._Usages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTIWRoomDailyUsageRequest(AbstractModel):
    """DescribeTIWRoomDailyUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 互动白板应用SdkAppId
        :type SdkAppId: int
        :param _SubProduct: 需要查询的子产品用量，支持传入以下值
- sp_tiw_board: 互动白板时长，单位为分钟
- sp_tiw_ric: 实时录制时长，单位分钟
        :type SubProduct: str
        :param _StartTime: 开始时间，格式YYYY-MM-DD，查询结果里包括该天数据
        :type StartTime: str
        :param _EndTime: 结束时间，格式YYYY-MM-DD，查询结果里包括该天数据，单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param _RoomIDs: 需要查询的房间ID列表，不填默认查询全部房间
        :type RoomIDs: list of int non-negative
        :param _Offset: 查询偏移量，默认为0
        :type Offset: int
        :param _Limit: 每次查询返回条目限制，默认为20
        :type Limit: int
        """
        self._SdkAppId = None
        self._SubProduct = None
        self._StartTime = None
        self._EndTime = None
        self._RoomIDs = None
        self._Offset = None
        self._Limit = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomIDs(self):
        return self._RoomIDs

    @RoomIDs.setter
    def RoomIDs(self, RoomIDs):
        self._RoomIDs = RoomIDs

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomIDs = params.get("RoomIDs")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTIWRoomDailyUsageResponse(AbstractModel):
    """DescribeTIWRoomDailyUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Usages: 指定区间指定产品的房间用量列表
        :type Usages: list of RoomUsageDataItem
        :param _Total: 用量列表总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Usages = None
        self._Total = None
        self._RequestId = None

    @property
    def Usages(self):
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self._Usages = []
            for item in params.get("Usages"):
                obj = RoomUsageDataItem()
                obj._deserialize(item)
                self._Usages.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeTranscodeByUrlRequest(AbstractModel):
    """DescribeTranscodeByUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Url: 经过URL编码后的转码文件地址。URL 编码会将字符转换为可通过因特网传输的格式，比如文档地址为http://example.com/测试.pdf，经过URL编码之后为http://example.com/%E6%B5%8B%E8%AF%95.pdf。为了提高URL解析的成功率，请对URL进行编码。	
        :type Url: str
        """
        self._SdkAppId = None
        self._Url = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeByUrlResponse(AbstractModel):
    """DescribeTranscodeByUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 转码的当前进度,取值范围为0~100
        :type Progress: int
        :param _Status: 任务的当前状态
- QUEUED: 正在排队等待转换
- PROCESSING: 转换中
- FINISHED: 转换完成
- EXCEPTION: 转换异常
        :type Status: str
        :param _TaskId: 转码任务的唯一标识Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Progress = None
        self._Status = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Progress = params.get("Progress")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeTranscodeCallbackRequest(AbstractModel):
    """DescribeTranscodeCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeCallbackResponse(AbstractModel):
    """DescribeTranscodeCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Callback: 文档转码回调地址
        :type Callback: str
        :param _CallbackKey: 文档转码回调鉴权密钥
        :type CallbackKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeTranscodeRequest(AbstractModel):
    """DescribeTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 文档转码任务的唯一标识Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeResponse(AbstractModel):
    """DescribeTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Pages: 文档的总页数
        :type Pages: int
        :param _Progress: 转码的当前进度,取值范围为0~100
        :type Progress: int
        :param _Resolution: 文档的分辨率
        :type Resolution: str
        :param _ResultUrl: 转码完成后结果的URL
动态转码：PPT转动态H5的链接
静态转码：文档每一页的图片URL前缀，比如，该URL前缀为`http://example.com/g0jb42ps49vtebjshilb/`，那么文档第1页的图片URL为
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它页以此类推
        :type ResultUrl: str
        :param _Status: 任务的当前状态
- QUEUED: 正在排队等待转换
- PROCESSING: 转换中
- FINISHED: 转换完成
        :type Status: str
        :param _TaskId: 转码任务的唯一标识Id
        :type TaskId: str
        :param _Title: 文档的文件名
        :type Title: str
        :param _ThumbnailUrl: 缩略图URL前缀，比如，该URL前缀为`http://example.com/g0jb42ps49vtebjshilb/ `，那么动态PPT第1页的缩略图URL为
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它页以此类推

如果发起文档转码请求参数中带了ThumbnailResolution参数，并且转码类型为动态转码，该参数不为空，其余情况该参数为空字符串
        :type ThumbnailUrl: str
        :param _ThumbnailResolution: 动态转码缩略图生成分辨率
        :type ThumbnailResolution: str
        :param _CompressFileUrl: 转码压缩文件下载的URL，如果发起文档转码请求参数中`CompressFileType`为空或者不是支持的压缩格式，该参数为空字符串
        :type CompressFileUrl: str
        :param _ResourceListUrl: 资源清单文件下载URL(内测体验)
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceListUrl: str
        :param _Ext: 文档制作方式(内测体验)
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        :param _CreateTime: 文档转码任务创建时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _AssignTime: 文档转码任务分配时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type AssignTime: int
        :param _FinishedTime: 文档转码任务完成时间，单位s
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishedTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Pages = None
        self._Progress = None
        self._Resolution = None
        self._ResultUrl = None
        self._Status = None
        self._TaskId = None
        self._Title = None
        self._ThumbnailUrl = None
        self._ThumbnailResolution = None
        self._CompressFileUrl = None
        self._ResourceListUrl = None
        self._Ext = None
        self._CreateTime = None
        self._AssignTime = None
        self._FinishedTime = None
        self._RequestId = None

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def ThumbnailUrl(self):
        return self._ThumbnailUrl

    @ThumbnailUrl.setter
    def ThumbnailUrl(self, ThumbnailUrl):
        self._ThumbnailUrl = ThumbnailUrl

    @property
    def ThumbnailResolution(self):
        return self._ThumbnailResolution

    @ThumbnailResolution.setter
    def ThumbnailResolution(self, ThumbnailResolution):
        self._ThumbnailResolution = ThumbnailResolution

    @property
    def CompressFileUrl(self):
        return self._CompressFileUrl

    @CompressFileUrl.setter
    def CompressFileUrl(self, CompressFileUrl):
        self._CompressFileUrl = CompressFileUrl

    @property
    def ResourceListUrl(self):
        return self._ResourceListUrl

    @ResourceListUrl.setter
    def ResourceListUrl(self, ResourceListUrl):
        self._ResourceListUrl = ResourceListUrl

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AssignTime(self):
        return self._AssignTime

    @AssignTime.setter
    def AssignTime(self, AssignTime):
        self._AssignTime = AssignTime

    @property
    def FinishedTime(self):
        return self._FinishedTime

    @FinishedTime.setter
    def FinishedTime(self, FinishedTime):
        self._FinishedTime = FinishedTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Pages = params.get("Pages")
        self._Progress = params.get("Progress")
        self._Resolution = params.get("Resolution")
        self._ResultUrl = params.get("ResultUrl")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._Title = params.get("Title")
        self._ThumbnailUrl = params.get("ThumbnailUrl")
        self._ThumbnailResolution = params.get("ThumbnailResolution")
        self._CompressFileUrl = params.get("CompressFileUrl")
        self._ResourceListUrl = params.get("ResourceListUrl")
        self._Ext = params.get("Ext")
        self._CreateTime = params.get("CreateTime")
        self._AssignTime = params.get("AssignTime")
        self._FinishedTime = params.get("FinishedTime")
        self._RequestId = params.get("RequestId")


class DescribeTranscodeSearchRequest(AbstractModel):
    """DescribeTranscodeSearch请求参数结构体

    """


class DescribeTranscodeSearchResponse(AbstractModel):
    """DescribeTranscodeSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TranscodeTaskSet: 转码任务搜索结果集合
        :type TranscodeTaskSet: list of TranscodeTaskSearchResult
        :param _TotalCount: 转码总任务数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TranscodeTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TranscodeTaskSet(self):
        return self._TranscodeTaskSet

    @TranscodeTaskSet.setter
    def TranscodeTaskSet(self, TranscodeTaskSet):
        self._TranscodeTaskSet = TranscodeTaskSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self._TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskSearchResult()
                obj._deserialize(item)
                self._TranscodeTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeUsageSummaryRequest(AbstractModel):
    """DescribeUsageSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BeginTime: 统计时间段的开始时间
        :type BeginTime: str
        :param _EndTime: 统计时间段的结束时间
        :type EndTime: str
        :param _SubProducts: 需要获取用量的子产品列表
        :type SubProducts: list of str
        :param _IsWeighted: true: 返回加权后的数据
false: 返回原始数据
        :type IsWeighted: bool
        """
        self._BeginTime = None
        self._EndTime = None
        self._SubProducts = None
        self._IsWeighted = None

    @property
    def BeginTime(self):
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SubProducts(self):
        return self._SubProducts

    @SubProducts.setter
    def SubProducts(self, SubProducts):
        self._SubProducts = SubProducts

    @property
    def IsWeighted(self):
        return self._IsWeighted

    @IsWeighted.setter
    def IsWeighted(self, IsWeighted):
        self._IsWeighted = IsWeighted


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._SubProducts = params.get("SubProducts")
        self._IsWeighted = params.get("IsWeighted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageSummaryResponse(AbstractModel):
    """DescribeUsageSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeUserListRequest(AbstractModel):
    """DescribeUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 白板应用的SdkAppId
        :type SdkAppId: int
        :param _RoomId: 需要查询用户列表的白板房间号
        :type RoomId: str
        :param _TimeRange: 查询时间段，Unix时间戳，单位毫秒，第一个值为开始时间戳，第二个值为结束时间
        :type TimeRange: list of int
        :param _Query: 额外的查询条件
        :type Query: str
        :param _MaxSize: 返回最大的数据条数，默认1000
        :type MaxSize: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._TimeRange = None
        self._Query = None
        self._MaxSize = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TimeRange(self):
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._TimeRange = params.get("TimeRange")
        self._Query = params.get("Query")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResponse(AbstractModel):
    """DescribeUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserList: 房间内的用户列表
        :type UserList: list of UserListItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserList = None
        self._RequestId = None

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserListItem()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserResourcesRequest(AbstractModel):
    """DescribeUserResources请求参数结构体

    """


class DescribeUserResourcesResponse(AbstractModel):
    """DescribeUserResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeUserStatusRequest(AbstractModel):
    """DescribeUserStatus请求参数结构体

    """


class DescribeUserStatusResponse(AbstractModel):
    """DescribeUserStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 客户的AppId
        :type AppId: int
        :param _IsTiwUser: 是否开通过白板（试用或正式）

0: 从未开通过白板服务
1: 已经开通过白板服务
        :type IsTiwUser: int
        :param _IsSaaSUser: 是否开通过互动课堂（试用或正式）
        :type IsSaaSUser: int
        :param _IsTiwOfflineRecordUser: 是否使用白板的课后录制
        :type IsTiwOfflineRecordUser: int
        :param _IsAuthenticated: 用户是否实名认证
        :type IsAuthenticated: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._IsTiwUser = None
        self._IsSaaSUser = None
        self._IsTiwOfflineRecordUser = None
        self._IsAuthenticated = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def IsTiwUser(self):
        return self._IsTiwUser

    @IsTiwUser.setter
    def IsTiwUser(self, IsTiwUser):
        self._IsTiwUser = IsTiwUser

    @property
    def IsSaaSUser(self):
        return self._IsSaaSUser

    @IsSaaSUser.setter
    def IsSaaSUser(self, IsSaaSUser):
        self._IsSaaSUser = IsSaaSUser

    @property
    def IsTiwOfflineRecordUser(self):
        return self._IsTiwOfflineRecordUser

    @IsTiwOfflineRecordUser.setter
    def IsTiwOfflineRecordUser(self, IsTiwOfflineRecordUser):
        self._IsTiwOfflineRecordUser = IsTiwOfflineRecordUser

    @property
    def IsAuthenticated(self):
        return self._IsAuthenticated

    @IsAuthenticated.setter
    def IsAuthenticated(self, IsAuthenticated):
        self._IsAuthenticated = IsAuthenticated

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._IsTiwUser = params.get("IsTiwUser")
        self._IsSaaSUser = params.get("IsSaaSUser")
        self._IsTiwOfflineRecordUser = params.get("IsTiwOfflineRecordUser")
        self._IsAuthenticated = params.get("IsAuthenticated")
        self._RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskCallbackRequest(AbstractModel):
    """DescribeVideoGenerationTaskCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskCallbackResponse(AbstractModel):
    """DescribeVideoGenerationTaskCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Callback: 录制视频生成回调地址
        :type Callback: str
        :param _CallbackKey: 录制视频生成回调鉴权密钥
        :type CallbackKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeVideoGenerationTaskRequest(AbstractModel):
    """DescribeVideoGenerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 录制视频生成的任务Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoGenerationTaskResponse(AbstractModel):
    """DescribeVideoGenerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 任务对应的群组Id
        :type GroupId: str
        :param _RoomId: 任务对应的房间号
        :type RoomId: int
        :param _TaskId: 任务的Id
        :type TaskId: str
        :param _Progress: 已废弃
        :type Progress: int
        :param _Status: 录制视频生成任务状态
- QUEUED: 正在排队
- PROCESSING: 正在生成视频
- FINISHED: 生成视频结束（成功完成或失败结束，可以通过错误码和错误信息进一步判断）
        :type Status: str
        :param _TotalTime: 回放视频总时长,单位：毫秒
        :type TotalTime: int
        :param _VideoInfos: 已废弃，请使用`VideoInfoList`参数
        :type VideoInfos: :class:`tencentcloud.tiw.v20190919.models.VideoInfo`
        :param _VideoInfoList: 录制视频生成视频列表
        :type VideoInfoList: list of VideoInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RoomId = None
        self._TaskId = None
        self._Progress = None
        self._Status = None
        self._TotalTime = None
        self._VideoInfos = None
        self._VideoInfoList = None
        self._RequestId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def VideoInfos(self):
        return self._VideoInfos

    @VideoInfos.setter
    def VideoInfos(self, VideoInfos):
        self._VideoInfos = VideoInfos

    @property
    def VideoInfoList(self):
        return self._VideoInfoList

    @VideoInfoList.setter
    def VideoInfoList(self, VideoInfoList):
        self._VideoInfoList = VideoInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RoomId = params.get("RoomId")
        self._TaskId = params.get("TaskId")
        self._Progress = params.get("Progress")
        self._Status = params.get("Status")
        self._TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self._VideoInfos = VideoInfo()
            self._VideoInfos._deserialize(params.get("VideoInfos"))
        if params.get("VideoInfoList") is not None:
            self._VideoInfoList = []
            for item in params.get("VideoInfoList"):
                obj = VideoInfo()
                obj._deserialize(item)
                self._VideoInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWarningCallbackRequest(AbstractModel):
    """DescribeWarningCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWarningCallbackResponse(AbstractModel):
    """DescribeWarningCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Callback: 告警事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param _CallbackKey: 告警回调鉴权密钥
        :type CallbackKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardApplicationConfigRequest(AbstractModel):
    """DescribeWhiteboardApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskTypes: 需要查询的任务类型
recording: 实时录制
transcode: 文档转码
        :type TaskTypes: list of str
        :param _SdkAppIds: 需要查询配置的SdkAppId列表
        :type SdkAppIds: list of int
        """
        self._SdkAppId = None
        self._TaskTypes = None
        self._SdkAppIds = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskTypes(self):
        return self._TaskTypes

    @TaskTypes.setter
    def TaskTypes(self, TaskTypes):
        self._TaskTypes = TaskTypes

    @property
    def SdkAppIds(self):
        return self._SdkAppIds

    @SdkAppIds.setter
    def SdkAppIds(self, SdkAppIds):
        self._SdkAppIds = SdkAppIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskTypes = params.get("TaskTypes")
        self._SdkAppIds = params.get("SdkAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardApplicationConfigResponse(AbstractModel):
    """DescribeWhiteboardApplicationConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Configs: 白板应用任务相关配置
        :type Configs: list of WhiteboardApplicationConfig
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SdkAppId = None
        self._Configs = None
        self._RequestId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self._Configs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardBucketConfigRequest(AbstractModel):
    """DescribeWhiteboardBucketConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskType: 需要查询的任务类型
recording: 实时录制
transcode: 文档转码
        :type TaskType: str
        """
        self._SdkAppId = None
        self._TaskType = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardBucketConfigResponse(AbstractModel):
    """DescribeWhiteboardBucketConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardPushCallbackRequest(AbstractModel):
    """DescribeWhiteboardPushCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushCallbackResponse(AbstractModel):
    """DescribeWhiteboardPushCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Callback: 白板推流事件回调地址，如果未设置回调地址，该字段为空字符串
        :type Callback: str
        :param _CallbackKey: 白板推流回调鉴权密钥
        :type CallbackKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Callback = None
        self._CallbackKey = None
        self._RequestId = None

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardPushRequest(AbstractModel):
    """DescribeWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 白板推流任务Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteboardPushResponse(AbstractModel):
    """DescribeWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FinishReason: 推流结束原因，
- AUTO: 房间内长时间没有音视频上行及白板操作导致自动停止推流
- USER_CALL: 主动调用了停止推流接口
- EXCEPTION: 推流异常结束
        :type FinishReason: str
        :param _TaskId: 需要查询结果的白板推流任务Id
        :type TaskId: str
        :param _Status: 推流任务状态
- PREPARED: 表示推流正在准备中（进房/启动推流服务等操作）
- PUSHING: 表示推流已开始
- STOPPED: 表示推流已停止
        :type Status: str
        :param _RoomId: 房间号
        :type RoomId: int
        :param _GroupId: 白板的群组 Id
        :type GroupId: str
        :param _PushUserId: 推流用户Id
        :type PushUserId: str
        :param _PushStartTime: 实际开始推流时间，Unix 时间戳，单位秒
        :type PushStartTime: int
        :param _PushStopTime: 实际停止推流时间，Unix 时间戳，单位秒
        :type PushStopTime: int
        :param _ExceptionCnt: 推流过程中出现异常的次数
        :type ExceptionCnt: int
        :param _IMSyncTime: 白板推流首帧对应的IM时间戳，可用于录制回放时IM聊天消息与白板推流视频进行同步对时。
        :type IMSyncTime: int
        :param _Backup: 备份推流任务结果信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FinishReason = None
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._GroupId = None
        self._PushUserId = None
        self._PushStartTime = None
        self._PushStopTime = None
        self._ExceptionCnt = None
        self._IMSyncTime = None
        self._Backup = None
        self._RequestId = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId

    @property
    def PushStartTime(self):
        return self._PushStartTime

    @PushStartTime.setter
    def PushStartTime(self, PushStartTime):
        self._PushStartTime = PushStartTime

    @property
    def PushStopTime(self):
        return self._PushStopTime

    @PushStopTime.setter
    def PushStopTime(self, PushStopTime):
        self._PushStopTime = PushStopTime

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def IMSyncTime(self):
        return self._IMSyncTime

    @IMSyncTime.setter
    def IMSyncTime(self, IMSyncTime):
        self._IMSyncTime = IMSyncTime

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._PushUserId = params.get("PushUserId")
        self._PushStartTime = params.get("PushStartTime")
        self._PushStopTime = params.get("PushStopTime")
        self._ExceptionCnt = params.get("ExceptionCnt")
        self._IMSyncTime = params.get("IMSyncTime")
        self._Backup = params.get("Backup")
        self._RequestId = params.get("RequestId")


class DescribeWhiteboardPushSearchRequest(AbstractModel):
    """DescribeWhiteboardPushSearch请求参数结构体

    """


class DescribeWhiteboardPushSearchResponse(AbstractModel):
    """DescribeWhiteboardPushSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WhiteboardPushTaskSet: 推流任务搜索结果集合
        :type WhiteboardPushTaskSet: list of WhiteboardPushTaskSearchResult
        :param _TotalCount: 推流总任务数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WhiteboardPushTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def WhiteboardPushTaskSet(self):
        return self._WhiteboardPushTaskSet

    @WhiteboardPushTaskSet.setter
    def WhiteboardPushTaskSet(self, WhiteboardPushTaskSet):
        self._WhiteboardPushTaskSet = WhiteboardPushTaskSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WhiteboardPushTaskSet") is not None:
            self._WhiteboardPushTaskSet = []
            for item in params.get("WhiteboardPushTaskSet"):
                obj = WhiteboardPushTaskSearchResult()
                obj._deserialize(item)
                self._WhiteboardPushTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Detail(AbstractModel):
    """计费用量数据里，带不同指标Tag的详情

    """

    def __init__(self):
        r"""
        :param _TagName: 用量指标
        :type TagName: str
        :param _Weight: 用量权重
        :type Weight: float
        :param _Value: 用量的值
        :type Value: float
        """
        self._TagName = None
        self._Weight = None
        self._Value = None

    @property
    def TagName(self):
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._TagName = params.get("TagName")
        self._Weight = params.get("Weight")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Interrupt(AbstractModel):
    """实时录制中出现的用户视频流断流次数统计

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _Count: 视频流断流次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._UserId = None
        self._Count = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayoutParams(AbstractModel):
    """自定义混流配置布局参数

    """

    def __init__(self):
        r"""
        :param _Width: 流画面宽，取值范围[2,3000]
        :type Width: int
        :param _Height: 流画面高，取值范围[2,3000]
        :type Height: int
        :param _X: 当前画面左上角顶点相对于Canvas左上角顶点的x轴偏移量，默认为0，取值范围[0,3000]
        :type X: int
        :param _Y: 当前画面左上角顶点相对于Canvas左上角顶点的y轴偏移量，默认为0， 取值范围[0,3000]
        :type Y: int
        :param _ZOrder: 画面z轴位置，默认为0
z轴确定了重叠画面的遮盖顺序，z轴值大的画面处于顶层
        :type ZOrder: int
        """
        self._Width = None
        self._Height = None
        self._X = None
        self._Y = None
        self._ZOrder = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def ZOrder(self):
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._ZOrder = params.get("ZOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixStream(AbstractModel):
    """混流配置

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启混流
        :type Enabled: bool
        :param _DisableAudio: 是否禁用音频混流
        :type DisableAudio: bool
        :param _ModelId: 内置混流布局模板ID, 取值 [1, 2], 区别见内置混流布局模板样式示例说明
在没有填Custom字段时候，ModelId是必填的
        :type ModelId: int
        :param _TeacherId: 老师用户ID
此字段只有在ModelId填了的情况下生效
填写TeacherId的效果是把指定为TeacherId的用户视频流显示在内置模板的第一个小画面中
        :type TeacherId: str
        :param _Custom: 自定义混流布局参数
当此字段存在时，ModelId 及 TeacherId 字段将被忽略
        :type Custom: :class:`tencentcloud.tiw.v20190919.models.CustomLayout`
        """
        self._Enabled = None
        self._DisableAudio = None
        self._ModelId = None
        self._TeacherId = None
        self._Custom = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DisableAudio(self):
        return self._DisableAudio

    @DisableAudio.setter
    def DisableAudio(self, DisableAudio):
        self._DisableAudio = DisableAudio

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def Custom(self):
        return self._Custom

    @Custom.setter
    def Custom(self, Custom):
        self._Custom = Custom


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._DisableAudio = params.get("DisableAudio")
        self._ModelId = params.get("ModelId")
        self._TeacherId = params.get("TeacherId")
        if params.get("Custom") is not None:
            self._Custom = CustomLayout()
            self._Custom._deserialize(params.get("Custom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationRequest(AbstractModel):
    """ModifyApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用SdkAppId
        :type SdkAppId: int
        :param _AppName: App名字
        :type AppName: str
        """
        self._SdkAppId = None
        self._AppName = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationResponse(AbstractModel):
    """ModifyApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubProduct: 资源Id，从DescribeUserResources接口中获取Level=1的正式月功能费的SubProduct，一般为sp_tiw_package
        :type SubProduct: str
        :param _ResourceId: 资源Id，从DescribeUserResources接口中获取Level=1的正式月功能费资源Id
        :type ResourceId: str
        :param _AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)，若业务无续费概念或无需自动续 费，需要设置为0
        :type AutoRenewFlag: int
        """
        self._SubProduct = None
        self._ResourceId = None
        self._AutoRenewFlag = None

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._SubProduct = params.get("SubProduct")
        self._ResourceId = params.get("ResourceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyWhiteboardApplicationConfigRequest(AbstractModel):
    """ModifyWhiteboardApplicationConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Configs: 白板应用任务相关配置
        :type Configs: list of WhiteboardApplicationConfig
        """
        self._SdkAppId = None
        self._Configs = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Configs(self):
        return self._Configs

    @Configs.setter
    def Configs(self, Configs):
        self._Configs = Configs


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Configs") is not None:
            self._Configs = []
            for item in params.get("Configs"):
                obj = WhiteboardApplicationConfig()
                obj._deserialize(item)
                self._Configs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardApplicationConfigResponse(AbstractModel):
    """ModifyWhiteboardApplicationConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyWhiteboardBucketConfigRequest(AbstractModel):
    """ModifyWhiteboardBucketConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskType: 需要查询的任务类型
recording: 实时录制
transcode: 文档转码
        :type TaskType: str
        :param _BucketName: COS存储桶名字
        :type BucketName: str
        :param _BucketLocation: COS存储桶地域
        :type BucketLocation: str
        :param _BucketPrefix: 存储桶里资源前缀
        :type BucketPrefix: str
        :param _ResultDomain: 返回Url域名
        :type ResultDomain: str
        """
        self._SdkAppId = None
        self._TaskType = None
        self._BucketName = None
        self._BucketLocation = None
        self._BucketPrefix = None
        self._ResultDomain = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketLocation(self):
        return self._BucketLocation

    @BucketLocation.setter
    def BucketLocation(self, BucketLocation):
        self._BucketLocation = BucketLocation

    @property
    def BucketPrefix(self):
        return self._BucketPrefix

    @BucketPrefix.setter
    def BucketPrefix(self, BucketPrefix):
        self._BucketPrefix = BucketPrefix

    @property
    def ResultDomain(self):
        return self._ResultDomain

    @ResultDomain.setter
    def ResultDomain(self, ResultDomain):
        self._ResultDomain = ResultDomain


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskType = params.get("TaskType")
        self._BucketName = params.get("BucketName")
        self._BucketLocation = params.get("BucketLocation")
        self._BucketPrefix = params.get("BucketPrefix")
        self._ResultDomain = params.get("ResultDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWhiteboardBucketConfigResponse(AbstractModel):
    """ModifyWhiteboardBucketConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OmittedDuration(AbstractModel):
    """拼接视频中被忽略的时间段

    """

    def __init__(self):
        r"""
        :param _VideoTime: 录制暂停时间戳对应的视频播放时间(单位: 毫秒)
        :type VideoTime: int
        :param _PauseTime: 录制暂停时间戳(单位: 毫秒)
        :type PauseTime: int
        :param _ResumeTime: 录制恢复时间戳(单位: 毫秒)
        :type ResumeTime: int
        """
        self._VideoTime = None
        self._PauseTime = None
        self._ResumeTime = None

    @property
    def VideoTime(self):
        return self._VideoTime

    @VideoTime.setter
    def VideoTime(self, VideoTime):
        self._VideoTime = VideoTime

    @property
    def PauseTime(self):
        return self._PauseTime

    @PauseTime.setter
    def PauseTime(self, PauseTime):
        self._PauseTime = PauseTime

    @property
    def ResumeTime(self):
        return self._ResumeTime

    @ResumeTime.setter
    def ResumeTime(self, ResumeTime):
        self._ResumeTime = ResumeTime


    def _deserialize(self, params):
        self._VideoTime = params.get("VideoTime")
        self._PauseTime = params.get("PauseTime")
        self._ResumeTime = params.get("ResumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PPTErr(AbstractModel):
    """PPT错误元素

    """

    def __init__(self):
        r"""
        :param _Name: 元素名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 0: 不支持的墨迹类型，1: 不支持自动翻页，2: 存在已损坏音视频，3: 存在不可访问资源，4: 只读文件
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _Detail: 错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Detail: str
        """
        self._Name = None
        self._Type = None
        self._Detail = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Detail = params.get("Detail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PPTErrSlide(AbstractModel):
    """PPT错误页面列表

    """

    def __init__(self):
        r"""
        :param _Page: 异常元素存在的页面，由页面类型+页码组成，页码类型包括：幻灯片、幻灯片母版、幻灯片布局等
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: str
        :param _Errs: 错误元素列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Errs: list of PPTErr
        """
        self._Page = None
        self._Errs = None

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Errs(self):
        return self._Errs

    @Errs.setter
    def Errs(self, Errs):
        self._Errs = Errs


    def _deserialize(self, params):
        self._Page = params.get("Page")
        if params.get("Errs") is not None:
            self._Errs = []
            for item in params.get("Errs"):
                obj = PPTErr()
                obj._deserialize(item)
                self._Errs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordRequest(AbstractModel):
    """PauseOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 实时录制任务 Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseOnlineRecordResponse(AbstractModel):
    """PauseOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RecordControl(AbstractModel):
    """录制控制参数， 用于指定全局录制控制及具体流录制控制参数，比如设置需要对哪些流进行录制，是否只录制小画面等

    """

    def __init__(self):
        r"""
        :param _Enabled: 设置是否开启录制控制参数，只有设置为true的时候，录制控制参数才生效。
        :type Enabled: bool
        :param _DisableRecord: 设置是否禁用录制的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流都不录制。
false - 所有流都录制。默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type DisableRecord: bool
        :param _DisableAudio: 设置是否禁用所有流的音频录制的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流的录制都不对音频进行录制。
false - 所有流的录制都需要对音频进行录制。默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type DisableAudio: bool
        :param _PullSmallVideo: 设置是否所有流都只录制小画面的全局控制参数。一般与`StreamControls`参数配合使用。

true - 所有流都只录制小画面。设置为true时，请确保上行端在推流的时候同时上行了小画面，否则录制视频可能是黑屏。
false - 所有流都录制大画面，默认为false。

这里的设置对所有流都生效，如果同时在 `StreamControls` 列表中针对指定流设置了控制参数，则优先采用`StreamControls`中设置的控制参数。
        :type PullSmallVideo: bool
        :param _StreamControls: 针对具体流指定控制参数，如果列表为空，则所有流采用全局配置的控制参数进行录制。列表不为空，则列表中指定的流将优先按此列表指定的控制参数进行录制。
        :type StreamControls: list of StreamControl
        """
        self._Enabled = None
        self._DisableRecord = None
        self._DisableAudio = None
        self._PullSmallVideo = None
        self._StreamControls = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def DisableAudio(self):
        return self._DisableAudio

    @DisableAudio.setter
    def DisableAudio(self, DisableAudio):
        self._DisableAudio = DisableAudio

    @property
    def PullSmallVideo(self):
        return self._PullSmallVideo

    @PullSmallVideo.setter
    def PullSmallVideo(self, PullSmallVideo):
        self._PullSmallVideo = PullSmallVideo

    @property
    def StreamControls(self):
        return self._StreamControls

    @StreamControls.setter
    def StreamControls(self, StreamControls):
        self._StreamControls = StreamControls


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._DisableRecord = params.get("DisableRecord")
        self._DisableAudio = params.get("DisableAudio")
        self._PullSmallVideo = params.get("PullSmallVideo")
        if params.get("StreamControls") is not None:
            self._StreamControls = []
            for item in params.get("StreamControls"):
                obj = StreamControl()
                obj._deserialize(item)
                self._StreamControls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskResult(AbstractModel):
    """实时录制结果

    """

    def __init__(self):
        r"""
        :param _FinishReason: AUTO - 自动停止录制， USER_CALL - 用户主动调用停止录制
        :type FinishReason: str
        :param _ExceptionCnt: 异常数
        :type ExceptionCnt: int
        :param _RoomId: 房间号
        :type RoomId: int
        :param _GroupId: 分组
        :type GroupId: str
        :param _RecordStartTime: 录制真实开始时间
        :type RecordStartTime: int
        :param _RecordStopTime: 录制结束时间
        :type RecordStopTime: int
        :param _TotalTime: 录制总时长
        :type TotalTime: int
        :param _VideoInfos: 视频信息列表
        :type VideoInfos: list of VideoInfo
        :param _OmittedDurations: 被忽略的视频时间段
        :type OmittedDurations: list of OmittedDuration
        :param _Details: 详情
        :type Details: str
        :param _ErrorCode: 任务失败错误码
        :type ErrorCode: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        """
        self._FinishReason = None
        self._ExceptionCnt = None
        self._RoomId = None
        self._GroupId = None
        self._RecordStartTime = None
        self._RecordStopTime = None
        self._TotalTime = None
        self._VideoInfos = None
        self._OmittedDurations = None
        self._Details = None
        self._ErrorCode = None
        self._ErrorMsg = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RecordStartTime(self):
        return self._RecordStartTime

    @RecordStartTime.setter
    def RecordStartTime(self, RecordStartTime):
        self._RecordStartTime = RecordStartTime

    @property
    def RecordStopTime(self):
        return self._RecordStopTime

    @RecordStopTime.setter
    def RecordStopTime(self, RecordStopTime):
        self._RecordStopTime = RecordStopTime

    @property
    def TotalTime(self):
        return self._TotalTime

    @TotalTime.setter
    def TotalTime(self, TotalTime):
        self._TotalTime = TotalTime

    @property
    def VideoInfos(self):
        return self._VideoInfos

    @VideoInfos.setter
    def VideoInfos(self, VideoInfos):
        self._VideoInfos = VideoInfos

    @property
    def OmittedDurations(self):
        return self._OmittedDurations

    @OmittedDurations.setter
    def OmittedDurations(self, OmittedDurations):
        self._OmittedDurations = OmittedDurations

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._ExceptionCnt = params.get("ExceptionCnt")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._RecordStartTime = params.get("RecordStartTime")
        self._RecordStopTime = params.get("RecordStopTime")
        self._TotalTime = params.get("TotalTime")
        if params.get("VideoInfos") is not None:
            self._VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self._VideoInfos.append(obj)
        if params.get("OmittedDurations") is not None:
            self._OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self._OmittedDurations.append(obj)
        self._Details = params.get("Details")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTaskSearchResult(AbstractModel):
    """实时录制任务搜索结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一ID
        :type TaskId: str
        :param _Status: 实时录制任务状态
- PAUSED: 录制已暂停
- PREPARED: 录制在准备阶段
- RECORDING: 正在录制
- STOPPED：录制已停止
- FINISHED: 录制已结束
        :type Status: str
        :param _RoomId: 实时录制房间号
        :type RoomId: int
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _SdkAppId: 用户应用SdkAppId
        :type SdkAppId: int
        :param _Result: 实时录制结果
        :type Result: :class:`tencentcloud.tiw.v20190919.models.RecordTaskResult`
        """
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._CreateTime = None
        self._SdkAppId = None
        self._Result = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._CreateTime = params.get("CreateTime")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self._Result = RecordTaskResult()
            self._Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordRequest(AbstractModel):
    """ResumeOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 恢复录制的实时录制任务 Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeOnlineRecordResponse(AbstractModel):
    """ResumeOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RoomListItem(AbstractModel):
    """日志查询里返回的白板房间数据

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID
        :type RoomId: str
        :param _StartTime: 房间在查询时间段内最早出现的时间，Unix时间戳，单位毫秒
        :type StartTime: int
        :param _EndTime: 房间在查询时间段内最晚出现的时间，Unix时间戳，单位毫秒
        :type EndTime: int
        :param _UserNumber: 房间里成员数
        :type UserNumber: int
        """
        self._RoomId = None
        self._StartTime = None
        self._EndTime = None
        self._UserNumber = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserNumber(self):
        return self._UserNumber

    @UserNumber.setter
    def UserNumber(self, UserNumber):
        self._UserNumber = UserNumber


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserNumber = params.get("UserNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomUsageDataItem(AbstractModel):
    """互动白板房间用量信息

    """

    def __init__(self):
        r"""
        :param _Time: 日期，格式为YYYY-MM-DD
        :type Time: str
        :param _SdkAppId: 白板应用SDKAppID
        :type SdkAppId: int
        :param _SubProduct: 互动白板子产品，请求参数传入的一致
- sp_tiw_board: 互动白板时长
- sp_tiw_ric: 实时录制时长
        :type SubProduct: str
        :param _Value: 用量值
- 白板时长、实时录制时长单位为分钟
        :type Value: float
        :param _RoomID: 互动白板房间号
        :type RoomID: int
        """
        self._Time = None
        self._SdkAppId = None
        self._SubProduct = None
        self._Value = None
        self._RoomID = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def RoomID(self):
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._Value = params.get("Value")
        self._RoomID = params.get("RoomID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunningTaskItem(AbstractModel):
    """正在运行的任务列表项

    """

    def __init__(self):
        r"""
        :param _SdkAppID: 应用SdkAppID
        :type SdkAppID: int
        :param _TaskID: 任务ID
        :type TaskID: str
        :param _TaskType: 任务类型
- TranscodeH5: 动态转码任务，文档转HTML5页面
- TranscodeJPG: 静态转码任务，文档转图片
- WhiteboardPush: 白板推流任务
- OnlineRecord: 实时录制任务
        :type TaskType: str
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _CancelTime: 任务取消时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CancelTime: str
        :param _Status: 任务状态
- QUEUED: 任务正在排队等待执行中
- PROCESSING: 任务正在执行中 
- FINISHED: 任务已完成
        :type Status: str
        :param _Progress: 任务当前进度
        :type Progress: int
        :param _FileURL: 转码任务中转码文件的原始URL
此参数只有任务类型为TranscodeH5、TranscodeJPG类型时才会有有效值。其他任务类型为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileURL: str
        :param _RoomID: 房间号

当任务类型为TranscodeH5、TranscodeJPG时，房间号为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomID: int
        """
        self._SdkAppID = None
        self._TaskID = None
        self._TaskType = None
        self._CreateTime = None
        self._CancelTime = None
        self._Status = None
        self._Progress = None
        self._FileURL = None
        self._RoomID = None

    @property
    def SdkAppID(self):
        return self._SdkAppID

    @SdkAppID.setter
    def SdkAppID(self, SdkAppID):
        self._SdkAppID = SdkAppID

    @property
    def TaskID(self):
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CancelTime(self):
        return self._CancelTime

    @CancelTime.setter
    def CancelTime(self, CancelTime):
        self._CancelTime = CancelTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def FileURL(self):
        return self._FileURL

    @FileURL.setter
    def FileURL(self, FileURL):
        self._FileURL = FileURL

    @property
    def RoomID(self):
        return self._RoomID

    @RoomID.setter
    def RoomID(self, RoomID):
        self._RoomID = RoomID


    def _deserialize(self, params):
        self._SdkAppID = params.get("SdkAppID")
        self._TaskID = params.get("TaskID")
        self._TaskType = params.get("TaskType")
        self._CreateTime = params.get("CreateTime")
        self._CancelTime = params.get("CancelTime")
        self._Status = params.get("Status")
        self._Progress = params.get("Progress")
        self._FileURL = params.get("FileURL")
        self._RoomID = params.get("RoomID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOfflineRecordCallbackRequest(AbstractModel):
    """SetOfflineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Callback: 课后录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOfflineRecordCallbackResponse(AbstractModel):
    """SetOfflineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetOnlineRecordCallbackKeyRequest(AbstractModel):
    """SetOnlineRecordCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param _CallbackKey: 设置实时录制回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥。回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackKeyResponse(AbstractModel):
    """SetOnlineRecordCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetOnlineRecordCallbackRequest(AbstractModel):
    """SetOnlineRecordCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Callback: 实时录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头。回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40258
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetOnlineRecordCallbackResponse(AbstractModel):
    """SetOnlineRecordCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetPPTCheckCallbackKeyRequest(AbstractModel):
    """SetPPTCheckCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param _CallbackKey: 设置回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257	
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPPTCheckCallbackKeyResponse(AbstractModel):
    """SetPPTCheckCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetPPTCheckCallbackRequest(AbstractModel):
    """SetPPTCheckCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId	
        :type SdkAppId: int
        :param _Callback: 进度回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。 回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260#c9cbe05f-fe1a-4410-b4dc-40cc301c7b81	
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPPTCheckCallbackResponse(AbstractModel):
    """SetPPTCheckCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetTranscodeCallbackKeyRequest(AbstractModel):
    """SetTranscodeCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param _CallbackKey: 设置文档转码回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackKeyResponse(AbstractModel):
    """SetTranscodeCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetTranscodeCallbackRequest(AbstractModel):
    """SetTranscodeCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Callback: 文档转码进度回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。
回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40260
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTranscodeCallbackResponse(AbstractModel):
    """SetTranscodeCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetVideoGenerationTaskCallbackKeyRequest(AbstractModel):
    """SetVideoGenerationTaskCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param _CallbackKey: 设置视频生成回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackKeyResponse(AbstractModel):
    """SetVideoGenerationTaskCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetVideoGenerationTaskCallbackRequest(AbstractModel):
    """SetVideoGenerationTaskCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Callback: 课后录制任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVideoGenerationTaskCallbackResponse(AbstractModel):
    """SetVideoGenerationTaskCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetWarningCallbackRequest(AbstractModel):
    """SetWarningCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Callback: 告警回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以http://或https://开头。
回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/90112
        :type Callback: str
        :param _CallbackKey: 设置告警回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥，回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._Callback = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWarningCallbackResponse(AbstractModel):
    """SetWarningCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackKeyRequest(AbstractModel):
    """SetWhiteboardPushCallbackKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用的SdkAppId
        :type SdkAppId: int
        :param _CallbackKey: 设置白板推流回调鉴权密钥，最长64字符，如果传入空字符串，那么删除现有的鉴权回调密钥。回调鉴权方式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type CallbackKey: str
        """
        self._SdkAppId = None
        self._CallbackKey = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackKeyResponse(AbstractModel):
    """SetWhiteboardPushCallbackKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetWhiteboardPushCallbackRequest(AbstractModel):
    """SetWhiteboardPushCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _Callback: 白板推流任务结果回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持 http或https协议，即回调地址以http://或https://开头。回调数据格式请参考文档：https://cloud.tencent.com/document/product/1137/40257
        :type Callback: str
        """
        self._SdkAppId = None
        self._Callback = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWhiteboardPushCallbackResponse(AbstractModel):
    """SetWhiteboardPushCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SnapshotCOS(AbstractModel):
    """板书文件存储cos参数

    """

    def __init__(self):
        r"""
        :param _Uin: cos所在腾讯云帐号uin
        :type Uin: int
        :param _Region: cos所在地区
        :type Region: str
        :param _Bucket: cos存储桶名称
        :type Bucket: str
        :param _TargetDir: 板书文件存储根目录
        :type TargetDir: str
        :param _Domain: CDN加速域名
        :type Domain: str
        """
        self._Uin = None
        self._Region = None
        self._Bucket = None
        self._TargetDir = None
        self._Domain = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def TargetDir(self):
        return self._TargetDir

    @TargetDir.setter
    def TargetDir(self, TargetDir):
        self._TargetDir = TargetDir

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._TargetDir = params.get("TargetDir")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotResult(AbstractModel):
    """白板板书结果

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 任务执行错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _Total: 快照生成图片总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Snapshots: 快照图片链接列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Snapshots: list of str
        """
        self._ErrorCode = None
        self._ErrorMessage = None
        self._Total = None
        self._Snapshots = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Snapshots(self):
        return self._Snapshots

    @Snapshots.setter
    def Snapshots(self, Snapshots):
        self._Snapshots = Snapshots


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._Total = params.get("Total")
        self._Snapshots = params.get("Snapshots")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotWhiteboard(AbstractModel):
    """生成白板板书时的白板参数，例如白板宽高等

    """

    def __init__(self):
        r"""
        :param _Width: 白板宽度大小，默认为1280，有效取值范围[0，2560]
        :type Width: int
        :param _Height: 白板高度大小，默认为720，有效取值范围[0，2560]
        :type Height: int
        :param _InitParams: 白板初始化参数的JSON转义字符串，透传到白板 SDK
        :type InitParams: str
        """
        self._Width = None
        self._Height = None
        self._InitParams = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def InitParams(self):
        return self._InitParams

    @InitParams.setter
    def InitParams(self, InitParams):
        self._InitParams = InitParams


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._InitParams = params.get("InitParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordRequest(AbstractModel):
    """StartOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _RoomId: 需要录制的房间号，取值范围: (1, 4294967295)
        :type RoomId: int
        :param _RecordUserId: 用于录制服务进房的用户ID，最大长度不能大于60个字节，格式为`tic_record_user_${RoomId}_${Random}`，其中 `${RoomId} `与录制房间号对应，`${Random}`为一个随机字符串。
该ID必须是一个单独的未在SDK中使用的ID，录制服务使用这个用户ID进入房间进行音视频与白板录制，若该ID和SDK中使用的ID重复，会导致SDK和录制服务互踢，影响正常录制。
        :type RecordUserId: str
        :param _RecordUserSig: 与RecordUserId对应的签名
        :type RecordUserSig: str
        :param _GroupId: （已废弃，设置无效）白板的 IM 群组 Id，默认同房间号
        :type GroupId: str
        :param _Concat: 录制视频拼接参数
        :type Concat: :class:`tencentcloud.tiw.v20190919.models.Concat`
        :param _Whiteboard: 录制白板参数，例如白板宽高等
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param _MixStream: 录制混流参数
特别说明：
1. 混流功能需要根据额外开通， 请联系腾讯云互动白板客服人员
2. 使用混流功能，必须提供 Extras 参数，且 Extras 参数中必须包含 "MIX_STREAM"
        :type MixStream: :class:`tencentcloud.tiw.v20190919.models.MixStream`
        :param _Extras: 使用到的高级功能列表
可以选值列表：
MIX_STREAM - 混流功能
        :type Extras: list of str
        :param _AudioFileNeeded: 是否需要在结果回调中返回各路流的纯音频录制文件，文件格式为mp3
        :type AudioFileNeeded: bool
        :param _RecordControl: 录制控制参数，用于更精细地指定需要录制哪些流，某一路流是否禁用音频，是否只录制小画面等
        :type RecordControl: :class:`tencentcloud.tiw.v20190919.models.RecordControl`
        :param _RecordMode: 录制模式

REALTIME_MODE - 实时录制模式（默认）
VIDEO_GENERATION_MODE - 视频生成模式（内测中，需邮件申请开通）
        :type RecordMode: str
        :param _ChatGroupId: 聊天群组ID，此字段仅适用于`视频生成模式`

在`视频生成模式`下，默认会记录白板群组内的非白板信令消息，如果指定了`ChatGroupId`，则会记录指定群ID的聊天消息。
        :type ChatGroupId: str
        :param _AutoStopTimeout: 自动停止录制超时时间，单位秒，取值范围[300, 86400], 默认值为300秒。

当超过设定时间房间内没有音视频上行且没有白板操作的时候，录制服务会自动停止当前录制任务。
        :type AutoStopTimeout: int
        :param _ExtraData: 内部参数，可忽略
        :type ExtraData: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RecordUserId = None
        self._RecordUserSig = None
        self._GroupId = None
        self._Concat = None
        self._Whiteboard = None
        self._MixStream = None
        self._Extras = None
        self._AudioFileNeeded = None
        self._RecordControl = None
        self._RecordMode = None
        self._ChatGroupId = None
        self._AutoStopTimeout = None
        self._ExtraData = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RecordUserId(self):
        return self._RecordUserId

    @RecordUserId.setter
    def RecordUserId(self, RecordUserId):
        self._RecordUserId = RecordUserId

    @property
    def RecordUserSig(self):
        return self._RecordUserSig

    @RecordUserSig.setter
    def RecordUserSig(self, RecordUserSig):
        self._RecordUserSig = RecordUserSig

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Concat(self):
        return self._Concat

    @Concat.setter
    def Concat(self, Concat):
        self._Concat = Concat

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def MixStream(self):
        return self._MixStream

    @MixStream.setter
    def MixStream(self, MixStream):
        self._MixStream = MixStream

    @property
    def Extras(self):
        return self._Extras

    @Extras.setter
    def Extras(self, Extras):
        self._Extras = Extras

    @property
    def AudioFileNeeded(self):
        return self._AudioFileNeeded

    @AudioFileNeeded.setter
    def AudioFileNeeded(self, AudioFileNeeded):
        self._AudioFileNeeded = AudioFileNeeded

    @property
    def RecordControl(self):
        return self._RecordControl

    @RecordControl.setter
    def RecordControl(self, RecordControl):
        self._RecordControl = RecordControl

    @property
    def RecordMode(self):
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def ChatGroupId(self):
        return self._ChatGroupId

    @ChatGroupId.setter
    def ChatGroupId(self, ChatGroupId):
        self._ChatGroupId = ChatGroupId

    @property
    def AutoStopTimeout(self):
        return self._AutoStopTimeout

    @AutoStopTimeout.setter
    def AutoStopTimeout(self, AutoStopTimeout):
        self._AutoStopTimeout = AutoStopTimeout

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RecordUserId = params.get("RecordUserId")
        self._RecordUserSig = params.get("RecordUserSig")
        self._GroupId = params.get("GroupId")
        if params.get("Concat") is not None:
            self._Concat = Concat()
            self._Concat._deserialize(params.get("Concat"))
        if params.get("Whiteboard") is not None:
            self._Whiteboard = Whiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("MixStream") is not None:
            self._MixStream = MixStream()
            self._MixStream._deserialize(params.get("MixStream"))
        self._Extras = params.get("Extras")
        self._AudioFileNeeded = params.get("AudioFileNeeded")
        if params.get("RecordControl") is not None:
            self._RecordControl = RecordControl()
            self._RecordControl._deserialize(params.get("RecordControl"))
        self._RecordMode = params.get("RecordMode")
        self._ChatGroupId = params.get("ChatGroupId")
        self._AutoStopTimeout = params.get("AutoStopTimeout")
        self._ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartOnlineRecordResponse(AbstractModel):
    """StartOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 录制任务Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartWhiteboardPushRequest(AbstractModel):
    """StartWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _RoomId: 需要推流的白板房间号，取值范围: (1, 4294967295)。

1. 白板推流默认以RoomId的字符串表达形式作为IM群组的GroupID（比如RoomId为1234，则IM群组的GroupID为"1234"）加群进行信令同步，请在开始推流前确保相应IM群组已创建完成，否则会导致推流失败。
2. 在没有指定TRTCRoomId和TRTCRoomIdStr的情况下，默认会以RoomId作为白板流进行推流的TRTC房间号。
        :type RoomId: int
        :param _PushUserId: 用于白板推流服务进入白板房间的用户ID。在没有额外指定`IMAuthParam`和`TRTCAuthParam`的情况下，这个用户ID同时会用于IM登录、IM加群、TRTC进房推流等操作。
用户ID最大长度不能大于60个字节，该用户ID必须是一个单独的未同时在其他地方使用的用户ID，白板推流服务使用这个用户ID进入房间进行白板音视频推流，若该用户ID和其他地方同时在使用的用户ID重复，会导致白板推流服务与其他使用场景帐号互踢，影响正常推流。
        :type PushUserId: str
        :param _PushUserSig: 与PushUserId对应的IM签名(usersig)。
        :type PushUserSig: str
        :param _Whiteboard: 白板参数，例如白板宽高、背景颜色等
        :type Whiteboard: :class:`tencentcloud.tiw.v20190919.models.Whiteboard`
        :param _AutoStopTimeout: 自动停止推流超时时间，单位秒，取值范围[300, 259200], 默认值为1800秒。

当白板超过设定时间没有操作的时候，白板推流服务会自动停止白板推流。
        :type AutoStopTimeout: int
        :param _AutoManageBackup: 对主白板推流任务进行操作时，是否同时同步操作备份任务
        :type AutoManageBackup: bool
        :param _Backup: 备份白板推流相关参数。

指定了备份参数的情况下，白板推流服务会在房间内新增一路白板画面视频流，即同一个房间内会有两路白板画面推流。
        :type Backup: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushBackupParam`
        :param _PrivateMapKey: TRTC高级权限控制参数，如果在实时音视频开启了高级权限控制功能，必须提供PrivateMapKey才能保证正常推流。
        :type PrivateMapKey: str
        :param _VideoFPS: 白板推流视频帧率，取值范围[0, 30]，默认20fps
        :type VideoFPS: int
        :param _VideoBitrate: 白板推流码率， 取值范围[0, 2000]，默认1200kbps。

这里的码率设置是一个参考值，实际推流的时候使用的是动态码率，所以真实码率不会固定为指定值，会在指定值附近波动。
        :type VideoBitrate: int
        :param _AutoRecord: 在实时音视频云端录制模式选择为 `指定用户录制` 模式的时候是否自动录制白板推流。

默认在实时音视频的云端录制模式选择为 `指定用户录制` 模式的情况下，不会自动进行白板推流录制，如果希望进行白板推流录制，请将此参数设置为true。

如果实时音视频的云端录制模式选择为 `全局自动录制` 模式，可忽略此参数。
        :type AutoRecord: bool
        :param _UserDefinedRecordId: 指定白板推流录制的RecordID，指定的RecordID会用于填充实时音视频云端录制完成后的回调消息中的 "userdefinerecordid" 字段内容，便于您更方便的识别录制回调，以及在点播媒体资源管理中查找相应的录制视频文件。

限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符。

此字段设置后，不管`AutoRecord`字段取值如何，都将自动进行白板推流录制。

默认RecordId生成规则如下：
urlencode(SdkAppID_RoomID_PushUserID)

例如：
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
那么：RecordId = 12345678_12345_push_user_1
        :type UserDefinedRecordId: str
        :param _AutoPublish: 在实时音视频旁路推流模式选择为`指定用户旁路`模式的时候，是否自动旁路白板推流。

默认在实时音视频的旁路推流模式选择为 `指定用户旁路` 模式的情况下，不会自动旁路白板推流，如果希望旁路白板推流，请将此参数设置为true。

如果实时音视频的旁路推流模式选择为 `全局自动旁路` 模式，可忽略此参数。
        :type AutoPublish: bool
        :param _UserDefinedStreamId: 指定实时音视频在旁路白板推流时的StreamID，设置之后，您就可以在腾讯云直播 CDN 上通过标准直播方案（FLV或HLS）播放该用户的音视频流。

限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符。

此字段设置后，不管`AutoPublish`字段取值如何，都将自动旁路白板推流。

默认StreamID生成规则如下：
urlencode(SdkAppID_RoomID_PushUserID_main)

例如：
SdkAppID = 12345678，RoomID = 12345，PushUserID = push_user_1
那么：StreamID = 12345678_12345_push_user_1_main
        :type UserDefinedStreamId: str
        :param _ExtraData: 内部参数，不需要关注此参数
        :type ExtraData: str
        :param _TRTCRoomId: TRTC数字类型房间号，取值范围: (1, 4294967295)。

在同时指定了RoomId与TRTCRoomId的情况下，优先使用TRTCRoomId作为白板流进行推流的TRTC房间号。

当指定了TRTCRoomIdStr的情况下，此字段将被忽略。
        :type TRTCRoomId: int
        :param _TRTCRoomIdStr: TRTC字符串类型房间号。

在指定了TRTCRoomIdStr的情况下，会优先使用TRTCRoomIdStr作为白板流进行推流的TRTC房间号。
        :type TRTCRoomIdStr: str
        :param _IMAuthParam: IM鉴权信息参数，用于IM鉴权。
当白板信令所使用的IM应用与白板应用的SdkAppId不一致时，可以通过此参数提供对应IM应用鉴权信息。

如果提供了此参数，白板推流服务会优先使用此参数指定的SdkAppId作为白板信令的传输通道，否则使用公共参数中的SdkAppId作为白板信令的传输通道。
        :type IMAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param _TRTCAuthParam: TRTC鉴权信息参数，用于TRTC进房推流鉴权。
当需要推流到的TRTC房间所对应的TRTC应用与白板应用的SdkAppId不一致时，可以通过此参数提供对应的TRTC应用鉴权信息。

如果提供了此参数，白板推流服务会优先使用此参数指定的SdkAppId作为白板推流的目标TRTC应用，否则使用公共参数中的SdkAppId作为白板推流的目标TRTC应用。
        :type TRTCAuthParam: :class:`tencentcloud.tiw.v20190919.models.AuthParam`
        :param _TRTCEnterRoomMode: 指定白板推流时推流用户进TRTC房间的进房模式。默认为 TRTCAppSceneVideoCall

TRTCAppSceneVideoCall - 视频通话场景，即绝大多数时间都是两人或两人以上视频通话的场景，内部编码器和网络协议优化侧重流畅性，降低通话延迟和卡顿率。
TRTCAppSceneLIVE - 直播场景，即绝大多数时间都是一人直播，偶尔有多人视频互动的场景，内部编码器和网络协议优化侧重性能和兼容性，性能和清晰度表现更佳。
        :type TRTCEnterRoomMode: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._PushUserId = None
        self._PushUserSig = None
        self._Whiteboard = None
        self._AutoStopTimeout = None
        self._AutoManageBackup = None
        self._Backup = None
        self._PrivateMapKey = None
        self._VideoFPS = None
        self._VideoBitrate = None
        self._AutoRecord = None
        self._UserDefinedRecordId = None
        self._AutoPublish = None
        self._UserDefinedStreamId = None
        self._ExtraData = None
        self._TRTCRoomId = None
        self._TRTCRoomIdStr = None
        self._IMAuthParam = None
        self._TRTCAuthParam = None
        self._TRTCEnterRoomMode = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId

    @property
    def PushUserSig(self):
        return self._PushUserSig

    @PushUserSig.setter
    def PushUserSig(self, PushUserSig):
        self._PushUserSig = PushUserSig

    @property
    def Whiteboard(self):
        return self._Whiteboard

    @Whiteboard.setter
    def Whiteboard(self, Whiteboard):
        self._Whiteboard = Whiteboard

    @property
    def AutoStopTimeout(self):
        return self._AutoStopTimeout

    @AutoStopTimeout.setter
    def AutoStopTimeout(self, AutoStopTimeout):
        self._AutoStopTimeout = AutoStopTimeout

    @property
    def AutoManageBackup(self):
        return self._AutoManageBackup

    @AutoManageBackup.setter
    def AutoManageBackup(self, AutoManageBackup):
        self._AutoManageBackup = AutoManageBackup

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def PrivateMapKey(self):
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey

    @property
    def VideoFPS(self):
        return self._VideoFPS

    @VideoFPS.setter
    def VideoFPS(self, VideoFPS):
        self._VideoFPS = VideoFPS

    @property
    def VideoBitrate(self):
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def AutoRecord(self):
        return self._AutoRecord

    @AutoRecord.setter
    def AutoRecord(self, AutoRecord):
        self._AutoRecord = AutoRecord

    @property
    def UserDefinedRecordId(self):
        return self._UserDefinedRecordId

    @UserDefinedRecordId.setter
    def UserDefinedRecordId(self, UserDefinedRecordId):
        self._UserDefinedRecordId = UserDefinedRecordId

    @property
    def AutoPublish(self):
        return self._AutoPublish

    @AutoPublish.setter
    def AutoPublish(self, AutoPublish):
        self._AutoPublish = AutoPublish

    @property
    def UserDefinedStreamId(self):
        return self._UserDefinedStreamId

    @UserDefinedStreamId.setter
    def UserDefinedStreamId(self, UserDefinedStreamId):
        self._UserDefinedStreamId = UserDefinedStreamId

    @property
    def ExtraData(self):
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def TRTCRoomId(self):
        return self._TRTCRoomId

    @TRTCRoomId.setter
    def TRTCRoomId(self, TRTCRoomId):
        self._TRTCRoomId = TRTCRoomId

    @property
    def TRTCRoomIdStr(self):
        return self._TRTCRoomIdStr

    @TRTCRoomIdStr.setter
    def TRTCRoomIdStr(self, TRTCRoomIdStr):
        self._TRTCRoomIdStr = TRTCRoomIdStr

    @property
    def IMAuthParam(self):
        return self._IMAuthParam

    @IMAuthParam.setter
    def IMAuthParam(self, IMAuthParam):
        self._IMAuthParam = IMAuthParam

    @property
    def TRTCAuthParam(self):
        return self._TRTCAuthParam

    @TRTCAuthParam.setter
    def TRTCAuthParam(self, TRTCAuthParam):
        self._TRTCAuthParam = TRTCAuthParam

    @property
    def TRTCEnterRoomMode(self):
        return self._TRTCEnterRoomMode

    @TRTCEnterRoomMode.setter
    def TRTCEnterRoomMode(self, TRTCEnterRoomMode):
        self._TRTCEnterRoomMode = TRTCEnterRoomMode


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._PushUserId = params.get("PushUserId")
        self._PushUserSig = params.get("PushUserSig")
        if params.get("Whiteboard") is not None:
            self._Whiteboard = Whiteboard()
            self._Whiteboard._deserialize(params.get("Whiteboard"))
        self._AutoStopTimeout = params.get("AutoStopTimeout")
        self._AutoManageBackup = params.get("AutoManageBackup")
        if params.get("Backup") is not None:
            self._Backup = WhiteboardPushBackupParam()
            self._Backup._deserialize(params.get("Backup"))
        self._PrivateMapKey = params.get("PrivateMapKey")
        self._VideoFPS = params.get("VideoFPS")
        self._VideoBitrate = params.get("VideoBitrate")
        self._AutoRecord = params.get("AutoRecord")
        self._UserDefinedRecordId = params.get("UserDefinedRecordId")
        self._AutoPublish = params.get("AutoPublish")
        self._UserDefinedStreamId = params.get("UserDefinedStreamId")
        self._ExtraData = params.get("ExtraData")
        self._TRTCRoomId = params.get("TRTCRoomId")
        self._TRTCRoomIdStr = params.get("TRTCRoomIdStr")
        if params.get("IMAuthParam") is not None:
            self._IMAuthParam = AuthParam()
            self._IMAuthParam._deserialize(params.get("IMAuthParam"))
        if params.get("TRTCAuthParam") is not None:
            self._TRTCAuthParam = AuthParam()
            self._TRTCAuthParam._deserialize(params.get("TRTCAuthParam"))
        self._TRTCEnterRoomMode = params.get("TRTCEnterRoomMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartWhiteboardPushResponse(AbstractModel):
    """StartWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 推流任务Id
        :type TaskId: str
        :param _Backup: 备份任务结果参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Backup = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Backup = params.get("Backup")
        self._RequestId = params.get("RequestId")


class StopOnlineRecordRequest(AbstractModel):
    """StopOnlineRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 需要停止录制的任务 Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopOnlineRecordResponse(AbstractModel):
    """StopOnlineRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopWhiteboardPushRequest(AbstractModel):
    """StopWhiteboardPush请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 客户的SdkAppId
        :type SdkAppId: int
        :param _TaskId: 需要停止的白板推流任务 Id
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWhiteboardPushResponse(AbstractModel):
    """StopWhiteboardPush返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Backup: 备份任务相关参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Backup = None
        self._RequestId = None

    @property
    def Backup(self):
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Backup = params.get("Backup")
        self._RequestId = params.get("RequestId")


class StreamControl(AbstractModel):
    """指定流录制的控制参数，比如是否禁用音频、视频是录制大画面还是录制小画面等

    """

    def __init__(self):
        r"""
        :param _StreamId: 视频流ID
视频流ID的取值含义如下：
1. tic_record_user - 表示白板视频流
2. tic_substream - 表示辅路视频流
3. 特定用户ID - 表示指定用户的视频流

在实际录制过程中，视频流ID的匹配规则为前缀匹配，只要真实流ID的前缀与指定的流ID一致就认为匹配成功。
        :type StreamId: str
        :param _DisableRecord: 设置是否对此路流开启录制。

true - 表示不对这路流进行录制，录制结果将不包含这路流的视频。
false - 表示需要对这路流进行录制，录制结果会包含这路流的视频。

默认为 false。
        :type DisableRecord: bool
        :param _DisableAudio: 设置是否禁用这路流的音频录制。

true - 表示不对这路流的音频进行录制，录制结果里这路流的视频将会没有声音。
false - 录制视频会保留音频，如果设置为true，则录制视频会丢弃这路流的音频。

默认为 false。
        :type DisableAudio: bool
        :param _PullSmallVideo: 设置当前流录制视频是否只录制小画面。

true - 录制小画面。设置为true时，请确保上行端同时上行了小画面，否则录制视频可能是黑屏。
false - 录制大画面。

默认为 false。
        :type PullSmallVideo: bool
        """
        self._StreamId = None
        self._DisableRecord = None
        self._DisableAudio = None
        self._PullSmallVideo = None

    @property
    def StreamId(self):
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def DisableAudio(self):
        return self._DisableAudio

    @DisableAudio.setter
    def DisableAudio(self, DisableAudio):
        self._DisableAudio = DisableAudio

    @property
    def PullSmallVideo(self):
        return self._PullSmallVideo

    @PullSmallVideo.setter
    def PullSmallVideo(self, PullSmallVideo):
        self._PullSmallVideo = PullSmallVideo


    def _deserialize(self, params):
        self._StreamId = params.get("StreamId")
        self._DisableRecord = params.get("DisableRecord")
        self._DisableAudio = params.get("DisableAudio")
        self._PullSmallVideo = params.get("PullSmallVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLayout(AbstractModel):
    """流布局参数

    """

    def __init__(self):
        r"""
        :param _LayoutParams: 流布局配置参数
        :type LayoutParams: :class:`tencentcloud.tiw.v20190919.models.LayoutParams`
        :param _InputStreamId: 视频流ID
流ID的取值含义如下：
1. tic_record_user - 表示当前画面用于显示白板视频流
2. tic_substream - 表示当前画面用于显示辅路视频流
3. 特定用户ID - 表示当前画面用于显示指定用户的视频流
4. 不填 - 表示当前画面用于备选，当有新的视频流加入时，会从这些备选的空位中选择一个没有被占用的位置来显示新的视频流画面
        :type InputStreamId: str
        :param _BackgroundColor: 背景颜色，默认为黑色，格式为RGB格式，如红色为"#FF0000"
        :type BackgroundColor: str
        :param _FillMode: 视频画面填充模式。

0 - 自适应模式，对视频画面进行等比例缩放，在指定区域内显示完整的画面。此模式可能存在黑边。
1 - 全屏模式，对视频画面进行等比例缩放，让画面填充满整个指定区域。此模式不会存在黑边，但会将超出区域的那一部分画面裁剪掉。
        :type FillMode: int
        """
        self._LayoutParams = None
        self._InputStreamId = None
        self._BackgroundColor = None
        self._FillMode = None

    @property
    def LayoutParams(self):
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def InputStreamId(self):
        return self._InputStreamId

    @InputStreamId.setter
    def InputStreamId(self, InputStreamId):
        self._InputStreamId = InputStreamId

    @property
    def BackgroundColor(self):
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor

    @property
    def FillMode(self):
        return self._FillMode

    @FillMode.setter
    def FillMode(self, FillMode):
        self._FillMode = FillMode


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self._LayoutParams = LayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        self._InputStreamId = params.get("InputStreamId")
        self._BackgroundColor = params.get("BackgroundColor")
        self._FillMode = params.get("FillMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeValue(AbstractModel):
    """查询指标返回的时间序列

    """

    def __init__(self):
        r"""
        :param _Time: Unix时间戳，单位秒
        :type Time: int
        :param _Value: 查询指标对应当前时间的值
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskResult(AbstractModel):
    """转码任务结果

    """

    def __init__(self):
        r"""
        :param _ResultUrl: 转码结果地址
        :type ResultUrl: str
        :param _Resolution: 分辨率
        :type Resolution: str
        :param _Title: 标题（一般为文件名）
        :type Title: str
        :param _Pages: 转码页数
        :type Pages: int
        :param _ThumbnailUrl: 缩略图URL前缀，比如，该URL前缀为http://example.com/g0jb42ps49vtebjshilb/，那么动态PPT第1页的缩略图URL为
http://example.com/g0jb42ps49vtebjshilb/1.jpg，其它页以此类推

如果发起文档转码请求参数中带了ThumbnailResolution参数，并且转码类型为动态转码，该参数不为空，其余情况该参数为空字符串
        :type ThumbnailUrl: str
        :param _ThumbnailResolution: 动态转码缩略图生成分辨率
        :type ThumbnailResolution: str
        :param _CompressFileUrl: 转码压缩文件下载的URL，如果发起文档转码请求参数中CompressFileType为空或者不是支持的压缩格式，该参数为空字符串
        :type CompressFileUrl: str
        :param _ErrorCode: 任务失败错误码
        :type ErrorCode: int
        :param _ErrorMsg: 任务失败错误信息
        :type ErrorMsg: str
        """
        self._ResultUrl = None
        self._Resolution = None
        self._Title = None
        self._Pages = None
        self._ThumbnailUrl = None
        self._ThumbnailResolution = None
        self._CompressFileUrl = None
        self._ErrorCode = None
        self._ErrorMsg = None

    @property
    def ResultUrl(self):
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def ThumbnailUrl(self):
        return self._ThumbnailUrl

    @ThumbnailUrl.setter
    def ThumbnailUrl(self, ThumbnailUrl):
        self._ThumbnailUrl = ThumbnailUrl

    @property
    def ThumbnailResolution(self):
        return self._ThumbnailResolution

    @ThumbnailResolution.setter
    def ThumbnailResolution(self, ThumbnailResolution):
        self._ThumbnailResolution = ThumbnailResolution

    @property
    def CompressFileUrl(self):
        return self._CompressFileUrl

    @CompressFileUrl.setter
    def CompressFileUrl(self, CompressFileUrl):
        self._CompressFileUrl = CompressFileUrl

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._ResultUrl = params.get("ResultUrl")
        self._Resolution = params.get("Resolution")
        self._Title = params.get("Title")
        self._Pages = params.get("Pages")
        self._ThumbnailUrl = params.get("ThumbnailUrl")
        self._ThumbnailResolution = params.get("ThumbnailResolution")
        self._CompressFileUrl = params.get("CompressFileUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskSearchResult(AbstractModel):
    """转码任务搜索结果

    """

    def __init__(self):
        r"""
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _TaskId: 任务唯一ID
        :type TaskId: str
        :param _Status: 任务的当前状态
- QUEUED: 正在排队等待转换
- PROCESSING: 转换中
- FINISHED: 转换完成
        :type Status: str
        :param _OriginalFilename: 转码文件原始名称
        :type OriginalFilename: str
        :param _SdkAppId: 用户应用SdkAppId
        :type SdkAppId: int
        :param _Result: 转码任务结果
        :type Result: :class:`tencentcloud.tiw.v20190919.models.TranscodeTaskResult`
        :param _IsStatic: 是否静态转码
        :type IsStatic: bool
        """
        self._CreateTime = None
        self._TaskId = None
        self._Status = None
        self._OriginalFilename = None
        self._SdkAppId = None
        self._Result = None
        self._IsStatic = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OriginalFilename(self):
        return self._OriginalFilename

    @OriginalFilename.setter
    def OriginalFilename(self, OriginalFilename):
        self._OriginalFilename = OriginalFilename

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def IsStatic(self):
        return self._IsStatic

    @IsStatic.setter
    def IsStatic(self, IsStatic):
        self._IsStatic = IsStatic


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._OriginalFilename = params.get("OriginalFilename")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self._Result = TranscodeTaskResult()
            self._Result._deserialize(params.get("Result"))
        self._IsStatic = params.get("IsStatic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageDataItem(AbstractModel):
    """互动白板用量信息

    """

    def __init__(self):
        r"""
        :param _Time: 日期，格式为YYYY-MM-DD
        :type Time: str
        :param _SdkAppId: 白板应用SDKAppID
        :type SdkAppId: int
        :param _SubProduct: 互动白板子产品，请求参数传入的一致
- sp_tiw_board: 互动白板时长
- sp_tiw_dt: 动态转码页数
- sp_tiw_st: 静态转码页数
- sp_tiw_ric: 实时录制时长
        :type SubProduct: str
        :param _Value: 用量值
- 静态转码、动态转码单位为页
- 白板时长、实时录制时长单位为分钟
        :type Value: float
        """
        self._Time = None
        self._SdkAppId = None
        self._SubProduct = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubProduct(self):
        return self._SubProduct

    @SubProduct.setter
    def SubProduct(self, SubProduct):
        self._SubProduct = SubProduct

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._SdkAppId = params.get("SdkAppId")
        self._SubProduct = params.get("SubProduct")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserListItem(AbstractModel):
    """日志查询里返回的白板用户数据

    """

    def __init__(self):
        r"""
        :param _UserId: 房间内的用户ID
        :type UserId: str
        :param _StartTime: 用户在查询时间段内最早出现的时间，Unix时间戳，单位毫秒
        :type StartTime: int
        :param _EndTime: 用户在查询时间段内最晚出现的时间，Unix时间戳，单位毫秒
        :type EndTime: int
        """
        self._UserId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoInfo(AbstractModel):
    """视频信息

    """

    def __init__(self):
        r"""
        :param _VideoPlayTime: 视频开始播放的时间（单位：毫秒）
        :type VideoPlayTime: int
        :param _VideoSize: 视频大小（字节）
        :type VideoSize: int
        :param _VideoFormat: 视频格式
        :type VideoFormat: str
        :param _VideoDuration: 视频播放时长（单位：毫秒）
        :type VideoDuration: int
        :param _VideoUrl: 视频文件URL
        :type VideoUrl: str
        :param _VideoId: 视频文件Id
        :type VideoId: str
        :param _VideoType: 视频流类型 
- 0：摄像头视频 
- 1：屏幕分享视频
- 2：白板视频 
- 3：混流视频
- 4：纯音频（mp3)
        :type VideoType: int
        :param _UserId: 摄像头/屏幕分享视频所属用户的 Id（白板视频为空、混流视频tic_mixstream_房间号_混流布局类型、辅路视频tic_substream_用户Id）
        :type UserId: str
        :param _Width: 视频分辨率的宽
        :type Width: int
        :param _Height: 视频分辨率的高
        :type Height: int
        """
        self._VideoPlayTime = None
        self._VideoSize = None
        self._VideoFormat = None
        self._VideoDuration = None
        self._VideoUrl = None
        self._VideoId = None
        self._VideoType = None
        self._UserId = None
        self._Width = None
        self._Height = None

    @property
    def VideoPlayTime(self):
        return self._VideoPlayTime

    @VideoPlayTime.setter
    def VideoPlayTime(self, VideoPlayTime):
        self._VideoPlayTime = VideoPlayTime

    @property
    def VideoSize(self):
        return self._VideoSize

    @VideoSize.setter
    def VideoSize(self, VideoSize):
        self._VideoSize = VideoSize

    @property
    def VideoFormat(self):
        return self._VideoFormat

    @VideoFormat.setter
    def VideoFormat(self, VideoFormat):
        self._VideoFormat = VideoFormat

    @property
    def VideoDuration(self):
        return self._VideoDuration

    @VideoDuration.setter
    def VideoDuration(self, VideoDuration):
        self._VideoDuration = VideoDuration

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def VideoId(self):
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def VideoType(self):
        return self._VideoType

    @VideoType.setter
    def VideoType(self, VideoType):
        self._VideoType = VideoType

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._VideoPlayTime = params.get("VideoPlayTime")
        self._VideoSize = params.get("VideoSize")
        self._VideoFormat = params.get("VideoFormat")
        self._VideoDuration = params.get("VideoDuration")
        self._VideoUrl = params.get("VideoUrl")
        self._VideoId = params.get("VideoId")
        self._VideoType = params.get("VideoType")
        self._UserId = params.get("UserId")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whiteboard(AbstractModel):
    """实时录制白板参数，例如白板宽高等

    """

    def __init__(self):
        r"""
        :param _Width: 实时录制结果里白板视频宽，取值必须大于等于2，默认为1280
        :type Width: int
        :param _Height: 实时录制结果里白板视频高，取值必须大于等于2，默认为960
        :type Height: int
        :param _InitParam: 白板初始化参数，透传到白板 SDK
        :type InitParam: str
        """
        self._Width = None
        self._Height = None
        self._InitParam = None

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def InitParam(self):
        return self._InitParam

    @InitParam.setter
    def InitParam(self, InitParam):
        self._InitParam = InitParam


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._InitParam = params.get("InitParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardApplicationConfig(AbstractModel):
    """白板应用配置，包括资源存储桶，域名，回调地址，回调密钥等

    """

    def __init__(self):
        r"""
        :param _TaskType: 任务类型

recording: 实时录制
transcode: 文档转码
        :type TaskType: str
        :param _BucketName: 存储桶名字
        :type BucketName: str
        :param _BucketLocation: 存储桶地域
        :type BucketLocation: str
        :param _BucketPrefix: 资源在存储桶中的前缀
        :type BucketPrefix: str
        :param _ResultDomain: 目标CDN域名
        :type ResultDomain: str
        :param _Callback: 回调地址
        :type Callback: str
        :param _CallbackKey: 回调鉴权密钥
        :type CallbackKey: str
        :param _SdkAppId: 配置的应用SdkAppId
        :type SdkAppId: int
        :param _AdminUserId: IM管理员UserId
        :type AdminUserId: str
        :param _AdminUserSig: IM管理员UserSig
        :type AdminUserSig: str
        """
        self._TaskType = None
        self._BucketName = None
        self._BucketLocation = None
        self._BucketPrefix = None
        self._ResultDomain = None
        self._Callback = None
        self._CallbackKey = None
        self._SdkAppId = None
        self._AdminUserId = None
        self._AdminUserSig = None

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketLocation(self):
        return self._BucketLocation

    @BucketLocation.setter
    def BucketLocation(self, BucketLocation):
        self._BucketLocation = BucketLocation

    @property
    def BucketPrefix(self):
        return self._BucketPrefix

    @BucketPrefix.setter
    def BucketPrefix(self, BucketPrefix):
        self._BucketPrefix = BucketPrefix

    @property
    def ResultDomain(self):
        return self._ResultDomain

    @ResultDomain.setter
    def ResultDomain(self, ResultDomain):
        self._ResultDomain = ResultDomain

    @property
    def Callback(self):
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AdminUserId(self):
        return self._AdminUserId

    @AdminUserId.setter
    def AdminUserId(self, AdminUserId):
        self._AdminUserId = AdminUserId

    @property
    def AdminUserSig(self):
        return self._AdminUserSig

    @AdminUserSig.setter
    def AdminUserSig(self, AdminUserSig):
        self._AdminUserSig = AdminUserSig


    def _deserialize(self, params):
        self._TaskType = params.get("TaskType")
        self._BucketName = params.get("BucketName")
        self._BucketLocation = params.get("BucketLocation")
        self._BucketPrefix = params.get("BucketPrefix")
        self._ResultDomain = params.get("ResultDomain")
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._SdkAppId = params.get("SdkAppId")
        self._AdminUserId = params.get("AdminUserId")
        self._AdminUserSig = params.get("AdminUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushBackupParam(AbstractModel):
    """白板推流备份相关请求参数

    """

    def __init__(self):
        r"""
        :param _PushUserId: 用于白板推流服务进房的用户ID，
该ID必须是一个单独的未在SDK中使用的ID，白板推流服务将使用这个用户ID进入房间进行白板推流，若该ID和SDK中使用的ID重复，会导致SDK和录制服务互踢，影响正常推流。
        :type PushUserId: str
        :param _PushUserSig: 与PushUserId对应的签名
        :type PushUserSig: str
        """
        self._PushUserId = None
        self._PushUserSig = None

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId

    @property
    def PushUserSig(self):
        return self._PushUserSig

    @PushUserSig.setter
    def PushUserSig(self, PushUserSig):
        self._PushUserSig = PushUserSig


    def _deserialize(self, params):
        self._PushUserId = params.get("PushUserId")
        self._PushUserSig = params.get("PushUserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushResult(AbstractModel):
    """白板推流任务结果

    """

    def __init__(self):
        r"""
        :param _FinishReason: AUTO - 自动停止推流， USER_CALL - 用户主动调用停止推流
        :type FinishReason: str
        :param _ExceptionCnt: 异常数
        :type ExceptionCnt: int
        :param _RoomId: 房间号
        :type RoomId: int
        :param _GroupId: IM群组ID
        :type GroupId: str
        :param _PushStartTime: 推流真实开始时间
        :type PushStartTime: int
        :param _PushStopTime: 推流结束时间
        :type PushStopTime: int
        :param _IMSyncTime: 白板推流首帧对应的IM时间戳，可用于录制回放时IM聊天消息与白板推流视频进行同步对时。
        :type IMSyncTime: int
        :param _ErrorCode: 任务失败错误码
        :type ErrorCode: int
        :param _ErrorMsg: 错误信息
        :type ErrorMsg: str
        """
        self._FinishReason = None
        self._ExceptionCnt = None
        self._RoomId = None
        self._GroupId = None
        self._PushStartTime = None
        self._PushStopTime = None
        self._IMSyncTime = None
        self._ErrorCode = None
        self._ErrorMsg = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def ExceptionCnt(self):
        return self._ExceptionCnt

    @ExceptionCnt.setter
    def ExceptionCnt(self, ExceptionCnt):
        self._ExceptionCnt = ExceptionCnt

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PushStartTime(self):
        return self._PushStartTime

    @PushStartTime.setter
    def PushStartTime(self, PushStartTime):
        self._PushStartTime = PushStartTime

    @property
    def PushStopTime(self):
        return self._PushStopTime

    @PushStopTime.setter
    def PushStopTime(self, PushStopTime):
        self._PushStopTime = PushStopTime

    @property
    def IMSyncTime(self):
        return self._IMSyncTime

    @IMSyncTime.setter
    def IMSyncTime(self, IMSyncTime):
        self._IMSyncTime = IMSyncTime

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._ExceptionCnt = params.get("ExceptionCnt")
        self._RoomId = params.get("RoomId")
        self._GroupId = params.get("GroupId")
        self._PushStartTime = params.get("PushStartTime")
        self._PushStopTime = params.get("PushStopTime")
        self._IMSyncTime = params.get("IMSyncTime")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WhiteboardPushTaskSearchResult(AbstractModel):
    """实时录制任务搜索结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一ID
        :type TaskId: str
        :param _Status: 白板推流任务状态
- PREPARED: 推流在准备阶段
- PUSHING: 正在推流
- STOPPED：推流已停止
        :type Status: str
        :param _RoomId: 白板推流房间号
        :type RoomId: int
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _SdkAppId: 用户应用SdkAppId
        :type SdkAppId: int
        :param _Result: 白板推流结果
        :type Result: :class:`tencentcloud.tiw.v20190919.models.WhiteboardPushResult`
        :param _PushUserId: 白板推流用户ID
        :type PushUserId: str
        """
        self._TaskId = None
        self._Status = None
        self._RoomId = None
        self._CreateTime = None
        self._SdkAppId = None
        self._Result = None
        self._PushUserId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def PushUserId(self):
        return self._PushUserId

    @PushUserId.setter
    def PushUserId(self, PushUserId):
        self._PushUserId = PushUserId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RoomId = params.get("RoomId")
        self._CreateTime = params.get("CreateTime")
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Result") is not None:
            self._Result = WhiteboardPushResult()
            self._Result._deserialize(params.get("Result"))
        self._PushUserId = params.get("PushUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        