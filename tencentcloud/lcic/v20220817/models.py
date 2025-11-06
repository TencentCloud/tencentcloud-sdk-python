# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AddGroupMemberRequest(AbstractModel):
    r"""AddGroupMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _MemberIds: 成员列表，最大值200
        :type MemberIds: list of str
        """
        self._GroupId = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupId(self):
        r"""群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        r"""成员列表，最大值200
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddGroupMemberResponse(AbstractModel):
    r"""AddGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AnswerInfo(AbstractModel):
    r"""房间问答答案详情

    """

    def __init__(self):
        r"""
        :param _Name: 用户名
        :type Name: str
        :param _Answer: 答案（按照位表示是否选择，如0x1表示选择A，0x11表示选择AB）
        :type Answer: int
        :param _CostTime: 答题用时
        :type CostTime: int
        :param _UserId: 用户ID
        :type UserId: str
        :param _IsCorrect: 答案是否正确（1正确0错误）
        :type IsCorrect: int
        """
        self._Name = None
        self._Answer = None
        self._CostTime = None
        self._UserId = None
        self._IsCorrect = None

    @property
    def Name(self):
        r"""用户名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Answer(self):
        r"""答案（按照位表示是否选择，如0x1表示选择A，0x11表示选择AB）
        :rtype: int
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CostTime(self):
        r"""答题用时
        :rtype: int
        """
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsCorrect(self):
        r"""答案是否正确（1正确0错误）
        :rtype: int
        """
        return self._IsCorrect

    @IsCorrect.setter
    def IsCorrect(self, IsCorrect):
        self._IsCorrect = IsCorrect


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Answer = params.get("Answer")
        self._CostTime = params.get("CostTime")
        self._UserId = params.get("UserId")
        self._IsCorrect = params.get("IsCorrect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnswerStat(AbstractModel):
    r"""每个选项答题人数统计

    """

    def __init__(self):
        r"""
        :param _Answer: 选项（按照位表示是否选择，如0x1表示选择A，0x11表示选择AB）
        :type Answer: int
        :param _Count: 答题人数
        :type Count: int
        """
        self._Answer = None
        self._Count = None

    @property
    def Answer(self):
        r"""选项（按照位表示是否选择，如0x1表示选择A，0x11表示选择AB）
        :rtype: int
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Count(self):
        r"""答题人数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Answer = params.get("Answer")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppConfig(AbstractModel):
    r"""应用配置信息

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _AppName: 应用名称
        :type AppName: str
        :param _State: 应用状态 1正常 2停用
        :type State: int
        :param _AppVersion: 1试用 2轻量版 3标准版 4旗舰版
        :type AppVersion: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _Callback: 回调
        :type Callback: str
        :param _CallbackKey: 回调Key
        :type CallbackKey: str
        """
        self._ApplicationId = None
        self._AppName = None
        self._State = None
        self._AppVersion = None
        self._CreatedAt = None
        self._Callback = None
        self._CallbackKey = None

    @property
    def ApplicationId(self):
        r"""应用ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppName(self):
        r"""应用名称
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def State(self):
        r"""应用状态 1正常 2停用
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AppVersion(self):
        r"""1试用 2轻量版 3标准版 4旗舰版
        :rtype: int
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Callback(self):
        r"""回调
        :rtype: str
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        r"""回调Key
        :rtype: str
        """
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._AppName = params.get("AppName")
        self._State = params.get("State")
        self._AppVersion = params.get("AppVersion")
        self._CreatedAt = params.get("CreatedAt")
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppCustomContent(AbstractModel):
    r"""应用自定义内容

    """

    def __init__(self):
        r"""
        :param _Scene: 场景参数，一个应用下可以设置多个不同场景。
        :type Scene: str
        :param _LogoUrl: logo地址，用于上课时展示的课堂或平台图标，支持开发商自定义业务品牌展示。
        :type LogoUrl: str
        :param _HomeUrl: HomeUrl：主页地址，用于上课结束后课堂跳转，支持跳转到自己的业务系统。如果配置为空则下课后关闭课堂页面。
        :type HomeUrl: str
        :param _JsUrl: JsUrl ：自定义js。针对应用用于开发上自定义课堂界面、模块功能、监控操作，支持数据请求与响应处理。
        :type JsUrl: str
        :param _CssUrl: Css : 自定义的css。针对应用用于支持课堂界面的、模块的UI渲染修改、皮肤配色修改、功能模块的隐藏和展示。
        :type CssUrl: str
        """
        self._Scene = None
        self._LogoUrl = None
        self._HomeUrl = None
        self._JsUrl = None
        self._CssUrl = None

    @property
    def Scene(self):
        r"""场景参数，一个应用下可以设置多个不同场景。
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LogoUrl(self):
        r"""logo地址，用于上课时展示的课堂或平台图标，支持开发商自定义业务品牌展示。
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def HomeUrl(self):
        r"""HomeUrl：主页地址，用于上课结束后课堂跳转，支持跳转到自己的业务系统。如果配置为空则下课后关闭课堂页面。
        :rtype: str
        """
        return self._HomeUrl

    @HomeUrl.setter
    def HomeUrl(self, HomeUrl):
        self._HomeUrl = HomeUrl

    @property
    def JsUrl(self):
        r"""JsUrl ：自定义js。针对应用用于开发上自定义课堂界面、模块功能、监控操作，支持数据请求与响应处理。
        :rtype: str
        """
        return self._JsUrl

    @JsUrl.setter
    def JsUrl(self, JsUrl):
        self._JsUrl = JsUrl

    @property
    def CssUrl(self):
        r"""Css : 自定义的css。针对应用用于支持课堂界面的、模块的UI渲染修改、皮肤配色修改、功能模块的隐藏和展示。
        :rtype: str
        """
        return self._CssUrl

    @CssUrl.setter
    def CssUrl(self, CssUrl):
        self._CssUrl = CssUrl


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._LogoUrl = params.get("LogoUrl")
        self._HomeUrl = params.get("HomeUrl")
        self._JsUrl = params.get("JsUrl")
        self._CssUrl = params.get("CssUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackgroundPictureConfig(AbstractModel):
    r"""背景图片配置

    """

    def __init__(self):
        r"""
        :param _Url: 背景图片的url
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""背景图片的url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddGroupMemberRequest(AbstractModel):
    r"""BatchAddGroupMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 待添加群组ID列表，最大值100
        :type GroupIds: list of str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _MemberIds: 待添加成员列表，最大值200
        :type MemberIds: list of str
        """
        self._GroupIds = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupIds(self):
        r"""待添加群组ID列表，最大值100
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        r"""待添加成员列表，最大值200
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddGroupMemberResponse(AbstractModel):
    r"""BatchAddGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchCreateGroupWithMembersRequest(AbstractModel):
    r"""BatchCreateGroupWithMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _GroupBaseInfos: 批量创建群组基础信息，最大长度限制256
        :type GroupBaseInfos: list of GroupBaseInfo
        :param _MemberIds: 群组绑定的成员列表，一次性最多200个
        :type MemberIds: list of str
        """
        self._SdkAppId = None
        self._GroupBaseInfos = None
        self._MemberIds = None

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def GroupBaseInfos(self):
        r"""批量创建群组基础信息，最大长度限制256
        :rtype: list of GroupBaseInfo
        """
        return self._GroupBaseInfos

    @GroupBaseInfos.setter
    def GroupBaseInfos(self, GroupBaseInfos):
        self._GroupBaseInfos = GroupBaseInfos

    @property
    def MemberIds(self):
        r"""群组绑定的成员列表，一次性最多200个
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("GroupBaseInfos") is not None:
            self._GroupBaseInfos = []
            for item in params.get("GroupBaseInfos"):
                obj = GroupBaseInfo()
                obj._deserialize(item)
                self._GroupBaseInfos.append(obj)
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateGroupWithMembersResponse(AbstractModel):
    r"""BatchCreateGroupWithMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 新创建群组ID列表，与输入创建参数顺序一致
        :type GroupIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupIds = None
        self._RequestId = None

    @property
    def GroupIds(self):
        r"""新创建群组ID列表，与输入创建参数顺序一致
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._RequestId = params.get("RequestId")


class BatchCreateRoomRequest(AbstractModel):
    r"""BatchCreateRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码平台的SdkAppId。
        :type SdkAppId: int
        :param _RoomInfos: 批量创建课堂的配置信息
        :type RoomInfos: list of RoomInfo
        """
        self._SdkAppId = None
        self._RoomInfos = None

    @property
    def SdkAppId(self):
        r"""低代码平台的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomInfos(self):
        r"""批量创建课堂的配置信息
        :rtype: list of RoomInfo
        """
        return self._RoomInfos

    @RoomInfos.setter
    def RoomInfos(self, RoomInfos):
        self._RoomInfos = RoomInfos


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("RoomInfos") is not None:
            self._RoomInfos = []
            for item in params.get("RoomInfos"):
                obj = RoomInfo()
                obj._deserialize(item)
                self._RoomInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateRoomResponse(AbstractModel):
    r"""BatchCreateRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomIds: 创建成功课堂ID，与传入课堂信息顺序一致
        :type RoomIds: list of int non-negative
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoomIds = None
        self._RequestId = None

    @property
    def RoomIds(self):
        r"""创建成功课堂ID，与传入课堂信息顺序一致
        :rtype: list of int non-negative
        """
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._RequestId = params.get("RequestId")


class BatchDeleteGroupMemberRequest(AbstractModel):
    r"""BatchDeleteGroupMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 待添加群组ID列表，最大值100
        :type GroupIds: list of str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _MemberIds: 待添加成员列表，最大值256
        :type MemberIds: list of str
        """
        self._GroupIds = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupIds(self):
        r"""待添加群组ID列表，最大值100
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        r"""待添加成员列表，最大值256
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteGroupMemberResponse(AbstractModel):
    r"""BatchDeleteGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchDeleteRecordRequest(AbstractModel):
    r"""BatchDeleteRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomIds: 房间ID列表
        :type RoomIds: list of int
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        """
        self._RoomIds = None
        self._SdkAppId = None

    @property
    def RoomIds(self):
        r"""房间ID列表
        :rtype: list of int
        """
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteRecordResponse(AbstractModel):
    r"""BatchDeleteRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomIds: 本次操作删除成功的房间ID列表。如果入参列表中某个房间ID的录制文件已经删除，则出参列表中无对应的房间ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomIds: list of int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoomIds = None
        self._RequestId = None

    @property
    def RoomIds(self):
        r"""本次操作删除成功的房间ID列表。如果入参列表中某个房间ID的录制文件已经删除，则出参列表中无对应的房间ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._RequestId = params.get("RequestId")


class BatchDescribeDocumentRequest(AbstractModel):
    r"""BatchDescribeDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _Page: 分页查询当前页数，从1开始递增
        :type Page: int
        :param _Limit: 每页数据量，最大200
        :type Limit: int
        :param _Permission: 课件权限。[0]：获取owner的私有课件；[1]：获取owner的公开课件; [0,1]：则获取owner的私有课件和公开课件；[2]：获取owner的私有课件和所有人(包括owner)的公开课件
        :type Permission: list of int non-negative
        :param _Owner: 课件所有者的user_id，不填默认获取SdkAppId下所有课件
        :type Owner: str
        :param _Keyword: 课件名称搜索词
        :type Keyword: str
        :param _DocumentId: 课件id列表，从列表中查询，忽略错误的id
        :type DocumentId: list of str
        """
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._Permission = None
        self._Owner = None
        self._Keyword = None
        self._DocumentId = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页数据量，最大200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        r"""课件权限。[0]：获取owner的私有课件；[1]：获取owner的公开课件; [0,1]：则获取owner的私有课件和公开课件；[2]：获取owner的私有课件和所有人(包括owner)的公开课件
        :rtype: list of int non-negative
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        r"""课件所有者的user_id，不填默认获取SdkAppId下所有课件
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Keyword(self):
        r"""课件名称搜索词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DocumentId(self):
        r"""课件id列表，从列表中查询，忽略错误的id
        :rtype: list of str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Permission = params.get("Permission")
        self._Owner = params.get("Owner")
        self._Keyword = params.get("Keyword")
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeDocumentResponse(AbstractModel):
    r"""BatchDescribeDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合查询条件文档总数
        :type Total: int
        :param _Documents: 文档信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Documents: list of DocumentInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Documents = None
        self._RequestId = None

    @property
    def Total(self):
        r"""符合查询条件文档总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Documents(self):
        r"""文档信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DocumentInfo
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._RequestId = params.get("RequestId")


class BatchRegisterRequest(AbstractModel):
    r"""BatchRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 批量注册用户信息列表
        :type Users: list of BatchUserRequest
        """
        self._Users = None

    @property
    def Users(self):
        r"""批量注册用户信息列表
        :rtype: list of BatchUserRequest
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = BatchUserRequest()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterResponse(AbstractModel):
    r"""BatchRegister返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 注册成功的用户列表
        :type Users: list of BatchUserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        r"""注册成功的用户列表
        :rtype: list of BatchUserInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = BatchUserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class BatchUserInfo(AbstractModel):
    r"""批量注册用户信息

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        :param _UserId: 用户ID。
        :type UserId: str
        :param _OriginId: 用户在客户系统的Id。 若用户注册时该字段为空，则默认为 UserId 值一致。
        :type OriginId: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._OriginId = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。

        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        r"""用户ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def OriginId(self):
        r"""用户在客户系统的Id。 若用户注册时该字段为空，则默认为 UserId 值一致。
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUserRequest(AbstractModel):
    r"""用户注册请求信息

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        :param _Name: 用户名称。

        :type Name: str
        :param _OriginId: 用户在客户系统的Id，需要在同一应用下唯一。入参为空时默认赋值为UserId
。
        :type OriginId: str
        :param _Avatar: 用户头像。

        :type Avatar: str
        """
        self._SdkAppId = None
        self._Name = None
        self._OriginId = None
        self._Avatar = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。

        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        r"""用户名称。

        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginId(self):
        r"""用户在客户系统的Id，需要在同一应用下唯一。入参为空时默认赋值为UserId
。
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Avatar(self):
        r"""用户头像。

        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._OriginId = params.get("OriginId")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomRequest(AbstractModel):
    r"""BindDocumentToRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        :param _DocumentId: 文档ID。
        :type DocumentId: str
        :param _BindType: 绑定类型。后台可透传到客户端，默认为0。除以下例值外支持自定义该字段，并在前端实现相应业务逻辑，示例参考：
示例值：0，仅绑定课件到房间
示例值：1，绑定课件到房间后，默认展示课件
        :type BindType: int
        """
        self._RoomId = None
        self._DocumentId = None
        self._BindType = None

    @property
    def RoomId(self):
        r"""房间ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DocumentId(self):
        r"""文档ID。
        :rtype: str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def BindType(self):
        r"""绑定类型。后台可透传到客户端，默认为0。除以下例值外支持自定义该字段，并在前端实现相应业务逻辑，示例参考：
示例值：0，仅绑定课件到房间
示例值：1，绑定课件到房间后，默认展示课件
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._DocumentId = params.get("DocumentId")
        self._BindType = params.get("BindType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindDocumentToRoomResponse(AbstractModel):
    r"""BindDocumentToRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ClassScoreItem(AbstractModel):
    r"""课堂评分字段

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂iD
        :type RoomId: int
        :param _UserId: 用户ID
        :type UserId: str
        :param _CreateTime: 评分时间
        :type CreateTime: int
        :param _Score: 课堂评分
        :type Score: int
        :param _ScoreMsg: 课堂评价
        :type ScoreMsg: str
        """
        self._RoomId = None
        self._UserId = None
        self._CreateTime = None
        self._Score = None
        self._ScoreMsg = None

    @property
    def RoomId(self):
        r"""课堂iD
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CreateTime(self):
        r"""评分时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Score(self):
        r"""课堂评分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def ScoreMsg(self):
        r"""课堂评价
        :rtype: str
        """
        return self._ScoreMsg

    @ScoreMsg.setter
    def ScoreMsg(self, ScoreMsg):
        self._ScoreMsg = ScoreMsg


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._CreateTime = params.get("CreateTime")
        self._Score = params.get("Score")
        self._ScoreMsg = params.get("ScoreMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentRequest(AbstractModel):
    r"""CreateDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _DocumentUrl: 文档地址。
        :type DocumentUrl: str
        :param _DocumentName: 文档名称。
        :type DocumentName: str
        :param _Owner: 文档所有者的Id
        :type Owner: str
        :param _TranscodeType: 转码类型，可以有如下取值：
0 无需转码（默认），bmp，jpg，jpeg，png，gif
1 需要转码的文档，ppt，pptx，pdf，doc，docx，xls，xlsx
2 需要转码的视频，mp4，3pg，mpeg，avi，flv，wmv，rm，h264等
2 需要转码的音频，mp3，wav，wma，aac，flac，opus
3 备用转码，建议 WPS 制作的课件使用此方式转码，保证课件显示效果
请注意，待录制的页面中任何视频的分辨率不能超过页面录制最大分辨率（1920*1080），否则将导致录制失败。
 - ppt课件内嵌视频或纯视频课件，在上传课件时，云api会进行转码，以确保视频分辨率不超过页面录制最大分辨率。
 - h5课件中内嵌音视频内容时，由于平台无法获取视频内容，因此在制作环节需确保视频分辨率不超过页面录制最大分辨率。

        :type TranscodeType: int
        :param _Permission: 权限，可以有如下取值：
0 私有文档（默认）
1 公共文档
        :type Permission: int
        :param _DocumentType: 文档后缀名。
        :type DocumentType: str
        :param _DocumentSize: 文档大小，单位 字节
        :type DocumentSize: int
        :param _AutoHandleUnsupportedElement: 是否对不支持元素开启自动处理的功能。默认关闭。
自动处理的元素如下：
1. 墨迹：移除不支持的墨迹（例如WPS墨迹）
2. 自动翻页：移除PPT上所有自动翻页设置，并设置为单击鼠标翻页
3. 已损坏音视频：移除PPT上对损坏音视频的引用
        :type AutoHandleUnsupportedElement: bool
        :param _MinScaleResolution: 转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率。该参数仅对TranscodeType=1的课件生效。示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
示例值：1280x720
        :type MinScaleResolution: str
        """
        self._SdkAppId = None
        self._DocumentUrl = None
        self._DocumentName = None
        self._Owner = None
        self._TranscodeType = None
        self._Permission = None
        self._DocumentType = None
        self._DocumentSize = None
        self._AutoHandleUnsupportedElement = None
        self._MinScaleResolution = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def DocumentUrl(self):
        r"""文档地址。
        :rtype: str
        """
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        r"""文档名称。
        :rtype: str
        """
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        r"""文档所有者的Id
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def TranscodeType(self):
        r"""转码类型，可以有如下取值：
0 无需转码（默认），bmp，jpg，jpeg，png，gif
1 需要转码的文档，ppt，pptx，pdf，doc，docx，xls，xlsx
2 需要转码的视频，mp4，3pg，mpeg，avi，flv，wmv，rm，h264等
2 需要转码的音频，mp3，wav，wma，aac，flac，opus
3 备用转码，建议 WPS 制作的课件使用此方式转码，保证课件显示效果
请注意，待录制的页面中任何视频的分辨率不能超过页面录制最大分辨率（1920*1080），否则将导致录制失败。
 - ppt课件内嵌视频或纯视频课件，在上传课件时，云api会进行转码，以确保视频分辨率不超过页面录制最大分辨率。
 - h5课件中内嵌音视频内容时，由于平台无法获取视频内容，因此在制作环节需确保视频分辨率不超过页面录制最大分辨率。

        :rtype: int
        """
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def Permission(self):
        r"""权限，可以有如下取值：
0 私有文档（默认）
1 公共文档
        :rtype: int
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def DocumentType(self):
        r"""文档后缀名。
        :rtype: str
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        r"""文档大小，单位 字节
        :rtype: int
        """
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def AutoHandleUnsupportedElement(self):
        r"""是否对不支持元素开启自动处理的功能。默认关闭。
自动处理的元素如下：
1. 墨迹：移除不支持的墨迹（例如WPS墨迹）
2. 自动翻页：移除PPT上所有自动翻页设置，并设置为单击鼠标翻页
3. 已损坏音视频：移除PPT上对损坏音视频的引用
        :rtype: bool
        """
        return self._AutoHandleUnsupportedElement

    @AutoHandleUnsupportedElement.setter
    def AutoHandleUnsupportedElement(self, AutoHandleUnsupportedElement):
        self._AutoHandleUnsupportedElement = AutoHandleUnsupportedElement

    @property
    def MinScaleResolution(self):
        r"""转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率。该参数仅对TranscodeType=1的课件生效。示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
示例值：1280x720
        :rtype: str
        """
        return self._MinScaleResolution

    @MinScaleResolution.setter
    def MinScaleResolution(self, MinScaleResolution):
        self._MinScaleResolution = MinScaleResolution


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._DocumentUrl = params.get("DocumentUrl")
        self._DocumentName = params.get("DocumentName")
        self._Owner = params.get("Owner")
        self._TranscodeType = params.get("TranscodeType")
        self._Permission = params.get("Permission")
        self._DocumentType = params.get("DocumentType")
        self._DocumentSize = params.get("DocumentSize")
        self._AutoHandleUnsupportedElement = params.get("AutoHandleUnsupportedElement")
        self._MinScaleResolution = params.get("MinScaleResolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentResponse(AbstractModel):
    r"""CreateDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档ID。
        :type DocumentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocumentId = None
        self._RequestId = None

    @property
    def DocumentId(self):
        r"""文档ID。
        :rtype: str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._RequestId = params.get("RequestId")


class CreateGroupWithMembersRequest(AbstractModel):
    r"""CreateGroupWithMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 待创建群组名称
        :type GroupName: str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _TeacherId: 默认绑定主讲老师ID
        :type TeacherId: str
        :param _MemberIds: 群组成员列表,一次性最多200个
        :type MemberIds: list of str
        """
        self._GroupName = None
        self._SdkAppId = None
        self._TeacherId = None
        self._MemberIds = None

    @property
    def GroupName(self):
        r"""待创建群组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherId(self):
        r"""默认绑定主讲老师ID
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def MemberIds(self):
        r"""群组成员列表,一次性最多200个
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._SdkAppId = params.get("SdkAppId")
        self._TeacherId = params.get("TeacherId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupWithMembersResponse(AbstractModel):
    r"""CreateGroupWithMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建成功群组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""创建成功群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateGroupWithSubGroupRequest(AbstractModel):
    r"""CreateGroupWithSubGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 待创建的新群组名
        :type GroupName: str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _SubGroupIds: 子群组ID列表，子群组ID不能重复，最多40个
        :type SubGroupIds: list of str
        :param _TeacherId: 群组默认主讲老师ID
        :type TeacherId: str
        """
        self._GroupName = None
        self._SdkAppId = None
        self._SubGroupIds = None
        self._TeacherId = None

    @property
    def GroupName(self):
        r"""待创建的新群组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubGroupIds(self):
        r"""子群组ID列表，子群组ID不能重复，最多40个
        :rtype: list of str
        """
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds

    @property
    def TeacherId(self):
        r"""群组默认主讲老师ID
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._SdkAppId = params.get("SdkAppId")
        self._SubGroupIds = params.get("SubGroupIds")
        self._TeacherId = params.get("TeacherId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupWithSubGroupResponse(AbstractModel):
    r"""CreateGroupWithSubGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 新创建群组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""新创建群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateRoomRequest(AbstractModel):
    r"""CreateRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 课堂名称。
字符数不超过256
        :type Name: str
        :param _StartTime: 预定的课堂开始时间，unix时间戳（秒）。
        :type StartTime: int
        :param _EndTime: 预定的课堂结束时间，unix时间戳（秒）。
        :type EndTime: int
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _Resolution: 头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
注意：连麦人数（MaxMicNumber）>6时，仅可使用标清
        :type Resolution: int
        :param _MaxMicNumber: 设置课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。该取值影响计费，请根据业务实际情况设置。计费规则见“购买指南”下“计费概述”。
        :type MaxMicNumber: int
        :param _SubType: 课堂子类型，可以有以下取值：videodoc 文档+视频video 纯视频
        :type SubType: str
        :param _TeacherId: 老师ID。通过[注册用户]接口获取的UserId。指定后该用户在房间内拥有老师权限。
        :type TeacherId: str
        :param _AutoMic: 进入课堂时是否自动连麦。可以有以下取值：
0 不自动连麦（需要手动申请上麦，默认值）
1 自动连麦
        :type AutoMic: int
        :param _TurnOffMic: 释放音视频权限后是否自动取消连麦。可以有以下取值：
0 自动取消连麦（默认值）
1 保持连麦状态
        :type TurnOffMic: int
        :param _AudioQuality: 声音音质。可以有以下取值：
0：流畅模式（默认值），占用更小的带宽、拥有更好的降噪效果，适用于1对1、小班教学、多人音视频会议等场景。
1：高音质模式，适合需要高保真传输音乐的场景，但降噪效果会被削弱，适用于音乐教学场景。
        :type AudioQuality: int
        :param _DisableRecord: 录制方式，可以有以下取值：0 开启自动录制（默认值）1  禁止录制2 开启手动录制 注： - 如果该配置取值为0，录制将从上课后开始，课堂结束后停止。 - 如果该配置取值为2，需通过startRecord、stopRecord接口控制录制的开始和结束。 
        :type DisableRecord: int
        :param _Assistants: 助教Id列表。通过[注册用户]接口获取的UserId。指定后该用户在房间内拥有助教权限。
        :type Assistants: list of str
        :param _RTCAudienceNumber: rtc人数。
        :type RTCAudienceNumber: int
        :param _AudienceType: 观看类型。互动观看 （默认）
        :type AudienceType: int
        :param _RecordLayout: 录制模板。未配置时默认取值0。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :type RecordLayout: int
        :param _GroupId: 课堂绑定的群组ID,非空时限制组成员进入
        :type GroupId: str
        :param _EnableDirectControl: 是否允许老师/助教直接控制学生的摄像头/麦克风。可以有以下取值：
0 不允许直接控制（需同意，默认值）
1 允许直接控制（无需同意）
        :type EnableDirectControl: int
        :param _InteractionMode: 开启专注模式。
0 收看全部角色音视频(默认)
1 只看老师和助教
        :type InteractionMode: int
        :param _VideoOrientation: 横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :type VideoOrientation: int
        :param _IsGradingRequiredPostClass: 开启课后评分。 0：不开启(默认)  1：开启
        :type IsGradingRequiredPostClass: int
        :param _RoomType: 课堂类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (预留参数，暂未开放); 3 圆桌会议 注：大班课的布局(layout)只有三分屏
        :type RoomType: int
        :param _Guests: 嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :type Guests: list of str
        :param _EndDelayTime: 拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :type EndDelayTime: int
        :param _LiveType: 直播类型：0 常规（默认）1 伪直播 2 RTMP推流直播
        :type LiveType: int
        :param _RecordLiveUrl: 伪直播链接。 支持的协议以及格式： 协议：HTTP、HTTPS、RTMP、HLS 。格式：FLV、MP3、MP4、MPEG-TS、MOV、MKV、M4A。视频编码：H.264、VP8。音频编码：AAC、OPUS。
        :type RecordLiveUrl: str
        :param _EnableAutoStart: 是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1或2的时候有效
        :type EnableAutoStart: int
        :param _RecordBackground: 录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :type RecordBackground: str
        :param _RecordScene: 录制自定义场景。注意：仅recordlayout=9的时候此参数有效。需注意各类参数配置正确能够生效。不然会造成录制失败，失败后无法补救。数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。

自定义场景参数的含义。如下：
     scene：自定义js/css对应的场景值。如scene=recordScene，会加载 recordScene 场景对应的 js/css，这样就可以自定义录制页面的元素。 
    lng：录制页面对应的语种。如lng=en，则录制界面为en。（枚举值：en,zh，zh-TW，jp，ar，kr，vi）
     customToken：录制页面中涉及客户自己的服务需要鉴权时进行配置。一般情况下，无需配置。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _RecordStream: 录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :type RecordStream: int
        :param _WhiteBoardSnapshotMode: 板书截图生成类型。0 不生成板书（默认）；1 全量模式；2 单页去重模式
        :type WhiteBoardSnapshotMode: int
        :param _SubtitlesTranscription: 字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :type SubtitlesTranscription: int
        :param _RecordMerge: 录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :type RecordMerge: int
        """
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._SubType = None
        self._TeacherId = None
        self._AutoMic = None
        self._TurnOffMic = None
        self._AudioQuality = None
        self._DisableRecord = None
        self._Assistants = None
        self._RTCAudienceNumber = None
        self._AudienceType = None
        self._RecordLayout = None
        self._GroupId = None
        self._EnableDirectControl = None
        self._InteractionMode = None
        self._VideoOrientation = None
        self._IsGradingRequiredPostClass = None
        self._RoomType = None
        self._Guests = None
        self._EndDelayTime = None
        self._LiveType = None
        self._RecordLiveUrl = None
        self._EnableAutoStart = None
        self._RecordBackground = None
        self._RecordScene = None
        self._RecordLang = None
        self._RecordStream = None
        self._WhiteBoardSnapshotMode = None
        self._SubtitlesTranscription = None
        self._RecordMerge = None

    @property
    def Name(self):
        r"""课堂名称。
字符数不超过256
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        r"""预定的课堂开始时间，unix时间戳（秒）。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""预定的课堂结束时间，unix时间戳（秒）。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Resolution(self):
        r"""头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
注意：连麦人数（MaxMicNumber）>6时，仅可使用标清
        :rtype: int
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        r"""设置课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。该取值影响计费，请根据业务实际情况设置。计费规则见“购买指南”下“计费概述”。
        :rtype: int
        """
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def SubType(self):
        r"""课堂子类型，可以有以下取值：videodoc 文档+视频video 纯视频
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TeacherId(self):
        r"""老师ID。通过[注册用户]接口获取的UserId。指定后该用户在房间内拥有老师权限。
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def AutoMic(self):
        r"""进入课堂时是否自动连麦。可以有以下取值：
0 不自动连麦（需要手动申请上麦，默认值）
1 自动连麦
        :rtype: int
        """
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def TurnOffMic(self):
        r"""释放音视频权限后是否自动取消连麦。可以有以下取值：
0 自动取消连麦（默认值）
1 保持连麦状态
        :rtype: int
        """
        return self._TurnOffMic

    @TurnOffMic.setter
    def TurnOffMic(self, TurnOffMic):
        self._TurnOffMic = TurnOffMic

    @property
    def AudioQuality(self):
        r"""声音音质。可以有以下取值：
0：流畅模式（默认值），占用更小的带宽、拥有更好的降噪效果，适用于1对1、小班教学、多人音视频会议等场景。
1：高音质模式，适合需要高保真传输音乐的场景，但降噪效果会被削弱，适用于音乐教学场景。
        :rtype: int
        """
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def DisableRecord(self):
        r"""录制方式，可以有以下取值：0 开启自动录制（默认值）1  禁止录制2 开启手动录制 注： - 如果该配置取值为0，录制将从上课后开始，课堂结束后停止。 - 如果该配置取值为2，需通过startRecord、stopRecord接口控制录制的开始和结束。 
        :rtype: int
        """
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        r"""助教Id列表。通过[注册用户]接口获取的UserId。指定后该用户在房间内拥有助教权限。
        :rtype: list of str
        """
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RTCAudienceNumber(self):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        r"""rtc人数。
        :rtype: int
        """
        return self._RTCAudienceNumber

    @RTCAudienceNumber.setter
    def RTCAudienceNumber(self, RTCAudienceNumber):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        self._RTCAudienceNumber = RTCAudienceNumber

    @property
    def AudienceType(self):
        r"""观看类型。互动观看 （默认）
        :rtype: int
        """
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def RecordLayout(self):
        r"""录制模板。未配置时默认取值0。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :rtype: int
        """
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def GroupId(self):
        r"""课堂绑定的群组ID,非空时限制组成员进入
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        r"""是否允许老师/助教直接控制学生的摄像头/麦克风。可以有以下取值：
0 不允许直接控制（需同意，默认值）
1 允许直接控制（无需同意）
        :rtype: int
        """
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        r"""开启专注模式。
0 收看全部角色音视频(默认)
1 只看老师和助教
        :rtype: int
        """
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        r"""横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :rtype: int
        """
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        r"""开启课后评分。 0：不开启(默认)  1：开启
        :rtype: int
        """
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        r"""课堂类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (预留参数，暂未开放); 3 圆桌会议 注：大班课的布局(layout)只有三分屏
        :rtype: int
        """
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def Guests(self):
        r"""嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :rtype: list of str
        """
        return self._Guests

    @Guests.setter
    def Guests(self, Guests):
        self._Guests = Guests

    @property
    def EndDelayTime(self):
        r"""拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :rtype: int
        """
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        r"""直播类型：0 常规（默认）1 伪直播 2 RTMP推流直播
        :rtype: int
        """
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        r"""伪直播链接。 支持的协议以及格式： 协议：HTTP、HTTPS、RTMP、HLS 。格式：FLV、MP3、MP4、MPEG-TS、MOV、MKV、M4A。视频编码：H.264、VP8。音频编码：AAC、OPUS。
        :rtype: str
        """
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        r"""是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1或2的时候有效
        :rtype: int
        """
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        r"""录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :rtype: str
        """
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RecordScene(self):
        r"""录制自定义场景。注意：仅recordlayout=9的时候此参数有效。需注意各类参数配置正确能够生效。不然会造成录制失败，失败后无法补救。数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。

自定义场景参数的含义。如下：
     scene：自定义js/css对应的场景值。如scene=recordScene，会加载 recordScene 场景对应的 js/css，这样就可以自定义录制页面的元素。 
    lng：录制页面对应的语种。如lng=en，则录制界面为en。（枚举值：en,zh，zh-TW，jp，ar，kr，vi）
     customToken：录制页面中涉及客户自己的服务需要鉴权时进行配置。一般情况下，无需配置。
        :rtype: str
        """
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        r"""录制自定义语言，仅recordlayout=9的时候此参数有效
        :rtype: str
        """
        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        self._RecordLang = RecordLang

    @property
    def RecordStream(self):
        r"""录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :rtype: int
        """
        return self._RecordStream

    @RecordStream.setter
    def RecordStream(self, RecordStream):
        self._RecordStream = RecordStream

    @property
    def WhiteBoardSnapshotMode(self):
        r"""板书截图生成类型。0 不生成板书（默认）；1 全量模式；2 单页去重模式
        :rtype: int
        """
        return self._WhiteBoardSnapshotMode

    @WhiteBoardSnapshotMode.setter
    def WhiteBoardSnapshotMode(self, WhiteBoardSnapshotMode):
        self._WhiteBoardSnapshotMode = WhiteBoardSnapshotMode

    @property
    def SubtitlesTranscription(self):
        r"""字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :rtype: int
        """
        return self._SubtitlesTranscription

    @SubtitlesTranscription.setter
    def SubtitlesTranscription(self, SubtitlesTranscription):
        self._SubtitlesTranscription = SubtitlesTranscription

    @property
    def RecordMerge(self):
        r"""录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :rtype: int
        """
        return self._RecordMerge

    @RecordMerge.setter
    def RecordMerge(self, RecordMerge):
        self._RecordMerge = RecordMerge


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._SubType = params.get("SubType")
        self._TeacherId = params.get("TeacherId")
        self._AutoMic = params.get("AutoMic")
        self._TurnOffMic = params.get("TurnOffMic")
        self._AudioQuality = params.get("AudioQuality")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._RTCAudienceNumber = params.get("RTCAudienceNumber")
        self._AudienceType = params.get("AudienceType")
        self._RecordLayout = params.get("RecordLayout")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        self._InteractionMode = params.get("InteractionMode")
        self._VideoOrientation = params.get("VideoOrientation")
        self._IsGradingRequiredPostClass = params.get("IsGradingRequiredPostClass")
        self._RoomType = params.get("RoomType")
        self._Guests = params.get("Guests")
        self._EndDelayTime = params.get("EndDelayTime")
        self._LiveType = params.get("LiveType")
        self._RecordLiveUrl = params.get("RecordLiveUrl")
        self._EnableAutoStart = params.get("EnableAutoStart")
        self._RecordBackground = params.get("RecordBackground")
        self._RecordScene = params.get("RecordScene")
        self._RecordLang = params.get("RecordLang")
        self._RecordStream = params.get("RecordStream")
        self._WhiteBoardSnapshotMode = params.get("WhiteBoardSnapshotMode")
        self._SubtitlesTranscription = params.get("SubtitlesTranscription")
        self._RecordMerge = params.get("RecordMerge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoomResponse(AbstractModel):
    r"""CreateRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoomId = None
        self._RequestId = None

    @property
    def RoomId(self):
        r"""房间ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._RequestId = params.get("RequestId")


class CreateSupervisorRequest(AbstractModel):
    r"""CreateSupervisor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID。
        :type SdkAppId: int
        :param _Users: 用户ID列表。
        :type Users: list of str
        """
        self._SdkAppId = None
        self._Users = None

    @property
    def SdkAppId(self):
        r"""应用ID。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Users(self):
        r"""用户ID列表。
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Users = params.get("Users")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSupervisorResponse(AbstractModel):
    r"""CreateSupervisor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CustomMsgContent(AbstractModel):
    r"""自定义消息

    """

    def __init__(self):
        r"""
        :param _Data: 自定义消息数据。
        :type Data: str
        :param _Desc: 自定义消息描述信息。
        :type Desc: str
        :param _Ext: 扩展字段。
        :type Ext: str
        """
        self._Data = None
        self._Desc = None
        self._Ext = None

    @property
    def Data(self):
        r"""自定义消息数据。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Desc(self):
        r"""自定义消息描述信息。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Ext(self):
        r"""扩展字段。
        :rtype: str
        """
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._Desc = params.get("Desc")
        self._Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomRecordInfo(AbstractModel):
    r"""自定义录制信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _StopTime: 结束时间
        :type StopTime: int
        :param _Duration: 总时长
        :type Duration: int
        :param _FileFormat: 文件格式
        :type FileFormat: str
        :param _RecordUrl: 流url
        :type RecordUrl: str
        :param _RecordSize: 流大小
        :type RecordSize: int
        :param _VideoId: 流ID
        :type VideoId: str
        :param _TaskId: 任务Id
        :type TaskId: str
        """
        self._StartTime = None
        self._StopTime = None
        self._Duration = None
        self._FileFormat = None
        self._RecordUrl = None
        self._RecordSize = None
        self._VideoId = None
        self._TaskId = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StopTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def Duration(self):
        r"""总时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FileFormat(self):
        r"""文件格式
        :rtype: str
        """
        return self._FileFormat

    @FileFormat.setter
    def FileFormat(self, FileFormat):
        self._FileFormat = FileFormat

    @property
    def RecordUrl(self):
        r"""流url
        :rtype: str
        """
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def RecordSize(self):
        r"""流大小
        :rtype: int
        """
        return self._RecordSize

    @RecordSize.setter
    def RecordSize(self, RecordSize):
        self._RecordSize = RecordSize

    @property
    def VideoId(self):
        r"""流ID
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def TaskId(self):
        r"""任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._StopTime = params.get("StopTime")
        self._Duration = params.get("Duration")
        self._FileFormat = params.get("FileFormat")
        self._RecordUrl = params.get("RecordUrl")
        self._RecordSize = params.get("RecordSize")
        self._VideoId = params.get("VideoId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppCustomContentRequest(AbstractModel):
    r"""DeleteAppCustomContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID。
        :type SdkAppId: int
        :param _Scenes: 指定需要删除的已设置的scene场景自定义元素，如果为空则删除应用下已设置的所有自定义元素。
        :type Scenes: list of str
        """
        self._SdkAppId = None
        self._Scenes = None

    @property
    def SdkAppId(self):
        r"""应用ID。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Scenes(self):
        r"""指定需要删除的已设置的scene场景自定义元素，如果为空则删除应用下已设置的所有自定义元素。
        :rtype: list of str
        """
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Scenes = params.get("Scenes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppCustomContentResponse(AbstractModel):
    r"""DeleteAppCustomContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDocumentRequest(AbstractModel):
    r"""DeleteDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档ID。
        :type DocumentId: str
        """
        self._DocumentId = None

    @property
    def DocumentId(self):
        r"""文档ID。
        :rtype: str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocumentResponse(AbstractModel):
    r"""DeleteDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteGroupMemberRequest(AbstractModel):
    r"""DeleteGroupMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID，联合群组无法删除群组成员
        :type GroupId: str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _MemberIds: 成员列表，最大值200
        :type MemberIds: list of str
        """
        self._GroupId = None
        self._SdkAppId = None
        self._MemberIds = None

    @property
    def GroupId(self):
        r"""群组ID，联合群组无法删除群组成员
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
        r"""成员列表，最大值200
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._MemberIds = params.get("MemberIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupMemberResponse(AbstractModel):
    r"""DeleteGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    r"""DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 待删除群组ID列表
        :type GroupIds: list of str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        """
        self._GroupIds = None
        self._SdkAppId = None

    @property
    def GroupIds(self):
        r"""待删除群组ID列表
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    r"""DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRecordRequest(AbstractModel):
    r"""DeleteRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间Id。
        :type RoomId: int
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        """
        self._RoomId = None
        self._SdkAppId = None

    @property
    def RoomId(self):
        r"""房间Id。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。

        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordResponse(AbstractModel):
    r"""DeleteRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRoomRequest(AbstractModel):
    r"""DeleteRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂ID。
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        r"""课堂ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoomResponse(AbstractModel):
    r"""DeleteRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSupervisorRequest(AbstractModel):
    r"""DeleteSupervisor请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID
        :type SdkAppId: int
        :param _Users: 用户ID列表
        :type Users: list of str
        """
        self._SdkAppId = None
        self._Users = None

    @property
    def SdkAppId(self):
        r"""应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Users(self):
        r"""用户ID列表
        :rtype: list of str
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Users = params.get("Users")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSupervisorResponse(AbstractModel):
    r"""DeleteSupervisor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    r"""DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 待删除用户的ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""待删除用户的ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    r"""DeleteUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteWhiteBoardSnapshotRequest(AbstractModel):
    r"""DeleteWhiteBoardSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂ID
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhiteBoardSnapshotResponse(AbstractModel):
    r"""DeleteWhiteBoardSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAnswerListRequest(AbstractModel):
    r"""DescribeAnswerList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QuestionId: 问题ID
        :type QuestionId: str
        :param _Page: 1
        :type Page: int
        :param _Limit: 100
        :type Limit: int
        """
        self._QuestionId = None
        self._Page = None
        self._Limit = None

    @property
    def QuestionId(self):
        r"""问题ID
        :rtype: str
        """
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def Page(self):
        r"""1
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._QuestionId = params.get("QuestionId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAnswerListResponse(AbstractModel):
    r"""DescribeAnswerList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合查询条件的房间答案总数
        :type Total: int
        :param _AnswerInfo: 房间提问答案列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AnswerInfo: list of AnswerInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AnswerInfo = None
        self._RequestId = None

    @property
    def Total(self):
        r"""符合查询条件的房间答案总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AnswerInfo(self):
        r"""房间提问答案列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AnswerInfo
        """
        return self._AnswerInfo

    @AnswerInfo.setter
    def AnswerInfo(self, AnswerInfo):
        self._AnswerInfo = AnswerInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("AnswerInfo") is not None:
            self._AnswerInfo = []
            for item in params.get("AnswerInfo"):
                obj = AnswerInfo()
                obj._deserialize(item)
                self._AnswerInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAppDetailRequest(AbstractModel):
    r"""DescribeAppDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID。低代码互动课堂的SdkAppId。

        :type ApplicationId: str
        :param _DeveloperId: 开发商ID
        :type DeveloperId: str
        """
        self._ApplicationId = None
        self._DeveloperId = None

    @property
    def ApplicationId(self):
        r"""应用ID。低代码互动课堂的SdkAppId。

        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def DeveloperId(self):
        r"""开发商ID
        :rtype: str
        """
        return self._DeveloperId

    @DeveloperId.setter
    def DeveloperId(self, DeveloperId):
        self._DeveloperId = DeveloperId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._DeveloperId = params.get("DeveloperId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppDetailResponse(AbstractModel):
    r"""DescribeAppDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SDK 对应的AppId 
        :type SdkAppId: str
        :param _AppConfig: 应用配置
        :type AppConfig: :class:`tencentcloud.lcic.v20220817.models.AppConfig`
        :param _SceneConfig: 场景配置
        :type SceneConfig: list of SceneItem
        :param _TransferConfig: 转存配置
        :type TransferConfig: :class:`tencentcloud.lcic.v20220817.models.TransferItem`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SdkAppId = None
        self._AppConfig = None
        self._SceneConfig = None
        self._TransferConfig = None
        self._RequestId = None

    @property
    def SdkAppId(self):
        r"""SDK 对应的AppId 
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppConfig(self):
        r"""应用配置
        :rtype: :class:`tencentcloud.lcic.v20220817.models.AppConfig`
        """
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig

    @property
    def SceneConfig(self):
        r"""场景配置
        :rtype: list of SceneItem
        """
        return self._SceneConfig

    @SceneConfig.setter
    def SceneConfig(self, SceneConfig):
        self._SceneConfig = SceneConfig

    @property
    def TransferConfig(self):
        r"""转存配置
        :rtype: :class:`tencentcloud.lcic.v20220817.models.TransferItem`
        """
        return self._TransferConfig

    @TransferConfig.setter
    def TransferConfig(self, TransferConfig):
        self._TransferConfig = TransferConfig

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AppConfig") is not None:
            self._AppConfig = AppConfig()
            self._AppConfig._deserialize(params.get("AppConfig"))
        if params.get("SceneConfig") is not None:
            self._SceneConfig = []
            for item in params.get("SceneConfig"):
                obj = SceneItem()
                obj._deserialize(item)
                self._SceneConfig.append(obj)
        if params.get("TransferConfig") is not None:
            self._TransferConfig = TransferItem()
            self._TransferConfig._deserialize(params.get("TransferConfig"))
        self._RequestId = params.get("RequestId")


class DescribeCurrentMemberListRequest(AbstractModel):
    r"""DescribeCurrentMemberList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂Id。
        :type RoomId: int
        :param _Page: 分页查询当前页数，从1开始递增。
        :type Page: int
        :param _Limit: 每页数据量，最大1000。
        :type Limit: int
        """
        self._RoomId = None
        self._Page = None
        self._Limit = None

    @property
    def RoomId(self):
        r"""课堂Id。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页数据量，最大1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCurrentMemberListResponse(AbstractModel):
    r"""DescribeCurrentMemberList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 记录总数。当前房间的总人数。
        :type Total: int
        :param _MemberRecords: 成员记录列表。
        :type MemberRecords: list of MemberRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._MemberRecords = None
        self._RequestId = None

    @property
    def Total(self):
        r"""记录总数。当前房间的总人数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberRecords(self):
        r"""成员记录列表。
        :rtype: list of MemberRecord
        """
        return self._MemberRecords

    @MemberRecords.setter
    def MemberRecords(self, MemberRecords):
        self._MemberRecords = MemberRecords

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self._MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self._MemberRecords.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeveloperRequest(AbstractModel):
    r"""DescribeDeveloper请求参数结构体

    """


class DescribeDeveloperResponse(AbstractModel):
    r"""DescribeDeveloper返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeveloperId: 开发商ID
        :type DeveloperId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeveloperId = None
        self._RequestId = None

    @property
    def DeveloperId(self):
        r"""开发商ID
        :rtype: str
        """
        return self._DeveloperId

    @DeveloperId.setter
    def DeveloperId(self, DeveloperId):
        self._DeveloperId = DeveloperId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeveloperId = params.get("DeveloperId")
        self._RequestId = params.get("RequestId")


class DescribeDocumentRequest(AbstractModel):
    r"""DescribeDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档Id（唯一id）
        :type DocumentId: str
        """
        self._DocumentId = None

    @property
    def DocumentId(self):
        r"""文档Id（唯一id）
        :rtype: str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentResponse(AbstractModel):
    r"""DescribeDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档Id
        :type DocumentId: str
        :param _DocumentUrl: 文档原址url
        :type DocumentUrl: str
        :param _DocumentName: 文档名称
        :type DocumentName: str
        :param _Owner: 文档所有者UserId
        :type Owner: str
        :param _SdkAppId: 应用Id
        :type SdkAppId: int
        :param _Permission: 文档权限
        :type Permission: int
        :param _TranscodeResult: 转码结果，无需转码为空，转码成功为结果url，转码失败为错误码
        :type TranscodeResult: str
        :param _TranscodeType: 转码类型
        :type TranscodeType: int
        :param _TranscodeProgress: 转码进度， 0 - 100 表示（0% - 100%）
        :type TranscodeProgress: int
        :param _TranscodeState: 转码状态，0为无需转码，1为正在转码，2为转码失败，3为转码成功
        :type TranscodeState: int
        :param _TranscodeInfo: 转码失败后的错误信息
        :type TranscodeInfo: str
        :param _DocumentType: 文档类型
        :type DocumentType: str
        :param _DocumentSize: 文档大小，单位：字节
        :type DocumentSize: int
        :param _UpdateTime: 更新的UNIX时间戳
        :type UpdateTime: int
        :param _Pages: 课件页数
        :type Pages: int
        :param _Preview: 课件预览地址
        :type Preview: str
        :param _Resolution: 文档的分辨率
        :type Resolution: str
        :param _MinScaleResolution: 转码后文档的最小分辨率，和创建文档时传入的参数一致。
        :type MinScaleResolution: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocumentId = None
        self._DocumentUrl = None
        self._DocumentName = None
        self._Owner = None
        self._SdkAppId = None
        self._Permission = None
        self._TranscodeResult = None
        self._TranscodeType = None
        self._TranscodeProgress = None
        self._TranscodeState = None
        self._TranscodeInfo = None
        self._DocumentType = None
        self._DocumentSize = None
        self._UpdateTime = None
        self._Pages = None
        self._Preview = None
        self._Resolution = None
        self._MinScaleResolution = None
        self._RequestId = None

    @property
    def DocumentId(self):
        r"""文档Id
        :rtype: str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def DocumentUrl(self):
        r"""文档原址url
        :rtype: str
        """
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        r"""文档名称
        :rtype: str
        """
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        r"""文档所有者UserId
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SdkAppId(self):
        r"""应用Id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Permission(self):
        r"""文档权限
        :rtype: int
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def TranscodeResult(self):
        r"""转码结果，无需转码为空，转码成功为结果url，转码失败为错误码
        :rtype: str
        """
        return self._TranscodeResult

    @TranscodeResult.setter
    def TranscodeResult(self, TranscodeResult):
        self._TranscodeResult = TranscodeResult

    @property
    def TranscodeType(self):
        r"""转码类型
        :rtype: int
        """
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def TranscodeProgress(self):
        r"""转码进度， 0 - 100 表示（0% - 100%）
        :rtype: int
        """
        return self._TranscodeProgress

    @TranscodeProgress.setter
    def TranscodeProgress(self, TranscodeProgress):
        self._TranscodeProgress = TranscodeProgress

    @property
    def TranscodeState(self):
        r"""转码状态，0为无需转码，1为正在转码，2为转码失败，3为转码成功
        :rtype: int
        """
        return self._TranscodeState

    @TranscodeState.setter
    def TranscodeState(self, TranscodeState):
        self._TranscodeState = TranscodeState

    @property
    def TranscodeInfo(self):
        r"""转码失败后的错误信息
        :rtype: str
        """
        return self._TranscodeInfo

    @TranscodeInfo.setter
    def TranscodeInfo(self, TranscodeInfo):
        self._TranscodeInfo = TranscodeInfo

    @property
    def DocumentType(self):
        r"""文档类型
        :rtype: str
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        r"""文档大小，单位：字节
        :rtype: int
        """
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def UpdateTime(self):
        r"""更新的UNIX时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Pages(self):
        r"""课件页数
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Preview(self):
        r"""课件预览地址
        :rtype: str
        """
        return self._Preview

    @Preview.setter
    def Preview(self, Preview):
        self._Preview = Preview

    @property
    def Resolution(self):
        r"""文档的分辨率
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MinScaleResolution(self):
        r"""转码后文档的最小分辨率，和创建文档时传入的参数一致。
        :rtype: str
        """
        return self._MinScaleResolution

    @MinScaleResolution.setter
    def MinScaleResolution(self, MinScaleResolution):
        self._MinScaleResolution = MinScaleResolution

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._DocumentUrl = params.get("DocumentUrl")
        self._DocumentName = params.get("DocumentName")
        self._Owner = params.get("Owner")
        self._SdkAppId = params.get("SdkAppId")
        self._Permission = params.get("Permission")
        self._TranscodeResult = params.get("TranscodeResult")
        self._TranscodeType = params.get("TranscodeType")
        self._TranscodeProgress = params.get("TranscodeProgress")
        self._TranscodeState = params.get("TranscodeState")
        self._TranscodeInfo = params.get("TranscodeInfo")
        self._DocumentType = params.get("DocumentType")
        self._DocumentSize = params.get("DocumentSize")
        self._UpdateTime = params.get("UpdateTime")
        self._Pages = params.get("Pages")
        self._Preview = params.get("Preview")
        self._Resolution = params.get("Resolution")
        self._MinScaleResolution = params.get("MinScaleResolution")
        self._RequestId = params.get("RequestId")


class DescribeDocumentsByRoomRequest(AbstractModel):
    r"""DescribeDocumentsByRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        :param _SdkAppId: 低代码互动课堂的SdkAppId
        :type SdkAppId: int
        :param _Page: 分页查询当前页数，从1开始递增，默认值为1
        :type Page: int
        :param _Limit: 每页数据量，最大1000，默认值为100
        :type Limit: int
        :param _Permission: 课件权限。
[0]：获取owner的私有课件；
[1]：获取owner的公开课件;
[0,1]：则获取owner的私有课件和公开课件；
[2]：获取owner的私有课件和所有人(包括owner)的公开课件。
默认值为[2]
        :type Permission: list of int non-negative
        :param _Owner: 文档所有者的user_id，不填默认获取SdkAppId下所有课件
        :type Owner: str
        """
        self._RoomId = None
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._Permission = None
        self._Owner = None

    @property
    def RoomId(self):
        r"""房间ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增，默认值为1
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页数据量，最大1000，默认值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        r"""课件权限。
[0]：获取owner的私有课件；
[1]：获取owner的公开课件;
[0,1]：则获取owner的私有课件和公开课件；
[2]：获取owner的私有课件和所有人(包括owner)的公开课件。
默认值为[2]
        :rtype: list of int non-negative
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        r"""文档所有者的user_id，不填默认获取SdkAppId下所有课件
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Permission = params.get("Permission")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentsByRoomResponse(AbstractModel):
    r"""DescribeDocumentsByRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Documents: 文档信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Documents: list of DocumentInfo
        :param _Total: 符合查询条件文档总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Documents = None
        self._Total = None
        self._RequestId = None

    @property
    def Documents(self):
        r"""文档信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DocumentInfo
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def Total(self):
        r"""符合查询条件文档总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDocumentsRequest(AbstractModel):
    r"""DescribeDocuments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SchoolId: 学校id
        :type SchoolId: int
        :param _Page: 分页查询当前页数，从1开始递增
        :type Page: int
        :param _Limit: 每页数据量，最大1000
        :type Limit: int
        :param _Permission: 课件权限。[0]：获取owner的私有课件；[1]：获取owner的公开课件; [0,1]：则获取owner的私有课件和公开课件；[2]：获取owner的私有课件和所有人(包括owner)的公开课件
        :type Permission: list of int non-negative
        :param _Owner: 课件所有者的user_id，不填默认获取school_id下所有课件
        :type Owner: str
        :param _Keyword: 课件名称搜索词
        :type Keyword: str
        :param _DocumentId: 课件id列表，从列表中查询，忽略错误的id
        :type DocumentId: list of str
        """
        self._SchoolId = None
        self._Page = None
        self._Limit = None
        self._Permission = None
        self._Owner = None
        self._Keyword = None
        self._DocumentId = None

    @property
    def SchoolId(self):
        r"""学校id
        :rtype: int
        """
        return self._SchoolId

    @SchoolId.setter
    def SchoolId(self, SchoolId):
        self._SchoolId = SchoolId

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页数据量，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        r"""课件权限。[0]：获取owner的私有课件；[1]：获取owner的公开课件; [0,1]：则获取owner的私有课件和公开课件；[2]：获取owner的私有课件和所有人(包括owner)的公开课件
        :rtype: list of int non-negative
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        r"""课件所有者的user_id，不填默认获取school_id下所有课件
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Keyword(self):
        r"""课件名称搜索词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DocumentId(self):
        r"""课件id列表，从列表中查询，忽略错误的id
        :rtype: list of str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._SchoolId = params.get("SchoolId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Permission = params.get("Permission")
        self._Owner = params.get("Owner")
        self._Keyword = params.get("Keyword")
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocumentsResponse(AbstractModel):
    r"""DescribeDocuments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合查询条件文档总数
        :type Total: int
        :param _Documents: 文档信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Documents: list of DocumentInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Documents = None
        self._RequestId = None

    @property
    def Total(self):
        r"""符合查询条件文档总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Documents(self):
        r"""文档信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DocumentInfo
        """
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupListRequest(AbstractModel):
    r"""DescribeGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _Page: 分页查询当前页数，默认从1开始递增。
        :type Page: int
        :param _Limit: 每页数据量，默认20，最大1000。
        :type Limit: int
        :param _TeacherId: 主讲人ID筛选群组，与MemberId有且只有一个,都传时以此字段获取
        :type TeacherId: str
        :param _MemberId: 成员ID刷选群组，与TeacherId有且只有一个
        :type MemberId: str
        """
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._TeacherId = None
        self._MemberId = None

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        r"""分页查询当前页数，默认从1开始递增。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页数据量，默认20，最大1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TeacherId(self):
        r"""主讲人ID筛选群组，与MemberId有且只有一个,都传时以此字段获取
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def MemberId(self):
        r"""成员ID刷选群组，与TeacherId有且只有一个
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._TeacherId = params.get("TeacherId")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupListResponse(AbstractModel):
    r"""DescribeGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 记录总数。当前匹配群组总数。
        :type Total: int
        :param _GroupInfos: 群组信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupInfos: list of GroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._GroupInfos = None
        self._RequestId = None

    @property
    def Total(self):
        r"""记录总数。当前匹配群组总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def GroupInfos(self):
        r"""群组信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of GroupInfo
        """
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGroupMemberListRequest(AbstractModel):
    r"""DescribeGroupMemberList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _Page: 分页值，默认1
        :type Page: int
        :param _Limit: 每页数据量，默认20，最大1000
        :type Limit: int
        """
        self._GroupId = None
        self._SdkAppId = None
        self._Page = None
        self._Limit = None

    @property
    def GroupId(self):
        r"""群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        r"""分页值，默认1
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页数据量，默认20，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupMemberListResponse(AbstractModel):
    r"""DescribeGroupMemberList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合查询条件总条数
        :type Total: int
        :param _MemberIds: 查询成员列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._MemberIds = None
        self._RequestId = None

    @property
    def Total(self):
        r"""符合查询条件总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberIds(self):
        r"""查询成员列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._MemberIds = params.get("MemberIds")
        self._RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    r"""DescribeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        """
        self._GroupId = None
        self._SdkAppId = None

    @property
    def GroupId(self):
        r"""群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    r"""DescribeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: str
        :param _GroupName: 群组名称
        :type GroupName: str
        :param _TeacherId: 群主主讲人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TeacherId: str
        :param _GroupType: 群组类型
0-基础群组
1-组合群组，若为1时会返回子群组ID
        :type GroupType: int
        :param _SubGroupIds: 子群组ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubGroupIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._GroupName = None
        self._TeacherId = None
        self._GroupType = None
        self._SubGroupIds = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""群组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        r"""群主主讲人ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupType(self):
        r"""群组类型
0-基础群组
1-组合群组，若为1时会返回子群组ID
        :rtype: int
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def SubGroupIds(self):
        r"""子群组ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._TeacherId = params.get("TeacherId")
        self._GroupType = params.get("GroupType")
        self._SubGroupIds = params.get("SubGroupIds")
        self._RequestId = params.get("RequestId")


class DescribeMarqueeRequest(AbstractModel):
    r"""DescribeMarquee请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 学校ID
        :type SdkAppId: int
        :param _RoomId: 房间号
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间号
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMarqueeResponse(AbstractModel):
    r"""DescribeMarquee返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MarqueeType:  跑马灯类型：1为固定值，2为用户昵称，3为固定值+用户昵称，4为用户ID，5为originId+固定值，6为用户昵称（originId）
        :type MarqueeType: int
        :param _Content: 固定值内容（当MarqueeType=1或5，则展示固定值内容）
        :type Content: str
        :param _FontSize: 字体大小（数字，像素单位，范围：10到24）
        :type FontSize: int
        :param _FontWeight: 字体粗细：1为粗体，0为细体
        :type FontWeight: int
        :param _FontColor: 字体颜色（十六进制颜色值）
        :type FontColor: str
        :param _FontOpacity: 字体透明度（数字，范围 0.0 到 1.0）
        :type FontOpacity: float
        :param _BackgroundColor: 背景颜色（十六进制颜色值）
        :type BackgroundColor: str
        :param _BackgroundOpacity: 背景透明度（数字，范围 0.0 到 1.0）
        :type BackgroundOpacity: float
        :param _DisplayMode: 显示方式：1为滚动，2为闪烁
        :type DisplayMode: int
        :param _Duration: 停留时长（秒，整数，范围 1～10）
        :type Duration: int
        :param _MarqueeCount: 跑马灯个数：目前仅支持1或2, 对应显示单排或双排
        :type MarqueeCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MarqueeType = None
        self._Content = None
        self._FontSize = None
        self._FontWeight = None
        self._FontColor = None
        self._FontOpacity = None
        self._BackgroundColor = None
        self._BackgroundOpacity = None
        self._DisplayMode = None
        self._Duration = None
        self._MarqueeCount = None
        self._RequestId = None

    @property
    def MarqueeType(self):
        r""" 跑马灯类型：1为固定值，2为用户昵称，3为固定值+用户昵称，4为用户ID，5为originId+固定值，6为用户昵称（originId）
        :rtype: int
        """
        return self._MarqueeType

    @MarqueeType.setter
    def MarqueeType(self, MarqueeType):
        self._MarqueeType = MarqueeType

    @property
    def Content(self):
        r"""固定值内容（当MarqueeType=1或5，则展示固定值内容）
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FontSize(self):
        r"""字体大小（数字，像素单位，范围：10到24）
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontWeight(self):
        r"""字体粗细：1为粗体，0为细体
        :rtype: int
        """
        return self._FontWeight

    @FontWeight.setter
    def FontWeight(self, FontWeight):
        self._FontWeight = FontWeight

    @property
    def FontColor(self):
        r"""字体颜色（十六进制颜色值）
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def FontOpacity(self):
        r"""字体透明度（数字，范围 0.0 到 1.0）
        :rtype: float
        """
        return self._FontOpacity

    @FontOpacity.setter
    def FontOpacity(self, FontOpacity):
        self._FontOpacity = FontOpacity

    @property
    def BackgroundColor(self):
        r"""背景颜色（十六进制颜色值）
        :rtype: str
        """
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor

    @property
    def BackgroundOpacity(self):
        r"""背景透明度（数字，范围 0.0 到 1.0）
        :rtype: float
        """
        return self._BackgroundOpacity

    @BackgroundOpacity.setter
    def BackgroundOpacity(self, BackgroundOpacity):
        self._BackgroundOpacity = BackgroundOpacity

    @property
    def DisplayMode(self):
        r"""显示方式：1为滚动，2为闪烁
        :rtype: int
        """
        return self._DisplayMode

    @DisplayMode.setter
    def DisplayMode(self, DisplayMode):
        self._DisplayMode = DisplayMode

    @property
    def Duration(self):
        r"""停留时长（秒，整数，范围 1～10）
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def MarqueeCount(self):
        r"""跑马灯个数：目前仅支持1或2, 对应显示单排或双排
        :rtype: int
        """
        return self._MarqueeCount

    @MarqueeCount.setter
    def MarqueeCount(self, MarqueeCount):
        self._MarqueeCount = MarqueeCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MarqueeType = params.get("MarqueeType")
        self._Content = params.get("Content")
        self._FontSize = params.get("FontSize")
        self._FontWeight = params.get("FontWeight")
        self._FontColor = params.get("FontColor")
        self._FontOpacity = params.get("FontOpacity")
        self._BackgroundColor = params.get("BackgroundColor")
        self._BackgroundOpacity = params.get("BackgroundOpacity")
        self._DisplayMode = params.get("DisplayMode")
        self._Duration = params.get("Duration")
        self._MarqueeCount = params.get("MarqueeCount")
        self._RequestId = params.get("RequestId")


class DescribeQuestionListRequest(AbstractModel):
    r"""DescribeQuestionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID
        :type RoomId: int
        :param _Page: 分页查询当前页数，从1开始递增，默认值为1
        :type Page: int
        :param _Limit: 分页查询当前页数，从1开始递增，默认值为1
        :type Limit: int
        """
        self._RoomId = None
        self._Page = None
        self._Limit = None

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增，默认值为1
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""分页查询当前页数，从1开始递增，默认值为1
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuestionListResponse(AbstractModel):
    r"""DescribeQuestionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 符合查询条件的房间问答问题总数
        :type Total: int
        :param _QuestionInfo: 房间问答问题列表
注意：此字段可能返回 null，表示取不到有效值。
        :type QuestionInfo: list of QuestionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._QuestionInfo = None
        self._RequestId = None

    @property
    def Total(self):
        r"""符合查询条件的房间问答问题总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def QuestionInfo(self):
        r"""房间问答问题列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QuestionInfo
        """
        return self._QuestionInfo

    @QuestionInfo.setter
    def QuestionInfo(self, QuestionInfo):
        self._QuestionInfo = QuestionInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("QuestionInfo") is not None:
            self._QuestionInfo = []
            for item in params.get("QuestionInfo"):
                obj = QuestionInfo()
                obj._deserialize(item)
                self._QuestionInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordRequest(AbstractModel):
    r"""DescribeRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 学校ID
        :type SdkAppId: int
        :param _RoomId: 房间ID
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordResponse(AbstractModel):
    r"""DescribeRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SchoolId: 学校ID
        :type SchoolId: int
        :param _ClassId: 课堂ID
        :type ClassId: int
        :param _RecordInfo: 录制信息
        :type RecordInfo: list of CustomRecordInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SchoolId = None
        self._ClassId = None
        self._RecordInfo = None
        self._RequestId = None

    @property
    def SchoolId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SchoolId

    @SchoolId.setter
    def SchoolId(self, SchoolId):
        self._SchoolId = SchoolId

    @property
    def ClassId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def RecordInfo(self):
        r"""录制信息
        :rtype: list of CustomRecordInfo
        """
        return self._RecordInfo

    @RecordInfo.setter
    def RecordInfo(self, RecordInfo):
        self._RecordInfo = RecordInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SchoolId = params.get("SchoolId")
        self._ClassId = params.get("ClassId")
        if params.get("RecordInfo") is not None:
            self._RecordInfo = []
            for item in params.get("RecordInfo"):
                obj = CustomRecordInfo()
                obj._deserialize(item)
                self._RecordInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordStreamRequest(AbstractModel):
    r"""DescribeRecordStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 学校ID
        :type SdkAppId: int
        :param _RoomId: 房间ID
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStreamResponse(AbstractModel):
    r"""DescribeRecordStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SchoolId: 学校ID
        :type SchoolId: int
        :param _ClassId: 课堂ID
        :type ClassId: int
        :param _ClassType: 课堂类型
        :type ClassType: int
        :param _StreamInfo: 用户流信息
        :type StreamInfo: list of SingleStreamInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SchoolId = None
        self._ClassId = None
        self._ClassType = None
        self._StreamInfo = None
        self._RequestId = None

    @property
    def SchoolId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SchoolId

    @SchoolId.setter
    def SchoolId(self, SchoolId):
        self._SchoolId = SchoolId

    @property
    def ClassId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def ClassType(self):
        r"""课堂类型
        :rtype: int
        """
        return self._ClassType

    @ClassType.setter
    def ClassType(self, ClassType):
        self._ClassType = ClassType

    @property
    def StreamInfo(self):
        r"""用户流信息
        :rtype: list of SingleStreamInfo
        """
        return self._StreamInfo

    @StreamInfo.setter
    def StreamInfo(self, StreamInfo):
        self._StreamInfo = StreamInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SchoolId = params.get("SchoolId")
        self._ClassId = params.get("ClassId")
        self._ClassType = params.get("ClassType")
        if params.get("StreamInfo") is not None:
            self._StreamInfo = []
            for item in params.get("StreamInfo"):
                obj = SingleStreamInfo()
                obj._deserialize(item)
                self._StreamInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordTaskRequest(AbstractModel):
    r"""DescribeRecordTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 学校ID
        :type SdkAppId: int
        :param _RoomId: 房间ID
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordTaskResponse(AbstractModel):
    r"""DescribeRecordTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeRoomForbiddenUserRequest(AbstractModel):
    r"""DescribeRoomForbiddenUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 房间ID。
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomForbiddenUserResponse(AbstractModel):
    r"""DescribeRoomForbiddenUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MutedAccountList: 禁言用户信息数组，内容包括被禁言的成员 ID，及其被禁言到的时间（使用 UTC 时间，即世界协调时间）
        :type MutedAccountList: list of MutedAccountList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MutedAccountList = None
        self._RequestId = None

    @property
    def MutedAccountList(self):
        r"""禁言用户信息数组，内容包括被禁言的成员 ID，及其被禁言到的时间（使用 UTC 时间，即世界协调时间）
        :rtype: list of MutedAccountList
        """
        return self._MutedAccountList

    @MutedAccountList.setter
    def MutedAccountList(self, MutedAccountList):
        self._MutedAccountList = MutedAccountList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MutedAccountList") is not None:
            self._MutedAccountList = []
            for item in params.get("MutedAccountList"):
                obj = MutedAccountList()
                obj._deserialize(item)
                self._MutedAccountList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoomRequest(AbstractModel):
    r"""DescribeRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂Id。
        :type RoomId: int
        :param _RTMPStreamingURL: 请求RTMP推流链接，0：否，1：是，默认为0。
        :type RTMPStreamingURL: int
        """
        self._RoomId = None
        self._RTMPStreamingURL = None

    @property
    def RoomId(self):
        r"""课堂Id。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RTMPStreamingURL(self):
        r"""请求RTMP推流链接，0：否，1：是，默认为0。
        :rtype: int
        """
        return self._RTMPStreamingURL

    @RTMPStreamingURL.setter
    def RTMPStreamingURL(self, RTMPStreamingURL):
        self._RTMPStreamingURL = RTMPStreamingURL


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._RTMPStreamingURL = params.get("RTMPStreamingURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomResponse(AbstractModel):
    r"""DescribeRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 课堂名称。
        :type Name: str
        :param _StartTime: 预定的课堂开始时间，unix时间戳（秒）。
        :type StartTime: int
        :param _EndTime: 预定的课堂结束时间，unix时间戳（秒）。
        :type EndTime: int
        :param _TeacherId: 老师的UserId。
        :type TeacherId: str
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _AudienceType: 观看类型。互动观看 （默认）	
        :type AudienceType: int
        :param _Resolution: 头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :type Resolution: int
        :param _MaxMicNumber: 设置课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :type MaxMicNumber: int
        :param _AutoMic: 进入课堂时是否自动连麦。可以有以下取值：
0 不自动连麦（需要手动申请上麦，默认值）
1 自动连麦
        :type AutoMic: int
        :param _AudioQuality: 高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
        :type AudioQuality: int
        :param _SubType: 课堂子类型，可以有以下取值：videodoc 文档+视频video 纯视频
        :type SubType: str
        :param _DisableRecord: 上课后是否禁止自动录制。可以有以下取值：
0 不禁止录制（自动开启录制，默认值）
1 禁止录制
注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :type DisableRecord: int
        :param _Assistants: 助教UserId列表。
        :type Assistants: list of str
        :param _RecordUrl: 录制地址（协议为https)。仅在房间结束后存在。
        :type RecordUrl: str
        :param _Status: 课堂状态。0为未开始，1为已开始，2为已结束，3为已过期。
        :type Status: int
        :param _GroupId: 课堂绑定的群组ID
        :type GroupId: str
        :param _EnableDirectControl: 打开学生麦克风/摄像头的授权开关
        :type EnableDirectControl: int
        :param _InteractionMode: 开启专注模式。
0 收看全部角色音视频(默认)
1 只看老师和助教
        :type InteractionMode: int
        :param _VideoOrientation: 横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :type VideoOrientation: int
        :param _IsGradingRequiredPostClass: 该课堂是否开启了课后评分功能。0：未开启  1：开启
        :type IsGradingRequiredPostClass: int
        :param _RoomType: 课堂类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (预留参数，暂未开放); 3 圆桌会议 注：大班课的布局(layout)只有三分屏
        :type RoomType: int
        :param _VideoDuration: 录制时长
        :type VideoDuration: int
        :param _EndDelayTime: 拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :type EndDelayTime: int
        :param _LiveType: 直播类型：0 常规（默认）1 伪直播 2 RTMP推流直播
        :type LiveType: int
        :param _RecordLiveUrl: 伪直播链接
        :type RecordLiveUrl: str
        :param _EnableAutoStart: 是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1的时候有效
        :type EnableAutoStart: int
        :param _RecordBackground: 录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :type RecordBackground: str
        :param _RTMPStreamingURL: RTMP推流链接
        :type RTMPStreamingURL: str
        :param _RecordScene: 录制自定义场景。注意：仅recordlayout=9的时候此参数有效。需注意各类参数配置正确能够生效。不然会造成录制失败，失败后无法补救。数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。自定义场景参数的含义。如下：     scene：自定义js/css对应的场景值。如scene=recordScene，会加载 recordScene 场景对应的 js/css，这样就可以自定义录制页面的元素。     lng：录制页面对应的语种。如lng=en，则录制界面为en。（枚举值：en,zh，zh-TW，jp，ar，kr，vi）     customToken：录制页面中涉及客户自己的服务需要鉴权时进行配置。一般情况下，无需配置。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _RecordStream: 录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :type RecordStream: int
        :param _RecordLayout: 录制模板。房间子类型为视频+白板（SubType=videodoc）时默认为3，房间子类型为纯视频（SubType=video）时默认为0。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :type RecordLayout: int
        :param _WhiteBoardSnapshotMode: 板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :type WhiteBoardSnapshotMode: int
        :param _SubtitlesTranscription: 字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :type SubtitlesTranscription: int
        :param _Guests: 嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :type Guests: list of str
        :param _RecordMerge: 录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :type RecordMerge: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._TeacherId = None
        self._SdkAppId = None
        self._AudienceType = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._AutoMic = None
        self._AudioQuality = None
        self._SubType = None
        self._DisableRecord = None
        self._Assistants = None
        self._RecordUrl = None
        self._Status = None
        self._GroupId = None
        self._EnableDirectControl = None
        self._InteractionMode = None
        self._VideoOrientation = None
        self._IsGradingRequiredPostClass = None
        self._RoomType = None
        self._VideoDuration = None
        self._EndDelayTime = None
        self._LiveType = None
        self._RecordLiveUrl = None
        self._EnableAutoStart = None
        self._RecordBackground = None
        self._RTMPStreamingURL = None
        self._RecordScene = None
        self._RecordLang = None
        self._RecordStream = None
        self._RecordLayout = None
        self._WhiteBoardSnapshotMode = None
        self._SubtitlesTranscription = None
        self._Guests = None
        self._RecordMerge = None
        self._RequestId = None

    @property
    def Name(self):
        r"""课堂名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        r"""预定的课堂开始时间，unix时间戳（秒）。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""预定的课堂结束时间，unix时间戳（秒）。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TeacherId(self):
        r"""老师的UserId。
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudienceType(self):
        r"""观看类型。互动观看 （默认）	
        :rtype: int
        """
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def Resolution(self):
        r"""头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :rtype: int
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        r"""设置课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :rtype: int
        """
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def AutoMic(self):
        r"""进入课堂时是否自动连麦。可以有以下取值：
0 不自动连麦（需要手动申请上麦，默认值）
1 自动连麦
        :rtype: int
        """
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def AudioQuality(self):
        r"""高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
        :rtype: int
        """
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def SubType(self):
        r"""课堂子类型，可以有以下取值：videodoc 文档+视频video 纯视频
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def DisableRecord(self):
        r"""上课后是否禁止自动录制。可以有以下取值：
0 不禁止录制（自动开启录制，默认值）
1 禁止录制
注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :rtype: int
        """
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        r"""助教UserId列表。
        :rtype: list of str
        """
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RecordUrl(self):
        r"""录制地址（协议为https)。仅在房间结束后存在。
        :rtype: str
        """
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def Status(self):
        r"""课堂状态。0为未开始，1为已开始，2为已结束，3为已过期。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GroupId(self):
        r"""课堂绑定的群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        r"""打开学生麦克风/摄像头的授权开关
        :rtype: int
        """
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        r"""开启专注模式。
0 收看全部角色音视频(默认)
1 只看老师和助教
        :rtype: int
        """
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        r"""横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :rtype: int
        """
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        r"""该课堂是否开启了课后评分功能。0：未开启  1：开启
        :rtype: int
        """
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        r"""课堂类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (预留参数，暂未开放); 3 圆桌会议 注：大班课的布局(layout)只有三分屏
        :rtype: int
        """
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def VideoDuration(self):
        r"""录制时长
        :rtype: int
        """
        return self._VideoDuration

    @VideoDuration.setter
    def VideoDuration(self, VideoDuration):
        self._VideoDuration = VideoDuration

    @property
    def EndDelayTime(self):
        r"""拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :rtype: int
        """
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        r"""直播类型：0 常规（默认）1 伪直播 2 RTMP推流直播
        :rtype: int
        """
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        r"""伪直播链接
        :rtype: str
        """
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        r"""是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1的时候有效
        :rtype: int
        """
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        r"""录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :rtype: str
        """
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RTMPStreamingURL(self):
        r"""RTMP推流链接
        :rtype: str
        """
        return self._RTMPStreamingURL

    @RTMPStreamingURL.setter
    def RTMPStreamingURL(self, RTMPStreamingURL):
        self._RTMPStreamingURL = RTMPStreamingURL

    @property
    def RecordScene(self):
        r"""录制自定义场景。注意：仅recordlayout=9的时候此参数有效。需注意各类参数配置正确能够生效。不然会造成录制失败，失败后无法补救。数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。自定义场景参数的含义。如下：     scene：自定义js/css对应的场景值。如scene=recordScene，会加载 recordScene 场景对应的 js/css，这样就可以自定义录制页面的元素。     lng：录制页面对应的语种。如lng=en，则录制界面为en。（枚举值：en,zh，zh-TW，jp，ar，kr，vi）     customToken：录制页面中涉及客户自己的服务需要鉴权时进行配置。一般情况下，无需配置。
        :rtype: str
        """
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        r"""录制自定义语言，仅recordlayout=9的时候此参数有效
        :rtype: str
        """
        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        self._RecordLang = RecordLang

    @property
    def RecordStream(self):
        r"""录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :rtype: int
        """
        return self._RecordStream

    @RecordStream.setter
    def RecordStream(self, RecordStream):
        self._RecordStream = RecordStream

    @property
    def RecordLayout(self):
        r"""录制模板。房间子类型为视频+白板（SubType=videodoc）时默认为3，房间子类型为纯视频（SubType=video）时默认为0。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :rtype: int
        """
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def WhiteBoardSnapshotMode(self):
        r"""板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :rtype: int
        """
        return self._WhiteBoardSnapshotMode

    @WhiteBoardSnapshotMode.setter
    def WhiteBoardSnapshotMode(self, WhiteBoardSnapshotMode):
        self._WhiteBoardSnapshotMode = WhiteBoardSnapshotMode

    @property
    def SubtitlesTranscription(self):
        r"""字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :rtype: int
        """
        return self._SubtitlesTranscription

    @SubtitlesTranscription.setter
    def SubtitlesTranscription(self, SubtitlesTranscription):
        self._SubtitlesTranscription = SubtitlesTranscription

    @property
    def Guests(self):
        r"""嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :rtype: list of str
        """
        return self._Guests

    @Guests.setter
    def Guests(self, Guests):
        self._Guests = Guests

    @property
    def RecordMerge(self):
        r"""录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :rtype: int
        """
        return self._RecordMerge

    @RecordMerge.setter
    def RecordMerge(self, RecordMerge):
        self._RecordMerge = RecordMerge

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TeacherId = params.get("TeacherId")
        self._SdkAppId = params.get("SdkAppId")
        self._AudienceType = params.get("AudienceType")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._AutoMic = params.get("AutoMic")
        self._AudioQuality = params.get("AudioQuality")
        self._SubType = params.get("SubType")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._RecordUrl = params.get("RecordUrl")
        self._Status = params.get("Status")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        self._InteractionMode = params.get("InteractionMode")
        self._VideoOrientation = params.get("VideoOrientation")
        self._IsGradingRequiredPostClass = params.get("IsGradingRequiredPostClass")
        self._RoomType = params.get("RoomType")
        self._VideoDuration = params.get("VideoDuration")
        self._EndDelayTime = params.get("EndDelayTime")
        self._LiveType = params.get("LiveType")
        self._RecordLiveUrl = params.get("RecordLiveUrl")
        self._EnableAutoStart = params.get("EnableAutoStart")
        self._RecordBackground = params.get("RecordBackground")
        self._RTMPStreamingURL = params.get("RTMPStreamingURL")
        self._RecordScene = params.get("RecordScene")
        self._RecordLang = params.get("RecordLang")
        self._RecordStream = params.get("RecordStream")
        self._RecordLayout = params.get("RecordLayout")
        self._WhiteBoardSnapshotMode = params.get("WhiteBoardSnapshotMode")
        self._SubtitlesTranscription = params.get("SubtitlesTranscription")
        self._Guests = params.get("Guests")
        self._RecordMerge = params.get("RecordMerge")
        self._RequestId = params.get("RequestId")


class DescribeRoomStatisticsRequest(AbstractModel):
    r"""DescribeRoomStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂Id。
        :type RoomId: int
        :param _Page: 分页查询当前页数，从1开始递增。
        :type Page: int
        :param _Limit: 每页数据量，最大1000。
        :type Limit: int
        """
        self._RoomId = None
        self._Page = None
        self._Limit = None

    @property
    def RoomId(self):
        r"""课堂Id。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页数据量，最大1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomStatisticsResponse(AbstractModel):
    r"""DescribeRoomStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PeakMemberNumber: 峰值在线成员人数。
        :type PeakMemberNumber: int
        :param _MemberNumber: 累计在线人数。
        :type MemberNumber: int
        :param _Total: 记录总数。包含进入房间或者应到未到的。
        :type Total: int
        :param _MemberRecords: 成员记录列表。
        :type MemberRecords: list of MemberRecord
        :param _RealStartTime: 秒级unix时间戳，实际房间开始时间。
        :type RealStartTime: int
        :param _RealEndTime: 秒级unix时间戳，实际房间结束时间。
        :type RealEndTime: int
        :param _MessageCount: 课堂消息总数。
        :type MessageCount: int
        :param _MicCount: 课堂连麦总数。
        :type MicCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PeakMemberNumber = None
        self._MemberNumber = None
        self._Total = None
        self._MemberRecords = None
        self._RealStartTime = None
        self._RealEndTime = None
        self._MessageCount = None
        self._MicCount = None
        self._RequestId = None

    @property
    def PeakMemberNumber(self):
        r"""峰值在线成员人数。
        :rtype: int
        """
        return self._PeakMemberNumber

    @PeakMemberNumber.setter
    def PeakMemberNumber(self, PeakMemberNumber):
        self._PeakMemberNumber = PeakMemberNumber

    @property
    def MemberNumber(self):
        r"""累计在线人数。
        :rtype: int
        """
        return self._MemberNumber

    @MemberNumber.setter
    def MemberNumber(self, MemberNumber):
        self._MemberNumber = MemberNumber

    @property
    def Total(self):
        r"""记录总数。包含进入房间或者应到未到的。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberRecords(self):
        r"""成员记录列表。
        :rtype: list of MemberRecord
        """
        return self._MemberRecords

    @MemberRecords.setter
    def MemberRecords(self, MemberRecords):
        self._MemberRecords = MemberRecords

    @property
    def RealStartTime(self):
        r"""秒级unix时间戳，实际房间开始时间。
        :rtype: int
        """
        return self._RealStartTime

    @RealStartTime.setter
    def RealStartTime(self, RealStartTime):
        self._RealStartTime = RealStartTime

    @property
    def RealEndTime(self):
        r"""秒级unix时间戳，实际房间结束时间。
        :rtype: int
        """
        return self._RealEndTime

    @RealEndTime.setter
    def RealEndTime(self, RealEndTime):
        self._RealEndTime = RealEndTime

    @property
    def MessageCount(self):
        r"""课堂消息总数。
        :rtype: int
        """
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def MicCount(self):
        r"""课堂连麦总数。
        :rtype: int
        """
        return self._MicCount

    @MicCount.setter
    def MicCount(self, MicCount):
        self._MicCount = MicCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PeakMemberNumber = params.get("PeakMemberNumber")
        self._MemberNumber = params.get("MemberNumber")
        self._Total = params.get("Total")
        if params.get("MemberRecords") is not None:
            self._MemberRecords = []
            for item in params.get("MemberRecords"):
                obj = MemberRecord()
                obj._deserialize(item)
                self._MemberRecords.append(obj)
        self._RealStartTime = params.get("RealStartTime")
        self._RealEndTime = params.get("RealEndTime")
        self._MessageCount = params.get("MessageCount")
        self._MicCount = params.get("MicCount")
        self._RequestId = params.get("RequestId")


class DescribeScoreListRequest(AbstractModel):
    r"""DescribeScoreList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂ID
        :type RoomId: int
        :param _Page: 分页查询当前页数，从1开始递增
        :type Page: int
        :param _Limit: 默认是10条
        :type Limit: int
        """
        self._RoomId = None
        self._Page = None
        self._Limit = None

    @property
    def RoomId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""默认是10条
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoreListResponse(AbstractModel):
    r"""DescribeScoreList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Scores: 课堂评分列表
        :type Scores: list of ClassScoreItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Scores = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Scores(self):
        r"""课堂评分列表
        :rtype: list of ClassScoreItem
        """
        return self._Scores

    @Scores.setter
    def Scores(self, Scores):
        self._Scores = Scores

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Scores") is not None:
            self._Scores = []
            for item in params.get("Scores"):
                obj = ClassScoreItem()
                obj._deserialize(item)
                self._Scores.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSdkAppIdUsersRequest(AbstractModel):
    r"""DescribeSdkAppIdUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID
        :type SdkAppId: int
        :param _Page: 分页，默认值为1
        :type Page: int
        :param _Limit: 分页数据限制，默认值为20
        :type Limit: int
        """
        self._SdkAppId = None
        self._Page = None
        self._Limit = None

    @property
    def SdkAppId(self):
        r"""应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        r"""分页，默认值为1
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""分页数据限制，默认值为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSdkAppIdUsersResponse(AbstractModel):
    r"""DescribeSdkAppIdUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 用户总数
        :type Total: int
        :param _Users: 当前获取用户信息数组列表
        :type Users: list of UserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Users = None
        self._RequestId = None

    @property
    def Total(self):
        r"""用户总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Users(self):
        r"""当前获取用户信息数组列表
        :rtype: list of UserInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSupervisorsRequest(AbstractModel):
    r"""DescribeSupervisors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        :param _Limit: 每页数据量，最大100。 不填默认20.
        :type Limit: int
        :param _Page: 分页查询当前页数，从1开始递增，不填默认为1。
        :type Page: int
        """
        self._SdkAppId = None
        self._Limit = None
        self._Page = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。

        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Limit(self):
        r"""每页数据量，最大100。 不填默认20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增，不填默认为1。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSupervisorsResponse(AbstractModel):
    r"""DescribeSupervisors返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数据总量
        :type Total: int
        :param _Page: 分页查询当前页数
        :type Page: int
        :param _Limit: 当前页数据量
        :type Limit: int
        :param _UserIds: 巡课列表
        :type UserIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Page = None
        self._Limit = None
        self._UserIds = None
        self._RequestId = None

    @property
    def Total(self):
        r"""数据总量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Page(self):
        r"""分页查询当前页数
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""当前页数据量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UserIds(self):
        r"""巡课列表
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._UserIds = params.get("UserIds")
        self._RequestId = params.get("RequestId")


class DescribeUserDetailRequest(AbstractModel):
    r"""DescribeUserDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询。
        :type UserId: str
        :param _OriginId: 用户在客户系统的Id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询（UserId不为空时，OriginId不生效）。
        :type OriginId: str
        """
        self._UserId = None
        self._OriginId = None

    @property
    def UserId(self):
        r"""用户id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def OriginId(self):
        r"""用户在客户系统的Id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询（UserId不为空时，OriginId不生效）。
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserDetailResponse(AbstractModel):
    r"""DescribeUserDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 当前获取用户信息数组列表
        :type Users: list of UserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        r"""当前获取用户信息数组列表
        :rtype: list of UserInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    r"""DescribeUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询。
        :type UserId: str
        :param _OriginId: 用户在客户系统的Id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询（UserId不为空时，OriginId不生效）。
        :type OriginId: str
        """
        self._UserId = None
        self._OriginId = None

    @property
    def UserId(self):
        r"""用户id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def OriginId(self):
        r"""用户在客户系统的Id。支持通过 user_id 或 OriginId 查询用户信息，优先使用 user_id 进行查询（UserId不为空时，OriginId不生效）。
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    r"""DescribeUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用Id。
        :type SdkAppId: int
        :param _UserId: 用户Id。
        :type UserId: str
        :param _Name: 用户昵称。
        :type Name: str
        :param _Avatar: 用户头像Url。
        :type Avatar: str
        :param _OriginId: 用户在客户系统的Id
        :type OriginId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Name = None
        self._Avatar = None
        self._OriginId = None
        self._RequestId = None

    @property
    def SdkAppId(self):
        r"""应用Id。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        r"""用户Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        r"""用户昵称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        r"""用户头像Url。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def OriginId(self):
        r"""用户在客户系统的Id
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._OriginId = params.get("OriginId")
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoardSnapshotRequest(AbstractModel):
    r"""DescribeWhiteBoardSnapshot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoardSnapshotResponse(AbstractModel):
    r"""DescribeWhiteBoardSnapshot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WhiteBoardSnapshotMode: 板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :type WhiteBoardSnapshotMode: int
        :param _Status: 板书任务状态，0：未开始，1：进行中，2：失败，3：成功，4：已删除
        :type Status: int
        :param _Result: 板书截图链接
        :type Result: list of str
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WhiteBoardSnapshotMode = None
        self._Status = None
        self._Result = None
        self._Total = None
        self._RequestId = None

    @property
    def WhiteBoardSnapshotMode(self):
        r"""板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :rtype: int
        """
        return self._WhiteBoardSnapshotMode

    @WhiteBoardSnapshotMode.setter
    def WhiteBoardSnapshotMode(self, WhiteBoardSnapshotMode):
        self._WhiteBoardSnapshotMode = WhiteBoardSnapshotMode

    @property
    def Status(self):
        r"""板书任务状态，0：未开始，1：进行中，2：失败，3：成功，4：已删除
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Result(self):
        r"""板书截图链接
        :rtype: list of str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WhiteBoardSnapshotMode = params.get("WhiteBoardSnapshotMode")
        self._Status = params.get("Status")
        self._Result = params.get("Result")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DocumentInfo(AbstractModel):
    r"""文档信息

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档Id
        :type DocumentId: str
        :param _DocumentUrl: 文档原址url
        :type DocumentUrl: str
        :param _DocumentName: 文档名称
        :type DocumentName: str
        :param _Owner: 文档所有者UserId
        :type Owner: str
        :param _SdkAppId: 应用Id
        :type SdkAppId: int
        :param _Permission: 文档权限，0：私有课件 1：公共课件
        :type Permission: int
        :param _TranscodeResult: 转码结果，无需转码为空，转码成功为结果url，转码失败为错误码
        :type TranscodeResult: str
        :param _TranscodeType: 转码类型
        :type TranscodeType: int
        :param _TranscodeProgress: 转码进度， 0 - 100 表示（0% - 100%）
        :type TranscodeProgress: int
        :param _TranscodeState: 转码状态，0为无需转码，1为正在转码，2为转码失败，3为转码成功
        :type TranscodeState: int
        :param _TranscodeInfo: 转码失败后的错误信息
        :type TranscodeInfo: str
        :param _DocumentType: 文档类型
        :type DocumentType: str
        :param _DocumentSize: 文档大小，单位：字节
        :type DocumentSize: int
        :param _UpdateTime: 更新的UNIX时间戳
        :type UpdateTime: int
        :param _Pages: 课件页数
        :type Pages: int
        :param _Width: 宽，仅在静态转码的课件有效
        :type Width: int
        :param _Height: 高，仅在静态转码的课件有效
        :type Height: int
        :param _Cover: 封面，仅转码的课件会生成封面
        :type Cover: str
        :param _Preview: 课件预览地址
        :type Preview: str
        :param _Resolution: 文档的分辨率
        :type Resolution: str
        :param _MinScaleResolution: 转码后文档的最小分辨率，和创建文档时传入的参数一致。
        :type MinScaleResolution: str
        """
        self._DocumentId = None
        self._DocumentUrl = None
        self._DocumentName = None
        self._Owner = None
        self._SdkAppId = None
        self._Permission = None
        self._TranscodeResult = None
        self._TranscodeType = None
        self._TranscodeProgress = None
        self._TranscodeState = None
        self._TranscodeInfo = None
        self._DocumentType = None
        self._DocumentSize = None
        self._UpdateTime = None
        self._Pages = None
        self._Width = None
        self._Height = None
        self._Cover = None
        self._Preview = None
        self._Resolution = None
        self._MinScaleResolution = None

    @property
    def DocumentId(self):
        r"""文档Id
        :rtype: str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def DocumentUrl(self):
        r"""文档原址url
        :rtype: str
        """
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        r"""文档名称
        :rtype: str
        """
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        r"""文档所有者UserId
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SdkAppId(self):
        r"""应用Id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Permission(self):
        r"""文档权限，0：私有课件 1：公共课件
        :rtype: int
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def TranscodeResult(self):
        r"""转码结果，无需转码为空，转码成功为结果url，转码失败为错误码
        :rtype: str
        """
        return self._TranscodeResult

    @TranscodeResult.setter
    def TranscodeResult(self, TranscodeResult):
        self._TranscodeResult = TranscodeResult

    @property
    def TranscodeType(self):
        r"""转码类型
        :rtype: int
        """
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def TranscodeProgress(self):
        r"""转码进度， 0 - 100 表示（0% - 100%）
        :rtype: int
        """
        return self._TranscodeProgress

    @TranscodeProgress.setter
    def TranscodeProgress(self, TranscodeProgress):
        self._TranscodeProgress = TranscodeProgress

    @property
    def TranscodeState(self):
        r"""转码状态，0为无需转码，1为正在转码，2为转码失败，3为转码成功
        :rtype: int
        """
        return self._TranscodeState

    @TranscodeState.setter
    def TranscodeState(self, TranscodeState):
        self._TranscodeState = TranscodeState

    @property
    def TranscodeInfo(self):
        r"""转码失败后的错误信息
        :rtype: str
        """
        return self._TranscodeInfo

    @TranscodeInfo.setter
    def TranscodeInfo(self, TranscodeInfo):
        self._TranscodeInfo = TranscodeInfo

    @property
    def DocumentType(self):
        r"""文档类型
        :rtype: str
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        r"""文档大小，单位：字节
        :rtype: int
        """
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def UpdateTime(self):
        r"""更新的UNIX时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Pages(self):
        r"""课件页数
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Width(self):
        r"""宽，仅在静态转码的课件有效
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""高，仅在静态转码的课件有效
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Cover(self):
        r"""封面，仅转码的课件会生成封面
        :rtype: str
        """
        return self._Cover

    @Cover.setter
    def Cover(self, Cover):
        self._Cover = Cover

    @property
    def Preview(self):
        r"""课件预览地址
        :rtype: str
        """
        return self._Preview

    @Preview.setter
    def Preview(self, Preview):
        self._Preview = Preview

    @property
    def Resolution(self):
        r"""文档的分辨率
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MinScaleResolution(self):
        r"""转码后文档的最小分辨率，和创建文档时传入的参数一致。
        :rtype: str
        """
        return self._MinScaleResolution

    @MinScaleResolution.setter
    def MinScaleResolution(self, MinScaleResolution):
        self._MinScaleResolution = MinScaleResolution


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._DocumentUrl = params.get("DocumentUrl")
        self._DocumentName = params.get("DocumentName")
        self._Owner = params.get("Owner")
        self._SdkAppId = params.get("SdkAppId")
        self._Permission = params.get("Permission")
        self._TranscodeResult = params.get("TranscodeResult")
        self._TranscodeType = params.get("TranscodeType")
        self._TranscodeProgress = params.get("TranscodeProgress")
        self._TranscodeState = params.get("TranscodeState")
        self._TranscodeInfo = params.get("TranscodeInfo")
        self._DocumentType = params.get("DocumentType")
        self._DocumentSize = params.get("DocumentSize")
        self._UpdateTime = params.get("UpdateTime")
        self._Pages = params.get("Pages")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Cover = params.get("Cover")
        self._Preview = params.get("Preview")
        self._Resolution = params.get("Resolution")
        self._MinScaleResolution = params.get("MinScaleResolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndRoomRequest(AbstractModel):
    r"""EndRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂ID
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndRoomResponse(AbstractModel):
    r"""EndRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EventDataInfo(AbstractModel):
    r"""房间事件对应的信息。

    """

    def __init__(self):
        r"""
        :param _RoomId: 事件发生的房间号。
        :type RoomId: int
        :param _UserId: 事件发生的用户。
        :type UserId: str
        :param _Device: 用户设备类型。0: Unknown; 1: Windows; 2: macOS; 3: Android; 4: iOS; 5: Web; 6: Mobile webpage; 7: Weixin Mini Program.
        :type Device: int
        :param _Duration: 录制时长。单位：秒
        :type Duration: int
        :param _RecordSize: 录制文件大小
        :type RecordSize: int
        :param _RecordUrl: 录制url
        :type RecordUrl: str
        """
        self._RoomId = None
        self._UserId = None
        self._Device = None
        self._Duration = None
        self._RecordSize = None
        self._RecordUrl = None

    @property
    def RoomId(self):
        r"""事件发生的房间号。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""事件发生的用户。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Device(self):
        r"""用户设备类型。0: Unknown; 1: Windows; 2: macOS; 3: Android; 4: iOS; 5: Web; 6: Mobile webpage; 7: Weixin Mini Program.
        :rtype: int
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Duration(self):
        r"""录制时长。单位：秒
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RecordSize(self):
        r"""录制文件大小
        :rtype: int
        """
        return self._RecordSize

    @RecordSize.setter
    def RecordSize(self, RecordSize):
        self._RecordSize = RecordSize

    @property
    def RecordUrl(self):
        r"""录制url
        :rtype: str
        """
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._Device = params.get("Device")
        self._Duration = params.get("Duration")
        self._RecordSize = params.get("RecordSize")
        self._RecordUrl = params.get("RecordUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    r"""房间事件信息。

    """

    def __init__(self):
        r"""
        :param _Timestamp: 事件发生的秒级unix时间戳。
        :type Timestamp: int
        :param _EventType: 事件类型,有以下值:
RoomStart:房间开始 RoomEnd:房间结束 MemberJoin:成员加入 MemberQuit:成员退出 RecordFinish:录制结束
CameraOn: 摄像头打开
CameraOff: 摄像头关闭
MicOn: 麦克风打开
MicOff: 麦克风关闭
ScreenOn: 屏幕共享打开
ScreenOff: 屏幕共享关闭
VisibleOn: 页面可见
VisibleOff: 页面不可见
        :type EventType: str
        :param _EventData: 事件详细内容，包含房间号,成员类型事件包含用户Id。
        :type EventData: :class:`tencentcloud.lcic.v20220817.models.EventDataInfo`
        """
        self._Timestamp = None
        self._EventType = None
        self._EventData = None

    @property
    def Timestamp(self):
        r"""事件发生的秒级unix时间戳。
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def EventType(self):
        r"""事件类型,有以下值:
RoomStart:房间开始 RoomEnd:房间结束 MemberJoin:成员加入 MemberQuit:成员退出 RecordFinish:录制结束
CameraOn: 摄像头打开
CameraOff: 摄像头关闭
MicOn: 麦克风打开
MicOff: 麦克风关闭
ScreenOn: 屏幕共享打开
ScreenOff: 屏幕共享关闭
VisibleOn: 页面可见
VisibleOff: 页面不可见
        :rtype: str
        """
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventData(self):
        r"""事件详细内容，包含房间号,成员类型事件包含用户Id。
        :rtype: :class:`tencentcloud.lcic.v20220817.models.EventDataInfo`
        """
        return self._EventData

    @EventData.setter
    def EventData(self, EventData):
        self._EventData = EventData


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._EventType = params.get("EventType")
        if params.get("EventData") is not None:
            self._EventData = EventDataInfo()
            self._EventData._deserialize(params.get("EventData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceMsgContent(AbstractModel):
    r"""表情消息

    """

    def __init__(self):
        r"""
        :param _Index: 表情索引，用户自定义。
        :type Index: int
        :param _Data: 额外数据。
        :type Data: str
        """
        self._Index = None
        self._Data = None

    @property
    def Index(self):
        r"""表情索引，用户自定义。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Data(self):
        r"""额外数据。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidSendMsgRequest(AbstractModel):
    r"""ForbidSendMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 课堂ID
        :type RoomId: int
        :param _MembersAccount: 需要禁言的用户账号，最多支持500个账号
        :type MembersAccount: list of str
        :param _MuteTime: 需禁言时间，单位为秒，为0时表示取消禁言，4294967295为永久禁言。
        :type MuteTime: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._MembersAccount = None
        self._MuteTime = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def MembersAccount(self):
        r"""需要禁言的用户账号，最多支持500个账号
        :rtype: list of str
        """
        return self._MembersAccount

    @MembersAccount.setter
    def MembersAccount(self, MembersAccount):
        self._MembersAccount = MembersAccount

    @property
    def MuteTime(self):
        r"""需禁言时间，单位为秒，为0时表示取消禁言，4294967295为永久禁言。
        :rtype: int
        """
        return self._MuteTime

    @MuteTime.setter
    def MuteTime(self, MuteTime):
        self._MuteTime = MuteTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._MembersAccount = params.get("MembersAccount")
        self._MuteTime = params.get("MuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidSendMsgResponse(AbstractModel):
    r"""ForbidSendMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class GetRoomEventRequest(AbstractModel):
    r"""GetRoomEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂Id。
        :type RoomId: int
        :param _SdkAppId: 应用Id。
        :type SdkAppId: int
        :param _Page: 起始页，1开始。keyword为空时有效。
        :type Page: int
        :param _Limit: 每页个数。keyword为空时有效。一次性最多100条。
        :type Limit: int
        :param _Keyword: 搜索事件类型。有以下事件类型:
RoomStart:房间开始
RoomEnd:房间结束
MemberJoin:成员加入
MemberQuit:成员退出
RecordFinish:录制结束
CameraOn: 摄像头打开
CameraOff: 摄像头关闭
MicOn: 麦克风打开
MicOff: 麦克风关闭
ScreenOn: 屏幕共享打开
ScreenOff: 屏幕共享关闭
VisibleOn: 页面可见
VisibleOff: 页面不可见
        :type Keyword: str
        """
        self._RoomId = None
        self._SdkAppId = None
        self._Page = None
        self._Limit = None
        self._Keyword = None

    @property
    def RoomId(self):
        r"""课堂Id。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""应用Id。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        r"""起始页，1开始。keyword为空时有效。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""每页个数。keyword为空时有效。一次性最多100条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        r"""搜索事件类型。有以下事件类型:
RoomStart:房间开始
RoomEnd:房间结束
MemberJoin:成员加入
MemberQuit:成员退出
RecordFinish:录制结束
CameraOn: 摄像头打开
CameraOff: 摄像头关闭
MicOn: 麦克风打开
MicOff: 麦克风关闭
ScreenOn: 屏幕共享打开
ScreenOff: 屏幕共享关闭
VisibleOn: 页面可见
VisibleOff: 页面不可见
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomEventResponse(AbstractModel):
    r"""GetRoomEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 该课堂的事件总数，keyword搜索不影响该值。
        :type Total: int
        :param _Events: 详细事件内容。包含相应的类型、发生的时间戳。
        :type Events: list of EventInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Events = None
        self._RequestId = None

    @property
    def Total(self):
        r"""该课堂的事件总数，keyword搜索不影响该值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Events(self):
        r"""详细事件内容。包含相应的类型、发生的时间戳。
        :rtype: list of EventInfo
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._RequestId = params.get("RequestId")


class GetRoomMessageRequest(AbstractModel):
    r"""GetRoomMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 课堂Id。	
        :type RoomId: int
        :param _Seq: 消息序列。获取该序列以前的消息(不包含该seq消息)
        :type Seq: int
        :param _Limit: 消息拉取的条数。最大数量不能超过套餐包限制。
        :type Limit: int
        :param _UserId: 请求消息的userId
        :type UserId: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._Seq = None
        self._Limit = None
        self._UserId = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""课堂Id。	
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Seq(self):
        r"""消息序列。获取该序列以前的消息(不包含该seq消息)
        :rtype: int
        """
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def Limit(self):
        r"""消息拉取的条数。最大数量不能超过套餐包限制。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UserId(self):
        r"""请求消息的userId
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._Seq = params.get("Seq")
        self._Limit = params.get("Limit")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomMessageResponse(AbstractModel):
    r"""GetRoomMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 消息列表
        :type Messages: list of MessageList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Messages = None
        self._RequestId = None

    @property
    def Messages(self):
        r"""消息列表
        :rtype: list of MessageList
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = MessageList()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._RequestId = params.get("RequestId")


class GetRoomsRequest(AbstractModel):
    r"""GetRooms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码平台的SdkAppId。

        :type SdkAppId: int
        :param _StartTime: 开始时间。默认以当前时间减去半小时作为开始时间。
        :type StartTime: int
        :param _EndTime: 结束时间。默认以当前时间加上半小时作为结束时间。
        :type EndTime: int
        :param _Page: 分页查询当前页数，从1开始递增
        :type Page: int
        :param _Limit: 默认10条，最大上限为100条
        :type Limit: int
        :param _Status: 课堂状态。默认展示所有课堂，0为未开始，1为正在上课，2为已结束，3为已过期
        :type Status: list of int non-negative
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Page = None
        self._Limit = None
        self._Status = None

    @property
    def SdkAppId(self):
        r"""低代码平台的SdkAppId。

        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""开始时间。默认以当前时间减去半小时作为开始时间。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间。默认以当前时间加上半小时作为结束时间。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Page(self):
        r"""分页查询当前页数，从1开始递增
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        r"""默认10条，最大上限为100条
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        r"""课堂状态。默认展示所有课堂，0为未开始，1为正在上课，2为已结束，3为已过期
        :rtype: list of int non-negative
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomsResponse(AbstractModel):
    r"""GetRooms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Rooms: 课堂列表
        :type Rooms: list of RoomItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Rooms = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Rooms(self):
        r"""课堂列表
        :rtype: list of RoomItem
        """
        return self._Rooms

    @Rooms.setter
    def Rooms(self, Rooms):
        self._Rooms = Rooms

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Rooms") is not None:
            self._Rooms = []
            for item in params.get("Rooms"):
                obj = RoomItem()
                obj._deserialize(item)
                self._Rooms.append(obj)
        self._RequestId = params.get("RequestId")


class GetWatermarkRequest(AbstractModel):
    r"""GetWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        """
        self._SdkAppId = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。

        :rtype: int
        """
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
        


class GetWatermarkResponse(AbstractModel):
    r"""GetWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TeacherLogo: 老师视频区域的水印参数配置
        :type TeacherLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param _BoardLogo: 白板区域的水印参数配置
        :type BoardLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param _BackgroundPicture: 背景图片配置
        :type BackgroundPicture: :class:`tencentcloud.lcic.v20220817.models.BackgroundPictureConfig`
        :param _Text: 文字水印配置
        :type Text: :class:`tencentcloud.lcic.v20220817.models.TextMarkConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TeacherLogo = None
        self._BoardLogo = None
        self._BackgroundPicture = None
        self._Text = None
        self._RequestId = None

    @property
    def TeacherLogo(self):
        r"""老师视频区域的水印参数配置
        :rtype: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        """
        return self._TeacherLogo

    @TeacherLogo.setter
    def TeacherLogo(self, TeacherLogo):
        self._TeacherLogo = TeacherLogo

    @property
    def BoardLogo(self):
        r"""白板区域的水印参数配置
        :rtype: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        """
        return self._BoardLogo

    @BoardLogo.setter
    def BoardLogo(self, BoardLogo):
        self._BoardLogo = BoardLogo

    @property
    def BackgroundPicture(self):
        r"""背景图片配置
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BackgroundPictureConfig`
        """
        return self._BackgroundPicture

    @BackgroundPicture.setter
    def BackgroundPicture(self, BackgroundPicture):
        self._BackgroundPicture = BackgroundPicture

    @property
    def Text(self):
        r"""文字水印配置
        :rtype: :class:`tencentcloud.lcic.v20220817.models.TextMarkConfig`
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TeacherLogo") is not None:
            self._TeacherLogo = WatermarkConfig()
            self._TeacherLogo._deserialize(params.get("TeacherLogo"))
        if params.get("BoardLogo") is not None:
            self._BoardLogo = WatermarkConfig()
            self._BoardLogo._deserialize(params.get("BoardLogo"))
        if params.get("BackgroundPicture") is not None:
            self._BackgroundPicture = BackgroundPictureConfig()
            self._BackgroundPicture._deserialize(params.get("BackgroundPicture"))
        if params.get("Text") is not None:
            self._Text = TextMarkConfig()
            self._Text._deserialize(params.get("Text"))
        self._RequestId = params.get("RequestId")


class GroupBaseInfo(AbstractModel):
    r"""批量创建群组基础信息

    """

    def __init__(self):
        r"""
        :param _GroupName: 待创建群组名
        :type GroupName: str
        :param _TeacherId: 群组主讲人ID
        :type TeacherId: str
        """
        self._GroupName = None
        self._TeacherId = None

    @property
    def GroupName(self):
        r"""待创建群组名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        r"""群组主讲人ID
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._TeacherId = params.get("TeacherId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    r"""获取群组列表返回的群组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
        :type GroupId: str
        :param _GroupName: 群组名称
        :type GroupName: str
        :param _TeacherId: 群组主讲人ID
        :type TeacherId: str
        :param _GroupType: 群组类型 
0-基础群组 
1-组合群组，若为1时会返回子群组ID列表
        :type GroupType: int
        :param _SubGroupIds: 子群组ID列表，如有。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubGroupIds: str
        """
        self._GroupId = None
        self._GroupName = None
        self._TeacherId = None
        self._GroupType = None
        self._SubGroupIds = None

    @property
    def GroupId(self):
        r"""群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""群组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        r"""群组主讲人ID
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupType(self):
        r"""群组类型 
0-基础群组 
1-组合群组，若为1时会返回子群组ID列表
        :rtype: int
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def SubGroupIds(self):
        r"""子群组ID列表，如有。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._TeacherId = params.get("TeacherId")
        self._GroupType = params.get("GroupType")
        self._SubGroupIds = params.get("SubGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    r"""单张图片信息

    """

    def __init__(self):
        r"""
        :param _Type: 图片类型：
1-原图
2-大图
3-缩略图

        :type Type: int
        :param _Size: 图片数据大小，单位：字节。
        :type Size: int
        :param _Width: 图片宽度，单位为像素。
        :type Width: int
        :param _Height: 图片高度，单位为像素。
        :type Height: int
        :param _URL: 图片下载地址。
        :type URL: str
        """
        self._Type = None
        self._Size = None
        self._Width = None
        self._Height = None
        self._URL = None

    @property
    def Type(self):
        r"""图片类型：
1-原图
2-大图
3-缩略图

        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        r"""图片数据大小，单位：字节。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Width(self):
        r"""图片宽度，单位为像素。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""图片高度，单位为像素。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def URL(self):
        r"""图片下载地址。
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._URL = params.get("URL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageMsgContent(AbstractModel):
    r"""图片消息

    """

    def __init__(self):
        r"""
        :param _UUID: 图片的唯一标识，客户端用于索引图片的键值。
        :type UUID: str
        :param _ImageFormat: 图片格式。
JPG = 1
GIF = 2
PNG = 3
BMP = 4
其他 = 255

        :type ImageFormat: int
        :param _ImageInfoList: 图片信息
        :type ImageInfoList: list of ImageInfo
        """
        self._UUID = None
        self._ImageFormat = None
        self._ImageInfoList = None

    @property
    def UUID(self):
        r"""图片的唯一标识，客户端用于索引图片的键值。
        :rtype: str
        """
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID

    @property
    def ImageFormat(self):
        r"""图片格式。
JPG = 1
GIF = 2
PNG = 3
BMP = 4
其他 = 255

        :rtype: int
        """
        return self._ImageFormat

    @ImageFormat.setter
    def ImageFormat(self, ImageFormat):
        self._ImageFormat = ImageFormat

    @property
    def ImageInfoList(self):
        r"""图片信息
        :rtype: list of ImageInfo
        """
        return self._ImageInfoList

    @ImageInfoList.setter
    def ImageInfoList(self, ImageInfoList):
        self._ImageInfoList = ImageInfoList


    def _deserialize(self, params):
        self._UUID = params.get("UUID")
        self._ImageFormat = params.get("ImageFormat")
        if params.get("ImageInfoList") is not None:
            self._ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._ImageInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KickUserFromRoomRequest(AbstractModel):
    r"""KickUserFromRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂Id。
        :type RoomId: int
        :param _SdkAppId: 低代码平台的SdkAppId。
        :type SdkAppId: int
        :param _UserId: 需要踢出成员Id
        :type UserId: str
        :param _KickType: 踢出类型：
1：临时踢出，可以使用Duration参数指定污点时间，污点时间间隔内用户无法进入房间。
2：永久踢出
        :type KickType: int
        :param _Duration: 污点时间(单位秒)，KickType = 1时生效，默认为0
        :type Duration: int
        """
        self._RoomId = None
        self._SdkAppId = None
        self._UserId = None
        self._KickType = None
        self._Duration = None

    @property
    def RoomId(self):
        r"""课堂Id。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""低代码平台的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        r"""需要踢出成员Id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def KickType(self):
        r"""踢出类型：
1：临时踢出，可以使用Duration参数指定污点时间，污点时间间隔内用户无法进入房间。
2：永久踢出
        :rtype: int
        """
        return self._KickType

    @KickType.setter
    def KickType(self, KickType):
        self._KickType = KickType

    @property
    def Duration(self):
        r"""污点时间(单位秒)，KickType = 1时生效，默认为0
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._KickType = params.get("KickType")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KickUserFromRoomResponse(AbstractModel):
    r"""KickUserFromRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class LoginOriginIdRequest(AbstractModel):
    r"""LoginOriginId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _OriginId: 用户在客户系统的Id，需要在同一应用下唯一。
        :type OriginId: str
        """
        self._SdkAppId = None
        self._OriginId = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def OriginId(self):
        r"""用户在客户系统的Id，需要在同一应用下唯一。
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginOriginIdResponse(AbstractModel):
    r"""LoginOriginId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id。
        :type UserId: str
        :param _Token: 登录/注册成功后返回登录态token。有效期7天。
        :type Token: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._Token = None
        self._RequestId = None

    @property
    def UserId(self):
        r"""用户Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        r"""登录/注册成功后返回登录态token。有效期7天。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class LoginUserRequest(AbstractModel):
    r"""LoginUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 注册获取的用户id。
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        r"""注册获取的用户id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginUserResponse(AbstractModel):
    r"""LoginUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id。
        :type UserId: str
        :param _Token: 注册成功后返回登录态token，有效期7天。token过期后可以通过调用“登录”或“源账号登录”进行更新。
        :type Token: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._Token = None
        self._RequestId = None

    @property
    def UserId(self):
        r"""用户Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        r"""注册成功后返回登录态token，有效期7天。token过期后可以通过调用“登录”或“源账号登录”进行更新。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class MemberRecord(AbstractModel):
    r"""成员记录信息。

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID。
        :type UserId: str
        :param _UserName: 用户名称。
        :type UserName: str
        :param _PresentTime: 在线时长，单位秒。
        :type PresentTime: int
        :param _Camera: 是否开启摄像头。
        :type Camera: int
        :param _Mic: 是否开启麦克风。
        :type Mic: int
        :param _Silence: 是否禁言。
        :type Silence: int
        :param _AnswerQuestions: 回答问题数量。
        :type AnswerQuestions: int
        :param _HandUps: 举手数量。
        :type HandUps: int
        :param _FirstJoinTimestamp: 首次进入房间的unix时间戳。
        :type FirstJoinTimestamp: int
        :param _LastQuitTimestamp: 最后一次退出房间的unix时间戳。
        :type LastQuitTimestamp: int
        :param _Rewords: 奖励次数。
        :type Rewords: int
        :param _IPAddress: 用户IP。
        :type IPAddress: str
        :param _Location: 用户位置信息。
        :type Location: str
        :param _Device: 用户设备平台信息。0:unknown  1:windows  2:mac  3:android  4:ios  5:web   6:h5   7:miniprogram （小程序）
        :type Device: int
        :param _PerMemberMicCount: 每个成员上麦次数。
        :type PerMemberMicCount: int
        :param _PerMemberMessageCount: 每个成员发送消息数量。

        :type PerMemberMessageCount: int
        :param _Role: 用户角色。0代表学生；1代表老师； 2助教；3巡课。
        :type Role: int
        :param _GroupId: 上课班号
        :type GroupId: str
        :param _SubGroupId: 子上课班号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubGroupId: list of str
        :param _Stage: 本堂课用户是否上过台。0 否；1 是
        :type Stage: int
        :param _CurrentState: 用户状态。0为未到，1为在线，2为离线，3为被踢，4为永久被踢，5为暂时掉线
        :type CurrentState: int
        """
        self._UserId = None
        self._UserName = None
        self._PresentTime = None
        self._Camera = None
        self._Mic = None
        self._Silence = None
        self._AnswerQuestions = None
        self._HandUps = None
        self._FirstJoinTimestamp = None
        self._LastQuitTimestamp = None
        self._Rewords = None
        self._IPAddress = None
        self._Location = None
        self._Device = None
        self._PerMemberMicCount = None
        self._PerMemberMessageCount = None
        self._Role = None
        self._GroupId = None
        self._SubGroupId = None
        self._Stage = None
        self._CurrentState = None

    @property
    def UserId(self):
        r"""用户ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        r"""用户名称。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PresentTime(self):
        r"""在线时长，单位秒。
        :rtype: int
        """
        return self._PresentTime

    @PresentTime.setter
    def PresentTime(self, PresentTime):
        self._PresentTime = PresentTime

    @property
    def Camera(self):
        r"""是否开启摄像头。
        :rtype: int
        """
        return self._Camera

    @Camera.setter
    def Camera(self, Camera):
        self._Camera = Camera

    @property
    def Mic(self):
        r"""是否开启麦克风。
        :rtype: int
        """
        return self._Mic

    @Mic.setter
    def Mic(self, Mic):
        self._Mic = Mic

    @property
    def Silence(self):
        r"""是否禁言。
        :rtype: int
        """
        return self._Silence

    @Silence.setter
    def Silence(self, Silence):
        self._Silence = Silence

    @property
    def AnswerQuestions(self):
        r"""回答问题数量。
        :rtype: int
        """
        return self._AnswerQuestions

    @AnswerQuestions.setter
    def AnswerQuestions(self, AnswerQuestions):
        self._AnswerQuestions = AnswerQuestions

    @property
    def HandUps(self):
        r"""举手数量。
        :rtype: int
        """
        return self._HandUps

    @HandUps.setter
    def HandUps(self, HandUps):
        self._HandUps = HandUps

    @property
    def FirstJoinTimestamp(self):
        r"""首次进入房间的unix时间戳。
        :rtype: int
        """
        return self._FirstJoinTimestamp

    @FirstJoinTimestamp.setter
    def FirstJoinTimestamp(self, FirstJoinTimestamp):
        self._FirstJoinTimestamp = FirstJoinTimestamp

    @property
    def LastQuitTimestamp(self):
        r"""最后一次退出房间的unix时间戳。
        :rtype: int
        """
        return self._LastQuitTimestamp

    @LastQuitTimestamp.setter
    def LastQuitTimestamp(self, LastQuitTimestamp):
        self._LastQuitTimestamp = LastQuitTimestamp

    @property
    def Rewords(self):
        r"""奖励次数。
        :rtype: int
        """
        return self._Rewords

    @Rewords.setter
    def Rewords(self, Rewords):
        self._Rewords = Rewords

    @property
    def IPAddress(self):
        r"""用户IP。
        :rtype: str
        """
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress

    @property
    def Location(self):
        r"""用户位置信息。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Device(self):
        r"""用户设备平台信息。0:unknown  1:windows  2:mac  3:android  4:ios  5:web   6:h5   7:miniprogram （小程序）
        :rtype: int
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def PerMemberMicCount(self):
        r"""每个成员上麦次数。
        :rtype: int
        """
        return self._PerMemberMicCount

    @PerMemberMicCount.setter
    def PerMemberMicCount(self, PerMemberMicCount):
        self._PerMemberMicCount = PerMemberMicCount

    @property
    def PerMemberMessageCount(self):
        r"""每个成员发送消息数量。

        :rtype: int
        """
        return self._PerMemberMessageCount

    @PerMemberMessageCount.setter
    def PerMemberMessageCount(self, PerMemberMessageCount):
        self._PerMemberMessageCount = PerMemberMessageCount

    @property
    def Role(self):
        r"""用户角色。0代表学生；1代表老师； 2助教；3巡课。
        :rtype: int
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def GroupId(self):
        r"""上课班号
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SubGroupId(self):
        r"""子上课班号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SubGroupId

    @SubGroupId.setter
    def SubGroupId(self, SubGroupId):
        self._SubGroupId = SubGroupId

    @property
    def Stage(self):
        r"""本堂课用户是否上过台。0 否；1 是
        :rtype: int
        """
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def CurrentState(self):
        r"""用户状态。0为未到，1为在线，2为离线，3为被踢，4为永久被踢，5为暂时掉线
        :rtype: int
        """
        return self._CurrentState

    @CurrentState.setter
    def CurrentState(self, CurrentState):
        self._CurrentState = CurrentState


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._PresentTime = params.get("PresentTime")
        self._Camera = params.get("Camera")
        self._Mic = params.get("Mic")
        self._Silence = params.get("Silence")
        self._AnswerQuestions = params.get("AnswerQuestions")
        self._HandUps = params.get("HandUps")
        self._FirstJoinTimestamp = params.get("FirstJoinTimestamp")
        self._LastQuitTimestamp = params.get("LastQuitTimestamp")
        self._Rewords = params.get("Rewords")
        self._IPAddress = params.get("IPAddress")
        self._Location = params.get("Location")
        self._Device = params.get("Device")
        self._PerMemberMicCount = params.get("PerMemberMicCount")
        self._PerMemberMessageCount = params.get("PerMemberMessageCount")
        self._Role = params.get("Role")
        self._GroupId = params.get("GroupId")
        self._SubGroupId = params.get("SubGroupId")
        self._Stage = params.get("Stage")
        self._CurrentState = params.get("CurrentState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageItem(AbstractModel):
    r"""单条消息体内容

    """

    def __init__(self):
        r"""
        :param _MessageType: 消息类型。0表示文本消息，1表示图片消息
        :type MessageType: int
        :param _TextMessage: 文本消息内容。message type为0时有效。
        :type TextMessage: str
        :param _ImageMessage: 图片消息URL。 message type为1时有效。
        :type ImageMessage: str
        :param _CustomMessage: 自定义消息内容。message type为2时有效。
        :type CustomMessage: :class:`tencentcloud.lcic.v20220817.models.CustomMsgContent`
        """
        self._MessageType = None
        self._TextMessage = None
        self._ImageMessage = None
        self._CustomMessage = None

    @property
    def MessageType(self):
        r"""消息类型。0表示文本消息，1表示图片消息
        :rtype: int
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def TextMessage(self):
        r"""文本消息内容。message type为0时有效。
        :rtype: str
        """
        return self._TextMessage

    @TextMessage.setter
    def TextMessage(self, TextMessage):
        self._TextMessage = TextMessage

    @property
    def ImageMessage(self):
        r"""图片消息URL。 message type为1时有效。
        :rtype: str
        """
        return self._ImageMessage

    @ImageMessage.setter
    def ImageMessage(self, ImageMessage):
        self._ImageMessage = ImageMessage

    @property
    def CustomMessage(self):
        r"""自定义消息内容。message type为2时有效。
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CustomMsgContent`
        """
        return self._CustomMessage

    @CustomMessage.setter
    def CustomMessage(self, CustomMessage):
        self._CustomMessage = CustomMessage


    def _deserialize(self, params):
        self._MessageType = params.get("MessageType")
        self._TextMessage = params.get("TextMessage")
        self._ImageMessage = params.get("ImageMessage")
        if params.get("CustomMessage") is not None:
            self._CustomMessage = CustomMsgContent()
            self._CustomMessage._deserialize(params.get("CustomMessage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MessageList(AbstractModel):
    r"""历史消息列表

    """

    def __init__(self):
        r"""
        :param _Timestamp: 消息时间戳
        :type Timestamp: int
        :param _FromAccount: 消息发送者
        :type FromAccount: str
        :param _Seq: 消息序列号，当前课堂内唯一且单调递增
        :type Seq: int
        :param _MessageBody: 历史消息列表
        :type MessageBody: list of MessageItem
        """
        self._Timestamp = None
        self._FromAccount = None
        self._Seq = None
        self._MessageBody = None

    @property
    def Timestamp(self):
        r"""消息时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def FromAccount(self):
        r"""消息发送者
        :rtype: str
        """
        return self._FromAccount

    @FromAccount.setter
    def FromAccount(self, FromAccount):
        self._FromAccount = FromAccount

    @property
    def Seq(self):
        r"""消息序列号，当前课堂内唯一且单调递增
        :rtype: int
        """
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def MessageBody(self):
        r"""历史消息列表
        :rtype: list of MessageItem
        """
        return self._MessageBody

    @MessageBody.setter
    def MessageBody(self, MessageBody):
        self._MessageBody = MessageBody


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._FromAccount = params.get("FromAccount")
        self._Seq = params.get("Seq")
        if params.get("MessageBody") is not None:
            self._MessageBody = []
            for item in params.get("MessageBody"):
                obj = MessageItem()
                obj._deserialize(item)
                self._MessageBody.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppRequest(AbstractModel):
    r"""ModifyApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _Callback: 回调地址。
        :type Callback: str
        :param _CallbackKey: 回调key。
        :type CallbackKey: str
        :param _TransferId: 转存id
        :type TransferId: str
        :param _TransferUrl: 转存地址
        :type TransferUrl: str
        """
        self._SdkAppId = None
        self._Callback = None
        self._CallbackKey = None
        self._TransferId = None
        self._TransferUrl = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Callback(self):
        r"""回调地址。
        :rtype: str
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CallbackKey(self):
        r"""回调key。
        :rtype: str
        """
        return self._CallbackKey

    @CallbackKey.setter
    def CallbackKey(self, CallbackKey):
        self._CallbackKey = CallbackKey

    @property
    def TransferId(self):
        r"""转存id
        :rtype: str
        """
        return self._TransferId

    @TransferId.setter
    def TransferId(self, TransferId):
        self._TransferId = TransferId

    @property
    def TransferUrl(self):
        r"""转存地址
        :rtype: str
        """
        return self._TransferUrl

    @TransferUrl.setter
    def TransferUrl(self, TransferUrl):
        self._TransferUrl = TransferUrl


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Callback = params.get("Callback")
        self._CallbackKey = params.get("CallbackKey")
        self._TransferId = params.get("TransferId")
        self._TransferUrl = params.get("TransferUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppResponse(AbstractModel):
    r"""ModifyApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyGroupRequest(AbstractModel):
    r"""ModifyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 需要修改的群组ID
        :type GroupId: str
        :param _SdkAppId: 低代码平台应用ID
        :type SdkAppId: int
        :param _TeacherId: 默认绑定主讲老师ID
        :type TeacherId: str
        :param _GroupName: 待修改的群组名称
        :type GroupName: str
        """
        self._GroupId = None
        self._SdkAppId = None
        self._TeacherId = None
        self._GroupName = None

    @property
    def GroupId(self):
        r"""需要修改的群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        r"""低代码平台应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherId(self):
        r"""默认绑定主讲老师ID
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupName(self):
        r"""待修改的群组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._SdkAppId = params.get("SdkAppId")
        self._TeacherId = params.get("TeacherId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupResponse(AbstractModel):
    r"""ModifyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRoomRequest(AbstractModel):
    r"""ModifyRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        :param _SdkAppId: 低代码互动课堂的SdkAppId
        :type SdkAppId: int
        :param _StartTime: 预定的房间开始时间，unix时间戳（秒）。直播开始后不允许修改。
        :type StartTime: int
        :param _EndTime: 预定的房间结束时间，unix时间戳（秒）。直播开始后不允许修改。
        :type EndTime: int
        :param _TeacherId: 老师ID。直播开始后不允许修改。
        :type TeacherId: str
        :param _Name: 房间名称。
字符数不超过256
        :type Name: str
        :param _Resolution: 分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
直播开始后不允许修改。
        :type Resolution: int
        :param _MaxMicNumber: 设置房间/课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :type MaxMicNumber: int
        :param _AutoMic: 进入房间时是否自动连麦。可以有以下取值：
0 不自动连麦（默认值）
1 自动连麦
直播开始后不允许修改。
        :type AutoMic: int
        :param _AudioQuality: 高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
直播开始后不允许修改。
        :type AudioQuality: int
        :param _SubType: 房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
直播开始后不允许修改。
        :type SubType: str
        :param _DisableRecord: 禁止录制。可以有以下取值：
0 不禁止录制（默认值）
1 禁止录制
直播开始后不允许修改。
        :type DisableRecord: int
        :param _Assistants: 助教Id列表。直播开始后不允许修改。
        :type Assistants: list of str
        :param _GroupId: 房间绑定的群组ID。直播开始后不允许修改。
        :type GroupId: str
        :param _EnableDirectControl: 打开学生麦克风/摄像头的授权开关。直播开始后不允许修改。
        :type EnableDirectControl: int
        :param _InteractionMode: 开启专注模式。
0 收看全部角色音视频(默认)
1 只看老师和助教
        :type InteractionMode: int
        :param _VideoOrientation: 横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :type VideoOrientation: int
        :param _IsGradingRequiredPostClass: 开启课后评分。 0：不开启(默认)  1：开启
        :type IsGradingRequiredPostClass: int
        :param _RoomType: 房间类型: 0 小班课（默认值）; 1 大班课; 2 1V1 （预留参数、暂未开放)
注：大班课的布局(layout)只有三分屏
        :type RoomType: int
        :param _RecordLayout: 录制模板。仅可修改还未开始的房间。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :type RecordLayout: int
        :param _EndDelayTime: 拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :type EndDelayTime: int
        :param _LiveType: 直播方式：0 常规模式（默认）1 回放直播模式（伪直播）。 目前支持从回放直播模式（伪直播）改为常规模式，不支持从常规模式改为回放直播模式（伪直播）
        :type LiveType: int
        :param _RecordLiveUrl: 伪直播链接
        :type RecordLiveUrl: str
        :param _EnableAutoStart: 是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1的时候有效
        :type EnableAutoStart: int
        :param _RecordScene: 录制自定义场景，仅recordlayout=9的时候此参数有效,数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _WhiteBoardSnapshotMode: 板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :type WhiteBoardSnapshotMode: int
        :param _SubtitlesTranscription: 字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :type SubtitlesTranscription: int
        :param _Guests: 嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :type Guests: list of str
        :param _RecordMerge: 录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :type RecordMerge: int
        """
        self._RoomId = None
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._TeacherId = None
        self._Name = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._AutoMic = None
        self._AudioQuality = None
        self._SubType = None
        self._DisableRecord = None
        self._Assistants = None
        self._GroupId = None
        self._EnableDirectControl = None
        self._InteractionMode = None
        self._VideoOrientation = None
        self._IsGradingRequiredPostClass = None
        self._RoomType = None
        self._RecordLayout = None
        self._EndDelayTime = None
        self._LiveType = None
        self._RecordLiveUrl = None
        self._EnableAutoStart = None
        self._RecordScene = None
        self._RecordLang = None
        self._WhiteBoardSnapshotMode = None
        self._SubtitlesTranscription = None
        self._Guests = None
        self._RecordMerge = None

    @property
    def RoomId(self):
        r"""房间ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""预定的房间开始时间，unix时间戳（秒）。直播开始后不允许修改。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""预定的房间结束时间，unix时间戳（秒）。直播开始后不允许修改。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TeacherId(self):
        r"""老师ID。直播开始后不允许修改。
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def Name(self):
        r"""房间名称。
字符数不超过256
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Resolution(self):
        r"""分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
直播开始后不允许修改。
        :rtype: int
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        r"""设置房间/课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :rtype: int
        """
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def AutoMic(self):
        r"""进入房间时是否自动连麦。可以有以下取值：
0 不自动连麦（默认值）
1 自动连麦
直播开始后不允许修改。
        :rtype: int
        """
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def AudioQuality(self):
        r"""高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
直播开始后不允许修改。
        :rtype: int
        """
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def SubType(self):
        r"""房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
直播开始后不允许修改。
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def DisableRecord(self):
        r"""禁止录制。可以有以下取值：
0 不禁止录制（默认值）
1 禁止录制
直播开始后不允许修改。
        :rtype: int
        """
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        r"""助教Id列表。直播开始后不允许修改。
        :rtype: list of str
        """
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def GroupId(self):
        r"""房间绑定的群组ID。直播开始后不允许修改。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        r"""打开学生麦克风/摄像头的授权开关。直播开始后不允许修改。
        :rtype: int
        """
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        r"""开启专注模式。
0 收看全部角色音视频(默认)
1 只看老师和助教
        :rtype: int
        """
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        r"""横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :rtype: int
        """
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        r"""开启课后评分。 0：不开启(默认)  1：开启
        :rtype: int
        """
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        r"""房间类型: 0 小班课（默认值）; 1 大班课; 2 1V1 （预留参数、暂未开放)
注：大班课的布局(layout)只有三分屏
        :rtype: int
        """
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def RecordLayout(self):
        r"""录制模板。仅可修改还未开始的房间。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :rtype: int
        """
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def EndDelayTime(self):
        r"""拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :rtype: int
        """
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        r"""直播方式：0 常规模式（默认）1 回放直播模式（伪直播）。 目前支持从回放直播模式（伪直播）改为常规模式，不支持从常规模式改为回放直播模式（伪直播）
        :rtype: int
        """
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        r"""伪直播链接
        :rtype: str
        """
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        r"""是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1的时候有效
        :rtype: int
        """
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordScene(self):
        r"""录制自定义场景，仅recordlayout=9的时候此参数有效,数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。
        :rtype: str
        """
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        r"""录制自定义语言，仅recordlayout=9的时候此参数有效
        :rtype: str
        """
        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        self._RecordLang = RecordLang

    @property
    def WhiteBoardSnapshotMode(self):
        r"""板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :rtype: int
        """
        return self._WhiteBoardSnapshotMode

    @WhiteBoardSnapshotMode.setter
    def WhiteBoardSnapshotMode(self, WhiteBoardSnapshotMode):
        self._WhiteBoardSnapshotMode = WhiteBoardSnapshotMode

    @property
    def SubtitlesTranscription(self):
        r"""字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :rtype: int
        """
        return self._SubtitlesTranscription

    @SubtitlesTranscription.setter
    def SubtitlesTranscription(self, SubtitlesTranscription):
        self._SubtitlesTranscription = SubtitlesTranscription

    @property
    def Guests(self):
        r"""嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :rtype: list of str
        """
        return self._Guests

    @Guests.setter
    def Guests(self, Guests):
        self._Guests = Guests

    @property
    def RecordMerge(self):
        r"""录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :rtype: int
        """
        return self._RecordMerge

    @RecordMerge.setter
    def RecordMerge(self, RecordMerge):
        self._RecordMerge = RecordMerge


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TeacherId = params.get("TeacherId")
        self._Name = params.get("Name")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._AutoMic = params.get("AutoMic")
        self._AudioQuality = params.get("AudioQuality")
        self._SubType = params.get("SubType")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        self._InteractionMode = params.get("InteractionMode")
        self._VideoOrientation = params.get("VideoOrientation")
        self._IsGradingRequiredPostClass = params.get("IsGradingRequiredPostClass")
        self._RoomType = params.get("RoomType")
        self._RecordLayout = params.get("RecordLayout")
        self._EndDelayTime = params.get("EndDelayTime")
        self._LiveType = params.get("LiveType")
        self._RecordLiveUrl = params.get("RecordLiveUrl")
        self._EnableAutoStart = params.get("EnableAutoStart")
        self._RecordScene = params.get("RecordScene")
        self._RecordLang = params.get("RecordLang")
        self._WhiteBoardSnapshotMode = params.get("WhiteBoardSnapshotMode")
        self._SubtitlesTranscription = params.get("SubtitlesTranscription")
        self._Guests = params.get("Guests")
        self._RecordMerge = params.get("RecordMerge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomResponse(AbstractModel):
    r"""ModifyRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyUserProfileRequest(AbstractModel):
    r"""ModifyUserProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 待修改用户ID
        :type UserId: str
        :param _Nickname: 待修改的用户名。对应注册用户下“Name“字段，本次修改是对此内容进行修改。
        :type Nickname: str
        :param _Avatar: 待修改头像url
        :type Avatar: str
        """
        self._UserId = None
        self._Nickname = None
        self._Avatar = None

    @property
    def UserId(self):
        r"""待修改用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Nickname(self):
        r"""待修改的用户名。对应注册用户下“Name“字段，本次修改是对此内容进行修改。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Avatar(self):
        r"""待修改头像url
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Nickname = params.get("Nickname")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserProfileResponse(AbstractModel):
    r"""ModifyUserProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MsgBody(AbstractModel):
    r"""自定义消息结构

    """

    def __init__(self):
        r"""
        :param _MsgType: TIM 消息对象类型，目前支持的消息对象包括：
TIMTextElem（文本消息）
TIMFaceElem（表情消息）
TIMImageElem（图像消息）
TIMCustomElem（自定义消息）
        :type MsgType: str
        :param _TextMsgContent: 文本消息，当MsgType 为TIMTextElem（文本消息）必选。
        :type TextMsgContent: :class:`tencentcloud.lcic.v20220817.models.TextMsgContent`
        :param _FaceMsgContent: 表情消息，当MsgType 为TIMFaceElem（表情消息）必选。
        :type FaceMsgContent: :class:`tencentcloud.lcic.v20220817.models.FaceMsgContent`
        :param _ImageMsgContent: 图像消息，当MsgType为TIMImageElem（图像消息）必选。
        :type ImageMsgContent: :class:`tencentcloud.lcic.v20220817.models.ImageMsgContent`
        :param _CustomMsgContent: 自定义消息，TIMCustomElem（自定义消息）必选。
        :type CustomMsgContent: :class:`tencentcloud.lcic.v20220817.models.CustomMsgContent`
        """
        self._MsgType = None
        self._TextMsgContent = None
        self._FaceMsgContent = None
        self._ImageMsgContent = None
        self._CustomMsgContent = None

    @property
    def MsgType(self):
        r"""TIM 消息对象类型，目前支持的消息对象包括：
TIMTextElem（文本消息）
TIMFaceElem（表情消息）
TIMImageElem（图像消息）
TIMCustomElem（自定义消息）
        :rtype: str
        """
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def TextMsgContent(self):
        r"""文本消息，当MsgType 为TIMTextElem（文本消息）必选。
        :rtype: :class:`tencentcloud.lcic.v20220817.models.TextMsgContent`
        """
        return self._TextMsgContent

    @TextMsgContent.setter
    def TextMsgContent(self, TextMsgContent):
        self._TextMsgContent = TextMsgContent

    @property
    def FaceMsgContent(self):
        r"""表情消息，当MsgType 为TIMFaceElem（表情消息）必选。
        :rtype: :class:`tencentcloud.lcic.v20220817.models.FaceMsgContent`
        """
        return self._FaceMsgContent

    @FaceMsgContent.setter
    def FaceMsgContent(self, FaceMsgContent):
        self._FaceMsgContent = FaceMsgContent

    @property
    def ImageMsgContent(self):
        r"""图像消息，当MsgType为TIMImageElem（图像消息）必选。
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ImageMsgContent`
        """
        return self._ImageMsgContent

    @ImageMsgContent.setter
    def ImageMsgContent(self, ImageMsgContent):
        self._ImageMsgContent = ImageMsgContent

    @property
    def CustomMsgContent(self):
        r"""自定义消息，TIMCustomElem（自定义消息）必选。
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CustomMsgContent`
        """
        return self._CustomMsgContent

    @CustomMsgContent.setter
    def CustomMsgContent(self, CustomMsgContent):
        self._CustomMsgContent = CustomMsgContent


    def _deserialize(self, params):
        self._MsgType = params.get("MsgType")
        if params.get("TextMsgContent") is not None:
            self._TextMsgContent = TextMsgContent()
            self._TextMsgContent._deserialize(params.get("TextMsgContent"))
        if params.get("FaceMsgContent") is not None:
            self._FaceMsgContent = FaceMsgContent()
            self._FaceMsgContent._deserialize(params.get("FaceMsgContent"))
        if params.get("ImageMsgContent") is not None:
            self._ImageMsgContent = ImageMsgContent()
            self._ImageMsgContent._deserialize(params.get("ImageMsgContent"))
        if params.get("CustomMsgContent") is not None:
            self._CustomMsgContent = CustomMsgContent()
            self._CustomMsgContent._deserialize(params.get("CustomMsgContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MutedAccountList(AbstractModel):
    r"""禁言用户信息数组，内容包括被禁言的成员 ID，及其被禁言到的时间（使用 UTC 时间，即世界协调时间）

    """

    def __init__(self):
        r"""
        :param _MemberAccount: 用户 ID
        :type MemberAccount: str
        :param _MutedUntil: 禁言到的时间（使用 UTC 时间，即世界协调时间）
        :type MutedUntil: int
        """
        self._MemberAccount = None
        self._MutedUntil = None

    @property
    def MemberAccount(self):
        r"""用户 ID
        :rtype: str
        """
        return self._MemberAccount

    @MemberAccount.setter
    def MemberAccount(self, MemberAccount):
        self._MemberAccount = MemberAccount

    @property
    def MutedUntil(self):
        r"""禁言到的时间（使用 UTC 时间，即世界协调时间）
        :rtype: int
        """
        return self._MutedUntil

    @MutedUntil.setter
    def MutedUntil(self, MutedUntil):
        self._MutedUntil = MutedUntil


    def _deserialize(self, params):
        self._MemberAccount = params.get("MemberAccount")
        self._MutedUntil = params.get("MutedUntil")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuestionInfo(AbstractModel):
    r"""房间问答问题详情

    """

    def __init__(self):
        r"""
        :param _QuestionId: 问题ID
        :type QuestionId: str
        :param _QuestionContent: 问题内容
        :type QuestionContent: str
        :param _Duration: 倒计时答题设置的秒数（0 表示不计时）
        :type Duration: int
        :param _CorrectAnswer: 正确答案（按照位表示是否选择，如0x1表示选择A，0x11表示选择AB）
        :type CorrectAnswer: int
        :param _AnswerStats: 每个选项答题人数统计
        :type AnswerStats: list of AnswerStat
        """
        self._QuestionId = None
        self._QuestionContent = None
        self._Duration = None
        self._CorrectAnswer = None
        self._AnswerStats = None

    @property
    def QuestionId(self):
        r"""问题ID
        :rtype: str
        """
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def QuestionContent(self):
        r"""问题内容
        :rtype: str
        """
        return self._QuestionContent

    @QuestionContent.setter
    def QuestionContent(self, QuestionContent):
        self._QuestionContent = QuestionContent

    @property
    def Duration(self):
        r"""倒计时答题设置的秒数（0 表示不计时）
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def CorrectAnswer(self):
        r"""正确答案（按照位表示是否选择，如0x1表示选择A，0x11表示选择AB）
        :rtype: int
        """
        return self._CorrectAnswer

    @CorrectAnswer.setter
    def CorrectAnswer(self, CorrectAnswer):
        self._CorrectAnswer = CorrectAnswer

    @property
    def AnswerStats(self):
        r"""每个选项答题人数统计
        :rtype: list of AnswerStat
        """
        return self._AnswerStats

    @AnswerStats.setter
    def AnswerStats(self, AnswerStats):
        self._AnswerStats = AnswerStats


    def _deserialize(self, params):
        self._QuestionId = params.get("QuestionId")
        self._QuestionContent = params.get("QuestionContent")
        self._Duration = params.get("Duration")
        self._CorrectAnswer = params.get("CorrectAnswer")
        if params.get("AnswerStats") is not None:
            self._AnswerStats = []
            for item in params.get("AnswerStats"):
                obj = AnswerStat()
                obj._deserialize(item)
                self._AnswerStats.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterUserRequest(AbstractModel):
    r"""RegisterUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _Name: 对应用户昵称。对应修改用户信息下“nickname“字段，在修改用户信息时，可以对该字段进行调整，从而更改用户的昵称。
        :type Name: str
        :param _OriginId: 用户在客户系统的Id，需要在同一应用下唯一。入参为空时默认赋值为UserId。
        :type OriginId: str
        :param _Avatar: 用户头像。
        :type Avatar: str
        """
        self._SdkAppId = None
        self._Name = None
        self._OriginId = None
        self._Avatar = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        r"""对应用户昵称。对应修改用户信息下“nickname“字段，在修改用户信息时，可以对该字段进行调整，从而更改用户的昵称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginId(self):
        r"""用户在客户系统的Id，需要在同一应用下唯一。入参为空时默认赋值为UserId。
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Avatar(self):
        r"""用户头像。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Name = params.get("Name")
        self._OriginId = params.get("OriginId")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterUserResponse(AbstractModel):
    r"""RegisterUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id。
        :type UserId: str
        :param _Token: 登录/注册成功后返回登录态token。有效期7天。
        :type Token: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserId = None
        self._Token = None
        self._RequestId = None

    @property
    def UserId(self):
        r"""用户Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        r"""登录/注册成功后返回登录态token。有效期7天。
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class RoomInfo(AbstractModel):
    r"""批量创建房间的房间信息

    """

    def __init__(self):
        r"""
        :param _Name: 房间名称。
字符数不超过256
        :type Name: str
        :param _StartTime: 预定的房间开始时间，unix时间戳。
        :type StartTime: int
        :param _EndTime: 预定的房间结束时间，unix时间戳。
        :type EndTime: int
        :param _Resolution: 头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :type Resolution: int
        :param _MaxMicNumber: 设置房间/课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :type MaxMicNumber: int
        :param _SubType: 房间子类型，可以有以下取值： videodoc 文档+视频 video 纯视频
        :type SubType: str
        :param _TeacherId: 老师ID。通过[注册用户]接口获取的UserId。
        :type TeacherId: str
        :param _AutoMic: 进入课堂时是否自动连麦。可以有以下取值： 0 不自动连麦（需要手动申请上麦，默认值） 1 自动连麦
        :type AutoMic: int
        :param _TurnOffMic: 释放音视频权限后是否自动取消连麦。可以有以下取值： 0 自动取消连麦（默认值） 1 保持连麦状态
        :type TurnOffMic: int
        :param _AudioQuality: 高音质模式。可以有以下取值： 0 不开启高音质（默认值） 1 开启高音质
        :type AudioQuality: int
        :param _DisableRecord: 上课后是否禁止自动录制。可以有以下取值： 0 不禁止录制（自动开启录制，默认值） 1 禁止录制 注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :type DisableRecord: int
        :param _Assistants: 助教Id列表。通过[注册用户]接口获取的UserId。
        :type Assistants: list of str
        :param _RTCAudienceNumber: rtc人数。
        :type RTCAudienceNumber: int
        :param _AudienceType: 观看类型。
        :type AudienceType: int
        :param _RecordLayout: 录制布局。
        :type RecordLayout: int
        :param _GroupId: 房间绑定的群组ID
        :type GroupId: str
        :param _EnableDirectControl: 打开学生麦克风/摄像头的授权开关
        :type EnableDirectControl: int
        :param _InteractionMode: 开启专注模式。 0 收看全部角色音视频(默认) 1 只看老师和助教
        :type InteractionMode: int
        :param _VideoOrientation: 横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :type VideoOrientation: int
        :param _IsGradingRequiredPostClass: 开启课后评分。 0：不开启(默认)  1：开启
        :type IsGradingRequiredPostClass: int
        :param _RoomType: 课堂类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (预留参数，暂未开放); 3 圆桌会议 注：大班课的布局(layout)只有三分屏
        :type RoomType: int
        :param _EndDelayTime: 拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :type EndDelayTime: int
        :param _LiveType: 直播类型：0 常规（默认）1 伪直播 2 RTMP推流直播
        :type LiveType: int
        :param _RecordLiveUrl: 伪直播回放链接
        :type RecordLiveUrl: str
        :param _EnableAutoStart: 是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1或2的时候有效
        :type EnableAutoStart: int
        :param _RecordBackground: 录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :type RecordBackground: str
        :param _RecordScene: 录制自定义场景。注意：仅recordlayout=9的时候此参数有效。需注意各类参数配置正确能够生效。不然会造成录制失败，失败后无法补救。数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。自定义场景参数的含义。如下：     scene：自定义js/css对应的场景值。如scene=recordScene，会加载 recordScene 场景对应的 js/css，这样就可以自定义录制页面的元素。     lng：录制页面对应的语种。如lng=en，则录制界面为en。（枚举值：en,zh，zh-TW，jp，ar，kr，vi）     customToken：录制页面中涉及客户自己的服务需要鉴权时进行配置。一般情况下，无需配置。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _RecordStream: 录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :type RecordStream: int
        :param _WhiteBoardSnapshotMode: 板书截图生成类型。0 不生成板书（默认）；1 全量模式；2 单页去重模式
        :type WhiteBoardSnapshotMode: int
        :param _SubtitlesTranscription: 字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :type SubtitlesTranscription: int
        :param _Guests: 嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :type Guests: list of str
        :param _RecordMerge: 录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :type RecordMerge: int
        """
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._Resolution = None
        self._MaxMicNumber = None
        self._SubType = None
        self._TeacherId = None
        self._AutoMic = None
        self._TurnOffMic = None
        self._AudioQuality = None
        self._DisableRecord = None
        self._Assistants = None
        self._RTCAudienceNumber = None
        self._AudienceType = None
        self._RecordLayout = None
        self._GroupId = None
        self._EnableDirectControl = None
        self._InteractionMode = None
        self._VideoOrientation = None
        self._IsGradingRequiredPostClass = None
        self._RoomType = None
        self._EndDelayTime = None
        self._LiveType = None
        self._RecordLiveUrl = None
        self._EnableAutoStart = None
        self._RecordBackground = None
        self._RecordScene = None
        self._RecordLang = None
        self._RecordStream = None
        self._WhiteBoardSnapshotMode = None
        self._SubtitlesTranscription = None
        self._Guests = None
        self._RecordMerge = None

    @property
    def Name(self):
        r"""房间名称。
字符数不超过256
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        r"""预定的房间开始时间，unix时间戳。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""预定的房间结束时间，unix时间戳。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Resolution(self):
        r"""头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :rtype: int
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        r"""设置房间/课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :rtype: int
        """
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def SubType(self):
        r"""房间子类型，可以有以下取值： videodoc 文档+视频 video 纯视频
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TeacherId(self):
        r"""老师ID。通过[注册用户]接口获取的UserId。
        :rtype: str
        """
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def AutoMic(self):
        r"""进入课堂时是否自动连麦。可以有以下取值： 0 不自动连麦（需要手动申请上麦，默认值） 1 自动连麦
        :rtype: int
        """
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def TurnOffMic(self):
        r"""释放音视频权限后是否自动取消连麦。可以有以下取值： 0 自动取消连麦（默认值） 1 保持连麦状态
        :rtype: int
        """
        return self._TurnOffMic

    @TurnOffMic.setter
    def TurnOffMic(self, TurnOffMic):
        self._TurnOffMic = TurnOffMic

    @property
    def AudioQuality(self):
        r"""高音质模式。可以有以下取值： 0 不开启高音质（默认值） 1 开启高音质
        :rtype: int
        """
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def DisableRecord(self):
        r"""上课后是否禁止自动录制。可以有以下取值： 0 不禁止录制（自动开启录制，默认值） 1 禁止录制 注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :rtype: int
        """
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        r"""助教Id列表。通过[注册用户]接口获取的UserId。
        :rtype: list of str
        """
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RTCAudienceNumber(self):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        r"""rtc人数。
        :rtype: int
        """
        return self._RTCAudienceNumber

    @RTCAudienceNumber.setter
    def RTCAudienceNumber(self, RTCAudienceNumber):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        self._RTCAudienceNumber = RTCAudienceNumber

    @property
    def AudienceType(self):
        r"""观看类型。
        :rtype: int
        """
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def RecordLayout(self):
        r"""录制布局。
        :rtype: int
        """
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def GroupId(self):
        r"""房间绑定的群组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        r"""打开学生麦克风/摄像头的授权开关
        :rtype: int
        """
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        r"""开启专注模式。 0 收看全部角色音视频(默认) 1 只看老师和助教
        :rtype: int
        """
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        r"""横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :rtype: int
        """
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        r"""开启课后评分。 0：不开启(默认)  1：开启
        :rtype: int
        """
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        r"""课堂类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (预留参数，暂未开放); 3 圆桌会议 注：大班课的布局(layout)只有三分屏
        :rtype: int
        """
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def EndDelayTime(self):
        r"""拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :rtype: int
        """
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        r"""直播类型：0 常规（默认）1 伪直播 2 RTMP推流直播
        :rtype: int
        """
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        r"""伪直播回放链接
        :rtype: str
        """
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        r"""是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1或2的时候有效
        :rtype: int
        """
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        r"""录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :rtype: str
        """
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RecordScene(self):
        r"""录制自定义场景。注意：仅recordlayout=9的时候此参数有效。需注意各类参数配置正确能够生效。不然会造成录制失败，失败后无法补救。数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。自定义场景参数的含义。如下：     scene：自定义js/css对应的场景值。如scene=recordScene，会加载 recordScene 场景对应的 js/css，这样就可以自定义录制页面的元素。     lng：录制页面对应的语种。如lng=en，则录制界面为en。（枚举值：en,zh，zh-TW，jp，ar，kr，vi）     customToken：录制页面中涉及客户自己的服务需要鉴权时进行配置。一般情况下，无需配置。
        :rtype: str
        """
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        r"""录制自定义语言，仅recordlayout=9的时候此参数有效
        :rtype: str
        """
        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        self._RecordLang = RecordLang

    @property
    def RecordStream(self):
        r"""录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :rtype: int
        """
        return self._RecordStream

    @RecordStream.setter
    def RecordStream(self, RecordStream):
        self._RecordStream = RecordStream

    @property
    def WhiteBoardSnapshotMode(self):
        r"""板书截图生成类型。0 不生成板书（默认）；1 全量模式；2 单页去重模式
        :rtype: int
        """
        return self._WhiteBoardSnapshotMode

    @WhiteBoardSnapshotMode.setter
    def WhiteBoardSnapshotMode(self, WhiteBoardSnapshotMode):
        self._WhiteBoardSnapshotMode = WhiteBoardSnapshotMode

    @property
    def SubtitlesTranscription(self):
        r"""字幕转写功能开关。可以有以下取值：
0 不开启字幕转写功能（默认值）
1 自动转写模式：上课自动开启，下课自动停止
2 手动转写模式：支持老师或者助教通过客户端API手动开启/关闭字幕转写
设置0和1时客户端均不展示手动开关，设置2时老师或者助教端展示字幕转写开关
        :rtype: int
        """
        return self._SubtitlesTranscription

    @SubtitlesTranscription.setter
    def SubtitlesTranscription(self, SubtitlesTranscription):
        self._SubtitlesTranscription = SubtitlesTranscription

    @property
    def Guests(self):
        r"""嘉宾Id列表。当圆桌会议模式（RoomType==3）时生效
        :rtype: list of str
        """
        return self._Guests

    @Guests.setter
    def Guests(self, Guests):
        self._Guests = Guests

    @property
    def RecordMerge(self):
        r"""录制文件合并开关。0 关闭 1 开启 注：只有在一节课多次启用手动录制时，此功能才有效
        :rtype: int
        """
        return self._RecordMerge

    @RecordMerge.setter
    def RecordMerge(self, RecordMerge):
        self._RecordMerge = RecordMerge


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Resolution = params.get("Resolution")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._SubType = params.get("SubType")
        self._TeacherId = params.get("TeacherId")
        self._AutoMic = params.get("AutoMic")
        self._TurnOffMic = params.get("TurnOffMic")
        self._AudioQuality = params.get("AudioQuality")
        self._DisableRecord = params.get("DisableRecord")
        self._Assistants = params.get("Assistants")
        self._RTCAudienceNumber = params.get("RTCAudienceNumber")
        self._AudienceType = params.get("AudienceType")
        self._RecordLayout = params.get("RecordLayout")
        self._GroupId = params.get("GroupId")
        self._EnableDirectControl = params.get("EnableDirectControl")
        self._InteractionMode = params.get("InteractionMode")
        self._VideoOrientation = params.get("VideoOrientation")
        self._IsGradingRequiredPostClass = params.get("IsGradingRequiredPostClass")
        self._RoomType = params.get("RoomType")
        self._EndDelayTime = params.get("EndDelayTime")
        self._LiveType = params.get("LiveType")
        self._RecordLiveUrl = params.get("RecordLiveUrl")
        self._EnableAutoStart = params.get("EnableAutoStart")
        self._RecordBackground = params.get("RecordBackground")
        self._RecordScene = params.get("RecordScene")
        self._RecordLang = params.get("RecordLang")
        self._RecordStream = params.get("RecordStream")
        self._WhiteBoardSnapshotMode = params.get("WhiteBoardSnapshotMode")
        self._SubtitlesTranscription = params.get("SubtitlesTranscription")
        self._Guests = params.get("Guests")
        self._RecordMerge = params.get("RecordMerge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomItem(AbstractModel):
    r"""房间列表

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _RoomId: 房间ID
        :type RoomId: int
        :param _Status: 房间状态。0 未开始 ；1进行中  ；2 已结束；3已过期
        :type Status: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _RealStartTime: 实际开始时间
        :type RealStartTime: int
        :param _RealEndTime: 实际结束时间
        :type RealEndTime: int
        :param _Resolution: 头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :type Resolution: int
        :param _MaxRTCMember: 最大允许连麦人数。已废弃，使用字段 MaxMicNumber
        :type MaxRTCMember: int
        :param _ReplayUrl: 房间录制地址。已废弃，使用新字段 RecordUrl
        :type ReplayUrl: str
        :param _RecordUrl: 录制地址（协议为https)。仅在房间结束后存在。
        :type RecordUrl: str
        :param _MaxMicNumber: 课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :type MaxMicNumber: int
        :param _EnableDirectControl: 打开学生麦克风/摄像头的授权开关 
        :type EnableDirectControl: int
        :param _InteractionMode: 开启专注模式。 0 收看全部角色音视频(默认) 1 只看老师和助教
        :type InteractionMode: int
        :param _VideoOrientation: 横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :type VideoOrientation: int
        :param _IsGradingRequiredPostClass: 开启课后评分。 0：不开启(默认)  1：开启
        :type IsGradingRequiredPostClass: int
        :param _RoomType: 房间类型。0:小班课（默认值）；1:大班课；2:1V1（后续扩展）
注：大班课的布局(layout)只有三分屏
        :type RoomType: int
        :param _EndDelayTime: 拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :type EndDelayTime: int
        :param _LiveType: 直播类型：0 常规（默认）1 伪直播
        :type LiveType: int
        :param _RecordLiveUrl: 伪直播回放链接	
        :type RecordLiveUrl: str
        :param _EnableAutoStart: 是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1的时候有效	
        :type EnableAutoStart: int
        :param _RecordBackground: 录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :type RecordBackground: str
        :param _RecordScene: 录制自定义场景，仅recordlayout=9的时候此参数有效,数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _WhiteBoardSnapshotMode: 板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :type WhiteBoardSnapshotMode: int
        :param _SubtitlesTranscription: 字幕转写功能开关：0关闭，1开启，默认关闭
        :type SubtitlesTranscription: int
        """
        self._Name = None
        self._RoomId = None
        self._Status = None
        self._StartTime = None
        self._EndTime = None
        self._RealStartTime = None
        self._RealEndTime = None
        self._Resolution = None
        self._MaxRTCMember = None
        self._ReplayUrl = None
        self._RecordUrl = None
        self._MaxMicNumber = None
        self._EnableDirectControl = None
        self._InteractionMode = None
        self._VideoOrientation = None
        self._IsGradingRequiredPostClass = None
        self._RoomType = None
        self._EndDelayTime = None
        self._LiveType = None
        self._RecordLiveUrl = None
        self._EnableAutoStart = None
        self._RecordBackground = None
        self._RecordScene = None
        self._RecordLang = None
        self._WhiteBoardSnapshotMode = None
        self._SubtitlesTranscription = None

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Status(self):
        r"""房间状态。0 未开始 ；1进行中  ；2 已结束；3已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RealStartTime(self):
        r"""实际开始时间
        :rtype: int
        """
        return self._RealStartTime

    @RealStartTime.setter
    def RealStartTime(self, RealStartTime):
        self._RealStartTime = RealStartTime

    @property
    def RealEndTime(self):
        r"""实际结束时间
        :rtype: int
        """
        return self._RealEndTime

    @RealEndTime.setter
    def RealEndTime(self, RealEndTime):
        self._RealEndTime = RealEndTime

    @property
    def Resolution(self):
        r"""头像区域，摄像头视频画面的分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :rtype: int
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxRTCMember(self):
        r"""最大允许连麦人数。已废弃，使用字段 MaxMicNumber
        :rtype: int
        """
        return self._MaxRTCMember

    @MaxRTCMember.setter
    def MaxRTCMember(self, MaxRTCMember):
        self._MaxRTCMember = MaxRTCMember

    @property
    def ReplayUrl(self):
        r"""房间录制地址。已废弃，使用新字段 RecordUrl
        :rtype: str
        """
        return self._ReplayUrl

    @ReplayUrl.setter
    def ReplayUrl(self, ReplayUrl):
        self._ReplayUrl = ReplayUrl

    @property
    def RecordUrl(self):
        r"""录制地址（协议为https)。仅在房间结束后存在。
        :rtype: str
        """
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def MaxMicNumber(self):
        r"""课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :rtype: int
        """
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def EnableDirectControl(self):
        r"""打开学生麦克风/摄像头的授权开关 
        :rtype: int
        """
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        r"""开启专注模式。 0 收看全部角色音视频(默认) 1 只看老师和助教
        :rtype: int
        """
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        r"""横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :rtype: int
        """
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        r"""开启课后评分。 0：不开启(默认)  1：开启
        :rtype: int
        """
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        r"""房间类型。0:小班课（默认值）；1:大班课；2:1V1（后续扩展）
注：大班课的布局(layout)只有三分屏
        :rtype: int
        """
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def EndDelayTime(self):
        r"""拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :rtype: int
        """
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        r"""直播类型：0 常规（默认）1 伪直播
        :rtype: int
        """
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        r"""伪直播回放链接	
        :rtype: str
        """
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        r"""是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1的时候有效	
        :rtype: int
        """
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        r"""录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :rtype: str
        """
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RecordScene(self):
        r"""录制自定义场景，仅recordlayout=9的时候此参数有效,数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。
        :rtype: str
        """
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        r"""录制自定义语言，仅recordlayout=9的时候此参数有效
        :rtype: str
        """
        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        self._RecordLang = RecordLang

    @property
    def WhiteBoardSnapshotMode(self):
        r"""板书截图生成类型。0 不生成板书；1 全量模式；2 单页去重模式
        :rtype: int
        """
        return self._WhiteBoardSnapshotMode

    @WhiteBoardSnapshotMode.setter
    def WhiteBoardSnapshotMode(self, WhiteBoardSnapshotMode):
        self._WhiteBoardSnapshotMode = WhiteBoardSnapshotMode

    @property
    def SubtitlesTranscription(self):
        r"""字幕转写功能开关：0关闭，1开启，默认关闭
        :rtype: int
        """
        return self._SubtitlesTranscription

    @SubtitlesTranscription.setter
    def SubtitlesTranscription(self, SubtitlesTranscription):
        self._SubtitlesTranscription = SubtitlesTranscription


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RoomId = params.get("RoomId")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RealStartTime = params.get("RealStartTime")
        self._RealEndTime = params.get("RealEndTime")
        self._Resolution = params.get("Resolution")
        self._MaxRTCMember = params.get("MaxRTCMember")
        self._ReplayUrl = params.get("ReplayUrl")
        self._RecordUrl = params.get("RecordUrl")
        self._MaxMicNumber = params.get("MaxMicNumber")
        self._EnableDirectControl = params.get("EnableDirectControl")
        self._InteractionMode = params.get("InteractionMode")
        self._VideoOrientation = params.get("VideoOrientation")
        self._IsGradingRequiredPostClass = params.get("IsGradingRequiredPostClass")
        self._RoomType = params.get("RoomType")
        self._EndDelayTime = params.get("EndDelayTime")
        self._LiveType = params.get("LiveType")
        self._RecordLiveUrl = params.get("RecordLiveUrl")
        self._EnableAutoStart = params.get("EnableAutoStart")
        self._RecordBackground = params.get("RecordBackground")
        self._RecordScene = params.get("RecordScene")
        self._RecordLang = params.get("RecordLang")
        self._WhiteBoardSnapshotMode = params.get("WhiteBoardSnapshotMode")
        self._SubtitlesTranscription = params.get("SubtitlesTranscription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneItem(AbstractModel):
    r"""场景配置

    """

    def __init__(self):
        r"""
        :param _Scene: 场景名称
        :type Scene: str
        :param _LogoUrl: logo地址
        :type LogoUrl: str
        :param _HomeUrl: 主页地址
        :type HomeUrl: str
        :param _JSUrl: 自定义的js
        :type JSUrl: str
        :param _CSSUrl: 自定义的css
        :type CSSUrl: str
        """
        self._Scene = None
        self._LogoUrl = None
        self._HomeUrl = None
        self._JSUrl = None
        self._CSSUrl = None

    @property
    def Scene(self):
        r"""场景名称
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LogoUrl(self):
        r"""logo地址
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def HomeUrl(self):
        r"""主页地址
        :rtype: str
        """
        return self._HomeUrl

    @HomeUrl.setter
    def HomeUrl(self, HomeUrl):
        self._HomeUrl = HomeUrl

    @property
    def JSUrl(self):
        r"""自定义的js
        :rtype: str
        """
        return self._JSUrl

    @JSUrl.setter
    def JSUrl(self, JSUrl):
        self._JSUrl = JSUrl

    @property
    def CSSUrl(self):
        r"""自定义的css
        :rtype: str
        """
        return self._CSSUrl

    @CSSUrl.setter
    def CSSUrl(self, CSSUrl):
        self._CSSUrl = CSSUrl


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._LogoUrl = params.get("LogoUrl")
        self._HomeUrl = params.get("HomeUrl")
        self._JSUrl = params.get("JSUrl")
        self._CSSUrl = params.get("CSSUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendRoomNormalMessageRequest(AbstractModel):
    r"""SendRoomNormalMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 房间ID。
        :type RoomId: int
        :param _FromAccount: 管理员指定消息发送方账号（若需设置 FromAccount 信息，则该参数取值不能为空）
        :type FromAccount: str
        :param _MsgBody: 自定义消息
        :type MsgBody: list of MsgBody
        :param _CloudCustomData: 消息自定义数据（云端保存，会发送到对端，程序卸载重装后还能拉取到）。
        :type CloudCustomData: str
        :param _NickName: 昵称，当FromAccount没有在房间中，需要填写NickName，当FromAccount在房间中，填写NickName无意义
        :type NickName: str
        :param _Priority: 消息的优先级，默认优先级 Normal。
可以指定3种优先级，从高到低依次为 High、Normal 和 Low，区分大小写。
        :type Priority: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._FromAccount = None
        self._MsgBody = None
        self._CloudCustomData = None
        self._NickName = None
        self._Priority = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def FromAccount(self):
        r"""管理员指定消息发送方账号（若需设置 FromAccount 信息，则该参数取值不能为空）
        :rtype: str
        """
        return self._FromAccount

    @FromAccount.setter
    def FromAccount(self, FromAccount):
        self._FromAccount = FromAccount

    @property
    def MsgBody(self):
        r"""自定义消息
        :rtype: list of MsgBody
        """
        return self._MsgBody

    @MsgBody.setter
    def MsgBody(self, MsgBody):
        self._MsgBody = MsgBody

    @property
    def CloudCustomData(self):
        r"""消息自定义数据（云端保存，会发送到对端，程序卸载重装后还能拉取到）。
        :rtype: str
        """
        return self._CloudCustomData

    @CloudCustomData.setter
    def CloudCustomData(self, CloudCustomData):
        self._CloudCustomData = CloudCustomData

    @property
    def NickName(self):
        r"""昵称，当FromAccount没有在房间中，需要填写NickName，当FromAccount在房间中，填写NickName无意义
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Priority(self):
        r"""消息的优先级，默认优先级 Normal。
可以指定3种优先级，从高到低依次为 High、Normal 和 Low，区分大小写。
        :rtype: str
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._FromAccount = params.get("FromAccount")
        if params.get("MsgBody") is not None:
            self._MsgBody = []
            for item in params.get("MsgBody"):
                obj = MsgBody()
                obj._deserialize(item)
                self._MsgBody.append(obj)
        self._CloudCustomData = params.get("CloudCustomData")
        self._NickName = params.get("NickName")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendRoomNormalMessageResponse(AbstractModel):
    r"""SendRoomNormalMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SendRoomNotificationMessageRequest(AbstractModel):
    r"""SendRoomNotificationMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 房间ID。

        :type RoomId: int
        :param _MsgContent: 消息。
        :type MsgContent: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._MsgContent = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间ID。

        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def MsgContent(self):
        r"""消息。
        :rtype: str
        """
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._MsgContent = params.get("MsgContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendRoomNotificationMessageResponse(AbstractModel):
    r"""SendRoomNotificationMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetAppCustomContentRequest(AbstractModel):
    r"""SetAppCustomContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CustomContent: 自定义内容。
        :type CustomContent: list of AppCustomContent
        :param _SdkAppId: 应用ID。
        :type SdkAppId: int
        """
        self._CustomContent = None
        self._SdkAppId = None

    @property
    def CustomContent(self):
        r"""自定义内容。
        :rtype: list of AppCustomContent
        """
        return self._CustomContent

    @CustomContent.setter
    def CustomContent(self, CustomContent):
        self._CustomContent = CustomContent

    @property
    def SdkAppId(self):
        r"""应用ID。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        if params.get("CustomContent") is not None:
            self._CustomContent = []
            for item in params.get("CustomContent"):
                obj = AppCustomContent()
                obj._deserialize(item)
                self._CustomContent.append(obj)
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAppCustomContentResponse(AbstractModel):
    r"""SetAppCustomContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetMarqueeRequest(AbstractModel):
    r"""SetMarquee请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 学校ID
        :type SdkAppId: int
        :param _RoomId: 房间号
        :type RoomId: int
        :param _MarqueeType:  跑马灯类型：1为固定值，2为用户昵称，3为固定值+用户昵称，4为用户ID，5为originId+固定值，6为用户昵称（originId）
        :type MarqueeType: int
        :param _DisplayMode: 显示方式：1为滚动，2为闪烁
        :type DisplayMode: int
        :param _Content: 固定值内容（当MarqueeType=1或5，则展示固定值内容）
        :type Content: str
        :param _FontSize: 字体大小（数字，像素单位，范围：10到24）。
        :type FontSize: int
        :param _FontWeight: 字体粗细：1为粗体，0为细体
        :type FontWeight: int
        :param _FontColor: 字体颜色（十六进制颜色值，例如：#00FF00（绿色））
        :type FontColor: str
        :param _FontOpacity: 字体透明度（数字，范围 0.0 到 1.0）
        :type FontOpacity: float
        :param _BackgroundColor: 背景颜色（十六进制颜色值，例如：#FFFF00（黄色））
        :type BackgroundColor: str
        :param _BackgroundOpacity: 背景透明度（数字，范围 0.0 到 1.0）
        :type BackgroundOpacity: float
        :param _Duration: 跑马灯文字移动/闪烁指定像素所需时间，范围：1-10；数值越小，跑马灯滚动/闪烁速度越快
        :type Duration: int
        :param _MarqueeCount: 跑马灯个数：目前仅支持1或2, 对应显示单排或双排
        :type MarqueeCount: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._MarqueeType = None
        self._DisplayMode = None
        self._Content = None
        self._FontSize = None
        self._FontWeight = None
        self._FontColor = None
        self._FontOpacity = None
        self._BackgroundColor = None
        self._BackgroundOpacity = None
        self._Duration = None
        self._MarqueeCount = None

    @property
    def SdkAppId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间号
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def MarqueeType(self):
        r""" 跑马灯类型：1为固定值，2为用户昵称，3为固定值+用户昵称，4为用户ID，5为originId+固定值，6为用户昵称（originId）
        :rtype: int
        """
        return self._MarqueeType

    @MarqueeType.setter
    def MarqueeType(self, MarqueeType):
        self._MarqueeType = MarqueeType

    @property
    def DisplayMode(self):
        r"""显示方式：1为滚动，2为闪烁
        :rtype: int
        """
        return self._DisplayMode

    @DisplayMode.setter
    def DisplayMode(self, DisplayMode):
        self._DisplayMode = DisplayMode

    @property
    def Content(self):
        r"""固定值内容（当MarqueeType=1或5，则展示固定值内容）
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FontSize(self):
        r"""字体大小（数字，像素单位，范围：10到24）。
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontWeight(self):
        r"""字体粗细：1为粗体，0为细体
        :rtype: int
        """
        return self._FontWeight

    @FontWeight.setter
    def FontWeight(self, FontWeight):
        self._FontWeight = FontWeight

    @property
    def FontColor(self):
        r"""字体颜色（十六进制颜色值，例如：#00FF00（绿色））
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def FontOpacity(self):
        r"""字体透明度（数字，范围 0.0 到 1.0）
        :rtype: float
        """
        return self._FontOpacity

    @FontOpacity.setter
    def FontOpacity(self, FontOpacity):
        self._FontOpacity = FontOpacity

    @property
    def BackgroundColor(self):
        r"""背景颜色（十六进制颜色值，例如：#FFFF00（黄色））
        :rtype: str
        """
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor

    @property
    def BackgroundOpacity(self):
        r"""背景透明度（数字，范围 0.0 到 1.0）
        :rtype: float
        """
        return self._BackgroundOpacity

    @BackgroundOpacity.setter
    def BackgroundOpacity(self, BackgroundOpacity):
        self._BackgroundOpacity = BackgroundOpacity

    @property
    def Duration(self):
        r"""跑马灯文字移动/闪烁指定像素所需时间，范围：1-10；数值越小，跑马灯滚动/闪烁速度越快
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def MarqueeCount(self):
        r"""跑马灯个数：目前仅支持1或2, 对应显示单排或双排
        :rtype: int
        """
        return self._MarqueeCount

    @MarqueeCount.setter
    def MarqueeCount(self, MarqueeCount):
        self._MarqueeCount = MarqueeCount


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._MarqueeType = params.get("MarqueeType")
        self._DisplayMode = params.get("DisplayMode")
        self._Content = params.get("Content")
        self._FontSize = params.get("FontSize")
        self._FontWeight = params.get("FontWeight")
        self._FontColor = params.get("FontColor")
        self._FontOpacity = params.get("FontOpacity")
        self._BackgroundColor = params.get("BackgroundColor")
        self._BackgroundOpacity = params.get("BackgroundOpacity")
        self._Duration = params.get("Duration")
        self._MarqueeCount = params.get("MarqueeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetMarqueeResponse(AbstractModel):
    r"""SetMarquee返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetWatermarkRequest(AbstractModel):
    r"""SetWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        :param _TeacherUrl: 老师视频区域的水印参数地址，设置为空字符串表示删除
        :type TeacherUrl: str
        :param _BoardUrl: 白板视频区域的水印参数地址，设置为空字符串表示删除
        :type BoardUrl: str
        :param _VideoUrl: 视频默认图片（在没有视频流的时候显示），设置为空字符串表示删除
        :type VideoUrl: str
        :param _BoardW: 白板区域水印的宽度，取值:0-100，默认为0，表示区域X方向的百分比
        :type BoardW: float
        :param _BoardH: 白板区域水印的高度，取值:0-100，默认为0, 表示区域Y方向的百分比
        :type BoardH: float
        :param _BoardX: 白板区域水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type BoardX: float
        :param _BoardY: 白板区域水印Y偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type BoardY: float
        :param _TeacherW: 老师视频区域水印的宽度，取值:0-100，默认为0，表示区域X方向的百分比
        :type TeacherW: float
        :param _TeacherH: 老师视频区域水印的高度，取值:0-100，默认为0, 表示区域Y方向的百分比
        :type TeacherH: float
        :param _TeacherX: 老师视频区域水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type TeacherX: float
        :param _TeacherY: 老师视频区域水印Y偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :type TeacherY: float
        :param _Text: 文字水印内容，设置为空字符串表示删除
        :type Text: str
        :param _TextColor: 文字水印颜色
        :type TextColor: str
        """
        self._SdkAppId = None
        self._TeacherUrl = None
        self._BoardUrl = None
        self._VideoUrl = None
        self._BoardW = None
        self._BoardH = None
        self._BoardX = None
        self._BoardY = None
        self._TeacherW = None
        self._TeacherH = None
        self._TeacherX = None
        self._TeacherY = None
        self._Text = None
        self._TextColor = None

    @property
    def SdkAppId(self):
        r"""低代码互动课堂的SdkAppId。

        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherUrl(self):
        r"""老师视频区域的水印参数地址，设置为空字符串表示删除
        :rtype: str
        """
        return self._TeacherUrl

    @TeacherUrl.setter
    def TeacherUrl(self, TeacherUrl):
        self._TeacherUrl = TeacherUrl

    @property
    def BoardUrl(self):
        r"""白板视频区域的水印参数地址，设置为空字符串表示删除
        :rtype: str
        """
        return self._BoardUrl

    @BoardUrl.setter
    def BoardUrl(self, BoardUrl):
        self._BoardUrl = BoardUrl

    @property
    def VideoUrl(self):
        r"""视频默认图片（在没有视频流的时候显示），设置为空字符串表示删除
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def BoardW(self):
        r"""白板区域水印的宽度，取值:0-100，默认为0，表示区域X方向的百分比
        :rtype: float
        """
        return self._BoardW

    @BoardW.setter
    def BoardW(self, BoardW):
        self._BoardW = BoardW

    @property
    def BoardH(self):
        r"""白板区域水印的高度，取值:0-100，默认为0, 表示区域Y方向的百分比
        :rtype: float
        """
        return self._BoardH

    @BoardH.setter
    def BoardH(self, BoardH):
        self._BoardH = BoardH

    @property
    def BoardX(self):
        r"""白板区域水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :rtype: float
        """
        return self._BoardX

    @BoardX.setter
    def BoardX(self, BoardX):
        self._BoardX = BoardX

    @property
    def BoardY(self):
        r"""白板区域水印Y偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :rtype: float
        """
        return self._BoardY

    @BoardY.setter
    def BoardY(self, BoardY):
        self._BoardY = BoardY

    @property
    def TeacherW(self):
        r"""老师视频区域水印的宽度，取值:0-100，默认为0，表示区域X方向的百分比
        :rtype: float
        """
        return self._TeacherW

    @TeacherW.setter
    def TeacherW(self, TeacherW):
        self._TeacherW = TeacherW

    @property
    def TeacherH(self):
        r"""老师视频区域水印的高度，取值:0-100，默认为0, 表示区域Y方向的百分比
        :rtype: float
        """
        return self._TeacherH

    @TeacherH.setter
    def TeacherH(self, TeacherH):
        self._TeacherH = TeacherH

    @property
    def TeacherX(self):
        r"""老师视频区域水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :rtype: float
        """
        return self._TeacherX

    @TeacherX.setter
    def TeacherX(self, TeacherX):
        self._TeacherX = TeacherX

    @property
    def TeacherY(self):
        r"""老师视频区域水印Y偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间
        :rtype: float
        """
        return self._TeacherY

    @TeacherY.setter
    def TeacherY(self, TeacherY):
        self._TeacherY = TeacherY

    @property
    def Text(self):
        r"""文字水印内容，设置为空字符串表示删除
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TextColor(self):
        r"""文字水印颜色
        :rtype: str
        """
        return self._TextColor

    @TextColor.setter
    def TextColor(self, TextColor):
        self._TextColor = TextColor


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TeacherUrl = params.get("TeacherUrl")
        self._BoardUrl = params.get("BoardUrl")
        self._VideoUrl = params.get("VideoUrl")
        self._BoardW = params.get("BoardW")
        self._BoardH = params.get("BoardH")
        self._BoardX = params.get("BoardX")
        self._BoardY = params.get("BoardY")
        self._TeacherW = params.get("TeacherW")
        self._TeacherH = params.get("TeacherH")
        self._TeacherX = params.get("TeacherX")
        self._TeacherY = params.get("TeacherY")
        self._Text = params.get("Text")
        self._TextColor = params.get("TextColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetWatermarkResponse(AbstractModel):
    r"""SetWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SingleStreamInfo(AbstractModel):
    r"""录制流信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _StopTime: 结束时间
        :type StopTime: int
        :param _Duration: 总时长
        :type Duration: int
        :param _FileFormat: 文件格式
        :type FileFormat: str
        :param _RecordUrl: 流url
        :type RecordUrl: str
        :param _RecordSize: 流大小
        :type RecordSize: int
        :param _VideoId: 流ID
        :type VideoId: str
        :param _Role: 流类型
        :type Role: str
        """
        self._UserId = None
        self._StartTime = None
        self._StopTime = None
        self._Duration = None
        self._FileFormat = None
        self._RecordUrl = None
        self._RecordSize = None
        self._VideoId = None
        self._Role = None

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def StopTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def Duration(self):
        r"""总时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FileFormat(self):
        r"""文件格式
        :rtype: str
        """
        return self._FileFormat

    @FileFormat.setter
    def FileFormat(self, FileFormat):
        self._FileFormat = FileFormat

    @property
    def RecordUrl(self):
        r"""流url
        :rtype: str
        """
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def RecordSize(self):
        r"""流大小
        :rtype: int
        """
        return self._RecordSize

    @RecordSize.setter
    def RecordSize(self, RecordSize):
        self._RecordSize = RecordSize

    @property
    def VideoId(self):
        r"""流ID
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def Role(self):
        r"""流类型
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._StartTime = params.get("StartTime")
        self._StopTime = params.get("StopTime")
        self._Duration = params.get("Duration")
        self._FileFormat = params.get("FileFormat")
        self._RecordUrl = params.get("RecordUrl")
        self._RecordSize = params.get("RecordSize")
        self._VideoId = params.get("VideoId")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRecordRequest(AbstractModel):
    r"""StartRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 学校ID
        :type SdkAppId: int
        :param _RoomId: 房间ID
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRecordResponse(AbstractModel):
    r"""StartRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartRoomRequest(AbstractModel):
    r"""StartRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂ID
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRoomResponse(AbstractModel):
    r"""StartRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopRecordRequest(AbstractModel):
    r"""StopRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 学校ID
        :type SdkAppId: int
        :param _RoomId: 课堂ID
        :type RoomId: int
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""学校ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""课堂ID
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TaskId(self):
        r"""任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordResponse(AbstractModel):
    r"""StopRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TextMarkConfig(AbstractModel):
    r"""文字水印配置

    """

    def __init__(self):
        r"""
        :param _Text: 文字水印内容
        :type Text: str
        :param _Color: 文字水印颜色
        :type Color: str
        """
        self._Text = None
        self._Color = None

    @property
    def Text(self):
        r"""文字水印内容
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Color(self):
        r"""文字水印颜色
        :rtype: str
        """
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextMsgContent(AbstractModel):
    r"""文本消息

    """

    def __init__(self):
        r"""
        :param _Text: 文本消息。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        r"""文本消息。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferItem(AbstractModel):
    r"""转存配置

    """

    def __init__(self):
        r"""
        :param _State: 转存状态， 1正常 2停用
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        """
        self._State = None

    @property
    def State(self):
        r"""转存状态， 1正常 2停用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDocumentFromRoomRequest(AbstractModel):
    r"""UnbindDocumentFromRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        :param _DocumentId: 文档ID。
        :type DocumentId: str
        """
        self._RoomId = None
        self._DocumentId = None

    @property
    def RoomId(self):
        r"""房间ID。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DocumentId(self):
        r"""文档ID。
        :rtype: str
        """
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._DocumentId = params.get("DocumentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDocumentFromRoomResponse(AbstractModel):
    r"""UnbindDocumentFromRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UnblockKickedUserRequest(AbstractModel):
    r"""UnblockKickedUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码平台的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 课堂Id。
        :type RoomId: int
        :param _UserId: 需要解禁踢出的成员Id。
        :type UserId: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None

    @property
    def SdkAppId(self):
        r"""低代码平台的SdkAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""课堂Id。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""需要解禁踢出的成员Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnblockKickedUserResponse(AbstractModel):
    r"""UnblockKickedUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UserInfo(AbstractModel):
    r"""用户信息结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用Id。
        :type SdkAppId: int
        :param _UserId: 用户Id。
        :type UserId: str
        :param _Name: 用户昵称。
        :type Name: str
        :param _Avatar: 用户头像Url。
        :type Avatar: str
        :param _OriginId: 用户在客户系统的Id
        :type OriginId: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Name = None
        self._Avatar = None
        self._OriginId = None

    @property
    def SdkAppId(self):
        r"""应用Id。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        r"""用户Id。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Name(self):
        r"""用户昵称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        r"""用户头像Url。
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def OriginId(self):
        r"""用户在客户系统的Id
        :rtype: str
        """
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._OriginId = params.get("OriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkConfig(AbstractModel):
    r"""水印配置

    """

    def __init__(self):
        r"""
        :param _Url: 水印图片的url
        :type Url: str
        :param _Width: 水印宽。为比例值
        :type Width: float
        :param _Height: 水印高。为比例值
        :type Height: float
        :param _LocationX: 水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间。
        :type LocationX: float
        :param _LocationY: 水印Y偏移, 取值:0-100, 表示区域Y方向的百分比。比如50，则表示位于Y轴中间。
        :type LocationY: float
        """
        self._Url = None
        self._Width = None
        self._Height = None
        self._LocationX = None
        self._LocationY = None

    @property
    def Url(self):
        r"""水印图片的url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Width(self):
        r"""水印宽。为比例值
        :rtype: float
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""水印高。为比例值
        :rtype: float
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def LocationX(self):
        r"""水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间。
        :rtype: float
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""水印Y偏移, 取值:0-100, 表示区域Y方向的百分比。比如50，则表示位于Y轴中间。
        :rtype: float
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        