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


class DescribeGoodsRecommendRequest(AbstractModel):
    r"""DescribeGoodsRecommend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param _SceneId: 场景ID，在控制台创建场景后获取
        :type SceneId: str
        :param _UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识，需和行为数据上报接口中的UserId一致，否则影响特征关联
        :type UserId: str
        :param _UserIdList: 用户设备ID数组，可传入用户的多个类型ID，用于关联画像信息
        :type UserIdList: list of StrUserIdInfo
        :param _GoodsCnt: 推荐返回数量，默认10个，最多支持50个的内容返回。如果有更多数量要求，<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决
        :type GoodsCnt: int
        :param _CurrentGoodsId: 当场景是相关推荐时该值必填，场景是非相关推荐时该值无效
        :type CurrentGoodsId: str
        :param _UserPortraitInfo: 用户的实时特征信息，用作特征
        :type UserPortraitInfo: :class:`tencentcloud.irp.v20220805.models.UserPortraitInfo`
        :param _BlackGoodsList: 本次请求针对该用户需要过滤的物品列表(不超过100个)
        :type BlackGoodsList: list of str
        :param _Extension: json字符串，扩展字段
        :type Extension: str
        """
        self._InstanceId = None
        self._SceneId = None
        self._UserId = None
        self._UserIdList = None
        self._GoodsCnt = None
        self._CurrentGoodsId = None
        self._UserPortraitInfo = None
        self._BlackGoodsList = None
        self._Extension = None

    @property
    def InstanceId(self):
        r"""实例ID，在控制台获取
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SceneId(self):
        r"""场景ID，在控制台创建场景后获取
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def UserId(self):
        r"""用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识，需和行为数据上报接口中的UserId一致，否则影响特征关联
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIdList(self):
        r"""用户设备ID数组，可传入用户的多个类型ID，用于关联画像信息
        :rtype: list of StrUserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def GoodsCnt(self):
        r"""推荐返回数量，默认10个，最多支持50个的内容返回。如果有更多数量要求，<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决
        :rtype: int
        """
        return self._GoodsCnt

    @GoodsCnt.setter
    def GoodsCnt(self, GoodsCnt):
        self._GoodsCnt = GoodsCnt

    @property
    def CurrentGoodsId(self):
        r"""当场景是相关推荐时该值必填，场景是非相关推荐时该值无效
        :rtype: str
        """
        return self._CurrentGoodsId

    @CurrentGoodsId.setter
    def CurrentGoodsId(self, CurrentGoodsId):
        self._CurrentGoodsId = CurrentGoodsId

    @property
    def UserPortraitInfo(self):
        r"""用户的实时特征信息，用作特征
        :rtype: :class:`tencentcloud.irp.v20220805.models.UserPortraitInfo`
        """
        return self._UserPortraitInfo

    @UserPortraitInfo.setter
    def UserPortraitInfo(self, UserPortraitInfo):
        self._UserPortraitInfo = UserPortraitInfo

    @property
    def BlackGoodsList(self):
        r"""本次请求针对该用户需要过滤的物品列表(不超过100个)
        :rtype: list of str
        """
        return self._BlackGoodsList

    @BlackGoodsList.setter
    def BlackGoodsList(self, BlackGoodsList):
        self._BlackGoodsList = BlackGoodsList

    @property
    def Extension(self):
        r"""json字符串，扩展字段
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SceneId = params.get("SceneId")
        self._UserId = params.get("UserId")
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = StrUserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        self._GoodsCnt = params.get("GoodsCnt")
        self._CurrentGoodsId = params.get("CurrentGoodsId")
        if params.get("UserPortraitInfo") is not None:
            self._UserPortraitInfo = UserPortraitInfo()
            self._UserPortraitInfo._deserialize(params.get("UserPortraitInfo"))
        self._BlackGoodsList = params.get("BlackGoodsList")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGoodsRecommendResponse(AbstractModel):
    r"""DescribeGoodsRecommend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataList: 推荐返回的商品信息列表
        :type DataList: list of RecGoodsData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataList = None
        self._RequestId = None

    @property
    def DataList(self):
        r"""推荐返回的商品信息列表
        :rtype: list of RecGoodsData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

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
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = RecGoodsData()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._RequestId = params.get("RequestId")


class DislikeInfo(AbstractModel):
    r"""不喜欢信息

    """

    def __init__(self):
        r"""
        :param _Type: 过滤的类别：<br>● author 作者名<br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :type Type: str
        :param _Value: Type对应字段名的值，如：需要过滤的作者名
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        r"""过滤的类别：<br>● author 作者名<br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""Type对应字段名的值，如：需要过滤的作者名
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
        


class DocItem(AbstractModel):
    r"""信息流内容

    """

    def __init__(self):
        r"""
        :param _ItemId: 内容唯一id，建议限制在128字符以内
        :type ItemId: str
        :param _ItemType: 内容类型：<br/>● article -图文<br>● text -纯文本<br/>● video -视频<br/>● short_video -时长15秒以内的视频<br/>● mini_video -竖屏视频<br/>● image -纯图片<br/>（如当前类型不满足，请登录控制台进入对应项目，在<b>物料管理->物料类型管理</b>中添加）
        :type ItemType: str
        :param _Status: 内容状态：
● 1 - 上架 
● 2 - 下架 
Status=2的内容不会在推荐结果中出现 
需要下架内容时，把Status的值修改为2即可
        :type Status: int
        :param _PublishTimestamp: 内容生成时间，秒级时间戳（1639624786），需大于0，<b>用作特征和物料管理</b>
        :type PublishTimestamp: int
        :param _ExpireTimestamp: 内容过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年，用作特征，过期则不会被推荐，<b>强烈建议</b>
        :type ExpireTimestamp: int
        :param _CategoryLevel: 类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配，<b>强烈建议</b>
        :type CategoryLevel: int
        :param _CategoryPath: 类目路径，一级二级三级等依次用英文冒号联接，和CategoryLevel字段值匹配，如体育：“足球:巴塞罗那”。<b>用于物料池管理，强烈建议</b>
        :type CategoryPath: str
        :param _Tags: 内容标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :type Tags: str
        :param _Author: 作者名，需保证作者名唯一，若有重名需要加编号区分。<b>用于召回过滤、规则打散，强烈建议</b>
        :type Author: str
        :param _SourceId: 内容来源类型，客户自定义，<b>用于物料池管理</b>
        :type SourceId: str
        :param _Title: 内容标题，<b>主要用于语义分析</b>
        :type Title: str
        :param _Content: 正文关键片段，建议控制在500字符以内，<b>主要用于语义分析</b>
        :type Content: str
        :param _ContentUrl: 正文详情，主要用于语义分析，当内容过大时建议用ContentUrl传递，<b>与Content可二选一</b>
        :type ContentUrl: str
        :param _VideoDuration: 视频时长，时间秒，大于等于0，小于 3600 * 10。<b>视频内容必填，其它内容非必填，用作特征</b>
        :type VideoDuration: int
        :param _Country: 国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :type Country: str
        :param _Province: 省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :type Province: str
        :param _City: 城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :type City: str
        :param _AuthorFans: 作者粉丝数，<b>用作特征</b>
        :type AuthorFans: int
        :param _AuthorLevel: 作者评级，<b>用作特征</b>
        :type AuthorLevel: str
        :param _CollectCnt: 内容累计收藏次数，<b>用作特征</b>
        :type CollectCnt: int
        :param _PraiseCnt: 内容累积点赞次数，<b>用作特征</b>
        :type PraiseCnt: int
        :param _CommentCnt: 内容累计评论次数，<b>用作特征</b>
        :type CommentCnt: int
        :param _ShareCnt: 内容累计分享次数，<b>用作特征</b>
        :type ShareCnt: int
        :param _RewardCnt: 内容累积打赏数，<b>用作特征</b>
        :type RewardCnt: int
        :param _Score: 内容质量评分，<b>用作特征</b>
        :type Score: float
        :param _Extension: json字符串，<b>用于物料池管理的自定义扩展</b>，需要base64加密
        :type Extension: str
        """
        self._ItemId = None
        self._ItemType = None
        self._Status = None
        self._PublishTimestamp = None
        self._ExpireTimestamp = None
        self._CategoryLevel = None
        self._CategoryPath = None
        self._Tags = None
        self._Author = None
        self._SourceId = None
        self._Title = None
        self._Content = None
        self._ContentUrl = None
        self._VideoDuration = None
        self._Country = None
        self._Province = None
        self._City = None
        self._AuthorFans = None
        self._AuthorLevel = None
        self._CollectCnt = None
        self._PraiseCnt = None
        self._CommentCnt = None
        self._ShareCnt = None
        self._RewardCnt = None
        self._Score = None
        self._Extension = None

    @property
    def ItemId(self):
        r"""内容唯一id，建议限制在128字符以内
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ItemType(self):
        r"""内容类型：<br/>● article -图文<br>● text -纯文本<br/>● video -视频<br/>● short_video -时长15秒以内的视频<br/>● mini_video -竖屏视频<br/>● image -纯图片<br/>（如当前类型不满足，请登录控制台进入对应项目，在<b>物料管理->物料类型管理</b>中添加）
        :rtype: str
        """
        return self._ItemType

    @ItemType.setter
    def ItemType(self, ItemType):
        self._ItemType = ItemType

    @property
    def Status(self):
        r"""内容状态：
● 1 - 上架 
● 2 - 下架 
Status=2的内容不会在推荐结果中出现 
需要下架内容时，把Status的值修改为2即可
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PublishTimestamp(self):
        r"""内容生成时间，秒级时间戳（1639624786），需大于0，<b>用作特征和物料管理</b>
        :rtype: int
        """
        return self._PublishTimestamp

    @PublishTimestamp.setter
    def PublishTimestamp(self, PublishTimestamp):
        self._PublishTimestamp = PublishTimestamp

    @property
    def ExpireTimestamp(self):
        r"""内容过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年，用作特征，过期则不会被推荐，<b>强烈建议</b>
        :rtype: int
        """
        return self._ExpireTimestamp

    @ExpireTimestamp.setter
    def ExpireTimestamp(self, ExpireTimestamp):
        self._ExpireTimestamp = ExpireTimestamp

    @property
    def CategoryLevel(self):
        r"""类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配，<b>强烈建议</b>
        :rtype: int
        """
        return self._CategoryLevel

    @CategoryLevel.setter
    def CategoryLevel(self, CategoryLevel):
        self._CategoryLevel = CategoryLevel

    @property
    def CategoryPath(self):
        r"""类目路径，一级二级三级等依次用英文冒号联接，和CategoryLevel字段值匹配，如体育：“足球:巴塞罗那”。<b>用于物料池管理，强烈建议</b>
        :rtype: str
        """
        return self._CategoryPath

    @CategoryPath.setter
    def CategoryPath(self, CategoryPath):
        self._CategoryPath = CategoryPath

    @property
    def Tags(self):
        r"""内容标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Author(self):
        r"""作者名，需保证作者名唯一，若有重名需要加编号区分。<b>用于召回过滤、规则打散，强烈建议</b>
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def SourceId(self):
        r"""内容来源类型，客户自定义，<b>用于物料池管理</b>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Title(self):
        r"""内容标题，<b>主要用于语义分析</b>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        r"""正文关键片段，建议控制在500字符以内，<b>主要用于语义分析</b>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentUrl(self):
        r"""正文详情，主要用于语义分析，当内容过大时建议用ContentUrl传递，<b>与Content可二选一</b>
        :rtype: str
        """
        return self._ContentUrl

    @ContentUrl.setter
    def ContentUrl(self, ContentUrl):
        self._ContentUrl = ContentUrl

    @property
    def VideoDuration(self):
        r"""视频时长，时间秒，大于等于0，小于 3600 * 10。<b>视频内容必填，其它内容非必填，用作特征</b>
        :rtype: int
        """
        return self._VideoDuration

    @VideoDuration.setter
    def VideoDuration(self, VideoDuration):
        self._VideoDuration = VideoDuration

    @property
    def Country(self):
        r"""国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        r"""省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        r"""城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def AuthorFans(self):
        r"""作者粉丝数，<b>用作特征</b>
        :rtype: int
        """
        return self._AuthorFans

    @AuthorFans.setter
    def AuthorFans(self, AuthorFans):
        self._AuthorFans = AuthorFans

    @property
    def AuthorLevel(self):
        r"""作者评级，<b>用作特征</b>
        :rtype: str
        """
        return self._AuthorLevel

    @AuthorLevel.setter
    def AuthorLevel(self, AuthorLevel):
        self._AuthorLevel = AuthorLevel

    @property
    def CollectCnt(self):
        r"""内容累计收藏次数，<b>用作特征</b>
        :rtype: int
        """
        return self._CollectCnt

    @CollectCnt.setter
    def CollectCnt(self, CollectCnt):
        self._CollectCnt = CollectCnt

    @property
    def PraiseCnt(self):
        r"""内容累积点赞次数，<b>用作特征</b>
        :rtype: int
        """
        return self._PraiseCnt

    @PraiseCnt.setter
    def PraiseCnt(self, PraiseCnt):
        self._PraiseCnt = PraiseCnt

    @property
    def CommentCnt(self):
        r"""内容累计评论次数，<b>用作特征</b>
        :rtype: int
        """
        return self._CommentCnt

    @CommentCnt.setter
    def CommentCnt(self, CommentCnt):
        self._CommentCnt = CommentCnt

    @property
    def ShareCnt(self):
        r"""内容累计分享次数，<b>用作特征</b>
        :rtype: int
        """
        return self._ShareCnt

    @ShareCnt.setter
    def ShareCnt(self, ShareCnt):
        self._ShareCnt = ShareCnt

    @property
    def RewardCnt(self):
        r"""内容累积打赏数，<b>用作特征</b>
        :rtype: int
        """
        return self._RewardCnt

    @RewardCnt.setter
    def RewardCnt(self, RewardCnt):
        self._RewardCnt = RewardCnt

    @property
    def Score(self):
        r"""内容质量评分，<b>用作特征</b>
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Extension(self):
        r"""json字符串，<b>用于物料池管理的自定义扩展</b>，需要base64加密
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
        self._ExpireTimestamp = params.get("ExpireTimestamp")
        self._CategoryLevel = params.get("CategoryLevel")
        self._CategoryPath = params.get("CategoryPath")
        self._Tags = params.get("Tags")
        self._Author = params.get("Author")
        self._SourceId = params.get("SourceId")
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._ContentUrl = params.get("ContentUrl")
        self._VideoDuration = params.get("VideoDuration")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._AuthorFans = params.get("AuthorFans")
        self._AuthorLevel = params.get("AuthorLevel")
        self._CollectCnt = params.get("CollectCnt")
        self._PraiseCnt = params.get("PraiseCnt")
        self._CommentCnt = params.get("CommentCnt")
        self._ShareCnt = params.get("ShareCnt")
        self._RewardCnt = params.get("RewardCnt")
        self._Score = params.get("Score")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeedBehaviorInfo(AbstractModel):
    r"""信息流行为

    """

    def __init__(self):
        r"""
        :param _UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :type UserId: str
        :param _ItemId: 内容唯一id
        :type ItemId: str
        :param _BehaviorType: 行为类型：<br> ● expose - 曝光，<b>必须</b><br> ● click - 点击，<b>必须</b><br/>  ● stay - 详情页停留时长，<b>强烈建议</b><br/>  ● videoover - 视频播放时长，<b>强烈建议</b><br/> ●  like - 点赞&喜欢，<b>正效果</b><br/> ● collect - 收藏，<b>正效果</b><br/> ●  share - 转发&分享，<b>正效果</b><br/> ● reward - 打赏，<b>正效果</b><br/> ● unlike - 踩&不喜欢，<b>负效果</b><br/> ●  comment - 评论<br/> 不支持的行为类型，可以映射到未被使用的其他行为类型。如实际业务数据中有私信行为，没有收藏行为，可以将私信行为映射到收藏行为
        :type BehaviorType: str
        :param _BehaviorValue: 行为类型对应的行为值：<br/> ● expose - 曝光，固定填1<br/> ● click - 点击，固定填1<br/>  ● stay - 详情页停留时长，填停留秒数，取值[1-86400]<br/>  ● videoover - 视频播放时长，填播放结束的秒数，取值[1-86400]<br/> ●  like - 点赞&喜欢，固定填1<br/> ● collect - 收藏，固定填1<br/> ●  share - 转发&分享，固定填1<br/> ● reward - 打赏，填打赏金额，没有则填1<br/> ● unlike - 踩&不喜欢，填不喜欢的原因，没有则填1<br/> ●  comment - 评论，填评论内容，如“上海加油”
        :type BehaviorValue: str
        :param _BehaviorTimestamp: 行为发生的时间戳： 秒级时间戳，尽量实时上报，最长不超过半小时否则会影响推荐结果的准确性
        :type BehaviorTimestamp: int
        :param _SceneId: 行为发生的场景ID，在控制台创建场景后获取
        :type SceneId: str
        :param _ItemTraceId: 推荐追踪ID，使用推荐结果中返回的ItemTraceId填入。 
注意：如果和推荐结果中的ItemTraceId不同，会影响行为特征归因，影响推荐算法效果
        :type ItemTraceId: str
        :param _ItemType: 内容类型，跟内容上报类型一致，用于效果分析，不做内容校验，<b>强烈建议</b>
        :type ItemType: str
        :param _ReferrerItemId: 相关推荐场景点击进入详情页的内容id，该字段用来注明行为发生于哪个内容的详情页推荐中，<b>相关推荐场景强烈建议</b>
        :type ReferrerItemId: str
        :param _UserIdList: 用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :type UserIdList: list of UserIdInfo
        :param _Source: 算法来源： <br>● business 业务自己的算法对照组<br/> ● tencent 腾讯算法<br/> ● other 其他算法<br/>默认为tencent，区分行为来源于哪个算法，<b>用于Poc阶段的效果对比验证</b>
        :type Source: str
        :param _Country: 行为发生时的国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :type Country: str
        :param _Province: 行为发生时的省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :type Province: str
        :param _City: 行为发生时的城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :type City: str
        :param _IP: 行为发生时的客户端ip，<b>用作特征</b>
        :type IP: str
        :param _Network: 行为发生时的客户端网络类型，<b>用作特征</b>
        :type Network: str
        :param _Platform: 行为发生时的客户端平台，ios/android/h5，<b>用作特征</b>
        :type Platform: str
        :param _AppVersion: 行为发生时的客户端app版本，<b>用作特征</b>
        :type AppVersion: str
        :param _OsVersion: 行为发生时的操作系统版本，<b>用作特征</b>
        :type OsVersion: str
        :param _DeviceModel: 行为发生时的机型，<b>用作特征</b>
        :type DeviceModel: str
        :param _Extension: json字符串，<b>用于行为数据的扩展</b>，需要base64加密
        :type Extension: str
        """
        self._UserId = None
        self._ItemId = None
        self._BehaviorType = None
        self._BehaviorValue = None
        self._BehaviorTimestamp = None
        self._SceneId = None
        self._ItemTraceId = None
        self._ItemType = None
        self._ReferrerItemId = None
        self._UserIdList = None
        self._Source = None
        self._Country = None
        self._Province = None
        self._City = None
        self._IP = None
        self._Network = None
        self._Platform = None
        self._AppVersion = None
        self._OsVersion = None
        self._DeviceModel = None
        self._Extension = None

    @property
    def UserId(self):
        r"""用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

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
    def BehaviorType(self):
        r"""行为类型：<br> ● expose - 曝光，<b>必须</b><br> ● click - 点击，<b>必须</b><br/>  ● stay - 详情页停留时长，<b>强烈建议</b><br/>  ● videoover - 视频播放时长，<b>强烈建议</b><br/> ●  like - 点赞&喜欢，<b>正效果</b><br/> ● collect - 收藏，<b>正效果</b><br/> ●  share - 转发&分享，<b>正效果</b><br/> ● reward - 打赏，<b>正效果</b><br/> ● unlike - 踩&不喜欢，<b>负效果</b><br/> ●  comment - 评论<br/> 不支持的行为类型，可以映射到未被使用的其他行为类型。如实际业务数据中有私信行为，没有收藏行为，可以将私信行为映射到收藏行为
        :rtype: str
        """
        return self._BehaviorType

    @BehaviorType.setter
    def BehaviorType(self, BehaviorType):
        self._BehaviorType = BehaviorType

    @property
    def BehaviorValue(self):
        r"""行为类型对应的行为值：<br/> ● expose - 曝光，固定填1<br/> ● click - 点击，固定填1<br/>  ● stay - 详情页停留时长，填停留秒数，取值[1-86400]<br/>  ● videoover - 视频播放时长，填播放结束的秒数，取值[1-86400]<br/> ●  like - 点赞&喜欢，固定填1<br/> ● collect - 收藏，固定填1<br/> ●  share - 转发&分享，固定填1<br/> ● reward - 打赏，填打赏金额，没有则填1<br/> ● unlike - 踩&不喜欢，填不喜欢的原因，没有则填1<br/> ●  comment - 评论，填评论内容，如“上海加油”
        :rtype: str
        """
        return self._BehaviorValue

    @BehaviorValue.setter
    def BehaviorValue(self, BehaviorValue):
        self._BehaviorValue = BehaviorValue

    @property
    def BehaviorTimestamp(self):
        r"""行为发生的时间戳： 秒级时间戳，尽量实时上报，最长不超过半小时否则会影响推荐结果的准确性
        :rtype: int
        """
        return self._BehaviorTimestamp

    @BehaviorTimestamp.setter
    def BehaviorTimestamp(self, BehaviorTimestamp):
        self._BehaviorTimestamp = BehaviorTimestamp

    @property
    def SceneId(self):
        r"""行为发生的场景ID，在控制台创建场景后获取
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def ItemTraceId(self):
        r"""推荐追踪ID，使用推荐结果中返回的ItemTraceId填入。 
注意：如果和推荐结果中的ItemTraceId不同，会影响行为特征归因，影响推荐算法效果
        :rtype: str
        """
        return self._ItemTraceId

    @ItemTraceId.setter
    def ItemTraceId(self, ItemTraceId):
        self._ItemTraceId = ItemTraceId

    @property
    def ItemType(self):
        r"""内容类型，跟内容上报类型一致，用于效果分析，不做内容校验，<b>强烈建议</b>
        :rtype: str
        """
        return self._ItemType

    @ItemType.setter
    def ItemType(self, ItemType):
        self._ItemType = ItemType

    @property
    def ReferrerItemId(self):
        r"""相关推荐场景点击进入详情页的内容id，该字段用来注明行为发生于哪个内容的详情页推荐中，<b>相关推荐场景强烈建议</b>
        :rtype: str
        """
        return self._ReferrerItemId

    @ReferrerItemId.setter
    def ReferrerItemId(self, ReferrerItemId):
        self._ReferrerItemId = ReferrerItemId

    @property
    def UserIdList(self):
        r"""用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :rtype: list of UserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def Source(self):
        r"""算法来源： <br>● business 业务自己的算法对照组<br/> ● tencent 腾讯算法<br/> ● other 其他算法<br/>默认为tencent，区分行为来源于哪个算法，<b>用于Poc阶段的效果对比验证</b>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Country(self):
        r"""行为发生时的国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        r"""行为发生时的省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        r"""行为发生时的城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def IP(self):
        r"""行为发生时的客户端ip，<b>用作特征</b>
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Network(self):
        r"""行为发生时的客户端网络类型，<b>用作特征</b>
        :rtype: str
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Platform(self):
        r"""行为发生时的客户端平台，ios/android/h5，<b>用作特征</b>
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def AppVersion(self):
        r"""行为发生时的客户端app版本，<b>用作特征</b>
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def OsVersion(self):
        r"""行为发生时的操作系统版本，<b>用作特征</b>
        :rtype: str
        """
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def DeviceModel(self):
        r"""行为发生时的机型，<b>用作特征</b>
        :rtype: str
        """
        return self._DeviceModel

    @DeviceModel.setter
    def DeviceModel(self, DeviceModel):
        self._DeviceModel = DeviceModel

    @property
    def Extension(self):
        r"""json字符串，<b>用于行为数据的扩展</b>，需要base64加密
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._ItemId = params.get("ItemId")
        self._BehaviorType = params.get("BehaviorType")
        self._BehaviorValue = params.get("BehaviorValue")
        self._BehaviorTimestamp = params.get("BehaviorTimestamp")
        self._SceneId = params.get("SceneId")
        self._ItemTraceId = params.get("ItemTraceId")
        self._ItemType = params.get("ItemType")
        self._ReferrerItemId = params.get("ReferrerItemId")
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        self._Source = params.get("Source")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
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
        


class FeedRecommendRequest(AbstractModel):
    r"""FeedRecommend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param _SceneId: 场景ID，在控制台创建场景后获取
        :type SceneId: str
        :param _UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :type UserId: str
        :param _UserIdList: 用户设备ID数组，可传入用户的多个类型ID，用于关联画像信息
        :type UserIdList: list of UserIdInfo
        :param _ItemCnt: 推荐返回数量，默认10个，最多支持50个的内容返回。如果有更多数量要求，<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决
        :type ItemCnt: int
        :param _CurrentItemId: 当场景是相关推荐时该值必填，场景是非相关推荐时该值无效
        :type CurrentItemId: str
        :param _Extension: 扩展字段，json字符串，需要base64加密
        :type Extension: str
        """
        self._InstanceId = None
        self._SceneId = None
        self._UserId = None
        self._UserIdList = None
        self._ItemCnt = None
        self._CurrentItemId = None
        self._Extension = None

    @property
    def InstanceId(self):
        r"""实例ID，在控制台获取
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SceneId(self):
        r"""场景ID，在控制台创建场景后获取
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def UserId(self):
        r"""用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIdList(self):
        r"""用户设备ID数组，可传入用户的多个类型ID，用于关联画像信息
        :rtype: list of UserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def ItemCnt(self):
        r"""推荐返回数量，默认10个，最多支持50个的内容返回。如果有更多数量要求，<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决
        :rtype: int
        """
        return self._ItemCnt

    @ItemCnt.setter
    def ItemCnt(self, ItemCnt):
        self._ItemCnt = ItemCnt

    @property
    def CurrentItemId(self):
        r"""当场景是相关推荐时该值必填，场景是非相关推荐时该值无效
        :rtype: str
        """
        return self._CurrentItemId

    @CurrentItemId.setter
    def CurrentItemId(self, CurrentItemId):
        self._CurrentItemId = CurrentItemId

    @property
    def Extension(self):
        r"""扩展字段，json字符串，需要base64加密
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SceneId = params.get("SceneId")
        self._UserId = params.get("UserId")
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        self._ItemCnt = params.get("ItemCnt")
        self._CurrentItemId = params.get("CurrentItemId")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeedRecommendResponse(AbstractModel):
    r"""FeedRecommend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataList: 推荐返回的内容信息列表，返回结果已按策略规则做好了排序
        :type DataList: list of RecItemData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataList = None
        self._RequestId = None

    @property
    def DataList(self):
        r"""推荐返回的内容信息列表，返回结果已按策略规则做好了排序
        :rtype: list of RecItemData
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

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
        if params.get("DataList") is not None:
            self._DataList = []
            for item in params.get("DataList"):
                obj = RecItemData()
                obj._deserialize(item)
                self._DataList.append(obj)
        self._RequestId = params.get("RequestId")


class FeedUserInfo(AbstractModel):
    r"""信息流用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :type UserId: str
        :param _UserIdList: 用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :type UserIdList: list of UserIdInfo
        :param _Tags: 用户标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :type Tags: str
        :param _DislikeInfoList: 过滤列表，<b>会在推荐结果里过滤掉这类内容</b>
        :type DislikeInfoList: list of DislikeInfo
        :param _Age: 用户年龄
        :type Age: int
        :param _Gender: 用户性别： 0 - 未知 1 - 男 2 - 女
        :type Gender: int
        :param _Degree: 用户学历 ：小学，初中，高中，大专，本科，硕士，博士
        :type Degree: str
        :param _School: 用户毕业学校全称
        :type School: str
        :param _Occupation: 用户职业
        :type Occupation: str
        :param _Industry: 用户所属行业
        :type Industry: str
        :param _ResidentCountry: 用户常驻国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”
        :type ResidentCountry: str
        :param _ResidentProvince: 用户常驻省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”
        :type ResidentProvince: str
        :param _ResidentCity: 用户常驻城市，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，
        :type ResidentCity: str
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
        :param _Extension: json字符串，用于画像数据的扩展，需要base64加密
        :type Extension: str
        """
        self._UserId = None
        self._UserIdList = None
        self._Tags = None
        self._DislikeInfoList = None
        self._Age = None
        self._Gender = None
        self._Degree = None
        self._School = None
        self._Occupation = None
        self._Industry = None
        self._ResidentCountry = None
        self._ResidentProvince = None
        self._ResidentCity = None
        self._RegisterTimestamp = None
        self._MembershipLevel = None
        self._LastLoginTimestamp = None
        self._LastLoginIp = None
        self._LastModifyTimestamp = None
        self._Extension = None

    @property
    def UserId(self):
        r"""用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIdList(self):
        r"""用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :rtype: list of UserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def Tags(self):
        r"""用户标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DislikeInfoList(self):
        r"""过滤列表，<b>会在推荐结果里过滤掉这类内容</b>
        :rtype: list of DislikeInfo
        """
        return self._DislikeInfoList

    @DislikeInfoList.setter
    def DislikeInfoList(self, DislikeInfoList):
        self._DislikeInfoList = DislikeInfoList

    @property
    def Age(self):
        r"""用户年龄
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Gender(self):
        r"""用户性别： 0 - 未知 1 - 男 2 - 女
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
        r"""用户职业
        :rtype: str
        """
        return self._Occupation

    @Occupation.setter
    def Occupation(self, Occupation):
        self._Occupation = Occupation

    @property
    def Industry(self):
        r"""用户所属行业
        :rtype: str
        """
        return self._Industry

    @Industry.setter
    def Industry(self, Industry):
        self._Industry = Industry

    @property
    def ResidentCountry(self):
        r"""用户常驻国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”
        :rtype: str
        """
        return self._ResidentCountry

    @ResidentCountry.setter
    def ResidentCountry(self, ResidentCountry):
        self._ResidentCountry = ResidentCountry

    @property
    def ResidentProvince(self):
        r"""用户常驻省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”
        :rtype: str
        """
        return self._ResidentProvince

    @ResidentProvince.setter
    def ResidentProvince(self, ResidentProvince):
        self._ResidentProvince = ResidentProvince

    @property
    def ResidentCity(self):
        r"""用户常驻城市，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，
        :rtype: str
        """
        return self._ResidentCity

    @ResidentCity.setter
    def ResidentCity(self, ResidentCity):
        self._ResidentCity = ResidentCity

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
    def Extension(self):
        r"""json字符串，用于画像数据的扩展，需要base64加密
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        self._Tags = params.get("Tags")
        if params.get("DislikeInfoList") is not None:
            self._DislikeInfoList = []
            for item in params.get("DislikeInfoList"):
                obj = DislikeInfo()
                obj._deserialize(item)
                self._DislikeInfoList.append(obj)
        self._Age = params.get("Age")
        self._Gender = params.get("Gender")
        self._Degree = params.get("Degree")
        self._School = params.get("School")
        self._Occupation = params.get("Occupation")
        self._Industry = params.get("Industry")
        self._ResidentCountry = params.get("ResidentCountry")
        self._ResidentProvince = params.get("ResidentProvince")
        self._ResidentCity = params.get("ResidentCity")
        self._RegisterTimestamp = params.get("RegisterTimestamp")
        self._MembershipLevel = params.get("MembershipLevel")
        self._LastLoginTimestamp = params.get("LastLoginTimestamp")
        self._LastLoginIp = params.get("LastLoginIp")
        self._LastModifyTimestamp = params.get("LastModifyTimestamp")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GoodsBehaviorInfo(AbstractModel):
    r"""电商行为

    """

    def __init__(self):
        r"""
        :param _UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :type UserId: str
        :param _GoodsId: 商品唯一ID，skuId或spuId，客户根据需求自行决定商品主键粒度
        :type GoodsId: str
        :param _BehaviorType: 行为类型：<br> ● expose - 曝光，<b>必须</b><br> ● click - 点击，<b>必须</b><br/>  ● stay - 详情页停留时长，<b>强烈建议</b><br/>  ● videoover - 视频播放时长，<b>强烈建议</b><br/> ●  like - 点赞&喜欢，<b>正效果</b><br/> ● collect - 收藏，<b>正效果</b><br/> ●  share - 转发&分享，<b>正效果</b><br/> ● reward - 打赏，<b>正效果</b><br/> ● unlike - 踩&不喜欢，<b>负效果</b><br/> ●  comment - 评论<br/> ●  order - 下单<br/> ●  buy - 购买成功<br/> ●  addcart - 加入购物车<br/>   
不支持的行为类型，可以映射到未被使用的其他行为类型。如实际业务数据中有私信行为，没有收藏行为，可以将私信行为映射到收藏行为
        :type BehaviorType: str
        :param _BehaviorValue: 行为类型对应的行为值：<br/> ● expose - 曝光，固定填1<br/> ● click - 点击，固定填1<br/>  ● stay - 详情页停留时长，填停留秒数，取值[1-86400]<br/>  ● videoover - 视频播放时长，填播放结束的秒数，取值[1-86400]<br/> ●  like - 点赞&喜欢，固定填1<br/> ● collect - 收藏，固定填1<br/> ●  share - 转发&分享，固定填1<br/> ● reward - 打赏，填打赏金额，没有则填1<br/> ● unlike - 踩&不喜欢，填不喜欢的原因，没有则填1<br/> ●  comment - 评论，填评论内容，如“上海加油”<br/> ●  order - 下单，固定填1<br/> ●  buy - 购买成功，固定填1<br/> ●  addcart - 加入购物车，固定填1
        :type BehaviorValue: str
        :param _BehaviorTimestamp: 行为发生的时间戳： 秒级时间戳，尽量实时上报，最长不超过半小时否则会影响推荐结果的准确性
        :type BehaviorTimestamp: int
        :param _SceneId: 行为发生的场景ID，在控制台创建场景后获取
        :type SceneId: str
        :param _Source: 算法来源： <br>● business 业务自己的算法对照组<br/> ● tencent 腾讯算法<br/> ● other 其他算法<br/>默认为tencent，区分行为来源于哪个算法，<b>用于Poc阶段的效果对比验证</b>
        :type Source: str
        :param _Page: 标识行为发生在app内哪个页面，取值客户自定，可以是明文或id，建议传明文便于理解、分析，如首页，发现页，用户中心等
<b>用作上下文特征，刻画不同场景用户行为分布的差异</b>
        :type Page: str
        :param _Module: 标识行为发生在页面的哪一区块，取值客户自定，可以是明文或id，建议传明文便于理解、分析，如横幅、广告位、猜你喜欢等
<b>用作上下文特征，刻画不同模块用户行为分布的差异</b>
        :type Module: str
        :param _GoodsTraceId: 推荐追踪ID，使用推荐结果中返回的GoodsTraceId填入。 
注意：如果和推荐结果中的GoodsTraceId不同，会影响行为特征归因，影响推荐算法效果。<b>强烈建议</b>
        :type GoodsTraceId: str
        :param _ReferrerGoodsId: 相关推荐场景点击进入详情页的内容id，该字段用来注明行为发生于哪个内容的详情页推荐中，<b>相关推荐场景强烈建议</b>
        :type ReferrerGoodsId: str
        :param _OrderGoodsCnt: 订单商品购买个数，当behaviorType=order，buy或addcart时有值，<b>用作特征</b>
        :type OrderGoodsCnt: int
        :param _OrderAmount: 订单总金额，当behaviorType=order或buy时有值（单位：元，统一货币体系，如统一为RMB，美元等），<b>用作特征</b>
        :type OrderAmount: float
        :param _UserIdList: 用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :type UserIdList: list of StrUserIdInfo
        :param _UserPortraitInfo: 行为发生时用户基础特征信息，<b>用作特征</b>
        :type UserPortraitInfo: :class:`tencentcloud.irp.v20220805.models.UserPortraitInfo`
        :param _Position: 标识行为发生在模块内的具体位置，如1、2、...
<b>用作上下文特征，刻画不同位置用户行为分布的差异</b>
        :type Position: int
        :param _Extension: json字符串，<b>用于行为数据的扩展</b>
        :type Extension: str
        """
        self._UserId = None
        self._GoodsId = None
        self._BehaviorType = None
        self._BehaviorValue = None
        self._BehaviorTimestamp = None
        self._SceneId = None
        self._Source = None
        self._Page = None
        self._Module = None
        self._GoodsTraceId = None
        self._ReferrerGoodsId = None
        self._OrderGoodsCnt = None
        self._OrderAmount = None
        self._UserIdList = None
        self._UserPortraitInfo = None
        self._Position = None
        self._Extension = None

    @property
    def UserId(self):
        r"""用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def GoodsId(self):
        r"""商品唯一ID，skuId或spuId，客户根据需求自行决定商品主键粒度
        :rtype: str
        """
        return self._GoodsId

    @GoodsId.setter
    def GoodsId(self, GoodsId):
        self._GoodsId = GoodsId

    @property
    def BehaviorType(self):
        r"""行为类型：<br> ● expose - 曝光，<b>必须</b><br> ● click - 点击，<b>必须</b><br/>  ● stay - 详情页停留时长，<b>强烈建议</b><br/>  ● videoover - 视频播放时长，<b>强烈建议</b><br/> ●  like - 点赞&喜欢，<b>正效果</b><br/> ● collect - 收藏，<b>正效果</b><br/> ●  share - 转发&分享，<b>正效果</b><br/> ● reward - 打赏，<b>正效果</b><br/> ● unlike - 踩&不喜欢，<b>负效果</b><br/> ●  comment - 评论<br/> ●  order - 下单<br/> ●  buy - 购买成功<br/> ●  addcart - 加入购物车<br/>   
不支持的行为类型，可以映射到未被使用的其他行为类型。如实际业务数据中有私信行为，没有收藏行为，可以将私信行为映射到收藏行为
        :rtype: str
        """
        return self._BehaviorType

    @BehaviorType.setter
    def BehaviorType(self, BehaviorType):
        self._BehaviorType = BehaviorType

    @property
    def BehaviorValue(self):
        r"""行为类型对应的行为值：<br/> ● expose - 曝光，固定填1<br/> ● click - 点击，固定填1<br/>  ● stay - 详情页停留时长，填停留秒数，取值[1-86400]<br/>  ● videoover - 视频播放时长，填播放结束的秒数，取值[1-86400]<br/> ●  like - 点赞&喜欢，固定填1<br/> ● collect - 收藏，固定填1<br/> ●  share - 转发&分享，固定填1<br/> ● reward - 打赏，填打赏金额，没有则填1<br/> ● unlike - 踩&不喜欢，填不喜欢的原因，没有则填1<br/> ●  comment - 评论，填评论内容，如“上海加油”<br/> ●  order - 下单，固定填1<br/> ●  buy - 购买成功，固定填1<br/> ●  addcart - 加入购物车，固定填1
        :rtype: str
        """
        return self._BehaviorValue

    @BehaviorValue.setter
    def BehaviorValue(self, BehaviorValue):
        self._BehaviorValue = BehaviorValue

    @property
    def BehaviorTimestamp(self):
        r"""行为发生的时间戳： 秒级时间戳，尽量实时上报，最长不超过半小时否则会影响推荐结果的准确性
        :rtype: int
        """
        return self._BehaviorTimestamp

    @BehaviorTimestamp.setter
    def BehaviorTimestamp(self, BehaviorTimestamp):
        self._BehaviorTimestamp = BehaviorTimestamp

    @property
    def SceneId(self):
        r"""行为发生的场景ID，在控制台创建场景后获取
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def Source(self):
        r"""算法来源： <br>● business 业务自己的算法对照组<br/> ● tencent 腾讯算法<br/> ● other 其他算法<br/>默认为tencent，区分行为来源于哪个算法，<b>用于Poc阶段的效果对比验证</b>
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Page(self):
        r"""标识行为发生在app内哪个页面，取值客户自定，可以是明文或id，建议传明文便于理解、分析，如首页，发现页，用户中心等
<b>用作上下文特征，刻画不同场景用户行为分布的差异</b>
        :rtype: str
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Module(self):
        r"""标识行为发生在页面的哪一区块，取值客户自定，可以是明文或id，建议传明文便于理解、分析，如横幅、广告位、猜你喜欢等
<b>用作上下文特征，刻画不同模块用户行为分布的差异</b>
        :rtype: str
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def GoodsTraceId(self):
        r"""推荐追踪ID，使用推荐结果中返回的GoodsTraceId填入。 
注意：如果和推荐结果中的GoodsTraceId不同，会影响行为特征归因，影响推荐算法效果。<b>强烈建议</b>
        :rtype: str
        """
        return self._GoodsTraceId

    @GoodsTraceId.setter
    def GoodsTraceId(self, GoodsTraceId):
        self._GoodsTraceId = GoodsTraceId

    @property
    def ReferrerGoodsId(self):
        r"""相关推荐场景点击进入详情页的内容id，该字段用来注明行为发生于哪个内容的详情页推荐中，<b>相关推荐场景强烈建议</b>
        :rtype: str
        """
        return self._ReferrerGoodsId

    @ReferrerGoodsId.setter
    def ReferrerGoodsId(self, ReferrerGoodsId):
        self._ReferrerGoodsId = ReferrerGoodsId

    @property
    def OrderGoodsCnt(self):
        r"""订单商品购买个数，当behaviorType=order，buy或addcart时有值，<b>用作特征</b>
        :rtype: int
        """
        return self._OrderGoodsCnt

    @OrderGoodsCnt.setter
    def OrderGoodsCnt(self, OrderGoodsCnt):
        self._OrderGoodsCnt = OrderGoodsCnt

    @property
    def OrderAmount(self):
        r"""订单总金额，当behaviorType=order或buy时有值（单位：元，统一货币体系，如统一为RMB，美元等），<b>用作特征</b>
        :rtype: float
        """
        return self._OrderAmount

    @OrderAmount.setter
    def OrderAmount(self, OrderAmount):
        self._OrderAmount = OrderAmount

    @property
    def UserIdList(self):
        r"""用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :rtype: list of StrUserIdInfo
        """
        return self._UserIdList

    @UserIdList.setter
    def UserIdList(self, UserIdList):
        self._UserIdList = UserIdList

    @property
    def UserPortraitInfo(self):
        r"""行为发生时用户基础特征信息，<b>用作特征</b>
        :rtype: :class:`tencentcloud.irp.v20220805.models.UserPortraitInfo`
        """
        return self._UserPortraitInfo

    @UserPortraitInfo.setter
    def UserPortraitInfo(self, UserPortraitInfo):
        self._UserPortraitInfo = UserPortraitInfo

    @property
    def Position(self):
        r"""标识行为发生在模块内的具体位置，如1、2、...
<b>用作上下文特征，刻画不同位置用户行为分布的差异</b>
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Extension(self):
        r"""json字符串，<b>用于行为数据的扩展</b>
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._GoodsId = params.get("GoodsId")
        self._BehaviorType = params.get("BehaviorType")
        self._BehaviorValue = params.get("BehaviorValue")
        self._BehaviorTimestamp = params.get("BehaviorTimestamp")
        self._SceneId = params.get("SceneId")
        self._Source = params.get("Source")
        self._Page = params.get("Page")
        self._Module = params.get("Module")
        self._GoodsTraceId = params.get("GoodsTraceId")
        self._ReferrerGoodsId = params.get("ReferrerGoodsId")
        self._OrderGoodsCnt = params.get("OrderGoodsCnt")
        self._OrderAmount = params.get("OrderAmount")
        if params.get("UserIdList") is not None:
            self._UserIdList = []
            for item in params.get("UserIdList"):
                obj = StrUserIdInfo()
                obj._deserialize(item)
                self._UserIdList.append(obj)
        if params.get("UserPortraitInfo") is not None:
            self._UserPortraitInfo = UserPortraitInfo()
            self._UserPortraitInfo._deserialize(params.get("UserPortraitInfo"))
        self._Position = params.get("Position")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GoodsInfo(AbstractModel):
    r"""电商物料内容

    """

    def __init__(self):
        r"""
        :param _GoodsId: 商品唯一ID，skuId或spuId，客户根据需求自行决定商品主键粒度。建议限制在128字符以内
        :type GoodsId: str
        :param _GoodsType: 商品物料展示类型：<br/>● article -图文<br>● text -纯文本<br/>● video -视频<br/>● short_video -时长15秒以内的视频<br/>● mini_video -竖屏视频<br/>● image -纯图片<br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :type GoodsType: str
        :param _Status: 商品状态：
● 1 - 上架 
● 2 - 下架 
Status=2的内容不会在推荐结果中出现 
需要下架内容时，把Status的值修改为2即可
        :type Status: int
        :param _PublishTimestamp: 商品生成时间，秒级时间戳（1639624786），需大于0，<b>用作特征和物料管理</b>
        :type PublishTimestamp: int
        :param _ExpireTimestamp: 商品过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年，<b>用作特征</b>，过期则不会被推荐，<b>强烈建议</b>
        :type ExpireTimestamp: int
        :param _SpuId: spu((Standard Product Unit))维度id，商品聚合信息的最小单位，<b>强烈建议</b>
        :type SpuId: str
        :param _CategoryLevel: 类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配，<b>强烈建议</b>
        :type CategoryLevel: int
        :param _CategoryPath: 类目路径，一级二级三级等依次用英文冒号联接，和CategoryLevel字段值匹配，如体育：“女装:裙子:半身裙”。<b>用于物料池管理，强烈建议</b>
        :type CategoryPath: str
        :param _Title: 商品标题，<b>主要用于语义分析</b>，<b>强烈建议</b>
        :type Title: str
        :param _Tags: 商品标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :type Tags: str
        :param _Brand: 商品对应的品牌，取值用户自定义，可以是品牌id或品牌明文，<b>用作特征以及打散/过滤规则，强烈建议</b>
        :type Brand: str
        :param _ShopId: 商品所属店铺ID，取值客户自定义，<b>用作特征，强烈建议</b>
        :type ShopId: str
        :param _OrgPrice: 商品原始价格（单位：元，统一货币体系，如统一为RMB或美元等），<b>用作特征，强烈建议</b>
        :type OrgPrice: float
        :param _CurPrice: 商品当前价格（单位：元，统一货币体系，如统一为RMB或美元等），<b>用作特征，强烈建议</b>
        :type CurPrice: float
        :param _SourceId: 商品来源类型，客户自定义，<b>用于物料池管理</b>
        :type SourceId: str
        :param _Content: 商品正文关键片段，建议控制在500字符以内，<b>主要用于语义分析</b>
        :type Content: str
        :param _ContentUrl: 商品正文详情，主要用于语义分析，当内容过大时建议用ContentUrl传递，<b>与Content可二选一</b>
        :type ContentUrl: str
        :param _PicUrlList: 商品封面url，不超过10个，<b>用作特征</b>
        :type PicUrlList: list of str
        :param _Country: 卖家所在国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :type Country: str
        :param _Province: 卖家所在省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :type Province: str
        :param _City: 卖家所在城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :type City: str
        :param _FreeShipping: 商品是否包邮；1:包邮；2:不包邮；3:满足条件包邮，<b>用作特征</b>
        :type FreeShipping: int
        :param _ShippingPrice: 商品邮费（单位：元，统一货币体系，如统一为RMB或美元等），<b>用作特征</b>
        :type ShippingPrice: float
        :param _PraiseCnt: 商品累计好评次数，<b>用作特征</b>
        :type PraiseCnt: int
        :param _CommentCnt: 商品累计评论次数，<b>用作特征</b>
        :type CommentCnt: int
        :param _ShareCnt: 商品累计分享次数，<b>用作特征</b>
        :type ShareCnt: int
        :param _CollectCnt: 商品累计收藏次数，<b>用作特征</b>
        :type CollectCnt: int
        :param _OrderCnt: 商品累积成交次数，<b>用作特征</b>
        :type OrderCnt: int
        :param _Score: 商品平均客户评分，取值范围用户自定，<b>用作特征</b>
        :type Score: float
        :param _Extension: json字符串，<b>用于物料池管理的自定义扩展</b>
        :type Extension: str
        """
        self._GoodsId = None
        self._GoodsType = None
        self._Status = None
        self._PublishTimestamp = None
        self._ExpireTimestamp = None
        self._SpuId = None
        self._CategoryLevel = None
        self._CategoryPath = None
        self._Title = None
        self._Tags = None
        self._Brand = None
        self._ShopId = None
        self._OrgPrice = None
        self._CurPrice = None
        self._SourceId = None
        self._Content = None
        self._ContentUrl = None
        self._PicUrlList = None
        self._Country = None
        self._Province = None
        self._City = None
        self._FreeShipping = None
        self._ShippingPrice = None
        self._PraiseCnt = None
        self._CommentCnt = None
        self._ShareCnt = None
        self._CollectCnt = None
        self._OrderCnt = None
        self._Score = None
        self._Extension = None

    @property
    def GoodsId(self):
        r"""商品唯一ID，skuId或spuId，客户根据需求自行决定商品主键粒度。建议限制在128字符以内
        :rtype: str
        """
        return self._GoodsId

    @GoodsId.setter
    def GoodsId(self, GoodsId):
        self._GoodsId = GoodsId

    @property
    def GoodsType(self):
        r"""商品物料展示类型：<br/>● article -图文<br>● text -纯文本<br/>● video -视频<br/>● short_video -时长15秒以内的视频<br/>● mini_video -竖屏视频<br/>● image -纯图片<br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :rtype: str
        """
        return self._GoodsType

    @GoodsType.setter
    def GoodsType(self, GoodsType):
        self._GoodsType = GoodsType

    @property
    def Status(self):
        r"""商品状态：
● 1 - 上架 
● 2 - 下架 
Status=2的内容不会在推荐结果中出现 
需要下架内容时，把Status的值修改为2即可
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PublishTimestamp(self):
        r"""商品生成时间，秒级时间戳（1639624786），需大于0，<b>用作特征和物料管理</b>
        :rtype: int
        """
        return self._PublishTimestamp

    @PublishTimestamp.setter
    def PublishTimestamp(self, PublishTimestamp):
        self._PublishTimestamp = PublishTimestamp

    @property
    def ExpireTimestamp(self):
        r"""商品过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年，<b>用作特征</b>，过期则不会被推荐，<b>强烈建议</b>
        :rtype: int
        """
        return self._ExpireTimestamp

    @ExpireTimestamp.setter
    def ExpireTimestamp(self, ExpireTimestamp):
        self._ExpireTimestamp = ExpireTimestamp

    @property
    def SpuId(self):
        r"""spu((Standard Product Unit))维度id，商品聚合信息的最小单位，<b>强烈建议</b>
        :rtype: str
        """
        return self._SpuId

    @SpuId.setter
    def SpuId(self, SpuId):
        self._SpuId = SpuId

    @property
    def CategoryLevel(self):
        r"""类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配，<b>强烈建议</b>
        :rtype: int
        """
        return self._CategoryLevel

    @CategoryLevel.setter
    def CategoryLevel(self, CategoryLevel):
        self._CategoryLevel = CategoryLevel

    @property
    def CategoryPath(self):
        r"""类目路径，一级二级三级等依次用英文冒号联接，和CategoryLevel字段值匹配，如体育：“女装:裙子:半身裙”。<b>用于物料池管理，强烈建议</b>
        :rtype: str
        """
        return self._CategoryPath

    @CategoryPath.setter
    def CategoryPath(self, CategoryPath):
        self._CategoryPath = CategoryPath

    @property
    def Title(self):
        r"""商品标题，<b>主要用于语义分析</b>，<b>强烈建议</b>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Tags(self):
        r"""商品标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Brand(self):
        r"""商品对应的品牌，取值用户自定义，可以是品牌id或品牌明文，<b>用作特征以及打散/过滤规则，强烈建议</b>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def ShopId(self):
        r"""商品所属店铺ID，取值客户自定义，<b>用作特征，强烈建议</b>
        :rtype: str
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def OrgPrice(self):
        r"""商品原始价格（单位：元，统一货币体系，如统一为RMB或美元等），<b>用作特征，强烈建议</b>
        :rtype: float
        """
        return self._OrgPrice

    @OrgPrice.setter
    def OrgPrice(self, OrgPrice):
        self._OrgPrice = OrgPrice

    @property
    def CurPrice(self):
        r"""商品当前价格（单位：元，统一货币体系，如统一为RMB或美元等），<b>用作特征，强烈建议</b>
        :rtype: float
        """
        return self._CurPrice

    @CurPrice.setter
    def CurPrice(self, CurPrice):
        self._CurPrice = CurPrice

    @property
    def SourceId(self):
        r"""商品来源类型，客户自定义，<b>用于物料池管理</b>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def Content(self):
        r"""商品正文关键片段，建议控制在500字符以内，<b>主要用于语义分析</b>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentUrl(self):
        r"""商品正文详情，主要用于语义分析，当内容过大时建议用ContentUrl传递，<b>与Content可二选一</b>
        :rtype: str
        """
        return self._ContentUrl

    @ContentUrl.setter
    def ContentUrl(self, ContentUrl):
        self._ContentUrl = ContentUrl

    @property
    def PicUrlList(self):
        r"""商品封面url，不超过10个，<b>用作特征</b>
        :rtype: list of str
        """
        return self._PicUrlList

    @PicUrlList.setter
    def PicUrlList(self, PicUrlList):
        self._PicUrlList = PicUrlList

    @property
    def Country(self):
        r"""卖家所在国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        r"""卖家所在省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        r"""卖家所在城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def FreeShipping(self):
        r"""商品是否包邮；1:包邮；2:不包邮；3:满足条件包邮，<b>用作特征</b>
        :rtype: int
        """
        return self._FreeShipping

    @FreeShipping.setter
    def FreeShipping(self, FreeShipping):
        self._FreeShipping = FreeShipping

    @property
    def ShippingPrice(self):
        r"""商品邮费（单位：元，统一货币体系，如统一为RMB或美元等），<b>用作特征</b>
        :rtype: float
        """
        return self._ShippingPrice

    @ShippingPrice.setter
    def ShippingPrice(self, ShippingPrice):
        self._ShippingPrice = ShippingPrice

    @property
    def PraiseCnt(self):
        r"""商品累计好评次数，<b>用作特征</b>
        :rtype: int
        """
        return self._PraiseCnt

    @PraiseCnt.setter
    def PraiseCnt(self, PraiseCnt):
        self._PraiseCnt = PraiseCnt

    @property
    def CommentCnt(self):
        r"""商品累计评论次数，<b>用作特征</b>
        :rtype: int
        """
        return self._CommentCnt

    @CommentCnt.setter
    def CommentCnt(self, CommentCnt):
        self._CommentCnt = CommentCnt

    @property
    def ShareCnt(self):
        r"""商品累计分享次数，<b>用作特征</b>
        :rtype: int
        """
        return self._ShareCnt

    @ShareCnt.setter
    def ShareCnt(self, ShareCnt):
        self._ShareCnt = ShareCnt

    @property
    def CollectCnt(self):
        r"""商品累计收藏次数，<b>用作特征</b>
        :rtype: int
        """
        return self._CollectCnt

    @CollectCnt.setter
    def CollectCnt(self, CollectCnt):
        self._CollectCnt = CollectCnt

    @property
    def OrderCnt(self):
        r"""商品累积成交次数，<b>用作特征</b>
        :rtype: int
        """
        return self._OrderCnt

    @OrderCnt.setter
    def OrderCnt(self, OrderCnt):
        self._OrderCnt = OrderCnt

    @property
    def Score(self):
        r"""商品平均客户评分，取值范围用户自定，<b>用作特征</b>
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Extension(self):
        r"""json字符串，<b>用于物料池管理的自定义扩展</b>
        :rtype: str
        """
        return self._Extension

    @Extension.setter
    def Extension(self, Extension):
        self._Extension = Extension


    def _deserialize(self, params):
        self._GoodsId = params.get("GoodsId")
        self._GoodsType = params.get("GoodsType")
        self._Status = params.get("Status")
        self._PublishTimestamp = params.get("PublishTimestamp")
        self._ExpireTimestamp = params.get("ExpireTimestamp")
        self._SpuId = params.get("SpuId")
        self._CategoryLevel = params.get("CategoryLevel")
        self._CategoryPath = params.get("CategoryPath")
        self._Title = params.get("Title")
        self._Tags = params.get("Tags")
        self._Brand = params.get("Brand")
        self._ShopId = params.get("ShopId")
        self._OrgPrice = params.get("OrgPrice")
        self._CurPrice = params.get("CurPrice")
        self._SourceId = params.get("SourceId")
        self._Content = params.get("Content")
        self._ContentUrl = params.get("ContentUrl")
        self._PicUrlList = params.get("PicUrlList")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._FreeShipping = params.get("FreeShipping")
        self._ShippingPrice = params.get("ShippingPrice")
        self._PraiseCnt = params.get("PraiseCnt")
        self._CommentCnt = params.get("CommentCnt")
        self._ShareCnt = params.get("ShareCnt")
        self._CollectCnt = params.get("CollectCnt")
        self._OrderCnt = params.get("OrderCnt")
        self._Score = params.get("Score")
        self._Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecGoodsData(AbstractModel):
    r"""推荐返回的内容信息

    """

    def __init__(self):
        r"""
        :param _GoodsId: 推荐返回的商品ID
        :type GoodsId: str
        :param _Score: 推荐结果分，取值范围[0,1000000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        :param _GoodsTraceId: 推荐追踪id，本次推荐内容产生的后续行为上报均要用该GoodsTraceId上报。每次接口调用返回的GoodsTraceId不同
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsTraceId: str
        :param _Position: 商品所在位置
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: int
        """
        self._GoodsId = None
        self._Score = None
        self._GoodsTraceId = None
        self._Position = None

    @property
    def GoodsId(self):
        r"""推荐返回的商品ID
        :rtype: str
        """
        return self._GoodsId

    @GoodsId.setter
    def GoodsId(self, GoodsId):
        self._GoodsId = GoodsId

    @property
    def Score(self):
        r"""推荐结果分，取值范围[0,1000000]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def GoodsTraceId(self):
        r"""推荐追踪id，本次推荐内容产生的后续行为上报均要用该GoodsTraceId上报。每次接口调用返回的GoodsTraceId不同
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GoodsTraceId

    @GoodsTraceId.setter
    def GoodsTraceId(self, GoodsTraceId):
        self._GoodsTraceId = GoodsTraceId

    @property
    def Position(self):
        r"""商品所在位置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position


    def _deserialize(self, params):
        self._GoodsId = params.get("GoodsId")
        self._Score = params.get("Score")
        self._GoodsTraceId = params.get("GoodsTraceId")
        self._Position = params.get("Position")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecItemData(AbstractModel):
    r"""推荐返回的内容信息

    """

    def __init__(self):
        r"""
        :param _ItemId: 推荐的内容ID
        :type ItemId: str
        :param _ItemType: 内容类型，同内容上报类型一致
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemType: str
        :param _ItemTraceId: 推荐追踪id，本次推荐内容产生的后续行为上报均要用该ItemTraceId上报。每次接口调用返回的ItemTraceId不同
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemTraceId: str
        :param _Score: 推荐预测分，分值越高被推荐的理由越充分，取值范围[0,1000000]，用于做二次排序的参考
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self._ItemId = None
        self._ItemType = None
        self._ItemTraceId = None
        self._Score = None

    @property
    def ItemId(self):
        r"""推荐的内容ID
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ItemType(self):
        r"""内容类型，同内容上报类型一致
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ItemType

    @ItemType.setter
    def ItemType(self, ItemType):
        self._ItemType = ItemType

    @property
    def ItemTraceId(self):
        r"""推荐追踪id，本次推荐内容产生的后续行为上报均要用该ItemTraceId上报。每次接口调用返回的ItemTraceId不同
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ItemTraceId

    @ItemTraceId.setter
    def ItemTraceId(self, ItemTraceId):
        self._ItemTraceId = ItemTraceId

    @property
    def Score(self):
        r"""推荐预测分，分值越高被推荐的理由越充分，取值范围[0,1000000]，用于做二次排序的参考
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._ItemType = params.get("ItemType")
        self._ItemTraceId = params.get("ItemTraceId")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedBehaviorRequest(AbstractModel):
    r"""ReportFeedBehavior请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param _FeedBehaviorList: 上报的行为数据数组，数量不超过50
        :type FeedBehaviorList: list of FeedBehaviorInfo
        """
        self._InstanceId = None
        self._FeedBehaviorList = None

    @property
    def InstanceId(self):
        r"""实例ID，在控制台获取
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FeedBehaviorList(self):
        r"""上报的行为数据数组，数量不超过50
        :rtype: list of FeedBehaviorInfo
        """
        return self._FeedBehaviorList

    @FeedBehaviorList.setter
    def FeedBehaviorList(self, FeedBehaviorList):
        self._FeedBehaviorList = FeedBehaviorList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FeedBehaviorList") is not None:
            self._FeedBehaviorList = []
            for item in params.get("FeedBehaviorList"):
                obj = FeedBehaviorInfo()
                obj._deserialize(item)
                self._FeedBehaviorList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedBehaviorResponse(AbstractModel):
    r"""ReportFeedBehavior返回参数结构体

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


class ReportFeedItemRequest(AbstractModel):
    r"""ReportFeedItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param _FeedItemList: 上报的信息流内容数组，一次数量不超过50
        :type FeedItemList: list of DocItem
        """
        self._InstanceId = None
        self._FeedItemList = None

    @property
    def InstanceId(self):
        r"""实例ID，在控制台获取
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FeedItemList(self):
        r"""上报的信息流内容数组，一次数量不超过50
        :rtype: list of DocItem
        """
        return self._FeedItemList

    @FeedItemList.setter
    def FeedItemList(self, FeedItemList):
        self._FeedItemList = FeedItemList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FeedItemList") is not None:
            self._FeedItemList = []
            for item in params.get("FeedItemList"):
                obj = DocItem()
                obj._deserialize(item)
                self._FeedItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedItemResponse(AbstractModel):
    r"""ReportFeedItem返回参数结构体

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


class ReportFeedUserRequest(AbstractModel):
    r"""ReportFeedUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param _FeedUserList: 上报的用户信息数组，数量不超过50
        :type FeedUserList: list of FeedUserInfo
        """
        self._InstanceId = None
        self._FeedUserList = None

    @property
    def InstanceId(self):
        r"""实例ID，在控制台获取
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def FeedUserList(self):
        r"""上报的用户信息数组，数量不超过50
        :rtype: list of FeedUserInfo
        """
        return self._FeedUserList

    @FeedUserList.setter
    def FeedUserList(self, FeedUserList):
        self._FeedUserList = FeedUserList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("FeedUserList") is not None:
            self._FeedUserList = []
            for item in params.get("FeedUserList"):
                obj = FeedUserInfo()
                obj._deserialize(item)
                self._FeedUserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedUserResponse(AbstractModel):
    r"""ReportFeedUser返回参数结构体

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


class ReportGoodsBehaviorRequest(AbstractModel):
    r"""ReportGoodsBehavior请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param _GoodsBehaviorList: 上报的商品对应的用户行为数据数组，数量不超过50
        :type GoodsBehaviorList: list of GoodsBehaviorInfo
        """
        self._InstanceId = None
        self._GoodsBehaviorList = None

    @property
    def InstanceId(self):
        r"""实例ID，在控制台获取
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GoodsBehaviorList(self):
        r"""上报的商品对应的用户行为数据数组，数量不超过50
        :rtype: list of GoodsBehaviorInfo
        """
        return self._GoodsBehaviorList

    @GoodsBehaviorList.setter
    def GoodsBehaviorList(self, GoodsBehaviorList):
        self._GoodsBehaviorList = GoodsBehaviorList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GoodsBehaviorList") is not None:
            self._GoodsBehaviorList = []
            for item in params.get("GoodsBehaviorList"):
                obj = GoodsBehaviorInfo()
                obj._deserialize(item)
                self._GoodsBehaviorList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportGoodsBehaviorResponse(AbstractModel):
    r"""ReportGoodsBehavior返回参数结构体

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


class ReportGoodsInfoRequest(AbstractModel):
    r"""ReportGoodsInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param _GoodsList: 上报的商品数组，一次数量不超过50
        :type GoodsList: list of GoodsInfo
        """
        self._InstanceId = None
        self._GoodsList = None

    @property
    def InstanceId(self):
        r"""实例ID，在控制台获取
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GoodsList(self):
        r"""上报的商品数组，一次数量不超过50
        :rtype: list of GoodsInfo
        """
        return self._GoodsList

    @GoodsList.setter
    def GoodsList(self, GoodsList):
        self._GoodsList = GoodsList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GoodsList") is not None:
            self._GoodsList = []
            for item in params.get("GoodsList"):
                obj = GoodsInfo()
                obj._deserialize(item)
                self._GoodsList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportGoodsInfoResponse(AbstractModel):
    r"""ReportGoodsInfo返回参数结构体

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


class StrUserIdInfo(AbstractModel):
    r"""用户信息

    """


class UserIdInfo(AbstractModel):
    r"""用户ID信息

    """

    def __init__(self):
        r"""
        :param _Type: 用户ID类型： <br/>● qq: qq号码 <br/>● qq_md5：qq的md5值 <br/>● imei：设备imei <br/>● imei_md5：imei的md5值 <br/>● idfa: Apple 向用户设备随机分配的设备标识符 <br/>● idfa_md5：idfa的md5值 <br/>● oaid：安卓10之后一种非永久性设备标识符 <br/>● oaid_md5：md5后的oaid <br/>● wx_openid：微信openid <br/>● qq_openid：QQ的openid <br/>● phone：电话号码 <br/>● phone_md5：md5后的电话号码 <br/>● phone_sha256：SHA256加密的手机号 <br/>● phone_sm3：国密SM3加密的手机号 <br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :type Type: str
        :param _Value: 用户ID值
        :type Value: str
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        r"""用户ID类型： <br/>● qq: qq号码 <br/>● qq_md5：qq的md5值 <br/>● imei：设备imei <br/>● imei_md5：imei的md5值 <br/>● idfa: Apple 向用户设备随机分配的设备标识符 <br/>● idfa_md5：idfa的md5值 <br/>● oaid：安卓10之后一种非永久性设备标识符 <br/>● oaid_md5：md5后的oaid <br/>● wx_openid：微信openid <br/>● qq_openid：QQ的openid <br/>● phone：电话号码 <br/>● phone_md5：md5后的电话号码 <br/>● phone_sha256：SHA256加密的手机号 <br/>● phone_sm3：国密SM3加密的手机号 <br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""用户ID值
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
        


class UserPortraitInfo(AbstractModel):
    r"""用户基础画像

    """