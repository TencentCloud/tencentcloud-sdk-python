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


class AuthorInfo(AbstractModel):
    """作者信息

    """

    def __init__(self):
        r"""
        :param Id: 作者id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Name: 作者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param SourceId: 作者来源
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceId: int
        :param FollowType: 关注类型：1-关注，2-取关
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowType: int
        :param IconUrl: 作者头像icon地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        """
        self.Id = None
        self.Name = None
        self.SourceId = None
        self.FollowType = None
        self.IconUrl = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.SourceId = params.get("SourceId")
        self.FollowType = params.get("FollowType")
        self.IconUrl = params.get("IconUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DislikeInfo(AbstractModel):
    """不喜欢信息

    """

    def __init__(self):
        r"""
        :param Type: 不喜欢的物料类别，对应物料上传协议中的字段名，如authorId，keyword，topic等
        :type Type: str
        :param Value: type对应字段名的值，如具体的topic名，作者id等
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocBehavior(AbstractModel):
    """行为数据

    """

    def __init__(self):
        r"""
        :param ItemId: 内容唯一ID，如 2824324234
        :type ItemId: str
        :param BehaviorType: 行为类型
        :type BehaviorType: int
        :param BehaviorValue: 行为值
        :type BehaviorValue: str
        :param BehaviorTimestamp: 行为时间戳： 秒级时间戳（默认为当前时间）,不能延迟太久，尽量实时上报，否则会影响推荐结果的准确性。
        :type BehaviorTimestamp: int
        :param SceneId: 场景id，在控制台创建场景后获取。
        :type SceneId: str
        :param UserIdList: 用户id列表
        :type UserIdList: list of UserIdInfo
        :param RecTraceId: 会话id，使用获取推荐结果中返回的RecTraceId填入。<br>注意：如果和在线推荐请求中的traceId不同，会影响行为特征归因，影响推荐算法效果
        :type RecTraceId: str
        :param Source: 算法来源：用来区分行为来源于哪个算法。值为**business，tencent，other** 三者之一<br>● business 表示业务自己的算法对照组<br>● tencent 为腾讯算法<br>● other 为其他算法
        :type Source: str
        :param ItemType: 物料类型
        :type ItemType: int
        :param AppId: 微信开放平台上查看appId
        :type AppId: str
        :param VideoPlayDuration: 回传video_over事件的时候，回传的用户播放视频的总时长（真正播放的，拖动不算，单位为秒）
        :type VideoPlayDuration: int
        :param ReferrerItemId: 来源物料内容：用来标识在指定内容页面产生的行为，如需要统计用户在A内容详情页里，对推荐内容B点击等行为，则ReferrerItemId代表内容A，ItemId代表内容B
        :type ReferrerItemId: str
        :param Country: 国家，统一用简写，比如中国则填写CN
        :type Country: str
        :param Province: 省
        :type Province: str
        :param City: 城市
        :type City: str
        :param District: 区县
        :type District: str
        :param IP: 客户端ip
        :type IP: str
        :param Network: 客户端网络类型
        :type Network: str
        :param Platform: 客户端平台，ios/android/h5
        :type Platform: str
        :param AppVersion: 客户端app版本
        :type AppVersion: str
        :param OsVersion: 操作系统版本
        :type OsVersion: str
        :param DeviceModel: 机型
        :type DeviceModel: str
        :param Extension: json字符串，用于行为数据的扩展
        :type Extension: str
        """
        self.ItemId = None
        self.BehaviorType = None
        self.BehaviorValue = None
        self.BehaviorTimestamp = None
        self.SceneId = None
        self.UserIdList = None
        self.RecTraceId = None
        self.Source = None
        self.ItemType = None
        self.AppId = None
        self.VideoPlayDuration = None
        self.ReferrerItemId = None
        self.Country = None
        self.Province = None
        self.City = None
        self.District = None
        self.IP = None
        self.Network = None
        self.Platform = None
        self.AppVersion = None
        self.OsVersion = None
        self.DeviceModel = None
        self.Extension = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.BehaviorType = params.get("BehaviorType")
        self.BehaviorValue = params.get("BehaviorValue")
        self.BehaviorTimestamp = params.get("BehaviorTimestamp")
        self.SceneId = params.get("SceneId")
        if params.get("UserIdList") is not None:
            self.UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self.UserIdList.append(obj)
        self.RecTraceId = params.get("RecTraceId")
        self.Source = params.get("Source")
        self.ItemType = params.get("ItemType")
        self.AppId = params.get("AppId")
        self.VideoPlayDuration = params.get("VideoPlayDuration")
        self.ReferrerItemId = params.get("ReferrerItemId")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.District = params.get("District")
        self.IP = params.get("IP")
        self.Network = params.get("Network")
        self.Platform = params.get("Platform")
        self.AppVersion = params.get("AppVersion")
        self.OsVersion = params.get("OsVersion")
        self.DeviceModel = params.get("DeviceModel")
        self.Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocItem(AbstractModel):
    """推荐物料信息

    """

    def __init__(self):
        r"""
        :param ItemId: 内容唯一id
        :type ItemId: str
        :param ItemType: 内容类型
        :type ItemType: int
        :param Status: 内容状态：1 - 上架， 2 - 下架
        :type Status: int
        :param PublishTimestamp: 内容生成时间，秒级时间戳（1639624786），需大于0
        :type PublishTimestamp: int
        :param SourceId: 物料来源ID
        :type SourceId: int
        :param Title: 标题名称
        :type Title: str
        :param Content: 内容正文
        :type Content: str
        :param Author: 作者
        :type Author: str
        :param AuthorId: 作者id
        :type AuthorId: str
        :param Keyword: 标签关键词，多个用英文分号分割
        :type Keyword: str
        :param Desc: 内容物料描述：物料的描述信息，推荐系统会对内容的描述信息，使用否LP技术，进行分词、提取关键词，作为news的特征使用。
        :type Desc: str
        :param PicUrlList: 图片url
        :type PicUrlList: list of str
        :param VideoUrlList: 视频url
        :type VideoUrlList: list of str
        :param VideoDuration: 视频时长，时间秒
        :type VideoDuration: int
        :param CategoryLevel: 类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配
        :type CategoryLevel: int
        :param CategoryPath: 类目路径，一级二级三级等依次用英文冒号联接，如体育：“足球:巴塞罗那”
        :type CategoryPath: str
        :param Country: 国家，统一用简写，比如中国则填写CN
        :type Country: str
        :param Province: 省
        :type Province: str
        :param City: 城市
        :type City: str
        :param District: 区县
        :type District: str
        :param ExpireTimestamp: 内容过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年
        :type ExpireTimestamp: int
        :param Topic: 所属话题
        :type Topic: str
        :param AuthorFans: 作者粉丝数
        :type AuthorFans: int
        :param AuthorLevel: 作者评级
        :type AuthorLevel: str
        :param CollectCnt: 内容累计收藏次数
        :type CollectCnt: int
        :param PraiseCnt: 内容累积点赞次数
        :type PraiseCnt: int
        :param CommentCnt: 内容累计评论次数
        :type CommentCnt: int
        :param ShareCnt: 内容累计分享次数
        :type ShareCnt: int
        :param RewardCnt: 内容累积打赏数
        :type RewardCnt: int
        :param Score: 内容质量评分，类似豆瓣电影的评分，这里为100分制，比如97分，满分100分，最低0分，范围外的将会被拦截
        :type Score: float
        :param PoolIdList: 内容池id，用于分内容池召回，一个内容支持指定一个或多个内容池， 内容池id不建议使用0（0表示不区分内容池）
        :type PoolIdList: list of str
        :param TagInfoList: 描述用户标签
        :type TagInfoList: list of TagInfo
        :param Extension: json字符串，用于物料数据的扩展
        :type Extension: str
        """
        self.ItemId = None
        self.ItemType = None
        self.Status = None
        self.PublishTimestamp = None
        self.SourceId = None
        self.Title = None
        self.Content = None
        self.Author = None
        self.AuthorId = None
        self.Keyword = None
        self.Desc = None
        self.PicUrlList = None
        self.VideoUrlList = None
        self.VideoDuration = None
        self.CategoryLevel = None
        self.CategoryPath = None
        self.Country = None
        self.Province = None
        self.City = None
        self.District = None
        self.ExpireTimestamp = None
        self.Topic = None
        self.AuthorFans = None
        self.AuthorLevel = None
        self.CollectCnt = None
        self.PraiseCnt = None
        self.CommentCnt = None
        self.ShareCnt = None
        self.RewardCnt = None
        self.Score = None
        self.PoolIdList = None
        self.TagInfoList = None
        self.Extension = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.ItemType = params.get("ItemType")
        self.Status = params.get("Status")
        self.PublishTimestamp = params.get("PublishTimestamp")
        self.SourceId = params.get("SourceId")
        self.Title = params.get("Title")
        self.Content = params.get("Content")
        self.Author = params.get("Author")
        self.AuthorId = params.get("AuthorId")
        self.Keyword = params.get("Keyword")
        self.Desc = params.get("Desc")
        self.PicUrlList = params.get("PicUrlList")
        self.VideoUrlList = params.get("VideoUrlList")
        self.VideoDuration = params.get("VideoDuration")
        self.CategoryLevel = params.get("CategoryLevel")
        self.CategoryPath = params.get("CategoryPath")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.District = params.get("District")
        self.ExpireTimestamp = params.get("ExpireTimestamp")
        self.Topic = params.get("Topic")
        self.AuthorFans = params.get("AuthorFans")
        self.AuthorLevel = params.get("AuthorLevel")
        self.CollectCnt = params.get("CollectCnt")
        self.PraiseCnt = params.get("PraiseCnt")
        self.CommentCnt = params.get("CommentCnt")
        self.ShareCnt = params.get("ShareCnt")
        self.RewardCnt = params.get("RewardCnt")
        self.Score = params.get("Score")
        self.PoolIdList = params.get("PoolIdList")
        if params.get("TagInfoList") is not None:
            self.TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagInfoList.append(obj)
        self.Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortraitInfo(AbstractModel):
    """画像信息

    """

    def __init__(self):
        r"""
        :param UserIdList: 用户id列表
        :type UserIdList: list of UserIdInfo
        :param AppId: 如果"userIdType"是10则必传，在微信开放平台上查看appId
        :type AppId: str
        :param Age: 用户年龄，值域在 0-200
        :type Age: int
        :param Gender: 用户性别：0-未知，1-男， 2-女
        :type Gender: int
        :param Degree: 用户学历 ：小学，初中，高中，大专，本科，硕士，博士
        :type Degree: str
        :param School: 用户毕业学校全称
        :type School: str
        :param Occupation: 用户职业，保证业务的唯一性
        :type Occupation: str
        :param Industry: 用户所属行业，保证业务的唯一性
        :type Industry: str
        :param ResidentCountry: 用户常驻国家，统一用简写，比如中国则填写CN
        :type ResidentCountry: str
        :param ResidentProvince: 用户常驻省份
        :type ResidentProvince: str
        :param ResidentCity: 用户常驻城市
        :type ResidentCity: str
        :param ResidentDistrict: 用户常驻区县
        :type ResidentDistrict: str
        :param PhoneMd5: 用户手机的MD5值
        :type PhoneMd5: str
        :param PhoneImei: 用户手机的IMEI号
        :type PhoneImei: str
        :param Idfa: 设备idfa信息
        :type Idfa: str
        :param RegisterTimestamp: 用户注册时间，秒级时间戳（1639624786）
        :type RegisterTimestamp: int
        :param MembershipLevel: 用户会员等级
        :type MembershipLevel: str
        :param LastLoginTimestamp: 用户上一次登录时间，秒级时间戳（1639624786）
        :type LastLoginTimestamp: int
        :param LastLoginIp: 用户上一次登录的ip
        :type LastLoginIp: str
        :param LastModifyTimestamp: 用户信息的最后修改时间戳，秒级时间戳（1639624786）
        :type LastModifyTimestamp: int
        :param TagInfoList: 用户标签
        :type TagInfoList: list of TagInfo
        :param AuthorInfoList: 用户关注作者列表
        :type AuthorInfoList: list of AuthorInfo
        :param DislikeInfoList: 用户不喜欢列表
        :type DislikeInfoList: list of DislikeInfo
        :param Extension: json字符串，用于画像数据的扩展
        :type Extension: str
        :param Oaid: 设备oaid信息
        :type Oaid: str
        :param AndroidId: 设备AndroidId信息
        :type AndroidId: str
        """
        self.UserIdList = None
        self.AppId = None
        self.Age = None
        self.Gender = None
        self.Degree = None
        self.School = None
        self.Occupation = None
        self.Industry = None
        self.ResidentCountry = None
        self.ResidentProvince = None
        self.ResidentCity = None
        self.ResidentDistrict = None
        self.PhoneMd5 = None
        self.PhoneImei = None
        self.Idfa = None
        self.RegisterTimestamp = None
        self.MembershipLevel = None
        self.LastLoginTimestamp = None
        self.LastLoginIp = None
        self.LastModifyTimestamp = None
        self.TagInfoList = None
        self.AuthorInfoList = None
        self.DislikeInfoList = None
        self.Extension = None
        self.Oaid = None
        self.AndroidId = None


    def _deserialize(self, params):
        if params.get("UserIdList") is not None:
            self.UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self.UserIdList.append(obj)
        self.AppId = params.get("AppId")
        self.Age = params.get("Age")
        self.Gender = params.get("Gender")
        self.Degree = params.get("Degree")
        self.School = params.get("School")
        self.Occupation = params.get("Occupation")
        self.Industry = params.get("Industry")
        self.ResidentCountry = params.get("ResidentCountry")
        self.ResidentProvince = params.get("ResidentProvince")
        self.ResidentCity = params.get("ResidentCity")
        self.ResidentDistrict = params.get("ResidentDistrict")
        self.PhoneMd5 = params.get("PhoneMd5")
        self.PhoneImei = params.get("PhoneImei")
        self.Idfa = params.get("Idfa")
        self.RegisterTimestamp = params.get("RegisterTimestamp")
        self.MembershipLevel = params.get("MembershipLevel")
        self.LastLoginTimestamp = params.get("LastLoginTimestamp")
        self.LastLoginIp = params.get("LastLoginIp")
        self.LastModifyTimestamp = params.get("LastModifyTimestamp")
        if params.get("TagInfoList") is not None:
            self.TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagInfoList.append(obj)
        if params.get("AuthorInfoList") is not None:
            self.AuthorInfoList = []
            for item in params.get("AuthorInfoList"):
                obj = AuthorInfo()
                obj._deserialize(item)
                self.AuthorInfoList.append(obj)
        if params.get("DislikeInfoList") is not None:
            self.DislikeInfoList = []
            for item in params.get("DislikeInfoList"):
                obj = DislikeInfo()
                obj._deserialize(item)
                self.DislikeInfoList.append(obj)
        self.Extension = params.get("Extension")
        self.Oaid = params.get("Oaid")
        self.AndroidId = params.get("AndroidId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecItemData(AbstractModel):
    """推荐内容信息

    """

    def __init__(self):
        r"""
        :param ItemId: 推荐的内容id，即用户行为上报中的itemId
        :type ItemId: str
        :param ItemType: 物料子类型，包括如下： 1-图文、2-长视频（横视频）、3-短视频（横视频）、4-小说、5-小视频（竖视频）、6-纯文本
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemType: int
        :param Weight: 推荐内容的权重，取值范围[0,1000000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param Score: 推荐预测分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        :param Keyword: 关键词，多个用英文分号分割，和物料上传的keyword一致
注意：此字段可能返回 null，表示取不到有效值。
        :type Keyword: str
        """
        self.ItemId = None
        self.ItemType = None
        self.Weight = None
        self.Score = None
        self.Keyword = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.ItemType = params.get("ItemType")
        self.Weight = params.get("Weight")
        self.Score = params.get("Score")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecommendContentRequest(AbstractModel):
    """RecommendContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param Bid: 业务id
        :type Bid: str
        :param SceneId: 场景id：比如有“猜你喜欢”，“热门内容”等推荐模块，每一个模块都有一个scene_id来表示。 在控制台创建场景后获取。需要跟行为上报时的id一致
        :type SceneId: str
        :param UserIdList: 用户唯一ID数组，每个数组元素详见userId结构体，若不填，则接口返回热门结果
        :type UserIdList: list of UserIdInfo
        :param RecTraceId: 会话id：必须和行为数据上报时所填写的traceId相同，用于行为数据来自于那次在线推荐请求的归因。**注意：此处如果没传，则响应会返回一个全局唯一ID返回给客户，并需客户透传给行为日志上报接口**
        :type RecTraceId: str
        :param ItemCnt: 推荐数量：物料优选的结果， 默认50个，目前最多支持200个的内容返回，如果返回个数更多，会影响性能，容易超时。
        :type ItemCnt: int
        :param PoolId: 物料池id，用于召回该pool_id下的商品，如果有多个，用英文;分割。**注意：此处poolId需和物料上报时的poolIdList对应上**
        :type PoolId: str
        :param CurrentItemId: 来源物料id，即用户当前浏览的物料id，用于在内容详情页获取关联推荐内容
        :type CurrentItemId: str
        :param ResponseTimeout: 请求响应超时时间，单位ms，默认300ms，数值设置的过小，会影响推荐效果，最小支持250ms
        :type ResponseTimeout: int
        :param ItemTypeRatio: 返回结果中不同物料类型的比例，比例顺序需严格按照（图文，长视频，短视频，小视频）进行。只允许传[0,100]数字，多个请用**英文冒号**分割，且加起来不能超过100，以及比例数量不能超过**场景绑定的物料类型**（图文，长视频，短视频，小视频）数。**示例：**图文和短视频比例为40%:60%时，则填40:60图文和短视频比例为0%:100%时，则填0:100图文，长视频和短视频的比例为，图文占20%，剩余80%由长视频和短视频随机返回，则填20:80或仅填20均可
        :type ItemTypeRatio: str
        """
        self.Bid = None
        self.SceneId = None
        self.UserIdList = None
        self.RecTraceId = None
        self.ItemCnt = None
        self.PoolId = None
        self.CurrentItemId = None
        self.ResponseTimeout = None
        self.ItemTypeRatio = None


    def _deserialize(self, params):
        self.Bid = params.get("Bid")
        self.SceneId = params.get("SceneId")
        if params.get("UserIdList") is not None:
            self.UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self.UserIdList.append(obj)
        self.RecTraceId = params.get("RecTraceId")
        self.ItemCnt = params.get("ItemCnt")
        self.PoolId = params.get("PoolId")
        self.CurrentItemId = params.get("CurrentItemId")
        self.ResponseTimeout = params.get("ResponseTimeout")
        self.ItemTypeRatio = params.get("ItemTypeRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecommendContentResponse(AbstractModel):
    """RecommendContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RecTraceId: 推荐追踪id，用于行为上报。每次接口调用返回的traceId不同
        :type RecTraceId: str
        :param DataList: 标识具体的物料信息
        :type DataList: list of RecItemData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RecTraceId = None
        self.DataList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RecTraceId = params.get("RecTraceId")
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = RecItemData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.RequestId = params.get("RequestId")


class ReportActionRequest(AbstractModel):
    """ReportAction请求参数结构体

    """

    def __init__(self):
        r"""
        :param Bid: 业务id
        :type Bid: str
        :param DocBehaviorList: 上报的行为对象数组，数量不超过50
        :type DocBehaviorList: list of DocBehavior
        """
        self.Bid = None
        self.DocBehaviorList = None


    def _deserialize(self, params):
        self.Bid = params.get("Bid")
        if params.get("DocBehaviorList") is not None:
            self.DocBehaviorList = []
            for item in params.get("DocBehaviorList"):
                obj = DocBehavior()
                obj._deserialize(item)
                self.DocBehaviorList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportActionResponse(AbstractModel):
    """ReportAction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReportMaterialRequest(AbstractModel):
    """ReportMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param Bid: 业务id
        :type Bid: str
        :param DocItemList: 上报的信息流数组，一次数量不超过50
        :type DocItemList: list of DocItem
        """
        self.Bid = None
        self.DocItemList = None


    def _deserialize(self, params):
        self.Bid = params.get("Bid")
        if params.get("DocItemList") is not None:
            self.DocItemList = []
            for item in params.get("DocItemList"):
                obj = DocItem()
                obj._deserialize(item)
                self.DocItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportMaterialResponse(AbstractModel):
    """ReportMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReportPortraitRequest(AbstractModel):
    """ReportPortrait请求参数结构体

    """

    def __init__(self):
        r"""
        :param Bid: 推荐平台上的业务id
        :type Bid: str
        :param PortraitList: 上报的用户画像数组，数量不超过50
        :type PortraitList: list of PortraitInfo
        """
        self.Bid = None
        self.PortraitList = None


    def _deserialize(self, params):
        self.Bid = params.get("Bid")
        if params.get("PortraitList") is not None:
            self.PortraitList = []
            for item in params.get("PortraitList"):
                obj = PortraitInfo()
                obj._deserialize(item)
                self.PortraitList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportPortraitResponse(AbstractModel):
    """ReportPortrait返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """标题信息

    """

    def __init__(self):
        r"""
        :param Id: 标签id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Name: 标签名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Weight: 推荐权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: float
        """
        self.Id = None
        self.Name = None
        self.Weight = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserIdInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param UserIdType: 用户id类型
        :type UserIdType: int
        :param UserId: 用户id
        :type UserId: str
        """
        self.UserIdType = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserIdType = params.get("UserIdType")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        