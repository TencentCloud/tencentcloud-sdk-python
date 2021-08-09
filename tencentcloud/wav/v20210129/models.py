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


class ActivityDetail(AbstractModel):
    """活动详情

    """

    def __init__(self):
        """
        :param ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityId: int\n        :param ActivityName: 活动名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityName: str\n        :param ActivityState: 活动状态，10:未开始状态、20:已开始（进行中）状态、30:已结束状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityState: int\n        :param ActivityType: 活动类型，100:留资活动
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityType: int\n        :param StartTime: 活动开始时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTime: int\n        :param EndTime: 活动结束时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: int\n        :param MainPhoto: 活动主图
注意：此字段可能返回 null，表示取不到有效值。\n        :type MainPhoto: str\n        :param PrivacyAgreementId: 协议编号
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivacyAgreementId: str\n        :param UpdateTime: 活动更新时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        :param ActivityDataList: 活动数据列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityDataList: str\n        """
        self.ActivityId = None
        self.ActivityName = None
        self.ActivityState = None
        self.ActivityType = None
        self.StartTime = None
        self.EndTime = None
        self.MainPhoto = None
        self.PrivacyAgreementId = None
        self.UpdateTime = None
        self.ActivityDataList = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.ActivityName = params.get("ActivityName")
        self.ActivityState = params.get("ActivityState")
        self.ActivityType = params.get("ActivityType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MainPhoto = params.get("MainPhoto")
        self.PrivacyAgreementId = params.get("PrivacyAgreementId")
        self.UpdateTime = params.get("UpdateTime")
        self.ActivityDataList = params.get("ActivityDataList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivityJoinDetail(AbstractModel):
    """活动参与详情

    """

    def __init__(self):
        """
        :param ActivityId: 活动id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityId: int\n        :param ActivityName: 活动名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityName: str\n        :param SalesName: 销售姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesName: str\n        :param SalesPhone: 销售电话
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesPhone: str\n        :param JoinId: 参与id
注意：此字段可能返回 null，表示取不到有效值。\n        :type JoinId: int\n        :param LiveCodeId: 活码id
注意：此字段可能返回 null，表示取不到有效值。\n        :type LiveCodeId: int\n        :param UserPhone: 用户电话
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserPhone: str\n        :param UserName: 用户姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserName: str\n        :param ActivityData: 活动数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActivityData: str\n        :param LeadId: 线索id
注意：此字段可能返回 null，表示取不到有效值。\n        :type LeadId: int\n        :param JoinTime: 参与时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type JoinTime: int\n        :param Duplicate: 线索是否是重复创建， 0 ：新建、 1：合并、 2：重复， 默认为0
注意：此字段可能返回 null，表示取不到有效值。\n        :type Duplicate: int\n        :param DuplicateLeadId: 重复线索id
注意：此字段可能返回 null，表示取不到有效值。\n        :type DuplicateLeadId: int\n        :param JoinState: 是否为参与多次活动， 1：参与一次、2、参与多次，默认为0
注意：此字段可能返回 null，表示取不到有效值。\n        :type JoinState: int\n        :param CreateTime: 创建时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param UpdateTime: 更新时间戳，单位：秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: int\n        """
        self.ActivityId = None
        self.ActivityName = None
        self.SalesName = None
        self.SalesPhone = None
        self.JoinId = None
        self.LiveCodeId = None
        self.UserPhone = None
        self.UserName = None
        self.ActivityData = None
        self.LeadId = None
        self.JoinTime = None
        self.Duplicate = None
        self.DuplicateLeadId = None
        self.JoinState = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.ActivityName = params.get("ActivityName")
        self.SalesName = params.get("SalesName")
        self.SalesPhone = params.get("SalesPhone")
        self.JoinId = params.get("JoinId")
        self.LiveCodeId = params.get("LiveCodeId")
        self.UserPhone = params.get("UserPhone")
        self.UserName = params.get("UserName")
        self.ActivityData = params.get("ActivityData")
        self.LeadId = params.get("LeadId")
        self.JoinTime = params.get("JoinTime")
        self.Duplicate = params.get("Duplicate")
        self.DuplicateLeadId = params.get("DuplicateLeadId")
        self.JoinState = params.get("JoinState")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelCodeInnerDetail(AbstractModel):
    """渠道活码详情

    """

    def __init__(self):
        """
        :param Id: 渠道活码id\n        :type Id: int\n        :param Type: 欢迎语类型，0：普通欢迎语、1:渠道欢迎语\n        :type Type: int\n        :param Source: 渠道来源\n        :type Source: str\n        :param SourceName: 渠道来源名称\n        :type SourceName: str\n        :param Name: 二维码名称\n        :type Name: str\n        :param UseUserIdList: 使用成员用户id集\n        :type UseUserIdList: list of int\n        :param UseUserOpenIdList: 使用成员企微账号id集\n        :type UseUserOpenIdList: list of str\n        :param TagList: 标签\n        :type TagList: list of WeComTagDetail\n        :param SkipVerify: 自动通过好友，0：开启、1：关闭，默认0开启\n        :type SkipVerify: int\n        :param Friends: 添加好友人数\n        :type Friends: int\n        :param Remark: 备注\n        :type Remark: str\n        :param MsgId: 欢迎语id（通过欢迎语新增返回的id）\n        :type MsgId: int\n        :param ConfigId: 联系我config_id\n        :type ConfigId: str\n        :param QrCodeUrl: 联系我二维码地址\n        :type QrCodeUrl: str\n        :param RecStatus: 记录状态， 0：有效、1：无效\n        :type RecStatus: int\n        :param AppId: 应用ID\n        :type AppId: str\n        """
        self.Id = None
        self.Type = None
        self.Source = None
        self.SourceName = None
        self.Name = None
        self.UseUserIdList = None
        self.UseUserOpenIdList = None
        self.TagList = None
        self.SkipVerify = None
        self.Friends = None
        self.Remark = None
        self.MsgId = None
        self.ConfigId = None
        self.QrCodeUrl = None
        self.RecStatus = None
        self.AppId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Source = params.get("Source")
        self.SourceName = params.get("SourceName")
        self.Name = params.get("Name")
        self.UseUserIdList = params.get("UseUserIdList")
        self.UseUserOpenIdList = params.get("UseUserOpenIdList")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = WeComTagDetail()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.SkipVerify = params.get("SkipVerify")
        self.Friends = params.get("Friends")
        self.Remark = params.get("Remark")
        self.MsgId = params.get("MsgId")
        self.ConfigId = params.get("ConfigId")
        self.QrCodeUrl = params.get("QrCodeUrl")
        self.RecStatus = params.get("RecStatus")
        self.AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatArchivingDetail(AbstractModel):
    """会话存档数据详情

    """

    def __init__(self):
        """
        :param MsgId: 消息id\n        :type MsgId: str\n        :param Action: 动作名称，switch表示切换企微账号，send表示企微普通消息\n        :type Action: str\n        :param MsgType: 消息类型，当Action != "switch"时存在，例如video, text, voice 等，和企微开放文档一一对应
https://open.work.weixin.qq.com/api/doc/90000/90135/91774
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgType: str\n        :param From: 消息发送人
注意：此字段可能返回 null，表示取不到有效值。\n        :type From: str\n        :param ToList: 消息接收人列表，注意接收人可能只有一个
注意：此字段可能返回 null，表示取不到有效值。\n        :type ToList: list of str\n        :param RoomId: 如果是群消息，则不为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type RoomId: str\n        :param MsgTime: 消息发送的时间戳，单位为秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgTime: int\n        :param Video: MsgType=video时的消息体，忽略此字段，见BodyJson字段
注意：此字段可能返回 null，表示取不到有效值。\n        :type Video: :class:`tencentcloud.wav.v20210129.models.ChatArchivingMsgTypeVideo`\n        :param BodyJson: 根据MsgType的不同取值，解析内容不同，参考：https://open.work.weixin.qq.com/api/doc/90000/90135/91774
注意：此字段可能返回 null，表示取不到有效值。\n        :type BodyJson: str\n        """
        self.MsgId = None
        self.Action = None
        self.MsgType = None
        self.From = None
        self.ToList = None
        self.RoomId = None
        self.MsgTime = None
        self.Video = None
        self.BodyJson = None


    def _deserialize(self, params):
        self.MsgId = params.get("MsgId")
        self.Action = params.get("Action")
        self.MsgType = params.get("MsgType")
        self.From = params.get("From")
        self.ToList = params.get("ToList")
        self.RoomId = params.get("RoomId")
        self.MsgTime = params.get("MsgTime")
        if params.get("Video") is not None:
            self.Video = ChatArchivingMsgTypeVideo()
            self.Video._deserialize(params.get("Video"))
        self.BodyJson = params.get("BodyJson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatArchivingMsgTypeVideo(AbstractModel):
    """会话存档的视频消息类型

    """

    def __init__(self):
        """
        :param PlayLength: 视频时长，单位秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type PlayLength: int\n        :param FileSize: 文件大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSize: int\n        :param CosKey: 视频资源对象Cos下载地址\n        :type CosKey: str\n        """
        self.PlayLength = None
        self.FileSize = None
        self.CosKey = None


    def _deserialize(self, params):
        self.PlayLength = params.get("PlayLength")
        self.FileSize = params.get("FileSize")
        self.CosKey = params.get("CosKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelCodeRequest(AbstractModel):
    """CreateChannelCode请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 欢迎语类型:0普通欢迎语,1渠道欢迎语\n        :type Type: int\n        :param UseUserId: 使用成员用户id集\n        :type UseUserId: list of int\n        :param UseUserOpenId: 使用成员企微账号id集\n        :type UseUserOpenId: list of str\n        :param AppIds: 应用ID,字典表中的APP_TYPE值,多个已逗号分隔\n        :type AppIds: str\n        :param Source: 渠道来源\n        :type Source: str\n        :param SourceName: 渠道来源名称\n        :type SourceName: str\n        :param Name: 二维码名称\n        :type Name: str\n        :param Tag: 标签\n        :type Tag: list of WeComTagDetail\n        :param SkipVerify: 自动通过好友：0开启 1关闭, 默认开启\n        :type SkipVerify: int\n        :param MsgId: 欢迎语id（通过欢迎语新增返回的id）\n        :type MsgId: int\n        :param Remark: 备注\n        :type Remark: str\n        :param SourceType: 渠道类型 0 未知 1 公域 2私域\n        :type SourceType: int\n        """
        self.Type = None
        self.UseUserId = None
        self.UseUserOpenId = None
        self.AppIds = None
        self.Source = None
        self.SourceName = None
        self.Name = None
        self.Tag = None
        self.SkipVerify = None
        self.MsgId = None
        self.Remark = None
        self.SourceType = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.UseUserId = params.get("UseUserId")
        self.UseUserOpenId = params.get("UseUserOpenId")
        self.AppIds = params.get("AppIds")
        self.Source = params.get("Source")
        self.SourceName = params.get("SourceName")
        self.Name = params.get("Name")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = WeComTagDetail()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.SkipVerify = params.get("SkipVerify")
        self.MsgId = params.get("MsgId")
        self.Remark = params.get("Remark")
        self.SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateChannelCodeResponse(AbstractModel):
    """CreateChannelCode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCorpTagRequest(AbstractModel):
    """CreateCorpTag请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 标签组名称，最长为15个字符\n        :type GroupName: str\n        :param Tags: 标签信息数组\n        :type Tags: list of TagInfo\n        :param Sort: 标签组次序值。sort值大的排序靠前。有效的值范围是[0, 2^32)\n        :type Sort: int\n        """
        self.GroupName = None
        self.Tags = None
        self.Sort = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorpTagResponse(AbstractModel):
    """CreateCorpTag返回参数结构体

    """

    def __init__(self):
        """
        :param TagGroup: 标签组信息\n        :type TagGroup: :class:`tencentcloud.wav.v20210129.models.TagGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TagGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TagGroup") is not None:
            self.TagGroup = TagGroup()
            self.TagGroup._deserialize(params.get("TagGroup"))
        self.RequestId = params.get("RequestId")


class ExternalContact(AbstractModel):
    """客户信息

    """

    def __init__(self):
        """
        :param ExternalUserId: 外部联系人的userId\n        :type ExternalUserId: str\n        :param Gender: 外部联系人性别 0-未知 1-男性 2-女性\n        :type Gender: int\n        :param Name: 外部联系人的名称\n        :type Name: str\n        :param Type: 外部联系人的类型，1表示该外部联系人是微信用户，2表示该外部联系人是企业微信用户\n        :type Type: int\n        :param UnionId: 外部联系人在微信开放平台的唯一身份标识（微信unionid），通过此字段企业可将外部联系人与公众号/小程序用户关联起来。仅当联系人类型是微信用户，且企业或第三方服务商绑定了微信开发者ID有此字段。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnionId: str\n        :param Phone: 外部联系人联系电话
注意：此字段可能返回 null，表示取不到有效值。\n        :type Phone: str\n        """
        self.ExternalUserId = None
        self.Gender = None
        self.Name = None
        self.Type = None
        self.UnionId = None
        self.Phone = None


    def _deserialize(self, params):
        self.ExternalUserId = params.get("ExternalUserId")
        self.Gender = params.get("Gender")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.UnionId = params.get("UnionId")
        self.Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalContactSimpleInfo(AbstractModel):
    """列部联系人简短信息

    """

    def __init__(self):
        """
        :param ExternalUserId: 外部联系人的userId\n        :type ExternalUserId: str\n        :param UserId: 添加了此外部联系人的企业成员userId\n        :type UserId: str\n        :param SalesName: 添加了此外部联系人的企业成员的姓名
注意：此字段可能返回 null，表示取不到有效值。\n        :type SalesName: str\n        """
        self.ExternalUserId = None
        self.UserId = None
        self.SalesName = None


    def _deserialize(self, params):
        self.ExternalUserId = params.get("ExternalUserId")
        self.UserId = params.get("UserId")
        self.SalesName = params.get("SalesName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalContactTag(AbstractModel):
    """外部联系人标签

    """

    def __init__(self):
        """
        :param GroupName: 该成员添加此外部联系人所打标签的分组名称（标签功能需要企业微信升级到2.7.5及以上版本）
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param TagName: 该成员添加此外部联系人所打标签名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagName: str\n        :param Type: 该成员添加此外部联系人所打标签类型, 1-企业设置, 2-用户自定义
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param TagId: 该成员添加此外部联系人所打企业标签的id，仅企业设置（type为1）的标签返回
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagId: str\n        """
        self.GroupName = None
        self.TagName = None
        self.Type = None
        self.TagId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.TagName = params.get("TagName")
        self.Type = params.get("Type")
        self.TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalUserMappingInfo(AbstractModel):
    """外部联系人映射信息

    """

    def __init__(self):
        """
        :param CorpExternalUserId: 企业主体对应的外部联系人userId\n        :type CorpExternalUserId: str\n        :param ExternalUserId: 乐销车应用主体对应的外部联系人, 当不存在好友关系时，该字段值为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalUserId: str\n        """
        self.CorpExternalUserId = None
        self.ExternalUserId = None


    def _deserialize(self, params):
        self.CorpExternalUserId = params.get("CorpExternalUserId")
        self.ExternalUserId = params.get("ExternalUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowUser(AbstractModel):
    """添加了此外部联系人的企业成员信息

    """

    def __init__(self):
        """
        :param UserId: 添加了此外部联系人的企业成员userid\n        :type UserId: str\n        :param Remark: 该成员对此外部联系人的备注
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param Description: 该成员对此外部联系人的描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param CreateTime: 该成员添加此外部联系人的时间戳，单位为秒\n        :type CreateTime: int\n        :param AddWay: 该成员添加此客户的来源，具体含义详见<a href="https://work.weixin.qq.com/api/doc/90000/90135/92114#%E6%9D%A5%E6%BA%90%E5%AE%9A%E4%B9%89">来源定义</a>\n        :type AddWay: int\n        :param OperUserId: 发起添加的userid，如果成员主动添加，为成员的userid；如果是客户主动添加，则为客户的外部联系人userid；如果是内部成员共享/管理员分配，则为对应的成员/管理员userid\n        :type OperUserId: str\n        :param Tags: 该成员添加此外部联系人所打标签信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of ExternalContactTag\n        """
        self.UserId = None
        self.Remark = None
        self.Description = None
        self.CreateTime = None
        self.AddWay = None
        self.OperUserId = None
        self.Tags = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Remark = params.get("Remark")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.AddWay = params.get("AddWay")
        self.OperUserId = params.get("OperUserId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ExternalContactTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LicenseInfo(AbstractModel):
    """license相关信息

    """

    def __init__(self):
        """
        :param License: license编号\n        :type License: str\n        :param LicenseEdition: license版本；1-基础版，2-标准版，3-增值版\n        :type LicenseEdition: int\n        :param ResourceStartTime: 生效开始时间, 格式yyyy-MM-dd HH:mm:ss\n        :type ResourceStartTime: str\n        :param ResourceEndTime: 生效结束时间, 格式yyyy-MM-dd HH:mm:ss\n        :type ResourceEndTime: str\n        :param IsolationDeadline: 隔离截止时间, 格式yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsolationDeadline: str\n        :param DestroyTime: 资源计划销毁时间, 格式yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。\n        :type DestroyTime: str\n        :param Status: 资源状态，1.正常，2.隔离，3.销毁\n        :type Status: int\n        :param Extra: 扩展信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Extra: str\n        """
        self.License = None
        self.LicenseEdition = None
        self.ResourceStartTime = None
        self.ResourceEndTime = None
        self.IsolationDeadline = None
        self.DestroyTime = None
        self.Status = None
        self.Extra = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.LicenseEdition = params.get("LicenseEdition")
        self.ResourceStartTime = params.get("ResourceStartTime")
        self.ResourceEndTime = params.get("ResourceEndTime")
        self.IsolationDeadline = params.get("IsolationDeadline")
        self.DestroyTime = params.get("DestroyTime")
        self.Status = params.get("Status")
        self.Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveCodeDetail(AbstractModel):
    """活动活码详情

    """

    def __init__(self):
        """
        :param LiveCodeId: 活码id\n        :type LiveCodeId: int\n        :param LiveCodeName: 活码名称\n        :type LiveCodeName: str\n        :param ShortChainAddress: 短链url
注意：此字段可能返回 null，表示取不到有效值。\n        :type ShortChainAddress: str\n        :param LiveCodePreview: 活码二维码
注意：此字段可能返回 null，表示取不到有效值。\n        :type LiveCodePreview: str\n        :param ActivityId: 活动id\n        :type ActivityId: int\n        :param ActivityName: 活动名称\n        :type ActivityName: str\n        :param LiveCodeState: 活码状态，-1：删除，0：启用，1禁用，默认为0\n        :type LiveCodeState: int\n        :param LiveCodeData: 活码参数，每个活码参数都是不一样的， 这个的值对应的是字符串json类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type LiveCodeData: str\n        :param CreateTime: 创建时间戳，单位为秒\n        :type CreateTime: int\n        :param UpdateTime: 更新时间戳，单位为秒\n        :type UpdateTime: int\n        """
        self.LiveCodeId = None
        self.LiveCodeName = None
        self.ShortChainAddress = None
        self.LiveCodePreview = None
        self.ActivityId = None
        self.ActivityName = None
        self.LiveCodeState = None
        self.LiveCodeData = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.LiveCodeId = params.get("LiveCodeId")
        self.LiveCodeName = params.get("LiveCodeName")
        self.ShortChainAddress = params.get("ShortChainAddress")
        self.LiveCodePreview = params.get("LiveCodePreview")
        self.ActivityId = params.get("ActivityId")
        self.ActivityName = params.get("ActivityName")
        self.LiveCodeState = params.get("LiveCodeState")
        self.LiveCodeData = params.get("LiveCodeData")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MiniAppCodeInfo(AbstractModel):
    """小程序码信息

    """

    def __init__(self):
        """
        :param Id: 主键id\n        :type Id: int\n        :param MiniAppName: 小程序名称\n        :type MiniAppName: str\n        :param MiniAppLogo: 小程序logo\n        :type MiniAppLogo: str\n        :param MiniAdminUrl: 小程序管理端地址\n        :type MiniAdminUrl: str\n        :param State: 状态：0正常，1删除\n        :type State: int\n        :param CreateTime: 创建时间戳，单位为秒\n        :type CreateTime: int\n        :param UpdateTime: 更新时间戳，单位为秒\n        :type UpdateTime: int\n        """
        self.Id = None
        self.MiniAppName = None
        self.MiniAppLogo = None
        self.MiniAdminUrl = None
        self.State = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MiniAppName = params.get("MiniAppName")
        self.MiniAppLogo = params.get("MiniAppLogo")
        self.MiniAdminUrl = params.get("MiniAdminUrl")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityJoinListRequest(AbstractModel):
    """QueryActivityJoinList请求参数结构体

    """

    def __init__(self):
        """
        :param ActivityId: 活动id\n        :type ActivityId: int\n        :param Cursor: 分页游标，对应结果返回的NextCursor,首次请求保持为空\n        :type Cursor: str\n        :param Limit: 单页数据限制\n        :type Limit: int\n        """
        self.ActivityId = None
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityJoinListResponse(AbstractModel):
    """QueryActivityJoinList返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageData: list of ActivityJoinDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextCursor = None
        self.PageData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self.PageData = []
            for item in params.get("PageData"):
                obj = ActivityJoinDetail()
                obj._deserialize(item)
                self.PageData.append(obj)
        self.RequestId = params.get("RequestId")


class QueryActivityListRequest(AbstractModel):
    """QueryActivityList请求参数结构体

    """

    def __init__(self):
        """
        :param Cursor: 分页游标，对应结果返回的NextCursor,首次请求保持为空\n        :type Cursor: str\n        :param Limit: 单页数据限制\n        :type Limit: int\n        """
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityListResponse(AbstractModel):
    """QueryActivityList返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageData: list of ActivityDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextCursor = None
        self.PageData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self.PageData = []
            for item in params.get("PageData"):
                obj = ActivityDetail()
                obj._deserialize(item)
                self.PageData.append(obj)
        self.RequestId = params.get("RequestId")


class QueryActivityLiveCodeListRequest(AbstractModel):
    """QueryActivityLiveCodeList请求参数结构体

    """

    def __init__(self):
        """
        :param Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填\n        :type Cursor: str\n        :param Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值\n        :type Limit: int\n        """
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryActivityLiveCodeListResponse(AbstractModel):
    """QueryActivityLiveCodeList返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageData: list of LiveCodeDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextCursor = None
        self.PageData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self.PageData = []
            for item in params.get("PageData"):
                obj = LiveCodeDetail()
                obj._deserialize(item)
                self.PageData.append(obj)
        self.RequestId = params.get("RequestId")


class QueryChannelCodeListRequest(AbstractModel):
    """QueryChannelCodeList请求参数结构体

    """

    def __init__(self):
        """
        :param Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填\n        :type Cursor: str\n        :param Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值\n        :type Limit: int\n        """
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChannelCodeListResponse(AbstractModel):
    """QueryChannelCodeList返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageData: list of ChannelCodeInnerDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextCursor = None
        self.PageData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self.PageData = []
            for item in params.get("PageData"):
                obj = ChannelCodeInnerDetail()
                obj._deserialize(item)
                self.PageData.append(obj)
        self.RequestId = params.get("RequestId")


class QueryChatArchivingListRequest(AbstractModel):
    """QueryChatArchivingList请求参数结构体

    """

    def __init__(self):
        """
        :param Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填\n        :type Cursor: str\n        :param Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值\n        :type Limit: int\n        """
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryChatArchivingListResponse(AbstractModel):
    """QueryChatArchivingList返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param PageData: 会话存档列表响应参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageData: list of ChatArchivingDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextCursor = None
        self.PageData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self.PageData = []
            for item in params.get("PageData"):
                obj = ChatArchivingDetail()
                obj._deserialize(item)
                self.PageData.append(obj)
        self.RequestId = params.get("RequestId")


class QueryExternalContactDetailRequest(AbstractModel):
    """QueryExternalContactDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ExternalUserId: 外部联系人的userid，注意不是企业成员的帐号\n        :type ExternalUserId: str\n        :param Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填。当客户在企业内的跟进人超过500人时需要使用cursor参数进行分页获取\n        :type Cursor: str\n        :param Limit: 当前接口Limit不需要传参， 保留Limit只是为了保持向后兼容性， Limit默认值为500，当返回结果超过500时， NextCursor才有返回值\n        :type Limit: int\n        """
        self.ExternalUserId = None
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.ExternalUserId = params.get("ExternalUserId")
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalContactDetailResponse(AbstractModel):
    """QueryExternalContactDetail返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param Customer: 客户信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Customer: :class:`tencentcloud.wav.v20210129.models.ExternalContact`\n        :param FollowUser: 添加了此外部联系人的企业成员信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowUser: list of FollowUser\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextCursor = None
        self.Customer = None
        self.FollowUser = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextCursor = params.get("NextCursor")
        if params.get("Customer") is not None:
            self.Customer = ExternalContact()
            self.Customer._deserialize(params.get("Customer"))
        if params.get("FollowUser") is not None:
            self.FollowUser = []
            for item in params.get("FollowUser"):
                obj = FollowUser()
                obj._deserialize(item)
                self.FollowUser.append(obj)
        self.RequestId = params.get("RequestId")


class QueryExternalContactListRequest(AbstractModel):
    """QueryExternalContactList请求参数结构体

    """

    def __init__(self):
        """
        :param Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填\n        :type Cursor: str\n        :param Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值\n        :type Limit: int\n        """
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalContactListResponse(AbstractModel):
    """QueryExternalContactList返回参数结构体

    """

    def __init__(self):
        """
        :param PageData: 外部联系人信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageData: list of ExternalContactSimpleInfo\n        :param NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PageData = None
        self.NextCursor = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PageData") is not None:
            self.PageData = []
            for item in params.get("PageData"):
                obj = ExternalContactSimpleInfo()
                obj._deserialize(item)
                self.PageData.append(obj)
        self.NextCursor = params.get("NextCursor")
        self.RequestId = params.get("RequestId")


class QueryExternalUserMappingInfoRequest(AbstractModel):
    """QueryExternalUserMappingInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CorpExternalUserIdList: 企业主体对应的外部联系人id列表，列表长度限制最大为50。\n        :type CorpExternalUserIdList: list of str\n        """
        self.CorpExternalUserIdList = None


    def _deserialize(self, params):
        self.CorpExternalUserIdList = params.get("CorpExternalUserIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalUserMappingInfoResponse(AbstractModel):
    """QueryExternalUserMappingInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ExternalUserIdMapping: 外部联系人映射信息, 只返回映射成功的记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExternalUserIdMapping: list of ExternalUserMappingInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ExternalUserIdMapping = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ExternalUserIdMapping") is not None:
            self.ExternalUserIdMapping = []
            for item in params.get("ExternalUserIdMapping"):
                obj = ExternalUserMappingInfo()
                obj._deserialize(item)
                self.ExternalUserIdMapping.append(obj)
        self.RequestId = params.get("RequestId")


class QueryLicenseInfoRequest(AbstractModel):
    """QueryLicenseInfo请求参数结构体

    """

    def __init__(self):
        """
        :param License: license编号\n        :type License: str\n        """
        self.License = None


    def _deserialize(self, params):
        self.License = params.get("License")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryLicenseInfoResponse(AbstractModel):
    """QueryLicenseInfo返回参数结构体

    """

    def __init__(self):
        """
        :param LicenseInfo: license响应信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type LicenseInfo: :class:`tencentcloud.wav.v20210129.models.LicenseInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LicenseInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LicenseInfo") is not None:
            self.LicenseInfo = LicenseInfo()
            self.LicenseInfo._deserialize(params.get("LicenseInfo"))
        self.RequestId = params.get("RequestId")


class QueryMiniAppCodeListRequest(AbstractModel):
    """QueryMiniAppCodeList请求参数结构体

    """

    def __init__(self):
        """
        :param Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填\n        :type Cursor: str\n        :param Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值\n        :type Limit: int\n        """
        self.Cursor = None
        self.Limit = None


    def _deserialize(self, params):
        self.Cursor = params.get("Cursor")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMiniAppCodeListResponse(AbstractModel):
    """QueryMiniAppCodeList返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextCursor: str\n        :param PageData: 小程序码列表响应数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageData: list of MiniAppCodeInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NextCursor = None
        self.PageData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NextCursor = params.get("NextCursor")
        if params.get("PageData") is not None:
            self.PageData = []
            for item in params.get("PageData"):
                obj = MiniAppCodeInfo()
                obj._deserialize(item)
                self.PageData.append(obj)
        self.RequestId = params.get("RequestId")


class TagDetailInfo(AbstractModel):
    """标签详细信息

    """

    def __init__(self):
        """
        :param TagName: 标签名称\n        :type TagName: str\n        :param BizTagId: 标签业务ID\n        :type BizTagId: str\n        :param TagId: 企微标签ID\n        :type TagId: str\n        :param Sort: 标签排序的次序值，sort值大的排序靠前。有效的值范围是[0, 2^32)\n        :type Sort: int\n        :param CreateTime: 标签创建时间,单位为秒\n        :type CreateTime: int\n        """
        self.TagName = None
        self.BizTagId = None
        self.TagId = None
        self.Sort = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TagName = params.get("TagName")
        self.BizTagId = params.get("BizTagId")
        self.TagId = params.get("TagId")
        self.Sort = params.get("Sort")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagGroup(AbstractModel):
    """标签组信息

    """

    def __init__(self):
        """
        :param GroupId: 企微标签组id\n        :type GroupId: str\n        :param BizGroupId: 标签组业务id\n        :type BizGroupId: str\n        :param GroupName: 企微标签组名称，不能超过15个字符\n        :type GroupName: str\n        :param Sort: 标签组次序值。sort值大的排序靠前。有效的值范围是[0, 2^32)\n        :type Sort: int\n        :param CreateTime: 标签组创建时间,单位为秒\n        :type CreateTime: int\n        :param Tags: 标签组内的标签列表, 上限为20\n        :type Tags: list of TagDetailInfo\n        """
        self.GroupId = None
        self.BizGroupId = None
        self.GroupName = None
        self.Sort = None
        self.CreateTime = None
        self.Tags = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.BizGroupId = params.get("BizGroupId")
        self.GroupName = params.get("GroupName")
        self.Sort = params.get("Sort")
        self.CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagDetailInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息

    """

    def __init__(self):
        """
        :param TagName: 标签名称, 最大长度限制15个字符\n        :type TagName: str\n        :param Sort: 标签组排序,值越大,排序越靠前\n        :type Sort: int\n        """
        self.TagName = None
        self.Sort = None


    def _deserialize(self, params):
        self.TagName = params.get("TagName")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeComTagDetail(AbstractModel):
    """企微个人标签信息,渠道活码使用

    """

    def __init__(self):
        """
        :param GroupName: 标签分组名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupName: str\n        :param BizGroupId: 标签分组业务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type BizGroupId: str\n        :param TagName: 标签名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagName: str\n        :param TagId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagId: str\n        :param BizTagId: 标签业务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type BizTagId: str\n        :param Type: 标签分类，1：企业设置、2：用户自定义
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param BizTagIdStr: 标签业务ID字符串格式
注意：此字段可能返回 null，表示取不到有效值。\n        :type BizTagIdStr: str\n        """
        self.GroupName = None
        self.BizGroupId = None
        self.TagName = None
        self.TagId = None
        self.BizTagId = None
        self.Type = None
        self.BizTagIdStr = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.BizGroupId = params.get("BizGroupId")
        self.TagName = params.get("TagName")
        self.TagId = params.get("TagId")
        self.BizTagId = params.get("BizTagId")
        self.Type = params.get("Type")
        self.BizTagIdStr = params.get("BizTagIdStr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        