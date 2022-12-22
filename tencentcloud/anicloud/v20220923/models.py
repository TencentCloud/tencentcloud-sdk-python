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


class CheckAppidExistRequest(AbstractModel):
    """CheckAppidExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param SDKAppid: 业务的appid
        :type SDKAppid: str
        :param Type: sub product code
        :type Type: str
        """
        self.SDKAppid = None
        self.Type = None


    def _deserialize(self, params):
        self.SDKAppid = params.get("SDKAppid")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAppidExistResponse(AbstractModel):
    """CheckAppidExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param Exist: appid是否存在
        :type Exist: bool
        :param HasError: 请求是否成功
        :type HasError: bool
        :param Msg: 出错消息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Exist = None
        self.HasError = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Exist = params.get("Exist")
        self.HasError = params.get("HasError")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class GoodsDetail(AbstractModel):
    """购买详情

    """

    def __init__(self):
        r"""
        :param ProductCode: 按照四层接入的产品需要传入产品标签,例如:p_cvm
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param SubProductCode: 四层定义的子产品标签,例如:sp_cvm_s1
注意：此字段可能返回 null，表示取不到有效值。
        :type SubProductCode: str
        :param Type: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: list of str
        :param GoodsNum: 资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsNum: int
        """
        self.ProductCode = None
        self.SubProductCode = None
        self.Type = None
        self.GoodsNum = None


    def _deserialize(self, params):
        self.ProductCode = params.get("ProductCode")
        self.SubProductCode = params.get("SubProductCode")
        self.Type = params.get("Type")
        self.GoodsNum = params.get("GoodsNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResourceInfoRequest(AbstractModel):
    """QueryResourceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResourceInfoResponse(AbstractModel):
    """QueryResourceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Resource: 资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.anicloud.v20220923.models.Resource`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Resource = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self.Resource = Resource()
            self.Resource._deserialize(params.get("Resource"))
        self.RequestId = params.get("RequestId")


class QueryResourceRequest(AbstractModel):
    """QueryResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 0: sdk 1:material
        :type Type: int
        :param PageNumber: 分页起始页
        :type PageNumber: int
        :param PageSize: 分页大小
        :type PageSize: int
        """
        self.Type = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryResourceResponse(AbstractModel):
    """QueryResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param Resources: 资源信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of Resource
        :param Total: 总量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Resources = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """资源信息

    """

    def __init__(self):
        r"""
        :param UIN: 资源拥有者
注意：此字段可能返回 null，表示取不到有效值。
        :type UIN: str
        :param AppId: 云平台应用ID，一般来说与uin存在一一对应的关系
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param ResourceId: 资源id，会展示到通知内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param ZoneId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param Status: 资源状态，1正常，2隔离，3销毁(如果资源已经删除或销毁，不需要返回)，4冻结/封禁
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param IsolatedTimestamp: 资源隔离时间，未隔离传"0000-00-00 00:00:00"，资源由隔离变回正常传"0000-00-00 00:00:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTimestamp: str
        :param CreateTime: 资源创建时间，用于更新新购订单的资源开始时间，按时长退费时的资源结束时间取自订单的资源结束时间，
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param PayMode: 0后付费 1预付费 2预留实例
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param Alias: 资源名称，账单中资源别名，生命周期通知中的资源名称，不返回则通知中展示为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param GoodsDetail: 购买详情
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsDetail: :class:`tencentcloud.anicloud.v20220923.models.GoodsDetail`
        :param RenewFlag: 预付费必填 ，自动续费标记，0表示默认状态(用户未设置，即初始状态即手动续费，用户开通了预付费不停服特权也会进行自动续费)， 1表示自动续费，2表示明确不自动续费(用户设置)，若业务无续费概念或无需自动续费，需要设置为0
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param ExpireTime: （仅预付费）资源到期时间，无到期概念传"0000-00-00 00:00:00"
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param Region: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param SdkAppId: sdk appid
注意：此字段可能返回 null，表示取不到有效值。
        :type SdkAppId: str
        :param AppName: app名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppName: str
        :param PackageName: app的package名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param URL: 资源链接
注意：此字段可能返回 null，表示取不到有效值。
        :type URL: str
        :param Entry: app的entry
注意：此字段可能返回 null，表示取不到有效值。
        :type Entry: str
        :param InstType: 0：sdk 1：素材
注意：此字段可能返回 null，表示取不到有效值。
        :type InstType: int
        :param Key: license的秘钥
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        """
        self.UIN = None
        self.AppId = None
        self.ResourceId = None
        self.ZoneId = None
        self.Status = None
        self.IsolatedTimestamp = None
        self.CreateTime = None
        self.PayMode = None
        self.Alias = None
        self.GoodsDetail = None
        self.RenewFlag = None
        self.ExpireTime = None
        self.Region = None
        self.SdkAppId = None
        self.AppName = None
        self.PackageName = None
        self.URL = None
        self.Entry = None
        self.InstType = None
        self.Key = None


    def _deserialize(self, params):
        self.UIN = params.get("UIN")
        self.AppId = params.get("AppId")
        self.ResourceId = params.get("ResourceId")
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        self.IsolatedTimestamp = params.get("IsolatedTimestamp")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.Alias = params.get("Alias")
        if params.get("GoodsDetail") is not None:
            self.GoodsDetail = GoodsDetail()
            self.GoodsDetail._deserialize(params.get("GoodsDetail"))
        self.RenewFlag = params.get("RenewFlag")
        self.ExpireTime = params.get("ExpireTime")
        self.Region = params.get("Region")
        self.SdkAppId = params.get("SdkAppId")
        self.AppName = params.get("AppName")
        self.PackageName = params.get("PackageName")
        self.URL = params.get("URL")
        self.Entry = params.get("Entry")
        self.InstType = params.get("InstType")
        self.Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        