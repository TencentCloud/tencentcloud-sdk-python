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


class AddGroupMemberRequest(AbstractModel):
    """AddGroupMember请求参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
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
    """AddGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class AnswerInfo(AbstractModel):
    """房间问答答案详情

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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsCorrect(self):
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
    """每个选项答题人数统计

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
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Count(self):
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
    """应用配置信息

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID
        :type ApplicationId: str
        :param _AppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param _State: 应用状态 1正常 2停用
注意：此字段可能返回 null，表示取不到有效值。
        :type State: int
        :param _AppVersion: 1试用 2轻量版 3标准版 4旗舰版
注意：此字段可能返回 null，表示取不到有效值。
        :type AppVersion: int
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _Callback: 回调
注意：此字段可能返回 null，表示取不到有效值。
        :type Callback: str
        :param _CallbackKey: 回调Key
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

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
    """应用自定义内容

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
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LogoUrl(self):
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def HomeUrl(self):
        return self._HomeUrl

    @HomeUrl.setter
    def HomeUrl(self, HomeUrl):
        self._HomeUrl = HomeUrl

    @property
    def JsUrl(self):
        return self._JsUrl

    @JsUrl.setter
    def JsUrl(self, JsUrl):
        self._JsUrl = JsUrl

    @property
    def CssUrl(self):
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
    """背景图片配置

    """

    def __init__(self):
        r"""
        :param _Url: 背景图片的url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
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
    """BatchAddGroupMember请求参数结构体

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
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
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
    """BatchAddGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class BatchCreateGroupWithMembersRequest(AbstractModel):
    """BatchCreateGroupWithMembers请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def GroupBaseInfos(self):
        return self._GroupBaseInfos

    @GroupBaseInfos.setter
    def GroupBaseInfos(self, GroupBaseInfos):
        self._GroupBaseInfos = GroupBaseInfos

    @property
    def MemberIds(self):
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
    """BatchCreateGroupWithMembers返回参数结构体

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
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._RequestId = params.get("RequestId")


class BatchCreateRoomRequest(AbstractModel):
    """BatchCreateRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码平台的SdkAppId。
        :type SdkAppId: int
        :param _RoomInfos: 创建房间ID列表
        :type RoomInfos: list of RoomInfo
        """
        self._SdkAppId = None
        self._RoomInfos = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomInfos(self):
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
    """BatchCreateRoom返回参数结构体

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
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._RequestId = params.get("RequestId")


class BatchDeleteGroupMemberRequest(AbstractModel):
    """BatchDeleteGroupMember请求参数结构体

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
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
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
    """BatchDeleteGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class BatchDeleteRecordRequest(AbstractModel):
    """BatchDeleteRecord请求参数结构体

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
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def SdkAppId(self):
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
    """BatchDeleteRecord返回参数结构体

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
        return self._RoomIds

    @RoomIds.setter
    def RoomIds(self, RoomIds):
        self._RoomIds = RoomIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomIds = params.get("RoomIds")
        self._RequestId = params.get("RequestId")


class BatchDescribeDocumentRequest(AbstractModel):
    """BatchDescribeDocument请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DocumentId(self):
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
    """BatchDescribeDocument返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Documents(self):
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def RequestId(self):
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
    """BatchRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 批量注册用户信息列表
        :type Users: list of BatchUserRequest
        """
        self._Users = None

    @property
    def Users(self):
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
    """BatchRegister返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Users: 注册成功的用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of BatchUserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Users = None
        self._RequestId = None

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
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
    """批量注册用户信息

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

        :type SdkAppId: int
        :param _UserId: 用户ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _OriginId: 用户在客户系统的Id。 若用户注册时该字段为空，则默认为 UserId 值一致。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginId: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._OriginId = None

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
    def OriginId(self):
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
    """用户注册请求信息

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Avatar(self):
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
    """BindDocumentToRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        :param _DocumentId: 文档ID。
        :type DocumentId: str
        :param _BindType: 绑定类型。后台可透传到客户端，默认为0。客户端可以根据这个字段实现业务逻辑。
        :type BindType: int
        """
        self._RoomId = None
        self._DocumentId = None
        self._BindType = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DocumentId(self):
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def BindType(self):
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
    """BindDocumentToRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ClassScoreItem(AbstractModel):
    """课堂评分字段

    """

    def __init__(self):
        r"""
        :param _RoomId: 课堂iD
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: int
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _CreateTime: 评分时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _Score: 课堂评分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _ScoreMsg: 课堂评价
注意：此字段可能返回 null，表示取不到有效值。
        :type ScoreMsg: str
        """
        self._RoomId = None
        self._UserId = None
        self._CreateTime = None
        self._Score = None
        self._ScoreMsg = None

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
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def ScoreMsg(self):
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
    """CreateDocument请求参数结构体

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
        :param _MinScaleResolution: 转码后文档的最小分辨率，不传、传空字符串或分辨率格式错误则使用文档原分辨率。示例：1280x720，注意分辨率宽高中间为英文字母"xyz"的"x"
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def DocumentUrl(self):
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def TranscodeType(self):
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def AutoHandleUnsupportedElement(self):
        return self._AutoHandleUnsupportedElement

    @AutoHandleUnsupportedElement.setter
    def AutoHandleUnsupportedElement(self, AutoHandleUnsupportedElement):
        self._AutoHandleUnsupportedElement = AutoHandleUnsupportedElement

    @property
    def MinScaleResolution(self):
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
    """CreateDocument返回参数结构体

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
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocumentId = params.get("DocumentId")
        self._RequestId = params.get("RequestId")


class CreateGroupWithMembersRequest(AbstractModel):
    """CreateGroupWithMembers请求参数结构体

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
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def MemberIds(self):
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
    """CreateGroupWithMembers返回参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateGroupWithSubGroupRequest(AbstractModel):
    """CreateGroupWithSubGroup请求参数结构体

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
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SubGroupIds(self):
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds

    @property
    def TeacherId(self):
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
    """CreateGroupWithSubGroup返回参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateRoomRequest(AbstractModel):
    """CreateRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 房间名称。
        :type Name: str
        :param _StartTime: 预定的房间开始时间，unix时间戳（秒）。
        :type StartTime: int
        :param _EndTime: 预定的房间结束时间，unix时间戳（秒）。
        :type EndTime: int
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _Resolution: 分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :type Resolution: int
        :param _MaxMicNumber: 设置房间/课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。该取值影响计费，请根据业务实际情况设置。计费规则见“购买指南”下“计费概述”。
        :type MaxMicNumber: int
        :param _SubType: 房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
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
        :param _DisableRecord: 上课后是否禁止自动录制。可以有以下取值：
0 不禁止录制（自动开启录制，默认值）
1 禁止录制
注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :type DisableRecord: int
        :param _Assistants: 助教Id列表。通过[注册用户]接口获取的UserId。指定后该用户在房间内拥有助教权限。
        :type Assistants: list of str
        :param _RTCAudienceNumber: rtc人数。
        :type RTCAudienceNumber: int
        :param _AudienceType: 观看类型。互动观看 （默认）
        :type AudienceType: int
        :param _RecordLayout: 录制模板。房间子类型为视频+白板（SubType=videodoc）时默认为3，房间子类型为纯视频（SubType=video）时默认为0。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :type RecordLayout: int
        :param _GroupId: 房间绑定的群组ID,非空时限制组成员进入
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
        :param _RoomType: 房间类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (预留参数，暂未开放)
注：大班课的布局(layout)只有三分屏
        :type RoomType: int
        :param _EndDelayTime: 拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
        :type EndDelayTime: int
        :param _LiveType: 直播类型：0 常规（默认）1 伪直播 2 RTMP推流直播
        :type LiveType: int
        :param _RecordLiveUrl: 伪直播链接
        :type RecordLiveUrl: str
        :param _EnableAutoStart: 是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1或2的时候有效
        :type EnableAutoStart: int
        :param _RecordBackground: 录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
        :type RecordBackground: str
        :param _RecordScene: 录制自定义场景，仅recordlayout=9的时候此参数有效,数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _RecordStream: 录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :type RecordStream: int
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
        self._EndDelayTime = None
        self._LiveType = None
        self._RecordLiveUrl = None
        self._EnableAutoStart = None
        self._RecordBackground = None
        self._RecordScene = None
        self._RecordLang = None
        self._RecordStream = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def TurnOffMic(self):
        return self._TurnOffMic

    @TurnOffMic.setter
    def TurnOffMic(self, TurnOffMic):
        self._TurnOffMic = TurnOffMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RTCAudienceNumber(self):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        return self._RTCAudienceNumber

    @RTCAudienceNumber.setter
    def RTCAudienceNumber(self, RTCAudienceNumber):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        self._RTCAudienceNumber = RTCAudienceNumber

    @property
    def AudienceType(self):
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def RecordLayout(self):
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def EndDelayTime(self):
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RecordScene(self):
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        self._RecordLang = RecordLang

    @property
    def RecordStream(self):
        return self._RecordStream

    @RecordStream.setter
    def RecordStream(self, RecordStream):
        self._RecordStream = RecordStream


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
        self._EndDelayTime = params.get("EndDelayTime")
        self._LiveType = params.get("LiveType")
        self._RecordLiveUrl = params.get("RecordLiveUrl")
        self._EnableAutoStart = params.get("EnableAutoStart")
        self._RecordBackground = params.get("RecordBackground")
        self._RecordScene = params.get("RecordScene")
        self._RecordLang = params.get("RecordLang")
        self._RecordStream = params.get("RecordStream")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoomResponse(AbstractModel):
    """CreateRoom返回参数结构体

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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._RequestId = params.get("RequestId")


class CreateSupervisorRequest(AbstractModel):
    """CreateSupervisor请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Users(self):
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
    """CreateSupervisor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class CustomMsgContent(AbstractModel):
    """自定义消息

    """

    def __init__(self):
        r"""
        :param _Data: 自定义消息数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Desc: 自定义消息描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Ext: 扩展字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: str
        """
        self._Data = None
        self._Desc = None
        self._Ext = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Ext(self):
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
        


class DeleteAppCustomContentRequest(AbstractModel):
    """DeleteAppCustomContent请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Scenes(self):
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
    """DeleteAppCustomContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteDocumentRequest(AbstractModel):
    """DeleteDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档ID。
        :type DocumentId: str
        """
        self._DocumentId = None

    @property
    def DocumentId(self):
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
    """DeleteDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteGroupMemberRequest(AbstractModel):
    """DeleteGroupMember请求参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MemberIds(self):
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
    """DeleteGroupMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

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
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def SdkAppId(self):
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
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteRecordRequest(AbstractModel):
    """DeleteRecord请求参数结构体

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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
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
    """DeleteRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteRoomRequest(AbstractModel):
    """DeleteRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
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
    """DeleteRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteSupervisorRequest(AbstractModel):
    """DeleteSupervisor请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Users(self):
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
    """DeleteSupervisor返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 待删除用户的ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
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
    """DeleteUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAnswerListRequest(AbstractModel):
    """DescribeAnswerList请求参数结构体

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
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
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
    """DescribeAnswerList返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AnswerInfo(self):
        return self._AnswerInfo

    @AnswerInfo.setter
    def AnswerInfo(self, AnswerInfo):
        self._AnswerInfo = AnswerInfo

    @property
    def RequestId(self):
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
    """DescribeAppDetail请求参数结构体

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
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def DeveloperId(self):
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
    """DescribeAppDetail返回参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AppConfig(self):
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig

    @property
    def SceneConfig(self):
        return self._SceneConfig

    @SceneConfig.setter
    def SceneConfig(self, SceneConfig):
        self._SceneConfig = SceneConfig

    @property
    def TransferConfig(self):
        return self._TransferConfig

    @TransferConfig.setter
    def TransferConfig(self, TransferConfig):
        self._TransferConfig = TransferConfig

    @property
    def RequestId(self):
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
    """DescribeCurrentMemberList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间Id。
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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
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
    """DescribeCurrentMemberList返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberRecords(self):
        return self._MemberRecords

    @MemberRecords.setter
    def MemberRecords(self, MemberRecords):
        self._MemberRecords = MemberRecords

    @property
    def RequestId(self):
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
    """DescribeDeveloper请求参数结构体

    """


class DescribeDeveloperResponse(AbstractModel):
    """DescribeDeveloper返回参数结构体

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
        return self._DeveloperId

    @DeveloperId.setter
    def DeveloperId(self, DeveloperId):
        self._DeveloperId = DeveloperId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeveloperId = params.get("DeveloperId")
        self._RequestId = params.get("RequestId")


class DescribeDocumentRequest(AbstractModel):
    """DescribeDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档Id（唯一id）
        :type DocumentId: str
        """
        self._DocumentId = None

    @property
    def DocumentId(self):
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
    """DescribeDocument返回参数结构体

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
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def DocumentUrl(self):
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def TranscodeResult(self):
        return self._TranscodeResult

    @TranscodeResult.setter
    def TranscodeResult(self, TranscodeResult):
        self._TranscodeResult = TranscodeResult

    @property
    def TranscodeType(self):
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def TranscodeProgress(self):
        return self._TranscodeProgress

    @TranscodeProgress.setter
    def TranscodeProgress(self, TranscodeProgress):
        self._TranscodeProgress = TranscodeProgress

    @property
    def TranscodeState(self):
        return self._TranscodeState

    @TranscodeState.setter
    def TranscodeState(self, TranscodeState):
        self._TranscodeState = TranscodeState

    @property
    def TranscodeInfo(self):
        return self._TranscodeInfo

    @TranscodeInfo.setter
    def TranscodeInfo(self, TranscodeInfo):
        self._TranscodeInfo = TranscodeInfo

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Preview(self):
        return self._Preview

    @Preview.setter
    def Preview(self, Preview):
        self._Preview = Preview

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MinScaleResolution(self):
        return self._MinScaleResolution

    @MinScaleResolution.setter
    def MinScaleResolution(self, MinScaleResolution):
        self._MinScaleResolution = MinScaleResolution

    @property
    def RequestId(self):
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
    """DescribeDocumentsByRoom请求参数结构体

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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
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
    """DescribeDocumentsByRoom返回参数结构体

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
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

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
        if params.get("Documents") is not None:
            self._Documents = []
            for item in params.get("Documents"):
                obj = DocumentInfo()
                obj._deserialize(item)
                self._Documents.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeDocumentsRequest(AbstractModel):
    """DescribeDocuments请求参数结构体

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
        return self._SchoolId

    @SchoolId.setter
    def SchoolId(self, SchoolId):
        self._SchoolId = SchoolId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def DocumentId(self):
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
    """DescribeDocuments返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Documents(self):
        return self._Documents

    @Documents.setter
    def Documents(self, Documents):
        self._Documents = Documents

    @property
    def RequestId(self):
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
    """DescribeGroupList请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def MemberId(self):
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
    """DescribeGroupList返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def GroupInfos(self):
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos

    @property
    def RequestId(self):
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
    """DescribeGroupMemberList请求参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
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
    """DescribeGroupMemberList返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberIds(self):
        return self._MemberIds

    @MemberIds.setter
    def MemberIds(self, MemberIds):
        self._MemberIds = MemberIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._MemberIds = params.get("MemberIds")
        self._RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup请求参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
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
    """DescribeGroup返回参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def SubGroupIds(self):
        return self._SubGroupIds

    @SubGroupIds.setter
    def SubGroupIds(self, SubGroupIds):
        self._SubGroupIds = SubGroupIds

    @property
    def RequestId(self):
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


class DescribeQuestionListRequest(AbstractModel):
    """DescribeQuestionList请求参数结构体

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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
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
    """DescribeQuestionList返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def QuestionInfo(self):
        return self._QuestionInfo

    @QuestionInfo.setter
    def QuestionInfo(self, QuestionInfo):
        self._QuestionInfo = QuestionInfo

    @property
    def RequestId(self):
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


class DescribeRecordStreamRequest(AbstractModel):
    """DescribeRecordStream请求参数结构体

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
    """DescribeRecordStream返回参数结构体

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
        return self._SchoolId

    @SchoolId.setter
    def SchoolId(self, SchoolId):
        self._SchoolId = SchoolId

    @property
    def ClassId(self):
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def ClassType(self):
        return self._ClassType

    @ClassType.setter
    def ClassType(self, ClassType):
        self._ClassType = ClassType

    @property
    def StreamInfo(self):
        return self._StreamInfo

    @StreamInfo.setter
    def StreamInfo(self, StreamInfo):
        self._StreamInfo = StreamInfo

    @property
    def RequestId(self):
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


class DescribeRoomForbiddenUserRequest(AbstractModel):
    """DescribeRoomForbiddenUser请求参数结构体

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
    """DescribeRoomForbiddenUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MutedAccountList: 禁言用户信息数组，内容包括被禁言的成员 ID，及其被禁言到的时间（使用 UTC 时间，即世界协调时间）
注意：此字段可能返回 null，表示取不到有效值。
        :type MutedAccountList: list of MutedAccountList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MutedAccountList = None
        self._RequestId = None

    @property
    def MutedAccountList(self):
        return self._MutedAccountList

    @MutedAccountList.setter
    def MutedAccountList(self, MutedAccountList):
        self._MutedAccountList = MutedAccountList

    @property
    def RequestId(self):
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
    """DescribeRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间Id。
        :type RoomId: int
        :param _RTMPStreamingURL: 请求RTMP推流链接，0：否，1：是，默认为0。
        :type RTMPStreamingURL: int
        """
        self._RoomId = None
        self._RTMPStreamingURL = None

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RTMPStreamingURL(self):
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
    """DescribeRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 房间名称。
        :type Name: str
        :param _StartTime: 预定的房间开始时间，unix时间戳（秒）。
        :type StartTime: int
        :param _EndTime: 预定的房间结束时间，unix时间戳（秒）。
        :type EndTime: int
        :param _TeacherId: 老师的UserId。
        :type TeacherId: str
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _AudienceType: 观看类型。互动观看 （默认）	
        :type AudienceType: int
        :param _Resolution: 分辨率。可以有如下取值：
1 标清
2 高清
3 全高清
        :type Resolution: int
        :param _MaxMicNumber: 设置房间/课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
        :type MaxMicNumber: int
        :param _AutoMic: 进入课堂时是否自动连麦。可以有以下取值：
0 不自动连麦（需要手动申请上麦，默认值）
1 自动连麦
        :type AutoMic: int
        :param _AudioQuality: 高音质模式。可以有以下取值：
0 不开启高音质（默认值）
1 开启高音质
        :type AudioQuality: int
        :param _SubType: 房间子类型，可以有以下取值：
videodoc 文档+视频
video 纯视频
        :type SubType: str
        :param _DisableRecord: 上课后是否禁止自动录制。可以有以下取值：
0 不禁止录制（自动开启录制，默认值）
1 禁止录制
注：如果该配置取值为0，录制将从上课后开始，课堂结束后停止。
        :type DisableRecord: int
        :param _Assistants: 助教UserId列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Assistants: list of str
        :param _RecordUrl: 录制地址（协议为https)。仅在房间结束后存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordUrl: str
        :param _Status: 课堂状态。0为未开始，1为已开始，2为已结束，3为已过期。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _GroupId: 房间绑定的群组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _EnableDirectControl: 打开学生麦克风/摄像头的授权开关
        :type EnableDirectControl: int
        :param _InteractionMode: 开启专注模式。
0 收看全部角色音视频(默认)
1 只看老师和助教
        :type InteractionMode: int
        :param _VideoOrientation: 横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
        :type VideoOrientation: int
        :param _IsGradingRequiredPostClass: 该房间是否开启了课后评分功能。0：未开启  1：开启
        :type IsGradingRequiredPostClass: int
        :param _RoomType: 房间类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (后续扩展)
注：大班课的布局(layout)只有三分屏
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
        :param _RecordScene: 录制自定义场景，仅recordlayout=9的时候此参数有效
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _RecordStream: 录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :type RecordStream: int
        :param _RecordLayout: 录制模板。房间子类型为视频+白板（SubType=videodoc）时默认为3，房间子类型为纯视频（SubType=video）时默认为0。录制模板枚举值参考：https://cloud.tencent.com/document/product/1639/89744
        :type RecordLayout: int
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
        self._RequestId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudienceType(self):
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def VideoDuration(self):
        return self._VideoDuration

    @VideoDuration.setter
    def VideoDuration(self, VideoDuration):
        self._VideoDuration = VideoDuration

    @property
    def EndDelayTime(self):
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RTMPStreamingURL(self):
        return self._RTMPStreamingURL

    @RTMPStreamingURL.setter
    def RTMPStreamingURL(self, RTMPStreamingURL):
        self._RTMPStreamingURL = RTMPStreamingURL

    @property
    def RecordScene(self):
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        self._RecordLang = RecordLang

    @property
    def RecordStream(self):
        return self._RecordStream

    @RecordStream.setter
    def RecordStream(self, RecordStream):
        self._RecordStream = RecordStream

    @property
    def RecordLayout(self):
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def RequestId(self):
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
        self._RequestId = params.get("RequestId")


class DescribeRoomStatisticsRequest(AbstractModel):
    """DescribeRoomStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间Id。
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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
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
    """DescribeRoomStatistics返回参数结构体

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
注意：此字段可能返回 null，表示取不到有效值。
        :type RealStartTime: int
        :param _RealEndTime: 秒级unix时间戳，实际房间结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealEndTime: int
        :param _MessageCount: 房间消息总数。
        :type MessageCount: int
        :param _MicCount: 房间连麦总数。
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
        return self._PeakMemberNumber

    @PeakMemberNumber.setter
    def PeakMemberNumber(self, PeakMemberNumber):
        self._PeakMemberNumber = PeakMemberNumber

    @property
    def MemberNumber(self):
        return self._MemberNumber

    @MemberNumber.setter
    def MemberNumber(self, MemberNumber):
        self._MemberNumber = MemberNumber

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MemberRecords(self):
        return self._MemberRecords

    @MemberRecords.setter
    def MemberRecords(self, MemberRecords):
        self._MemberRecords = MemberRecords

    @property
    def RealStartTime(self):
        return self._RealStartTime

    @RealStartTime.setter
    def RealStartTime(self, RealStartTime):
        self._RealStartTime = RealStartTime

    @property
    def RealEndTime(self):
        return self._RealEndTime

    @RealEndTime.setter
    def RealEndTime(self, RealEndTime):
        self._RealEndTime = RealEndTime

    @property
    def MessageCount(self):
        return self._MessageCount

    @MessageCount.setter
    def MessageCount(self, MessageCount):
        self._MessageCount = MessageCount

    @property
    def MicCount(self):
        return self._MicCount

    @MicCount.setter
    def MicCount(self, MicCount):
        self._MicCount = MicCount

    @property
    def RequestId(self):
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
    """DescribeScoreList请求参数结构体

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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
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
    """DescribeScoreList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Scores: 课堂评分列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Scores: list of ClassScoreItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Scores = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Scores(self):
        return self._Scores

    @Scores.setter
    def Scores(self, Scores):
        self._Scores = Scores

    @property
    def RequestId(self):
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
    """DescribeSdkAppIdUsers请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
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
    """DescribeSdkAppIdUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 用户总数
        :type Total: int
        :param _Users: 当前获取用户信息数组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of UserInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Users = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
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
    """DescribeSupervisors请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
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
    """DescribeSupervisors返回参数结构体

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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def RequestId(self):
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


class DescribeUserRequest(AbstractModel):
    """DescribeUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户Id。
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
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
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser返回参数结构体

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
注意：此字段可能返回 null，表示取不到有效值。
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
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def RequestId(self):
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


class DocumentInfo(AbstractModel):
    """文档信息

    """

    def __init__(self):
        r"""
        :param _DocumentId: 文档Id
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentId: str
        :param _DocumentUrl: 文档原址url
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentUrl: str
        :param _DocumentName: 文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentName: str
        :param _Owner: 文档所有者UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param _SdkAppId: 应用Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppId: int
        :param _Permission: 文档权限，0：私有课件 1：公共课件
注意：此字段可能返回 null，表示取不到有效值。
        :type Permission: int
        :param _TranscodeResult: 转码结果，无需转码为空，转码成功为结果url，转码失败为错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeResult: str
        :param _TranscodeType: 转码类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeType: int
        :param _TranscodeProgress: 转码进度， 0 - 100 表示（0% - 100%）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeProgress: int
        :param _TranscodeState: 转码状态，0为无需转码，1为正在转码，2为转码失败，3为转码成功
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeState: int
        :param _TranscodeInfo: 转码失败后的错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TranscodeInfo: str
        :param _DocumentType: 文档类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentType: str
        :param _DocumentSize: 文档大小，单位：字节
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentSize: int
        :param _UpdateTime: 更新的UNIX时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _Pages: 课件页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        :param _Width: 宽，仅在静态转码的课件有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 高，仅在静态转码的课件有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Cover: 封面，仅转码的课件会生成封面
注意：此字段可能返回 null，表示取不到有效值。
        :type Cover: str
        :param _Preview: 课件预览地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Preview: str
        :param _Resolution: 文档的分辨率
注意：此字段可能返回 null，表示取不到有效值。
        :type Resolution: str
        :param _MinScaleResolution: 转码后文档的最小分辨率，和创建文档时传入的参数一致。
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._DocumentId

    @DocumentId.setter
    def DocumentId(self, DocumentId):
        self._DocumentId = DocumentId

    @property
    def DocumentUrl(self):
        return self._DocumentUrl

    @DocumentUrl.setter
    def DocumentUrl(self, DocumentUrl):
        self._DocumentUrl = DocumentUrl

    @property
    def DocumentName(self):
        return self._DocumentName

    @DocumentName.setter
    def DocumentName(self, DocumentName):
        self._DocumentName = DocumentName

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Permission(self):
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def TranscodeResult(self):
        return self._TranscodeResult

    @TranscodeResult.setter
    def TranscodeResult(self, TranscodeResult):
        self._TranscodeResult = TranscodeResult

    @property
    def TranscodeType(self):
        return self._TranscodeType

    @TranscodeType.setter
    def TranscodeType(self, TranscodeType):
        self._TranscodeType = TranscodeType

    @property
    def TranscodeProgress(self):
        return self._TranscodeProgress

    @TranscodeProgress.setter
    def TranscodeProgress(self, TranscodeProgress):
        self._TranscodeProgress = TranscodeProgress

    @property
    def TranscodeState(self):
        return self._TranscodeState

    @TranscodeState.setter
    def TranscodeState(self, TranscodeState):
        self._TranscodeState = TranscodeState

    @property
    def TranscodeInfo(self):
        return self._TranscodeInfo

    @TranscodeInfo.setter
    def TranscodeInfo(self, TranscodeInfo):
        self._TranscodeInfo = TranscodeInfo

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentSize(self):
        return self._DocumentSize

    @DocumentSize.setter
    def DocumentSize(self, DocumentSize):
        self._DocumentSize = DocumentSize

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

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
    def Cover(self):
        return self._Cover

    @Cover.setter
    def Cover(self, Cover):
        self._Cover = Cover

    @property
    def Preview(self):
        return self._Preview

    @Preview.setter
    def Preview(self, Preview):
        self._Preview = Preview

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MinScaleResolution(self):
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
    """EndRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
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
    """EndRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class EventDataInfo(AbstractModel):
    """房间事件对应的信息。

    """

    def __init__(self):
        r"""
        :param _RoomId: 事件发生的房间号。
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: int
        :param _UserId: 事件发生的用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _Device: 用户设备类型。0: Unknown; 1: Windows; 2: macOS; 3: Android; 4: iOS; 5: Web; 6: Mobile webpage; 7: Weixin Mini Program.
注意：此字段可能返回 null，表示取不到有效值。
        :type Device: int
        :param _Duration: 录制时长。单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _RecordSize: 录制文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordSize: int
        :param _RecordUrl: 录制url
注意：此字段可能返回 null，表示取不到有效值。
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
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RecordSize(self):
        return self._RecordSize

    @RecordSize.setter
    def RecordSize(self, RecordSize):
        self._RecordSize = RecordSize

    @property
    def RecordUrl(self):
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
    """房间事件信息。

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
注意：此字段可能返回 null，表示取不到有效值。
        :type EventData: :class:`tencentcloud.lcic.v20220817.models.EventDataInfo`
        """
        self._Timestamp = None
        self._EventType = None
        self._EventData = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def EventData(self):
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
    """表情消息

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
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Data(self):
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
    """ForbidSendMsg请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 房间ID。
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
    def MembersAccount(self):
        return self._MembersAccount

    @MembersAccount.setter
    def MembersAccount(self, MembersAccount):
        self._MembersAccount = MembersAccount

    @property
    def MuteTime(self):
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
    """ForbidSendMsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class GetRoomEventRequest(AbstractModel):
    """GetRoomEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间Id。
        :type RoomId: int
        :param _SdkAppId: 应用Id。
        :type SdkAppId: int
        :param _Page: 起始页，1开始。keyword为空时有效。
        :type Page: int
        :param _Limit: 每页个数。keyword为空时有效。一次性最多200条。
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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
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
    """GetRoomEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 该房间的事件总数，keyword搜索不影响该值。
        :type Total: int
        :param _Events: 详细事件内容。包含相应的类型、发生的时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type Events: list of EventInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Events = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def RequestId(self):
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
    """GetRoomMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 房间Id。	
        :type RoomId: int
        :param _Seq: 消息序列。获取该序列以前的消息(不包含该seq消息)
        :type Seq: int
        :param _Limit: 消息拉取的条数。最大数量不能超过套餐包限制。
        :type Limit: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._Seq = None
        self._Limit = None

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
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._Seq = params.get("Seq")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoomMessageResponse(AbstractModel):
    """GetRoomMessage返回参数结构体

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
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def RequestId(self):
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
    """GetRooms请求参数结构体

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
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
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
    """GetRooms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Rooms: 房间列表
        :type Rooms: list of RoomItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Rooms = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Rooms(self):
        return self._Rooms

    @Rooms.setter
    def Rooms(self, Rooms):
        self._Rooms = Rooms

    @property
    def RequestId(self):
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
    """GetWatermark请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。

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
        


class GetWatermarkResponse(AbstractModel):
    """GetWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TeacherLogo: 老师视频区域的水印参数配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TeacherLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param _BoardLogo: 白板区域的水印参数配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BoardLogo: :class:`tencentcloud.lcic.v20220817.models.WatermarkConfig`
        :param _BackgroundPicture: 背景图片配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BackgroundPicture: :class:`tencentcloud.lcic.v20220817.models.BackgroundPictureConfig`
        :param _Text: 文字水印配置
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._TeacherLogo

    @TeacherLogo.setter
    def TeacherLogo(self, TeacherLogo):
        self._TeacherLogo = TeacherLogo

    @property
    def BoardLogo(self):
        return self._BoardLogo

    @BoardLogo.setter
    def BoardLogo(self, BoardLogo):
        self._BoardLogo = BoardLogo

    @property
    def BackgroundPicture(self):
        return self._BackgroundPicture

    @BackgroundPicture.setter
    def BackgroundPicture(self, BackgroundPicture):
        self._BackgroundPicture = BackgroundPicture

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def RequestId(self):
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
    """批量创建群组基础信息

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
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
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
    """获取群组列表返回的群组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 群组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 群组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _TeacherId: 群组主讲人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TeacherId: str
        :param _GroupType: 群组类型 
0-基础群组 
1-组合群组，若为1时会返回子群组ID列表
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def SubGroupIds(self):
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
    """单张图片信息

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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

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
    def URL(self):
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
    """图片消息

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
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID

    @property
    def ImageFormat(self):
        return self._ImageFormat

    @ImageFormat.setter
    def ImageFormat(self, ImageFormat):
        self._ImageFormat = ImageFormat

    @property
    def ImageInfoList(self):
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
    """KickUserFromRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间Id。
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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

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
    def KickType(self):
        return self._KickType

    @KickType.setter
    def KickType(self, KickType):
        self._KickType = KickType

    @property
    def Duration(self):
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
    """KickUserFromRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class LoginOriginIdRequest(AbstractModel):
    """LoginOriginId请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def OriginId(self):
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
    """LoginOriginId返回参数结构体

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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class LoginUserRequest(AbstractModel):
    """LoginUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 注册获取的用户id。
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
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
    """LoginUser返回参数结构体

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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class MemberRecord(AbstractModel):
    """成员记录信息。

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
        :param _Stage: 用户的上台状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Stage: int
        :param _CurrentState: 用户状态。0为未到，1为在线，2为离线，3为被踢，4为永久被踢，5为暂时掉线
注意：此字段可能返回 null，表示取不到有效值。
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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PresentTime(self):
        return self._PresentTime

    @PresentTime.setter
    def PresentTime(self, PresentTime):
        self._PresentTime = PresentTime

    @property
    def Camera(self):
        return self._Camera

    @Camera.setter
    def Camera(self, Camera):
        self._Camera = Camera

    @property
    def Mic(self):
        return self._Mic

    @Mic.setter
    def Mic(self, Mic):
        self._Mic = Mic

    @property
    def Silence(self):
        return self._Silence

    @Silence.setter
    def Silence(self, Silence):
        self._Silence = Silence

    @property
    def AnswerQuestions(self):
        return self._AnswerQuestions

    @AnswerQuestions.setter
    def AnswerQuestions(self, AnswerQuestions):
        self._AnswerQuestions = AnswerQuestions

    @property
    def HandUps(self):
        return self._HandUps

    @HandUps.setter
    def HandUps(self, HandUps):
        self._HandUps = HandUps

    @property
    def FirstJoinTimestamp(self):
        return self._FirstJoinTimestamp

    @FirstJoinTimestamp.setter
    def FirstJoinTimestamp(self, FirstJoinTimestamp):
        self._FirstJoinTimestamp = FirstJoinTimestamp

    @property
    def LastQuitTimestamp(self):
        return self._LastQuitTimestamp

    @LastQuitTimestamp.setter
    def LastQuitTimestamp(self, LastQuitTimestamp):
        self._LastQuitTimestamp = LastQuitTimestamp

    @property
    def Rewords(self):
        return self._Rewords

    @Rewords.setter
    def Rewords(self, Rewords):
        self._Rewords = Rewords

    @property
    def IPAddress(self):
        return self._IPAddress

    @IPAddress.setter
    def IPAddress(self, IPAddress):
        self._IPAddress = IPAddress

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def PerMemberMicCount(self):
        return self._PerMemberMicCount

    @PerMemberMicCount.setter
    def PerMemberMicCount(self, PerMemberMicCount):
        self._PerMemberMicCount = PerMemberMicCount

    @property
    def PerMemberMessageCount(self):
        return self._PerMemberMessageCount

    @PerMemberMessageCount.setter
    def PerMemberMessageCount(self, PerMemberMessageCount):
        self._PerMemberMessageCount = PerMemberMessageCount

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SubGroupId(self):
        return self._SubGroupId

    @SubGroupId.setter
    def SubGroupId(self, SubGroupId):
        self._SubGroupId = SubGroupId

    @property
    def Stage(self):
        return self._Stage

    @Stage.setter
    def Stage(self, Stage):
        self._Stage = Stage

    @property
    def CurrentState(self):
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
    """单条消息体内容

    """

    def __init__(self):
        r"""
        :param _MessageType: 消息类型。0表示文本消息，1表示图片消息
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageType: int
        :param _TextMessage: 文本消息内容。message type为0时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextMessage: str
        :param _ImageMessage: 图片消息URL。 message type为1时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageMessage: str
        :param _CustomMessage: 自定义消息内容。message type为2时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomMessage: :class:`tencentcloud.lcic.v20220817.models.CustomMsgContent`
        """
        self._MessageType = None
        self._TextMessage = None
        self._ImageMessage = None
        self._CustomMessage = None

    @property
    def MessageType(self):
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def TextMessage(self):
        return self._TextMessage

    @TextMessage.setter
    def TextMessage(self, TextMessage):
        self._TextMessage = TextMessage

    @property
    def ImageMessage(self):
        return self._ImageMessage

    @ImageMessage.setter
    def ImageMessage(self, ImageMessage):
        self._ImageMessage = ImageMessage

    @property
    def CustomMessage(self):
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
    """历史消息列表

    """

    def __init__(self):
        r"""
        :param _Timestamp: 消息时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: int
        :param _FromAccount: 消息发送者
注意：此字段可能返回 null，表示取不到有效值。
        :type FromAccount: str
        :param _Seq: 消息序列号，当前课堂内唯一且单调递增
注意：此字段可能返回 null，表示取不到有效值。
        :type Seq: int
        :param _MessageBody: 历史消息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MessageBody: list of MessageItem
        """
        self._Timestamp = None
        self._FromAccount = None
        self._Seq = None
        self._MessageBody = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def FromAccount(self):
        return self._FromAccount

    @FromAccount.setter
    def FromAccount(self, FromAccount):
        self._FromAccount = FromAccount

    @property
    def Seq(self):
        return self._Seq

    @Seq.setter
    def Seq(self, Seq):
        self._Seq = Seq

    @property
    def MessageBody(self):
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
    """ModifyApp请求参数结构体

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

    @property
    def TransferId(self):
        return self._TransferId

    @TransferId.setter
    def TransferId(self, TransferId):
        self._TransferId = TransferId

    @property
    def TransferUrl(self):
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
    """ModifyApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup请求参数结构体

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
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def GroupName(self):
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
    """ModifyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyRoomRequest(AbstractModel):
    """ModifyRoom请求参数结构体

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

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

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
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def RecordLayout(self):
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def EndDelayTime(self):
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordScene(self):
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        self._RecordLang = RecordLang


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoomResponse(AbstractModel):
    """ModifyRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyUserProfileRequest(AbstractModel):
    """ModifyUserProfile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 待修改用户ID
        :type UserId: str
        :param _Nickname: 待修改的用户名
        :type Nickname: str
        :param _Avatar: 待修改头像url
        :type Avatar: str
        """
        self._UserId = None
        self._Nickname = None
        self._Avatar = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Avatar(self):
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
    """ModifyUserProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class MsgBody(AbstractModel):
    """自定义消息结构

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
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def TextMsgContent(self):
        return self._TextMsgContent

    @TextMsgContent.setter
    def TextMsgContent(self, TextMsgContent):
        self._TextMsgContent = TextMsgContent

    @property
    def FaceMsgContent(self):
        return self._FaceMsgContent

    @FaceMsgContent.setter
    def FaceMsgContent(self, FaceMsgContent):
        self._FaceMsgContent = FaceMsgContent

    @property
    def ImageMsgContent(self):
        return self._ImageMsgContent

    @ImageMsgContent.setter
    def ImageMsgContent(self, ImageMsgContent):
        self._ImageMsgContent = ImageMsgContent

    @property
    def CustomMsgContent(self):
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
    """禁言用户信息数组，内容包括被禁言的成员 ID，及其被禁言到的时间（使用 UTC 时间，即世界协调时间）

    """

    def __init__(self):
        r"""
        :param _MemberAccount: 用户 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberAccount: str
        :param _MutedUntil: 禁言到的时间（使用 UTC 时间，即世界协调时间）
注意：此字段可能返回 null，表示取不到有效值。
        :type MutedUntil: int
        """
        self._MemberAccount = None
        self._MutedUntil = None

    @property
    def MemberAccount(self):
        return self._MemberAccount

    @MemberAccount.setter
    def MemberAccount(self, MemberAccount):
        self._MemberAccount = MemberAccount

    @property
    def MutedUntil(self):
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
    """房间问答问题详情

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
注意：此字段可能返回 null，表示取不到有效值。
        :type AnswerStats: list of AnswerStat
        """
        self._QuestionId = None
        self._QuestionContent = None
        self._Duration = None
        self._CorrectAnswer = None
        self._AnswerStats = None

    @property
    def QuestionId(self):
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId

    @property
    def QuestionContent(self):
        return self._QuestionContent

    @QuestionContent.setter
    def QuestionContent(self, QuestionContent):
        self._QuestionContent = QuestionContent

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def CorrectAnswer(self):
        return self._CorrectAnswer

    @CorrectAnswer.setter
    def CorrectAnswer(self, CorrectAnswer):
        self._CorrectAnswer = CorrectAnswer

    @property
    def AnswerStats(self):
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
    """RegisterUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码互动课堂的SdkAppId。
        :type SdkAppId: int
        :param _Name: 用户名称。
        :type Name: str
        :param _OriginId: 用户在客户系统的Id，需要在同一应用下唯一。
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OriginId(self):
        return self._OriginId

    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    @property
    def Avatar(self):
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
    """RegisterUser返回参数结构体

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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class RoomInfo(AbstractModel):
    """批量创建房间的房间信息

    """

    def __init__(self):
        r"""
        :param _Name: 房间名称。
        :type Name: str
        :param _StartTime: 预定的房间开始时间，unix时间戳。
        :type StartTime: int
        :param _EndTime: 预定的房间结束时间，unix时间戳。
        :type EndTime: int
        :param _Resolution: 分辨率。可以有如下取值： 1 标清 2 高清 3 全高清
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
        :param _RoomType: 房间类型: 0 小班课（默认值）; 1 大班课; 2 1V1 (后续扩展)
注：大班课的布局(layout)只有三分屏
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
        :param _RecordScene: 录制自定义场景，仅recordlayout=9的时候此参数有效,数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
        :param _RecordStream: 录制类型 0 仅录制混流（默认） ;1 录制混流+单流，该模式下除混流录制基础上，分别录制老师、台上学生的音视频流，每路录制都会产生相应的录制费用 。示例：0
        :type RecordStream: int
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

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def TeacherId(self):
        return self._TeacherId

    @TeacherId.setter
    def TeacherId(self, TeacherId):
        self._TeacherId = TeacherId

    @property
    def AutoMic(self):
        return self._AutoMic

    @AutoMic.setter
    def AutoMic(self, AutoMic):
        self._AutoMic = AutoMic

    @property
    def TurnOffMic(self):
        return self._TurnOffMic

    @TurnOffMic.setter
    def TurnOffMic(self, TurnOffMic):
        self._TurnOffMic = TurnOffMic

    @property
    def AudioQuality(self):
        return self._AudioQuality

    @AudioQuality.setter
    def AudioQuality(self, AudioQuality):
        self._AudioQuality = AudioQuality

    @property
    def DisableRecord(self):
        return self._DisableRecord

    @DisableRecord.setter
    def DisableRecord(self, DisableRecord):
        self._DisableRecord = DisableRecord

    @property
    def Assistants(self):
        return self._Assistants

    @Assistants.setter
    def Assistants(self, Assistants):
        self._Assistants = Assistants

    @property
    def RTCAudienceNumber(self):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        return self._RTCAudienceNumber

    @RTCAudienceNumber.setter
    def RTCAudienceNumber(self, RTCAudienceNumber):
        warnings.warn("parameter `RTCAudienceNumber` is deprecated", DeprecationWarning) 

        self._RTCAudienceNumber = RTCAudienceNumber

    @property
    def AudienceType(self):
        return self._AudienceType

    @AudienceType.setter
    def AudienceType(self, AudienceType):
        self._AudienceType = AudienceType

    @property
    def RecordLayout(self):
        return self._RecordLayout

    @RecordLayout.setter
    def RecordLayout(self, RecordLayout):
        self._RecordLayout = RecordLayout

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def EndDelayTime(self):
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RecordScene(self):
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        warnings.warn("parameter `RecordLang` is deprecated", DeprecationWarning) 

        self._RecordLang = RecordLang

    @property
    def RecordStream(self):
        return self._RecordStream

    @RecordStream.setter
    def RecordStream(self, RecordStream):
        self._RecordStream = RecordStream


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoomItem(AbstractModel):
    """房间列表

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _RoomId: 房间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomId: int
        :param _Status: 房间状态。0 未开始 ；1进行中  ；2 已结束；3已过期
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param _RealStartTime: 实际开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RealStartTime: int
        :param _RealEndTime: 实际结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RealEndTime: int
        :param _Resolution: 分辨率。1 标清
2 高清
3 全高清
注意：此字段可能返回 null，表示取不到有效值。
        :type Resolution: int
        :param _MaxRTCMember: 最大允许连麦人数。已废弃，使用字段 MaxMicNumber
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRTCMember: int
        :param _ReplayUrl: 房间录制地址。已废弃，使用新字段 RecordUrl
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplayUrl: str
        :param _RecordUrl: 录制地址（协议为https)。仅在房间结束后存在。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordUrl: str
        :param _MaxMicNumber: 课堂同时最大可与老师进行连麦互动的人数，该参数支持正式上课/开播前调用修改房间修改。小班课取值范围[0,16]，大班课取值范围[0,1]，当取值为0时表示当前课堂/直播，不支持连麦互动。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxMicNumber: int
        :param _EnableDirectControl: 打开学生麦克风/摄像头的授权开关 
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableDirectControl: int
        :param _InteractionMode: 开启专注模式。 0 收看全部角色音视频(默认) 1 只看老师和助教
注意：此字段可能返回 null，表示取不到有效值。
        :type InteractionMode: int
        :param _VideoOrientation: 横竖屏。0：横屏开播（默认值）; 1：竖屏开播，当前仅支持移动端的纯视频类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoOrientation: int
        :param _IsGradingRequiredPostClass: 开启课后评分。 0：不开启(默认)  1：开启
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGradingRequiredPostClass: int
        :param _RoomType: 房间类型。0:小班课（默认值）；1:大班课；2:1V1（后续扩展）
注：大班课的布局(layout)只有三分屏
注意：此字段可能返回 null，表示取不到有效值。
        :type RoomType: int
        :param _EndDelayTime: 拖堂时间：单位分钟，0为不限制(默认值), -1为不能拖堂，大于0为拖堂的时间，最大值120分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type EndDelayTime: int
        :param _LiveType: 直播类型：0 常规（默认）1 伪直播
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveType: int
        :param _RecordLiveUrl: 伪直播回放链接	
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordLiveUrl: str
        :param _EnableAutoStart: 是否自动开始上课：0 不自动上课（默认） 1 自动上课 live_type=1的时候有效	
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableAutoStart: int
        :param _RecordBackground: 录制文件背景图片，支持png、jpg、jpeg、bmp格式，暂不支持透明通道
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordBackground: str
        :param _RecordScene: 录制自定义场景，仅recordlayout=9的时候此参数有效,数据内容为用户自定义场景参数，数据格式为json键值对方式，其中键值对的value为string类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordScene: str
        :param _RecordLang: 录制自定义语言，仅recordlayout=9的时候此参数有效
        :type RecordLang: str
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

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def RealStartTime(self):
        return self._RealStartTime

    @RealStartTime.setter
    def RealStartTime(self, RealStartTime):
        self._RealStartTime = RealStartTime

    @property
    def RealEndTime(self):
        return self._RealEndTime

    @RealEndTime.setter
    def RealEndTime(self, RealEndTime):
        self._RealEndTime = RealEndTime

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MaxRTCMember(self):
        return self._MaxRTCMember

    @MaxRTCMember.setter
    def MaxRTCMember(self, MaxRTCMember):
        self._MaxRTCMember = MaxRTCMember

    @property
    def ReplayUrl(self):
        return self._ReplayUrl

    @ReplayUrl.setter
    def ReplayUrl(self, ReplayUrl):
        self._ReplayUrl = ReplayUrl

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def MaxMicNumber(self):
        return self._MaxMicNumber

    @MaxMicNumber.setter
    def MaxMicNumber(self, MaxMicNumber):
        self._MaxMicNumber = MaxMicNumber

    @property
    def EnableDirectControl(self):
        return self._EnableDirectControl

    @EnableDirectControl.setter
    def EnableDirectControl(self, EnableDirectControl):
        self._EnableDirectControl = EnableDirectControl

    @property
    def InteractionMode(self):
        return self._InteractionMode

    @InteractionMode.setter
    def InteractionMode(self, InteractionMode):
        self._InteractionMode = InteractionMode

    @property
    def VideoOrientation(self):
        return self._VideoOrientation

    @VideoOrientation.setter
    def VideoOrientation(self, VideoOrientation):
        self._VideoOrientation = VideoOrientation

    @property
    def IsGradingRequiredPostClass(self):
        return self._IsGradingRequiredPostClass

    @IsGradingRequiredPostClass.setter
    def IsGradingRequiredPostClass(self, IsGradingRequiredPostClass):
        self._IsGradingRequiredPostClass = IsGradingRequiredPostClass

    @property
    def RoomType(self):
        return self._RoomType

    @RoomType.setter
    def RoomType(self, RoomType):
        self._RoomType = RoomType

    @property
    def EndDelayTime(self):
        return self._EndDelayTime

    @EndDelayTime.setter
    def EndDelayTime(self, EndDelayTime):
        self._EndDelayTime = EndDelayTime

    @property
    def LiveType(self):
        return self._LiveType

    @LiveType.setter
    def LiveType(self, LiveType):
        self._LiveType = LiveType

    @property
    def RecordLiveUrl(self):
        return self._RecordLiveUrl

    @RecordLiveUrl.setter
    def RecordLiveUrl(self, RecordLiveUrl):
        self._RecordLiveUrl = RecordLiveUrl

    @property
    def EnableAutoStart(self):
        return self._EnableAutoStart

    @EnableAutoStart.setter
    def EnableAutoStart(self, EnableAutoStart):
        self._EnableAutoStart = EnableAutoStart

    @property
    def RecordBackground(self):
        return self._RecordBackground

    @RecordBackground.setter
    def RecordBackground(self, RecordBackground):
        self._RecordBackground = RecordBackground

    @property
    def RecordScene(self):
        return self._RecordScene

    @RecordScene.setter
    def RecordScene(self, RecordScene):
        self._RecordScene = RecordScene

    @property
    def RecordLang(self):
        return self._RecordLang

    @RecordLang.setter
    def RecordLang(self, RecordLang):
        self._RecordLang = RecordLang


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SceneItem(AbstractModel):
    """场景配置

    """

    def __init__(self):
        r"""
        :param _Scene: 场景名称
        :type Scene: str
        :param _LogoUrl: logo地址
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoUrl: str
        :param _HomeUrl: 主页地址
注意：此字段可能返回 null，表示取不到有效值。
        :type HomeUrl: str
        :param _JSUrl: 自定义的js
注意：此字段可能返回 null，表示取不到有效值。
        :type JSUrl: str
        :param _CSSUrl: 自定义的css
注意：此字段可能返回 null，表示取不到有效值。
        :type CSSUrl: str
        """
        self._Scene = None
        self._LogoUrl = None
        self._HomeUrl = None
        self._JSUrl = None
        self._CSSUrl = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def LogoUrl(self):
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def HomeUrl(self):
        return self._HomeUrl

    @HomeUrl.setter
    def HomeUrl(self, HomeUrl):
        self._HomeUrl = HomeUrl

    @property
    def JSUrl(self):
        return self._JSUrl

    @JSUrl.setter
    def JSUrl(self, JSUrl):
        self._JSUrl = JSUrl

    @property
    def CSSUrl(self):
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
    """SendRoomNormalMessage请求参数结构体

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
        """
        self._SdkAppId = None
        self._RoomId = None
        self._FromAccount = None
        self._MsgBody = None
        self._CloudCustomData = None
        self._NickName = None

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
    def FromAccount(self):
        return self._FromAccount

    @FromAccount.setter
    def FromAccount(self, FromAccount):
        self._FromAccount = FromAccount

    @property
    def MsgBody(self):
        return self._MsgBody

    @MsgBody.setter
    def MsgBody(self, MsgBody):
        self._MsgBody = MsgBody

    @property
    def CloudCustomData(self):
        return self._CloudCustomData

    @CloudCustomData.setter
    def CloudCustomData(self, CloudCustomData):
        self._CloudCustomData = CloudCustomData

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendRoomNormalMessageResponse(AbstractModel):
    """SendRoomNormalMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class SendRoomNotificationMessageRequest(AbstractModel):
    """SendRoomNotificationMessage请求参数结构体

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
    def MsgContent(self):
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
    """SendRoomNotificationMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class SetAppCustomContentRequest(AbstractModel):
    """SetAppCustomContent请求参数结构体

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
        return self._CustomContent

    @CustomContent.setter
    def CustomContent(self, CustomContent):
        self._CustomContent = CustomContent

    @property
    def SdkAppId(self):
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
    """SetAppCustomContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class SetWatermarkRequest(AbstractModel):
    """SetWatermark请求参数结构体

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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TeacherUrl(self):
        return self._TeacherUrl

    @TeacherUrl.setter
    def TeacherUrl(self, TeacherUrl):
        self._TeacherUrl = TeacherUrl

    @property
    def BoardUrl(self):
        return self._BoardUrl

    @BoardUrl.setter
    def BoardUrl(self, BoardUrl):
        self._BoardUrl = BoardUrl

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def BoardW(self):
        return self._BoardW

    @BoardW.setter
    def BoardW(self, BoardW):
        self._BoardW = BoardW

    @property
    def BoardH(self):
        return self._BoardH

    @BoardH.setter
    def BoardH(self, BoardH):
        self._BoardH = BoardH

    @property
    def BoardX(self):
        return self._BoardX

    @BoardX.setter
    def BoardX(self, BoardX):
        self._BoardX = BoardX

    @property
    def BoardY(self):
        return self._BoardY

    @BoardY.setter
    def BoardY(self, BoardY):
        self._BoardY = BoardY

    @property
    def TeacherW(self):
        return self._TeacherW

    @TeacherW.setter
    def TeacherW(self, TeacherW):
        self._TeacherW = TeacherW

    @property
    def TeacherH(self):
        return self._TeacherH

    @TeacherH.setter
    def TeacherH(self, TeacherH):
        self._TeacherH = TeacherH

    @property
    def TeacherX(self):
        return self._TeacherX

    @TeacherX.setter
    def TeacherX(self, TeacherX):
        self._TeacherX = TeacherX

    @property
    def TeacherY(self):
        return self._TeacherY

    @TeacherY.setter
    def TeacherY(self, TeacherY):
        self._TeacherY = TeacherY

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TextColor(self):
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
    """SetWatermark返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class SingleStreamInfo(AbstractModel):
    """录制流信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param _StopTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StopTime: int
        :param _Duration: 总时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _FileFormat: 文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type FileFormat: str
        :param _RecordUrl: 流url
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordUrl: str
        :param _RecordSize: 流大小
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordSize: int
        :param _VideoId: 流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoId: str
        :param _Role: 流类型
注意：此字段可能返回 null，表示取不到有效值。
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
    def StopTime(self):
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FileFormat(self):
        return self._FileFormat

    @FileFormat.setter
    def FileFormat(self, FileFormat):
        self._FileFormat = FileFormat

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def RecordSize(self):
        return self._RecordSize

    @RecordSize.setter
    def RecordSize(self, RecordSize):
        self._RecordSize = RecordSize

    @property
    def VideoId(self):
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def Role(self):
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
        


class StartRoomRequest(AbstractModel):
    """StartRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoomId: 房间ID。
        :type RoomId: int
        """
        self._RoomId = None

    @property
    def RoomId(self):
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
    """StartRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class TextMarkConfig(AbstractModel):
    """文字水印配置

    """

    def __init__(self):
        r"""
        :param _Text: 文字水印内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Color: 文字水印颜色
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: str
        """
        self._Text = None
        self._Color = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Color(self):
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
    """文本消息

    """

    def __init__(self):
        r"""
        :param _Text: 文本消息。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
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
    """转存配置

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
    """UnbindDocumentFromRoom请求参数结构体

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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def DocumentId(self):
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
    """UnbindDocumentFromRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UnblockKickedUserRequest(AbstractModel):
    """UnblockKickedUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 低代码平台的SdkAppId。
        :type SdkAppId: int
        :param _RoomId: 房间Id。
        :type RoomId: int
        :param _UserId: 需要解禁踢出的成员Id。
        :type UserId: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None

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
    """UnblockKickedUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class UserInfo(AbstractModel):
    """用户信息结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppId: int
        :param _UserId: 用户Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _Name: 用户昵称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Avatar: 用户头像Url。
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _OriginId: 用户在客户系统的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginId: str
        """
        self._SdkAppId = None
        self._UserId = None
        self._Name = None
        self._Avatar = None
        self._OriginId = None

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
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def OriginId(self):
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
    """水印配置

    """

    def __init__(self):
        r"""
        :param _Url: 水印图片的url
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Width: 水印宽。为比例值
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: float
        :param _Height: 水印高。为比例值
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: float
        :param _LocationX: 水印X偏移, 取值:0-100, 表示区域X方向的百分比。比如50，则表示位于X轴中间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationX: float
        :param _LocationY: 水印Y偏移, 取值:0-100, 表示区域Y方向的百分比。比如50，则表示位于Y轴中间。
注意：此字段可能返回 null，表示取不到有效值。
        :type LocationY: float
        """
        self._Url = None
        self._Width = None
        self._Height = None
        self._LocationX = None
        self._LocationY = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

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
    def LocationX(self):
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
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
        