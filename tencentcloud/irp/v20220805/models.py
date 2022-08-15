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


class DislikeInfo(AbstractModel):
    """不喜欢信息

    """

    def __init__(self):
        r"""
        :param Type: 过滤的类别：<br>● author 作者名<br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :type Type: str
        :param Value: Type对应字段名的值，如：需要过滤的作者名
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
        


class DocItem(AbstractModel):
    """信息流内容

    """

    def __init__(self):
        r"""
        :param ItemId: 内容唯一id，建议限制在128字符以内
        :type ItemId: str
        :param ItemType: 内容类型：<br/>● article -图文<br>● text -纯文本<br/>● video -视频<br/>● short_video -时长15秒以内的视频<br/>● mini_video -竖屏视频<br/>● image -纯图片<br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :type ItemType: str
        :param Status: 内容状态：
● 1 - 上架 
● 2 - 下架 
Status=2的内容不会在推荐结果中出现 
需要下架内容时，把Status的值修改为2即可
        :type Status: int
        :param PublishTimestamp: 内容生成时间，秒级时间戳（1639624786），需大于0，<b>用作特征和物料管理</b>
        :type PublishTimestamp: int
        :param ExpireTimestamp: 内容过期时间，秒级时间戳（1639624786），如未填，则默认PublishTimestamp往后延一年，用作特征，过期则不会被推荐，<b>强烈建议</b>
        :type ExpireTimestamp: int
        :param CategoryLevel: 类目层级数，例如3级类目，则填3，和CategoryPath字段的类数据匹配，<b>强烈建议</b>
        :type CategoryLevel: int
        :param CategoryPath: 类目路径，一级二级三级等依次用英文冒号联接，和CategoryLevel字段值匹配，如体育：“足球:巴塞罗那”。<b>用于物料池管理，强烈建议</b>
        :type CategoryPath: str
        :param Tags: 内容标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :type Tags: str
        :param Author: 作者名，需保证作者名唯一，若有重名需要加编号区分。<b>用于召回过滤、规则打散，强烈建议</b>
        :type Author: str
        :param SourceId: 内容来源类型，客户自定义，<b>用于物料池管理</b>
        :type SourceId: str
        :param Title: 内容标题，<b>主要用于语义分析</b>
        :type Title: str
        :param Content: 正文关键片段，建议控制在500字符以内，<b>主要用于语义分析</b>
        :type Content: str
        :param ContentUrl: 正文详情，主要用于语义分析，当内容过大时建议用ContentUrl传递，<b>与Content可二选一</b>
        :type ContentUrl: str
        :param VideoDuration: 视频时长，时间秒，大于等于0，小于 3600 * 10。<b>视频内容必填，其它内容非必填，用作特征</b>
        :type VideoDuration: int
        :param Country: 国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :type Country: str
        :param Province: 省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :type Province: str
        :param City: 城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :type City: str
        :param AuthorFans: 作者粉丝数，<b>用作特征</b>
        :type AuthorFans: int
        :param AuthorLevel: 作者评级，<b>用作特征</b>
        :type AuthorLevel: str
        :param CollectCnt: 内容累计收藏次数，<b>用作特征</b>
        :type CollectCnt: int
        :param PraiseCnt: 内容累积点赞次数，<b>用作特征</b>
        :type PraiseCnt: int
        :param CommentCnt: 内容累计评论次数，<b>用作特征</b>
        :type CommentCnt: int
        :param ShareCnt: 内容累计分享次数，<b>用作特征</b>
        :type ShareCnt: int
        :param RewardCnt: 内容累积打赏数，<b>用作特征</b>
        :type RewardCnt: int
        :param Score: 内容质量评分，<b>用作特征</b>
        :type Score: float
        :param Extension: json字符串，<b>用于物料池管理的自定义扩展</b>
        :type Extension: str
        """
        self.ItemId = None
        self.ItemType = None
        self.Status = None
        self.PublishTimestamp = None
        self.ExpireTimestamp = None
        self.CategoryLevel = None
        self.CategoryPath = None
        self.Tags = None
        self.Author = None
        self.SourceId = None
        self.Title = None
        self.Content = None
        self.ContentUrl = None
        self.VideoDuration = None
        self.Country = None
        self.Province = None
        self.City = None
        self.AuthorFans = None
        self.AuthorLevel = None
        self.CollectCnt = None
        self.PraiseCnt = None
        self.CommentCnt = None
        self.ShareCnt = None
        self.RewardCnt = None
        self.Score = None
        self.Extension = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.ItemType = params.get("ItemType")
        self.Status = params.get("Status")
        self.PublishTimestamp = params.get("PublishTimestamp")
        self.ExpireTimestamp = params.get("ExpireTimestamp")
        self.CategoryLevel = params.get("CategoryLevel")
        self.CategoryPath = params.get("CategoryPath")
        self.Tags = params.get("Tags")
        self.Author = params.get("Author")
        self.SourceId = params.get("SourceId")
        self.Title = params.get("Title")
        self.Content = params.get("Content")
        self.ContentUrl = params.get("ContentUrl")
        self.VideoDuration = params.get("VideoDuration")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.AuthorFans = params.get("AuthorFans")
        self.AuthorLevel = params.get("AuthorLevel")
        self.CollectCnt = params.get("CollectCnt")
        self.PraiseCnt = params.get("PraiseCnt")
        self.CommentCnt = params.get("CommentCnt")
        self.ShareCnt = params.get("ShareCnt")
        self.RewardCnt = params.get("RewardCnt")
        self.Score = params.get("Score")
        self.Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeedBehaviorInfo(AbstractModel):
    """信息流行为

    """

    def __init__(self):
        r"""
        :param UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :type UserId: str
        :param ItemId: 内容唯一id
        :type ItemId: str
        :param BehaviorType: 行为类型：<br> ● expose - 曝光，<b>必须</b><br> ● click - 点击，<b>必须</b><br/>  ● stay - 详情页停留时长，<b>强烈建议</b><br/>  ● videoover - 视频播放时长，<b>强烈建议</b><br/> ●  like - 点赞&喜欢，<b>正效果</b><br/> ● collect - 收藏，<b>正效果</b><br/> ●  share - 转发&分享，<b>正效果</b><br/> ● reward - 打赏，<b>正效果</b><br/> ● unlike - 踩&不喜欢，<b>负效果</b><br/> ●  comment - 评论<br/> 不支持的行为类型，可以映射到未被使用的其他行为类型。如实际业务数据中有私信行为，没有收藏行为，可以将私信行为映射到收藏行为
        :type BehaviorType: str
        :param BehaviorValue: 行为类型对应的行为值：<br/> ● expose - 曝光，固定填1<br/> ● click - 点击，固定填1<br/>  ● stay - 详情页停留时长，填停留秒数，取值[1-86400]<br/>  ● videoover - 视频播放时长，填播放结束的秒数，取值[1-86400]<br/> ●  like - 点赞&喜欢，固定填1<br/> ● collect - 收藏，固定填1<br/> ●  share - 转发&分享，固定填1<br/> ● reward - 打赏，填打赏金额，没有则填1<br/> ● unlike - 踩&不喜欢，填不喜欢的原因，没有则填1<br/> ●  comment - 评论，填评论内容，如“上海加油”
        :type BehaviorValue: str
        :param BehaviorTimestamp: 行为发生的时间戳： 秒级时间戳，尽量实时上报，最长不超过半小时否则会影响推荐结果的准确性
        :type BehaviorTimestamp: int
        :param SceneId: 行为发生的场景ID，在控制台创建场景后获取
        :type SceneId: str
        :param ItemTraceId: 推荐追踪ID，使用推荐结果中返回的ItemTraceId填入。 
注意：如果和推荐结果中的ItemTraceId不同，会影响行为特征归因，影响推荐算法效果
        :type ItemTraceId: str
        :param ItemType: 内容类型，跟内容上报类型一致，用于效果分析，不做内容校验，<b>强烈建议</b>
        :type ItemType: str
        :param ReferrerItemId: 相关推荐场景点击进入详情页的内容id，该字段用来注明行为发生于哪个内容的详情页推荐中，<b>相关推荐场景强烈建议</b>
        :type ReferrerItemId: str
        :param UserIdList: 用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :type UserIdList: list of UserIdInfo
        :param Source: 算法来源： <br>● business 业务自己的算法对照组<br/> ● tencent 腾讯算法<br/> ● other 其他算法<br/>默认为tencent，区分行为来源于哪个算法，<b>用于Poc阶段的效果对比验证</b>
        :type Source: str
        :param Country: 行为发生时的国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”，<b>用作特征</b>
        :type Country: str
        :param Province: 行为发生时的省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”，<b>用作特征</b>
        :type Province: str
        :param City: 行为发生时的城市地区，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，其他国家统一用国际公认城市简称或者城市编码，<b>用作特征</b>
        :type City: str
        :param IP: 行为发生时的客户端ip，<b>用作特征</b>
        :type IP: str
        :param Network: 行为发生时的客户端网络类型，<b>用作特征</b>
        :type Network: str
        :param Platform: 行为发生时的客户端平台，ios/android/h5，<b>用作特征</b>
        :type Platform: str
        :param AppVersion: 行为发生时的客户端app版本，<b>用作特征</b>
        :type AppVersion: str
        :param OsVersion: 行为发生时的操作系统版本，<b>用作特征</b>
        :type OsVersion: str
        :param DeviceModel: 行为发生时的机型，<b>用作特征</b>
        :type DeviceModel: str
        :param Extension: json字符串，<b>用于行为数据的扩展</b>
        :type Extension: str
        """
        self.UserId = None
        self.ItemId = None
        self.BehaviorType = None
        self.BehaviorValue = None
        self.BehaviorTimestamp = None
        self.SceneId = None
        self.ItemTraceId = None
        self.ItemType = None
        self.ReferrerItemId = None
        self.UserIdList = None
        self.Source = None
        self.Country = None
        self.Province = None
        self.City = None
        self.IP = None
        self.Network = None
        self.Platform = None
        self.AppVersion = None
        self.OsVersion = None
        self.DeviceModel = None
        self.Extension = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.ItemId = params.get("ItemId")
        self.BehaviorType = params.get("BehaviorType")
        self.BehaviorValue = params.get("BehaviorValue")
        self.BehaviorTimestamp = params.get("BehaviorTimestamp")
        self.SceneId = params.get("SceneId")
        self.ItemTraceId = params.get("ItemTraceId")
        self.ItemType = params.get("ItemType")
        self.ReferrerItemId = params.get("ReferrerItemId")
        if params.get("UserIdList") is not None:
            self.UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self.UserIdList.append(obj)
        self.Source = params.get("Source")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
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
        


class FeedRecommendRequest(AbstractModel):
    """FeedRecommend请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param SceneId: 场景ID，在控制台创建场景后获取
        :type SceneId: str
        :param UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :type UserId: str
        :param UserIdList: 用户设备ID数组，可传入用户的多个类型ID，用于关联画像信息
        :type UserIdList: list of UserIdInfo
        :param ItemCnt: 推荐返回数量，默认10个，最多支持50个的内容返回。如果有更多数量要求，<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决
        :type ItemCnt: int
        :param CurrentItemId: 当场景是相关推荐时该值必填，场景是非相关推荐时该值无效
        :type CurrentItemId: str
        """
        self.InstanceId = None
        self.SceneId = None
        self.UserId = None
        self.UserIdList = None
        self.ItemCnt = None
        self.CurrentItemId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SceneId = params.get("SceneId")
        self.UserId = params.get("UserId")
        if params.get("UserIdList") is not None:
            self.UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self.UserIdList.append(obj)
        self.ItemCnt = params.get("ItemCnt")
        self.CurrentItemId = params.get("CurrentItemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeedRecommendResponse(AbstractModel):
    """FeedRecommend返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataList: 推荐返回的内容信息列表
        :type DataList: list of RecItemData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = RecItemData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.RequestId = params.get("RequestId")


class FeedUserInfo(AbstractModel):
    """信息流用户信息

    """

    def __init__(self):
        r"""
        :param UserId: 用户唯一ID，客户自定义用户ID，作为一个用户的唯一标识
        :type UserId: str
        :param UserIdList: 用户设备ID数组，可传入用户的多个类型ID，详见UserIdInfo结构体，建议补齐，<b>用于构建用户画像信息</b>
        :type UserIdList: list of UserIdInfo
        :param Tags: 用户标签，多个标签用英文冒号联接，<b>用作特征，强烈建议</b>
        :type Tags: str
        :param DislikeInfoList: 过滤列表，<b>会在推荐结果里过滤掉这类内容</b>
        :type DislikeInfoList: list of DislikeInfo
        :param Age: 用户年龄
        :type Age: int
        :param Gender: 用户性别： 0 - 未知 1 - 男 2 - 女
        :type Gender: int
        :param Degree: 用户学历 ：小学，初中，高中，大专，本科，硕士，博士
        :type Degree: str
        :param School: 用户毕业学校全称
        :type School: str
        :param Occupation: 用户职业
        :type Occupation: str
        :param Industry: 用户所属行业
        :type Industry: str
        :param ResidentCountry: 用户常驻国家，ISO 3166-1 alpha-2编码，参考<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2" target="_blank">ISO 3166-1 alpha-2</a>，中国：“CN”
        :type ResidentCountry: str
        :param ResidentProvince: 用户常驻省份，ISO 3166-2行政区编码，如中国参考<a href="https://zh.wikipedia.org/wiki/ISO_3166-2:CN" target="_blank">ISO_3166-2:CN</a>，广东省：“CN-GD”
        :type ResidentProvince: str
        :param ResidentCity: 用户常驻城市，统一用国家最新标准地区行政编码，如：<a href="https://www.mca.gov.cn/article/sj/xzqh/2020/" target="_blank">2020年行政区编码</a>，
        :type ResidentCity: str
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
        :param Extension: json字符串，用于画像数据的扩展
        :type Extension: str
        """
        self.UserId = None
        self.UserIdList = None
        self.Tags = None
        self.DislikeInfoList = None
        self.Age = None
        self.Gender = None
        self.Degree = None
        self.School = None
        self.Occupation = None
        self.Industry = None
        self.ResidentCountry = None
        self.ResidentProvince = None
        self.ResidentCity = None
        self.RegisterTimestamp = None
        self.MembershipLevel = None
        self.LastLoginTimestamp = None
        self.LastLoginIp = None
        self.LastModifyTimestamp = None
        self.Extension = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        if params.get("UserIdList") is not None:
            self.UserIdList = []
            for item in params.get("UserIdList"):
                obj = UserIdInfo()
                obj._deserialize(item)
                self.UserIdList.append(obj)
        self.Tags = params.get("Tags")
        if params.get("DislikeInfoList") is not None:
            self.DislikeInfoList = []
            for item in params.get("DislikeInfoList"):
                obj = DislikeInfo()
                obj._deserialize(item)
                self.DislikeInfoList.append(obj)
        self.Age = params.get("Age")
        self.Gender = params.get("Gender")
        self.Degree = params.get("Degree")
        self.School = params.get("School")
        self.Occupation = params.get("Occupation")
        self.Industry = params.get("Industry")
        self.ResidentCountry = params.get("ResidentCountry")
        self.ResidentProvince = params.get("ResidentProvince")
        self.ResidentCity = params.get("ResidentCity")
        self.RegisterTimestamp = params.get("RegisterTimestamp")
        self.MembershipLevel = params.get("MembershipLevel")
        self.LastLoginTimestamp = params.get("LastLoginTimestamp")
        self.LastLoginIp = params.get("LastLoginIp")
        self.LastModifyTimestamp = params.get("LastModifyTimestamp")
        self.Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecItemData(AbstractModel):
    """推荐返回的内容信息

    """

    def __init__(self):
        r"""
        :param ItemId: 推荐的内容ID
        :type ItemId: str
        :param ItemType: 内容类型，同内容上报类型一致
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemType: str
        :param ItemTraceId: 推荐追踪id，本次推荐内容产生的后续行为上报均要用该ItemTraceId上报。每次接口调用返回的ItemTraceId不同
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemTraceId: str
        :param Score: 推荐结果分，取值范围[0,1000000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self.ItemId = None
        self.ItemType = None
        self.ItemTraceId = None
        self.Score = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.ItemType = params.get("ItemType")
        self.ItemTraceId = params.get("ItemTraceId")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedBehaviorRequest(AbstractModel):
    """ReportFeedBehavior请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param FeedBehaviorList: 上报的行为数据数组，数量不超过50
        :type FeedBehaviorList: list of FeedBehaviorInfo
        """
        self.InstanceId = None
        self.FeedBehaviorList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FeedBehaviorList") is not None:
            self.FeedBehaviorList = []
            for item in params.get("FeedBehaviorList"):
                obj = FeedBehaviorInfo()
                obj._deserialize(item)
                self.FeedBehaviorList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedBehaviorResponse(AbstractModel):
    """ReportFeedBehavior返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReportFeedItemRequest(AbstractModel):
    """ReportFeedItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param FeedItemList: 上报的信息流内容数组，一次数量不超过50
        :type FeedItemList: list of DocItem
        """
        self.InstanceId = None
        self.FeedItemList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FeedItemList") is not None:
            self.FeedItemList = []
            for item in params.get("FeedItemList"):
                obj = DocItem()
                obj._deserialize(item)
                self.FeedItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedItemResponse(AbstractModel):
    """ReportFeedItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReportFeedUserRequest(AbstractModel):
    """ReportFeedUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID，在控制台获取
        :type InstanceId: str
        :param FeedUserList: 上报的用户信息数组，数量不超过50
        :type FeedUserList: list of FeedUserInfo
        """
        self.InstanceId = None
        self.FeedUserList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("FeedUserList") is not None:
            self.FeedUserList = []
            for item in params.get("FeedUserList"):
                obj = FeedUserInfo()
                obj._deserialize(item)
                self.FeedUserList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFeedUserResponse(AbstractModel):
    """ReportFeedUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserIdInfo(AbstractModel):
    """用户ID信息

    """

    def __init__(self):
        r"""
        :param Type: 用户ID类型： <br/>● qq: qq号码 <br/>● qq_md5：qq的md5值 <br/>● imei：设备imei <br/>● imei_md5：imei的md5值 <br/>● idfa: Apple 向用户设备随机分配的设备标识符 <br/>● idfa_md5：idfa的md5值 <br/>● oaid：安卓10之后一种非永久性设备标识符 <br/>● oaid_md5：md5后的oaid <br/>● wx_openid：微信openid <br/>● qq_openid：QQ的openid <br/>● phone：电话号码 <br/>● phone_md5：md5后的电话号码 <br/>● phone_sha256：SHA256加密的手机号 <br/>● phone_sm3：国密SM3加密的手机号 <br/>（如当前类型不满足，请<a href="https://console.cloud.tencent.com/workorder/category" target="_blank">提单</a>沟通解决方案）
        :type Type: str
        :param Value: 用户ID值
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
        