# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class LiveCodeDetail(AbstractModel):
    """活动活码详情

    """

    def __init__(self):
        """
        :param LiveCodeId: 活码id
        :type LiveCodeId: int
        :param LiveCodeName: 活码名称
        :type LiveCodeName: str
        :param ShortChainAddress: 短链url
注意：此字段可能返回 null，表示取不到有效值。
        :type ShortChainAddress: str
        :param LiveCodePreview: 活码二维码
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveCodePreview: str
        :param ActivityId: 活动id
        :type ActivityId: int
        :param ActivityName: 活动名称
        :type ActivityName: str
        :param LiveCodeState: 活码状态，-1：删除，0：启用，1禁用，默认为0
        :type LiveCodeState: int
        :param LiveCodeData: 活码参数，每个活码参数都是不一样的， 这个的值对应的是字符串json类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveCodeData: str
        :param CreateTime: 创建时间戳，单位为秒
        :type CreateTime: int
        :param UpdateTime: 更新时间戳，单位为秒
        :type UpdateTime: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryActivityLiveCodeListRequest(AbstractModel):
    """QueryActivityLiveCodeList请求参数结构体

    """

    def __init__(self):
        """
        :param Cursor: 用于分页查询的游标，字符串类型，由上一次调用返回，首次调用可不填
        :type Cursor: str
        :param Limit: 返回的最大记录数，整型，最大值100，默认值50，超过最大值时取最大值
        :type Limit: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryActivityLiveCodeListResponse(AbstractModel):
    """QueryActivityLiveCodeList返回参数结构体

    """

    def __init__(self):
        """
        :param NextCursor: 分页游标，再下次请求时填写以获取之后分页的记录，如果已经没有更多的数据则返回空
注意：此字段可能返回 null，表示取不到有效值。
        :type NextCursor: str
        :param PageData: 活码列表响应参数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageData: list of LiveCodeDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        