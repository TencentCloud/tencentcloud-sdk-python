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


class AuthorInfo(AbstractModel):
    r"""作者信息

    """

    def __init__(self):
        r"""
        :param _Id: 作者id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 作者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _SourceId: 作者来源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceId: int
        :param _FollowType: 关注类型：1-关注，2-取关
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowType: int
        :param _IconUrl: 作者头像icon地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        """
        self._Id = None
        self._Name = None
        self._SourceId = None
        self._FollowType = None
        self._IconUrl = None

    @property
    def Id(self):
        r"""作者id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""作者名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceId(self):
        r"""作者来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def FollowType(self):
        r"""关注类型：1-关注，2-取关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FollowType

    @FollowType.setter
    def FollowType(self, FollowType):
        self._FollowType = FollowType

    @property
    def IconUrl(self):
        r"""作者头像icon地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._SourceId = params.get("SourceId")
        self._FollowType = params.get("FollowType")
        self._IconUrl = params.get("IconUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DislikeInfo(AbstractModel):
    r"""不喜欢信息

    """

    def __init__(self):
        r"""
        :param _Type: 不喜欢的物料类别，对应物料上传协议中的字段名，如authorId，keyword，topic等
        :type Type: str
        :param _Value: type对应字段名的值，如具体的topic名，作者id等
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        r"""不喜欢的物料类别，对应物料上传协议中的字段名，如authorId，keyword，topic等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""type对应字段名的值，如具体的topic名，作者id等
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocBehavior(AbstractModel):
    r"""行为数据

    """

    def __init__(self):
        r"""
        :param _ItemId: 内容唯一ID，如 2824324234
        :type ItemId: str
        :param _BehaviorType: 行为类型
        :type BehaviorType: int
        :param _BehaviorValue: 行为值
        :type BehaviorValue: str
        :param _BehaviorTimestamp: 行为时间戳： 秒级时间戳（默认为当前时间）,不能延迟太久，尽量实时上报，否则会影响推荐结果的准确性。
        :type BehaviorTimestamp: int
        :param _SceneId: 场景id，在控制台创建场景后获取。
        :type SceneId: str
        :param _UserIdList: 用户id列表
        :type UserIdList: list of UserIdInfo
        :param _RecTraceId: 会话id，使用获取推荐结果中返回的RecTraceId填入。<br>注意：如果和在线推荐请求中的traceId不同，会影响行为特征归因，影响推荐算法效果
        :type RecTraceId: str
        :param _Source: 算法来源：用来区分行为来源于哪个算法。值为**business，tencent，other** 三者之一<br>● business 表示业务自己的算法对照组<br>● tencent 为腾讯算法<br>● other 为其他算法
        :type Source: str
        :param _ItemType: 物料类型
        :type ItemType: int
        :param _AppId: 微信开放平台上查看appId
        :type AppId: str
        :param _VideoPlayDuration: 回传video_over事件的时候，回传的用户播放视频的总时长（真正播放的，拖动不算，单位为秒）
        :type VideoPlayDuration: int
        :param _ReferrerItemId: 来源物料内容：用来标识在指定内容页面产生的行为，如需要统计用户在A内容详情页里，对推荐内容B点击等行为，则ReferrerItemId代表内容A，ItemId代表内容B
        :type ReferrerItemId: str
        :param _Country: 国家，统一用简写，比如中国则填写CN
        :type Country: str
        :param _Province: 省
        :type Province: str
        :param _City: 城市
        :type City: str
        :param _District: 区县
        :type District: str
        :param _IP: 客户端ip
        :type IP: str
        :param _Network: 客户端网络类型
        :type Network: str
        :param _Platform: 客户端平台，ios/android/h5
        :type Platform: str
        :param _AppVersion: 客户端app版本
        :type AppVersion: str
        :param _OsVersion: 操作系统版本
        :type OsVersion: str
        :param _DeviceModel: 机型
        :type DeviceModel: str
        :param _Extension: json字符串，用于行为数据的扩展
        :type Extension: str
        """
        self._ItemId = None
        self._BehaviorType = None
        self._BehaviorValue = None
        self._BehaviorTimestamp = None
        self._SceneId = None
        self._UserIdList = None
        self._RecTraceId = None
        self._Source = None
        self._ItemType = None
        self._AppId = None
        self._VideoPlayDuration = None
        self._ReferrerItemId = None
        self._Country = None
        self._Province = None
        self._City = None
        self._District = None
        self._IP = None
        self._Network = None
        self._Platform = None
        self._AppVersion = None
        self._OsVersion = None
        self._DeviceModel = None
        self._Extension = None

    @property
    def ItemId(self):
        r"""内容唯一ID，如 2824324234
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def BehaviorType(self):
        r"""行为类型
        :rtype: int
        """
        return self._BehaviorType

    @BehaviorType.setter
    def BehaviorType(self, BehaviorType):
        self._BehaviorType = BehaviorType

    @property
    def BehaviorValue(self):
        r"""行为值
        :rtype: str
        """
        return self._BehaviorValue

    @BehaviorValue.setter
    def BehaviorValue(self, BehaviorValue):
        self._BehaviorValue = BehaviorValue

    @property
    def BehaviorTimestamp(self):
        r"""行为时间戳： 秒级时间戳（默认为当前时间）,不能延迟太久，尽量实时上报，否则会影响推荐结果的准确性。
        :rtype: int
        """
        return self._BehaviorTimestamp

    @BehaviorTimestamp.setter
    def BehaviorTimestamp(self, BehaviorTimestamp):
        self._BehaviorTimestamp = BehaviorTimestamp

    @property
    def SceneId(self):
        r"""场景id，在控制台创建场景后获取。
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def UserIdList(self):
        r"""用户id列表
        :rtype: list of UserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def RecTraceId(self):
        r"""会话id，使用获取推荐结果中返回的RecTraceId填入。<br>注意：如果和在线推荐请求中的traceId不同，会影响行为特征归因，影响推荐算法效果
        :rtype: str
        """
        return self._RecTraceId

    @RecTraceId.setter
    def RecTraceId(self, RecTraceId):
        self._RecTraceId = RecTraceId

    @property
    def Source(self):
        r"""算法来源：用来区分行为来源于哪个算法。值为**business，tencent，other** 三者之一<br>● business 表示业务自己的算法对照组<br>● tencent 为腾讯算法<br>● other 为其他算法
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def ItemType(self):
        r"""物料类型
        :rtype: int
        """
        return self._ItemType

    @ItemType.setter
    def ItemType(self, ItemType):
        self._ItemType = ItemType

    @property
    def AppId(self):
        r"""微信开放平台上查看appId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def VideoPlayDuration(self):
        r"""回传video_over事件的时候，回传的用户播放视频的总时长（真正播放的，拖动不算，单位为秒）
        :rtype: int
        """
        return self._VideoPlayDuration

    @VideoPlayDuration.setter
    def VideoPlayDuration(self, VideoPlayDuration):
        self._VideoPlayDuration = VideoPlayDuration

    @property
    def ReferrerItemId(self):
        r"""来源物料内容：用来标识在指定内容页面产生的行为，如需要统计用户在A内容详情页里，对推荐内容B点击等行为，则ReferrerItemId代表内容A，ItemId代表内容B
        :rtype: str
        """
        return self._ReferrerItemId

    @ReferrerItemId.setter
    def ReferrerItemId(self, ReferrerItemId):
        self._ReferrerItemId = ReferrerItemId

    @property
    def Country(self):
        r"""国家，统一用简写，比如中国则填写CN
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        r"""省
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        r"""城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        r"""区县
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def IP(self):
        r"""客户端ip
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Network(self):
        r"""客户端网络类型
        :rtype: str
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Platform(self):
        r"""客户端平台，ios/android/h5
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def AppVersion(self):
        r"""客户端app版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def OsVersion(self):
        r"""操作系统版本
        :rtype: str
        """
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def DeviceModel(self):
        r"""机型
        :rtype: str
        """
        return self._DeviceModel

    @DeviceModel.setter
    def DeviceModel(self, DeviceModel):
        self._DeviceModel = DeviceModel

    @property
    def Extension(self):
        r"""json字符串，用于行为数据的扩展
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._BehaviorType = params.get("BehaviorType")
        self._BehaviorValue = params.get("BehaviorValue")
        self._BehaviorTimestamp = params.get("BehaviorTimestamp")
        self._SceneId = params.get("SceneId")
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        self._RecTraceId = params.get("RecTraceId")
        self._Source = params.get("Source")
        self._ItemType = params.get("ItemType")
        self._AppId = params.get("AppId")
        self._VideoPlayDuration = params.get("VideoPlayDuration")
        self._ReferrerItemId = params.get("ReferrerItemId")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._District = params.get("District")
        self._IP = params.get("IP")
        self._Network = params.get("Network")
        self._Platform = params.get("Platform")
        self._AppVersion = params.get("AppVersion")
        self._OsVersion = params.get("OsVersion")
        self._DeviceModel = params.get("DeviceModel")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocItem(AbstractModel):
    r"""推荐物料信息

    """

    def __init__(self):
        r"""
        :param _ItemId: 内容唯一id
        :type ItemId: str
        :param _ItemType: 内容类型
        :type ItemType: int
        :param _Status: 内容状态：1 - 上架， 2 - 下架
        :type Status: int
        :param _PublishTimestamp: 内容生成时间，秒级时间戳（1639624786），需大于0
        :type PublishTimestamp: int
        :param _SourceId: 物料来源ID
        :type SourceId: int
        :param _Title: 标题名称
        :type Title: str
        :param _Content: 内容正文
        :type Content: str
        :param _Author: 作者
        :type Author: str
        :param _AuthorId: 作者id
        :type AuthorId: str
        :param _Keyword: 标签关键词，多个用英文分号分割
        :type Keyword: str
        :param _Desc: 内容物料描述：物料的描述信息，推荐系统会对内容的描述信息，使用否LP技术，进行分词、提取关键词，作为news的特征使用。
        :type Desc: str
        :param _PicUrlList: 图片url
        :type PicUrlList: list of str
        :param _VideoUrlList: 视频url
        :type VideoUrlList: list of str
        :param _VideoDuration: 视频时长，时间秒
        :type VideoDuration: int
        :param _CategoryLevel: 类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配
        :type CategoryLevel: int
        :param _CategoryPath: 类目路径，一级二级三级等依次用英文冒号联接，如体育：“足球:巴塞罗那”
        :type CategoryPath: str
        :param _Country: 国家，统一用简写，比如中国则填写CN
        :type Country: str
        :param _Province: 省
        :type Province: str
        :param _City: 城市
        :type City: str
        :param _District: 区县
        :type District: str
        :param _ExpireTimestamp: 内容过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年
        :type ExpireTimestamp: int
        :param _Topic: 所属话题
        :type Topic: str
        :param _AuthorFans: 作者粉丝数
        :type AuthorFans: int
        :param _AuthorLevel: 作者评级
        :type AuthorLevel: str
        :param _CollectCnt: 内容累计收藏次数
        :type CollectCnt: int
        :param _PraiseCnt: 内容累积点赞次数
        :type PraiseCnt: int
        :param _CommentCnt: 内容累计评论次数
        :type CommentCnt: int
        :param _ShareCnt: 内容累计分享次数
        :type ShareCnt: int
        :param _RewardCnt: 内容累积打赏数
        :type RewardCnt: int
        :param _Score: 内容质量评分，类似豆瓣电影的评分，这里为100分制，比如97分，满分100分，最低0分，范围外的将会被拦截
        :type Score: float
        :param _PoolIdList: 内容池id，用于分内容池召回，一个内容支持指定一个或多个内容池， 内容池id不建议使用0（0表示不区分内容池）
        :type PoolIdList: list of str
        :param _TagInfoList: 描述用户标签
        :type TagInfoList: list of TagInfo
        :param _Extension: json字符串，用于物料数据的扩展
        :type Extension: str
        """
        self._ItemId = None
        self._ItemType = None
        self._Status = None
        self._PublishTimestamp = None
        self._SourceId = None
        self._Title = None
        self._Content = None
        self._Author = None
        self._AuthorId = None
        self._Keyword = None
        self._Desc = None
        self._PicUrlList = None
        self._VideoUrlList = None
        self._VideoDuration = None
        self._CategoryLevel = None
        self._CategoryPath = None
        self._Country = None
        self._Province = None
        self._City = None
        self._District = None
        self._ExpireTimestamp = None
        self._Topic = None
        self._AuthorFans = None
        self._AuthorLevel = None
        self._CollectCnt = None
        self._PraiseCnt = None
        self._CommentCnt = None
        self._ShareCnt = None
        self._RewardCnt = None
        self._Score = None
        self._PoolIdList = None
        self._TagInfoList = None
        self._Extension = None

    @property
    def ItemId(self):
        r"""内容唯一id
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ItemType(self):
        r"""内容类型
        :rtype: int
        """
        return self._ItemType

    @ItemType.setter
    def ItemType(self, ItemType):
        self._ItemType = ItemType

    @property
    def Status(self):
        r"""内容状态：1 - 上架， 2 - 下架
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PublishTimestamp(self):
        r"""内容生成时间，秒级时间戳（1639624786），需大于0
        :rtype: int
        """
        return self._PublishTimestamp

    @PublishTimestamp.setter
    def PublishTimestamp(self, PublishTimestamp):
        self._PublishTimestamp = PublishTimestamp

    @property
    def SourceId(self):
        r"""物料来源ID
        :rtype: int
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Title(self):
        r"""标题名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        r"""内容正文
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Author(self):
        r"""作者
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def AuthorId(self):
        r"""作者id
        :rtype: str
        """
        return self._AuthorId

    @AuthorId.setter
    def AuthorId(self, AuthorId):
        self._AuthorId = AuthorId

    @property
    def Keyword(self):
        r"""标签关键词，多个用英文分号分割
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Desc(self):
        r"""内容物料描述：物料的描述信息，推荐系统会对内容的描述信息，使用否LP技术，进行分词、提取关键词，作为news的特征使用。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def PicUrlList(self):
        r"""图片url
        :rtype: list of str
        """
        return self._PicUrlList

    @PicUrlList.setter
    def PicUrlList(self, PicUrlList):
        self._PicUrlList = PicUrlList

    @property
    def VideoUrlList(self):
        r"""视频url
        :rtype: list of str
        """
        return self._VideoUrlList

    @VideoUrlList.setter
    def VideoUrlList(self, VideoUrlList):
        self._VideoUrlList = VideoUrlList

    @property
    def VideoDuration(self):
        r"""视频时长，时间秒
        :rtype: int
        """
        return self._VideoDuration

    @VideoDuration.setter
    def VideoDuration(self, VideoDuration):
        self._VideoDuration = VideoDuration

    @property
    def CategoryLevel(self):
        r"""类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配
        :rtype: int
        """
        return self._CategoryLevel

    @CategoryLevel.setter
    def CategoryLevel(self, CategoryLevel):
        self._CategoryLevel = CategoryLevel

    @property
    def CategoryPath(self):
        r"""类目路径，一级二级三级等依次用英文冒号联接，如体育：“足球:巴塞罗那”
        :rtype: str
        """
        return self._CategoryPath

    @CategoryPath.setter
    def CategoryPath(self, CategoryPath):
        self._CategoryPath = CategoryPath

    @property
    def Country(self):
        r"""国家，统一用简写，比如中国则填写CN
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        r"""省
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        r"""城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def District(self):
        r"""区县
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def ExpireTimestamp(self):
        r"""内容过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年
        :rtype: int
        """
        return self._ExpireTimestamp

    @ExpireTimestamp.setter
    def ExpireTimestamp(self, ExpireTimestamp):
        self._ExpireTimestamp = ExpireTimestamp

    @property
    def Topic(self):
        r"""所属话题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def AuthorFans(self):
        r"""作者粉丝数
        :rtype: int
        """
        return self._AuthorFans

    @AuthorFans.setter
    def AuthorFans(self, AuthorFans):
        self._AuthorFans = AuthorFans

    @property
    def AuthorLevel(self):
        r"""作者评级
        :rtype: str
        """
        return self._AuthorLevel

    @AuthorLevel.setter
    def AuthorLevel(self, AuthorLevel):
        self._AuthorLevel = AuthorLevel

    @property
    def CollectCnt(self):
        r"""内容累计收藏次数
        :rtype: int
        """
        return self._CollectCnt

    @CollectCnt.setter
    def CollectCnt(self, CollectCnt):
        self._CollectCnt = CollectCnt

    @property
    def PraiseCnt(self):
        r"""内容累积点赞次数
        :rtype: int
        """
        return self._PraiseCnt

    @PraiseCnt.setter
    def PraiseCnt(self, PraiseCnt):
        self._PraiseCnt = PraiseCnt

    @property
    def CommentCnt(self):
        r"""内容累计评论次数
        :rtype: int
        """
        return self._CommentCnt

    @CommentCnt.setter
    def CommentCnt(self, CommentCnt):
        self._CommentCnt = CommentCnt

    @property
    def ShareCnt(self):
        r"""内容累计分享次数
        :rtype: int
        """
        return self._ShareCnt

    @ShareCnt.setter
    def ShareCnt(self, ShareCnt):
        self._ShareCnt = ShareCnt

    @property
    def RewardCnt(self):
        r"""内容累积打赏数
        :rtype: int
        """
        return self._RewardCnt

    @RewardCnt.setter
    def RewardCnt(self, RewardCnt):
        self._RewardCnt = RewardCnt

    @property
    def Score(self):
        r"""内容质量评分，类似豆瓣电影的评分，这里为100分制，比如97分，满分100分，最低0分，范围外的将会被拦截
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def PoolIdList(self):
        r"""内容池id，用于分内容池召回，一个内容支持指定一个或多个内容池， 内容池id不建议使用0（0表示不区分内容池）
        :rtype: list of str
        """
        return self._PoolIdList

    @PoolIdList.setter
    def PoolIdList(self, PoolIdList):
        self._PoolIdList = PoolIdList

    @property
    def TagInfoList(self):
        r"""描述用户标签
        :rtype: list of TagInfo
        """
        return self._TagInfoList

    @TagInfoList.setter
    def TagInfoList(self, TagInfoList):
        self._TagInfoList = TagInfoList

    @property
    def Extension(self):
        r"""json字符串，用于物料数据的扩展
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._ItemType = params.get("ItemType")
        self._Status = params.get("Status")
        self._PublishTimestamp = params.get("PublishTimestamp")
        self._SourceId = params.get("SourceId")
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._Author = params.get("Author")
        self._AuthorId = params.get("AuthorId")
        self._Keyword = params.get("Keyword")
        self._Desc = params.get("Desc")
        self._PicUrlList = params.get("PicUrlList")
        self._VideoUrlList = params.get("VideoUrlList")
        self._VideoDuration = params.get("VideoDuration")
        self._CategoryLevel = params.get("CategoryLevel")
        self._CategoryPath = params.get("CategoryPath")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._District = params.get("District")
        self._ExpireTimestamp = params.get("ExpireTimestamp")
        self._Topic = params.get("Topic")
        self._AuthorFans = params.get("AuthorFans")
        self._AuthorLevel = params.get("AuthorLevel")
        self._CollectCnt = params.get("CollectCnt")
        self._PraiseCnt = params.get("PraiseCnt")
        self._CommentCnt = params.get("CommentCnt")
        self._ShareCnt = params.get("ShareCnt")
        self._RewardCnt = params.get("RewardCnt")
        self._Score = params.get("Score")
        self._PoolIdList = params.get("PoolIdList")
        if params.get("TagInfoList") is not None:
            self._TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagInfoList.append(obj)
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortraitInfo(AbstractModel):
    r"""画像信息

    """

    def __init__(self):
        r"""
        :param _UserIdList: 用户id列表
        :type UserIdList: list of UserIdInfo
        :param _AppId: 如果"userIdType"是10则必传，在微信开放平台上查看appId
        :type AppId: str
        :param _Age: 用户年龄，值域在 0-200
        :type Age: int
        :param _Gender: 用户性别：0-未知，1-男， 2-女
        :type Gender: int
        :param _Degree: 用户学历 ：小学，初中，高中，大专，本科，硕士，博士
        :type Degree: str
        :param _School: 用户毕业学校全称
        :type School: str
        :param _Occupation: 用户职业，保证业务的唯一性
        :type Occupation: str
        :param _Industry: 用户所属行业，保证业务的唯一性
        :type Industry: str
        :param _ResidentCountry: 用户常驻国家，统一用简写，比如中国则填写CN
        :type ResidentCountry: str
        :param _ResidentProvince: 用户常驻省份
        :type ResidentProvince: str
        :param _ResidentCity: 用户常驻城市
        :type ResidentCity: str
        :param _ResidentDistrict: 用户常驻区县
        :type ResidentDistrict: str
        :param _PhoneMd5: 用户手机的MD5值
        :type PhoneMd5: str
        :param _PhoneImei: 用户手机的IMEI号
        :type PhoneImei: str
        :param _Idfa: 设备idfa信息
        :type Idfa: str
        :param _RegisterTimestamp: 用户注册时间，秒级时间戳（1639624786）
        :type RegisterTimestamp: int
        :param _MembershipLevel: 用户会员等级
        :type MembershipLevel: str
        :param _LastLoginTimestamp: 用户上一次登录时间，秒级时间戳（1639624786）
        :type LastLoginTimestamp: int
        :param _LastLoginIp: 用户上一次登录的ip
        :type LastLoginIp: str
        :param _LastModifyTimestamp: 用户信息的最后修改时间戳，秒级时间戳（1639624786）
        :type LastModifyTimestamp: int
        :param _TagInfoList: 用户标签
        :type TagInfoList: list of TagInfo
        :param _AuthorInfoList: 用户关注作者列表
        :type AuthorInfoList: list of AuthorInfo
        :param _DislikeInfoList: 用户不喜欢列表
        :type DislikeInfoList: list of DislikeInfo
        :param _Extension: json字符串，用于画像数据的扩展
        :type Extension: str
        :param _Oaid: 设备oaid信息
        :type Oaid: str
        :param _AndroidId: 设备AndroidId信息
        :type AndroidId: str
        """
        self._UserIdList = None
        self._AppId = None
        self._Age = None
        self._Gender = None
        self._Degree = None
        self._School = None
        self._Occupation = None
        self._Industry = None
        self._ResidentCountry = None
        self._ResidentProvince = None
        self._ResidentCity = None
        self._ResidentDistrict = None
        self._PhoneMd5 = None
        self._PhoneImei = None
        self._Idfa = None
        self._RegisterTimestamp = None
        self._MembershipLevel = None
        self._LastLoginTimestamp = None
        self._LastLoginIp = None
        self._LastModifyTimestamp = None
        self._TagInfoList = None
        self._AuthorInfoList = None
        self._DislikeInfoList = None
        self._Extension = None
        self._Oaid = None
        self._AndroidId = None

    @property
    def UserIdList(self):
        r"""用户id列表
        :rtype: list of UserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def AppId(self):
        r"""如果"userIdType"是10则必传，在微信开放平台上查看appId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Age(self):
        r"""用户年龄，值域在 0-200
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Gender(self):
        r"""用户性别：0-未知，1-男， 2-女
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Degree(self):
        r"""用户学历 ：小学，初中，高中，大专，本科，硕士，博士
        :rtype: str
        """
        return self._Degree

    @Degree.setter
    def Degree(self, Degree):
        self._Degree = Degree

    @property
    def School(self):
        r"""用户毕业学校全称
        :rtype: str
        """
        return self._School

    @School.setter
    def School(self, School):
        self._School = School

    @property
    def Occupation(self):
        r"""用户职业，保证业务的唯一性
        :rtype: str
        """
        return self._Occupation

    @Occupation.setter
    def Occupation(self, Occupation):
        self._Occupation = Occupation

    @property
    def Industry(self):
        r"""用户所属行业，保证业务的唯一性
        :rtype: str
        """
        return self._Industry

    @Industry.setter
    def Industry(self, Industry):
        self._Industry = Industry

    @property
    def ResidentCountry(self):
        r"""用户常驻国家，统一用简写，比如中国则填写CN
        :rtype: str
        """
        return self._ResidentCountry

    @ResidentCountry.setter
    def ResidentCountry(self, ResidentCountry):
        self._ResidentCountry = ResidentCountry

    @property
    def ResidentProvince(self):
        r"""用户常驻省份
        :rtype: str
        """
        return self._ResidentProvince

    @ResidentProvince.setter
    def ResidentProvince(self, ResidentProvince):
        self._ResidentProvince = ResidentProvince

    @property
    def ResidentCity(self):
        r"""用户常驻城市
        :rtype: str
        """
        return self._ResidentCity

    @ResidentCity.setter
    def ResidentCity(self, ResidentCity):
        self._ResidentCity = ResidentCity

    @property
    def ResidentDistrict(self):
        r"""用户常驻区县
        :rtype: str
        """
        return self._ResidentDistrict

    @ResidentDistrict.setter
    def ResidentDistrict(self, ResidentDistrict):
        self._ResidentDistrict = ResidentDistrict

    @property
    def PhoneMd5(self):
        r"""用户手机的MD5值
        :rtype: str
        """
        return self._PhoneMd5

    @PhoneMd5.setter
    def PhoneMd5(self, PhoneMd5):
        self._PhoneMd5 = PhoneMd5

    @property
    def PhoneImei(self):
        r"""用户手机的IMEI号
        :rtype: str
        """
        return self._PhoneImei

    @PhoneImei.setter
    def PhoneImei(self, PhoneImei):
        self._PhoneImei = PhoneImei

    @property
    def Idfa(self):
        r"""设备idfa信息
        :rtype: str
        """
        return self._Idfa

    @Idfa.setter
    def Idfa(self, Idfa):
        self._Idfa = Idfa

    @property
    def RegisterTimestamp(self):
        r"""用户注册时间，秒级时间戳（1639624786）
        :rtype: int
        """
        return self._RegisterTimestamp

    @RegisterTimestamp.setter
    def RegisterTimestamp(self, RegisterTimestamp):
        self._RegisterTimestamp = RegisterTimestamp

    @property
    def MembershipLevel(self):
        r"""用户会员等级
        :rtype: str
        """
        return self._MembershipLevel

    @MembershipLevel.setter
    def MembershipLevel(self, MembershipLevel):
        self._MembershipLevel = MembershipLevel

    @property
    def LastLoginTimestamp(self):
        r"""用户上一次登录时间，秒级时间戳（1639624786）
        :rtype: int
        """
        return self._LastLoginTimestamp

    @LastLoginTimestamp.setter
    def LastLoginTimestamp(self, LastLoginTimestamp):
        self._LastLoginTimestamp = LastLoginTimestamp

    @property
    def LastLoginIp(self):
        r"""用户上一次登录的ip
        :rtype: str
        """
        return self._LastLoginIp

    @LastLoginIp.setter
    def LastLoginIp(self, LastLoginIp):
        self._LastLoginIp = LastLoginIp

    @property
    def LastModifyTimestamp(self):
        r"""用户信息的最后修改时间戳，秒级时间戳（1639624786）
        :rtype: int
        """
        return self._LastModifyTimestamp

    @LastModifyTimestamp.setter
    def LastModifyTimestamp(self, LastModifyTimestamp):
        self._LastModifyTimestamp = LastModifyTimestamp

    @property
    def TagInfoList(self):
        r"""用户标签
        :rtype: list of TagInfo
        """
        return self._TagInfoList

    @TagInfoList.setter
    def TagInfoList(self, TagInfoList):
        self._TagInfoList = TagInfoList

    @property
    def AuthorInfoList(self):
        r"""用户关注作者列表
        :rtype: list of AuthorInfo
        """
        return self._AuthorInfoList

    @AuthorInfoList.setter
    def AuthorInfoList(self, AuthorInfoList):
        self._AuthorInfoList = AuthorInfoList

    @property
    def DislikeInfoList(self):
        r"""用户不喜欢列表
        :rtype: list of DislikeInfo
        """
        return self._DislikeInfoList

    @DislikeInfoList.setter
    def DislikeInfoList(self, DislikeInfoList):
        self._DislikeInfoList = DislikeInfoList

    @property
    def Extension(self):
        r"""json字符串，用于画像数据的扩展
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension

    @property
    def Oaid(self):
        r"""设备oaid信息
        :rtype: str
        """
        return self._Oaid

    @Oaid.setter
    def Oaid(self, Oaid):
        self._Oaid = Oaid

    @property
    def AndroidId(self):
        r"""设备AndroidId信息
        :rtype: str
        """
        return self._AndroidId

    @AndroidId.setter
    def AndroidId(self, AndroidId):
        self._AndroidId = AndroidId


    def _deserialize(self, params):
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        self._AppId = params.get("AppId")
        self._Age = params.get("Age")
        self._Gender = params.get("Gender")
        self._Degree = params.get("Degree")
        self._School = params.get("School")
        self._Occupation = params.get("Occupation")
        self._Industry = params.get("Industry")
        self._ResidentCountry = params.get("ResidentCountry")
        self._ResidentProvince = params.get("ResidentProvince")
        self._ResidentCity = params.get("ResidentCity")
        self._ResidentDistrict = params.get("ResidentDistrict")
        self._PhoneMd5 = params.get("PhoneMd5")
        self._PhoneImei = params.get("PhoneImei")
        self._Idfa = params.get("Idfa")
        self._RegisterTimestamp = params.get("RegisterTimestamp")
        self._MembershipLevel = params.get("MembershipLevel")
        self._LastLoginTimestamp = params.get("LastLoginTimestamp")
        self._LastLoginIp = params.get("LastLoginIp")
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        if params.get("TagInfoList") is not None:
            self._TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagInfoList.append(obj)
        if params.get("AuthorInfoList") is not None:
            self._AuthorInfoList = []
            for item in params.get("AuthorInfoList"):
                obj = AuthorInfo()
                obj._deserialize(item)
                self._AuthorInfoList.append(obj)
        if params.get("DislikeInfoList") is not None:
            self._DislikeInfoList = []
            for item in params.get("DislikeInfoList"):
                obj = DislikeInfo()
                obj._deserialize(item)
                self._DislikeInfoList.append(obj)
        self._Extension = params.get("Extension")
        self._Oaid = params.get("Oaid")
        self._AndroidId = params.get("AndroidId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecItemData(AbstractModel):
    r"""推荐内容信息

    """

    def __init__(self):
        r"""
        :param _ItemId: 推荐的内容id，即用户行为上报中的itemId
        :type ItemId: str
        :param _ItemType: 物料子类型，包括如下： 1-图文、2-长视频（横视频）、3-短视频（横视频）、4-小说、5-小视频（竖视频）、6-纯文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemType: int
        :param _Weight: 推荐内容的权重，取值范围[0,1000000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _Score: 推荐预测分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        :param _Keyword: 关键词，多个用英文分号分割，和物料上传的keyword一致
注意：此字段可能返回 null，表示取不到有效值。
        :type Keyword: str
        """
        self._ItemId = None
        self._ItemType = None
        self._Weight = None
        self._Score = None
        self._Keyword = None

    @property
    def ItemId(self):
        r"""推荐的内容id，即用户行为上报中的itemId
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ItemType(self):
        r"""物料子类型，包括如下： 1-图文、2-长视频（横视频）、3-短视频（横视频）、4-小说、5-小视频（竖视频）、6-纯文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ItemType

    @ItemType.setter
    def ItemType(self, ItemType):
        self._ItemType = ItemType

    @property
    def Weight(self):
        r"""推荐内容的权重，取值范围[0,1000000]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Score(self):
        r"""推荐预测分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Keyword(self):
        r"""关键词，多个用英文分号分割，和物料上传的keyword一致
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._ItemType = params.get("ItemType")
        self._Weight = params.get("Weight")
        self._Score = params.get("Score")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecommendContentRequest(AbstractModel):
    r"""RecommendContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Bid: 业务id
        :type Bid: str
        :param _SceneId: 场景id：比如有“猜你喜欢”，“热门内容”等推荐模块，每一个模块都有一个scene_id来表示。 在控制台创建场景后获取。需要跟行为上报时的id一致
        :type SceneId: str
        :param _UserIdList: 用户唯一ID数组，每个数组元素详见userId结构体，若不填，则接口返回热门结果
        :type UserIdList: list of UserIdInfo
        :param _RecTraceId: 会话id：必须和行为数据上报时所填写的traceId相同，用于行为数据来自于那次在线推荐请求的归因。**注意：此处如果没传，则响应会返回一个全局唯一ID返回给客户，并需客户透传给行为日志上报接口**
        :type RecTraceId: str
        :param _ItemCnt: 推荐数量：物料优选的结果， 默认50个，目前最多支持200个的内容返回，如果返回个数更多，会影响性能，容易超时。
        :type ItemCnt: int
        :param _PoolId: 物料池id，用于召回该pool_id下的商品，如果有多个，用英文;分割。**注意：此处poolId需和物料上报时的poolIdList对应上**
        :type PoolId: str
        :param _CurrentItemId: 来源物料id，即用户当前浏览的物料id，用于在内容详情页获取关联推荐内容
        :type CurrentItemId: str
        :param _ResponseTimeout: 请求响应超时时间，单位ms，默认300ms，数值设置的过小，会影响推荐效果，最小支持250ms
        :type ResponseTimeout: int
        :param _ItemTypeRatio: 返回结果中不同物料类型的比例，比例顺序需严格按照（图文，长视频，短视频，小视频）进行。只允许传[0,100]数字，多个请用**英文冒号**分割，且加起来不能超过100，以及比例数量不能超过**场景绑定的物料类型**（图文，长视频，短视频，小视频）数。**示例：**图文和短视频比例为40%:60%时，则填40:60图文和短视频比例为0%:100%时，则填0:100图文，长视频和短视频的比例为，图文占20%，剩余80%由长视频和短视频随机返回，则填20:80或仅填20均可
        :type ItemTypeRatio: str
        """
        self._Bid = None
        self._SceneId = None
        self._UserIdList = None
        self._RecTraceId = None
        self._ItemCnt = None
        self._PoolId = None
        self._CurrentItemId = None
        self._ResponseTimeout = None
        self._ItemTypeRatio = None

    @property
    def Bid(self):
        r"""业务id
        :rtype: str
        """
        return self._Bid

    @Bid.setter
    def Bid(self, Bid):
        self._Bid = Bid

    @property
    def SceneId(self):
        r"""场景id：比如有“猜你喜欢”，“热门内容”等推荐模块，每一个模块都有一个scene_id来表示。 在控制台创建场景后获取。需要跟行为上报时的id一致
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def UserIdList(self):
        r"""用户唯一ID数组，每个数组元素详见userId结构体，若不填，则接口返回热门结果
        :rtype: list of UserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def RecTraceId(self):
        r"""会话id：必须和行为数据上报时所填写的traceId相同，用于行为数据来自于那次在线推荐请求的归因。**注意：此处如果没传，则响应会返回一个全局唯一ID返回给客户，并需客户透传给行为日志上报接口**
        :rtype: str
        """
        return self._RecTraceId

    @RecTraceId.setter
    def RecTraceId(self, RecTraceId):
        self._RecTraceId = RecTraceId

    @property
    def ItemCnt(self):
        r"""推荐数量：物料优选的结果， 默认50个，目前最多支持200个的内容返回，如果返回个数更多，会影响性能，容易超时。
        :rtype: int
        """
        return self._ItemCnt

    @ItemCnt.setter
    def ItemCnt(self, ItemCnt):
        self._ItemCnt = ItemCnt

    @property
    def PoolId(self):
        r"""物料池id，用于召回该pool_id下的商品，如果有多个，用英文;分割。**注意：此处poolId需和物料上报时的poolIdList对应上**
        :rtype: str
        """
        return self._PoolId

    @PoolId.setter
    def PoolId(self, PoolId):
        self._PoolId = PoolId

    @property
    def CurrentItemId(self):
        r"""来源物料id，即用户当前浏览的物料id，用于在内容详情页获取关联推荐内容
        :rtype: str
        """
        return self._CurrentItemId

    @CurrentItemId.setter
    def CurrentItemId(self, CurrentItemId):
        self._CurrentItemId = CurrentItemId

    @property
    def ResponseTimeout(self):
        r"""请求响应超时时间，单位ms，默认300ms，数值设置的过小，会影响推荐效果，最小支持250ms
        :rtype: int
        """
        return self._ResponseTimeout

    @ResponseTimeout.setter
    def ResponseTimeout(self, ResponseTimeout):
        self._ResponseTimeout = ResponseTimeout

    @property
    def ItemTypeRatio(self):
        r"""返回结果中不同物料类型的比例，比例顺序需严格按照（图文，长视频，短视频，小视频）进行。只允许传[0,100]数字，多个请用**英文冒号**分割，且加起来不能超过100，以及比例数量不能超过**场景绑定的物料类型**（图文，长视频，短视频，小视频）数。**示例：**图文和短视频比例为40%:60%时，则填40:60图文和短视频比例为0%:100%时，则填0:100图文，长视频和短视频的比例为，图文占20%，剩余80%由长视频和短视频随机返回，则填20:80或仅填20均可
        :rtype: str
        """
        return self._ItemTypeRatio

    @ItemTypeRatio.setter
    def ItemTypeRatio(self, ItemTypeRatio):
        self._ItemTypeRatio = ItemTypeRatio


    def _deserialize(self, params):
        self._Bid = params.get("Bid")
        self._SceneId = params.get("SceneId")
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        self._RecTraceId = params.get("RecTraceId")
        self._ItemCnt = params.get("ItemCnt")
        self._PoolId = params.get("PoolId")
        self._CurrentItemId = params.get("CurrentItemId")
        self._ResponseTimeout = params.get("ResponseTimeout")
        self._ItemTypeRatio = params.get("ItemTypeRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecommendContentResponse(AbstractModel):
    r"""RecommendContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecTraceId: 推荐追踪id，用于行为上报。每次接口调用返回的traceId不同
        :type RecTraceId: str
        :param _DataList: 标识具体的物料信息
        :type DataList: list of RecItemData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecTraceId = None
        self._DataList = None
        self._RequestId = None

    @property
    def RecTraceId(self):
        r"""推荐追踪id，用于行为上报。每次接口调用返回的traceId不同
        :rtype: str
        """
        return self._RecTraceId

    @RecTraceId.setter
    def RecTraceId(self, RecTraceId):
        self._RecTraceId = RecTraceId

    @property
    def DataList(self):
        r"""标识具体的物料信息
        :rtype: list of RecItemData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecTraceId = params.get("RecTraceId")
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = RecItemData()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._RequestId = params.get("RequestId")


class ReportActionRequest(AbstractModel):
    r"""ReportAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Bid: 业务id
        :type Bid: str
        :param _DocBehaviorList: 上报的行为对象数组，数量不超过50
        :type DocBehaviorList: list of DocBehavior
        """
        self._Bid = None
        self._DocBehaviorList = None

    @property
    def Bid(self):
        r"""业务id
        :rtype: str
        """
        return self._Bid

    @Bid.setter
    def Bid(self, Bid):
        self._Bid = Bid

    @property
    def DocBehaviorList(self):
        r"""上报的行为对象数组，数量不超过50
        :rtype: list of DocBehavior
        """
        return self._DocBehaviorList

    @DocBehaviorList.setter
    def DocBehaviorList(self, DocBehaviorList):
        self._DocBehaviorList = DocBehaviorList


    def _deserialize(self, params):
        self._Bid = params.get("Bid")
        if params.get("DocBehaviorList") is not None:
            self._DocBehaviorList = []
            for item in params.get("DocBehaviorList"):
                obj = DocBehavior()
                obj._deserialize(item)
                self._DocBehaviorList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportActionResponse(AbstractModel):
    r"""ReportAction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReportMaterialRequest(AbstractModel):
    r"""ReportMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Bid: 业务id
        :type Bid: str
        :param _DocItemList: 上报的信息流数组，一次数量不超过50
        :type DocItemList: list of DocItem
        """
        self._Bid = None
        self._DocItemList = None

    @property
    def Bid(self):
        r"""业务id
        :rtype: str
        """
        return self._Bid

    @Bid.setter
    def Bid(self, Bid):
        self._Bid = Bid

    @property
    def DocItemList(self):
        r"""上报的信息流数组，一次数量不超过50
        :rtype: list of DocItem
        """
        return self._DocItemList

    @DocItemList.setter
    def DocItemList(self, DocItemList):
        self._DocItemList = DocItemList


    def _deserialize(self, params):
        self._Bid = params.get("Bid")
        if params.get("DocItemList") is not None:
            self._DocItemList = []
            for item in params.get("DocItemList"):
                obj = DocItem()
                obj._deserialize(item)
                self._DocItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportMaterialResponse(AbstractModel):
    r"""ReportMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReportPortraitRequest(AbstractModel):
    r"""ReportPortrait请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Bid: 推荐平台上的业务id
        :type Bid: str
        :param _PortraitList: 上报的用户画像数组，数量不超过50
        :type PortraitList: list of PortraitInfo
        """
        self._Bid = None
        self._PortraitList = None

    @property
    def Bid(self):
        r"""推荐平台上的业务id
        :rtype: str
        """
        return self._Bid

    @Bid.setter
    def Bid(self, Bid):
        self._Bid = Bid

    @property
    def PortraitList(self):
        r"""上报的用户画像数组，数量不超过50
        :rtype: list of PortraitInfo
        """
        return self._PortraitList

    @PortraitList.setter
    def PortraitList(self, PortraitList):
        self._PortraitList = PortraitList


    def _deserialize(self, params):
        self._Bid = params.get("Bid")
        if params.get("PortraitList") is not None:
            self._PortraitList = []
            for item in params.get("PortraitList"):
                obj = PortraitInfo()
                obj._deserialize(item)
                self._PortraitList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportPortraitResponse(AbstractModel):
    r"""ReportPortrait返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    r"""标题信息

    """

    def __init__(self):
        r"""
        :param _Id: 标签id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Name: 标签名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Weight: 推荐权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: float
        """
        self._Id = None
        self._Name = None
        self._Weight = None

    @property
    def Id(self):
        r"""标签id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""标签名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Weight(self):
        r"""推荐权重
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserIdInfo(AbstractModel):
    r"""用户信息

    """

    def __init__(self):
        r"""
        :param _UserIdType: 用户ID类型：
1 - qq
2 - qq_md5：md5后的qq
3 - imei：设备imei（安卓10之后不会再授权imei，安卓10之后的imei映射关系可能拿不到，故安卓10之后的设备建议用oaid）
4 - imei_md5：md5后的imei
5 - idfa: Apple 向用户设备随机分配的设备标识符
6 - idfa_md5：md5之后的idfa
7 - gdt_openid：广点通生成的openid
8 - oaid：安卓10之后一种非永久性设备标识符
9 - oaid_md5：md5后的oaid
10 - wx_openid：微信openid
11 - qq_openid：QQ的openid
12 - phone：电话号码
13 - phone_md5：md5后的电话号码
14 - phone_sha256：SHA256加密的手机号
15 - phone_sm3：国密SM3加密的手机号
1000 - 客户自定义id
        :type UserIdType: int
        :param _UserId: 用户id
        :type UserId: str
        """
        self._UserIdType = None
        self._UserId = None

    @property
    def UserIdType(self):
        r"""用户ID类型：
1 - qq
2 - qq_md5：md5后的qq
3 - imei：设备imei（安卓10之后不会再授权imei，安卓10之后的imei映射关系可能拿不到，故安卓10之后的设备建议用oaid）
4 - imei_md5：md5后的imei
5 - idfa: Apple 向用户设备随机分配的设备标识符
6 - idfa_md5：md5之后的idfa
7 - gdt_openid：广点通生成的openid
8 - oaid：安卓10之后一种非永久性设备标识符
9 - oaid_md5：md5后的oaid
10 - wx_openid：微信openid
11 - qq_openid：QQ的openid
12 - phone：电话号码
13 - phone_md5：md5后的电话号码
14 - phone_sha256：SHA256加密的手机号
15 - phone_sm3：国密SM3加密的手机号
1000 - 客户自定义id
        :rtype: int
        """
        return self._UserIdType

    @UserIdType.setter
    def UserIdType(self, UserIdType):
        self._UserIdType = UserIdType

    @property
    def UserId(self):
        r"""用户id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserIdType = params.get("UserIdType")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        