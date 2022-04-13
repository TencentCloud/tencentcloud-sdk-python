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


class GetIndustryV1HomeMembersReqPayload(AbstractModel):
    """获取成员列表入参payload

    """

    def __init__(self):
        r"""
        :param ID: 用户ID
        :type ID: str
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRequest(AbstractModel):
    """GetIndustryV1HomeMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Payload: 无
        :type Payload: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersReqPayload`
        :param Metadata: 无
        :type Metadata: :class:`tencentcloud.icr.v20211014.models.ReqMetadata`
        """
        self.Payload = None
        self.Metadata = None


    def _deserialize(self, params):
        if params.get("Payload") is not None:
            self.Payload = GetIndustryV1HomeMembersReqPayload()
            self.Payload._deserialize(params.get("Payload"))
        if params.get("Metadata") is not None:
            self.Metadata = ReqMetadata()
            self.Metadata._deserialize(params.get("Metadata"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespData(AbstractModel):
    """获取成员列表回包DataList

    """

    def __init__(self):
        r"""
        :param EditTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EditTime: int
        :param FeatureList: 功能列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureList: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespFeature`
        :param ID: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param IndustryType: 用户行业分类
注意：此字段可能返回 null，表示取不到有效值。
        :type IndustryType: str
        :param MemberNum: 子用户数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberNum: int
        :param ProductList: 机器人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductList: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespProduct`
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Status: 是否有效
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param TypeList: 功能列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeList: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespType`
        :param UserAccount: 用户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAccount: str
        """
        self.EditTime = None
        self.FeatureList = None
        self.ID = None
        self.IndustryType = None
        self.MemberNum = None
        self.ProductList = None
        self.Remark = None
        self.Status = None
        self.TypeList = None
        self.UserAccount = None


    def _deserialize(self, params):
        self.EditTime = params.get("EditTime")
        if params.get("FeatureList") is not None:
            self.FeatureList = GetIndustryV1HomeMembersRespFeature()
            self.FeatureList._deserialize(params.get("FeatureList"))
        self.ID = params.get("ID")
        self.IndustryType = params.get("IndustryType")
        self.MemberNum = params.get("MemberNum")
        if params.get("ProductList") is not None:
            self.ProductList = GetIndustryV1HomeMembersRespProduct()
            self.ProductList._deserialize(params.get("ProductList"))
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        if params.get("TypeList") is not None:
            self.TypeList = GetIndustryV1HomeMembersRespType()
            self.TypeList._deserialize(params.get("TypeList"))
        self.UserAccount = params.get("UserAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespFeature(AbstractModel):
    """获取成员列表接口回包Feature

    """

    def __init__(self):
        r"""
        :param FeatureName: 功能名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureName: str
        :param ID: 功能ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        """
        self.FeatureName = None
        self.ID = None


    def _deserialize(self, params):
        self.FeatureName = params.get("FeatureName")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespIndustry(AbstractModel):
    """获取成员列表回包Industry

    """

    def __init__(self):
        r"""
        :param ID: 行业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param IndustryName: 行业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IndustryName: str
        """
        self.ID = None
        self.IndustryName = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.IndustryName = params.get("IndustryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespPayload(AbstractModel):
    """获取成员列表回包Payload

    """

    def __init__(self):
        r"""
        :param AccountLevel: 用户级别
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountLevel: str
        :param DataList: 用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DataList: list of GetIndustryV1HomeMembersRespData
        :param Limit: 每页数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param Offset: 分页偏移量，从0开始
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param Total: 用户总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self.AccountLevel = None
        self.DataList = None
        self.Limit = None
        self.Offset = None
        self.Total = None


    def _deserialize(self, params):
        self.AccountLevel = params.get("AccountLevel")
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = GetIndustryV1HomeMembersRespData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespProduct(AbstractModel):
    """获取成员列表接口回包ProductList

    """

    def __init__(self):
        r"""
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param EditTime: 编辑时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EditTime: str
        :param AppKey: 机器人ID（AppKey信息）
注意：此字段可能返回 null，表示取不到有效值。
        :type AppKey: str
        :param Image: 机器人图标
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param Industry: 行业信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Industry: list of GetIndustryV1HomeMembersRespIndustry
        :param OperatorList: 操作员列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorList: str
        :param ProductName: 机器人名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param TemplateList: 模板列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateList: str
        """
        self.CreateTime = None
        self.EditTime = None
        self.AppKey = None
        self.Image = None
        self.Industry = None
        self.OperatorList = None
        self.ProductName = None
        self.Remark = None
        self.TemplateList = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.EditTime = params.get("EditTime")
        self.AppKey = params.get("AppKey")
        self.Image = params.get("Image")
        if params.get("Industry") is not None:
            self.Industry = []
            for item in params.get("Industry"):
                obj = GetIndustryV1HomeMembersRespIndustry()
                obj._deserialize(item)
                self.Industry.append(obj)
        self.OperatorList = params.get("OperatorList")
        self.ProductName = params.get("ProductName")
        self.Remark = params.get("Remark")
        self.TemplateList = params.get("TemplateList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersRespType(AbstractModel):
    """获取成员列表接口回包TypeList

    """

    def __init__(self):
        r"""
        :param Type: 类型ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param TypeName: 类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeName: str
        """
        self.Type = None
        self.TypeName = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetIndustryV1HomeMembersResponse(AbstractModel):
    """GetIndustryV1HomeMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Metadata: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.icr.v20211014.models.RspMetadata`
        :param Payload: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Payload: :class:`tencentcloud.icr.v20211014.models.GetIndustryV1HomeMembersRespPayload`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Metadata = None
        self.Payload = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Metadata") is not None:
            self.Metadata = RspMetadata()
            self.Metadata._deserialize(params.get("Metadata"))
        if params.get("Payload") is not None:
            self.Payload = GetIndustryV1HomeMembersRespPayload()
            self.Payload._deserialize(params.get("Payload"))
        self.RequestId = params.get("RequestId")


class ReqMetadata(AbstractModel):
    """请求的Metadata

    """

    def __init__(self):
        r"""
        :param ChannelID: 渠道
        :type ChannelID: str
        :param BusinessName: 无
        :type BusinessName: str
        :param GUID: 无
        :type GUID: str
        :param AppKey: 无
        :type AppKey: str
        :param LBS: 位置定位服务
        :type LBS: :class:`tencentcloud.icr.v20211014.models.ReqMetadataLBS`
        :param Vagrants: 透传字段
        :type Vagrants: list of ReqMetadataVagrant
        """
        self.ChannelID = None
        self.BusinessName = None
        self.GUID = None
        self.AppKey = None
        self.LBS = None
        self.Vagrants = None


    def _deserialize(self, params):
        self.ChannelID = params.get("ChannelID")
        self.BusinessName = params.get("BusinessName")
        self.GUID = params.get("GUID")
        self.AppKey = params.get("AppKey")
        if params.get("LBS") is not None:
            self.LBS = ReqMetadataLBS()
            self.LBS._deserialize(params.get("LBS"))
        if params.get("Vagrants") is not None:
            self.Vagrants = []
            for item in params.get("Vagrants"):
                obj = ReqMetadataVagrant()
                obj._deserialize(item)
                self.Vagrants.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReqMetadataLBS(AbstractModel):
    """请求参数的lbs

    """

    def __init__(self):
        r"""
        :param Latitude: 纬度
        :type Latitude: float
        :param Longitude: 经度
        :type Longitude: float
        """
        self.Latitude = None
        self.Longitude = None


    def _deserialize(self, params):
        self.Latitude = params.get("Latitude")
        self.Longitude = params.get("Longitude")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReqMetadataVagrant(AbstractModel):
    """请求参数Vagrant

    """

    def __init__(self):
        r"""
        :param Key: 无
        :type Key: str
        :param Value: 无
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RspMetadata(AbstractModel):
    """回包的meta data

    """

    def __init__(self):
        r"""
        :param Code: 无
        :type Code: int
        :param Message: 无
        :type Message: str
        :param SessionID: 无
        :type SessionID: str
        :param SessionDelta: 无
        :type SessionDelta: str
        """
        self.Code = None
        self.Message = None
        self.SessionID = None
        self.SessionDelta = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.SessionID = params.get("SessionID")
        self.SessionDelta = params.get("SessionDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        